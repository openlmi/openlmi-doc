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
import atexit
import getpass
import readline
import urlparse

import M2Crypto.SSL
import M2Crypto.SSL.Checker
import M2Crypto.X509

from lmi.shell.compat import *

from lmi.shell.LMICIMXMLClient import LMICIMXMLClient
from lmi.shell.LMIWSMANClient import LMIWSMANClient
from lmi.shell.LMIShellClient import LMIShellClient
from lmi.shell.LMINamespace import LMINamespaceRoot
from lmi.shell.LMIReturnValue import LMIReturnValue
from lmi.shell.LMISubscription import LMISubscription
from lmi.shell.LMIObjectFactory import LMIObjectFactory

from lmi.shell.LMIExceptions import CIMError
from lmi.shell.LMIExceptions import ConnectionError
from lmi.shell.LMIExceptions import LMIIndicationError
from lmi.shell.LMIExceptions import LMINamespaceNotFound

from lmi.shell.LMIShellLogger import lmi_get_logger

from lmi.shell.LMIUtil import lmi_raise_or_dump_exception
from lmi.shell.LMIUtil import lmi_is_localhost

logger = lmi_get_logger()


def __lmi_raw_input(prompt, use_echo=True):
    """
    Reads a string from the standard input.

    :param string prompt: input prompt
    :param bool use_echo: whether to echo the input on the command line
    :returns: input string
    :raises: :py:exc:`EOFError`
    """
    if not sys.stderr.isatty() and not sys.stdout.isatty():
        logger.warn(
            "Both stdout and stderr are detached from terminal, "
            "using stdout for prompt")
    elif not sys.stdout.isatty() and sys.stderr.isatty():
        # read the input with prompt printed to stderr
        stream = sys.stderr
    else:
        # read the input with prompt printed to stdout
        stream = sys.stdout

    # Define input function
    if use_echo:
        def get_input(prompt):
            return raw_input(prompt)
    else:
        def get_input(prompt):
            return getpass.getpass(prompt, stream)

    try:
        result = get_input(prompt)
    except EOFError, e:
        stream.write("\n")
        return None
    except KeyboardInterrupt, e:
        raise e

    if result and use_echo:
        cur_hist_len = readline.get_current_history_length()
        if cur_hist_len > 1:
            readline.remove_history_item(cur_hist_len - 1)

    return result


