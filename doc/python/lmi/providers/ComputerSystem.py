# -*- encoding: utf-8 -*-
# Software Management Providers
#
# Copyright (C) 2012-2014 Red Hat, Inc.  All rights reserved.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
"""
Just a common functionality related to associated class ``CIM_ComputerSystem``.
"""

import pywbem

from lmi.base.BaseConfiguration import BaseConfiguration
from lmi.providers import cmpi_logging
from lmi.providers import is_this_system

class UninitializedError(Exception):
    """
    Raised when the initialization parameter is not passed to function upon
    its first invocation.
    """
    pass

class NotInstrumentedError(Exception):
    """
    Raised when some CIM class is not instrumented in current *CIMOM*.
    """
    pass

@cmpi_logging.trace_function
def get_path(env=None):
    """
    Get the instance name of preferred computer system. Instance is cached,
    so the broker is accessed just upon the first invocation. Confiruation
    instance must be instantiated before this function is called.

    :param ProviderEnvironment env: Provider environment, taken from CIMOM
        callback (e.g. ``get_providers()``). It's needed just upon the first
        invocation.
    :returns: Instance of ``CIM_ComputerSystem``. Exact subclass is defined
        in configuration file.
    :rtype: :py:class:`pywbem.CIMInstanceName`
    """
    if not hasattr(get_path, '_instance'):
        if env is None:
            raise UninitializedError("get_computer_system_path() needs to be"
                    " given environment object at first invocation")
        inames = [ i for i in env.get_cimom_handle().EnumerateInstanceNames(
                        "root/cimv2",
                        BaseConfiguration.INSTANCE.system_class_name) ]
        if len(inames) < 1:
            raise NotInstrumentedError("CIM_ComputerSystem class is not"
                    " instrumented or EnumerateInstanceNames() operation"
                    " is not supported")
        get_path._instance = inames[0]
    return get_path._instance.copy()

@cmpi_logging.trace_function
def get_system_name(env=None):
    """
    Get the name of system contained in a ``Name`` property of instance of
    ``CIM_ComputerSystem``.

    :param ProviderEnvironment env: Provider environment, taken from CIMOM
        callback (e.g. ``get_providers()``). It's needed only upon a
        first invocation of this function or
        :py:func:`get_computer_system_path`.
    :returns: Name of computer system.
    :rtype: string
    """
    return get_path(env)["Name"]

@cmpi_logging.trace_function
def check_path(env, system, prop_name):
    """
    Checks instance name of ``CIM_ComputerSystem``. If the object path matches
    this computer system, ``True`` is returned. Exception is raised otherwise.
    Especially useful when checking arguments of instance's method taking
    reference to computer system an argument.

    :param system: Instance name of computer system to check.
    :type system: :py:class:`pywbem.CIMInstanceName`
    :param string prop_name: Name of argument or property referring to the object
        path being checked. This is used in exception messages upon
        unsuccessful checks.
    :returns: ``True``
    :rtype: boolean
    """
    if not isinstance(system, pywbem.CIMInstanceName):
        raise pywbem.CIMError(pywbem.CIM_ERR_INVALID_PARAMETER,
                "\"%s\" must be a CIMInstanceName" % prop_name)
    our_system = get_path(env)
    ch = env.get_cimom_handle()
    if system.namespace != our_system.namespace:
        raise pywbem.CIMError(pywbem.CIM_ERR_NOT_FOUND,
                'Namespace of "%s" does not match "%s"' % (
                    prop_name, our_system.namespace))
    if not ch.is_subclass(our_system.namespace,
            sub=system.classname,
            super="CIM_ComputerSystem"):
        raise pywbem.CIMError(pywbem.CIM_ERR_NOT_FOUND,
                "Class of \"%s\" must be a sublass of %s" % (
                    prop_name, our_system.classname))
    if not 'CreationClassName' in system or not 'Name' in system:
        raise pywbem.CIMError(pywbem.CIM_ERR_NOT_FOUND,
                "\"%s\" is missing one of keys", prop_name)
    if not ch.is_subclass(our_system.namespace,
            sub=system['CreationClassName'],
            super="CIM_ComputerSystem"):
        raise pywbem.CIMError(pywbem.CIM_ERR_NOT_FOUND,
                "CreationClassName of \"%s\" must be a sublass of %s" % (
                prop_name, our_system.classname))
    if not is_this_system(system['Name']):
        raise pywbem.CIMError(pywbem.CIM_ERR_NOT_FOUND,
                "Name of \"%s\" does not match \"%s\"" % (
                prop_name, our_system['Name']))
    return True

@cmpi_logging.trace_function
def check_path_property(env, op, prop_name):
    """
    This checks, whether the object path contains correct instance name of
    ``CIM_ComputerSystem`` corresponding to this system. If not, an exception
    is raised.

    Example usage in ``get_instance()`` method of provider: ::

        # body of get_instance() method of some association class having
        # *System* property referring to an instance of *CIM_ComputerSystem*.
        ComputerSystem.check_path_property(env, model, "System")

    :param op: Object path to check.
    :param string prop_name: Name of property referring to the object path being
        checked. This is used in exception messages when check is unsuccessful.
    :returns: ``True``
    :rtype: boolean
    """
    if not prop_name in op:
        raise pywbem.CIMError(pywbem.CIM_ERR_INVALID_PARAMETER,
                "Missing %s key property!" % prop_name)
    return check_path(env, op[prop_name], prop_name)

