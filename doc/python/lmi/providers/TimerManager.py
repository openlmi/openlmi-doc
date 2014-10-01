# Copyright (C) 2013-2014 Red Hat, Inc.  All rights reserved.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#
# Authors: Jan Safranek <jsafrane@redhat.com>
# -*- coding: utf-8 -*-
"""
Module with functionality to create timers, which can be used in CMPI providers.

Default python threading.Timer is not suitable, because it creates thread
for each timer, which is inefficient. In addition, each such thread would need
to be registered at CIMOM to enable logging in timer callbacks.

Usage:

1. Initialize the TimerManager when your provider initializes!
Otherwise you may encounter weird exceptions.

2. When any provider needs timer, create it using Time.create_timer() to create
Timer instance.

3. Call Timer.start() to start the timer. It will call registered callback
when the timer expires. The callback is called in context of TimerManager
thread, which has enabled logging to CIMOM, i.e. the callback can log as usual.

4. (optionally) cancel the timer before expiration using Timer.cancel().
However, this does not guarantee that the timer callback won't be called -
it may be already being scheduled / called.

.. autoclass:: TimerManager
        :members:

.. autoclass:: Timer
        :members:

.. autoclass:: MonotonicClock
        :members:
"""

import ctypes
import threading
import Queue

from lmi.base import singletonmixin
from lmi.providers import cmpi_logging

LOG = cmpi_logging.get_logger(__name__)

class TimerException(Exception):
    pass

class MonotonicClock(object):
    """
    Monotonic clock, represented by clock_gettime() and CLOCK_MONOTONIC.
    This clock is not influenced by NTP or administrator setting time or date.
    """
    CLOCK_MONOTONIC = ctypes.c_int(1)

    class timespec(ctypes.Structure):
        _fields_ = [
                ("tv_sec", ctypes.c_long),
                ("tv_nsec", ctypes.c_long)]

    def __init__(self):
        libc = ctypes.CDLL("librt.so.1")
        self._clock_gettime = libc.clock_gettime

    def now(self):
        """
        Return current time, i.e. float representing seconds with precision up
        to nanoseconds (depends on glibc). The actual value of current time is
        meaningless, it can be used only to measure time differences.

        :returns: ``float`` with current time in seconds.
        """
        t = MonotonicClock.timespec(0, 0)
        ret = self._clock_gettime(self.CLOCK_MONOTONIC, ctypes.pointer(t))

        if ret < 0:
            raise TimerException("Cannot get clock time, clock_gettime() failed.")
        return t.tv_sec + t.tv_nsec * 10 ** (-9)

class Timer(object):
    """
    A class representing a timer. A timer has a timeout and after the timeout,
    given callback is called and the timer is deleted.
    """

    @cmpi_logging.trace_method
    def __init__(self, timer_manager, name, callback=None, *args, **kwargs):
        """
        Create a timer. If specified, given callback is registered.
        The callback is called with *args and **kwargs.

        :param timer_manager: (``TimerManager)`` Instance of the timer manager
            which will manage the timer.
        :param name: (``string``) Name of the timer, used for logging.
        :param callback: (``function``) Callback to call when the timer expires.
        :param *args, **kwargs: Parameters of the callback.
        """
        self._mgr = timer_manager
        self._name = name
        self._callback = callback
        self._args = args
        self._kwargs = kwargs

        LOG().trace_info("Timer: Timer %s created", name)

    @cmpi_logging.trace_method
    def set_callback(self, callback, *args, **kwargs):
        """
        Set callback to call when the timer expires.

        :param callback: (``function``) Callback to call when the timer expires.
        :param *args, **kwargs: Parameters of the callback.
        """
        self._callback = callback
        self._args = args
        self._kwargs = kwargs

    @cmpi_logging.trace_method
    def start(self, timeout):
        """
        Start the timer with given timeout. After the timeout, the registered
        callback will be called.

        :param timeout: (``float``) Timeout in seconds.
        """

        self._timeout = timeout
        now = self._mgr.now()
        self._end_time = now + timeout
        LOG().trace_info("Timer: Timer %s started at %f for %f seconds",
                self._name, now, self._timeout)
        self._mgr._add_timer(self)

    @cmpi_logging.trace_method
    def cancel(self):
        """
        Cancel the timer. This method does not guarantee that the callback won't
        be called, the timer might be calling the callback right now,
        """
        LOG().trace_info("Timer: Timer %s cancelled", self._name)
        self._mgr._remove_timer(self)

    @cmpi_logging.trace_method
    def _expired(self, now):
        """
        Returns True, if the timer is expired.

        :param now: (``float``) Current time, as returned by MonotonicClock.now().
        :returns: (``boolean``) ``True``, if the timer is expired.
        """
        if self._end_time <= now:
            LOG().trace_info("Timer: Timer %s has expired", self._name)
            return True
        return False

    @cmpi_logging.trace_method
    def _expire(self):
        """
        Called when the timer expired. It calls the callback.
        """
        LOG().trace_info("Timer: Calling callback for timer %s", self._name)
        self._callback(*self._args, **self._kwargs)