def connect(uri, username="", password="", interactive=False, use_cache=True,
            key_file=None, cert_file=None, verify_server_cert=True,
            prompt_prefix=""):
    """
    Creates a connection object with provided URI and credentials.

    :param string uri: URI of the CIMOM
    :param string username: account, under which, the CIM calls will be
        performed
    :param string password: user's password

    :param bool interactive: flag indicating, if the LMIShell client is running
        in the interactive mode; default value is False.
    :param bool use_cache: flag indicating, if the LMIShell client should use
        cache for :py:class:`wbem.CIMClass` objects. This saves lot's of
        communication, if there are :func:`EnumerateInstances` and
        :func:`EnumerateClasses` intrinsic methods often issued. Default value
        is True.
    :param string key_file: path to x509 key file; default value is None
    :param string cert_file: path to x509 cert file; default value is None
    :param bool verify_server_cert: flag indicating, whether a server side
        certificate needs to be verified, if SSL used; default value is True.
    :param string prompt_prefix: username and password prompt prefix in case
        the user is asked for credentials. Default value is empty string.
    :returns: :py:class:`.LMIConnection` object or None, if LMIShell does not
        use exceptions
    :raises: :py:exc:`.ConnectionError`

    **NOTE:** If interactive is set to True, LMIShell will:

    * prompt for username and password, if missing and connection via
      Unix socket can not be established.
    * use pager for the output of: :py:meth:`.LMIInstance.doc`,
      :py:meth:`.LMIClass.doc`, :py:meth:`.LMIInstance.tomof` and
      :py:meth:`.LMIMethod.tomof`

    **Usage:** :ref:`startup_connection`.
    """
    connection = None

    if lmi_is_localhost(uri) and \
            not username and not password and \
            not cert_file and not key_file:
        try:
            # Try to get socket's permissions. If we can talk to TOG-Pegasus,
            # stat() will return stat buf; OSError will be raised otherwise.
            os.stat("/var/run/tog-pegasus/cimxml.socket")

            connection = LMIConnection(
                uri, interactive=interactive, use_cache=use_cache)

            # Verify the connection
            rval, _, errorstr = connection.connect()
            if not rval:
                logger.warning("Can't connect via Unix socket")
                del connection
            else:
                logger.info("Connected via Unix socket")
                return connection
        except OSError, e:
            # It is fine not to do anything here. User will be prompted for
            # necessary credentials, if necessary.
            pass

    if interactive and not key_file and not cert_file:
        try:
            if not username:
                username = __lmi_raw_input(
                    prompt_prefix + "username: ", True)
            if not password:
                password = __lmi_raw_input(
                    prompt_prefix + "password: ", False)
        except KeyboardInterrupt, e:
            sys.stdout.write("\n")
            return None

    try:
        # Try to create a LMIConnection. We may fail to construct such object,
        # if WSMAN isn't supported (package pywsman not available).
        connection = LMIConnection(
            uri, username, password, interactive=interactive,
            use_cache=use_cache, key_file=key_file, cert_file=cert_file,
            verify_server_cert=verify_server_cert)
    except Exception as e:
        lmi_raise_or_dump_exception(e)
        return

    # Verify the connection
    rval, _, errorstr = connection.connect()

    if not rval:
        logger.error(errorstr)
        return None
    else:
        logger.info("Connected to %s", uri)

    return connection


