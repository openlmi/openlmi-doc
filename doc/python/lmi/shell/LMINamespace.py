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

import LMIExceptions

from lmi.shell.LMIBaseObject import LMIWrapperBaseObject

from lmi.shell.LMIUtil import lmi_wrap_cim_namespace
from lmi.shell.LMIUtil import lmi_wrap_cim_class
from lmi.shell.LMIUtil import lmi_transform_to_lmi


class LMINamespace(LMIWrapperBaseObject):
    """
    LMI class representing CIM namespace.

    :param LMIConnection conn: connection object
    :param string name: namespace name
    """
    def __init__(self, conn, name):
        super(LMINamespace, self).__init__(conn)
        self._name = name

    def __getattr__(self, name):
        """
        Returns a :py:class:`.LMIClass` object.

        :param string name: class name
        :returns: :py:class:`.LMIClass` object
        """
        return lmi_wrap_cim_class(self._conn, name, self.name)

    def __repr__(self):
        """
        :returns: pretty string for the object
        """
        return "%s(namespace='%s', ...)" % (self.__class__.__name__, self.name)

    def classes(self):
        """
        Returns a list of class names.

        :param string filter_key: substring of a class name
        :param bool exact_match: tells, if to search for exact match or
            substring
        :returns: list of class names

        **Usage:** :ref:`namespaces_available_classes`.
        """
        class_names, _, errorstr = self._conn.client.get_class_names(
            self._name, DeepInheritance=True)
        if not class_names:
            return []
        return class_names

    def get_class(self, classname):
        """
        Returns :py:class:`.LMIClass`.

        :param string classname: class name of new :py:class:`.LMIClass`
        :raises: :py:exc:`.LMIClassNotFound`
        """
        class_names, _, _ = self._conn.client.get_class_names(
            self._name, DeepInheritance=True)
        if class_names is not None and classname in class_names:
            return lmi_wrap_cim_class(self._conn, classname, self.name)
        raise LMIExceptions.LMIClassNotFound(self.name, classname)

    def print_classes(self):
        """
        Prints out a list of classes.

        :param string filter_key: substring of a class name
        :param bool exact_match: tells, if to search for exact match, or to
            search for a matching substring

        **Usage:** :ref:`namespaces_available_classes`.
        """
        for c in self.classes():
            sys.stdout.write("%s\n" % c)

    def cql(self, query):
        """
        Executes a CQL query and returns a list of :py:class:`.LMIInstance`
        objects.

        :param string query: CQL query to execute
        :returns: :py:class:`.LMIReturnValue` object with ``rval`` set to a
            list of :py:class:`.LMIInstance` objects

        **Usage:** :ref:`namespaces_queries`.
        """
        inst_list, _, errorstr = self._conn.client.exec_query(
            self._conn.client.QUERY_LANG_CQL, query, self._name)
        if not inst_list:
            return []
        return lmi_transform_to_lmi(self._conn, inst_list)

    def wql(self, query):
        """
        Executes a WQL query and returns a list of :py:class:`.LMIInstance`
        objects.

        :param string query: WQL query to execute
        :returns: :py:class:`.LMIReturnValue` object with ``rval`` set to a
            list of :py:class:`.LMIInstance` objects

        **Usage:** :ref:`namespaces_queries`.
        """
        inst_list, _, errorstr = self._conn.client.exec_query(
            self._conn.client.QUERY_LANG_WQL, query, self._name)
        if not inst_list:
            return []
        return lmi_transform_to_lmi(self._conn, inst_list)

    @property
    def name(self):
        """
        :returns: namespace name
        :rtype: string
        """
        return self._name


class LMINamespaceRoot(LMINamespace):
    """
    Derived class for *root* namespace. Object of this class is accessible from
    :py:class:`.LMIConnection` object as a hierarchy entry.

    :param LMIConnection conn: connection object
    """
    _SUPPORTED_NAMESPACES = [
        "cimv2",
        "dcim",
        "interop",
        "PG_InterOp",
        "PG_Internal"
    ]

    def __init__(self, conn):
        super(LMINamespaceRoot, self).__init__(conn, "root")

    def __getattr__(self, name):
        if name in LMINamespaceRoot._SUPPORTED_NAMESPACES:
            return lmi_wrap_cim_namespace(self._conn, "root/" + name)
        raise AttributeError(name)

    @property
    def namespaces(self):
        """
        :returns: list of strings with available namespaces

        **Usage:** :ref:`namespaces_available_namespaces`.
        """
        return LMINamespaceRoot._SUPPORTED_NAMESPACES

    def print_namespaces(self):
        """
        Prints out all available namespaces accessible via the namespace
        `root`.

        **Usage:** :ref:`namespaces_available_namespaces`.
        """
        for ns in LMINamespaceRoot._SUPPORTED_NAMESPACES:
            sys.stdout.write("%s\n" % ns)
