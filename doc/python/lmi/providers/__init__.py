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
#
# Authors: Michal Minar <miminar@redhat.com>
#
"""
Common utilities for OpenLMI python providers.
"""

import socket

def parse_instance_id(instance_id, classname=None):
    """
    Parse InstanceID, check it has LMI:<classname>:<ID> format and return
    the ID. Return None if the format is bad.
    :param instance_id: (``string``) String to parse.
    :param classname: (``string``) Name of class, whose InstanceID we parse.
        If the classname is None, it won't be checked.
    :returns: ``string`` with the ID.
    """
    parts = instance_id.split(":", 2)
    if len(parts) != 3:
        return None
    if parts[0] != "LMI":
        return None
    real_classname = parts[1]
    if classname and real_classname.lower() != classname.lower():
        return None
    return parts[2]

def is_this_system(system_name):
    """
    Return ``True`` if given *system_name* matches the hostname of currently
    running system.

    Global configuration object must be initialized before calling this
    function.

    :rtype: boolean
    """
    try:
        return (  socket.gethostbyaddr(system_name)[0]
               == socket.gethostbyaddr(socket.gethostname())[0])
    except socket.gaierror:     # name resolution failed
        if system_name == socket.gethostname():
            # hostname can not be translated to IP
            return True
        return False
