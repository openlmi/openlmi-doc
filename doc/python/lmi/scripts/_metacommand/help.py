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

from lmi.scripts.common import errors
from lmi.scripts.common import get_logger
from lmi.scripts.common.command import LmiEndPointCommand
from lmi.scripts._metacommand import cmdutil
from lmi.scripts._metacommand import exit

LOG = get_logger(__name__)

class Help(LmiEndPointCommand):
    """
    Print the list of supported commands with short description.
    If a subcommand is given, its detailed help will be printed.

    Usage: %(cmd)s [<subcommand>...]
    """
    OWN_USAGE = True

    def execute(self, subcommand):
        mgr = self.app.command_manager
        node = self.app.active_command
        toplevel = self
        while toplevel.parent is not None:
            toplevel = toplevel.parent

        if node or subcommand:
            # Help for some subcommand will be printed.
            if node is None:
                node = toplevel
            if subcommand:
                index = 0
                try:
                    while index < len(subcommand) and not node.is_end_point():
                        while node.is_selector():
                            cmd_factory, _ = node.select_cmds().next()
                            node = cmd_factory(self.app, node.cmd_name,
                                    node.parent)
                        # selector may return either multiplexer or end-point
                        if node.is_end_point():
                            break
                        cmd_factory = cmdutil.get_subcommand_factory(node,
                                subcommand[index])
                        node = cmd_factory(self.app, subcommand[index], node)
                        index += 1
                except errors.LmiCommandNotFound as err:
                    LOG().error(str(err))
            if node is not toplevel:
                self.app.stdout.write(node.get_usage(True))
                if node is self.app.active_command:
                    # show additional information only when no command given
                    self.app.stdout.write('\nTo get help for built-in commands,'
                            ' type:\n    :help\n')
                return exit.EXIT_CODE_SUCCESS

        # let's print the summary of available commands
        self.app.stdout.write("Commands:\n")
        max_cmd_len = max(len(n) for n in mgr)
        cmd_line = "  %%-%ds - %%s\n" % max_cmd_len
        for cmd in sorted(mgr):
            self.app.stdout.write(cmd_line
                    % (cmd, mgr[cmd].get_description()
                        .strip().split("\n", 1)[0]))
        self.app.stdout.write(
                "\nFor more informations about particular command type:\n"
                "    help <command>\n")

        return exit.EXIT_CODE_SUCCESS