class LMIConnection(object):
    """
    Class representing a connection object. Each desired connection to separate
    CIMOM should have its own connection object created. This class provides an
    entry point to the namespace/classes/instances/methods hierarchy present in
    the LMIShell.

    :param string uri: URI of the CIMOM
    :param string username: account, under which, the CIM calls will be
        performed
    :param string password: user's password
    :param bool interactive: flag indicating, if the LMIShell client is running
        in the interactive mode; default value is False.
    :param bool use_cache: flag indicating, if the LMIShell client should use
        cache for CIMClass objects. This saves lot's of communication, if there
        are :func:`EnumerateInstances` and :func:`EnumerateClasses` intrinsic
        methods often issued. Default value is True.
    :param string key_file: path to x509 key file; default value is None
    :param string cert_file: path to x509 cert file; default value is None
    :param bool verify_server_cert: flag indicating, whether a server side
        certificate needs to be verified, if SSL used; default value is True

    **NOTE:** If interactive is set to True, LMIShell will:

    * prompt for username and password, if missing and connection via
      Unix socket can not be established.
    * use pager for the output of: :py:meth:`.LMIInstance.doc`,
      :py:meth:`.LMIClass.doc`, :py:meth:`.LMIInstance.tomof` and
      :py:meth:`.LMIMethod.tomof`
    """
    def __init__(self, uri, username="", password="", interactive=False,
                 use_cache=True, key_file=None, cert_file=None,
                 verify_server_cert=True):
        parse_res = urlparse.urlparse(uri)
        if parse_res.path != "/wsman":
            # We talk to CIMOM via CIM-XML
            self._client = LMIShellClient(
                uri, username, password, interactive=interactive,
                use_cache=use_cache, key_file=key_file,
                cert_file=cert_file, verify_server_cert=verify_server_cert)
        else:
            # We talk to CIMOM via WSMAN
            self._client = LMIWSMANClient(
                uri, username, password, interactive=interactive,
                key_file=key_file, cert_file=cert_file,
                verify_server_cert=verify_server_cert)

        self._indications = {}

        # Register LMIConnection.unsubscribe_all_indications() to be called at
        # LMIShell's exit.
        atexit.register(lambda: self.unsubscribe_all_indications())

    def __del__(self):
        """
        Disconnects and frees :py:class:`.LMICIMXMLClient` object.
        """
        try:
            self._client.disconnect()
            del self._client
        except AttributeError:
            pass

    def __repr__(self):
        """
        :returns: pretty string for the object.
        """
        return "%s(URI='%s', user='%s'...)" % (
            self.__class__.__name__, self._client.uri, self._client.username)

    @property
    def client(self):
        """
        :returns: CIMOM client
        :rtype: :py:class:`.LMICIMXMLClient` or :py:class:`.LMIWSMANClient`
        """
        return self._client

    @property
    def uri(self):
        """
        :returns: URI of the CIMOM
        :rtype: string
        """
        return self._client.uri

    @property
    def hostname(self):
        """
        :returns: hostname of CIMOM
        :rtype: string
        """
        return self._client.hostname

    @property
    def namespaces(self):
        """
        :returns: list of all available namespaces

        **Usage:** :ref:`namespaces_available_namespaces`.
        """
        return ["root"]

    @property
    def root(self):
        """
        :returns: :py:class:`.LMINamespaceRoot` object for *root* namespace
        """
        return LMINamespaceRoot(self)

    @property
    def timeout(self):
        """
        :returns: CIMOM connection timeout for a transaction (milliseconds)
        :rtype: int
        """
        return self._client._cliconn.timeout

    @timeout.setter
    def timeout(self, timeout):
        """
        Sets CIMOM connection timeout for a transaction (milliseconds).

        :param inst timeout: timeout in milliseconds
        """
        self._client._cliconn.timeout = timeout

    def print_namespaces(self):
        """
        Prints out all available namespaces.
        """
        sys.stdout.write("root\n")

    def get_namespace(self, namespace):
        """
        :param string namespace: namespace path (eg. `root/cimv2`)
        :returns: :py:class:`.LMINamespace` object
        :raises: :py:exc:`.LMINamespaceNotFound`
        """
        def get_namespace_priv(namespace, namespace_path):
            if not namespace_path:
                return namespace
            ns = namespace_path.pop(0)
            return get_namespace_priv(getattr(namespace, ns), namespace_path)

        namespace_path = namespace.split("/")
        ns = namespace_path.pop(0)
        if ns not in self.namespaces:
            raise LMINamespaceNotFound(ns)
        return get_namespace_priv(getattr(self, ns), namespace_path)

    def clear_cache(self):
        """
        Clears the cache.
        """
        if hasattr(self._client, "cache"):
            self._client.cache.clear()

    def use_cache(self, active=True):
        """
        Sets a bool flag, which defines, if the LMIShell should use a cache.

        :param bool active: whether the LMIShell's cache should be used
        """
        if hasattr(self._client, "cache"):
            self._client.cache.active = active

    def connect(self):
        """
        Connects to CIMOM and verifies credentials by performing a "dummy"
        request.

        :returns: :py:class:`.LMIReturnValue` object with rval set to True, if
            the user was properly authenticated; False otherwise. In case of
            any error, rval is set to False and errorstr contains appropriate
            error string.
        :rtype: :py:class:`.LMIReturnValue`
        """
        # Connect to CIMOM. We may fail before the actual "dummy" request is
        # sent. This only applies for LMIWBEM.
        rval, _, errorstr = self._client.connect()
        if not rval:
            return LMIReturnValue(rval=False, errorstr=errorstr)

        # Perform "dummy" request to check the connection and credentials.
        return self._client.dummy()

    def disconnect(self):
        """
        Disconnects from CIMOM.
        """
        self._client.disconnect()

    def is_wsman(self):
        """
        Returns True, if the connection is made with WSMAN CIMOM; False
        otherwise.
        """
        return isinstance(self._client, LMIWSMANClient)

    def subscribe_indication(self, **kwargs):
        """
        Subscribes to an indication. Indication is formed by 3 objects, where 2
        of them (filter and handler) can be provided, if the LMIShell should
        not create those 2 by itself.

        **NOTE:** Currently the call registers :py:mod:`atexit` hook, which
        auto-deletes all subscribed indications by the LMIShell.

        :param dictionary kwargs: parameters for the indication subscription

            * **Filter** (*LMIInstance*) -- if provided, the
              :py:class:`.LMIInstance` object will be used instead of creating
              a new one;
              **optional**
            * **Handler** (*LMIInstance*) -- if provided, the
              :py:class:`.LMIInstance` object will be used instead of creating
              a new one; **optional**
            * **Query** (*string*) -- string containing a query for the
              indications filtering
            * **QueryLanguage** (*string*) -- query language; eg. *WQL*, or
              *DMTF:CQL*.  This parameter is optional, default value is
              *DMTF:CQL*.
            * **Name** (*string*) -- indication name
            * **CreationNamespace** (*string*) -- creation namespace. This
              parameter is optional, default value is *root/interop*.
            * **SubscriptionCreationClassName** (*string*) -- subscription
              object class name. This parameter is optional, default value is
              *CIM_IndicationSubscription*.
            * **Permanent** (*bool*) -- whether to preserve the created
              subscription on LMIShell's quit. Default value is False.
            * **FilterCreationClassName** (*string*) -- creation class name of
              the filter object. This parameter is options, default value is
              *CIM_IndicationFilter*.
            * **FilterSystemCreationClassName** (*string*) -- system creation
              class name of the filter object. This parameter is optional,
              default value is *CIM_ComputerSystem*.
            * **FilterSourceNamespace** (*string*) -- local namespace where the
              indications originate. This parameter is optional, default value
              is *root/cimv2*.
            * **HandlerCreationClassName** (*string*) -- creation class name of
              the handler object. This parameter is optional, default value is
              *CIM_IndicationHandlerCIMXML*.
            * **HandlerSystemCreationClassName** (*string*) -- system creation
              name of the handler object. This parameter is optional, default
              value is *CIM_ComputerSystem*.
            * **Destination** (*string*) -- destination URI, where the
              indications should be delivered

        :returns: :py:class:`.LMIReturnValue` object with ``rval`` set to True,
            if indication was subscribed; False otherwise. If a error occurs,
            ``errorstr`` is set to appropriate error string.
        """
        if self.is_wsman():
            # TODO: support WSMAN events
            return LMIReturnValue(
                rval=False,
                errorstr="Indication subscription not supported")
        try:
            indication_namespace = kwargs.get(
                "CreationNamespace", "root/interop")
            cim_filter_provided = "Filter" in kwargs
            if cim_filter_provided:
                filt = kwargs["Filter"]
                cim_filter = None
                if isinstance(filt, LMIObjectFactory().LMIInstance):
                    cim_filter = filt._cim_instance
                elif isinstance(filt, wbem.CIMInstance):
                    cim_filter = filt
                else:
                    errorstr = "Filter argument accepts instances of " \
                        "CIMInstance or LMIInstance"
                    lmi_raise_or_dump_exception(LMIIndicationError(errorstr))
                    return LMIReturnValue(rval=False, errorstr=errorstr)
            else:
                cim_filter_props = {
                    "CreationClassName": kwargs.get(
                        "FilterCreationClassName",
                        "CIM_IndicationFilter"),
                    "SystemCreationClassName": kwargs.get(
                        "FilterSystemCreationClassName",
                        "CIM_ComputerSystem"),
                    "SourceNamespace": kwargs.get(
                        "FilterSourceNamespace",
                        "root/cimv2"),
                    "SystemName": self._client.uri,
                    "Query": kwargs["Query"],
                    "QueryLanguage": kwargs.get(
                        "QueryLanguage",
                        LMICIMXMLClient.QUERY_LANG_CQL),
                    "Name": kwargs["Name"] + "-filter"
                }
                cim_filter, _, errorstr = self._client.create_instance(
                    cim_filter_props["CreationClassName"],
                    indication_namespace,
                    self.hostname,
                    cim_filter_props
                )
                if not cim_filter:
                    lmi_raise_or_dump_exception(LMIIndicationError(errorstr))
                    return LMIReturnValue(rval=False, errorstr=errorstr)
            cim_handler_provided = "Handler" in kwargs
            if cim_handler_provided:
                cim_handler = kwargs["Handler"]._cim_instance
            else:
                cim_handler_props = {
                    "CreationClassName": kwargs.get(
                        "HandlerCreationClassName",
                        "CIM_IndicationHandlerCIMXML"),
                    "SystemCreationClassName": kwargs.get(
                        "HandlerSystemCreationClassName",
                        "CIM_ComputerSystem"),
                    "SystemName": self._client.uri,
                    "Destination": "%s/CIMListener/%s" % (
                        kwargs["Destination"],
                        kwargs["Name"]),
                    "Name": kwargs["Name"] + "-handler"
                }
                cim_handler, _, errorstr = self._client.create_instance(
                    cim_handler_props["CreationClassName"],
                    indication_namespace,
                    self.hostname,
                    cim_handler_props)
                if not cim_handler:
                    if "Filter" not in kwargs:
                        self._client.delete_instance(cim_filter.path)
                    lmi_raise_or_dump_exception(LMIIndicationError(errorstr))
                    return LMIReturnValue(rval=False, errorstr=errorstr)
            cim_subscription_props = {
                "Filter": cim_filter.path,
                "Handler": cim_handler.path
            }
            cim_subscription, _, errorstr = self._client.create_instance(
                kwargs.get(
                    "SubscriptionCreationClassName",
                    "CIM_IndicationSubscription"),
                indication_namespace,
                self.hostname,
                cim_subscription_props)
            if not cim_subscription:
                if "Filter" not in kwargs:
                    self._client.delete_instance(cim_filter.path)
                if "Handler" not in kwargs:
                    self._client.delete_instance(cim_handler.path)
                lmi_raise_or_dump_exception(LMIIndicationError(errorstr))
                return LMIReturnValue(rval=False, errorstr=errorstr)
            # XXX: Should we auto-delete all the indications?
            permanent = kwargs.get("Permanent", False)
            self._indications[kwargs["Name"]] = LMISubscription(
                self._client,
                (cim_filter, not cim_filter_provided),
                (cim_handler, not cim_handler_provided),
                cim_subscription,
                permanent)
        except KeyError, e:
            errorstr = "Not all necessary parameters provided, missing: %s" % e
            lmi_raise_or_dump_exception(LMIIndicationError(errorstr))
            return LMIReturnValue(rval=False, errorstr=errorstr)
        return LMIReturnValue(rval=True)

    def unsubscribe_indication(self, name):
        """
        Unsubscribes an indication.

        :param string name: indication name
        :returns: :py:class:`.LMIReturnValue` object with ``rval`` set to True,
            if unsubscribed; False otherwise
        """
        if name not in self._indications:
            errorstr = "No such indication"
            lmi_raise_or_dump_exception(LMIIndicationError(errorstr))
            return LMIReturnValue(rval=False, errorstr=errorstr)
        indication = self._indications.pop(name)
        indication.delete()
        return LMIReturnValue(rval=True)

    def unsubscribe_all_indications(self):
        """
        Unsubscribes all the indications. This call ignores *Permanent* flag,
        which may be provided in
        :py:meth:`.LMIConnection.subscribe_indication`, and deletes all the
        subscribed indications.
        """
        for subscription in self._indications.values():
            if not subscription.permanent:
                subscription.delete()
        self._indications = {}

    def print_subscribed_indications(self):
        """
        Prints out all the subscribed indications.
        """
        for i in self._indications.keys():
            sys.stdout.write("%s\n" % i)

    def subscribed_indications(self):
        """
        :returns: list of all the subscribed indications
        """
        return self._indications.keys()
