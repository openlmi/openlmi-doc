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
import urlparse

from lmi.shell.compat import *

from lmi.shell.LMIReturnValue import LMIReturnValue
from lmi.shell.LMIUtil import lmi_parse_uri
from lmi.shell.LMIUtil import lmi_raise_or_dump_exception
from lmi.shell.LMIUtil import lmi_get_use_exceptions
from lmi.shell.LMIUtil import lmi_set_use_exceptions
from lmi.shell.LMIUtil import lmi_instance_to_path
from lmi.shell.LMIUtil import lmi_is_localhost

from lmi.shell.LMIDecorators import lmi_wrap_cim_exceptions
from lmi.shell.LMIDecorators import lmi_wrap_cim_exceptions_rval

from lmi.shell.LMIExceptions import CIMError
from lmi.shell.LMIExceptions import ConnectionError
from lmi.shell.LMIExceptions import LMIFilterError


def filter_kwargs(**kwargs):
    return {k: v for k, v in kwargs.iteritems() if v is not None}


class LMICIMXMLClient(object):
    """
    CIM-XML client.

    :param string uri: URI of the CIMOM
    :param string username: account, under which, the CIM calls will be
        performed
    :param string password: user's password
    :param bool verify_server_cert: indicates, whether a server side
        certificate needs to be verified, if SSL used; default value is True
    :param string key_file: path to x509 key file; default value is None
    :param string cert_file: path to x509 cert file; default value is None
    """
    QUERY_LANG_CQL = "DMTF:CQL"
    QUERY_LANG_WQL = "WQL"

    # Unix sockets used by TOG-Pegasus, SFCB or OpenWBEM.
    PEGASUS_SOCKET = "/var/run/tog-pegasus/cimxml.socket"

    def __init__(self, uri, username="", password="",
                 verify_server_cert=True,
                 key_file=None, cert_file=None):
        self._uri = uri
        if not self._uri.startswith("http://") and \
                not self._uri.startswith("https://"):
            self._uri = "https://" + uri

        # Parse CIMOM URI
        _, hostname, _, path, username_, password_ = lmi_parse_uri(self._uri)
        if username_ is not None:
            username = username_
            password = password_

        creds = (username, password)
        x509 = {
            "cert_file": cert_file,
            "key_file": key_file
        }

        # If we are connecting to localhost without username or certificate
        # set, we will use the local UNIX socket for higher performance (and
        # skip authentication).
        connect_locally = lmi_is_localhost(uri) and \
            path != "/wsman" and \
            not username and not password and \
            not cert_file and not key_file

        if HAVE_LMIWBEM:
            # LMIWBEM
            self._cliconn = wbem.WBEMConnection(
                self._uri,
                creds=creds,
                x509=x509,
                no_verification=not verify_server_cert,
                connect_locally=connect_locally)
        else:
            # PyWBEM
            if connect_locally:
                self._cliconn = wbem.PegasusUDSConnection()
            else:
                self._cliconn = wbem.WBEMConnection(
                    self._uri,
                    creds=creds,
                    x509=x509,
                    no_verification=not verify_server_cert)

                # LMIWBEM defines hostname attribute, so we define it here,
                # as well.
                self._cliconn.hostname = hostname

    def __del__(self):
        """
        Disconnects and frees :py:class:`WBEMConnection` object.

        **NOTE:** Applicable only wbem :py:mod:`lmiwbem` is used.
        """
        if HAVE_LMIWBEM:
            self.disconnect()
            del self._cliconn

    @lmi_wrap_cim_exceptions(False)
    def connect(self):
        """
        Connects to CIMOM.

        **NOTE:** Applicable only wbem :py:mod:`lmiwbem` is used.
        """
        if HAVE_LMIWBEM:
            self._cliconn.connect()
        return LMIReturnValue(rval=True)

    def disconnect(self):
        """
        Disconnects from CIMOM.

        **NOTE:** Applicable only wbem :py:mod:`lmiwbem` is used.
        """
        if HAVE_LMIWBEM:
            self._cliconn.disconnect()

    def dummy(self):
        """
        Sends a "dummy" request to verify credentials.

        :returns: :py:class:`.LMIReturnValue` with rval set to True, if
            provided credentials are OK; False otherwise. If LMIShell uses
            exceptions, :py:exc:`.CIMError` or :py:exc:`.ConnectionError` will
            be raised.
        :raises: :py:exc:`.CIMError`, :py:exc:`.ConnectionError`
        """
        try:
            use_exceptions = lmi_get_use_exceptions()
            lmi_set_use_exceptions(True)
            try:
                # Perform a dummy request
                self.get_class("SomeNonExistingClass")
            except:
                raise
            finally:
                lmi_set_use_exceptions(use_exceptions)
        except CIMError, e:
            if e.args[0] == wbem.CIM_ERR_NOT_FOUND:
                return LMIReturnValue(rval=True)
            lmi_raise_or_dump_exception(e)
            errorstr = e.args[1]
        except ConnectionError, e:
            lmi_raise_or_dump_exception(e)
            errorstr = e.args[1]

        return LMIReturnValue(rval=False, errorstr=errorstr)

    # NOTE: usage with Key=something, Value=something is deprecated
    # NOTE: inst_filter is either None or dict
    def get_instance_names(self, classname, namespace=None, inst_filter=None,
                           limit=-1, **kwargs):
        """
        Returns a list of :py:class:`wbem.CIMInstanceName` objects.

        :param string classname: class name
        :param string namespace: namespace name, where the instance names live
        :param dictionary inst_filter: dictionary containing filter values. The
            key corresponds to the primary key of the
            :py:class:`wbem.CIMInstanceName`; value contains the filtering
            value.
        :param int limit: unused
        :param dictionary kwargs: supported keyword arguments (these are
            **deprecated**)

            * **Key** or **key** (*string*) -- filtering key, see above
            * **Value** or **value** (*string*) -- filtering value, see above

        :returns: :py:class:`.LMIReturnValue` object with ``rval`` contains a
            list of :py:class:`wbem.CIMInstanceName` objects, if no error
            occurs; otherwise ``rval`` is set to None and ``errorstr`` contains
            appropriate error string
        :raises: :py:exc:`.LMIFilterError`, :py:exc:`.CIMError`,
            :py:exc:`.ConnectionError`
        """
        @lmi_wrap_cim_exceptions(prefix="EnumerateInstanceNames " + classname)
        def get_instance_names_core(classname, namespace):
            return LMIReturnValue(
                rval=self._cliconn.EnumerateInstanceNames(
                    classname, namespace))

        filter_value = ""
        filter_key = "Name"
        if inst_filter is None:
            inst_filter = {}
        if "key" in kwargs:
            filter_key = kwargs["key"]
            kwargs.pop("key")
        elif "Key" in kwargs:
            filter_key = kwargs["Key"]
            kwargs.pop("Key")
        if "value" in kwargs:
            filter_value = kwargs["value"]
            kwargs.pop("value")
        if "Value" in kwargs:
            filter_value = kwargs["Value"]
            kwargs.pop("Value")
        if filter_value:
            inst_filter[filter_key] = filter_value
        try:
            inst_name_list, _, errorstr = get_instance_names_core(
                classname, namespace)
            if inst_filter:
                inst_name_list_filtered = []
                for inst_name in inst_name_list:
                    append = True
                    for filter_key, filter_value in inst_filter.iteritems():
                        if inst_name[filter_key] != filter_value:
                            append = False
                            break
                    if append:
                        inst_name_list_filtered.append(inst_name)
                inst_name_list = inst_name_list_filtered
        except KeyError, e:
            errorstr = "Can not filter by '%s'" % filter_key
            lmi_raise_or_dump_exception(LMIFilterError(errorstr))
            return LMIReturnValue(rval=None, errorstr=errorstr)
        return LMIReturnValue(rval=inst_name_list, errorstr=errorstr)

    def get_instance(self, instance, LocalOnly=True, IncludeQualifiers=False,
                     IncludeClassOrigin=False, PropertyList=None):
        """
        Returns a :py:class:`wbem.CIMInstance` object.

        :param path: path of the object, which is about to be retrieved. The
            object needs to be instance of following classes:

            * :py:class:`wbem.CIMInstanceName`
            * :py:class:`wbem.CIMInstance`
            * :py:class:`.LMIInstanceName`
            * :py:class:`.LMIInstance`

        :param bool LocalOnly: indicates if to include the only elements
            (properties, methods, references) overridden or defined in the
            class
        :param bool IncludeQualifiers: indicates, if all Qualifiers for the
            class and its elements shall be included in the response
        :param bool IncludeClassOrigin: indicates, if the ``CLASSORIGIN``
            attribute shall be present on all appropriate elements in the
            returned class
        :param list PropertyList: if present and not None, the members of the
            list define one or more property names. The returned class shall
            not include elements for properties missing from this list. Note
            that if LocalOnly is specified as True, it acts as an additional
            filter on the set of properties returned. For example, if property
            A is included in the PropertyList but LocalOnly is set to True and
            A is not local to the requested class, it is not included in the
            response. If the PropertyList input parameter is an empty list, no
            properties are included in the response. If the PropertyList input
            parameter is None, no additional filtering is defined.
        :returns: :py:class:`.LMIReturnValue` object, where ``rval`` is set to
            :py:class:`wbem.CIMInstance` object, if no error occurs; otherwise
            ``rval`` is set to None and ``errorstr`` is set to corresponding
            error string.
        :raises: :py:exc:`.CIMError`, :py:exc:`.ConnectionError`,
            :py:exc:`TypeError`
        """
        @lmi_wrap_cim_exceptions(prefix="GetInstance " + instance.classname)
        def get_instance_core(path, **kwargs):
            return LMIReturnValue(
                rval=self._cliconn.GetInstance(path, **kwargs))

        return get_instance_core(
            lmi_instance_to_path(instance),
            **filter_kwargs(
                LocalOnly=LocalOnly,
                IncludeQualifiers=IncludeQualifiers,
                IncludeClassOrigin=IncludeClassOrigin,
                PropertyList=PropertyList))

    # NOTE: usage with Key=something, Value=something is deprecated
    # NOTE: inst_filter is either None or dict
    def get_instances(self, classname, namespace=None, inst_filter=None,
                      client_filtering=False, limit=-1, **kwargs):
        """
        Returns a list of :py:class:`wbem.CIMInstance` objects.

        :param string classname: class name
        :param string namespace: namespace, where the instances live
        :param dictionary inst_filter: dictionary containing filter values. The
            key corresponds to the primary key of the
            :py:class:`wbem.CIMInstanceName`; value contains the filtering
            value.
        :param bool client_filtering: if True, client-side filtering will be
            performed, otherwise the filtering will be done by a CIMOM. Default
            value is False.
        :param int limit: unused
        :param dictionary kwargs: supported keyword arguments (these are
            **deprecated**)

            * **Key** or **key** (*string*) -- filtering key, see above
            * **Value** or **value** (*string*) -- filtering value, see above

        :returns: :py:class:`.LMIReturnValue` object with ``rval`` set to a
            list of :py:class:`wbem.CIMIntance` objects, if no error occurs;
            otherwise ``rval`` is set to None and ``errorstr`` is set to
            corresponding error string.
        :raises: :py:exc:`.CIMError`, :py:exc:`.ConnectionError`
        """
        @lmi_wrap_cim_exceptions([], prefix="EnumerateInstances " + classname)
        def get_instances_core(classname, namespace, **kwargs):
            return LMIReturnValue(
                rval=self._cliconn.EnumerateInstances(
                    classname, namespace, **kwargs))

        filter_value = ""
        filter_key = "Name"
        if inst_filter is None:
            inst_filter = {}
        if "key" in kwargs:
            filter_key = kwargs["key"]
            kwargs.pop("key")
        elif "Key" in kwargs:
            filter_key = kwargs["Key"]
            kwargs.pop("Key")
        if "value" in kwargs:
            filter_value = kwargs["value"]
            kwargs.pop("value")
        if "Value" in kwargs:
            filter_value = kwargs["Value"]
            kwargs.pop("Value")
        if filter_value:
            inst_filter[filter_key] = filter_value

        if not client_filtering:
            query = "select * from %s" % classname
            if inst_filter:
                more = False
                query += " where"
                for filter_key, filter_value in inst_filter.iteritems():
                    if more:
                        query += " and"
                    quotes = isinstance(filter_value, basestring)
                    query += " %s =" % filter_key
                    if quotes:
                        query += " \"%s\"" % filter_value
                    else:
                        query += " %s" % filter_value
                    more = True
            return self.exec_query(
                LMICIMXMLClient.QUERY_LANG_WQL, query, namespace)

        # Client-side filtering - this is not a pretty solution, but it needs
        # to be present due to TOG-Pegasus, which does not raise an exception,
        # if an error occurs while performing CQL/WQL query.
        inst_list, _, errorstr = get_instances_core(
            classname,
            namespace,
            LocalOnly=False,
            DeepInheritance=True,
            IncludeQualifiers=False)

        if inst_list and inst_filter:
            inst_list_filtered = []
            for inst in inst_list:
                for filter_key, filter_value in inst_filter.iteritems():
                    if filter_key not in inst.properties or \
                            inst.properties[filter_key].value != filter_value:
                        break
                else:
                    inst_list_filtered.append(inst)
            inst_list = inst_list_filtered
        return LMIReturnValue(rval=inst_list, errorstr=errorstr)

    @lmi_wrap_cim_exceptions(prefix="EnumerateClassNames")
    def get_class_names(self, namespace=None, ClassName=None,
                        DeepInheritance=False):
        """
        Returns a list of class names.

        :param string namespace: namespace, from which the class names list
            should be retrieved; if None, default namespace will be used
            (**NOTE:** see :py:mod:`wbem`)
        :param string ClassName: defines the class that is the basis for the
            enumeration.  If the ClassName input parameter is absent, this
            implies that the names of all classes.
        :param bool DeepInheritance: if not present, of False, only the names
            of immediate child subclasses are returned, otherwise the names of
            all subclasses of the specified class should be returned.
        :returns: :py:class:`.LMIReturnValue` object with ``rval`` set to a
            list of strings containing class names, if no error occurs;
            otherwise ``rval`` is set to None and ``errorstr``
            contains an appropriate error string
        :raises: :py:exc:`.CIMError`, :py:exc:`.ConnectionError`
        """
        return LMIReturnValue(
            rval=self._cliconn.EnumerateClassNames(
                namespace,
                **filter_kwargs(
                    ClassName=ClassName,
                    DeepInheritance=DeepInheritance)))

    @lmi_wrap_cim_exceptions(prefix="GetClass")
    def get_class(self, classname, namespace=None, LocalOnly=True,
                  IncludeQualifiers=True, IncludeClassOrigin=False,
                  PropertyList=None):
        """
        Returns a :py:class:`wbem.CIMClass` object.

        :param string classname: class name
        :param string namespace: -- namespace name, from which the
            :py:class:`wbem.CIMClass` should be retrieved; if None, default
            namespace will be used (**NOTE:** see :py:mod:`wbem`)
        :param bool LocalOnly: indicates, if only local members should be
            present in the returned :py:class:`wbem.CIMClass`; any CIM elements
            (properties, methods, and qualifiers), except those added or
            overridden in the class as specified in the classname input
            parameter, shall not be included in the returned class.
        :param bool IncludeQualifiers: indicates, if qualifiers for the class
            (including qualifiers on the class and on any returned properties,
            methods, or method parameters) shall be included in the response.
        :param bool IncludeClassOrigin: indicates, if the ``CLASSORIGIN``
            attribute shall be present on all appropriate elements in the
            returned class.
        :param list PropertyList: if present and not None, the members of the
            list define one or more property names. The returned class shall
            not include elements for properties missing from this list. Note
            that if LocalOnly is specified as True, it acts as an additional
            filter on the set of properties returned. For example, if property
            A is included in the PropertyList but LocalOnly is set to True and
            A is not local to the requested class, it is not included in the
            response. If the PropertyList input parameter is an empty list, no
            properties are included in the response. If the PropertyList input
            parameter is None, no additional filtering is defined.
        :returns: :py:class:`.LMIReturnValue` object with rval set to
            :py:class:`wbem.CIMClass`, if no error occurs; otherwise rval is
            set to None and errorstr to appropriate error string
        :raises: :py:exc:`.CIMError`, :py:exc:`.ConnectionError`
        """
        return LMIReturnValue(
            rval=self._cliconn.GetClass(
                classname,
                namespace,
                **filter_kwargs(LocalOnly=LocalOnly,
                    IncludeQualifiers=IncludeQualifiers,
                    IncludeClassOrigin=IncludeClassOrigin,
                    PropertyList=PropertyList)))

    def get_superclass(self, classname, namespace=None):
        """
        Returns a superclass to given class.

        :param string classname: class name
        :param string namespace: namespace name
        :returns: superclass to given class, if such superclass exists,
            None otherwise
        :raises: :py:exc:`.CIMError`, :py:exc:`.ConnectionError`
        """
        minimal_class, rparams, errorstr = LMICIMXMLClient.get_class(
            self, classname, namespace, LocalOnly=True,
            IncludeQualifiers=False, PropertyList=[])
        if not minimal_class:
            return LMIReturnValue(
                rval=None, rparams=rparams, errorstr=errorstr)
        return LMIReturnValue(rval=minimal_class.superclass)

    def call_method(self, instance, method, **params):
        """
        Executes a method within a given instance.

        :param instance: object, on which the method will be executed. The
            object needs to be instance of following classes:

            * :py:class:`wbem.CIMInstance`
            * :py:class:`wbem.CIMInstanceName`
            * :py:class:`.LMIInstance`
            * :py:class:`.LMIInstanceName`

        :param string method: string containing a method name
        :param dictionary params: parameters passed to the method call
        :returns: :py:class:`.LMIReturnValue` object with rval set to return
            value of the method call, rparams set to returned parameters from
            the method call, if no error occurs; otherwise rval is set to -1
            and errorstr to appropriate error string
        :raises: :py:exc:`.CIMError`, :py:exc:`.ConnectionError`,
            :py:exc:`TypeError`
        """
        @lmi_wrap_cim_exceptions(-1, prefix="InvokeMethod " + method)
        def call_method_core(path, method, **params):
            rval, rparams = self._cliconn.InvokeMethod(method, path, **params)
            return LMIReturnValue(rval=rval, rparams=rparams)

        path = lmi_instance_to_path(instance)
        return call_method_core(path, method, **params)

    @lmi_wrap_cim_exceptions_rval([], prefix="AssociatorNames")
    def get_associator_names(self, instance, AssocClass=None, ResultClass=None,
                             Role=None, ResultRole=None, limit=-1):
        """
        Returns a list of associated :py:class:`wbem.CIMInstanceName` objects
        with an input instance.

        :param instance: for this object the list of associated
            :py:class:`wbem.CIMInstanceName` will be returned. The object needs
            to be instance of following classes:

            * :py:class:`wbem.CIMInstance`
            * :py:class:`wbem.CIMInstanceName`
            * :py:class:`.LMIInstance`
            * :py:class:`.LMIInstanceName`

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
        :param int limit: unused
        :returns: list of associated :py:class:`wbem.CIMInstanceName` objects
            with an input instance, if no error occurs; otherwise an empty list
            is returned
        :raises: :py:exc:`.CIMError`, :py:exc:`.ConnectionError`,
            :py:exc:`TypeError`
        """
        return self._cliconn.AssociatorNames(
            lmi_instance_to_path(instance),
            **filter_kwargs(
                AssocClass=AssocClass,
                ResultClass=ResultClass,
                Role=Role,
                ResultRole=ResultRole))

    @lmi_wrap_cim_exceptions_rval([], prefix="Associators")
    def get_associators(self, instance, AssocClass=None, ResultClass=None,
                        Role=None, ResultRole=None, IncludeQualifiers=False,
                        IncludeClassOrigin=False, PropertyList=None,
                        limit=-1):
        """
        Returns a list of associated :py:class:`wbem.CIMInstance` objects with
        an input instance.

        :param instance: for this object the list of associated
            :py:class:`wbem.CIMInstance` objects will be returned. The object
            needs to be instance of following classes:

            * :py:class:`wbem.CIMInstance`
            * :py:class:`wbem.CIMInstanceName`
            * :py:class:`.LMIInstance`
            * :py:class:`.LMIInstanceName`

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
        :param bool IncludeQualifiers: indicates, if all qualifiers for each
            object (including qualifiers on the object and on any returned
            properties) shall be included as ``<QUALIFIER>`` elements in the
            response.
        :param bool IncludeClassOrigin: indicates, if the ``CLASSORIGIN``
            attribute shall be present on all appropriate elements in each
            returned object.
        :param list PropertyList: if not None, the members of the array define
            one or more property names. Each returned object shall not include
            elements for any properties missing from this list. If PropertyList
            is an empty list, no properties are included in each returned
            object. If it is None, no additional filtering is defined.
        :param int limit: unused
        :returns: list of associated :py:class:`wbem.CIMInstance` objects with
            an input instance, if no error occurs; otherwise an empty list is
            returned
        :raises: :py:exc:`.CIMError`, :py:exc:`.ConnectionError`,
            :py:exc:`TypeError`
        """
        return self._cliconn.Associators(
            lmi_instance_to_path(instance),
            **filter_kwargs(
                AssocClass=AssocClass,
                ResultClass=ResultClass,
                Role=Role,
                ResultRole=ResultRole,
                IncludeQualifiers=IncludeQualifiers,
                IncludeClassOrigin=IncludeClassOrigin,
                PropertyList=PropertyList))

    @lmi_wrap_cim_exceptions_rval([], prefix="ReferenceNames")
    def get_reference_names(self, instance, ResultClass=None, Role=None,
                            limit=-1):
        """
        Returns a list of association :py:class:`wbem.CIMInstanceName` objects
        with an input instance.

        :param instance: for this object the association
            :py:class:`wbem.CIMInstanceName` objects will be returned. The
            object needs to be instance of following classes:

            * :py:class:`wbem.CIMInstance`
            * :py:class:`wbem.CIMInstanceName`
            * :py:class:`.LMIInstance`
            * :py:class:`.LMIInstanceName`

        :param string ResultClass: valid CIM class name. It acts as a filter on
            the returned set of object names by mandating that each returned
            Object Name identify an instance of this class (or one of its
            subclasses) or this class (or one of its subclasses).
        :param string Role: valid property name. It acts as a filter on the
            returned set of object names by mandating that each returned object
            name shall identify an object that refers to the target instance
            through a property with a name that matches the value of this
            parameter.
        :param int limit: unused
        :returns: list of association :py:class:`wbem.CIMInstanceName` objects
            with an input instance, if no error occurs; otherwise an empty list
            is returned
        :raises: :py:exc:`.CIMError`, :py:exc:`.ConnectionError`,
            :py:exc:`TypeError`
        """
        return self._cliconn.ReferenceNames(
            lmi_instance_to_path(instance),
            **filter_kwargs(
                ResultClass=ResultClass,
                Role=Role))

    @lmi_wrap_cim_exceptions_rval([], prefix="References")
    def get_references(self, instance, ResultClass=None, Role=None,
                       IncludeQualifiers=False, IncludeClassOrigin=False,
                       PropertyList=None, limit=-1):
        """
        Returns a list of association :py:class:`wbem.CIMInstance` objects with
        an input instance.

        :param instance: for this object the list of association
            :py:class:`wbem.CIMInstance` objects will be returned. The object
            needs to be instance of following classes:

            * :py:class:`wbem.CIMInstance`
            * :py:class:`wbem.CIMInstanceName`
            * :py:class:`.LMIInstance`
            * :py:class:`.LMIInstanceName`

        :param string ResultClass: valid CIM class name. It acts as a filter on
            the returned set of objects by mandating that each returned object
            shall be an instance of this class (or one of its subclasses) or
            this class (or one of its subclasses).
        :param string Role: valid property name. It acts as a filter on the
            returned set of objects by mandating that each returned object
            shall refer to the target object through a property with a name
            that matches the value of this parameter.
        :param bool IncludeQualifiers: bool flag indicating, if all qualifiers
            for each object (including qualifiers on the object and on any
            returned properties) shall be included as ``<QUALIFIER>``
            elements in the response.
        :param bool IncludeClassOrigin: bool flag indicating, if the
            ``CLASSORIGIN`` attribute shall be present on all appropriate
            elements in each returned object.
        :param list PropertyList: if not None, the members of the list define
            one or more property names. Each returned object shall not include
            elements for any properties missing from this list. If PropertyList
            is an empty list, no properties are included in each returned
            object. If PropertyList is None, no additional filtering is
            defined.
        :param int limit: unused
        :returns: list of association :py:class:`wbem.CIMInstance` objects with
            an input instance, if no error occurs; otherwise an empty list is
            returned
        :raises: :py:exc:`.CIMError`, :py:exc:`.ConnectionError`,
            :py:exc:`TypeError`
        """
        return self._cliconn.References(
            lmi_instance_to_path(instance),
            **filter_kwargs(
                ResultClass=ResultClass,
                Role=Role,
                IncludeQualifiers=IncludeQualifiers,
                IncludeClassOrigin=IncludeClassOrigin,
                PropertyList=PropertyList))

    @lmi_wrap_cim_exceptions(None, prefix="CreateInstance")
    def create_instance(self, classname, namespace=None, host=None,
                        properties=None, qualifiers=None, property_list=None):
        """
        Creates a new :py:class:`wbem.CIMInstance` object.

        :param string classname: class name of a new instance
        :param string namespace: namespace, of the new instance
        :param dictionary properties: property names and values
        :param dictionary qualifiers: qualifier names and values
        :param list property_list: list for property filtering; see
            :py:class:`wbem.CIMInstance`
        :returns: new :class:`wbem.CIMInstance`, if no error occurs; otherwise
            None is returned
        :raises: :py:exc:`.CIMError`, :py:exc:`.ConnectionError`
        """
        # Create a new dictionaries from the input ones, we do not want to
        # modify user's input variables.
        properties = dict(properties) if properties is not None else {}
        qualifiers = dict(qualifiers) if qualifiers is not None else {}
        cim_instance = wbem.CIMInstance(
            classname,
            properties,
            qualifiers,
            wbem.CIMInstanceName(
                classname,
                namespace=namespace,
                host=host),
            property_list)
        cim_path = self._cliconn.CreateInstance(NewInstance=cim_instance)
        return self.get_instance(cim_path, LocalOnly=False)

    @lmi_wrap_cim_exceptions(-1, prefix="ModifyInstance")
    def modify_instance(self, instance, IncludeQualifiers=True,
                        PropertyList=None):
        """
        Modifies a :py:class:`wbem.CIMInstance` object at CIMOM side.

        :param wbem.CIMInstance instance: object to be modified
        :param bool IncludeQualifiers: indicates, if the qualifiers are
            modified as specified in `ModifiedInstance`.
        :param list PropertyList: if not None, the members of the list define
            one or more property names. Only properties specified in the
            PropertyList are modified.  Properties of the *ModifiedInstance*
            that are missing from the PropertyList are ignored. If the
            PropertyList is an empty list, no properties are modified.  If the
            PropertyList is None, the set of properties to be modified consists
            of those of *ModifiedInstance* with values different from the
            current values in the instance to be modified.
        :returns: :py:class:`.LMIReturnValue` object with ``rval`` set to 0,
            if no error occurs; otherwise ``rval`` is set to -1 and
            ``errorstr`` is set to corresponding error string.
        :raises: :py:exc:`.CIMError`, :py:exc:`.ConnectionError`
        """
        self._cliconn.ModifyInstance(
            instance,
            **filter_kwargs(
                IncludeQualifiers=IncludeQualifiers,
                PropertyList=PropertyList))
        return LMIReturnValue(rval=0)

    @lmi_wrap_cim_exceptions(False, prefix="DeleteInstance")
    def delete_instance(self, instance):
        """
        Deletes a :py:class:`wbem.CIMInstance` from the CIMOM side.

        :param instance: object to be deleted. The object needs to be instance
            of following classes:

            * :py:class:`wbem.CIMInstance`
            * :py:class:`wbem.CIMInstanceName`
            * :py:class:`.LMIInstance`
            * :py:class:`.LMIInstanceName`

        :returns: :py:class:`.LMIReturnValue` object with ``rval`` set to True,
            if no error occurs; otherwise ``rval`` is set to False and
            ``errorstr`` is set to corresponding error string
        :raises: :py:exc:`.CIMError`, :py:exc:`.ConnectionError`,
            :py:exc:`TypeError`
        """
        self._cliconn.DeleteInstance(lmi_instance_to_path(instance))
        return LMIReturnValue(rval=True)

    @lmi_wrap_cim_exceptions(prefix="ExecQuery")
    def exec_query(self, query_lang, query, namespace=None):
        """
        Executes a query and returns a list of :py:class:`wbem.CIMInstance`
        objects.

        :param string query_lang: query language
        :param string query: query to execute
        :param string namespace: target namespace for the query
        :returns: :py:class:`.LMIReturnValue` object with ``rval`` set to list
            of :py:class:`wbem.CIMInstance` objects, if no error occurs;
            otherwise ``rval`` is set to None and ``errorstr`` is set to
            corresponding error string
        :raises: :py:exc:`.CIMError`, :py:exc:`.ConnectionError`
        """
        inst_list = self._cliconn.ExecQuery(query_lang, query, namespace)
        return LMIReturnValue(rval=inst_list)

    @property
    def username(self):
        """
        :returns: user name as a part of provided credentials
        :rtype: string
        """
        return self._cliconn.creds[0]

    @property
    def uri(self):
        """
        :returns: URI of the CIMOM
        :rtype: string
        """
        return self._uri

    @property
    def hostname(self):
        """
        :returns: hostname of CIMOM
        :rtype: string
        """
        return self._cliconn.hostname
