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

import os
import sys
import hashlib
import logging
import urlparse

from lmi.shell import wbem

from lmi.shell.LMIObjectFactory import LMIObjectFactory

LOCALHOST_VARIANTS = (
    "localhost",
    "localhost.localdomain",
    "localhost4",
    "localhost4.localdomain4",
    "localhost6",
    "localhost6.localdomain6",
    "127.0.0.1",
    "::1",
)


# By default, the LMIShell does not use exceptions; LMIReturnValue
# is used instead (with proper error string).
class LMIUseExceptionsHelper(object):
    """
    Singleton helper class used for storing a bool flag, which defines,
    if the LMIShell should propagate exceptions or dump them.
    """
    _instance = None

    def __new__(cls):
        """
        Return a new :py:class:`.LMIUseExceptionsHelper` instance, if no shared
        object is present; otherwise an existing instance is returned. By
        default the ``use_exceptions`` flag is set to False.
        """
        if cls._instance is None:
            cls._instance = super(LMIUseExceptionsHelper, cls).__new__(cls)
            cls._instance._use_exceptions = False
        return cls._instance

    @property
    def use_exceptions(self):
        """
        :returns: whether the LMIShell should propagate the exceptions, or
            throw them away
        :rtype: bool
        """
        return self._use_exceptions

    @use_exceptions.setter
    def use_exceptions(self, use=True):
        """
        Property setter, which modifies the bool flag, which indicates, if the
        LMIShell should propagate the exceptions, or dump them.

        :param bool use: specifies, whether to use exceptions in LMIShell
        """
        self._use_exceptions = use


class LMIPassByRef(object):
    """
    Helper class used for passing a value by reference. It uses the advantage
    of python, where all the dictionaries are passed by reference.

    :param val: value, which will be passed by reference

    Example of usage:

    .. code-block:: python

        by_ref = LMIPassByRef(some_value)
        by_ref.value == some_value
    """
    def __init__(self, val):
        self._val = {0: val}

    @property
    def value(self):
        """
        :returns: value passed by reference.
        """
        return self._val[0]

    @value.setter
    def value(self, new_val):
        """
        Property setter for the value passed by reference.

        :param new_val: new value, which is passed by reference
        """
        self._val[0] = new_val


def lmi_get_use_exceptions():
    """
    :returns: whether the LMIShell should use the exceptions, or throw them
        away
    :rtype: bool
    """
    return LMIUseExceptionsHelper().use_exceptions


def lmi_set_use_exceptions(use=True):
    """
    Sets a global flag indicating, if the LMIShell should use the exceptions,
    or throw them away.

    :param bool use: specifies, whether the LMIShell should use the exceptions
    """
    LMIUseExceptionsHelper().use_exceptions = use


def lmi_raise_or_dump_exception(e=None):
    """
    Function which either raises an exception, or throws it away.

    :param Exception e: exception, which will be either raised or thrown away
    """
    if not lmi_get_use_exceptions():
        return
    et, ei, tb = sys.exc_info()
    if e is None:
        raise et, ei, tb
    else:
        raise type(e), e, tb


def lmi_parse_uri(uri):
    """
    Parses URI into scheme, hostname, port, username and password.
    """
    scheme, netloc, path = urlparse.urlparse(uri)[0:3]
    hp = netloc
    if "@" in netloc:
        up, hp = netloc.split("@")
        try:
            username, password = up.split(":")
        except ValueError:
            raise ValueError("Wrong uri format")
    else:
        username = None
        password = None

    if ":" in hp:
        hostname, str_port = hp.split(":")
        port = int(str_port)
    else:
        hostname = hp
        if scheme == "http":
            port = 5985
        else:
            port = 5986

    return scheme, hostname, port, path, username, password


def _lmi_do_cast(t, value, cast):
    """
    Helper function, which preforms the actual cast.

    :param string t: string of CIM type
    :param value: variable to cast
    :param dictionary cast: dictionary with :samp:`type : cast_func`
    :returns: cast value
    """
    cast_func = cast.get(t.lower(), lambda x: x)
    if isinstance(value, (dict, wbem.NocaseDict)):
        return wbem.NocaseDict(
            dict((k, _lmi_do_cast(t, v, cast)) for k, v in value.iteritems()))
    elif isinstance(value, list):
        return [_lmi_do_cast(t, v, cast) for v in value]
    elif isinstance(value, tuple):
        return (_lmi_do_cast(t, v, cast) for v in value)
    return cast_func(value) if value is not None else value


