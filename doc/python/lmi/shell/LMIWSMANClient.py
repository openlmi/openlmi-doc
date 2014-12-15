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

try:
    import pywsman
    HAVE_PYWSMAN = True
except ImportError:
    HAVE_PYWSMAN = False
import types

from lmi.shell.compat import *

from lmi.shell.LMIDecorators import lmi_wrap_cim_exceptions
from lmi.shell.LMIDecorators import lmi_wrap_cim_exceptions_rval

from lmi.shell.LMIExceptions import CIMError
from lmi.shell.LMIExceptions import ConnectionError
from lmi.shell.LMIExceptions import LMINotSupported

from lmi.shell.LMIShellLogger import lmi_get_logger

from lmi.shell.LMIReturnValue import LMIReturnValue

from lmi.shell.LMIUtil import lmi_instance_to_path
from lmi.shell.LMIUtil import lmi_parse_uri
from lmi.shell.LMIUtil import lmi_raise_or_dump_exception

SCHEMES = {
    "CIM": "http://schemas.dmtf.org/wbem/wscim/1/cim-schema/2",
    "PRS": "http://schemas.dmtf.org/wbem/wscim/1/cim-schema/2",
    "Win32": "http://schemas.microsoft.com/wbem/wsman/1/wmi",
    "OpenWBEM": "http://schema.openwbem.org/wbem/wscim/1/cim-schema/2",
    "Linux": "http://sblim.sf.net/wbem/wscim/1/cim-schema/2",
    "OMC": "http://schema.omc-project.org/wbem/wscim/1/cim-schema/2",
    "PG": "http://schema.openpegasus.org/wbem/wscim/1/cim-schema/2",
    "AMT": "http://intel.com/wbem/wscim/1/amt-schema/1",
    "IPS": "http://intel.com/wbem/wscim/1/ips-schema/1",
    "Sun": "http://schemas.sun.com/wbem/wscim/1/cim-schema/2",
    "Msvm": "http://schemas.microsoft.com/wbem/wsman/1/wmi",
    # XXX: Dell's iDrac uses this schema
    # "DCIM": "http://schemas.dmtf.org/wbem/wscim/1/cim-schema/2"
    "DCIM": "http://schemas.dell.com/wbem/wscim/1/cim-schema/2"
}

logger = lmi_get_logger()


