# Copyright (C) 2012-2014 Red Hat, Inc.  All rights reserved.
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
# Authors: Michal Minar <miminar@redhat.com>
# -*- coding: utf-8 -*-
"""
    .. autoclass:: IndicationManager
        :members:
"""

import pywbem
from Queue import Queue
import re
import socket
import threading

from lmi.base import singletonmixin
from lmi.providers import cmpi_logging

RE_FILTER_NAME = re.compile(r'^(?P<prefix>lmi:'
    r'(?P<class_name>[a-z0-9_]+):)(?P<filter_id>.*)$', re.IGNORECASE)

FILTER_DEFAULTS = {
        "SourceNamespace"  : "root/cimv2",
        "SourceNamespaces" : ["root/cimv2"],
        "QueryLanguage"    : "CIM:CQL"
}

LOG = cmpi_logging.get_logger(__name__)

@cmpi_logging.trace_function
def enumerate_namespaces(ch):
    """
    Return tuple ``([CIM_Namespace instance, ...], ns_interop)``. Where
    first item is a list of object paths of all namespaces in broker and
    the second is a name of namespace, where this information can be found.

    :param ch: CIMOM handle.
    """
    nsclasses = ["CIM_Namespace", "__Namespace"]
    namespaces = ['root/cimv2', 'root/PG_InterOp', 'Interop',
            'interop', 'root', 'root/interop']
    nspaths = []
    ns = None
    for cls in nsclasses:
        for ns in namespaces:
            try:
                nspaths = [nm for nm in ch.EnumerateInstanceNames(ns, cls)]
                if nspaths:
                    break
            except pywbem.CIMError as exc:
                if exc[0] in (
                        pywbem.CIM_ERR_INVALID_NAMESPACE,
                        pywbem.CIM_ERR_NOT_SUPPORTED,
                        pywbem.CIM_ERR_INVALID_CLASS):
                    pass
                if exc[0] == pywbem.CIM_ERR_FAILED:
                    LOG().error("EnumerateInstanceNames failed for %s:%s: %s",
                            ns, cls, str(exc))
                else:
                    raise
        if nspaths:
            break
    if not nspaths:
        LOG().error("failed to enumerate namespaces")
        ns = None
    return (nspaths, ns)

@cmpi_logging.trace_function
def find_ns_interop(ch):
    """
    Return name of interop namespace, where ``CIM_IndicationFilter``
    class reside.

    :param ch: CIMOM handle.
    """
    _, ns_interop = enumerate_namespaces(ch)
    return ns_interop

def make_filter_name(class_name, fltr_id):
    """
    Return value for ``CIM_IndicationFilter.Name`` property.
    """
    return "LMI:%s:%s" % (class_name, fltr_id)

def parse_filter_name(name):
    """
    Return tuple ``(class_name, filter_id)``.

    :param name: (``string``) Value of cim filter's *Name* property.
    """
    match = RE_FILTER_NAME.match(name)
    if not match:
        raise ValueError('Could not parse filter name: "%s"' % name)
    return (match.group("class_name"), match.group("filter_id"))

@cmpi_logging.trace_function
def make_indication_filter_path(class_name, fltr_id, ns_interop):
    """
    Return CIM_IndicationFilter instance path for given filter id.

    :param class_name: (``string``) *Scoped class* name.
    :param fltr_id: (``string``) Filter name.
    :param ns_interop: (``string``) Interop namespace.
    """
    for arg in ('class_name', 'fltr_id', 'ns_interop'):
        if not isinstance(locals()[arg], basestring):
            raise TypeError("%s must be basestring" % arg)
    cop = pywbem.CIMInstanceName("CIM_IndicationFilter",
            namespace=ns_interop)
    cop['CreationClassName'] = 'CIM_IndicationFilter'
    cop['SystemCreationClassName'] = 'CIM_ComputerSystem'
    cop['SystemName'] = socket.gethostname()
    cop['Name'] = make_filter_name(class_name, fltr_id)
    return cop

