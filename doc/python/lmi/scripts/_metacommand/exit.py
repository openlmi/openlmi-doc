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
Module containing help command.
"""

from lmi.scripts.common import get_logger
from lmi.scripts.common.command import LmiEndPointCommand
from lmi.scripts.common import errors

LOG = get_logger(__name__)

EXIT_CODE_SUCCESS = 0
EXIT_CODE_FAILURE = 1
EXIT_CODE_KEYBOARD_INTERRUPT = 2
EXIT_CODE_COMMAND_NOT_FOUND = 3
EXIT_CODE_INVALID_SYNTAX = 4
EXIT_CODE_UNSATISFIED_DEPENDENCIES = 5

def _execute_exit(exit_code):
    """ Associated function with ``Exit`` command. """
    raise errors.LmiTerminate(exit_code)

class Exit(LmiEndPointCommand):
    """
    Terminate the shell.

    Usage: %(cmd)s [<exit_code>]
    """
    CALLABLE = _execute_exit
    OWN_USAGE = True

    def verify_options(self, options):
        code = options['<exit_code>']
        if code is not None:
            try:
                int(code)
            except ValueError:
                raise errors.LmiInvalidOptions(
                        "<exit_code> must be an integer not \"%s\"" % code)

    def transform_options(self, options):
        code = options.get('<exit_code>', None)
        if code is None:
            code = EXIT_CODE_SUCCESS
        options['<exit_code>'] = int(code)

