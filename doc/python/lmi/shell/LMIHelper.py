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
import subprocess
from site import _Helper


class LMIHelper(_Helper):
    """
    LMI Helper class, which overrides python help.
    """
    def __repr__(self):
        """
        :returns: pretty string for the object.
        """
        return "Type help() to see man page for lmishell, " \
            "or help(object) for help about object."

    def __call__(self, request=None):
        """
        Executes either man page for LMIShell or prints pydoc help for an
        object.
        """
        if request is None:
            try:
                # Python 3+
                from subprocess import DEVNULL as devnull
                devnull_close = lambda: None
            except ImportError:
                devnull = open(os.devnull, "wb")
                devnull_close = lambda: devnull.close()
            rcode = subprocess.call(["man", "lmishell"], stderr=devnull)
            devnull_close()
            if rcode > 0:
                sys.stderr.write("Man page for lmishell can not be found, ")
                sys.stderr.write("refer to official documentation.\n\n")
                sys.stderr.write("Available at: http://www.openlmi.org\n")
        else:
            import pydoc
            return pydoc.help(request)
