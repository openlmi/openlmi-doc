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

import abc
import sys
import re

from lmi.shell.LMIShellLogger import lmi_get_logger
from lmi.shell.LMIUtil import lmi_cast_to_lmi

logger = lmi_get_logger()


class LMIConstantValues(object):
    """
    Abstract class for constant value objects.

    :param cim_obj: this object is either of type
        :py:class:`wbem.CIMParameter`, :py:class:`wbem.CIMProperty` or
        :py:class:`wbem.CIMMethod`. Construction of this object requires to
        have a member ``_cast_type`` to properly cast CIM object. When
        constructing derived objects, make sure, that the mentioned member is
        present before calling this constructor.
    :param cast_type: parameter/property cast type
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, cim_obj, cast_type):
        items = zip(
            cim_obj.qualifiers["Values"].value,
            cim_obj.qualifiers["ValueMap"].value)
        self._value_map = {}
        self._value_map_inv = {}
        self._cast_type = cast_type
        # Fill two dictionaries for bidirectional access to constant values.
        cnt = 1
        for key, value in items:
            try:
                # Cast constant value first. If we get ValueError, no key
                # modifications are necessary.
                val = lmi_cast_to_lmi(self._cast_type, value)

                # Keys can contain various undesirable characters, such as
                # python operators, etc. So we drop them.
                mod_key = re.sub("\W", "", key)
                if mod_key[0].isdigit():
                    mod_key = "Key_" + mod_key
                if mod_key in self._value_map:
                    mod_key += str(cnt)
                    cnt += 1
                    logger.warn("Constant value mapped as: '%s' -> '%s'" %
                                (key, mod_key))

                self._value_map[mod_key] = val
                # For inverse mapping, we use unmodified key.
                self._value_map_inv[val] = key
            except ValueError, e:
                # Can not cast such value as interval. Can be found in
                # DMTFReserved, VendorReserved values.
                pass

    def __repr__(self):
        """
        Returns a string of all constant names with corresponding value.

        :returns: pretty string
        """
        result = ""
        for k, v in self._value_map.iteritems():
            result += "%s = %s\n" % (k, v)
        return result[:-1]

    def __getattr__(self, name):
        """
        Returns either a member of the class, or a constant value.

        Simplifies the code and constant value can be retrieved by
        :samp:`object.constant_value`.

        :param string name: member to retrieve
        :returns: class member
        """
        if name in self._value_map:
            return self._value_map[name]
        raise AttributeError(name)

    def print_values(self):
        """
        Prints all available constant names.

        **Usage:** :ref:`class_get_valuemap_properties`.
        """
        for k in self._value_map.keys():
            sys.stdout.write("%s\n" % k)

    def values_dict(self):
        """
        :returns: dictionary of constants' names and values
        """
        return self._value_map

    def values(self):
        """
        :returns: list of all available constant values
        """
        return self._value_map.keys()

    def value(self, value_name):
        """
        :param string value_name: constant name
        :returns: constant value

        **Usage:** :ref:`class_get_valuemap_property_value`.
        """
        return getattr(self, value_name)

    def value_name(self, value):
        """
        :param int value: numeric constant value
        :returns: constant value
        :rtype: string

        **Usage:** :ref:`class_get_valuemap_property_name`.
        """
        return self._value_map_inv[value]


class LMIConstantValuesParamProp(LMIConstantValues):
    """
    Derived class used for constant values of :py:class:`wbem.CIMProperty` and
    :py:class:`wbem.CIMParameter`.

    :param cim_property: :py:class:`wbem.CIMProperty` or
        :py:class:`wbem.CIMParameter` object. Both objects have necessary
        member ``type`` which is needed for proper casting.
    """
    def __init__(self, cim_property):
        super(LMIConstantValuesParamProp, self).__init__(
            cim_property, cim_property.type)


class LMIConstantValuesMethodReturnType(LMIConstantValues):
    """
    Derived class used for constant values of :py:class:`wbem.CIMMethod`.

    :param CIMMethod cim_method: :py:class:`wbem.CIMMethod` object
    """
    def __init__(self, cim_method):
        super(LMIConstantValuesMethodReturnType, self).__init__(
            cim_method, cim_method.return_type)
