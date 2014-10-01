# Copyright (C) 2012-2014 Peter Hatina <phatina@redhat.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

import sys
import logging
import signal
import socket
import urlparse
import threading
import collections

from lmi.shell.compat import *

from lmi.shell.LMIBaseObject import LMIWrapperBaseObject
from lmi.shell.LMIShellConfig import LMIShellConfig
from lmi.shell.LMIObjectFactory import LMIObjectFactory
from lmi.shell.LMIFormatter import LMIMethodFormatter
from lmi.shell.LMIFormatter import LMIMofFormatter
from lmi.shell.LMIReturnValue import LMIReturnValue
from lmi.shell.LMIConstantValues import LMIConstantValuesParamProp
from lmi.shell.LMIConstantValues import LMIConstantValuesMethodReturnType
from lmi.shell.LMIIndicationListener import LMIIndicationListener

from lmi.shell.LMIJob import lmi_is_job_finished
from lmi.shell.LMIJob import lmi_is_job_completed
from lmi.shell.LMIJob import lmi_is_job_terminated
from lmi.shell.LMIJob import lmi_is_job_killed
from lmi.shell.LMIJob import lmi_is_job_exception
from lmi.shell.LMIJob import JOB_NOT_FINISHED
from lmi.shell.LMIJob import JOB_FINISH_DELAYED
from lmi.shell.LMIJob import JOB_FINISH_EARLY

from lmi.shell.LMIUtil import LMIPassByRef
from lmi.shell.LMIUtil import lmi_get_use_exceptions
from lmi.shell.LMIUtil import lmi_raise_or_dump_exception
from lmi.shell.LMIUtil import lmi_transform_to_cim_param
from lmi.shell.LMIUtil import lmi_transform_to_lmi
from lmi.shell.LMIUtil import lmi_wrap_cim_class

from lmi.shell.LMIExceptions import *

logger = logging.getLogger(__name__)


class LMISignalHelperBase(object):
    """
    Base signal handling class.
    """

    @staticmethod
    def signal(signo, handler):
        """
        Calls signal() for signo, handler and returns the old signal handler.
        If signo is list of signals, the signal() call is applied for each
        signo. If handler is also list, each signal from signo will be handled
        by corresponding handler. In such case, tuple of previous handlers will
        be returned.
        """
        if isinstance(signo, (list, tuple)):
            if not isinstance(handler, (list, tuple)):
                handler = [handler] * len(signo)
            signo_handler = zip(signo, handler)
            if not signo_handler:
                return (None,) * len(signo)
            old_handlers = []
            for signal, handler in signo_handler:
                old_handlers.append(
                    LMISignalHelperBase.signal_core(signal, handler))
            return tuple(old_handlers)
        else:
            return LMISignalHelperBase.signal_core(signal, handler)

    @staticmethod
    def signal_core(signo, handler):
        """
        Wrapper method for signal.signal(). In case of ValueError, it returns
        None, old signal handler otherwise. If handler is None, default signal
        handler is set for such signal.
        """
        try:
            if handler is None:
                handler = signal.SIG_DFL
            return signal.signal(signo, handler)
        except ValueError:
            return None


class LMIMethodSignalHelper(LMISignalHelperBase):
    """
    Helper class which takes care of signal (de)registration and handling.
    """

    INTERRUPT_SIGNALS = (
        signal.SIGINT,
        signal.SIGTERM)

    def __init__(self):
        super(LMIMethodSignalHelper, self).__init__()
        self._signal_handled = False
        self._signal_prev_handlers = (signal.SIG_DFL,) * 2
        self._callbacks = collections.OrderedDict()

    def signal_attach(self):
        """
        Registers *SIGINT* and *SIGTERM* signals to local handler in which, the
        flags for each signal are modified, if such signal is caught.
        """
        def handler(sig, action):
            self.signal_handler(sig, action)

        self._signal_handled = False
        self._signal_prev_handlers = self.signal(
            self.INTERRUPT_SIGNALS, handler)

    def signal_detach(self):
        """
        Unregisters *SIGINT* and *SIGTERM* handler and removes all the attached
        callbacks.
        """
        self.signal(self.INTERRUPT_SIGNALS, self._signal_prev_handlers)

    def signal_handled(self):
        """
        :returns: True, if any of *SIGINT* or *SIGTERM* has been caught; \
            False otherwise
        """
        return self._signal_handled

    def callback_attach(self, cb_name, cb):
        """
        Registers a callback, which will be called when a *SIGINT* or *SIGTERM*
        is caught.

        :param string cb_name: callback name
        :param cb: callable object, which takes zero arguments
        """
        self._callbacks[cb_name] = cb

    def callback_detach(self, cb_name):
        """
        Removes a callback from the callback dictionary.

        :param string cb_name: callback name
        """
        self._callbacks.pop(cb_name)

    def signal_handler(self, signo, frame):
        """
        Signal handler, which is called, when *SIGINT* and *SIGTERM* are sent
        to the LMIShell.

        :param int signo: signal number
        :param frame: -- stack frame
        """
        if signo in self.INTERRUPT_SIGNALS:
            self._signal_handled = True
        [cb() for cb in self._callbacks.values()]


