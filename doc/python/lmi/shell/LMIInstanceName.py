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

from lmi.shell.LMIObjectFactory import LMIObjectFactory
from lmi.shell.LMIBaseObject import LMIWrapperBaseObject
from lmi.shell.LMIDecorators import lmi_instance_name_fetch_lazy
from lmi.shell.LMIDecorators import lmi_possibly_deleted
from lmi.shell.LMIUtil import lmi_transform_to_lmi
from lmi.shell.LMIUtil import lmi_wrap_cim_method


class LMIInstanceName(LMIWrapperBaseObject):
    """
    LMI wrapper class representing :py:class:`wbem.CIMInstanceName`.

    :param LMIConnection conn: connection object
    :param CIMInstanceName cim_instance_name: wrapped object
    """
    def __init__(self, conn, cim_instance_name):
        if isinstance(cim_instance_name, LMIInstanceName):
            cim_instance_name = cim_instance_name.wrapped_object
        # We use __dict__ to avoid recursion potentially caused by
        # combo __setattr__ and __getattr__
        self.__dict__["_cim_instance_name"] = cim_instance_name
        self.__dict__["_deleted"] = False
        self.__dict__["_lmi_class"] = None
        super(LMIInstanceName, self).__init__(conn)

    def __cmp__(self, other):
        """
        :param LMIInstanceName other: :py:class:`.LMIInstanceName` object to
            compare
        :returns: negative number, if self < other; 0 if self == other or
            positive number, if self > other
        :rtype: int
        """
        if not isinstance(other, LMIInstanceName):
            return -1
        if self._deleted and not other._deleted:
            return -1
        elif not self._deleted and other._deleted:
            return 1
        return cmp(self._cim_instance_name, other._cim_instance_name)

    @lmi_possibly_deleted(False)
    def __contains__(self, key):
        """
        :param string key: key name, which will be tested for presence in
            keybindings
        :returns: True, if the specified key is present in keybindings, False
            otherwise
        :raises: :py:exc:`.LMIDeletedObjectError`

        **NOTE:** If the method :py:meth:`.LMIInstanceName.delete` was called,
        this method will not execute its code and will return False. If the
        shell uses exceptions, :py:exc:`.LMIDeletedObjectError` will be raised.
        """
        return key in self._cim_instance_name

    @lmi_possibly_deleted(None)
    def __getattr__(self, name):
        """
        Returns class member or key property.

        :param string name: class member or key property name
        :returns: class member or key property
        :raises: :py:exc:`AttributeError`, :py:exc:`.LMIDeletedObjectError`

        **NOTE:** If the method :py:meth:`.LMIInstanceName.delete` was called,
        this method will not execute its code and will return None. If the
        shell uses exceptions, :py:exc:`.LMIDeletedObjectError` will be raised.
        """
        if name in self._cim_instance_name:
            member = self._cim_instance_name[name]
            if isinstance(member, wbem.CIMInstanceName):
                member = lmi_transform_to_lmi(self._conn, member)
            return member
        elif not self._conn.is_wsman() and name in self.methods():
            return lmi_wrap_cim_method(self._conn, name, self)
        elif self._conn.is_wsman() and not name.startswith("_"):
            return lmi_wrap_cim_method(self._conn, name, self)
        raise AttributeError(name)

    @lmi_possibly_deleted(None)
    def __setattr__(self, name, value):
        """
        Assigns a new value to class member or key property.

        :param string name: class member or key property name
        :param value: new value to assign
        :raises: :py:exc:`.LMIDeletedObjectError`

        **NOTE:** If the method :py:meth:`.LMIInstanceName.delete` was called,
        this method will not execute its code and will return None. If the
        shell uses exceptions, :py:exc:`.LMIDeletedObjectError` will be raised.
        """
        if name in self._cim_instance_name.keys():
            if isinstance(value, str):
                # Convert string value into unicode
                value = unicode(value, "utf-8")
            elif isinstance(
                    value,
                    (LMIObjectFactory().LMIInstanceName,
                     LMIObjectFactory().LMIInstance)):
                # Unpack wrapped LMI object
                value = value.wrapped_object
            self._cim_instance_name[name] = value
        else:
            self.__dict__[name] = value

    @lmi_possibly_deleted("")
    def __str__(self):
        """
        :returns: string containing object path
        :raises: :py:exc:`.LMIDeletedObjectError`

        **NOTE:** If the method :py:meth:`.LMIInstanceName.delete` was called,
        this method will not execute its code and will return an empty string.
        If the shell uses exceptions, :py:exc:`.LMIDeletedObjectError` will be
        raised.
        """
        return unicode(self).encode("utf-8")

    @lmi_possibly_deleted(u"")
    def __unicode__(self):
        """
        :returns: unicode string containing object path
        :raises: :py:exc:`.LMIDeletedObjectError`

        **NOTE:** If the method :py:meth:`.LMIInstanceName.delete` was called,
        this method will not execute its code and will return an empty unicode
        string. If the shell uses exceptions, :py:exc:`.LMIDeletedObjectError`
        will be raised.
        """
        return unicode(self._cim_instance_name)

    @lmi_possibly_deleted("")
    def __repr__(self):
        """
        :returns: pretty string for the object
        :raises: :py:exc:`.LMIDeletedObjectError`

        **NOTE:** If the method :py:meth:`.LMIInstanceName.delete` was called,
        this method will not execute its code and will return an empty string.
        If the shell uses exceptions, :py:exc:`.LMIDeletedObjectError` will be
        raised.
        """
        return "%s(classname=\"%s\"...)" % (
            self.__class__.__name__,
            self.classname)

    @lmi_possibly_deleted([])
    def associator_names(self, AssocClass=None, ResultClass=None, Role=None,
                         ResultRole=None):
        """
        Returns a list of associated :py:class:`.LMIInstanceName` with this
        object.

        :param string AssocClass: valid CIM association class name. It acts as
            a filter on the returned set of names by mandating that each
            returned name identify an object that shall be associated to the
            source object through an instance of this class or one of its
            subclasses.
        :param string ResultClass: valid CIM class name. It acts as a filter on
            the returned set of names by mandating that each returned name
            identify an object that shall be either an instance of this class
            (or one of its subclasses) or be this class (or one of its
            subclasses).
        :param string Role: valid property name. It acts as a filter on the
            returned set of names by mandating that each returned name identify
            an object that shall be associated to the source object through an
            association in which the source object plays the specified role.
            That is, the name of the property in the association class that
            refers to the source object shall match the value of this
            parameter.
        :param string ResultRole: valid property name. It acts as a filter on
            the returned set of names by mandating that each returned name
            identify an object that shall be associated to the source object
            through an association in which the named returned object plays the
            specified role. That is, the name of the property in the
            association class that refers to the returned object shall match
            the value of this parameter.
        :returns: list of associated :py:class:`.LMIInstanceName` objects
        :raises: :py:exc:`.LMIDeletedObjectError`

        **NOTE:** If the method :py:meth:`.LMIInstanceName.delete` was called,
        this method will not execute its code and will return an empty list. If
        the shell uses exceptions, :py:exc:`.LMIDeletedObjectError` will be
        raised.

        **Usage:** :ref:`associators_instance_names`.
        """
        assoc_names = self._conn.client.get_associator_names(
            self._cim_instance_name, AssocClass, ResultClass, Role, ResultRole)
        return lmi_transform_to_lmi(self._conn, assoc_names)

    @lmi_possibly_deleted(None)
    def first_associator_name(self, AssocClass=None, ResultClass=None,
                              Role=None, ResultRole=None):
        """
        Returns the first associated :py:class:`.LMIInstanceName` with this
        object.

        :param string AssocClass: valid CIM association class name. It acts as
            a filter on the returned set of names by mandating that each
            returned name identify an object that shall be associated to the
            source object through an instance of this class or one of its
            subclasses.
        :param string ResultClass: valid CIM class name. It acts as a filter on
            the returned set of names by mandating that each returned name
            identify an object that shall be either an instance of this class
            (or one of its subclasses) or be this class (or one of its
            subclasses).
        :param string Role: valid property name. It acts as a filter on the
            returned set of names by mandating that each returned name identify
            an object that shall be associated to the source object through an
            association in which the source object plays the specified role.
            That is, the name of the property in the association class that
            refers to the source object shall match the value of this
            parameter.
        :param string ResultRole: valid property name. It acts as a filter on
            the returned set of names by mandating that each returned name
            identify an object that shall be associated to the source object
            through an association in which the named returned object plays the
            specified role. That is, the name of the property in the
            association class that refers to the returned object shall match
            the value of this parameter.
        :returns: first associated :py:class:`.LMIInstanceName` object
        :raises: :py:exc:`.LMIDeletedObjectError`

        **NOTE:** If the method :py:meth:`.LMIInstanceName.delete` was called,
        this method will not execute its code and will return None. If the
        shell uses exceptions, :py:exc:`.LMIDeletedObjectError` will be raised.

        **Usage:** :ref:`associators_instance_names`.
        """
        assoc_names = self._conn.client.get_associator_names(
            self._cim_instance_name, AssocClass, ResultClass, Role, ResultRole,
            limit=1)
        if not assoc_names:
            return None
        return lmi_transform_to_lmi(self._conn, assoc_names[0])

    @lmi_possibly_deleted([])
    def associators(self, AssocClass=None, ResultClass=None, Role=None,
                    ResultRole=None, IncludeQualifiers=False,
                    IncludeClassOrigin=False, PropertyList=None):
        """
        Returns a list of associated :py:class:`.LMIInstance` objects with this
        instance.

        :param string AssocClass: valid CIM association class name. It acts as
            a filter on the returned set of objects by mandating that each
            returned object shall be associated to the source object through an
            instance of this class or one of its subclasses.
        :param string ResultClass: valid CIM class name. It acts as a filter on
            the returned set of objects by mandating that each returned object
            shall be either an instance of this class (or one of its
            subclasses) or be this class (or one of its subclasses).
        :param string Role: valid property name. It acts as a filter on the
            returned set of objects by mandating that each returned object
            shall be associated with the source object through an association
            in which the source object plays the specified role. That is, the
            name of the property in the association class that refers to the
            source object shall match the value of this parameter.
        :param string ResultRole: valid property name. It acts as a filter on
            the returned set of objects by mandating that each returned object
            shall be associated to the source object through an association in
            which the returned object plays the specified role. That is, the
            name of the property in the association class that refers to the
            returned object shall match the value of this parameter.
        :param bool IncludeQualifiers: bool flag indicating, if all qualifiers
            for each object (including qualifiers on the object and on any
            returned properties) shall be included as ``<QUALIFIER>`` elements
            in the response.
        :param bool IncludeClassOrigin: bool flag indicating, if the
            ``CLASSORIGIN`` attribute shall be present on all appropriate
            elements in each returned object.
        :param list PropertyList: if not None, the members of the array define
            one or more property names. Each returned object shall not include
            elements for any properties missing from this list. If
            *PropertyList* is an empty list, no properties are included in each
            returned object.  If it is None, no additional filtering is
            defined.
        :returns: list of associated :py:class:`.LMIInstance` objects
        :raises: :py:exc:`.LMIDeletedObjectError`

        **NOTE:** If the method :py:meth:`.LMIInstanceName.delete` was called,
        this method will not execute its code and will return an empty list. If
        the shell uses exceptions, :py:exc:`.LMIDeletedObjectError` will be
        raised.

        **Usage:** :ref:`associators_instances`.
        """
        associators = self._conn.client.get_associators(
            self._cim_instance_name, AssocClass, ResultClass, Role, ResultRole,
            IncludeQualifiers, IncludeClassOrigin, PropertyList)
        return lmi_transform_to_lmi(self._conn, associators)

    @lmi_possibly_deleted(None)
    def first_associator(self, AssocClass=None, ResultClass=None, Role=None,
                         ResultRole=None, IncludeQualifiers=False,
                         IncludeClassOrigin=False, PropertyList=None):
        """
        Returns the first associated :py:class:`.LMIInstance` with this object.

        :param string AssocClass: valid CIM association class name. It acts as
            a filter on the returned set of objects by mandating that each
            returned object shall be associated to the source object through an
            instance of this class or one of its subclasses.
        :param string ResultClass: valid CIM class name. It acts as a filter on
            the returned set of objects by mandating that each returned object
            shall be either an instance of this class (or one of its
            subclasses) or be this class (or one of its subclasses).
        :param string Role: valid property name. It acts as a filter on the
            returned set of objects by mandating that each returned object
            shall be associated with the source object through an association
            in which the source object plays the specified role. That is, the
            name of the property in the association class that refers to the
            source object shall match the value of this parameter.
        :param string ResultRole: valid property name. It acts as a filter on
            the returned set of objects by mandating that each returned object
            shall be associated to the source object through an association in
            which the returned object plays the specified role. That is, the
            name of the property in the association class that refers to the
            returned object shall match the value of this parameter.
        :param bool IncludeQualifiers: bool flag indicating, if all qualifiers
            for each object (including qualifiers on the object and on any
            returned properties) shall be included as ``<QUALIFIER>`` elements
            in the response.
        :param bool IncludeClassOrigin: bool flag indicating, if the
            ``CLASSORIGIN`` attribute shall be present on all appropriate
            elements in each returned object.
        :param list PropertyList: if not None, the members of the array define
            one or more property names. Each returned object shall not include
            elements for any properties missing from this list. If PropertyList
            is an empty list, no properties are included in each returned
            object. If it is None, no additional filtering is defined.
        :returns: first associated :py:class:`.LMIInstance`
        :raises: :py:exc:`.LMIDeletedObjectError`

        **NOTE:** If the method :py:meth:`.LMIInstanceName.delete` was called,
        this method will not execute its code and will return None. If the
        shell uses exceptions, :py:exc:`.LMIDeletedObjectError` will be raised.

        **Usage:** :ref:`associators_instances`.
        """
        associators = self._conn.client.get_associators(
            self._cim_instance_name, AssocClass, ResultClass, Role, ResultRole,
            IncludeQualifiers, IncludeClassOrigin, PropertyList, limit=1)
        if not associators:
            return None
        return lmi_transform_to_lmi(self._conn, associators[0])

    @lmi_possibly_deleted([])
    def reference_names(self, ResultClass=None, Role=None):
        """
        Returns a list of association :py:class:`.LMIInstanceName` objects with
        this object.

        :param string ResultClass: valid CIM class name. It acts as a filter on
            the returned set of object names by mandating that each returned
            Object Name identify an instance of this class (or one of its
            subclasses) or this class (or one of its subclasses).
        :param string Role: valid property name. It acts as a filter on the
            returned set of object names by mandating that each returned object
            name shall identify an object that refers to the target instance
            through a property with a name that matches the value of this
            parameter.
        :returns: list of association :py:class:`.LMIInstanceName` objects
        :raises: :py:exc:`.LMIDeletedObjectError`

        **NOTE:** If the method :py:meth:`.LMIInstanceName.delete` was called,
        this method will not execute its code and will return an empty list. If
        the shell uses exceptions, :py:exc:`.LMIDeletedObjectError` will be
        raised.

        **Usage:** :ref:`references_instance_names`.
        """
        reference_names = self._conn.client.get_reference_names(
            self._cim_instance_name, ResultClass, Role)
        return lmi_transform_to_lmi(self._conn, reference_names)

    @lmi_possibly_deleted(None)
    def first_reference_name(self, ResultClass=None, Role=None):
        """
        Returns the first association :py:class:`.LMIInstanceName` with this
        object.

        :param string ResultClass: valid CIM class name. It acts as a filter on
            the returned set of object names by mandating that each returned
            Object Name identify an instance of this class (or one of its
            subclasses) or this class (or one of its subclasses).
        :param string Role: valid property name. It acts as a filter on the
            returned set of object names by mandating that each returned object
            name shall identify an object that refers to the target instance
            through a property with a name that matches the value of this
            parameter.
        :returns: first association :py:class:`.LMIInstanceName` object
        :raises: :py:exc:`.LMIDeletedObjectError`

        **NOTE:** If the method :py:meth:`.LMIInstanceName.delete` was called,
        this method will not execute its code and will return None. If the
        shell uses exceptions, :py:exc:`.LMIDeletedObjectError` will be raised.

        **Usage:** :ref:`references_instance_names`.
        """
        reference_names = self._conn.client.get_reference_names(
            self._cim_instance_name, ResultClass, Role, limit=1)
        if not reference_names:
            return None
        return lmi_transform_to_lmi(self._conn, reference_names[0])

    @lmi_possibly_deleted([])
    def references(self, ResultClass=None, Role=None, IncludeQualifiers=False,
                   IncludeClassOrigin=False, PropertyList=None):
        """
        Returns a list of association :py:class:`.LMIInstance` objects with
        this object.

        :param string ResultClass: valid CIM class name. It acts as a filter on
            the returned set of objects by mandating that each returned object
            shall be an instance of this class (or one of its subclasses) or
            this class (or one of its subclasses).
        :param string Role: valid property name. It acts as a filter on the
            returned set of objects by mandating that each returned object
            shall refer to the target object through a property with a name
            that matches the value of this parameter.
        :param bool IncludeQualifiers: flag indicating, if all qualifiers for
            each object (including qualifiers on the object and on any returned
            properties) shall be included as ``<QUALIFIER>`` elements in the
            response.
        :param bool IncludeClassOrigin: flag indicating, if the ``CLASSORIGIN``
            attribute shall be present on all appropriate elements in each
            returned object.
        :param list PropertyList: if not None, the members of the list define
            one or more property names. Each returned object shall not include
            elements for any properties missing from this list. If PropertyList
            is an empty list, no properties are included in each returned
            object. If PropertyList is None, no additional filtering is
            defined.
        :returns: list of association :py:class:`.LMIInstance` objects
        :raises: :py:exc:`.LMIDeletedObjectError`

        **NOTE:** If the method :py:meth:`.LMIInstanceName.delete` was called,
        this method will not execute its code and will return an empty list. If
        the shell uses exceptions, :py:exc:`.LMIDeletedObjectError` will be
        raised.

        **Usage:** :ref:`references_instances`.
        """
        references = self._conn.client.get_references(
            self._cim_instance_name, ResultClass, Role, IncludeQualifiers,
            IncludeClassOrigin, PropertyList)
        return lmi_transform_to_lmi(self._conn, references)

    @lmi_possibly_deleted(None)
    def first_reference(self, ResultClass=None, Role=None,
                        IncludeQualifiers=False, IncludeClassOrigin=False,
                        PropertyList=None):
        """
        Returns the first association :py:class:`.LMIInstance` with this
        object.

        :param string ResultClass: valid CIM class name. It acts as a filter on
            the returned set of objects by mandating that each returned object
            shall be an instance of this class (or one of its subclasses) or
            this class (or one of its subclasses).
        :param string Role: valid property name. It acts as a filter on the
            returned set of objects by mandating that each returned object
            shall refer to the target object through a property with a name
            that matches the value of this parameter.
        :param bool IncludeQualifiers: flag indicating, if all qualifiers for
            each object (including qualifiers on the object and on any returned
            properties) shall be included as ``<QUALIFIER>`` elements in the
            response.
        :param bool IncludeClassOrigin: flag indicating, if the ``CLASSORIGIN``
            attribute shall be present on all appropriate elements in each
            returned object.
        :param list PropertyList: if not None, the members of the list define
            one or more property names. Each returned object shall not include
            elements for any properties missing from this list. If PropertyList
            is an empty list, no properties are included in each returned
            object. If PropertyList is None, no additional filtering is
            defined.
        :returns: first association :py:class:`.LMIInstance` object
        :raises: :py:exc:`.LMIDeletedObjectError`

        **NOTE:** If the method :py:meth:`.LMIInstanceName.delete` was called,
        this method will not execute its code and will return None. If the
        shell uses exceptions, :py:exc:`.LMIDeletedObjectError` will be raised.

        **Usage:** :ref:`references_instances`.
        """
        references = self._conn.client.get_references(
            self._cim_instance_name, ResultClass, Role, IncludeQualifiers,
            IncludeClassOrigin, PropertyList, limit=1)
        if not references:
            return None
        return lmi_transform_to_lmi(self._conn, references[0])

    def copy(self):
        """
        :returns: copy of itself
        """
        return lmi_transform_to_lmi(self._conn, self._cim_instance_name.copy())

    @lmi_possibly_deleted(True)
    def delete(self):
        """
        Deletes the instance defined by this object path from the CIMOM.

        :returns: True, if the instance is deleted; False otherwise
        :raises: :py:exc:`.LMIDeletedObjectError`

        **NOTE:** If the method :py:meth:`.LMIInstanceName.delete` was called,
        this method will not execute its code and will return True. If the
        shell uses exceptions, :py:exc:`.LMIDeletedObjectError` will be raised.

        **Usage:** :ref:`instance_names_delete`.
        """
        rval, _, _ = self._conn.client.delete_instance(
            self._cim_instance_name)
        self._deleted = rval
        return self._deleted

    @lmi_possibly_deleted(None)
    def to_instance(self):
        """
        Creates a new :py:class:`.LMIInstance` object from
        :py:class:`.LMIInstanceName`.

        :returns: :py:class:`.LMIInstance` object if the object was retrieved
            successfully; None otherwise.
        :raises: :py:exc:`.LMIDeletedObjectError`

        **NOTE:** If the method :py:meth:`.LMIInstanceName.delete` was called,
        this method will not execute its code and will return None. If the
        shell uses exceptions, :py:exc:`.LMIDeletedObjectError` will be raised.

        **Usage:** :ref:`instance_names_conversion`.
        """
        instance, _, _ = self._conn.client.get_instance(
            self._cim_instance_name, LocalOnly=False)
        if not instance:
            return None
        return lmi_transform_to_lmi(self._conn, instance)

    @lmi_possibly_deleted([])
    @lmi_instance_name_fetch_lazy()
    def methods(self):
        """
        Returns a list of :py:class:`wbem.CIMInstance` methods' names.

        :returns: list of :py:class:`wbem.CIMInstance` methods' names
        :raises: :py:exc:`.LMIDeletedObjectError`

        **NOTE:** If the method :py:meth:`.LMIInstanceName.delete` was called,
        this method will not execute its code and will return an empty list. If
        the shell uses exceptions, :py:exc:`.LMIDeletedObjectError` will be
        raised.

        **Usage:** :ref:`instances_methods`.
        """
        return self._lmi_class.methods()

    @lmi_possibly_deleted(None)
    @lmi_instance_name_fetch_lazy()
    def print_methods(self):
        """
        Prints out the list of :py:class:`wbem.CIMInstance` methods' names.

        :raises: :py:exc:`.LMIDeletedObjectError`

        **NOTE:** If the method :py:meth:`.LMIInstanceName.delete` was called,
        this method will not execute its code and will return None. If the
        shell uses exceptions, :py:exc:`.LMIDeletedObjectError` will be raised.

        **Usage:** :ref:`instances_methods`.
        """
        self._lmi_class.print_methods()

    @lmi_possibly_deleted([])
    def key_properties(self):
        """
        :returns: list of strings of key properties
        :raises: :py:exc:`.LMIDeletedObjectError`

        **NOTE:** If the method :py:meth:`.LMIInstanceName.delete` was called,
        this method will not execute its code and will return an empty list. If
        the shell uses exceptions, :py:exc:`.LMIDeletedObjectError` will be
        raised.

        **Usage:** :ref:`instance_names_key_properties`.
        """
        return self._cim_instance_name.keys()

    @lmi_possibly_deleted(None)
    def print_key_properties(self):
        """
        Prints out the list of key properties.

        :raises: :py:exc:`.LMIDeletedObjectError`

        **NOTE:** If the method :py:meth:`.LMIInstanceName.delete` was called,
        this method will not execute its code and will return None. If the
        shell uses exceptions, :py:exc:`.LMIDeletedObjectError` will be raised.

        **Usage:** :ref:`instance_names_key_properties`.
        """
        for name, key_prop in self._cim_instance_name.iteritems():
            value = str(key_prop)
            if isinstance(key_prop, basestring):
                value = "'%s'" % value
            sys.stdout.write("%s = %s\n" % (name, value))

    @lmi_possibly_deleted({})
    def key_properties_dict(self):
        """
        :returns: dictionary with key properties and corresponding values
        :raises: :py:exc:`.LMIDeletedObjectError`

        **NOTE:** If the method :py:meth:`.LMIInstanceName.delete` was called,
        this method will not execute its code and will return an empty
        dictionary. If the shell uses exceptions,
        :py:exc:`.LMIDeletedObjectError` will be raised.
        """
        return self._cim_instance_name.keybindings.copy()

    @lmi_possibly_deleted(None)
    def key_property_value(self, prop_name):
        """
        :param string prop_name: key property name
        :returns: key property value
        :raises: :py:exc:`.LMIDeletedObjectError`

        **NOTE:** If the method :py:meth:`.LMIInstanceName.delete` was called,
        this method will not execute its code and will return None. If the
        shell uses exceptions, :py:exc:`.LMIDeletedObjectError` will be raised.
        """
        return getattr(self, prop_name)

    @property
    @lmi_possibly_deleted("")
    def classname(self):
        """
        :returns: class name
        :rtype: string
        :raises: :py:exc:`.LMIDeletedObjectError`

        **NOTE:** If the method :py:meth:`.LMIInstanceName.delete` was called,
        this method will not execute its code and will return an empty string.
        If the shell uses exceptions, :py:exc:`.LMIDeletedObjectError` will be
        raised.
        """
        return self._cim_instance_name.classname

    @property
    @lmi_possibly_deleted("")
    def namespace(self):
        """
        :returns: namespace name
        :rtype: string
        :raises: :py:exc:`.LMIDeletedObjectError`

        **NOTE:** If the method :py:meth:`.LMIInstanceName.delete` was called,
        this method will not execute its code and will return an empty string.
        If the shell uses exceptions, :py:exc:`.LMIDeletedObjectError` will be
        raised.
        """
        return self._cim_instance_name.namespace

    @property
    @lmi_possibly_deleted("")
    def hostname(self):
        """
        :returns: host name
        :rtype: string
        :raises: :py:exc:`.LMIDeletedObjectError`

        **NOTE:** If the method :py:meth:`.LMIInstanceName.delete` was called,
        this method will not execute its code and will return an empty string.
        If the shell uses exceptions, :py:exc:`.LMIDeletedObjectError` will be
        raised.
        """
        return self._cim_instance_name.host

    @property
    def is_deleted(self):
        """
        :returns: True, if the instance was deleted from the CIMOM; False
            otherwise
        """
        return self._deleted

    @property
    @lmi_possibly_deleted(None)
    def wrapped_object(self):
        """
        :returns: wrapped :py:class:`wbem.CIMInstanceName` object
        :raises: :py:exc:`.LMIDeletedObjectError`

        **NOTE:** If the method :py:meth:`.LMIInstanceName.delete` was called,
        this method will not execute its code and will return None. If the
        shell uses exceptions, :py:exc:`.LMIDeletedObjectError` will be raised.
        """
        return self._cim_instance_name