def lmi_cast_to_cim(t, value):
    """
    Casts the value to CIM type.

    :param string t: string of CIM type
    :param value: variable to cast
    :returns: cast value in :py:mod:`wbem` type
    """
    cast = {
        "sint8": lambda x: wbem.Sint8(x),
        "uint8": lambda x: wbem.Uint8(x),
        "sint16": lambda x: wbem.Sint16(x),
        "uint16": lambda x: wbem.Uint16(x),
        "sint32": lambda x: wbem.Sint32(x),
        "uint32": lambda x: wbem.Uint32(x),
        "sint64": lambda x: wbem.Sint64(x),
        "uint64": lambda x: wbem.Uint64(x),
        "string": lambda x: unicode(x, "utf-8") if isinstance(x, str) else x,
        "reference": lambda x: lmi_instance_to_path(x)
    }
    return _lmi_do_cast(t, value, cast)


def lmi_cast_to_lmi(t, value):
    """
    Casts the value to LMI (python) type.

    :param string t: string of CIM type
    :param value: variable to cast
    :returns: cast value in :py:mod:`python` native type
    """
    cast = {
        "sint8": lambda x: int(x),
        "uint8": lambda x: int(x),
        "sint16": lambda x: int(x),
        "uint16": lambda x: int(x),
        "sint32": lambda x: int(x),
        "uint32": lambda x: int(x),
        "sint64": lambda x: int(x),
        "uint64": lambda x: int(x),
    }
    return _lmi_do_cast(t, value, cast)


def lmi_wrap_cim_namespace(conn, cim_namespace_name):
    """
    Helper function, which returns wrapped CIM namespace in
    :py:class:`.LMINamespace`.

    :param LMIConnection conn: connection object
    :param string cim_namespace_name: CIM namespace name
    :returns: wrapped CIM namespace into :py:class:`.LMINamespace`
    """
    return LMIObjectFactory().LMINamespace(conn, cim_namespace_name)


def lmi_wrap_cim_class(conn, cim_class_name, cim_namespace_name):
    """
    Helper function, which returns wrapped :py:class:`wbem.CIMClass` into
    :py:class:`.LMIClass`.

    :param LMIConnection conn: connection object
    :param string cim_class_name: string containing :py:class:`wbem.CIMClass`
        name
    :param string cim_namespace_name: string containing
        :py:class:`wbem.CIMNamespace` name, or None, if the namespace is not
        known
    :returns: wrapped :py:class:`wbem.CIMClass` into :py:class:`.LMIClass`
    """
    lmi_namespace = None
    if cim_namespace_name:
        lmi_namespace = lmi_wrap_cim_namespace(conn, cim_namespace_name)
    return LMIObjectFactory().LMIClass(conn, lmi_namespace, cim_class_name)


def lmi_wrap_cim_instance(conn, cim_instance, cim_class_name,
                          cim_namespace_name):
    """
    Helper function, which returns wrapped :py:class:`wbem.CIMInstance` into
    :py:class:`.LMIInstance`.

    :param LMIConnection conn: connection object
    :param CIMInstance cim_instance: :py:class:`wbem.CIMInstance` object to be
        wrapped
    :param string cim_class_name: :py:class:`wbem.CIMClass` name
    :param string cim_namespace_name: :py:class:`wbem.CIMNamespace` name, or
        None, if the namespace is not known
    :returns: wrapped :py:class:`wbem.CIMInstance` into
        :py:class:`.LMIInstance`
    """
    lmi_class = lmi_wrap_cim_class(conn, cim_class_name, cim_namespace_name)
    return LMIObjectFactory().LMIInstance(conn, lmi_class, cim_instance)