@cmpi_logging.trace_function
def remove_cimom_filter(ch, fltr_path):
    """
    Deletes instance of CIM_IndicationFilter installed at broker with all
    referencing subscriptions.

    Returns list of subscription instace names, that were deleted.

    :param ch: CIMOM handle.
    :param fltr_path: (``CIMInstanceName``) Path of ``CIM_IndicationFilter`` to
        remove.
    """
    if not isinstance(fltr_path, pywbem.CIMInstanceName):
        raise TypeError("fltr_path must be a CIMInstanceName")

    referents = []
    for ref in ch.AssociatorNames(fltr_path,
            role="Filter",
            resultRole="Handler",
            resultClass="CIM_IndicationSubscription"):
        ch.DeleteInstance(ref)
        referents.append(ref)
    ch.DeleteInstance(fltr_path)
    LOG().debug('removed indication filter "%s" with %d referents',
            fltr_path["Name"], len(referents))
    return referents

class IndicationManager(singletonmixin.Singleton):
    """
    Using ``IndicationManager`` class
    providers can send indications without bothering with handling of
    indication subscriptions.

    Usage:

    1. Subclass CIM_InstCreation and CIM_InstModification.

    2. In your initialization routine, create one ``IndicationManager``
    instance. E.g. one for whole ``LMI_Storage`` may is enough. Like
    this::

        indication_manager = \
                IndicationManager.get_instance(env, "Storage", "root/cimv2")

    3. Call ``indication_manager.add_filters()`` with all filters your
    providers support for particular CIM class. This method can be called
    multiple times.
    For example::

      filters = {
          "JobPercentUpdated": {
              "Query" : "SELECT * FROM CIM_InstModification WHERE"
                " SourceInstance ISA LMI_StorageJob AND"
                " SourceInstance.CIM_ConcreteJob::PercentComplete <>"
                " PreviousInstance.CIM_ConcreteJob::PercentComplete",
              "Description" : "Modification of Percentage Complete for"
                " a Concrete Job.",
          },
          "JobSucceeded": {
              "Query" : "SELECT * FROM CIM_InstModification WHERE"
                " SourceInstance ISA LMI_StorageJob AND"
                " SourceInstance.CIM_ConcreteJob::JobState = "
                " CIM_ConcreteJob.JobState#'Completed'",
              "Description": "Modification of Operational Status for"
                " a Concrete Job to 'Complete' and 'OK'.",
          },
          #... other indications
      }
      instance_manager.add_filters("LMI_StorageJob", filters)

    First argument is a name of class to which indications apply. We'll call
    it *Scoping class*.

    4. In your provider module, implement indication functions like this::

        def authorize_filter(env, fltr, ns, classes, owner):
            indication_manager.authorize_filter(env, fltr, ns, classes, owner)

        def activate_filter (env, fltr, ns, classes, first_activation):
            indication_manager.activate_filter(env, fltr, ns, classes,
                first_activation)

        def deactivate_filter(env, fltr, ns, classes, last_activation):
            indication_manager.deactivate_filter(env, fltr, ns, classes,
                last_activation)

        def enable_indications(env):
            indication_manager.enable_indications(env)

        def disable_indications(env):
            indication_manager.disable_indications(env)

    From now on, the ``IndicationManager`` will track all subscribed filters.
    You can query the ``indication_manager.is_subscribed()`` before you create
    and send an indication. Use ``indication_manager.send_indication()``
    to send your indications.

    Only static (=preconfigured, read-only) indication filters are
    supported.

    For user to use these preconfigured filters, they need to be installed
    at broker as instances of ``CIM_IndicationFilter``. But since they can
    not be guarded against removel by accident, this object provides a way
    to reinstall them. But using this is not recomended, since it can upset
    users. See :ref:`_update_context-label`.

    The supported filters must be passed to add_filters method. The filters
    are passed as dictionary ``'filter_id' -> {dictionary 'IndicationFilter
    property' -> 'value'}``. There must be at least ``Query`` property in
    each filter, CQL is assumed.

    This helper automatically tracks which filters are subscribed. Provider
    can query ``is_subscribed()`` to check, if filter with given
    ``filter_id`` is subscribed before generating indications.

    The CMPI interface to send indications is complicated -
    when an indication is send from CIMOM callback (e.g. ``get_instance``),
    it must use current ``env`` parameter of the callback and it would be
    tedious to pass it to ``IndicationManager`` each time. Therefore
    ``IndicationManager`` creates its own thread, registers it at CIMOM
    using ``PrepareAttachThread``/``AttachThread``.

    As side-effect, indication can be sent from any thread, there is no
    need to call ``PrepareAttachThread``/``AttachThread``.
    """
    SEVERITY_INFO = pywbem.Uint16(2)  # CIM_Indication.PerceivedSeverity

    COMMAND_STOP = 1  # Command to the IndicationManager thread to stop.

    @cmpi_logging.trace_method
    def __init__(self, env, nameprefix, namespace, ns_interop=None,
            queue=None):
        """
        Create new ``IndicationManager``. Usually only one instance
        is necessary for one provider process.

        :param env: (``ProviderEnvironment``) Provider enviroment, taken
            from CIMOM callback (e.g. ``get_providers()``).
        :param nameprefix: (``string``) Prefix of your ``CIM_InstCreation``
            and ``CIM_InstModification`` subclasses, e.g. 'Storage' for
            ``LMI_StorageInstCreation``.
        :param namespace: (``string``) Namespace, which will be set to
            outgoing indications instances.
        :param ns_interop: (``string``) Namespace, where filters and
            subscriptions are stored.
        :param queue: Optional custom input queue with the same interface as
            ``Queue.Queue``.
        """

        # { class_name :
        #   { filter_id : filter_properties
        #   , ... }
        # }
        self._filters = pywbem.NocaseDict()
        self._enabled = False
        # { (class_name, filter_id), ... }
        self._subscribed_filters = set()
        self._nameprefix = nameprefix
        self._namespace = namespace
        self._ns_interop = ns_interop
        self._access_lock = threading.RLock()
        self._env = env

        if queue is None:
            queue = Queue()
        self._queue = queue
        # prepare indication thread
        ch = env.get_cimom_handle()
        new_broker = ch.PrepareAttachThread()
        self._indication_sender = threading.Thread(
                target=self._send_indications_loop, args=(new_broker,))
        self._indication_sender.daemon = False
        self._indication_sender.start()

    @property
    def enabled(self):
        """
        Return a boolean saying, whether indication sending is enabled.
        """
        with self._access_lock:
            return self.enabled

    @property
    def namespace(self):
        """
        Return namespace of outgoing indication instances.
        """
        return self._namespace

    @property
    def nameprefix(self):
        """
        Return prefix of indication class names.
        """
        return self._nameprefix

    @property
    def ns_interop(self):
        """
        Return interop namespace name.
        """
        with self._access_lock:
            if self._ns_interop is None:
                ch = self._env.get_cimom_handle()
                self._ns_interop = find_ns_interop(ch)
                LOG().info('found interop namespace: %s', self._ns_interop)
            return self._ns_interop

    @property
    def instcreation_classname(self):
        """
        Return whole class name of InstCreation indication.
        """
        return "LMI_" + self._nameprefix + "InstCreation"

    @property
    def instmodification_classname(self):
        """
        Return whole class name of InstModification indication.
        """
        return "LMI_" + self._nameprefix + "InstModification"

    @property
    def instdeletetion_classname(self):
        """
        Return whole class name of InstDeletion indication.
        """
        return "LMI_" + self._nameprefix + "InstDeletion"

    @cmpi_logging.trace_method
    def _get_filter_inst(self, class_name, fltr_id):
        """
        Return instance of CIM_IndicationFilter registered in CIMOM if any.

        :param class_name: (``string``) *Scoping class* name.
        :param fltr_id: (``string``) Indication name.
        """
        ch = self._env.get_cimom_handle()
        cop = make_indication_filter_path(class_name, fltr_id, self.ns_interop)
        try:
            return ch.GetInstance(cop)
        except pywbem.CIMError as exc:
            if exc.args[0] == pywbem.CIM_ERR_NOT_FOUND:
                return None
            raise

    @cmpi_logging.trace_method
    def _ensure_cimom_has_filter(self, class_name, fltr_id):
        """
        Ensures, that cimom has ``fltr_id`` filter registered as instance.
        If it has, but the query differs it is recreated at broker.

        :param class_name: (``string``) *Scoping class* name.
        :param fltr_id: (``string``) Indication name.
        """
        inst = self._get_filter_inst(class_name, fltr_id)
        ch = self._env.get_cimom_handle()
        installed = inst is not None
        referents = []
        if installed:
            for prop_name, val in self._filters[class_name][fltr_id].items():
                if inst[prop_name] != val:
                    LOG().info("filter \"%s\" is installed, but its property"
                            " \"%s\" has outdated value; removing...",
                            fltr_id, prop_name)
                    referents = remove_cimom_filter(ch, inst.path)
                    installed = False
        if not installed:
            if inst is not None:
                path = inst.path
            else:
                path = make_indication_filter_path(class_name, fltr_id,
                        self.ns_interop)
            inst = pywbem.CIMInstance(path.classname, path=path)
            kwargs = FILTER_DEFAULTS.copy()
            for key, val in path.keybindings.items():
                kwargs[key] = val
            kwargs.update(self._filters[class_name][fltr_id])
            inst.update(kwargs)
            try:
                inst = ch.CreateInstance(inst)
                LOG().info("filter \"%s\" installed", fltr_id)
            except pywbem.CIMError:
                LOG().exception("failed to install indication filter \"%s\"",
                        fltr_id)
            if referents:
                LOG().debug('reinstalling %d filter subscriptions',
                        len(referents))
                for ref in referents:
                    ch.CreateInstance(ref)
        return inst

    @cmpi_logging.trace_method
    def _get_matching_filter(self, query):
        """
        Try to find matching filter properties in local ``_filters`` storage
        and return it. ``None`` is returned if not found.

        Return a tuple ``(class_name, filter_id, filter_properties)``.

        :param query: (``string``) Is filter query.
        """
        if not isinstance(query, basestring):
            raise TypeError("query must be a string")
        for clsname, fltrs in self._filters.iteritems():
            for fltr_id, props in fltrs.iteritems():
                if query == props["Query"]:
                    return (clsname, fltr_id, props)
        return None

    @cmpi_logging.trace_method
    def ensure_filters_installed(self, class_name=None, fltr_id=None):
        """
        This function checks for existence of filters at broker. Filters
        must be registered with this instance before the check can be done.
        Without arguments all registered filters will be checked.

        :param class_name: (``string``) Name of *Scoped class* that reduces
            searched filters.
        :param fltr_id: (``string``) Indication name reducing filters that
            will be checked.
        """
        cls_to_check = self._filters.keys()
        if class_name is not None:
            cls_to_check = [class_name]
        filters_to_check = list(
                    (c, f)
                for c in cls_to_check
                for f in self._filters[c].keys()
                if fltr_id is None or fltr_id == f)
        with self._access_lock:
            try:
                for clsname, fltr_id in filters_to_check:
                    self._ensure_cimom_has_filter(clsname, fltr_id)
                LOG().debug('filters installed')
                return True
            except pywbem.CIMError as exc:
                if exc.args[0] == pywbem.CIM_ERR_ACCESS_DENIED:
                    LOG().error("filters could not be checked"
                            " for presence due to invalid context")
                    return False
                raise

    @cmpi_logging.trace_method
    def update_context(self, env):
        """
        .. _update_context-label

        When ``IndicationManager`` is initialized upon provider initialization,
        the conxet given does not contain any user credentials that are
        needed for communication with broker. In order to check for filter's
        existence at broker, this method needs to be called first with
        context containing user's credentials.

        This needs to be called only once.

        **Note** that if you don't plan to check for filter's presence at
        broker at runtime, you are not interested in this function.
        """
        with self._access_lock:
            self._env = env

    @cmpi_logging.trace_method
    def add_filters(self, class_name, filters, ensure_installed=False):
        """
        Add new filters to the helper. These filters will be allowed for
        subscription.

        :param filters: (``dictionary filter_id -> filter properties``)
            The filters. ``filter properties`` is dictionary
            ``property_name -> value``, where at least ``Query`` property
            must be set. ``Name`` property will be automatically created
            as 'LMI:<class_name>:<filter_id>'.
        :param ensure_installed: (``bool``) Whether to check for filter presence
            at broker and install them if missing. **Note** That in order
            for this to work, the context must be updated with user's
            credentials. See :ref:`update_context-label`.
        """
        with self._access_lock:
            if not class_name in self._filters:
                self._filters[class_name] = pywbem.NocaseDict()
            self._filters[class_name].update(filters)
            if ensure_installed:
                self.ensure_filters_installed(class_name=class_name)

    @cmpi_logging.trace_method
    def authorize_filter(self, _env, fltr, _class_name, _op, _owner):
        """
        AuthorizeFilter callback from CIMOM. Call this method from appropriate
        CIMOM callback

        It asks us to verify whether this filter is allowed.

        :param fltr: Contains the filter that must be authorized.
        :param _class_name: (``String``) Contains the class name extracted
            from the filter FROM clause.
        :param _op: The name of the class for which monitoring is required.
            Only the namespace part is set if className is a process indication.
        :param _owner The owner argument is the destination owner.
        """
        with self._access_lock:
            res = self._get_matching_filter(fltr)
            if res is not None:
                self._subscribed_filters.add((res[0], res[1]))
                LOG().info("InstanceFilter %s: %s authorized",
                        make_filter_name(res[0], res[1]), fltr)
                return True
            return False

    @cmpi_logging.trace_method
    def activate_filter(self, _env, fltr, _class_name, _class_path,
            first_activation):
        """
        ActivateFilter callback from CIMOM. Call this method from appropriate
        CIMOM callback.

        It ask us to begin monitoring a resource. The function shall begin
        monitoring the resource according to the filter express only.

        :param fltr: The filter argument contains the filter specification
            for this subscription to become active.
        :param _class_name: (``String``) The class name extracted from the filter
            FROM clause.
        :param _class_path: (``CIMInstanceName``) The name of the class for
            which monitoring is required. Only the namespace part is set if
            eventType is a process indication.
        :param first_activation: (``bool``) Set to true if this is the first
            filter for className.
        """
        with self._access_lock:
            if not first_activation:
                return
            res = self._get_matching_filter(fltr)
            if res is not None:
                self._subscribed_filters.add((res[0], res[1]))
                LOG().info("InstanceFilter %s: %s started",
                        make_filter_name(res[0], res[1]), fltr)

    @cmpi_logging.trace_method
    def deactivate_filter(self, _env, fltr, _class_name, _class_path,
            last_activation):
        """
        DeactivateFilter callback from CIMOM. Call this method from appropriate
        CIMOM callback.

        Informs us that monitoring using this filter should stop.

        :param fltr: The filter argument contains the filter specification for
            this subscription to become active.
        :param class_name: (``String``) The class name extracted from the filter
            FROM clause.
        :param class_path: (``CIMInstanceName``) class_path The name of the
            class for which monitoring is required. Only the namespace part is
            set if className is a process indication.
        :last_activation: (``bool``) Set to true if this is the last filter for
            className.
        """
        with self._access_lock:
            if not last_activation:
                return
            res = self._get_matching_filter(fltr)
            if res is not None:
                self._subscribed_filters.remove((res[0], res[1]))
                LOG().info("InstanceFilter %s: %s stopped",
                        make_filter_name(res[0], res[1]), fltr)

    @cmpi_logging.trace_method
    def enable_indications(self, _env):
        """
        EnableIndications callback from CIMOM. Call this method from
        appropriate CIMOM callback.

        Tells us that indications can now be generated. The MB is now prepared
        to process indications. The function is normally called by the MB after
        having done its intialization and processing of persistent subscription
        requests.
        """
        with self._access_lock:
            self._enabled = True
        LOG().info("Indications enabled")

    @cmpi_logging.trace_method
    def disable_indications(self, _env):
        """
        EnableIndications callback from CIMOM. Call this method from
        appropriate CIMOM callback.

        Tells us that we should stop generating indications. MB will not accept
        any indications until enabled again. The function is normally called
        when the MB is shutting down indication services either temporarily or
        permanently.
        """
        with self._access_lock:
            self._enabled = False
        LOG().info("Indications disabled")

    @cmpi_logging.trace_method
    def send_indication(self, indication):
        """
        Send indication to all subscribers. Call this method from appropriate
        CIMOM callback.
        """
        self._queue.put(indication)

    @cmpi_logging.trace_method
    def send_instcreation(self, instance, filter_id):
        """
        Send ``LMI_<nameprefix>InstCreation`` indication with given instance.

        :param instance: (``CIMInstance``) The created instance.
        :param filter_id: (``string``) The ID of registered filter which
            corresponds to this indication.
        """
        if not self.is_subscribed(instance.classname, filter_id):
            return
        path = pywbem.CIMInstanceName(
                classname=self.instcreation_classname,
                namespace=self.namespace)
        ind = pywbem.CIMInstance(
                self.instcreation_classname,
                path=path)
        ind['SourceInstance'] = instance
        ind['SourceInstanceHost'] = socket.gethostname()
        ind['SourceInstanceModelPath'] = str(instance.path)
        ind['IndicationFilterName'] = make_filter_name(
                instance.classname, filter_id)
        ind['PerceivedSeverity'] = self.SEVERITY_INFO

        LOG().info("Sending indication %s for %s",
                ind["IndicationFilterName"], str(path))
        self.send_indication(ind)

    @cmpi_logging.trace_method
    def send_instmodification(self, old_instance, new_instance, filter_id):
        """
        Send ``LMI_<nameprefix>InstModification`` indication with given
        instance.

        :param old_instance: (``CIMInstance``) The instance before
            modification.
        :param new_instance: (``CIMInstance``) The instance after modification.
        :param filter_id: (``string``) The ID of registered filter which
            corresponds to this indication.
        """
        if not self.is_subscribed(new_instance.classname, filter_id):
            return
        path = pywbem.CIMInstanceName(
                classname=self.instmodification_classname,
                namespace=self.namespace)
        ind = pywbem.CIMInstance(
                self.instcreation_classname,
                path=path)
        ind['SourceInstance'] = new_instance
        ind['PreviousInstance'] = old_instance
        ind['SourceInstanceHost'] = socket.gethostname()
        ind['SourceInstanceModelPath'] = str(new_instance.path)
        ind['IndicationFilterName'] = make_filter_name(
                new_instance.classname, filter_id)
        ind['PerceivedSeverity'] = self.SEVERITY_INFO

        LOG().info("Sending indication %s for %s",
                ind["IndicationFilterName"], str(path))
        self.send_indication(ind)

    @cmpi_logging.trace_method
    def is_subscribed(self, class_name, fltr_id):
        """
        Return True, if there is someone subscribed for given filter.

        :param class_name: (``string``) *Scoping class* name.
        :param fltr_id: (``string``) ID of the filter to check.
        """
        with self._access_lock:
            if not self._enabled:
                return False
            if (class_name, fltr_id) in self._subscribed_filters:
                return True
            return False

    @cmpi_logging.trace_method
    def is_registered(self, class_name, fltr_id):
        """
        Return True, if filter id has been registered with current instance.

        :param class_name: (``string``) *Scoping class* name.
        :param fltr_id: (``string``) ID of the filter to check.
        """
        with self._access_lock:
            return (class_name in self._filters
                   and fltr_id in self._filters[class_name])

    def _send_indications_loop(self, broker):
        """
        This method runs in its own thread. It just sends all enqueued
        indications.

        :param broker: (``BrokerCIMOMHandle``) Handle of the CIMOM.
        """
        broker.AttachThread()
        while True:
            command = self._queue.get()

            if isinstance(command, pywbem.CIMInstance) :
                indication = command
                LOG().trace_info("Delivering indication %s",
                        str(indication.path))
                broker.DeliverIndication(self.namespace, indication)

            elif isinstance(command, int):
                LOG().trace_info("Received command %d", command)
                if command == self.COMMAND_STOP:
                    if hasattr(self._queue, "task_done"):
                        self._queue.task_done()
                    break

            if hasattr(self._queue, "task_done"):
                self._queue.task_done()

        LOG().info("Stopped Indication thread.")

    @cmpi_logging.trace_method
    def shutdown(self):
        """
        Stop the thread. This method blocks until the thread is safely
        destroyed.
        """
        self._queue.put(self.COMMAND_STOP)
        self._indication_sender.join()
