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
# Authors: Michal Minar <miminar@redhat.com>
#
"""
Base class and utilities for test suits written upon lmi shell.
"""

import functools
import inspect
import random
import Queue

from lmi.test import base
from lmi.test import CIMError
from lmi.test import wbem
from lmi.shell import connect
from lmi.shell import LMIInstance
from lmi.shell import LMIInstanceName
from lmi.shell import LMIUtil
from lmi.shell import LMIIndicationListener

def enable_lmi_exceptions(method):
    """
    Function or method decorator enabling exceptions to be raised from under
    lmi shell intestines.
    """
    @functools.wraps(method)
    def _wrapper(*args, **kwargs):
        """ Enable exceptions in wrapped function. """
        original = LMIUtil.lmi_get_use_exceptions()
        LMIUtil.lmi_set_use_exceptions(True)
        try:
            retval = method(*args, **kwargs)
        finally:
            LMIUtil.lmi_set_use_exceptions(original)
        return retval

    return _wrapper

def with_connection_timeout(timeout):
    """
    Method decorator for children of `LmiTestCase`. It temporarily changes
    connection timeout for the execution of test represented by wrapped method.
    Once the method exits, connection timeout is reset to previous value.

    :param int timeout: Maximum number of seconds to wait for broker's
        response. If reached, `lmi.shell.compat.ConnectionError` will be raised.
    """
    if not isinstance(timeout, (int, long)):
        raise TypeError("timeout must be an integer")

    if wbem.__name__ == 'lmiwbem':
        def _decorator(method):
            """ Real method decorator. """
            @functools.wraps(method)
            def _wrapper(self, *args, **kwargs):
                """ Temporarily change timeout of connection object. """
                original = self.ns._cliconn.connection.timeout
                self.ns._cliconn.connection.timeout = timeout * 1000
                try:
                    result = method(self, *args, **kwargs)
                finally:
                    self.ns._cliconn.connection.timeout = original
                return result

            return _wrapper

    else:
        # Timeout can't be specified with pywbem.
        def _decorator(method):
            return method

    return _decorator

def to_cim_object(obj):
    """
    :returns: Wrapped object of from inside of shell abstractions.
    """
    if isinstance(obj, (LMIInstance, LMIInstanceName)):
        return obj.wrapped_object
    return obj

