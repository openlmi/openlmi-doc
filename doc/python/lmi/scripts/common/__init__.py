# Copyright (C) 2013-2014 Michal Minar <miminar@redhat.com>
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
"""
Package with client-side python modules and command line utilities.
"""

import logging

from lmi.shell import LMINamespace
from lmi.shell import LMIExceptions
from lmi.scripts.common.configuration import Configuration
from lmi.scripts.common.lmi_logging import get_logger

LOG = get_logger(__name__)

def get_computer_system(ns):
    """
    Obtain an instance of ``CIM_ComputerSystem`` or its subclass. Preferred
    class name can be configured in configuration file. If such class does
    not exist, a base class (``CIM_ComputerSystem``) is enumerated instead.
    First feasible instance is cached and returned.

    :param ns: Namespace object where to look for computer system class.
    :type ns: :py:class:`lmi.shell.LMINamespace`
    :returns: Instance of ``CIM_ComputerSystem``.
    :rtype: :py:class:`lmi.shell.LMIInstance`.
    """
    if not isinstance(ns, LMINamespace):
        raise TypeError("ns must be an instance of LMINamespace")
    if not hasattr(get_computer_system, '_cs_cache'):
        get_computer_system._cs_cache = {}
    ns_path = ns.connection.uri + '/' + ns.name
    if not ns_path in get_computer_system._cs_cache:
        config = Configuration.get_instance()
        try:
            get_computer_system._cs_cache[ns_path] = cs = \
                    getattr(ns, config.system_class_name).first_instance()
        except LMIExceptions.LMIClassNotFound:
            LOG().warn('Failed to get instance of %s on host "%s"'
                    ' - falling back to CIM_ComputerSystem.',
                    config.system_class_name, ns.connection.uri)
            get_computer_system._cs_cache[ns_path] = cs = \
                    ns.CIM_ComputerSystem.first_instance_name()
        LOG().debug('Loaded instance of %s:%s for host "%s".',
            ns.name, cs.classname, ns.connection.uri)
    return get_computer_system._cs_cache[ns_path]
