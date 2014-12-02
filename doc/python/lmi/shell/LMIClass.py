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

from lmi.shell.compat import *

from lmi.shell.LMIBaseObject import LMIWrapperBaseObject
from lmi.shell.LMIFormatter import LMIClassFormatter
from lmi.shell.LMIConstantValues import LMIConstantValuesParamProp
from lmi.shell.LMIObjectFactory import LMIObjectFactory

from lmi.shell.LMIExceptions import LMIUnknownPropertyError

from lmi.shell.LMIDecorators import lmi_class_fetch_lazy
from lmi.shell.LMIDecorators import lmi_wrap_cim_exceptions_rval
from lmi.shell.LMIDecorators import lmi_return_val_if_fail
from lmi.shell.LMIDecorators import lmi_return_if_fail

from lmi.shell.LMIShellLogger import lmi_get_logger

from lmi.shell.LMIUtil import lmi_cast_to_cim
from lmi.shell.LMIUtil import lmi_get_use_exceptions
from lmi.shell.LMIUtil import lmi_set_use_exceptions
from lmi.shell.LMIUtil import lmi_raise_or_dump_exception
from lmi.shell.LMIUtil import lmi_transform_to_lmi


class LMIClass(LMIWrapperBaseObject):
    """
    LMI wrapper class representing :py:class:`wbem.CIMClass`.

    :param LMIConnection conn: connection object
    :param LMINamespace namespace: namespace object
    :param string classname: CIM class name
    """
    def __init__(self, conn, namespace, classname):
        # We use __dict__ to avoid recursion potentially caused by
        # combo __setattr__ and __getattr__
        self.__dict__["_namespace"] = namespace
        self.__dict__["_cim_class"] = None
        self.__dict__["_cim_class_full_fetch"] = False
        self.__dict__["_cim_classname"] = classname
        self.__dict__["_valuemap_properties_list"] = []
        super(LMIClass, self).__init__(conn)

    def __repr__(self):
        """
        :returns: a pretty string for the object
        """
        return "%s(classname='%s', ...)" % (
            self.__class__.__name__, self.classname)

    def __getattr__(self, name):
        """
        Returns either a class member, or a constant value.

        Simplifies the code and constant value can be retrieved by
        :samp:`object.constant_value`.

        :param string name: object member or constant values member
        :returns: class member of :py:class:`.LMIConstantValuesParamProp`
            object
        """
        if not self._conn.is_wsman() and name.endswith("Values"):
            if not self.is_fetched(True):
                self.fetch(True)
            property_name = name[:-6]
            return LMIConstantValuesParamProp(
                self._cim_class.properties[property_name])
        raise AttributeError(name)

    @lmi_class_fetch_lazy()
    @lmi_return_val_if_fail(lambda obj: obj._namespace, None)
    def create_instance(self, properties=None, qualifiers=None,
                        property_list=None):
        """
        Creates a new :py:class:`wbem.CIMInstance` at the server side and
        returns :py:class:`.LMIReturnValue` object containing
        :py:class:`.LMIInstance` as a result.

        :param dictionary properties: initial properties with corresponding
            values
        :param dictionary qualifiers: initial qualifiers
        :param list property_list: list of properties, which should be present
            in :py:class:`.LMIInstance` object

        **Usage:** See :ref:`class_create_instance`.
        """
        if self._conn.is_wsman():
            # WSMAN client doesn't support CreateInstance()
            lmi_get_logger().info("WSMAN client doesn't support CreateInstance()")
            return None

        # No need to copy dictionaries to avoid the variable mix-up, the
        # copying is done in client.create_instance(), we just pass
        # what we get.
        properties = properties if properties is not None else {}
        qualifiers = qualifiers if qualifiers is not None else {}
        self_properties = self._cim_class.properties
        for key, value in properties.iteritems():
            if key not in self._cim_class.properties:
                errorstr = "No such instance property '%s'" % key
                lmi_raise_or_dump_exception(LMIUnknownPropertyError(errorstr))
                return None
            if isinstance(value, LMIObjectFactory().LMIInstanceName):
                value = value.wrapped_object
            t = self._cim_class.properties[key].type
            properties[key] = lmi_cast_to_cim(t, value)
        instance, rparams, errorstr = self._conn.client.create_instance(
            self.classname, self.namespace, self._conn.hostname,
            properties, qualifiers, property_list)
        if not instance:
            return None
        return lmi_transform_to_lmi(self._conn, instance)

    @lmi_class_fetch_lazy(True)
    @lmi_return_if_fail(lambda obj: obj._namespace)
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

        LMIClassFormatter(self._cim_class).fancy_format(
            self._conn.client.interactive)

    def is_fetched(self, full_fetch=False):
        """
        Returns True, if :py:class:`wbem.CIMClass` has been fetched.

        :param bool full_fetch: defines, if qualifiers are also included
        """
        if self._conn.is_wsman():
            # WSMAN doesn't support GetClass(). We return always False.
            return False

        return bool(self._cim_class) and \
            (not full_fetch or self._cim_class_full_fetch)

    @lmi_wrap_cim_exceptions_rval(None)
    def fetch(self, full_fetch=False):
        """
        Manually fetches a wrapped :py:class:`wbem.CIMClass` object.

        :param bool full_fetch: True, if :py:class:`wbem.CIMClass` should
            include qualifiers and class origin. Default value is False.
        :raises: :py:exc:`.CIMError`, :py:exc:`.ConnectionError`

        **Usage:** See :ref:`class_fetching_a_class`.
        """
        if self._conn.is_wsman():
            # WSMAN doesn't support GetClass(). We do not try to fetch the
            # class.
            return

        if self.is_fetched(full_fetch) or not self._namespace:
            # We already have CIMClass (at certain level of detail), or we do
            # not know the namespace, from which the class should be fetched.
            return

        full_cim_class, _, _ = self._conn.client.get_class(
            self._cim_classname,
            self._namespace.name,
            full_fetch=full_fetch,
            LocalOnly=False)

        self._cim_class = full_cim_class

        if full_fetch and self._cim_class:
            self._cim_class_full_fetch = full_fetch
            # Store the constant values as a list. This can consume some time,
            # if computed on demand.
            self._valuemap_properties_list = [
                k for k, v in self._cim_class.properties.iteritems()
                if "ValueMap" in v.qualifiers and "Values" in v.qualifiers]

    # NOTE: usage with Key=something, Value=something is deprecated
    # NOTE: inst_filter is either None or dict
    @lmi_return_val_if_fail(lambda obj: obj._namespace, [])
    def instance_names(self, inst_filter=None, **kwargs):
        """
        Returns a LMIReturnValue containing a list of LMIInstanceNames.

        :param dictionary inst_filter: filter values. The key corresponds to
            the primary key of the :py:class:`wbem.CIMInstanceName`; value
            contains the filtering value
        :param dictionary kwargs: deprecated keyword arguments

            * **Key** or **key** (*string*) -- filtering key, see above
            * **Value** or **value** -- filtering value, see above

        :returns: :py:class:`.LMIReturnValue` object with ``rval`` set to a
            list of :py:class:`.LMIInstanceName` objects

        **Usage:** See :ref:`class_get_instance_names` and
        :ref:`class_instance_filtering`.
        """
        inst_name_list, _, errorstr = self._conn.client.get_instance_names(
            self._cim_classname, self._namespace.name, inst_filter, **kwargs)
        if not inst_name_list:
            return []
        return lmi_transform_to_lmi(self._conn, inst_name_list)

    def new_instance_name(self, keybindings):
        """
        Create new :py:class:`.LMIInstanceName` object by passing all the
            keys/values of the object.

        :param dictionary keybindings: primary keys of instance name with
            corresponding values
        :returns: new :py:class:`.LMIInstanceName` object

        **Usage:** See :ref:`class_new_instance_name`.
        """
        kbs = wbem.NocaseDict()
        for key, value in keybindings.iteritems():
            if isinstance(value, LMIObjectFactory().LMIInstanceName):
                value = value.wrapped_object
            elif isinstance(value, str):
                # Convert strings to unicode
                value = unicode(value, "utf-8")
            kbs[key] = value
        cim_inst_name = wbem.CIMInstanceName(
            self.classname, kbs, namespace=self.namespace)
        return lmi_transform_to_lmi(self._conn, cim_inst_name)

    # NOTE: usage with Key=something, Value=something is deprecated
    # NOTE: inst_filter is either None or dict
    def first_instance_name(self, inst_filter=None, **kwargs):
        """
        Returns the first :py:class:`.LMIInstanceName` of the corresponding
        class.

        :param dictionary inst_filter: filter values, where the key corresponds
            to the primary key of :py:class:`wbem.CIMInstanceName`; value
            contains the filtering value
        :param dictionary kwargs: deprecated keyword arguments

            * **Key** or **key** (*string*) -- filtering key, see above
            * **Value** or **value** -- filtering value, see above

        :returns: first :py:class:`.LMIInstanceName` object

        **Usage:** See :ref:`class_get_instance_names` and
        :ref:`class_instance_filtering`.
        """
        inst_name_list, _, errorstr = self._conn.client.get_instance_names(
            self._cim_classname, self._namespace.name, inst_filter, limit=1,
            **kwargs)
        if not inst_name_list:
            return None
        return lmi_transform_to_lmi(self._conn, inst_name_list[0])

    # NOTE: usage with Key=something, Value=something is deprecated
    # NOTE: inst_filter is either None or dict
    @lmi_return_val_if_fail(lambda obj: obj._namespace, [])
    def instances(self, inst_filter=None, client_filtering=False, **kwargs):
        """
        Returns a list of objects of :py:class:`.LMIInstance`.

        :param dictionary inst_filter: filter values, where the key corresponds
            to the key of :py:class:`wbem.CIMInstance`; value contains the
            filtering value
        :param bool client_filtering: if True, client-side filtering will be
            performed, otherwise the filtering will be done by a CIMOM. Default
            value is False.
        :param dictionary kwargs: deprecated keyword arguments

            * **Key** or **key** (*string*) -- filtering key, see above
            * **Value** or **value** -- filtering value, see above

        :returns: list of :py:class:`.LMIInstance` objects

        **Usage:** See :ref:`class_get_instances` and
        :ref:`class_instance_filtering`.
        """
        instance_list, _, errorstr = self._conn.client.get_instances(
            self._cim_classname, self._namespace.name, inst_filter,
            client_filtering, **kwargs)
        if not instance_list:
            return []
        return lmi_transform_to_lmi(self._conn, instance_list)

    # NOTE: usage with Key=something, Value=something is deprecated
    # NOTE: inst_filter is either None or dict
    def first_instance(self, inst_filter=None, client_filtering=False,
                       **kwargs):
        """
        Returns the first :py:class:`.LMIInstance` of the corresponding class.

        :param dictionary inst_filter: filter values, where the key corresponds
            to the key of :py:class:`wbem.CIMInstance`; value contains the
            filtering value.
        :param bool client_filtering: if True, client-side filtering will be
            performed, otherwise the filtering will be done by a CIMOM. Default
            value is False.
        :param dictionary kwargs: deprecated keyword arguments

            * **Key** or **key** -- filtering key, see above
            * **Value** or **value** -- filtering value, see above

        :returns: first :py:class:`.LMIInstance` object

        **Usage:** See :ref:`class_get_instances` and
        :ref:`class_instance_filtering`.
        """
        filter_value = "value" in [k.lower() for k in kwargs.keys()]
        if inst_filter or filter_value:
            instance_list, _, errorstr = self._conn.client.get_instances(
                self._cim_classname, self._namespace.name, inst_filter,
                client_filtering, limit=1, **kwargs)
            if not instance_list:
                return None
            instance = instance_list[0]
            return lmi_transform_to_lmi(self._conn, instance)
        inst_name = self.first_instance_name(inst_filter, **kwargs)
        return inst_name.to_instance() if inst_name else None

    @lmi_class_fetch_lazy(True)
    @lmi_return_val_if_fail(lambda obj: obj._namespace, [])
    def valuemap_properties(self):
        """
        :returns: list of strings of the constant names

        **Usage:** :ref:`class_get_valuemap_properties`.
        """
        return self._valuemap_properties_list

    @lmi_class_fetch_lazy(True)
    @lmi_return_if_fail(lambda obj: obj._namespace)
    def print_valuemap_properties(self):
        """
        Prints out the list of string of constant names.

        **Usage:** :ref:`class_get_valuemap_properties`.
        """
        for i in self._valuemap_properties_list:
            sys.stdout.write("%s\n" % i)

    @lmi_class_fetch_lazy()
    @lmi_return_val_if_fail(lambda obj: obj._namespace, [])
    def properties(self):
        """
        :returns: list of strings of the :py:class:`wbem.CIMClass` properties

        **Usage:** See :ref:`class_properties`.
        """
        if self._conn.is_wsman():
            # WSMAN does not support GetClass().
            return []

        return self._cim_class.properties.keys()

    @lmi_class_fetch_lazy()
    @lmi_return_if_fail(lambda obj: obj._namespace)
    def print_properties(self):
        """
        Prints out the list of :py:class:`wbem.CIMClass` properties.

        **Usage:** See :ref:`class_properties`.
        """
        for prop in self.methods():
            sys.stdout.write("%s\n" % prop)

    @lmi_class_fetch_lazy()
    @lmi_return_val_if_fail(lambda obj: obj._namespace, [])
    def methods(self):
        """
        :returns: list of strings of :py:class:`wbem.CIMClass` methods.

        **Usage:** See :ref:`class_methods`.
        **Note:** When caching is turned off, this method may consume some
        time.
        """
        if self._conn.is_wsman():
            # WSMAN does not support GetClass().
            return []

        methods_lst = self._cim_class.methods.keys()
        class_names, _, _ = self._conn.client.get_class_names(
            self.namespace, DeepInheritance=True)

        if class_names is not None:
            # Iterate through a list of all CIM methods and append any method
            # which can be called in the synchronous way. One type of such
            # method is the method, which has its counterpart class
            # __MethodParameters_<Method>.  The other one is the method, which
            # defines a Job return paremeter.
            for name, method in self._cim_class.methods.iteritems():
                if "__MethodParameters_" + name in class_names or \
                        "Job" in method.parameters:
                    methods_lst.append("Sync" + name)

        return methods_lst

    @lmi_class_fetch_lazy(True)
    @lmi_return_if_fail(lambda obj: obj._namespace)
    def print_methods(self):
        """
        Prints out the list of :py:class:`wbem.CIMClass` methods.

        **Usage:** See :ref:`class_methods`.
        """
        for name, method in self._cim_class.methods.iteritems():
            in_params = [
                "%s %s" % (param.type, pname)
                for pname, param in method.parameters.iteritems()
                if "Out" not in param.qualifiers or \
                    not param.qualifiers["Out"]]
            out_params = [
                "%s:%s" % (pname, param.type)
                for pname, param in method.parameters.iteritems()
                if "Out" in param.qualifiers and \
                    param.qualifiers["Out"]]
            sys.stdout.write(
                "LMIReturnValue(%s rval, rparams={%s}) %s(%s)\n" % (
                    method.return_type, ", ".join(out_params),
                    name, ", ".join(in_params)))

    @property
    def classname(self):
        """
        :returns: class name
        :rtype: string
        """
        return self._cim_classname

    @property
    @lmi_return_val_if_fail(lambda obj: obj._namespace, "Unknown")
    def namespace(self):
        """
        :returns: namespace name
        :rtype: string
        """
        return self._namespace.name

    @property
    @lmi_class_fetch_lazy()
    def wrapped_object(self):
        """
        :returns: wrapped :py:class:`wbem.CIMClass` object
        """
        return self._cim_class