class LmiTestCase(base.BaseLmiTestCase):
    """
    Base class for all LMI test cases based on lmi shell.
    """

    #: Once you override this in subclass with a name of CIM class to be tested,
    #: you can use :py:attr:`LmiTestCase.cim_class` to get reference to a shell
    #: wrapper of this class.
    CLASS_NAME = None

    #: Says, whether the test case needs indication listener running or not.
    #: Each subclass shall override this property and set it to ``True`` if
    #: it wants to test indication events.
    NEEDS_INDICATIONS = False

    #: Says, whether the LMIShell intestines shall throw exception upon
    #: failure or error. Having them disabled is a default behaviour of
    #: LMIShell. If the TestCase prefers to have them enabled, it shall
    #: override this property in its body and set it to ``True``.
    USE_EXCEPTIONS = False

    _SYSTEM_INAME = None

    _LMICONNECTION = None

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
        LMIUtil.lmi_set_use_exceptions(cls.USE_EXCEPTIONS)
        if cls.needs_indications():
            cls.indication_port = random.randint(12000, 13000)
            cls.indication_queue = Queue.Queue()
            cls.listener = LMIIndicationListener(
                "0.0.0.0", cls.indication_port)

    @classmethod
    def tearDownClass(cls):
        if cls.needs_indications():
            cls.listener.stop()

    @property
    def conn(self):
        """
        :returns: Active connection to *CIMOM* wrapped by *lmi shell*
            abstraction.
        :rtype: :py:class:`lmi.shell.LMIConnection`
        """
        if LmiTestCase._LMICONNECTION is None:
            kwargs = {}
            con_argspec = inspect.getargspec(connect)
            # support older versions of lmi shell
            if 'verify_server_cert' in con_argspec.args or con_argspec.keywords:
                # newer name
                kwargs['verify_server_cert'] = False
            elif 'verify_certificate' in con_argspec.args:
                # older one
                kwargs['verify_certificate'] = False
            LmiTestCase._LMICONNECTION = connect(
                    self.url, self.username, self.password, **kwargs)

        return LmiTestCase._LMICONNECTION

    @property
    def ns(self):
        """
        :returns: Namespace object representing CIM ``"root/cimv2"`` namespace.
        :rtype: :py:class:`lmi.shell.LMINamespace`
        """
        return self.conn.root.cimv2

    @property
    def cim_class(self):
        """
        A convenience accessor to ``self.conn.root.cimv2.<CLASS_NAME>``.
        You need to override ``CLASS_NAME`` attribute of this class in order
        to use this.

        :returns: Lmi shell wrapper of CIM class to be tested.
        :rtype: :py:class:`lmi.shell.LMIClass`
        """
        if self.CLASS_NAME is None:
            return None
        return getattr(self.ns, self.CLASS_NAME)

    @property
    def system_iname(self):
        """
        :returns: Instance of ``CIM_ComputerSystem`` registered with *CIMOM*.
        :rtype: :py:class:`lmi.shell.LMIInstanceName`
        """
        if LmiTestCase._SYSTEM_INAME is None:
            LmiTestCase._SYSTEM_INAME = getattr(self.ns, self.system_cs_name) \
                    .first_instance_name()
        return LmiTestCase._SYSTEM_INAME.copy()

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
        return self.assertTrue(wbem.is_subclass(self.conn._client._cliconn,
            "root/cimv2", base_cls, cls))

    def assertRaisesCIM(self, cim_err_code, func, *args, **kwds):
        """
        This test passes if given function called with supplied arguments
        raises :py:class:`lmiwbem.CIMError` or
        :py:class:`lmi.shell.LMIExceptions.CIMError` with given cim error code.
        """
        try:
            func(*args, **kwds)
        except Exception as cm:
            # We only want to know, if any kind of CIMError is raised.
            if not isinstance(cm, CIMError) and \
                    (CIMError is not wbem.CIMError or
                        not isinstance(cm, wbem.CIMError)):
                raise cm
        self.assertEqual(cim_err_code, cm.args[0])

    def assertCIMNameEqual(self, fst, snd, msg=None):
        """
        Compare two objects of :py:class:`lmiwbem.CIMInstanceName`. Their host
        properties are not checked.
        """
        base.BaseLmiTestCase.assertCIMNameEqual(
                self,
                to_cim_object(fst),
                to_cim_object(snd),
                msg)

    def assertCIMNameIn(self, name, candidates):
        """
        Checks that given :py:class:`lmiwbem.CIMInstanceName` is present in
        set of candidates. It compares all properties but ``host``.
        """
        name = to_cim_object(name)
        candidates = [to_cim_object(c) for c in candidates]
        base.BaseLmiTestCase.assertCIMNameIn(self, name, candidates)

    def _process_indication(self, ind, **kwargs):
        """ Callback to process one indication."""
        self.indication_queue.put(ind)

    def get_indication(self, timeout):
        """ Wait for an indication for given nr. of seconds and return it."""
        try:
            indication = self.indication_queue.get(timeout=timeout)
        except Queue.Empty:
            raise AssertionError("Timeout when waiting for indication")
        self.indication_queue.task_done()
        return indication

    def subscribe(self, filter_name, query, querylang="DMTF:CQL"):
        """
        Create indication subscription for given filter name.
        """
        if not self.needs_indications():
            raise Exception("can not subscribe to indications, enable them"
                    " with NEEDS_INDICATIONS")

        # Connect the listener
        subscription = self.listener.add_handler(filter_name + "-XXXXXXXX", self._process_indication)

        # Subscribe the indication
        ret = self.conn.subscribe_indication(QueryLanguage=querylang,
            Query=query,
            Name=subscription,
            CreationNamespace="root/interop",
            SubscriptionCreationClassName="CIM_IndicationSubscription",
            FilterCreationClassName="CIM_IndicationFilter",
            FilterSystemCreationClassName=self.system_cs_name,
            FilterSourceNamespace="root/cimv2",
            HandlerCreationClassName="CIM_IndicationHandlerCIMXML",
            HandlerSystemCreationClassName="CIM_ComputerSystem",
            Destination="http://localhost:%d" % (self.indication_port)
        )
        if not ret or not ret.rval:
            raise AssertionError("Indication subscription failed")

        # Start the listener if not running already
        if not self.listener.is_alive:
            self.listener.start()
        return subscription

    def unsubscribe(self, filter_name):
        """
        Unsubscribe from given filter.
        """
        if not self.needs_indications():
            raise Exception("can not unsubscribe to indications, enable them"
                    " with NEEDS_INDICATIONS")
        self.conn.unsubscribe_indication(filter_name)