def lmi_wrap_cim_instance_name(conn, cim_instance_name):
    """
    Helper function, which returns wrapped :py:class:`wbem.CIMInstanceName`
    into :py:class:`.LMIInstanceName`.

    :param LMIConnection conn: connection object
    :param CIMInstanceName cim_instance_name: :py:class:`wbem.CIMInstanceName`
        object to be wrapped
    :returns: wrapped :py:class:`wbem.CIMInstanceName` into
        :py:class:`.LMIInstanceName`
    """
    return LMIObjectFactory().LMIInstanceName(conn, cim_instance_name)


def lmi_wrap_cim_method(conn, cim_method_name, lmi_instance):
    """
    Helper function, which returns wrapped :py:class:`wbem.CIMMethod` into
    :py:class:`.LMIMethod`.

    :param LMIConnection conn: connection object
    :param string cim_method_name: method name
    :param LMIInstance lmi_instance: object, on which the method call will be
        issued
    :returns: wrapped :py:class:`wbem.CIMMethod` into :py:class:`.LMIMethod`
    """
    return LMIObjectFactory().LMIMethod(conn, lmi_instance, cim_method_name)


def lmi_transform_to_lmi(conn, value):
    """
    Transforms returned values from a method call into LMI wrapped objects.
    Returns transformed input, where :py:class:`wbem.CIMInstance` and
    :py:class:`wbem.CIMInstanceName` are wrapped into LMI wrapper classes and
    primitive types are cast to python native types.

    :param LMIConnection conn: connection object
    :param value: object to be transformed into :py:mod:`python` type from
        :mod:`wbem` one
    :returns: transformed py::mod:`wbem` object into LMIShell one
    """
    if isinstance(value, wbem.CIMInstance):
        namespace = value.path.namespace if value.path else None
        return lmi_wrap_cim_instance(conn, value, value.classname, namespace)
    elif isinstance(value, wbem.CIMInstanceName):
        return lmi_wrap_cim_instance_name(conn, value)
    elif isinstance(value, wbem.CIMInt):
        return int(value)
    elif isinstance(value, wbem.CIMFloat):
        return float(value)
    elif isinstance(value, (dict, wbem.NocaseDict)):
        return wbem.NocaseDict(
            dict(
                (k, lmi_transform_to_lmi(conn, v))
                for k, v in value.iteritems()))
    elif isinstance(value, list):
        return [lmi_transform_to_lmi(conn, val) for val in value]
    elif isinstance(value, tuple):
        return (lmi_transform_to_lmi(conn, val) for val in value)
    return value


def lmi_transform_to_cim_param(t, value):
    """
    Helper function for method calls, which transforms input object into
    :py:class:`wbem.CIMInstanceName` object. Members if lists, dictionaries and
    tuples are transformed as well. The function does not cast numeric types.

    :param string t: string of CIM type
    :param value: object to be transformed to :py:mod:`wbem` type.
    :returns: transformed LMIShell's object into :py:mod:`wbem` one
    """
    if isinstance(value, LMIObjectFactory().LMIInstance):
        return value.wrapped_object.path
    elif isinstance(value, LMIObjectFactory().LMIInstanceName):
        return value.wrapped_object
    elif isinstance(value, (dict, wbem.NocaseDict)):
        return wbem.NocaseDict(
            dict(
                (k, lmi_transform_to_cim_param(t, val))
                for k, val in value.iteritems()))
    elif isinstance(value, list):
        return [lmi_transform_to_cim_param(t, val) for val in value]
    elif isinstance(value, tuple):
        return (lmi_transform_to_cim_param(t, val) for val in value)
    return lmi_cast_to_cim(t, value)


