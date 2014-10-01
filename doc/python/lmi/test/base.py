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
Base classes for *OpenLMI Provider* test cases.
"""

import os
import socket

from lmi.test import CIMError
from lmi.test import unittest
from lmi.test import util
from lmi.test import wbem

def render_iname(iname, indent=2):
    """
    Render object path in human readable way. Result will occupy multiple
    lines. The first line is a class name, which is not indented at all. Other
    lines will be indented with *indent* spaces.

    :param iname: Object path to render.
    :type iname: :py:class:`lmiwbem.CIMInstanceName`
    :param integer ident: Number of spaces prefixing all lines but the first.
    :returns: *iname* nicely rendered.
    :rtype: string
    """
    if not isinstance(iname, wbem.CIMInstanceName):
        return repr(iname)
    lines = [ "%s" % iname.classname
            , " "*indent + "namespace: %s" % iname.namespace
            , " "*indent + "keys:"]
    align = max([len(k) for k in iname.keybindings.iterkeys()])
    for key, value in iname.keybindings.iteritems():
        if isinstance(value, wbem.CIMInstanceName):
            value = render_iname(value, indent + 4)
        lines.append(" "*indent + ("  %%-%ds : %%s" % align) % (key, value))
    return "\n".join(lines)

class BaseLmiTestCase(unittest.TestCase):
    """
    Base class for all LMI test cases.
    """

    #: Value used in ``SystemName`` key properties in various *CIM* instances.
    #: It's also used to fill ``CIM_ComputerySystem.Name`` property.
    SYSTEM_NAME = socket.gethostname()

    @classmethod
    def setUpClass(cls):
        #: Cached value of SystemCreationClassName set with
        #: ``LMI_CS_CLASSNAME`` environment variable.
        cls.system_cs_name = os.environ.get(
                "LMI_CS_CLASSNAME", "PG_ComputerSystem")
        #: *URL* of *CIMOM* we connect to. Overriden with ``LMI_CIMOM_URL``
        #: environment variable.
        cls.url = os.environ.get("LMI_CIMOM_URL", "https://localhost:5989")
        #: User name for authentication with *CIMOM*. Overriden with
        #: ``LMI_CIMOM_USERNAME`` variable.
        cls.username = os.environ.get("LMI_CIMOM_USERNAME", "root")
        #: User's password for authentication with *CIMOM*. Overriden with
        #: ``LMI_CIMOM_PASSWORD`` environment variable.
        cls.password = os.environ.get("LMI_CIMOM_PASSWORD", "")
        #: Name of *CIMOM* we connect to. There are two possible values:
        #: ``"tog-pegasus"`` and ``"sblim-sfcb"``. Overriden with
        #: ``LMI_CIMOM_BROKER`` environment variable.
        cls.cimom = os.environ.get("LMI_CIMOM_BROKER", "tog-pegasus")
        #: Boolean value saying whether to run dangerous tests. These are marked
        #: with :py:func:`mark_dangerous` decorator. This is set with
        #: ``LMI_RUN_DANGEROUS`` environment variable.
        cls.run_dangerous = util.get_environvar('LMI_RUN_DANGEROUS', '0', bool)
        #: Boolean value saying whether to run tedious tests. These are marked
        #: with :py:func:`mark_tedious` decorator. This is set with
        #: ``LMI_RUN_TEDIOUS`` environment variable.
        cls.run_tedious = util.get_environvar('LMI_RUN_TEDIOUS', '1', bool)

    def assertRaisesCIM(self, cim_err_code, func, *args, **kwds):
        """
        This test passes if given function called with supplied arguments
        raises `CIMError` with given cim error code.
        """
        with self.assertRaises(CIMError) as cm:
            func(*args, **kwds)
        self.assertEqual(cim_err_code, cm.exception.args[0])

    def assertCIMNameEqual(self, fst, snd, msg=None):
        """
        Compare two objects of :py:class:`lmiwbem.CIMInstanceName`. Their host
        properties are not checked.
        """
        if msg is None:
            msg = ( "%s\n\nis not equal to: %s"
                  % (render_iname(fst), render_iname(snd)))
        self.assertTrue(util.check_inames_equal(fst, snd), msg)

    def assertCIMNameIn(self, name, candidates):
        """
        Checks that given :py:class:`lmiwbem.CIMInstanceName` is present in
        set of candidates. It compares all properties but ``host``.
        """
        for candidate in candidates:
            if util.check_inames_equal(name, candidate):
                return
        self.assertTrue(False, 'name "%s" is not in candidates' % str(name))

    def assertNocaseDictEqual(self, fst, snd, msg=None):
        """
        Compare two no-case dictionaries ignoring the case of their keys.
        """
        fst_dict = {}
        for (key, value) in fst.iteritems():
            fst_dict[key.lower()] = value
        snd_dict = {}
        for (key, value) in snd.iteritems():
            snd_dict[key.lower()] = value
        self.assertEqual(fst_dict, snd_dict, msg)