class TimerManager(singletonmixin.Singleton):
    """
    Manages set of timers.

    Python standard Timer class creates a thread for

    each timer, which is inefficient. This class uses only one thread, which
    is registered at CIMOM, i.e. it can log as usual.

    This class is singleton, use TimerManager.get_instance() to get the
    instance.

    Still, the singleton needs to be initialized with ProviderEnvironment to
    enable logging in the timer thread. Use TimerManager.get_instance(env) in
    you provider initialization.
    """

    # Commands to the timer thread
    COMMAND_STOP = 1
    COMMAND_RESCHEDULE = 2

    @cmpi_logging.trace_method
    def __init__(self, env=None):
        """
        Initialize new thread manager.

        :param env: (``ProviderEnvironment``) Environment to use for logging.
        """
        self._clock = MonotonicClock()
        self._lock = threading.RLock()
        self._queue = Queue.Queue()

        # Array of timers. Assumption: nr. of timers is relatively small,
        # i.e. hundreds at the worst.
        self._timers = []

        new_broker = None
        if env:
            broker = env.get_cimom_handle()
            new_broker = broker.PrepareAttachThread()

        self._timer_thread = threading.Thread(
                target=self._timer_loop, args=(new_broker,))
        self._timer_thread.daemon = False
        self._timer_thread.start()

    def create_timer(self, name, callback=None, *args, **kwargs):
        """
        Create new timer. If specified, given callback is registered.
        The callback is called with *args and **kwargs.

        :param name: (``string``) Name of the timer, used for logging.
        :param callback: (``function``) Callback to call when the timer expires.
        :param *args, **kwargs: Parameters of the callback.
        """
        return Timer(self, name, callback, *args, **kwargs)

    def _timer_loop(self, broker):
        """
        TimerManager thread main loop. It waits for timeout of all timers
        and calls their callbacks.

        :param broker: (``BrokerCIMOMHandle``) CIM broker handle, used for
                logging.
        """
        if broker:
            broker.AttachThread()
        LOG().info("Started Timer thread.")
        while True:
            self._handle_expired()
            timeout = self._find_timeout()
            if timeout != 0:
                # Wait for the timeout or any change in timers.
                try:
                    command = self._queue.get(timeout=timeout)
                    self._queue.task_done()
                    if command == self.COMMAND_STOP:
                        break  # stop the thread
                    # process COMMAND_RESCHEDULE in next loop
                except Queue.Empty:
                    # Timeout has happened, ignore the exception.
                    pass
        LOG().info("Stopped Timer thread.")

    @cmpi_logging.trace_method
    def _handle_expired(self):
        """
        Finds all expired timers, calls their callback and removes them from
        list of timers.
        """

        # Get list of expired timers.
        with self._lock:
            now = self.now()
            LOG().trace_info("Timer: Checking for expired, now=%f.", now)
            expired = [t for t in self._timers if t._expired(now)]

        # Call the callbacks (unlocked!).
        for t in expired:
            t._expire()

        # Remove the timers (locked).
        with self._lock:
            for t in expired:
                try:
                    LOG().trace_info("Timer: Removing %s", t._name)
                    self._timers.remove(t)
                except ValueError:
                    # The timer has already been removed.
                    pass

    @cmpi_logging.trace_method
    def _find_timeout(self):
        """
        Return nearest timeout, in seconds (as float, i.e. subsecond timeout
        is possible). If no timer is scheduled, None is returned.
        If there are expired timers, 0 is returned.

        :returns: Positive ``float``: Nearest timeout.
        :returns: ``0``: Some timer has expired.
        :returns: ``None``: No timer is scheduled.
        """
        with self._lock:
            if not self._timers:
                LOG().trace_info("Timer: No timers scheduled, waiting forever.")
                return None
            closest = min(self._timers, key=lambda timer: timer._end_time)
            now = self.now()
            timeout = closest._end_time - now
            if timeout > 0:
                LOG().trace_info("Timer: Waiting for %f seconds, now=%f.",
                        timeout, now)
                return timeout
            LOG().trace_info(
                    "Timer: Some timer has already expired, no waiting.")
            return 0

    @cmpi_logging.trace_method
    def _add_timer(self, timer):
        """
        Adds timer to list of timers. The timer must be started, i.e. its
        timeout must be nozero!
        This is internal method called by Timer.start().

        :param timer: (``Timer``) Timer to add.
        """
        with self._lock:
            self._timers.append(timer)
        # Wake up the timer manager thread.
        self._queue.put(self.COMMAND_RESCHEDULE)
        LOG().trace_info("Timer: Timer %s added", timer._name)

    @cmpi_logging.trace_method
    def _remove_timer(self, timer):
        """
        Remove timer from list of timers.
        This is internal method called by Timer.cancel().
        :param timer: (``Timer``) Timer to remove.
        """
        with self._lock:
            try:
                self._timers.remove(timer)
            except ValueError:
                pass
        # Wake up the timer manager thread.
        self._queue.put(self.COMMAND_RESCHEDULE)
        LOG().trace_info("Timer: Timer %s removed", timer._name)

    def now(self):
        """
        Return current time, not influenced by NTP or admin setting date or
        time. The actual value of current time is meaningless, it can be used
        only to measure time differences.

        :returns: ``float`` Current time, in seconds.
        """
        return self._clock.now()

    @cmpi_logging.trace_method
    def shutdown(self):
        """
        Stop the thread. This method blocks until the thread is safely
        destroyed.
        """
        self._queue.put(self.COMMAND_STOP)
        self._timer_thread.join()

if __name__ == "__main__":
    LOG = cmpi_logging.CMPILogger("")
    import time

    class Env(object):
        def AttachThread(self):
            pass
        def PrepareAttachThread(self):
            return self
        def get_cimom_handle(self):
            return self

    clock = MonotonicClock()

    start = clock.now()
    time.sleep(0.5)
    print "Clock 0.5:", clock.now() - start

    time.sleep(0.5)
    print "Clock 1:", clock.now() - start

    mgr = TimerManager.get_instance(Env())

    def callback(msg):
        if callback.first:
            t = mgr.create_timer("internal 0.5")
            t.set_callback(callback, "internal 0.5")
            t.start(0.5)
            callback.first = False

        print clock.now(), msg

    callback.first = True

    t1 = mgr.create_timer("one second")
    t1.set_callback(callback, "1")
    t1.start(1)
    t2 = mgr.create_timer("two seconds")
    t2.set_callback(callback, "2")
    t2.start(2)
    t22 = mgr.create_timer("two seconds 2")
    t22.set_callback(callback, "2 again")
    t22.start(2)
    t15 = mgr.create_timer("one+half seconds")
    t15.set_callback(callback, "1.5")
    t15.start(1.5)

    time.sleep(4)

    mgr.stop_thread()
