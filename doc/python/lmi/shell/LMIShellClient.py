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

from lmi.shell.LMICIMXMLClient import LMICIMXMLClient
from lmi.shell.LMIReturnValue import LMIReturnValue
from lmi.shell.LMIShellCache import LMIShellCache


class LMIShellClient(LMICIMXMLClient):
    """
    :class:`.LMIShellClient` overrides few methods due to caching purposes.

    :param string uri: URI of the CIMOM
    :param string username: account, under which, the CIM calls will be
        performed
    :param string password: user's password
    :param bool interactive: flag indicating, if the LMIShell client is running
        in the interactive mode; default value is False.
    :param bool use_cache: flag indicating, if the LMIShell client should use
        cache for :class:`CIMClass` objects. This saves a lot's of
        communication, if there is often the
        :meth:`.LMIShellClient.get_class_names()` or
        :meth:`.LMIShellClient.attr.get_class()` call issued.

    :param string key_file: path to x509 key file; default value is None
    :param string cert_file: path to x509 cert file; default value is None
    :param bool verify_server_cert: indicates, whether a server side
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
        super(LMIShellClient, self).__init__(
            uri, username, password, key_file=key_file,
            cert_file=cert_file, verify_server_cert=verify_server_cert)
        self._interactive = interactive
        self._cache = LMIShellCache(use_cache)

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
            otherwise ``rval`` is set to None and ``errorstr`` contains an
            appropriate error string
        :raises: :py:exc:`.CIMError`, :py:exc:`.ConnectionError`
        """
        if self._cache.active:
            class_list = self._cache.get_classes(namespace)
            if class_list is None:
                class_list, _, errorstr = LMICIMXMLClient.get_class_names(
                    self, namespace, ClassName, DeepInheritance)
                if not class_list:
                    return LMIReturnValue(rval=class_list, errorstr=errorstr)
                self._cache.set_classes(class_list, namespace)
            return LMIReturnValue(rval=class_list)
        return LMICIMXMLClient.get_class_names(
            self, namespace, ClassName, DeepInheritance)

    def get_class(self, classname, namespace=None, LocalOnly=True,
                  IncludeQualifiers=True, IncludeClassOrigin=False,
                  PropertyList=None, full_fetch=False):
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
            set to none and errorstr to appropriate error string
        :raises: :py:exc:`.CIMError`, :py:exc:`.ConnectionError`
        """
        if full_fetch:
            IncludeQualifiers = full_fetch
            IncludeClassOrigin = full_fetch

        if self._cache.active:
            cls_cache_entry = self._cache.get_class(classname, namespace)
            if cls_cache_entry is None or \
                    (not cls_cache_entry.full_fetch and full_fetch):
                cls, _, errorstr = LMICIMXMLClient.get_class(
                    self, classname, namespace, LocalOnly, IncludeQualifiers,
                    IncludeClassOrigin, PropertyList)
                if cls is None:
                    return LMIReturnValue(rval=cls, errorstr=errorstr)
                self._cache.add_class(cls, namespace, full_fetch)
                self._cache.add_superclass(
                    cls.classname, cls.superclass, namespace)
            else:
                cls = cls_cache_entry.cim_class
            return LMIReturnValue(rval=cls)
        return LMICIMXMLClient.get_class(
            self, classname, namespace, LocalOnly, IncludeQualifiers,
            IncludeClassOrigin, PropertyList)

    def get_superclass(self, classname, namespace=None):
        """
        Returns string of a superclass to given class, if such superclass
        exists, None otherwise.

        :param string classname: class name
        :param string namespace: namespace name
        :returns: superclass name to a given classname or None
        :raises: :exc:`CIMError`, :exc:`ConnectionError`
        """
        if self._cache.active:
            rparams = None
            errorstr = ""
            if self._cache.has_superclass(classname, namespace):
                superclass = self._cache.get_superclass(classname, namespace)
            else:
                superclass, rparams, errorstr = LMICIMXMLClient.get_superclass(
                    self, classname, namespace)
                self._cache.add_superclass(classname, superclass, namespace)
            return LMIReturnValue(
                rval=superclass, rparams=rparams, errorstr=errorstr)
        return LMICIMXMLClient.get_superclass(self, classname, namespace)

    @property
    def interactive(self):
        """
        :returns: flag, if the LMIShell is run in the interactive mode
        :rtype: bool
        """
        return self._interactive

    @interactive.setter
    def interactive(self, i):
        """
        Property setter for interactive flag.

        :param bool i: new :attr:`.LMIShellClient.interactive` state
        """
        self._interactive = bool(i)

    @property
    def cache(self):
        """
        :returns: LMIShell's cache
        :rtype: :py:class:`.LMIShellCache`
        """
        return self._cache

    @property
    def use_cache(self):
        """
        :returns: flag, which tells, if the LMIShell should use a cache
        :rtype: bool
        """
        return self._cache.active

    @use_cache.setter
    def use_cache(self, active):
        """
        Property setter for cache activity.

        :param bool active: new :attr:LMIShellClient.use_cache` state
        """
        self._cache.active = active