class LMIMethod(LMIWrapperBaseObject):
    """
    LMI wrapper class representing :py:class:`wbem.CIMMethod`.

    :param LMIConnection conn: connection object
    :param LMIInstance(Name) lmi_instance: :py:class:`.LMIInstance` or
        :py:class:`.LMIInstanceName` object, on which the method call will be
        issued
    :param string method_name: method name
    """
    # 15 seconds sleep timeout for main waiting thread
    _COND_WAIT_TIME = 15
    # Wake count of main thread, when the GetInstance is performed to check,
    # if the job object is present. Prevents infinite waiting for indication
    # delivery. Maximum waiting time, before the GetInstance for job object
    # will be called is: _COND_WAIT_TIME * _COND_WAIT_WAKE_CNT
    _COND_WAIT_WAKE_CNT = 4
    # Default tcp port, where the indications will be delivered.
    # TODO: create a configuration option for the port
    _INDICATION_DESTINATION_PORT = 10240
    # Default number retries when bind fails.
    _INDICATION_BIND_TRIES = 10
    # Job classes, which can be used for synchro method calls
    # TODO: create a configuration option for the static filters' classnames
    _INDICATION_JOB_CLASSNAMES = (
        "LMI_SELinuxJob",
        "LMI_StorageJob",
        "LMI_SoftwareInstallationJob",
        "LMI_SoftwareVerificationJob",
        "LMI_NetworkJob")
    # Default namespace where the indication subscriptions, used for
    # synchronous method calls, will be registered.
    _INDICATION_NAMESPACE = "root/interop"
    # When performing a synchronous method call and using the polling method to
    # get a job object status, the sleep time between 2 polls doubles if it is
    # less than _POLLING_ADAPT_MAX_WAITING_TIME.
    _POLLING_ADAPT_MAX_WAITING_TIME = 32

    def __init__(self, conn, lmi_instance, method_name):
        super(LMIMethod, self).__init__(conn)
        if not isinstance(lmi_instance, (
                LMIObjectFactory().LMIInstance,
                LMIObjectFactory().LMIInstanceName)):
            raise TypeError("lmi_instance must be LMIInstance(Name) type")
        self._lmi_instance = lmi_instance
        self._sync_method = False
        self._method = None
        self._method_name = method_name
        self._valuemap_parameters_list = []

        is_sync = method_name.startswith("Sync")

        if not conn.is_wsman():
            if is_sync:
                # Store the synchronous flag and trim the method name
                self._sync_method = True
                self._method_name = method_name[4:]

            # We need to have CIMClass with qualifiers. Fetch full class.
            if isinstance(self._lmi_instance, LMIObjectFactory().LMIInstance):
                # LMIInstance
                lmi_class = self._lmi_instance._lmi_class
            else:
                # LMIInstanceName
                lmi_class = lmi_wrap_cim_class(
                    self._conn,
                    self._lmi_instance.classname,
                    self._lmi_instance.namespace)
            lmi_class.fetch(True)

            self._method = lmi_class._cim_class.methods[self._method_name]

            # Store the constant values as a list. This can consume some time, if
            # computed on demand.
            self._valuemap_parameters_list = [
                k for k, v in self._method.parameters.iteritems()
                if "ValueMap" in v.qualifiers]

            # For simplicity, we add return value constants to the same list
            if "ValueMap" in self._method.qualifiers:
                self._valuemap_parameters_list.append(self._method_name)
        elif conn.is_wsman() and is_sync:
            # XXX: We can't perform synchro calls using WSMAN
            errorstr = "Can't perform synchronous method calls using WSMAN"
            raise ValueError(errorstr)

    def __return_synchro_method_call(self, job_inst, job_refresh=True):
        """
        Returns a :py:class:`.LMIReturnValue` object with Job output parameters
        set.

        :param LMIInstance job_inst: job returned from a synchronous method
            call
        :param bool job_refresh: flag, which indicates, if the ``job_inst``
            needs to be refreshed
        :returns: :py:class:`.LMIReturnValue` object with ``rval`` set to Job
            output parameters
        """
        def get_rval_errorstr(err_list):
            for err in err_list:
                if err.CIMStatusCode is not None:
                    return err.CIMStatusCode, err.Message
            # There is no CIM_Error instance with CIMStatusCode set. In such
            # case, we set rval to CIM_ERR_FAILED and for error message we use
            # the first instance from err_list.
            message = err_list[0].Message if err_list else "Failed"
            return wbem.CIM_ERR_FAILED, message

        # Adjust return value from the job object.
        if job_refresh:
            job_inst.refresh()
        rval = None
        rparams = wbem.NocaseDict()
        if job_inst.JobOutParameters is not None:
            props = job_inst.JobOutParameters.properties
            rparams = wbem.NocaseDict()
            for name, prop in props.iteritems():
                # Return just those properties of given class that are listed
                # as output parameters of particular method.
                if self._method.parameters.has_key(name) \
                        and (self._method.parameters[name].qualifiers is None \
                            or self._method.parameters[name].qualifiers.get(
                                'Out', False)):
                    rparams[name] = prop.value
                elif name == '__ReturnValue':
                    rval = prop.value
        errorstr = ""

        # Is job in exception state? If so, adjust corresponding error string
        # from job.GetError() instance
        if lmi_is_job_exception(job_inst):
            try:
                refreshed, _, errorstr = job_inst.refresh()
            except CIMError, e:
                logger.debug(
                    "Sync%s: Job instance can not be refreshed; %s" %
                    (self._method_name, str(e)))
                job_exception.value = e
            if not refreshed:
                logger.debug(
                    "Sync%s: Job instance can not be refreshed; %s" %
                    (self._method_name, errorstr))
                raise LMISynchroMethodCallError(errorstr)
            exc_rval, exc_rparams, exc_errorstr = job_inst.GetErrors()
            err_list = exc_rparams.get("errors", None)
            if not err_list:
                logger.debug(
                    "Sync%s: Can not retrieve Error instances; %s" %
                    (self._method_name, exc_errorstr))
                raise LMISynchroMethodCallError(
                    "Could not get Job error message")

            rval, errorstr = get_rval_errorstr(err_list)
            if lmi_get_use_exceptions():
                raise CIMError(rval, errorstr)

        return LMIReturnValue(rval=rval, rparams=rparams, errorstr=errorstr)

    def __handle_synchro_method_call_indication(self, job_inst):
        """
        Handles a synchronous call for asynchronous methods returning a job
        object. This method uses static filters installed by each OpenLMI
        provider, which is capable of using jobs.

        :param LMIInstance job_inst: job object returned from a synchronous
            method call
        :returns: :py:class:`.LMIReturnValue` object with ``rval`` set to 0 and
            ``rparams`` set to job's output parameters
        :raises: :py:exc:`.LMIIndicationListenerError`,
            :py:exc:`.LMISynchroMethodCallError`,
            :py:exc:`.LMISynchroMethodCallFilterError`

        **NOTE:** Static filters' names need to be in format
            "``LMI:<job_class_name>:Changed``"

        """
        def handle_job(ind, cond, job_finished, job_exception):
            """
            :py:class:`.LMIListener` handler for synchronous method call, which
            uses indication means of waiting for the job. This function is
            called, when a job changes its state.

            :param threading.Condition cond: condition object used for thread
                synchronization
            :param LMIPassByRef job_finished: used for synchronization, whether
                the job has finished
            :param LMIPassByRef job_exception: contains an exception object, if
                any exception was raised
            """
            cond.acquire()
            try:
                src_inst = ind["SourceInstance"]
                if lmi_is_job_finished(src_inst):
                    # Job has just finished
                    job_finished.value = JOB_FINISH_DELAYED
            except Exception, e:
                # Notify main thread, we are not able to work with such
                # objects.
                job_finished.value = JOB_FINISH_DELAYED
                job_exception.value = e
            finally:
                # XXX: Let's be defensive, always notify+release main thread.
                cond.notify()
                cond.release()

        cond = threading.Condition()
        job_finished = LMIPassByRef(JOB_NOT_FINISHED)
        job_exception = LMIPassByRef(None)
        # There needs to be a pattern of at least 8 "X" in a row at the end of
        # the indication_name.
        indication_name = "synchro-method-call-XXXXXXXX"

        # Start the indication listener
        listener = LMIIndicationListener(
            "0.0.0.0",
            self._INDICATION_DESTINATION_PORT,
            LMIShellConfig().cert_file,
            LMIShellConfig().key_file)
        indication_name = listener.add_handler(
            indication_name, handle_job, cond, job_finished, job_exception)
        listener.start(self._INDICATION_BIND_TRIES)
        logger.debug(
            "Choosing port for Sync%s() indications: %d" %
            (self._method_name, listener.port))

        # Search for necessary static filter
        filter_name = "LMI:%s:Changed" % job_inst.classname
        cim_filters, _, _ = self._conn.client.get_instances(
            "CIM_IndicationFilter", LMIMethod._INDICATION_NAMESPACE,
            {"Name": filter_name})
        if not cim_filters:
            listener.stop()
            errorstr = "Can not find proper CIM_IndicationFilter"
            raise LMISynchroMethodCallFilterError(errorstr)
        cim_filter = cim_filters[0]

        netloc = urlparse.urlparse(self._conn.uri).netloc
        if not netloc:
            listener.stop()
            errorstr = "Can not determine netloc from client's uri"
            raise LMISynchroMethodCallError(errorstr)
        netloc = netloc.split(":")[0]
        # NOTE: This will work only on a local area network. Complicated
        # networks may require additional configuration to make this work. See
        # LMIMethod() and PreferPolling.
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect((netloc, listener.port))
        except socket.gaierror, e:
            listener.stop()
            errorstr = "Can not determine IP address of this machine"
            raise LMISynchroMethodCallError(errorstr)
        destination = s.getsockname()[0]
        s.close()

        # Create handler object
        cim_handler_props = {
            "Name": indication_name,
            "Destination": "%s://%s:%d/CIMListener/%s" % (
                "https" if listener.uses_ssl else "http",
                destination, listener.port, indication_name),
        }
        cim_handler, _, _ = self._conn.client.create_instance(
            "CIM_IndicationHandlerCIMXML",
            LMIMethod._INDICATION_NAMESPACE,
            self._conn.hostname,
            cim_handler_props)
        if not cim_handler:
            listener.stop()
            errorstr = "Can not create CIM_IndicationHandlerCIMXML object"
            raise LMISynchroMethodCallError(errorstr)

        # Create indication subscription object
        cim_subscription_props = {
            "Filter": cim_filter.path,
            "Handler": cim_handler.path
        }
        cim_subscription, _, _ = self._conn.client.create_instance(
            "CIM_IndicationSubscription",
            LMIMethod._INDICATION_NAMESPACE,
            self._conn.hostname,
            cim_subscription_props)
        if not cim_subscription:
            self._conn.client.delete_instance(cim_handler)
            listener.stop()
            errorstr = "Can not create CIM_IndicationSubscription object"
            raise LMISynchroMethodCallError(errorstr)

        # Check, if the job is not already in finished state,
        # while we were subscribing for the indications
        job_inst.refresh()
        if lmi_is_job_finished(job_inst):
            job_finished.value = JOB_FINISH_EARLY

        # Register signal callback for SIGINT, SIGTERM with callback,
        # which awakes waiting thread for immediate return.
        signal_helper = LMIMethodSignalHelper()
        signal_helper.callback_attach(
            "indication", lambda: LMIMethod.__wake(cond))
        signal_helper.signal_attach()

        # Wait for the job to finish
        wake_cnt = 0
        cond.acquire()
        while not signal_helper.signal_handled() and \
                not job_finished.value and \
                not lmi_is_job_finished(job_inst):
            cond.wait(LMIMethod._COND_WAIT_TIME)
            wake_cnt += 1
            # XXX: threading.Condition.wait() does not inform about timeout or
            # being awaken by notify call. There is a counting to 4 sleep
            # cycles before we actually check for job status manually. This
            # number can be increased, so we rely more on indications, rather
            # then on manual polling.
            if wake_cnt >= LMIMethod._COND_WAIT_WAKE_CNT and \
                    not job_finished.value:
                wake_cnt = 0
                try:
                    refreshed, _, errorstr = job_inst.refresh()
                except CIMError, e:
                    logger.debug(
                        "Sync%s: Job instance can not be refreshed; %s" %
                        (self._method_name, str(e)))
                    job_exception.value = e
                    break
                if not refreshed:
                    logger.debug(
                        "Sync%s: Job instance can not be refreshed; %s" %
                        (self._method_name, errorstr))
                    job_exception.value = LMISynchroMethodCallError(errorstr)
                    break

        # Unregister signal handler
        signal_helper.signal_detach()
        signal_helper.callback_detach("indication")

        cond.release()

        # Cleanup
        listener.stop()
        self._conn.client.delete_instance(cim_subscription.path)
        self._conn.client.delete_instance(cim_handler.path)
        if job_exception.value:
            raise job_exception.value
        if signal_helper.signal_handled() and not job_finished.value:
            # We got SIGINT or SIGTERM, when waiting for the job, cancelling
            # the job
            logger.warn("Cancelling a job '%s'" % job_inst.Name)
            rstate = job_inst.RequestStateChange.RequestedStateValues.Terminate
            job_inst.RequestStateChange(RequestedState=rstate)
            return LMIReturnValue(rval=None)

        # Return the job return values, refresh the job_inst object, if we got
        # notified about the job finish state by indication.
        return self.__return_synchro_method_call(
            job_inst, job_finished.value == JOB_FINISH_DELAYED)

    def __handle_synchro_method_call_polling(self, job_inst):
        """
        Handles a synchronous call for asynchronous methods returning a job
        object.  This call uses polling method to wait for the job to finish.

        :param LMIInstance job_inst: job object
        :returns: :py:class:`.LMIReturnValue` object with ``rval`` set to 0 and
            ``rparams`` set to job's output parameters.
        :raises: :py:exc:`.LMISynchroMethodCallError`
        """

        # Register signal callback for SIGINT, SIGTERM with callback,
        # which awakes waiting thread for immediate return.
        signal_helper = LMIMethodSignalHelper()
        signal_helper.callback_attach(
            "polling", lambda: LMIMethod.__wake(cond))
        signal_helper.signal_attach()

        cond = threading.Condition()
        cond.acquire()

        job_exception = None

        try:
            sleep_time = 1
            while not signal_helper.signal_handled() and \
                    not lmi_is_job_finished(job_inst):
                # Sleep, a bit longer in every iteration
                cond.wait(sleep_time)
                if sleep_time < LMIMethod._POLLING_ADAPT_MAX_WAITING_TIME:
                    sleep_time *= 2
                refreshed, _, errorstr = job_inst.refresh()
                if not refreshed:
                    logger.debug(
                        "Sync%s: Job instance can not be refreshed; %s" %
                        (self._method_name, errorstr))
                    job_exception = LMISynchroMethodCallError(errorstr)
                    break
        except CIMError, e:
            logger.debug(
                "Sync%s: Job instance can not be refreshed; %s" %
                (self._method_name, str(e)))
            job_exception = LMISynchroMethodCallError(e.message)
        finally:
            cond.release()

        # Unregister signal handler and callback
        signal_helper.signal_detach()
        signal_helper.callback_detach("polling")

        if signal_helper.signal_handled() and \
                not lmi_is_job_finished(job_inst):
            # We got SIGINT or SIGTERM, when waiting for the job, cancelling
            # the job
            logger.warn("Cancelling a job '%s'" % job_inst.Name)
            rstate = job_inst.RequestStateChange.RequestedStateValues.Terminate
            job_inst.RequestStateChange(RequestedState=rstate)
            return LMIReturnValue(rval=None)

        if job_exception is not None:
            raise job_exception

        # Return the job return values. No need to refresh the job instance, we
        # already have a "fresh" one.
        return self.__return_synchro_method_call(job_inst, False)

    def __call__(self, method_args=None, **kwargs):
        """
        Perform a method call.

        Method arguments are preferably passed by dictionary (parameter :
        value). Using former means of passing arguments, by keyword arguments,
        to a method call works too.

        If performing a synchronous method call, passing PreferPolling can be
        used to select which method should be used -- either subscribing to an
        indication or polling method. This is available only, when talking to
        CIMOM via CIM-XML.

        :param dictionary method_args: method arguments
        :param dictionary kwargs: keyword method arguments (``method_args``
            preffered)

            * **RefreshInstance** (*bool*) flag, which tells the LMIShell,
              whether the instance should be refreshed after a method call.
              Default value is False.

        :returns: :py:class:`.LMIReturnValue` object with ``rval`` set to
            method's return value; ``rparams`` set to method's return
            parameters; ``errorstr`` set method's error string in case of
            failure
        :raises: :py:exc:`.LMIUnknownParameterError`,
            :py:exc:`.LMIMethodCallError`
            :py:exc:`.LMISynchroMethodCallError`

        **Usage:** :ref:`instances_methods`.
        """
        synchro_method_polling = kwargs.pop("PreferPolling", False)
        refresh_requested = kwargs.pop("RefreshInstance", False)

        # Prepare method parameters
        if method_args is None:
            method_args = {}
        method_args.update(kwargs)
        if not self._conn.is_wsman():
            for param, value in method_args.iteritems():
                if param in self._method.parameters:
                    # Cast input parameters into acceptable CIM types
                    t = self._method.parameters[param].type
                    method_args[param] = lmi_transform_to_cim_param(t, value)
                else:
                    # NOTE: maybe we could check for wbem type and not to exit
                    # prematurely
                    errorstr = "Unknown parameter '%s' supplied for method '%s'" % \
                        (param, self._method.name)
                    lmi_raise_or_dump_exception(LMIUnknownParameterError(errorstr))
                    return LMIReturnValue(rval=-1, errorstr=errorstr)
        else:
            for param, value in method_args.iteritems():
                method_args[param] = str(value)

        # Call CIM method
        client = self._conn.client
        rval, call_rparams, call_errorstr = client.call_method(
            self._lmi_instance, self._method_name, **method_args)
        rval = lmi_transform_to_lmi(self._conn, rval)

        # Do we have any return parameters? If so, transform them to LMIShells'
        # types. If it is possible, perform synchronous method call.
        if call_rparams:
            call_rparams = lmi_transform_to_lmi(self._conn, call_rparams)
            if not call_rparams:
                # NOTE: this is wrong! What should we do?
                errorstr = "Could not perform CIM -> LMI object transformation"
                lmi_raise_or_dump_exception(LMIMethodCallError(errorstr))
                return LMIReturnValue(rval=rval, errorstr=errorstr)
            # Check if we can perform synchronous method call
            job = call_rparams.get("job", None)
            can_perform_sync_call = False
            if not self._conn.is_wsman() and job and \
                    job.classname in LMIMethod._INDICATION_JOB_CLASSNAMES:
                # We can perform synchro methods only using CIM-XML
                can_perform_sync_call = True

            # Perform synchronous method call
            if self._sync_method and can_perform_sync_call:
                # We work with LMIInstance object, which simplifies the code
                # with instance refreshing and stuff.
                job_inst = call_rparams["job"].to_instance()
                # At first, try to wait for the call to finish by subscribing
                # to an indication
                handled_by_indication = False
                if not synchro_method_polling:
                    try:
                        rval, call_rparams, call_errorstr = \
                            self.__handle_synchro_method_call_indication(
                                job_inst)
                        handled_by_indication = True
                    except CIMError, e:
                        lmi_raise_or_dump_exception(e)
                        return LMIReturnValue(rval=-1, errorstr=e.args[1])
                    except LMISynchroMethodCallError, e:
                        lmi_raise_or_dump_exception(e)
                        return LMIReturnValue(rval=-1, errorstr=e.message)
                    # Fall through, try to handle the synchro call by polling
                    except LMIHandlerNamePatternError, e:
                        handled_by_indication = False
                    except LMISynchroMethodCallFilterError, e:
                        handled_by_indication = False
                    except LMIIndicationListenerError, e:
                        handled_by_indication = False
                if not handled_by_indication:
                    # Executed, when LMIListener can not be started
                    try:
                        rval, call_rparams, call_errorstr = \
                            self.__handle_synchro_method_call_polling(job_inst)
                    except LMISynchroMethodCallError, e:
                        lmi_raise_or_dump_exception(e)
                        return LMIReturnValue(rval=-1, errorstr=e.message)
                call_rparams = lmi_transform_to_lmi(self._conn, call_rparams)

        # Refresh is requested
        if refresh_requested:
            # Refresh the instance, within which the method was called
            ref_rval, _, ref_errorstr = self.__refresh_instance()
            if not ref_rval:
                errorstr = "Could not update an LMI object after a method call"
                lmi_raise_or_dump_exception(LMIMethodCallError(ref_errorstr))
                return LMIReturnValue(rval=ref_rval, errorstr=ref_errorstr)

        return LMIReturnValue(
            rval=rval, rparams=call_rparams, errorstr=call_errorstr)

    def __getattr__(self, name):
        """
        Returns either a class member, or a constant value.

        :param string name: class member, or the constant value name
        """
        if not self._conn.is_wsman() and name.endswith("Values"):
            parameter_name = name[:-6]
            if parameter_name in self._method.parameters:
                return LMIConstantValuesParamProp(
                    self._method.parameters[parameter_name])
            elif parameter_name == self._method.name:
                return LMIConstantValuesMethodReturnType(self._method)
        raise AttributeError(name)

    @staticmethod
    def __wake(cond):
        """
        Helper function used for manual :py:attr:`threading.Condition` wakeup.

        :param threading.Condition cond: condition object
        """
        cond.acquire()
        cond.notify()
        cond.release()

    def __refresh_instance(self):
        """
        Refreshes nested :py:class:`.LMIInstance`.

        **NOTE:** This method refreshes only nested :py:class:`.LMIInstance`.
        Objects of this class may also contain :py:class:`.LMIInstanceName`; in
        this case, no refreshing is performed.

        :rtype: :py:class:`.LMIReturnValue`
        """
        if not isinstance(self._lmi_instance, LMIObjectFactory().LMIInstance):
            # There is nothing to refresh here.
            return LMIReturnValue(rval=True)
        return self._lmi_instance.refresh()

    def doc(self):
        """
        Prints out pretty verbose message with documentation for the class. If
        the LMIShell is run in a interactive mode, the output will be
        redirected to a pager set by environment variable :envvar:`PAGER`. If
        there is not :envvar:`PAGER` set, less or more will be used as a
        fall-back.
        """
        if self._conn.is_wsman():
            # WSMAN doesn't support reflextion, we can't call GetClass().
            lmi_get_logger().info("WSMAN client doesn't support GetClass()")
            return

        formatter = LMIMethodFormatter(self._method)
        formatter.fancy_format(self._conn.client.interactive)

    @property
    def return_type(self):
        """
        :returns: string of the method call's return type
        """
        if self._conn.is_wsman():
            # WSMAN doesn't support reflextion, we can't call GetClass().
            return "unknown"
        return self._method.return_type

    def tomof(self):
        """
        Prints out a message with MOF representation of
        :py:class:`wbem.CIMMethod`.  If the LMIShell is run in a interactive
        mode, the output will be redirected to a pager set by environment
        variable :envvar:`PAGER`. If there is not :envvar:`PAGER` set, less or
        more will be used as a fall-back.
        """
        if self._conn.is_wsman():
            # WSMAN doesn't support reflextion, we can't call GetClass().
            lmi_get_logger().info("WSMAN client doesn't support GetClass()")
            return

        formatter = LMIMofFormatter(self._method)
        formatter.fancy_format(self._conn.client.interactive)

    def valuemap_parameters(self):
        """
        :returns: list of strings of the constant names
        """
        return self._valuemap_parameters_list

    def print_valuemap_parameters(self):
        """
        Prints out the list of strings of constant names.
        """
        for i in self._valuemap_parameters_list:
            sys.stdout.write("%s\n" % i)

    def parameters(self):
        """
        :returns: list of strings of :py:class:`wbem.CIMMethod`'s parameters
        """
        if self._conn.is_wsman():
            # WSMAN doesn't support reflextion, we can't call GetClass().
            return []

        return self._method.parameters

    def print_parameters(self):
        """
        Prints out :py:class:`wbem.CIMMethod`'s parameters.
        """
        if self._conn.is_wsman():
            # WSMAN doesn't support reflextion, we can't call GetClass().
            return

        for param, value in self._method.parameters.iteritems():
            sys.stdout.write(
                "%s %s%s\n" %
                (value.type, param, "[]" if value.is_array else ""))

    @property
    def wrapped_object(self):
        """
        :returns: wrapped :py:class:`wbem.CIMmethod` object
        """
        return self._method