class LMIWSMANClient(object):
    """
    WS-MAN client.

    :param string uri: URI of the CIMOM
    :param string username: account, under which, the CIM calls will be
        performed
    :param string password: user's password
    :param bool verify_server_cert: indicates, whether a server side
        certificate needs to be verified, if SSL used; default value is True
    :param string key_file: path to x509 key file; default value is None
    :param string cert_file: path to x509 cert file; default value is None
    """

    ASSOC_ASSOCIATORS, \
        ASSOC_REFERENCES, \
        RES_INSTANCE, \
        RES_INSTANCE_NAME = range(4)

    QUERY_LANG_CQL = "CQL"
    QUERY_LANG_WQL = "WQL"

    WSM_XML_FAULT, \
        WSM_XML_NO_RESPONSE, \
        WSM_XML_NO_FAULT = range(-1, -4, -1)

    def __init__(self, uri, username="", password="", interactive=False,
                 verify_server_cert=True, key_file=None, cert_file=None):
        if not HAVE_PYWSMAN:
            logger.error("WSMAN not supported")
            raise ConnectionError(
                wbem.CIM_ERR_NOT_SUPPORTED,
                "WSMAN not supported")

        if not uri.startswith("http://") and \
                not uri.startswith("https://"):
            uri = "https://" + uri
        self._uri = uri

        # Parse CIMOM URI
        scheme, hostname, port, path, username_, password_ = lmi_parse_uri(uri)
        if username_ is not None:
            username = username_
            password = password_

        # Create a WSMAN client
        self._cliconn = pywsman.Client(
            hostname, port, path, scheme, username, password)

        transport = self._cliconn.transport()
        if username:
            transport.set_auth_method(pywsman.BASIC_AUTH_STR)
        if cert_file:
            transport.set_cert(cert_file)
            transport.set_key(key_file)

        # X509 verification
        transport.set_verify_peer(verify_server_cert)
        transport.set_verify_host(verify_server_cert)

        # Add dummy auth_request_callback
        pywsman.Client.auth_request_callback = lambda cliconn: None

    @staticmethod
    def _get_filter(classname, inst_filter=None,
                    query_lang=QUERY_LANG_WQL):
        """
        Creates :py:class:`pywsman.Filter` out of inst_filter.

        :param str classname: string containing classname for the filter
        :param dict inst_filter: dictionary containing keys and values for the
            filter
        :param str query_lang: query language for the filter
        :rtype: :py:class:`pywsman.Filter`
        """
        if not inst_filter:
            return None
        query = "select * from %s where " % classname
        conds = []
        for k, v in inst_filter.iteritems():
            quotes = isinstance(v, basestring)
            cond = "%s =" % k
            if quotes:
                cond += " \"%s\"" % v
            else:
                cond += " %s" % v
            conds.append(cond)
        query += " and ".join(conds)

        filt = pywsman.Filter()
        if query_lang == LMIWSMANClient.QUERY_LANG_WQL:
            filt.wql(query)
        elif query_lang == LMIWSMANClient.QUERY_LANG_CQL:
            filt.cql(query)
        else:
            raise ValueError("Unknown query language '%s'" % query_lang)

        return filt

    @staticmethod
    def _query_to_scheme_prefix_classnames(query):
        """
        Transforms a query to WS-MAN prefix and list of class names.

        :param str query: query
        :rtype: tuple containing class name prefix, WS-MAN scheme and list of
            class names
        :raises: :py:exc:`ValueError`
        """
        tokens = query.split(" ")
        tokens_lower = [token.lower() for token in tokens]

        # CIM query languages *do not* define "data change" operations;
        # such as INSERT, UPDATE or DELETE.
        try:
            begin = tokens_lower.index("from") + 1
        except ValueError:
            raise ValueError("Wrong query")

        end = len(tokens)
        try:
            end = tokens_lower.index("where")
        except ValueError:
            pass

        classenames = []
        for token in tokens[begin:end]:
            classenames += [cls for cls in token.split(",") if cls]

        rprefix = ""
        rscheme = ""
        for cls in classenames:
            for prefix, scheme in SCHEMES.iteritems():
                if cls.startswith(prefix.lower()):
                    if rscheme and rscheme != scheme:
                        raise ValueError("Classes not from 1 scheme")
                    rprefix = prefix
                    rscheme = scheme

        return rprefix, rscheme, classenames

    @staticmethod
    def _uri_to_cls_ns(uri):
        """
        Transforms URI to class name and namespace.

        :param str uri: URI
        :rtype: tuple containing class name and namespace
        :raises: :py:exc:`ValueError`
        """
        for prefix, scheme in SCHEMES.iteritems():
            if not uri.startswith(scheme):
                continue
            try:
                cls, ns = uri[len(scheme) + 1:].rsplit("/", 1)[::-1]
                if cls == "*":
                    cls = None
            except ValueError:
                # Dell's iDrac doesn't include namespace in ResourceURI
                cls = uri[len(scheme) + 1:]
                ns = ""
            return cls, ns
        raise ValueError("Wrong URI format")

    @staticmethod
    def _uri_to_cls(uri):
        """
        Transforms URI to class name.

        :param str uri: URI
        :rtype: str
        """

        return LMIWSMANClient._uri_to_cls_ns(uri)[0]

    @staticmethod
    def _uri_to_ns(uri):
        """
        Transforms URI to namespace.

        :param str uri: URI
        :rtype: str
        """
        return LMIWSMANClient._uri_to_cls_ns(uri)[1]

    @staticmethod
    def _cls_ns_to_uri(classname, namespace, wildcard=False):
        """
        Creates URI from class name and namespace.

        :param str classname: class name
        :param str namespace: namespace
        :param bool wildcard: if class name is prefixed by "Win32" and wildcard
            is set to True, asterisk is used instead of the class name in
            resulting URI. Otherwise, the parameter is ignored.
        :rtype: str
        """
        for prefix, scheme in SCHEMES.iteritems():
            if not classname.startswith(prefix):
                continue
            if wildcard and prefix == "Win32":
                # Wildcards can be used with Microsoft WMI
                classname = "*"
            members = [
                m for m in [scheme, namespace, classname]
                if isinstance(m, basestring)
            ]
            return "/".join(members)
        raise ValueError("No scheme for class %s" % classname)

    @staticmethod
    def _xml_to_wbem_instance_name(epr, namespace, host=None):
        """
        Creates :py:class:`wbem.CIMInstanceName` from
        :py:class:`pywsman.XmlNode`.

        :param pywsman.XmlNode epr: XML node containing the instance name
        :param str namespace: string containing namespace of the instance name
        :param str host: string containing host name of the instance name
        :rtype: :py:class:`wbem.CIMInstanceName`
        """
        ref_parameters = epr.get("ReferenceParameters")
        uri = ref_parameters.get("ResourceURI")
        selectors = ref_parameters.get("SelectorSet")
        classname = LMIWSMANClient._uri_to_cls(str(uri))
        keybindings = wbem.NocaseDict()
        for selector in selectors:
            name = selector.attr_find(None, "Name").value()
            value = selector.child()
            if value and value.name() == "EndpointReference":
                value = LMIWSMANClient._xml_to_wbem_instance_name(
                    value, namespace, host)
            else:
                value = str(selector)
            keybindings[name] = value

        return wbem.CIMInstanceName(classname, keybindings, host, namespace)

    @staticmethod
    def _xml_to_wbem_property(prop, host=None):
        """
        Creates :py:class:`wbem.CIMProperty` from :py:class:`pywsman.XmlNode`.

        :param pywsman.XmlNode prop: XML node containing the property
        :param str host: string containing host name of a potential
            :py:class:`wbem.CIMInstanceName`
        :rtype: :py:class:`wbem.CIMProperty`
        """
        ref_parameters = prop.get("ReferenceParameters")
        if ref_parameters is not None:
            value = LMIWSMANClient._xml_to_wbem_instance_name(prop, host)
            t = "reference"
        else:
            value = str(prop)
            # For now, let's assume, all the properties are strings except
            # references. See above.
            t = "string"
        return wbem.CIMProperty(prop.name(), value, t)

    @staticmethod
    def _xml_to_wbem_instance(instance, namespace, host):
        """
        Creates :py:class:`wbem.CIMInstance` from :py:class:`pywsman.XmlNode`.

        :param pywsman.XmlNode instance: XML node containing the instance
        :param str namespace: string containing the namespace of the instance
        :param str host: string containing the host name of the instance
        :rtype: :py:class:`wbem.CIMInstance`
        """
        classname = instance.name()
        properties = wbem.NocaseDict()
        qualifiers = wbem.NocaseDict()
        property_list = []

        for prop in instance:
            properties[prop.name()] = LMIWSMANClient._xml_to_wbem_property(
                prop, host)
            property_list.append(prop.name())

        # Reconstruct wbem.CIMInstanceName
        # XXX: keybindings?
        keybindings = None
        path = wbem.CIMInstanceName(classname, keybindings, host, namespace)

        return wbem.CIMInstance(
            classname, properties, qualifiers, path, property_list)

    @staticmethod
    def _xml_check_response(doc):
        """
        Performs a XML response check and raises an exception, if necessary.

        :param pywsman.XmlDoc doc: XML doc containing WS-MAN response
        :raises: :py:exc:`.CIMError`
        """
        if doc is None:
            # We should get at least a XML response.
            raise wbem.CIMError(
                LMIWSMANClient.WSM_XML_NO_RESPONSE, "No response from CIMOM")
        elif doc.is_fault():
            fault = doc.fault()
            raise wbem.CIMError(LMIWSMANClient.WSM_XML_FAULT, fault.reason())

    @staticmethod
    def _xml_invoke_rval(method_doc, namespace, host):
        """
        Creates :py:class:`.LMIReturnValue` from :py:class:`pywsman.XmlNode`.

        :param pywsman.XmlNode method_doc: XML node containing the method
            result value and parameters
        :param str namespace: string containing namespace of a potential
            :py:class:`wbem.CIMInstanceName` in return parameters
        :param str host: string containing host name of potential
            :py:class:`wbem.CIMInstanceName` in return parameters
        :rtype: :py:class:`.LMIReturnValue`
        """
        rval = None
        rparams = {}
        for param in method_doc:
            name = param.name()
            value = param.child()
            if value and value.name() == "EndPointReference":
                value = LMIWSMANClient._xml_to_wbem_instance_name(
                    value, namespace, host)
            else:
                value = str(param)

            if name == "ReturnValue":
                rval = value
            else:
                rparams[name] = value

        return LMIReturnValue(rval=rval, rparams=rparams)

    @staticmethod
    def _path_to_xml(path):
        """
        Transforms :py:class:`wbem.CIMInstanceName` to XML string.

        :param wbem.CIMInstanceName path: instance name
        :rtype: string containing a XML node
        """
        epr = pywsman.EndPointReference(
            LMIWSMANClient._cls_ns_to_uri(path.classname, path.namespace),
            pywsman.WSA_TO_ANONYMOUS)
        for k, v in path.keybindings.iteritems():
            if isinstance(v, wbem.CIMInstanceName):
                value = LMIWSMANClient.path_to_xml(v)
            else:
                value = str(v)
            epr.add_selector(k, value)
        # Ugly, but needs to be done. PyWSMan escapes XML selector.
        # WSMan needs to encode whole EndPointReference into XML rather
        # than resource URI.
        return epr.to_xml().replace("&lt;", "<").replace("&gt;", ">")

    def connect(self):
        """
        Compatibility method present due to :py:class:`.LMICIMXMLClient`.
        """
        return LMIReturnValue(rval=True)

    def disconnect(self):
        """
        Compatibility method present due to :py:class:`.LMICIMXMLClient`.
        """
        pass

    def dummy(self):
        """
        Sends a "dummy" request to verify credentials.

        :returns: :py:class:`.LMIReturnValue` with rval set to True, if
            provided credentials are OK; False otherwise. If LMIShell uses
            exceptions, :py:exc:`.CIMError` will be raised.
        :raises: :py:exc:`.CIMError`
        """
        options = pywsman.ClientOptions()
        doc = self._cliconn.identify(options)

        try:
            self._xml_check_response(doc)
        except CIMError, e:
            lmi_raise_or_dump_exception(e)
            return LMIReturnValue(rval=False, errorstr=e.args[1])
        return LMIReturnValue(rval=True)

    def enumerate_iter_with_uri(self, uri, filt, options=None, limit=-1):
        """
        Enumerates instance (names).

        :param str uri: URI of the resource
        :param pywsman.Filter filt: filter for enumeration
        :param pywsman.ClientOptions options: options for enumeration
        :param int limit: enumeration limit
        :rtype: list containing :py:class:`wbem.CIMInstance` of
            :py:class:`wbem.CIMInstanceName`
        :raises: :py:exc:`.CIMError`
        """
        if options is None:
            options = pywsman.ClientOptions()

        namespace = self._uri_to_ns(uri)

        doc = self._cliconn.enumerate(options, filt, uri)
        self._xml_check_response(doc)

        context = doc.root().find(
            pywsman.XML_NS_ENUMERATION,
            "EnumerationContext")

        # Transformation function
        if options.get_flags() & pywsman.FLAG_ENUMERATION_ENUM_EPR:
            def xml_to_wbem_obj(doc):
                return self._xml_to_wbem_instance_name(
                    doc, namespace, self._cliconn.host())
        else:
            def xml_to_wbem_obj(doc):
                return self._xml_to_wbem_instance(
                    doc, namespace, self._cliconn.host())

        # Pull each Instance(Name)
        cnt = 0
        rval = []
        while context is not None and (cnt < limit or limit == -1):
            doc = self._cliconn.pull(options, None, uri, str(context))
            self._xml_check_response(doc)

            root = doc.root()
            context = root.find(
                pywsman.XML_NS_ENUMERATION,
                "EnumerationContext")
            items = root.find(pywsman.XML_NS_ENUMERATION, "Items")

            for item in items:
                rval.append(xml_to_wbem_obj(item))

            # Count the instances
            cnt += 1

        # Do we have all the instance(names)?
        if context is not None and cnt == limit:
            # Release the enumeration context from CIMOM.
            self._cliconn.release(options, uri, str(context))

        return rval

    def enumerate_iter(self, classname, namespace, filt, options=None,
                       limit=-1):
        """
        Enumerates instance (names).

        :param pywsman.Filter filt: filter for enumeration
        :param pywsman.ClientOptions options: options for enumeration
        :param int limit: enumeration limit
        :rtype: list containing :py:class:`wbem.CIMInstance` of
            :py:class:`wbem.CIMInstanceName`
        :raises: :py:exc:`.CIMError`
        """
        uri = self._cls_ns_to_uri(classname, namespace, bool(filt))
        return self.enumerate_iter_with_uri(uri, filt, options, limit)

    def enumerate(self, result_cls, classname, namespace=None,
                  inst_filter=None, limit=-1, **kwargs):
        """
        Enumerates instance (names).

        :param int result_cls: either :py:attr:`.LMIWSMANClient.RES_INSTANCE`
            or :py:attr:`.LMIWSMANClient.RES_INSTANCE_NAME`
        :param str classname: class name to enumerate
        :param str namespace: namespace where the class is located
        :param dict inst_filter: dictionary containing keys and values for the
            filter
        :param int limit: enumeration limit
        :param kwargs: keyword arguments used for inst_filter
        :rtype: list containing :py:class:`wbem.CIMInstance` of
            :py:class:`wbem.CIMInstanceName`
        :raises: :py:exc:`.CIMError`
        """
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

        options = pywsman.ClientOptions()
        if result_cls == LMIWSMANClient.RES_INSTANCE_NAME:
            options.set_flags(pywsman.FLAG_ENUMERATION_ENUM_EPR)
        filt = self._get_filter(
            classname, inst_filter, LMIWSMANClient.QUERY_LANG_WQL)

        return self.enumerate_iter(
            classname, namespace, filt, options, limit)

    def association(self, instance, relationship, result_cls, AssocClass=None,
                    ResultClass=None, Role=None, ResultRole=None, limit=-1):
        """
        Enumerates association instance (names).

        :param instance: object, for which the association objects will be
            enumerated. The object needs to be instance of following classes:

            * :py:class:`wbem.CIMInstance`
            * :py:class:`wbem.CIMInstanceName`
            * :py:class:`.LMIInstance`
            * :py:class:`.LMIInstanceName`

        :param relationship: :py:attr:`.LMIWSMANClient.ASSOC_ASSOCIATORS` or
            :py:attr:`.LMIWSMANClient.ASSOC_REFERENCES`
        :param result_cls: :py:attr:`.LMIWSMANClient.RES_INSTANCE` or
            :py:attr:`.LMIWSMANClient.RES_INSTANCE_NAME`
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
        :param int limit: enumeration limit
        :returns: list of association objects
        """
        path = lmi_instance_to_path(instance)
        uri = self._cls_ns_to_uri(path.classname, path.namespace)

        # Create EndPointReference
        epr = pywsman.EndPointReference(uri, pywsman.WSA_TO_ANONYMOUS)
        for k, v in path.keybindings.iteritems():
            epr.add_selector(k, str(v))

        # Create filter
        filt = pywsman.Filter()
        if relationship == LMIWSMANClient.ASSOC_ASSOCIATORS:
            filt.associators(
                epr, AssocClass, ResultClass, Role, ResultRole, None, 0)
        else:
            filt.references(
                epr, AssocClass, ResultClass, Role, ResultRole, None, 0)

        options = pywsman.ClientOptions()
        if result_cls == LMIWSMANClient.RES_INSTANCE_NAME:
            options.set_flags(pywsman.FLAG_ENUMERATION_ENUM_EPR)

        # Enumerate association objects
        assoc = self.enumerate_iter(
            path.classname, path.namespace, filt, options, limit)

        return assoc

    # NOTE: usage with Key=something, Value=something is deprecated
    # NOTE: inst_filter is either None or dict
    def get_instance_names(self, classname, namespace=None, inst_filter=None,
                           limit=-1, **kwargs):
        """
        Returns a list of :py:class:`wbem.CIMInstanceName` objects.

        :param string classname: class name
        :param string namespace: namespace name, where the instance names live
        :param dict inst_filter: dictionary containing filter values. The
            key corresponds to the primary key of the
            :py:class:`wbem.CIMInstanceName`; value contains the filtering
            value.
        :param int limit: enumeration limit
        :param dictionary kwargs: supported keyword arguments (these are
            **deprecated**)

            * **Key** or **key** (*string*) -- filtering key, see above
            * **Value** or **value** (*string*) -- filtering value, see above

        :returns: :py:class:`.LMIReturnValue` object with ``rval`` contains a
            list of :py:class:`wbem.CIMInstanceName` objects, if no error
            occurs; otherwise ``rval`` is set to None and ``errorstr`` contains
            appropriate error string
        :raises: :py:exc:`.CIMError`
        """
        @lmi_wrap_cim_exceptions(prefix="EnumerateInstanceNames " + classname)
        def get_instance_names_core():
            inst_names_list = self.enumerate(
                LMIWSMANClient.RES_INSTANCE_NAME, classname, namespace,
                inst_filter, limit, **kwargs)
            return LMIReturnValue(rval=inst_names_list)
        return get_instance_names_core()

    # NOTE: usage with Key=something, Value=something is deprecated
    # NOTE: inst_filter is either None or dict
    @lmi_wrap_cim_exceptions(prefix="EnumerateInstances")
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
        :param int limit: enumeration limit
        :param dictionary kwargs: supported keyword arguments (these are
            **deprecated**)

            * **Key** or **key** (*string*) -- filtering key, see above
            * **Value** or **value** (*string*) -- filtering value, see above

        :returns: :py:class:`.LMIReturnValue` object with ``rval`` set to a
            list of :py:class:`wbem.CIMIntance` objects, if no error occurs;
            otherwise ``rval`` is set to None and ``errorstr`` is set to
            corresponding error string.
        :raises: :py:exc:`.CIMError`
        """
        # We do not enumerate instances directly. First instance names are
        # pulled from CIMOM. This is done due to lack of keybindings
        # information in the pull response of the instance.
        inst_names_list, _, errorstr = self.get_instance_names(
            classname, namespace, inst_filter, limit, **kwargs)
        if not inst_names_list:
            return LMIReturnValue(rval=None, errorstr=errorstr)

        # Get all the instances from instance names. Now we can construct
        # LMIInstance also with object path information.
        inst_list = []
        for inst_name in inst_names_list:
            inst, _, errorstr = self.get_instance(inst_name)
            if not inst:
                return LMIReturnValue(rval=[], errorstr=errorstr)
            inst_list.append(inst)

        # Client-side filtering present due to LMICIMXMLClient compatibility.
        if inst_list and inst_filter and client_filtering:
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

    def get_instance(self, instance, LocalOnly=True, IncludeQualifiers=False,
                     IncludeClassOrigin=False, PropertyList=None):
        """
        Returns a :py:class:`wbem.CIMInstance` object.

        :param instance: path of the object, which is about to be retrieved.
            The object needs to be instance of following classes:

            * :py:class:`wbem.CIMInstanceName`
            * :py:class:`wbem.CIMInstance`
            * :py:class:`.LMIInstanceName`
            * :py:class:`.LMIInstance`

        :param LocalOnly: unused
        :param IncludeQualifiers: unused
        :param IncludeClassOrigin: unused
        :param PropertyList: unused
        :returns: :py:class:`.LMIReturnValue` object, where ``rval`` is set to
            :py:class:`wbem.CIMInstance` object, if no error occurs; otherwise
            ``errorstr`` is set to corresponding error string
        :raises: :py:exc:`.CIMError`
        """
        @lmi_wrap_cim_exceptions(prefix="GetInstance " + instance.classname)
        def get_instance_core(path, options):
            uri = self._cls_ns_to_uri(path.classname, path.namespace)
            doc = self._cliconn.get(options, uri)
            self._xml_check_response(doc)
            inst = self._xml_to_wbem_instance(
                doc.body().child(), path.namespace, self._cliconn.host())
            inst.path = path
            return LMIReturnValue(rval=inst)

        path = lmi_instance_to_path(instance)

        options = pywsman.ClientOptions()
        for k, v in path.keybindings.iteritems():
            if isinstance(v, wbem.CIMInstanceName):
                value = self._path_to_xml(v)
            else:
                value = str(v)
            options.add_selector(k, value)

        return get_instance_core(path, options)

    def get_class_names(self, *args, **kwargs):
        """
        Not supported.
        """
        lmi_raise_or_dump_exception(LMINotSupported("GetClassNames()"))
        return LMIReturnValue(rval=[], errorstr="GetClassName() not supported")

    def get_class(self, *args, **kwargs):
        """
        Not supported.
        """
        lmi_raise_or_dump_exception(LMINotSupported("GetClass()"))
        return LMIReturnValue(rval=None, errorstr="GetClass() not supported")

    def get_superclass(self, *args, **kwargs):
        """
        Not supported.
        """
        lmi_raise_or_dump_exception(LMINotSupported("GetSuperClass()"))
        return LMIReturnValue(
            rval=None, errorstr="GetSuperClass() not supported")

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
        :raises: :py:exc:`.CIMError`
        """
        @lmi_wrap_cim_exceptions(-1, prefix="InvokeMethod " + method)
        def call_method_core(method, path, options):
            uri = self._cls_ns_to_uri(path.classname, path.namespace)
            doc = self._cliconn.invoke(options, uri, method)
            self._xml_check_response(doc)
            method_doc = doc.body().get(method + "_OUTPUT")
            return self._xml_invoke_rval(
                method_doc, path.namespace, self._cliconn.host())

        path = lmi_instance_to_path(instance)

        options = pywsman.ClientOptions()
        for k, v in path.keybindings.iteritems():
            options.add_selector(k, str(v))

        # Add method parameters
        for k, v in params.iteritems():
            options.add_property(k, str(v))

        # Invoke the method
        return call_method_core(method, path, options)

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
        :param int limit: enumeration limit
        :returns: list of associated :py:class:`wbem.CIMInstanceName` objects
            with an input instance, if no error occurs; otherwise en empty list
            is returned
        :raises: :py:exc:`.CIMError`
        """
        return self.association(
            instance, LMIWSMANClient.ASSOC_ASSOCIATORS,
            LMIWSMANClient.RES_INSTANCE_NAME, AssocClass, ResultClass, Role,
            ResultRole, limit)

    @lmi_wrap_cim_exceptions_rval([], prefix="Associators")
    def get_associators(self, instance, AssocClass=None, ResultClass=None,
                        Role=None, ResultRole=None, IncludeQualifiers=False,
                        IncludeClassOrigin=False, PropertyList=None, limit=-1):
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
            instance of this class or one of its subclasses. Default value is
            None.
        :param string ResultClass: valid CIM class name. It acts as a filter on
            the returned set of objects by mandating that each returned object
            shall be either an instance of this class (or one of its
            subclasses) or be this class (or one of its subclasses). Default
            value is None.
        :param string Role: valid property name. It acts as a filter on the
            returned set of objects by mandating that each returned object
            shall be associated with the source object through an association
            in which the source object plays the specified role. That is, the
            name of the property in the association class that refers to the
            source object shall match the value of this parameter.  Default
            value is None.
        :param string ResultRole: valid property name. It acts as a filter on
            the returned set of objects by mandating that each returned object
            shall be associated to the source object through an association in
            which the returned object plays the specified role. That is, the
            name of the property in the association class that refers to the
            returned object shall match the value of this parameter.  Default
            value is None.
        :param IncludeQualifiers: unused
        :param IncludeClassOrigin: unused
        :param PropertyList: unused
        :param int limit: enumeration limit
        :returns: list of associated :py:class:`wbem.CIMInstance` objects with
            an input instance, if no error occurs; otherwise an empty list is
            returned
        :raises: :py:exc:`.CIMError`
        """
        return self.association(
            instance, LMIWSMANClient.ASSOC_ASSOCIATORS,
            LMIWSMANClient.RES_INSTANCE, AssocClass,
            ResultClass, Role, ResultRole, limit)

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
        :param int limit: enumeration limit
        :returns: list of association :py:class:`wbem.CIMInstanceName` objects
            with an input instance, if no error occurs; otherwise an empty list
            is returned
        :raises: :py:exc:`.CIMError`
        """
        return self.association(
            instance, LMIWSMANClient.ASSOC_REFERENCES,
            LMIWSMANClient.RES_INSTANCE_NAME, None,
            ResultClass, Role, None, limit)

    @lmi_wrap_cim_exceptions_rval([], prefix="References")
    def get_references(self, instance, ResultClass=None, Role=None,
                       IncludeQualifiers=False, IncludeClassOrigin=False,
                       PropertyList=None, limit=-1):
        """
        Returns a list of association :py:class:`wbem.CIMInstance` objects with
        an input instance.

        :param instance: for this object the association
            :py:class:`wbem.CIMInstances` objects will be returned. The
            object needs to be instance of following classes:

            * :py:class:`wbem.CIMInstance`
            * :py:class:`wbem.CIMInstanceName`
            * :py:class:`.LMIInstance`
            * :py:class:`.LMIInstanceName`

        :param string ResultClass: valid CIM class name. It acts as a filter on
            the returned set of objects by mandating that each returned object
            shall be an instance of this class (or one of its subclasses) or
            this class (or one of its subclasses). Default value is None.
        :param string Role: valid property name. It acts as a filter on the
            returned set of objects by mandating that each returned object
            shall refer to the target object through a property with a name
            that matches the value of this parameter. Default value is None.
        :param IncludeQualifiers: unused
        :param IncludeClassOrigin: unused
        :param PropertyList: unused
        :param int limit: enumeration limit
        :returns: list of association :py:class:`wbem.CIMInstance` objects with
            an input instance, if no error occurs; otherwise an empty list is
            returned
        :raises: :py:exc:`.CIMError`
        """
        return self.association(
            instance, LMIWSMANClient.ASSOC_REFERENCES,
            LMIWSMANClient.RES_INSTANCE, None,
            ResultClass, Role, None, limit)

    def create_instance(self, *args, **kwargs):
        """
        Not supported.
        """
        lmi_raise_or_dump_exception(LMINotSupported("CreateInstance()"))
        return LMIReturnValue(
            rval=None, errorstr="CreateInstance() not supported")

    def modify_instance(self, *args, **kwargs):
        """
        Not supported.
        """
        lmi_raise_or_dump_exception(LMINotSupported("ModifyInstance()"))
        return LMIReturnValue(
            rval=False, errorstr="ModifyInstance() not supported")

    def delete_instance(self, *args, **kwargs):
        """
        Not supported.
        """
        lmi_raise_or_dump_exception(LMINotSupported("DeleteInstance()"))
        return LMIReturnValue(
            rval=False, errorstr="DeleteInstance() not supported")

    @lmi_wrap_cim_exceptions(prefix="ExecQuery")
    def exec_query(self, query_lang, query, namespace=wbem.DEFAULT_NAMESPACE):
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
        :raises: :py:exc:`.CIMError`
        """
        # Parse CIM query and return WSMAN scheme, scheme prefix and classes
        # defined in the query.
        scheme, prefix, classes = self._query_to_scheme_prefix_classnames(
            query)

        # Grammar of CIM query language states, that there can be a list of
        # classes present in FROM statement. We support only one class.
        if len(classes) != 1:
            raise ValueError("Wrong query, too many classnames")
        classname = classes[0]

        filt = pywsman.Filter()
        if query_lang == LMIWSMANClient.QUERY_LANG_WQL:
            filt.wql(query)
        elif query_lang == LMIWSMANClient.QUERY_LANG_CQL:
            filt.cql(query)
        else:
            lmi_raise_or_dump_exception(
                ValueError("Unknown query language '%s'" % query_lang))

        uri = self._cls_ns_to_uri(classname, namespace, True)

        insts = self.enumerate_iter_with_uri(uri, filt)
        return LMIReturnValue(rval=insts)

    @property
    def username(self):
        """
        :returns: user name as a part of provided credentials
        :rtype: string
        """
        return self._cliconn.user()

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
        return self._cliconn.host()
