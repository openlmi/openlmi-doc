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
    Basic infrastructure for asynchronous jobs. All necessary CIM classes and
    indications are implemented here.

    .. autoclass:: JobManager
        :members:

    .. autoclass:: Job
        :members:

    .. autoclass:: LMI_ConcreteJob
        :members:

    .. autoclass:: LMI_OwningJobElement
        :members:

    .. autoclass:: LMI_AffectedJobElement
        :members:

    .. autoclass:: LMI_MethodResult
        :members:

    .. autoclass:: LMI_AssociatedJobMethodResult
        :members:
"""

from datetime import datetime, timedelta
import threading
from Queue import Queue
import pywbem
from pywbem.cim_provider2 import CIMProvider2
import socket
import traceback

from lmi.providers import cmpi_logging, parse_instance_id
from lmi.providers.IndicationManager import IndicationManager

LOG = cmpi_logging.get_logger(__name__)

@cmpi_logging.trace_function
def register_filters(job_clsname, indication_manager=None):
    """
    This function registers static indication filters at IndicationManager.
    It should be called upon provider's initialization.

    :param job_clsname: (``String``) CIM class name for asynchonous jobs.
        Will be part of filter queries.
    :param indication_manager: If not given, global instance will be obtained.
    """
    if indication_manager is None:
        ind_manager = IndicationManager.get_instance()
    filters = {}
    query_args = {
            "classname" : job_clsname,
            "prefix"    : indication_manager.nameprefix
        }
    for fltr_id, fltr_props in JobManager.IND_FILTERS.items():
        filters[fltr_id] = fltr_props.copy()
        filters[fltr_id]['Query'] = fltr_props['Query'] % query_args
    indication_manager.add_filters(job_clsname, filters)

# Too many instance attributes
# pylint: disable-msg=R0902
class Job(object):
    """
        Generic abstract class representing one CIM_ConcreteJob.
        It remembers input and output arguments, affected ManagedElements and
        owning ManagedElement (to be able to create associations to them)
        and all CIM_ConcreteJob properties.

        Due to multiple threads processing the job, each job has its own
        lock to guard its status changes. It is expected that number of jobs
        is quite low.
    """

    DEFAULT_TIME_BEFORE_REMOVAL = 60  # in seconds

    STATE_QUEUED = 1  # Job has not started yet
    STATE_RUNNING = 2  # Job is running
    STATE_FINISHED_OK = 3  # Job finished OK
    STATE_FAILED = 4  # Job finished with error
    STATE_SUSPENDED = 5  # Job is queued and suspended
    STATE_TERMINATED = 6  # Job was queued and terminated

    FINAL_STATES = [STATE_FINISHED_OK, STATE_FAILED, STATE_SUSPENDED,
            STATE_TERMINATED]

    # There is no way how to suspend/terminate running job!

    @cmpi_logging.trace_method
    def __init__(self, job_manager, job_name, input_arguments,
            method_name, affected_elements, owning_element):
        """
        Create new storage job.

        :param job_manager: (``JobManager``) Reference to ``JobManager``, which
            will manage this job.
        :param job_name: (``string``) User-friendly name of the job.
        :param input_arguments: (``dictionary param_name -> param_value``)
            Input arguments of the method, which spawned this job.
        :param method_name: (``string``) Name of the CIM method, which spawned
            this job.
        :param affected_elements: (``array of CIMInstanceName``) List of
            affected elements.  ``LMI_AffectedJobElement`` association will be
            created for them.
        :param owning_element: (``CIMInstanceName``) Reference to service, which
            spawned the job. ``LMI_OwningJobElement`` association will be
            created for it.
        """
        self.job_manager = job_manager
        self.timer_manager = job_manager.timer_manager

        # Unique ID
        self.the_id = job_manager.get_next_id()

        # User friendly name of the job
        self.job_name = job_name

        # Dictionary of input arguments, 'parameter_name' -> 'parameter_value'
        # The parameter value must be CIMProperty or something that can be
        # assigned to it.
        self.input_arguments = input_arguments

        # Dictionary of output arguments, 'parameter_name' -> 'parameter_value'
        # The parameter value must be CIMProperty or something that can be
        # assigned to it.
        self.output_arguments = None

        # Method return value, as CIMProperty or something that can be
        # assigned to it.
        self.return_value = None
        # Value of Job.ReturnValueType
        self.return_value_type = None

        # Name of the method
        self.method_name = method_name

        # Time when the job was created
        self.time_submitted = datetime.utcnow()

        # Nr. of seconds before the job is removed when the job finishes
        self.time_before_removal = self.DEFAULT_TIME_BEFORE_REMOVAL

        # If the job should be removed after completion
        self.delete_on_completion = True

        self.percent_complete = 0

        # State of the job
        self.job_state = self.STATE_QUEUED

        # Last change of job state, wall clock time
        self.clocktime_of_last_state_change = self.time_submitted

        # Duration of the job in RUNNING state (in seconds)
        self.elapsed_time = None

        # When the job started (= switched to RUNNING), wall clock time
        self.start_clocktime = None
        # When the job started (= switched to RUNNING), monotonic clock time
        self.start_monotime = None
        # When the job finished (= switched from RUNNING), monotonic clock time
        self.finish_monotime = None

        # Array of CIMInstanceNames of affected elements, so we can
        # enumerate associations to them.
        self.affected_elements = affected_elements

        # CIMInstanceName to owning element (service), so we can enumerate
        # instances.
        self.owning_element = owning_element

        # Timer used to delete the job after time_before_removal seconds
        self.timer = None

        # CIMError with result code
        self.error = None

        # internal lock to protect state changes from races
        self._lock = threading.RLock()

        self._execute = None
        self._execargs = None
        self._execkwargs = None
        self._cancel = None
        self._cancelargs = None
        self._cancelkwargs = None

        self._finished_event = threading.Event()

    @cmpi_logging.trace_method
    def set_execute_action(self, callback, *args, **kwargs):
        """
        Set callback, which will be called when the job is to be executed. It is
        expected that the callback will take some time to execute. The callback
        must change state of the job and set output parameters and error in a
        thread-safe way, i.e. by calling ``finish_method()``.

        :param callback: (``function``) Reference to callback to call.
        :param args, kwargs: All other parameters will be passed to the
            callback. It is highly recommended to add reference to the job
            to the callback.
        """
        self._execute = callback
        self._execargs = args
        self._execkwargs = kwargs

    @cmpi_logging.trace_method
    def set_cancel_action(self, callback, *args, **kwargs):
        """
        Set callbacks, which will be called when the job is to be
        cancelled. The callback must be quick, the job is already locked!

        :param callback: (``function``) Reference to callback to call.
        :param args, kwargs: All other parameters will be passed to the
            callback. It is highly recommended to add reference to the job
            to the callback.
        """
        self._cancel = callback
        self._cancelargs = args
        self._cancelkwargs = kwargs

    @cmpi_logging.trace_method
    def finish_method(self, new_state, return_value=None, return_type=None,
            output_arguments=None, error=None, affected_elements=None):
        """
        Mark the job as finished, with given return value, output parameters and
        error.
        This method is thread-safe.

        :param new_state: (``Job.STATE_* value``) Resulting state of the job.
        :param return_value: (``string``) Return value of the job, encoded
            into string. Can be None when the job does not return any value.
        :param return_type: (``Job.RetunValueType.* value``) Type of the return
            value. Can be None when the job does not return any value.
        :param output_arguments: (``dictionary param_name -> param_value``)
            Output arguments of the job. Can be None when the job does not have
            any output parameters.
        :param error: (``CIMError``) Error raised by the job. Can be None,
            when the job finished successfully.
        :param affected_elements: (``array of CIMInstanceName``) New list of
            affected elements to generate LMI_<name>JobAffectedElement
            association. If None, the old list, passed to constructor, remains
            untouched.
        """
        self.lock()
        self.return_value = return_value
        self.return_value_type = return_type
        self.output_arguments = output_arguments
        self.error = error
        if affected_elements is not None:
            self.affected_elements = affected_elements
        self.change_state(new_state, 100)
        self.unlock()
        self._finished_event.set()

    @cmpi_logging.trace_method
    def change_state(self, new_state, percent=None):
        """
        Change state of a job. (Re-)calculate various times based on the state
        change. Send indications as necessary.
        This method is thread-safe.

        :param new_state: (``Job.STATE_* value``) New state of the job.
            It can be the same as the previous state to indicate progress of
            the job.
        :param percent: (``int``)) Percent complete of the job. When None,
            this valuu will be automatically calculated (in progress = 50%,
            finished = 100%).
        """
        self.lock()

        LOG().debug("Job %s: %s changes state from %d to %d",
                self.the_id, self.job_name, self.job_state, new_state)

        # For sending indications
        prev_instance = None
        send_indication = False
        indication_ids = []

        if self.job_state != new_state:
            # Remember to send indications
            prev_instance = self.job_manager.get_job_instance(self)
            send_indication = True
            indication_ids.append(JobManager.IND_JOB_CHANGED)

            # Check if the job has just finished
            if (self.job_state not in self.FINAL_STATES
                    and new_state in self.FINAL_STATES):
                # Remember finish time
                self.finish_clocktime = datetime.utcnow()
                self.finish_monotime = self.timer_manager.now()
                # Remember job execution time.
                if self.start_monotime:
                    self.elapsed_time = self.finish_monotime \
                        - self.start_monotime
                # Send indication
                if new_state == self.STATE_FAILED:
                    indication_ids.append(JobManager.IND_JOB_FAILED)
                if new_state == self.STATE_FINISHED_OK:
                    indication_ids.append(JobManager.IND_JOB_SUCCEEDED)

            # Check if the job has just started
            if new_state == self.STATE_RUNNING:
                self.start_clocktime = datetime.utcnow()
                self.start_monotime = self.timer_manager.now()

            self.clocktime_of_last_state_change = datetime.utcnow()
            self.job_state = new_state

        if percent is None:
            # guess the percentage from status
            if new_state == self.STATE_QUEUED:
                percent = 0
            elif new_state == self.STATE_RUNNING:
                percent = 50
            else:
                percent = 100
        if self.percent_complete != percent:
            # Remember to send indications
            if not send_indication:
                self.clocktime_of_last_state_change = datetime.utcnow()
                prev_instance = self.job_manager.get_job_instance(self)
                send_indication = True
            indication_ids.append(JobManager.IND_JOB_PERCENT_UPDATED)
            self.percent_complete = percent

        if send_indication:
            current_instance = self.job_manager.get_job_instance(self)
            self.job_manager.send_modify_indications(
                    prev_instance, current_instance, indication_ids)

        # start / update the timer if necesasry
        self._restart_timer()
        self.unlock()

    @cmpi_logging.trace_method
    def _expire(self):
        """
        Callback when a Job completes and time_before_removal second passed.
        The job gets removed from its JobManager.
        """
        LOG().debug("Job %s: %s expired", self.the_id, self.job_name)

        self.job_manager.remove_job(self)

    @cmpi_logging.trace_method
    def _restart_timer(self):
        """
        Re-schedule timer for TimeBeforeRemoval because some property has
        changed.
        """
        if not self.job_state in self.FINAL_STATES:
            return

        # Stop the old timer.
        if self.timer:
            self.timer.cancel()
            self.timer = None

        # Start the new timer.
        if self.delete_on_completion:
            now = self.timer_manager.now()
            passed = now - self.finish_monotime
            timeout = self.time_before_removal - passed
            if timeout <= 0:
                # Just in case...
                self._expire()
                return

            LOG().debug("Starting timer for job %s: '%s' for %f seconds",
                    self.the_id, self.job_name, timeout)
            self.timer = self.timer_manager.create_timer(
                    "Job " + self.job_name,
                    callback=self._expire)
            self.timer.start(timeout)

    @cmpi_logging.trace_method
    def lock(self):
        """
        Lock internal mutex. Other threads will block on subsequent lock().
        The lock is recursive, i.e. can be called multiple times from
        single thread.
        """
        self._lock.acquire()

    @cmpi_logging.trace_method
    def unlock(self):
        """ Unlock internal mutex."""
        self._lock.release()

    @cmpi_logging.trace_method
    def execute(self):
        """
        Start executing the job. It calls the execute callback, set by
        ``set_execute_action()``.

        job_state must be already set to STATE_RUNNING.
        Any exception is translated to CIMError and appropriate state is set.
        """
        try:
            self._execute(*(self._execargs), **(self._execkwargs))
        except pywbem.CIMError, error:
            LOG().trace_warn("Job.execute caught an CIMError %s", str(error))
            LOG().trace_info("traceback: %s", traceback.format_exc())
            self.finish_method(Job.STATE_FAILED, error=error)
        except Exception, ex:
            LOG().trace_warn("Job.execute caught an Exception %s", str(ex))
            LOG().trace_info("traceback: %s", traceback.format_exc())
            error = pywbem.CIMError(pywbem.CIM_ERR_FAILED, str(ex))
            self.finish_method(Job.STATE_FAILED, error=error)

    @cmpi_logging.trace_method
    def cancel(self):
        """
        Cancels queued action. The action must have not been started.
        """
        self.change_state(self.STATE_TERMINATED)
        if self._cancel:
            self._cancel(*(self._cancelargs), **(self._cancelkwargs))
        self._finished_event.set()

    @cmpi_logging.trace_method
    def get_name(self):
        """
        Return CIMInstanceName of the job.

        :rtype: ``CIMInstanceName``
        """
        name = pywbem.CIMInstanceName(
                classname=self.job_manager.job_classname,
                namespace=self.job_manager.namespace,
                keybindings={
                        'InstanceID': self.get_instance_id()
        })
        return name

    @cmpi_logging.trace_method
    def get_instance_id(self, classname=None):
        """
        Return InstanceID.

        :param classname: (``string``) Optional classname to generate InstanceID
            for different class, e.g. for LMI_<name>MethodResult.
        :rtype: ``string``
        """
        if classname is None:
            classname = self.job_manager.job_classname
        return 'LMI:' + classname + ':' + str(self.the_id)

    @cmpi_logging.trace_method
    def get_pre_call(self):
        """
        Return indication that describes the pre-execution values of the
        job's invocation.

        :rtype: ``CIMInstance of CIM_InstMethodCall``
        """
        path = pywbem.CIMInstanceName(
                classname="CIM_InstMethodCall",
                keybindings={},
                host=socket.gethostname(),
                namespace=self.job_manager.namespace)
        inst = pywbem.CIMInstance(
                classname="CIM_InstMethodCall",
                path=path)
        src_instance = self._get_cim_instance()
        inst['SourceInstance'] = src_instance
        inst['SourceInstanceModelPath'] = str(src_instance.path)
        inst['MethodName'] = self.method_name
        # TODO: uncomment when Pegasus can correctly handle instances
        # of unregistered classes
        # inst['MethodParameters'] = self.get_method_params(
        #        '__MethodParameters', True, False)
        inst['PreCall'] = True
        return inst

    @cmpi_logging.trace_method
    def get_cim_error(self):
        """
        Return job error as CIMInstance of CIM_Error.
        :returns: CIMInstance of CIM_Error
        """
        path = pywbem.CIMInstanceName(
                classname="CIM_Error",
                host=socket.gethostname(),
                namespace=self.job_manager.namespace)
        err = pywbem.CIMInstance(
                classname="CIM_Error",
                path=path)
        err['CIMStatusCode'] = pywbem.Uint32(self.error[0])
        err['Message'] = self.error[1]
        return err

    @cmpi_logging.trace_method
    def get_post_call(self):
        """
        Return indication that describes the post-execution values of the
        job's invocation.

        :rtype: ``CIMInstance of CIM_InstMethodCall``
        """
        path = pywbem.CIMInstanceName(
                classname="CIM_InstMethodCall",
                keybindings={},
                host=socket.gethostname(),
                namespace=self.job_manager.namespace)
        inst = pywbem.CIMInstance(
                classname="CIM_InstMethodCall",
                path=path)

        src_instance = self._get_cim_instance()
        inst['SourceInstance'] = src_instance
        inst['SourceInstanceModelPath'] = str(src_instance.path)
        inst['MethodName'] = self.method_name
        # TODO: add input parameters too when Pegasus can correctly handle
        # instances of unregistered classes
        # TODO: also fix the class name to __MethodParameters
        params = self.get_method_params(
                '__MethodParameters_' + self.method_name, False, True)
        if params:
            inst['MethodParameters'] = params
        inst['PreCall'] = False

        if self.return_value_type is not None:
            inst['ReturnValueType'] = self.return_value_type
        if self.return_value is not None:
            inst['ReturnValue'] = str(self.return_value)
        if self.error is not None:
            err = self.get_cim_error()
            inst['Error'] = [err, ]
        return inst

    @cmpi_logging.trace_method
    def _get_cim_instance(self):
        """
        Return CIMInstance of this job.

        :rtype: CIMInstance
        """
        return self.job_manager.get_job_instance(self)

    @cmpi_logging.trace_method
    def get_method_params(self, class_name, include_input, include_output):
        """
        Create a class of given name with all input or output parameters
        of the asynchronous method. Typically used to assemble
        CIM_ConcreteJob.JobInParameters or CIM_InstMethodCall.MethodParameters
        values.

        :param class_name: (``string``) Name of the class to create.
        :param input: (``boolean``) Whether input parameters should be
            included in the returned class
        :param output: (``boolean``) Whether output parameters should be
            included in the returned class
        :rtype: CIMInstance of the created class.
        """
        path = pywbem.CIMInstanceName(
                classname=class_name,
                namespace=self.job_manager.namespace)
        inst = pywbem.CIMInstance(classname=class_name, path=path)
        if include_input and self.input_arguments:
            for (name, value) in self.input_arguments.iteritems():
                inst[name] = value
        if include_output and self.output_arguments:
            # overwrite any input parameter
            for (name, value) in self.output_arguments.iteritems():
                inst[name] = value
        return inst


    @cmpi_logging.trace_method
    def wait_for_job(self, timeout=None):
        """
        Block and wait until the job completes.

        :param timeout: (``float``) Number of seconds to wait for the job
            to complete.
        :rtype: ``bool`` - True, when the job is finished, False if the timeout
            occurred.
        """
        return self._finished_event.wait(timeout)

    # pylint: disable-msg=R0903
    class ReturnValueType(object):
        """ CIM_InstMethodCall.ReturnValueType values."""
        Boolean = pywbem.Uint16(2)
        String = pywbem.Uint16(3)
        Char16 = pywbem.Uint16(4)
        Uint8 = pywbem.Uint16(5)
        Sint8 = pywbem.Uint16(6)
        Uint16 = pywbem.Uint16(7)
        Sint16 = pywbem.Uint16(8)
        Uint32 = pywbem.Uint16(9)
        Sint32 = pywbem.Uint16(10)
        Uint64 = pywbem.Uint16(11)
        Sint64 = pywbem.Uint16(12)
        Datetime = pywbem.Uint16(13)
        Real32 = pywbem.Uint16(14)
        Real64 = pywbem.Uint16(15)
        Reference = pywbem.Uint16(16)

class JobManager(object):
    """
    Container of all queued, running or finished ``LMI_ConcreteJobs``.

    Usage:

     1. Create MOF file for these classes:

        * ``LMI_<name>Job``

        * ``LMI_<name>MethodResult``

        * ``LMI_Affected<name>JobElement``

        * ``LMI_Owning<name>JobElement``

        * ``LMI_Associated<name>JobMethodResult``

        Where ``<name>`` is prefix of your classes, for example 'Storage'

     2. During initialization, initialize ``TimerManager`` and create
        ``JobManager``.

     3. When needed. create new Job instance:

     4. Set its execute callback using ``set_execute_action()``. This callback
        will be called when the job is to be executed. It will be called in
        context of ``JobManager`` worker thread!

     5. Optionally, set cancel callback using ``set_execute_action()``. This
        callback will be called when the job is still queued and is cancelled by
        application. This callback will be called in context of CIMOM callback
        and should be quick!

     6. Enqueue the job using ``JobManager.add_job()`` method.

     7. When your execute callback is called, you can optionally call
        ``job.change_state()`` to update percentage of completion.

     8. When your execute callback is finished, don't forget to set method
        result using ``job.finish_method()``.

    * ``JobManager`` automatically sends all job-related indications.
    * ``Job`` automatically tracks various timestamps.
    * By default, the job automatically disappears after 60 seconds after it
      finishes. Application may set ``DeleteOnCompletion`` and
      ``TimeBeforeRemoval`` properties of ``LMI_<name>Job`` to override this
      timeout.
    """

    COMMAND_STOP = 1

    IND_JOB_PERCENT_UPDATED = "PercentUpdated"
    IND_JOB_SUCCEEDED = "Succeeded"
    IND_JOB_FAILED = "Failed"
    IND_JOB_CHANGED = "Changed"
    IND_JOB_CREATED = "Created"

    IND_FILTERS = {
        IND_JOB_PERCENT_UPDATED: {
            "Query" : "SELECT * FROM LMI_%(prefix)sInstModification WHERE "
                "SourceInstance ISA %(classname)s AND "
                "SourceInstance.CIM_ConcreteJob::PercentComplete <> "
                "PreviousInstance.CIM_ConcreteJob::PercentComplete",
            "Description" : "Modification of Percentage Complete for a "
                "Concrete Job.",
        },
        IND_JOB_SUCCEEDED: {
            "Query" : "SELECT * FROM LMI_%(prefix)sInstModification WHERE "
                "SourceInstance ISA %(classname)s AND "
                "SourceInstance.CIM_ConcreteJob::JobState = 7",
            "Description": "Modification of Job State for a "
                "Concrete Job to 'Complete'.",
        },
        IND_JOB_FAILED: {
            "Query" : "SELECT * FROM LMI_%(prefix)sInstModification WHERE "
                "SourceInstance ISA %(classname)s AND "
                "SourceInstance.CIM_ConcreteJob::JobState = 10",
            "Description": "Modification of Job State for a "
                "Concrete Job to 'Exception'.",
        },
        IND_JOB_CHANGED: {
            "Query" : "SELECT * FROM LMI_%(prefix)sInstModification WHERE "
                "SourceInstance ISA %(classname)s AND "
                "SourceInstance.CIM_ConcreteJob::JobState <> "
                "PreviousInstance.CIM_ConcreteJob::JobState",
            "Description": "Modification of Job State for a ConcreteJob.",
        },
        IND_JOB_CREATED: {
            "Query" : "SELECT * FROM LMI_%(prefix)sInstCreation WHERE "
                "SourceInstance ISA %(classname)s",
            "Description": "Creation of a ConcreteJob.",
        },
    }

    @cmpi_logging.trace_method
    def __init__(self, name, namespace, indication_manager, timer_manager):
        """
        Initialize new Manager. It automatically registers all job-related
        filters to indication_manager and starts a worker thread.

        :param name: (``string``) String with classname infix. For example
            'Storage' for ``LMI_StorageJob``, ``LMI_StorageJobMethodResult``
            etc.
        :param namespace: (``string``) Namespace of all providers.
        :param indication_manager: (``IndicationManager``): a manager where
            indications and filters should be added.
        :param timer_manager: (``TimerManager``): Timer manager instance.
        """
        # List of all jobs. Dictionary job_id -> Job.
        self.jobs = {}
        # Queue of jobs scheduled to execute.
        self.queue = Queue()
        # Last created job_id.
        self.last_instance_id = 0
        # Classname infix.
        self.name = name
        # CIMProvider2 instances for job classes.
        self.providers = {}
        self.namespace = namespace
        self.indication_manager = indication_manager
        self.timer_manager = timer_manager

        # Start the worker thread (don't forget to register it at CIMOM)
        self.worker = threading.Thread(target=self._worker_main)
        self.worker.daemon = False
        self.worker.start()

        # Various classnames for job-related classes, with correct infixes.
        self.job_classname = 'LMI_' + self.name + 'Job'
        self.method_result_classname = "LMI_" + self.name + "MethodResult"
        self.affected_classname = "LMI_Affected" + self.name + "JobElement"
        self.owning_classname = "LMI_Owning" + self.name + "JobElement"
        self.associated_result_classname = ('LMI_Associated' + self.name
                + 'JobMethodResult')
        self.indication_filter_classname = ('LMI_' + self.name
                + 'JobIndicationFilter')
        self.job_provider = None
        self._add_indication_filters()

    @cmpi_logging.trace_method
    def _add_indication_filters(self):
        """
        Add all job-related ``IndicationFilters`` to indication manager.
        """
        register_filters(self.job_classname, self.indication_manager)

    @cmpi_logging.trace_method
    def get_providers(self):
        """
        Get dictionary of providers for these classes:

        * ``LMI_<name>Job``
        * ``LMI_<name>MethodResult``
        * ``LMI_Affected<name>JobElement``
        * ``LMI_Owning<name>JobElement``
        * ``LMI_Associated<name>JobMethodResult``

        :rtype: dictionary class_name -> CIMProvider2
        """

        if not self.providers:
            job_provider = LMI_ConcreteJob(self.job_classname, job_manager=self)
            self.providers[self.job_classname] = job_provider
            self.job_provider = job_provider

            provider = LMI_MethodResult(
                    self.method_result_classname, job_manager=self)
            self.providers[self.method_result_classname] = provider

            provider = LMI_AffectedJobElement(
                    self.affected_classname, job_manager=self)
            self.providers[self.affected_classname] = provider

            provider = LMI_OwningJobElement(
                    self.owning_classname, job_manager=self)
            self.providers[self.owning_classname] = provider

            provider = LMI_AssociatedJobMethodResult(
                    self.owning_classname, job_manager=self)
            self.providers[self.associated_result_classname] = provider

        return self.providers

    @cmpi_logging.trace_method
    def add_job(self, job):
        """
        Enqueue new job. Send indication when needed.

        :param job: (``Job``) A job to enqueue.
        """
        LOG().debug("Job %s: '%s' enqueued", job.the_id, job.job_name)

        self.jobs[job.the_id] = job
        self.queue.put(job)
        # send indication
        if self.indication_manager.is_subscribed(
                        self.job_classname, self.IND_JOB_CREATED):
            job_instance = self.get_job_instance(job)
            self.indication_manager.send_instcreation(
                    job_instance, self.IND_JOB_CREATED)

    def send_modify_indications(self, prev_instance, current_instance,
            indication_ids):
        """
        Send InstModification. This is helper method called by ``Job`` when
        needed.

        :param prev_instance: Instance of ``LMI_<name>Job`` before it was
            modified.
        :param current_instance: Instance of ``LMI_<name>Job`` after it was
            modified.
        """
        for _id in indication_ids:
            self.indication_manager.send_instmodification(prev_instance,
                    current_instance, _id)

    @cmpi_logging.trace_method
    def remove_job(self, job):
        """
        Remove existing job. Note that jobs are removed automatically after a
        timeout, providers should not call this method directly.

        :param job: (``Job``) Job to remove.
        """
        LOG().debug("Job %s: '%s' removed from queue.",
                job.the_id, job.job_name)
        del self.jobs[job.the_id]
        # The job may still be in the queue!
        # There is no way, how to remove it, it will be skipped by the
        # worker thread.

    @cmpi_logging.trace_method
    def get_job_for_instance_id(self, instance_id, classname=None):
        """
        Return Job for given InstanceID or None when no such Job exist.

        :param instance_id: (``string``) InstanceID value to parse.
        :param classname: (``string``) Optional classname to parse the
            InstanceID (e.g. when parsing InstanceID of
            ``LMI_<name>MethodResult``).
        :rtype: ``Job``
        """
        if classname is None:
            classname = self.job_classname
        the_id = parse_instance_id(instance_id, classname)
        if not the_id.isdigit():
            return None
        return self.jobs.get(the_id, None)

    @cmpi_logging.trace_method
    def _worker_main(self):
        """
        This is the main loop of the job queue. It just processes enqueued
        jobs and never ends.
        """
        LOG().info("Started Job thread.")
        while True:
            command = self.queue.get()
            if isinstance(command, Job):
                # we need to protect from changes between checking state and
                # setting new state
                job = command
                job.lock()
                if job.job_state == Job.STATE_QUEUED:
                    # the job was not cancelled
                    job.change_state(Job.STATE_RUNNING)
                    job.unlock()
                    LOG().info("Starting job %s: '%s'",
                            job.the_id, job.job_name)

                    job.execute()
                    if job.error:
                        LOG().warn("Job %s: '%s' finished with error: %s",
                                job.the_id, job.job_name, str(job.error))
                    else:
                        LOG().info("Job %s: '%s' finished OK",
                                job.the_id, job.job_name)
                else:
                    # just skip suspended and terminated jobs
                    job.unlock()

            elif isinstance(command, int):
                self.queue.task_done()
                break

            self.queue.task_done()

        LOG().info("Stopped Job thread.")

    @cmpi_logging.trace_method
    def get_next_id(self):
        """
        Return next unused job id.

        :rtype: string
        """
        self.last_instance_id += 1
        return str(self.last_instance_id)

    @cmpi_logging.trace_method
    def get_job_instance(self, job):
        """
        Return CIMInstance for given job.

        :param job: (``Job``)
        :rtype: ``CIMInstance``
        """
        path = pywbem.CIMInstanceName(
                classname=self.job_classname,
                keybindings={'InstanceID': job.get_instance_id()},
                host=socket.gethostname(),
                namespace=self.namespace)
        inst = pywbem.CIMInstance(classname=self.job_classname, path=path)
        inst['InstanceID'] = job.get_instance_id()
        return self.job_provider.get_instance(None, inst)

    @cmpi_logging.trace_method
    def shutdown(self, timeout=1):
        """
        Stop the thread. If a job is running, it may leave the job process
        (mkfs, resize2fs, ...) and the worker thread (waiting for the process to
        finish) still running.

        JobManager still needs Indication Manager and TimeManager working at
        this point!

        :param timeout: Nr. of seconds to wait for the current job. Afterwards
            the thread is abandoned, leaving the process still running.
        """
        # Empty the queue, we don't want the worker to proceed with any other
        # queued job.
        while not self.queue.empty():
            self.queue.get(False)
            self.queue.task_done()

        self.queue.put(self.COMMAND_STOP)
        self.worker.join(timeout)

        # Cancel all running/suspended/queued jobs.
        # This will send indications.
        for job in self.jobs.itervalues():
            if job.job_state in (Job.STATE_QUEUED, Job.STATE_SUSPENDED,
                    Job.STATE_RUNNING):
                job.cancel()

        if self.worker.isAlive():
            # There is no way, how to stop the thread in Python, so abandon it.
            self.worker.daemon = True
            self.indication_manager = None
            self.timer_manager = None

    def can_shutdown(self):
        """
        Return True, if there is no running Job.
        """
        return self.queue.empty()


class LMI_ConcreteJob(CIMProvider2):
    """
    Provider of LMI_ConcreteJob class or its subclass.
    """
    @cmpi_logging.trace_method
    def __init__(self, classname, job_manager):
        self.classname = classname
        self.job_manager = job_manager

    @cmpi_logging.trace_method
    def enum_instances(self, env, model, keys_only):
        """
        Provider implementation of EnumerateInstances intrinsic method.
        """
        model.path.update({'InstanceID': None})
        for job in self.job_manager.jobs.values():
            model['InstanceID'] = job.get_instance_id()
            if keys_only:
                yield model
            else:
                yield self.get_instance(env, model, job)

    @cmpi_logging.trace_method
    def get_job_states(self, job):
        """
        Return JobState and OperationalStatus property values.

        :param job: (``int``) Job.STATE_* value.
        :rtype: tuple ``(JobState, OperationalStatus)`` values.
        """
        if job.job_state == Job.STATE_QUEUED:
            jobstate = self.Values.JobState.New
            opstate = [self.Values.OperationalStatus.Dormant]
        elif job.job_state == Job.STATE_RUNNING:
            jobstate = self.Values.JobState.Running
            opstate = [self.Values.OperationalStatus.OK]
        elif job.job_state == Job.STATE_FINISHED_OK:
            jobstate = self.Values.JobState.Completed
            opstate = [self.Values.OperationalStatus.OK,
                    self.Values.OperationalStatus.Completed]
        elif job.job_state == Job.STATE_SUSPENDED:
            jobstate = self.Values.JobState.Suspended
            opstate = [self.Values.OperationalStatus.OK]
        elif job.job_state == Job.STATE_FAILED:
            jobstate = self.Values.JobState.Exception
            opstate = [self.Values.OperationalStatus.Error,
                    self.Values.OperationalStatus.Completed]
        elif job.job_state == Job.STATE_TERMINATED:
            jobstate = self.Values.JobState.Terminated
            opstate = [self.Values.OperationalStatus.Stopped]
        return jobstate, opstate

    @cmpi_logging.trace_method
    # pylint: disable-msg=W0221
    def get_instance(self, env, model, job=None):
        """
        Provider implementation of GetInstance intrinsic method.
        """
        if not job:
            instance_id = model['InstanceID']
            job = self.job_manager.get_job_for_instance_id(instance_id)
        if not job:
            raise pywbem.CIMError(pywbem.CIM_ERR_NOT_FOUND,
                    "Job not found.")

        model['DeleteOnCompletion'] = job.delete_on_completion
        model['Name'] = job.job_name

        # convert seconds to timedelta
        seconds = job.time_before_removal
        if seconds:
            delta = timedelta(seconds=seconds)
            model['TimeBeforeRemoval'] = pywbem.CIMDateTime(delta)
        else:
            model['TimeBeforeRemoval'] = pywbem.CIMProperty(
                    name='TimeBeforeRemoval',
                    value=None,
                    type='datetime')

        if job.clocktime_of_last_state_change:
            model['TimeOfLastStateChange'] = pywbem.CIMDateTime(
                    job.clocktime_of_last_state_change)
        else:
            model['TimeOfLastStateChange'] = pywbem.CIMProperty(
                    name='TimeOfLastStateChange',
                    value=None,
                    type='datetime')

        if job.elapsed_time:
            elapsed_time = timedelta(seconds=job.elapsed_time)
            model['ElapsedTime'] = pywbem.CIMDateTime(elapsed_time)
        else:
            model['ElapsedTime'] = pywbem.CIMProperty(
                    name='ElapsedTime',
                    value=None,
                    type='datetime')

        model['Description'] = job.job_name
        model['LocalOrUtcTime'] = self.Values.LocalOrUtcTime.UTC_Time
        model['PercentComplete'] = pywbem.Uint16(job.percent_complete)
        if job.start_clocktime:
            model['StartTime'] = pywbem.CIMDateTime(job.start_clocktime)
        else:
            model['StartTime'] = pywbem.CIMProperty(
                    name='StartTime',
                    value=None,
                    type='datetime')

        # TODO: uncomment when Pegasus can correctly handle instances
        # of unregistered classes
        # if job.input_arguments:
        #    model['JobInParameters'] = job.get_method_params(
        #            "__JobInParameters", True, False)

        if job.job_state in Job.FINAL_STATES:
            # assemble output parameters with return value
            # TODO: use __JobOutParameters when Pegasus can create instances
            # of unregistered classes
            outparams = job.get_method_params(
                    "__MethodParameters_" + job.method_name + "_Result",
                    False,
                    True)
            if job.return_value is not None:
                outparams['__ReturnValue'] = job.return_value
            model['JobOutParameters'] = outparams

        model['TimeSubmitted'] = pywbem.CIMDateTime(job.time_submitted)
        # set correct state
        jobstate, opstate = self.get_job_states(job)
        model['JobState'] = jobstate
        model['OperationalStatus'] = opstate
        return model

    @cmpi_logging.trace_method
    def set_instance(self, env, instance, modify_existing):
        """Return a newly created or modified instance.

        :param env: Provider Environment (pycimmb.ProviderEnvironment)
        :param instance: The new pywbem.CIMInstance.  If modifying an existing
            instance, the properties on this instance have been filtered by
            the PropertyList from the request.
        :param modify_existing: True if ModifyInstance, False if CreateInstance

        Return the new instance.  The keys must be set on the new instance.
        """
        if not modify_existing:
            raise pywbem.CIMError(pywbem.CIM_ERR_NOT_SUPPORTED,
                    "Creation of Job instances is not supported.")

        job = self.job_manager.get_job_for_instance_id(instance['InstanceID'])
        if not job:
            raise pywbem.CIMError(pywbem.CIM_ERR_NOT_FOUND,
                    "Job not found.")

        try:
            job.lock()
            restart_timer = False

            for (key, value) in instance.iteritems():
                if value is None:
                    continue
                if key == 'DeleteOnCompletion':
                    job.delete_on_completion = value
                    restart_timer = True
                elif key == 'TimeBeforeRemoval':
                    job.time_before_removal = value.total_seconds()
                    restart_timer = True
                elif key == 'JobRunTimes':
                    if value != 1:
                        raise pywbem.CIMError(pywbem.CIM_ERR_NOT_SUPPORTED,
                                "JobRunTimes property is not supported.")
                elif key == 'LocalOrUtcTime':
                    if value != self.Values.LocalOrUtcTime.UTC_Time:
                        raise pywbem.CIMError(pywbem.CIM_ERR_NOT_SUPPORTED,
                                "Setting of LocalOrUtcTime property is not"
                                " supported.")
                else:
                    raise pywbem.CIMError(pywbem.CIM_ERR_NOT_SUPPORTED,
                            "Setting of %s property is not supported." % (key,))

            if restart_timer:
                job._restart_timer()
        finally:
            job.unlock()
        return instance

    @cmpi_logging.trace_method
    def delete_instance(self, env, instance_name):
        """Delete an instance.

        :param env: Provider Environment (pycimmb.ProviderEnvironment)
        :param instance_name: A pywbem.CIMInstanceName specifying the instance
            to delete.
        """
        job = self.job_manager.get_job_for_instance_id(
                instance_name['InstanceID'])
        if not job:
            raise pywbem.CIMError(pywbem.CIM_ERR_NOT_FOUND,
                    "Job not found.")
        if not job.job_status in Job.FINAL_STATES:
            raise pywbem.CIMError(pywbem.CIM_ERR_FAILED,
                    "Job has not finished.")

        self.job_manager.remove_job(job)

    @cmpi_logging.trace_method
    def cim_method_geterrors(self, env, object_name):
        """Implements LMI_StorageJob.GetErrors()

        If JobState is "Completed" and Operational Status is "Completed"
        then no instance of CIM_Error is returned.

        If JobState is "Exception" then GetErrors may return intances of
        CIM_Error related to the execution of the procedure or method invoked by
        the job.

        If Operatational Status is not "OK" or "Completed" then
        GetErrors may return CIM_Error instances related to the running of
        the job.

        :param env: -- Provider Environment (pycimmb.ProviderEnvironment)
        :param object_name: -- A pywbem.CIMInstanceName or pywbem.CIMCLassName
            specifying the object on which the method GetErrors()
            should be invoked.

        Output parameters:

        * Errors -- (type pywbem.CIMInstance(classname='CIM_Error', ...))
            If the OperationalStatus on the Job is not "OK", then this
            method will return one or more CIM Error instance(s).
            Otherwise, when the Job is "OK", null is returned.
        """
        job = self.job_manager.get_job_for_instance_id(
                object_name['InstanceID'])
        if not job:
            raise pywbem.CIMError(pywbem.CIM_ERR_NOT_FOUND,
                    "Job not found.")

        if job.error is None:
            errors = []
        else:
            err = job.get_cim_error()
            errors = [err, ]
        out_params = [
                pywbem.CIMParameter(
                        name='Errors',
                        value=errors,
                        type='instance',
                        is_array=True,
                        array_size=len(errors))
        ]
        rval = self.Values.GetErrors.Success

        return (rval, out_params)

    @cmpi_logging.trace_method
    def cim_method_requeststatechange(self, env, object_name,
                                      param_requestedstate=None,
                                      param_timeoutperiod=None):
        """Implements LMI_StorageJob.RequestStateChange()

        Requests that the state of the job be changed to the value
        specified in the RequestedState parameter. Invoking the
        RequestStateChange method multiple times could result in earlier
        requests being overwritten or lost.

        If 0 is returned, then the
        task completed successfully. Any other return code indicates an
        error condition.

        :param env: Provider Environment (pycimmb.ProviderEnvironment)
        :param object_name:  A pywbem.CIMInstanceName or pywbem.CIMCLassName
            specifying the object on which the method RequestStateChange()
            should be invoked.
        :param param_requestedstate:  The input parameter RequestedState (type pywbem.Uint16 self.Values.RequestStateChange.RequestedState)
            RequestStateChange changes the state of a job. The possible
            values are as follows: Start (2) changes the state to
            \'Running\'. Suspend (3) stops the job temporarily. The
            intention is to subsequently restart the job with \'Start\'.
            It might be possible to enter the \'Service\' state while
            suspended. (This is job-specific.) Terminate (4) stops the
            job cleanly, saving data, preserving the state, and shutting
            down all underlying processes in an orderly manner. Kill (5)
            terminates the job immediately with no requirement to save
            data or preserve the state. Service (6) puts the job into a
            vendor-specific service state. It might be possible to restart
            the job.

        :param param_timeoutperiod: --  The input parameter TimeoutPeriod (type pywbem.CIMDateTime)
            A timeout period that specifies the maximum amount of time that
            the client expects the transition to the new state to take.
            The interval format must be used to specify the TimeoutPeriod.
            A value of 0 or a null parameter indicates that the client has
            no time requirements for the transition. If this property
            does not contain 0 or null and the implementation does not
            support this parameter, a return code of \'Use Of Timeout
            Parameter Not Supported\' must be returned.
        """
        job = self.job_manager.get_job_for_instance_id(
                object_name['InstanceID'])
        if not job:
            raise pywbem.CIMError(pywbem.CIM_ERR_NOT_FOUND,
                    "Job not found.")

        try:
            job.lock()
            states = self.Values.RequestStateChange.RequestedState
            retcodes = self.Values.RequestStateChange
            if param_requestedstate == states.Suspend:
                if job.job_state != Job.STATE_QUEUED:
                    # Can suspend only queued jobs
                    rval = retcodes.Invalid_State_Transition
                else:
                    job.change_state(Job.STATE_SUSPENDED)
                    rval = retcodes.Completed_with_No_Error

            elif param_requestedstate == states.Terminate:
                if job.job_state not in (Job.STATE_QUEUED, Job.STATE_SUSPENDED):
                    # Can terminate only queued or suspended jobs
                    rval = retcodes.Invalid_State_Transition
                else:
                    job.cancel()
                    rval = retcodes.Completed_with_No_Error

            elif param_requestedstate == states.Start:
                if job.job_state != Job.STATE_SUSPENDED:
                    # Can start only suspended jobs
                    rval = retcodes.Invalid_State_Transition
                else:
                    job.change_state(Job.STATE_QUEUED)
                    # Enqueue the job again, it may be already processed
                    # (we might get the job in the queue twice, but
                    # we have only one worker thread so it won't collide).
                    self.job_manager.add_job(job)
                    rval = retcodes.Completed_with_No_Error

            else:
                rval = retcodes.Invalid_State_Transition
        finally:
            job.unlock()
        return (rval, [])

    @cmpi_logging.trace_method
    def cim_method_killjob(self, env, object_name,
                           param_deleteonkill=None):
        """Implements LMI_StorageJob.KillJob() """
        raise pywbem.CIMError(pywbem.CIM_ERR_NOT_SUPPORTED)

    @cmpi_logging.trace_method
    def cim_method_geterror(self, env, object_name):
        """Implements LMI_StorageJob.GetError()

        GetError is deprecated because Error should be an array,not a
        scalar.

        When the job is executing or has terminated without
        error, then this method returns no CIM_Error instance. However, if
        the job has failed because of some internal problem or because the
        job has been terminated by a client, then a CIM_Error instance is
        returned.

        :param env: Provider Environment (pycimmb.ProviderEnvironment)
        :param object_name: A pywbem.CIMInstanceName or pywbem.CIMCLassName
            specifying the object on which the method GetError()
            should be invoked.

        Output parameters:

        * Error -- (``pywbem.CIMInstance(classname='CIM_Error', ...)``)
          If the OperationalStatus on the Job is not "OK", then this
          method will return a CIM Error instance. Otherwise, when the
          Job is "OK", null is returned.
        """
        job = self.job_manager.get_job_for_instance_id(
                object_name['InstanceID'])
        if not job:
            raise pywbem.CIMError(pywbem.CIM_ERR_NOT_FOUND,
                    "Job not found.")

        if job.error is None:
            error = pywbem.CIMParameter(
                        name='error',
                        value=None,
                        type='instance',
                        is_array=False)
        else:
            err = job.get_cim_error()
            error = pywbem.CIMParameter(
                        name='error',
                        value=err,
                        type='instance')
        rval = self.Values.GetError.Success
        return (rval, [error])

    class Values(object):
        class JobState(object):
            New = pywbem.Uint16(2)
            Starting = pywbem.Uint16(3)
            Running = pywbem.Uint16(4)
            Suspended = pywbem.Uint16(5)
            Shutting_Down = pywbem.Uint16(6)
            Completed = pywbem.Uint16(7)
            Terminated = pywbem.Uint16(8)
            Killed = pywbem.Uint16(9)
            Exception = pywbem.Uint16(10)
            Service = pywbem.Uint16(11)
            Query_Pending = pywbem.Uint16(12)
            # DMTF_Reserved = 13..32767
            # Vendor_Reserved = 32768..65535

        class LocalOrUtcTime(object):
            Local_Time = pywbem.Uint16(1)
            UTC_Time = pywbem.Uint16(2)

        class OperationalStatus(object):
            Unknown = pywbem.Uint16(0)
            Other = pywbem.Uint16(1)
            OK = pywbem.Uint16(2)
            Degraded = pywbem.Uint16(3)
            Stressed = pywbem.Uint16(4)
            Predictive_Failure = pywbem.Uint16(5)
            Error = pywbem.Uint16(6)
            Non_Recoverable_Error = pywbem.Uint16(7)
            Starting = pywbem.Uint16(8)
            Stopping = pywbem.Uint16(9)
            Stopped = pywbem.Uint16(10)
            In_Service = pywbem.Uint16(11)
            No_Contact = pywbem.Uint16(12)
            Lost_Communication = pywbem.Uint16(13)
            Aborted = pywbem.Uint16(14)
            Dormant = pywbem.Uint16(15)
            Supporting_Entity_in_Error = pywbem.Uint16(16)
            Completed = pywbem.Uint16(17)
            Power_Mode = pywbem.Uint16(18)
            Relocating = pywbem.Uint16(19)
            # DMTF_Reserved = ..
            # Vendor_Reserved = 0x8000..

        class GetErrors(object):
            Success = pywbem.Uint32(0)
            Not_Supported = pywbem.Uint32(1)
            Unspecified_Error = pywbem.Uint32(2)
            Timeout = pywbem.Uint32(3)
            Failed = pywbem.Uint32(4)
            Invalid_Parameter = pywbem.Uint32(5)
            Access_Denied = pywbem.Uint32(6)
            # DMTF_Reserved = ..
            # Vendor_Specific = 32768..65535

        class GetError(object):
            Success = pywbem.Uint32(0)
            Not_Supported = pywbem.Uint32(1)
            Unspecified_Error = pywbem.Uint32(2)
            Timeout = pywbem.Uint32(3)
            Failed = pywbem.Uint32(4)
            Invalid_Parameter = pywbem.Uint32(5)
            Access_Denied = pywbem.Uint32(6)
            # DMTF_Reserved = ..
            # Vendor_Specific = 32768..65535

        class RequestStateChange(object):
            Completed_with_No_Error = pywbem.Uint32(0)
            Not_Supported = pywbem.Uint32(1)
            Unknown_Unspecified_Error = pywbem.Uint32(2)
            Can_NOT_complete_within_Timeout_Period = pywbem.Uint32(3)
            Failed = pywbem.Uint32(4)
            Invalid_Parameter = pywbem.Uint32(5)
            In_Use = pywbem.Uint32(6)
            # DMTF_Reserved = ..
            Method_Parameters_Checked___Transition_Started = pywbem.Uint32(4096)
            Invalid_State_Transition = pywbem.Uint32(4097)
            Use_of_Timeout_Parameter_Not_Supported = pywbem.Uint32(4098)
            Busy = pywbem.Uint32(4099)
            # Method_Reserved = 4100..32767
            # Vendor_Specific = 32768..65535
            class RequestedState(object):
                Start = pywbem.Uint16(2)
                Suspend = pywbem.Uint16(3)
                Terminate = pywbem.Uint16(4)
                Kill = pywbem.Uint16(5)
                Service = pywbem.Uint16(6)
                # DMTF_Reserved = 7..32767
                # Vendor_Reserved = 32768..65535

class LMI_OwningJobElement(CIMProvider2):
    """ Instrumentation of LMI_OwningJobElement class and its subclasses."""

    @cmpi_logging.trace_method
    def __init__(self, classname, job_manager):
        self.classname = classname
        self.job_manager = job_manager

    @cmpi_logging.trace_method
    def get_instance(self, env, model):
        """Return an instance."""
        instance_id = model['OwnedElement']['InstanceID']
        job = self.job_manager.get_job_for_instance_id(instance_id)
        if not job:
            raise pywbem.CIMError(pywbem.CIM_ERR_NOT_FOUND,
                    "OwnedElement not found.")

        if job.owning_element != model['OwningElement']:
            raise pywbem.CIMError(pywbem.CIM_ERR_NOT_FOUND,
                    "OwnedElement is not associated to OwningElement.")
        return model

    @cmpi_logging.trace_method
    def enum_instances(self, env, model, keys_only):
        """Enumerate instances."""
        model.path.update({'OwnedElement': None, 'OwningElement': None})
        for job in self.job_manager.jobs.values():
            if job.owning_element:
                model['OwnedElement'] = job.get_name()
                model['OwningElement'] = job.owning_element
                yield model

    @cmpi_logging.trace_method
    def references(self, env, object_name, model, result_class_name, role,
                   result_role, keys_only):
        """Instrument Associations."""
        ch = env.get_cimom_handle()
        if ch.is_subclass(object_name.namespace,
                  sub=object_name.classname,
                  super='CIM_ManagedElement') or \
            ch.is_subclass(object_name.namespace,
                  sub=object_name.classname,
                  super=self.job_manager.job_classname):
            return self.simple_refs(env, object_name, model,
                          result_class_name, role, result_role, keys_only)

class LMI_AffectedJobElement(CIMProvider2):
    """ Instrumentation of LMI_AffectedJobElement class and its subclasses."""

    @cmpi_logging.trace_method
    def __init__(self, classname, job_manager):
        self.classname = classname
        self.job_manager = job_manager

    @cmpi_logging.trace_method
    def get_instance(self, env, model):
        """Return an instance."""
        instance_id = model['AffectingElement']['InstanceID']
        job = self.job_manager.get_job_for_instance_id(instance_id)
        if not job:
            raise pywbem.CIMError(pywbem.CIM_ERR_NOT_FOUND,
                    "AffectingElement not found.")

        if job.affected_elements is None:
            raise pywbem.CIMError(pywbem.CIM_ERR_NOT_FOUND,
                    "The AffectingElement has no AffectedElement.")
        if model['AffectedElement'] not in job.affected_elements:
            raise pywbem.CIMError(pywbem.CIM_ERR_NOT_FOUND,
                    "AffectedElement is not associated to AffectingElement.")
        model['ElementEffects'] = [self.Values.ElementEffects.Unknown, ]
        return model

    @cmpi_logging.trace_method
    def enum_instances(self, env, model, keys_only):
        """Enumerate instances."""
        model.path.update({'AffectingElement': None, 'AffectedElement': None})
        for job in self.job_manager.jobs.values():
            if job.affected_elements is None:
                continue
            for element in job.affected_elements:
                model['AffectingElement'] = job.get_name()
                model['AffectedElement'] = element
                if keys_only:
                    yield model
                else:
                    yield self.get_instance(env, model)

    @cmpi_logging.trace_method
    def references(self, env, object_name, model, result_class_name, role,
                   result_role, keys_only):
        """Instrument Associations."""
        ch = env.get_cimom_handle()
        if ch.is_subclass(object_name.namespace,
                  sub=object_name.classname,
                  super='CIM_ManagedElement') or \
            ch.is_subclass(object_name.namespace,
                  sub=object_name.classname,
                  super=self.job_manager.job_classname):
            return self.simple_refs(env, object_name, model,
                          result_class_name, role, result_role, keys_only)

    class Values(object):
        class ElementEffects(object):
            Unknown = pywbem.Uint16(0)
            Other = pywbem.Uint16(1)
            Exclusive_Use = pywbem.Uint16(2)
            Performance_Impact = pywbem.Uint16(3)
            Element_Integrity = pywbem.Uint16(4)
            Create = pywbem.Uint16(5)


class LMI_MethodResult(CIMProvider2):
    """Instrumentation of LMI_MethodResult class and its subclasses."""

    @cmpi_logging.trace_method
    def __init__(self, classname, job_manager):
        self.classname = classname
        self.job_manager = job_manager

    @cmpi_logging.trace_method
    # pylint: disable-msg=W0221
    def get_instance(self, env, model, job=None):
        """Return an instance."""
        if not job:
            instance_id = model['InstanceID']
            job = self.job_manager.get_job_for_instance_id(
                    instance_id, self.classname)
        if not job:
            raise pywbem.CIMError(pywbem.CIM_ERR_NOT_FOUND,
                    "Job not found.")

        model['Description'] = job.job_name
        if job.job_state in Job.FINAL_STATES:
            model['PostCallIndication'] = pywbem.CIMProperty(
                    name='PostCallIndication',
                    value=job.get_post_call())
        else:
            model['PostCallIndication'] = pywbem.CIMProperty(
                    name='PostCallIndication',
                    type='instance',
                    value=None)
        model['PreCallIndication'] = pywbem.CIMProperty(
                    name='PreCallIndication',
                    value=job.get_pre_call())
        return model

    @cmpi_logging.trace_method
    def enum_instances(self, env, model, keys_only):
        """Enumerate instances."""
        model.path.update({'InstanceID': None})
        for job in self.job_manager.jobs.values():
            model['InstanceID'] = job.get_instance_id(
                    classname=self.classname)
            if keys_only:
                yield model
            else:
                yield self.get_instance(env, model, job)

class LMI_AssociatedJobMethodResult(CIMProvider2):
    """
        Instrumentation of LMI_AssociatedJobMethodResult class and its
        subclasses.
    """

    @cmpi_logging.trace_method
    def __init__(self, classname, job_manager):
        self.classname = classname
        self.job_manager = job_manager

    @cmpi_logging.trace_method
    def get_instance(self, env, model):
        """Return an instance."""
        instance_id = model['Job']['InstanceID']
        job = self.job_manager.get_job_for_instance_id(instance_id)
        if not job:
            raise pywbem.CIMError(pywbem.CIM_ERR_NOT_FOUND,
                    "Job not found.")

        expected_result_id = job.get_instance_id(
                classname=self.job_manager.method_result_classname)
        if model['JobParameters']['InstanceID'] != expected_result_id:
            raise pywbem.CIMError(pywbem.CIM_ERR_NOT_FOUND,
                    "Job is not associated to JobParameters.")
        return model

    @cmpi_logging.trace_method
    def enum_instances(self, env, model, keys_only):
        """Enumerate instances."""
        model.path.update({'JobParameters': None, 'Job': None})
        for job in self.job_manager.jobs.values():
            if job.owning_element:
                model['Job'] = job.get_name()
                model['JobParameters'] = pywbem.CIMInstanceName(
                    classname=self.job_manager.method_result_classname,
                    namespace=self.job_manager.namespace,
                    keybindings={
                        'InstanceID': job.get_instance_id(
                            classname=self.job_manager.method_result_classname)
                })
                yield model

    @cmpi_logging.trace_method
    def references(self, env, object_name, model, result_class_name, role,
                   result_role, keys_only):
        """Instrument Associations."""
        ch = env.get_cimom_handle()
        if ch.is_subclass(object_name.namespace,
                  sub=object_name.classname,
                  super=self.job_manager.method_result_classname) or \
            ch.is_subclass(object_name.namespace,
                  sub=object_name.classname,
                  super=self.job_manager.job_classname):
            return self.simple_refs(env, object_name, model,
                          result_class_name, role, result_role, keys_only)

