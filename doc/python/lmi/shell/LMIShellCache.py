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

from lmi.shell.compat import *


class LMIClassCacheEntry(object):
    """
    Class used for storing :py:class:`wbem.CIMClass` in
    :py:class:`.LMIShellCache`.

    :param CIMClass cim_class: :py:class:`wbem.CIMClass` to cache
    :param bool full_fetch: True, if class is cached with qualifiers
    """
    def __init__(self, cim_class, full_fetch):
        self.cim_class = cim_class
        self.full_fetch = full_fetch


class LMIShellCache(object):
    """
    Class representing a LMIShell cache.

    :param bool active: specifies, if the cache is active
    :param list classname_list: list of strings of cached class names
    :param dictionary class_dict: cached :py:class:`wbem.CIMClass` objects,
        where the key is the class name and value is :class:`CIMClass` object
    :param dictionary class_superclass_dict: dictionary, where the key is
        namespace and value is dictionary of classname:superclass
    """
    def __init__(self, active=True, classname_dict=None, class_dict=None,
                 class_superclass_dict=None):
        self._classname_dict = classname_dict \
            if classname_dict is not None else {}
        self._class_dict = class_dict if class_dict is not None else {}
        self._class_superclass_dict = class_superclass_dict \
            if class_superclass_dict is not None else {}
        self._active = active

    def clear(self):
        """
        Clears the cache.
        """
        self._classname_dict = {}
        self._class_dict = {}
        self._class_superclass_dict = {}

    def get_classes(self, namespace=wbem.DEFAULT_NAMESPACE):
        """
        :param string namespace: namespace storing cached classes
        :returns: list of cached class names or None, if no cached
            classes is stored
        """
        return self._classname_dict.get(namespace, None)

    def set_classes(self, classname_list, namespace=wbem.DEFAULT_NAMESPACE):
        """
        Stores a new class names' list.

        :param string namespace: namespace storing cached classes
        """
        self._classname_dict[namespace] = classname_list

    def get_class(self, classname, namespace=wbem.DEFAULT_NAMESPACE):
        """
        :param string classname: cached class name
        :param string namespace: namespace storing cached classes
        :returns: cache object, if proper class name provided, None otherwise
        :rtype: :py:class:`.LMIClassCacheEntry`
        """
        if namespace not in self._class_dict or \
                classname not in self._class_dict[namespace]:
            return None
        return self._class_dict[namespace][classname]

    def add_class(self, cim_class, namespace=wbem.DEFAULT_NAMESPACE,
                  full_fetch=False):
        """
        Stores a new :py:class:`wbem.CIMClass` object into the cache.

        :param CIMClass cim_class: :py:class:`wbem.CIMClass` object
        :param string namespace: namespace storing cached classes
        """
        if namespace not in self._class_dict:
            self._class_dict[namespace] = {}
        self._class_dict[namespace][cim_class.classname] = LMIClassCacheEntry(
            cim_class, full_fetch)

    def has_superclass(self, classname, namespace):
        """
        :param string classname: cached class name
        :param string namespace: namespace name
        :returns: True, if the cache contains superclass to the given class
            name; False otherwise
        """
        if namespace not in self._class_superclass_dict:
            return False
        if classname not in self._class_superclass_dict[namespace]:
            return False
        return True

    def get_superclass(self, classname, namespace):
        """
        :param string classname: cached class name
        :param string namespace: namespace name
        :returns: cached superclass to the given class name
        :rtype: string
        """
        if not self.has_superclass(classname, namespace):
            return None
        return self._class_superclass_dict[namespace][classname]

    def add_superclass(self, classname, superclass, namespace):
        """
        Stores a new pair classname : superclassname into the cache.

        :param string classname: class name to be stored
        :param string superclass: super class name to be stored
        :param string namespace: namespace name of the classname
        """
        if namespace not in self._class_superclass_dict:
            self._class_superclass_dict[namespace] = {}
        self._class_superclass_dict[namespace][classname] = superclass

    @property
    def active(self):
        """
        :returns: True, if the cache is active; False otherwise
        """
        return self._active

    @active.setter
    def active(self, val):
        """
        Property setter for the property active.
        """
        self._active = val
