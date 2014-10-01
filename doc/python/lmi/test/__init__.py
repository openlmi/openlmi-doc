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

# hack to use lmi.test.unittest as common module for unittest or unittest2,
# based on python version
import sys
if sys.version_info[0] > 2 or sys.version_info[1] > 6:
    import unittest
else:
    import unittest2 as unittest

# If lmiwbem is not available, fallback to pywbem.
try:
    import lmiwbem as wbem
except ImportError:
    import pywbem as wbem

# Ensure that CIMError is defined.
# Two possible cases:
#   1. We use newer lmi.shell on top of lmiwbem that exports its own CIMError.
#   2. We use older lmi.shell without its own CIMError.
try:
    # Prefer LMIShell's abstraction.
    from lmi.shell.LMIExceptions import CIMError
except ImportError:
    # Fallback to wbem's CIMError
    try:
        from lmiwbem import CIMError
    except ImportError:
        from pywbem import CIMError
