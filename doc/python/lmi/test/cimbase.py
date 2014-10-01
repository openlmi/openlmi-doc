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
# Authors: Roman Rakus <rrakus@redhat.com>
#
"""
Base class and utilities for test suits written with plain lmiwbem
abastractions.
"""

import BaseHTTPServer
import Queue
import random
import subprocess
import threading
import time

from lmi.test import base
from lmi.test import CIMError
from lmi.test import wbem

JOB_CREATED = 4096


class CIMTestCase(base.BaseLmiTestCase):
    """
    Base class for LMI test cases based on plain lmiwbem.
    """

    #: Says, whether the test case needs indication listener running or not.
    #: Each subclass shall override this property and set it to ``True`` if
    #: it want to test indication events.
    NEEDS_INDICATIONS = False

    _WBEMCONNECTION = None
    _SYSTEM_INAME = None

    @classmethod
    def needs_indications(cls):
        """
        Whether the indication listener should be started for this test case.
        In subclasses override ``NEEDS_INDICATIONS`` property and set it to
        ``True`` if indication testing is desired.
        """
        return cls.NEEDS_INDICATIONS

    @classmethod
    def setUpClass(cls):
        base.BaseLmiTestCase.setUpClass.im_func(cls)
        if cls.needs_indications():
            cls.indication_port = random.randint(12000, 13000)
            cls.indication_queue = Queue.Queue()
            cls.listener = wbem.CIMIndicationListener(
                "0.0.0.0", cls.indication_port)
            cls.listener.add_handler("", cls._process_indication)

    @classmethod
    def tearDownClass(cls):
        if cls.needs_indications():
            cls.listener.stop()

    @classmethod
    def _start_listening(cls):
        """ Start listening for incoming indications. """
        cls.listener.start()

    @classmethod
    def _process_indication(cls, indication):
        """ Callback to process one indication."""
        print "Got indication"
        cls.indication_queue.put(indication)

    @property
    def wbemconnection(self):
        """
        :returns: Active connection to *CIMOM*.
        :rtype: :py:class:`lmiwbem.WBEMConnection`
        """
        if CIMTestCase._WBEMCONNECTION is None:
            CIMTestCase._WBEMCONNECTION = wbem.WBEMConnection(self.url,
                    (self.username, self.password))
        return CIMTestCase._WBEMCONNECTION

    @property
    def system_iname(self):
        """
        :returns: Instance of ``CIM_ComputerSystem`` registered with *CIMOM*.
        :rtype: :py:class:`lmi.shell.LMIInstanceName`
        """
        if CIMTestCase._SYSTEM_INAME is None:
            CIMTestCase._SYSTEM_INAME = self.wbemconnection. \
                    EnumerateInstanceNames(self.system_cs_name, 'root/cimv2')[0]
        return CIMTestCase._SYSTEM_INAME.copy()

    def setUp(self):
        self.subscribed = {}

    def tearDown(self):
        for name in self.subscribed.keys():
            self.unsubscribe(name)

    def assertCIMIsSubclass(self, cls, base_cls):
        """
        Checks, whether cls is subclass of base_cls from CIM perspective.
        @param cls name of subclass
        @param base_cls name of base class
        """
        if not isinstance(cls, basestring):
            raise TypeError("cls must be a string")
        if not isinstance(base_cls, basestring):
            raise TypeError("base_cls must be a string")
        return self.assertTrue(wbem.is_subclass(self.wbemconnection,
            "root/cimv2", base_cls, cls))

    def get_indication(self, timeout):
        """ Wait for an indication for given nr. of seconds and return it."""
        try:
            indication = self.indication_queue.get(timeout=timeout)
        except Queue.Empty:
            raise AssertionError("Timeout when waiting for indication")
        self.indication_queue.task_done()
        return indication

    def make_filter_iname(self, filter_name):
        """
        Create an instance name of ``CIM_IndicationFilter``.

        :rtype: :py:class:`lmiwbem.CIMInstanceName`
        """
        return wbem.CIMInstanceName(
                    classname="CIM_IndicationFilter",
                    namespace="root/interop",
                    keybindings={
                        'CreationClassName': 'CIM_IndicationFilter',
                        'SystemClassName': self.system_cs_name,
                        'SystemName': self.SYSTEM_NAME,
                        'Name': filter_name})

    def make_filter_inst(self, filter_name, query, query_lang="DMTF:CQL"):
        """
        Create an instance of ``CIM_IndicationFilter``.

        :rtype: :py:class:`lmiwbem.CIMInstance`
        """
        inst = wbem.CIMInstance('CIM_IndicationFilter')
        inst['CreationClassName'] = 'CIM_IndicationFilter'
        inst['SystemCreationClassName'] = self.system_cs_name
        inst['SystemName'] = self.SYSTEM_NAME
        inst['Name'] = filter_name
        inst['Query'] = query
        inst['QueryLanguage'] = query_lang
        inst['SourceNamespace'] = "root/cimv2"
        inst.path = self.make_filter_iname(filter_name)
        return inst

    def subscribe(self, filter_name, query=None, querylang="DMTF:CQL"):
        """
        Create indication subscription for given filter name.
        """
        if not self.needs_indications():
            raise Exception("can not subscribe to indications, enable them"
                    " with NEEDS_INDICATIONS")

        if query is not None:
            # Create filter first
            indfilter = self.wbemconnection.CreateInstance(
                    self.make_filter_inst(filter_name, query, querylang))
        else:
            # the filter is already created, assemble its name
            indfilter = self.make_filter_iname(filter_name)

        # create destination
        destinst = wbem.CIMInstance('CIM_ListenerDestinationCIMXML')
        destinst['CreationClassName'] = 'CIM_ListenerDestinationCIMXML'
        destinst['SystemCreationClassName'] = self.system_cs_name
        destinst['SystemName'] = self.SYSTEM_NAME
        destinst['Name'] = filter_name
        destinst['Destination'] = "http://localhost:%d" % (self.indication_port)
        destinst['PersistenceType'] = wbem.Uint16(3) # Transient
        cop = wbem.CIMInstanceName(
                'CIM_ListenerDestinationCIMXML', namespace="root/interop")
        cop.keybindings = {
                'CreationClassName' : 'CIM_ListenerDestinationCIMXML',
                'SystemClassName'   : self.system_cs_name,
                'SystemName'        : self.SYSTEM_NAME,
                'Name'              : filter_name }
        destinst.path = cop
        destname = self.wbemconnection.CreateInstance(destinst)

        # create the subscription
        subinst = wbem.CIMInstance(
                'CIM_IndicationSubscription')
        subinst['Filter'] = indfilter
        subinst['Handler'] = destname
        cop = wbem.CIMInstanceName(
                'CIM_IndicationSubscription', namespace="root/interop")
        cop.keybindings = {
                'Filter': indfilter,
                'Handler': destname }
        subinst.path = cop
        subscription = self.wbemconnection.CreateInstance(subinst)

        self.subscribed[filter_name] = [subscription, destname]

        if not self.listener.is_alive:
            self._start_listening()
        return subscription

    def unsubscribe(self, filter_name):
        """
        Unsubscribe from given filter.
        """
        if not self.needs_indications():
            raise Exception("can not unsubscribe to indications, enable them"
                    " with NEEDS_INDICATIONS")
        for instance in self.subscribed.pop(filter_name):
            self.wbemconnection.DeleteInstance(instance)

    def finish_job(self,
            jobname,
            assoc_class,
            return_constructor=int):
        """
        Wait until the job finishes and return ``(ret, outparams)``just as
        ``InvokeMethod`` would.

        It's hard to reconstruct these outparams, since the embedded
        instances / ojects do not work in our ``CIMOMS``, therefore special
        care is needed.

        :param jobname: Name of the job.
        :type jobname: :py:class:`lmiwbem.CIMInstanceName`
        :param callable return_constructor: Callable, which converts
            string to the right type, for example ``int``.
        :returns: ``(retvalue, outparams)`` in the same way as
            ``finish_method()`` would.
        :rtype: tuple
        """
        # Use busy loop for now
        # TODO: rework to something sane
        while True:
            job = self.wbemconnection.GetInstance(jobname)
            if job['JobState'] > 5:  # all states higher than 5 are final
                break
            time.sleep(0.1)

        # get the MethodResult
        resultname = self.wbemconnection.AssociatorNames(
                jobname,
                AssocClass=assoc_class)[0]
        result = self.wbemconnection.GetInstance(resultname)
        ind = result['PostCallIndication']
        # check for error
        if ind['Error'] is not None:
            err = ind['Error'][0]
            code = err['CIMStatusCode']
            msg = err['Message']
            raise CIMError(code, msg)

        ret = return_constructor(ind['ReturnValue'])

        # convert output parameters to format returned by InvokeMethod
        outparams = wbem.NocaseDict()
        try:
            params = ind['MethodParameters']
        except KeyError:
            params = {}
        if params:
            for (key, value) in params.iteritems():
                outparams[key] = value

        return (ret, outparams)

    def invoke_async_method(self,
            method_name,
            object_name,
            return_constructor=int,
            *args, **kwargs):
        """
        Invoke a method and if it returns a job, wait for the job.

        :param string method_name: Name of the method.
        :param object_name: Instance, on which the method should be invoked.
        :type object_name: :py:class:`lmiwbem.CIMInstanceName`
        :param callable return_constructor: Callable, which converts
            string to the right type, for example ``int``.
        :param list args: Positional arguments passed to invoked method.
        :param dictionary kwargs: Keyword arguments passed to invoked method.
        :returns: ``(retvalue, outparams)`` in the same way as
            ``finish_method()`` would.
        :rtype: tuple
        """
        (ret, outparams) = self.wbemconnection.InvokeMethod(
                method_name,
                object_name,
                *args,
                **kwargs)
        if ret == JOB_CREATED:
            # wait for the job
            jobname = outparams['Job']
            (ret, outparams) = self.finish_job(jobname, return_constructor)
        return (ret, outparams)

    def restart_cim(self):
        """
        Restart CIMOM
        """
        ret = self.log_run(["service", self.cimom, "restart"])
        time.sleep(1)
        if ret == 0:
            CIMTestCase._WBEMCONNECTION = None
        return ret

    def log_run(self, args):
        """
        Print arguments and run them.
        args must be prepared for subprocess.call()
        """
        print "Running:", " ".join(args)
        return subprocess.call(args)
