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

"""
LMIShell compatibility module. It imports WBEM backend modules and sets
necessary attributes to either LMIWBEM or PyWBEM.
"""

import sys

from lmi.shell.LMIShellLogger import lmi_get_logger

logger = lmi_get_logger()

# First, try to import LMIWBEM module.
try:
    HAVE_LMIWBEM = True

    import lmiwbem as wbem

    logger.debug("Using LMIWBEM backend")

    class Error(Exception):
        pass

    class AuthError(Error):
        pass

    # We add thse exceptions to LMIWBEM module, so that exception handlers in
    # lmi.shell.LMIDecorators can catch also these types. They exist due to
    # PyWBEM module.
    setattr(wbem, "Error", Error)
    setattr(wbem, "AuthError", AuthError)
except ImportError, e:
    HAVE_LMIWBEM = False

    # LMIWBEM could not be imported, fall back to PyWBEM.
    try:
        import pywbem as wbem
    except ImportError, e:
        # We can't import any backend, exit with error!
        logger.error("Can't import either lmiwbem or pywbem module.")
        sys.exit(1)

    logger.debug("Using PyWBEM backend")

    from lmi.shell.compat.CIMIndicationListener import CIMIndicationListener

    class ConnectionError(Exception):
        pass

    class NocaseDict(wbem.NocaseDict):
        """
        :py:class:`pywbem.NocaseDict` with compatibility API
        """
        def get(self, key, default=None):
            if key in self:
                return self[key]
            else:
                return default

        def pop(self, key, default=None):
            if key in self:
                rval = self[key]
                del self[key]
                return rval
            else:
                return default

    # We add these exception to PyWBEM module, so that exception handlers in
    # lmi.shell.LMIDecorators can catch also these types. They exist due to
    # LMIWBEM module.
    setattr(wbem, "ConnectionError", ConnectionError)
    setattr(wbem, "AuthError", wbem.cim_http.AuthError)

    # PyWBEM does not define any indication listener. We need to define one in
    # this compat module and provide it to PyWBEM module.
    setattr(wbem, "CIMIndicationListener", CIMIndicationListener)

    # NocaseDict defined in PyWBEM does not provide .pop() and .get() methods.
    # So we define them in our subclass of pywbem.NocaseDict and add necessary
    # interface.
    delattr(wbem, "NocaseDict")
    setattr(wbem, "NocaseDict", NocaseDict)