def lmi_isinstance(lmi_obj, lmi_class):
    """
    Function returns True if :samp:`lmi_obj` is an instance of a
    :samp:`lmi_class`, False otherwise. When passed :py:class:`.LMIInstance`,
    :py:class:`.LMIInstanceName` as :samp:`lmi_obj` and :samp:`lmi_class` is of
    :py:class:`.LMIClass` type, function can tell, if such :samp:`lmi_obj` is
    direct instance of :py:class:`.LMIClass`, or it's super class.

    If :samp:`lmi_obj` and :samp:`lmi_class` is not instance of mentioned
    classes, an exception will be raised.

    :param lmi_obj: instance of :py:class:`.LMIInstance` or
        :py:class:`.LMIInstanceName` which is checked, if such instance is
        instance of the ``lmi_class``
    :param LMIClass lmi_class: instance of :py:class:`.LMIClass` object
    :returns: whether **lmi_obj** is instance of **lmi_class**
    :rtype: bool
    :raises: :py:exc:`TypeError`
    """
    cls = (
        LMIObjectFactory().LMIInstance,
        LMIObjectFactory().LMIInstanceName)
    if not isinstance(lmi_obj, cls) or \
            not isinstance(lmi_class, LMIObjectFactory().LMIClass):
        errorstr = "Use with types LMIInstance/LMIInstanceName and LMIClass"
        lmi_raise_or_dump_exception(TypeError(errorstr))
        return False
    client = lmi_obj._conn.client
    classname = lmi_obj.classname
    namespace = lmi_obj.namespace
    while classname:
        if classname == lmi_class.classname:
            return True
        classname, _, errorstr = client.get_superclass(classname, namespace)
    return False


def lmi_associators(assoc_classes):
    """
    Helper function to speed up associator traversal. Returns a list of tuples,
    where each tuple contains :py:class:`.LMIInstance` objects, which are in
    association.

    :param list assoc_classes: list of :py:class:`.LMIClass` objects, for which
        the associations will be returned
    :returns: list of tuples of :py:class:`.LMIInstance` objects in association
    """
    def make_key(path):
        path.host = None
        sum = hashlib.md5(
            path.classname.lower() + path.namespace.lower() +
            str(dict((k.lower(), v) for k, v in path.keybindings.iteritems())))
        return sum.hexdigest()

    result = []

    instances = {}
    for assoc_class in assoc_classes:
        conn = assoc_class._conn
        assoc_class.fetch()

        # Reference properties
        ref_props = [
            pname
            for pname, prop in assoc_class._cim_class.properties.iteritems()
            if prop.type == "reference"
        ]

        # Reference class names
        ref_class_names = [
            assoc_class._cim_class.properties[ref_prop].reference_class
            for ref_prop in ref_props
        ]

        # Get instances, which will be joined as associators
        for ref_class_name in ref_class_names:
            inst_list, out, err = conn.client.get_instances(ref_class_name)
            instances.update(
                dict((make_key(inst.path), inst) for inst in inst_list))

        # Join associated objects
        assoc_instance_names, out, err = conn.client.get_instance_names(
            assoc_class.classname)
        for assoc in assoc_instance_names:
            ref_list = []
            for ref_prop in ref_props:
                path = assoc[ref_prop]
                # XXX: Some association classes report in key property a class,
                # which its instances do not refer to.
                inst = instances.get(make_key(path), None)
                if inst:
                    ref_list.append(
                        lmi_wrap_cim_instance(
                            conn, inst, inst.classname, inst.path.namespace))

            if len(ref_list) == len(ref_class_names):
                result.append(tuple(ref_list))

    return result


def lmi_instance_to_path(instance):
    """
    Helper function, which returns :py:class:`wbem.CIMInstanceName` extracted
    out of input instance.

    :param instance: object, which can be instance of following classes:

        * :py:class:`wbem.CIMInstance`
        * :py:class:`wbem.CIMInstanceName`
        * :py:class:`.LMIInstance`
        * :py:class:`.LMIInstanceName`

    :returns: extracteed :py:class:`wbem.CIMInstanceName` object
    :raises: :py:exc:`TypeError`
    """
    if isinstance(instance, wbem.CIMInstance):
        return instance.path
    elif isinstance(instance, wbem.CIMInstanceName):
        return instance
    elif isinstance(instance, LMIObjectFactory().LMIInstance):
        return instance.wrapped_object.path
    elif isinstance(instance, LMIObjectFactory().LMIInstanceName):
        return instance.wrapped_object
    raise TypeError(
        "instance has to be wbem.CIMInstance(Name) or LMIInstance(Name)")

def lmi_is_localhost(uri):
    """
    Helper function, which returns True, if URI points to localhost.

    :param str uri: URI to check
    """
    return uri in LOCALHOST_VARIANTS
