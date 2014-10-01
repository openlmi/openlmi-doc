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
Utility functions for command inspection.
"""
from lmi.scripts.common import errors
from lmi.scripts.common.command import LmiBaseCommand
from lmi.scripts.common.command import LmiCommandMultiplexer

def get_subcommand_names(command):
    """
    :param command: Either a multiplexer command or top-level one.
    :returns: Names of children commands.
    :rtype: list
    """
    if not isinstance(command, LmiBaseCommand):
        raise TypeError("command must be an instance of LmiBaseCommand")
    if isinstance(command, LmiCommandMultiplexer):
        return command.child_commands().keys()
    if command.parent is None:  # top level command
        return command.app.command_manager.command_names
    raise ValueError("command must be either multiplexer or top-level command")

def get_subcommand_factory(command, name):
    """
    :param command: Either a multiplexer command or top-level one.
    :returns: Callable returning an instance of
        :py:class:`~lmi.scripts.common.command.multiplexer.LmiCommandMultiplexer`
    :rtype: callable
    """
    if isinstance(command, LmiCommandMultiplexer):
        try:
            return command.child_commands()[name]
        except KeyError:
            cmd_path = command.cmd_name_parts
            cmd_path.append(name)
            raise errors.LmiCommandNotFound(" ".join(cmd_path))
    if command.parent is None:  # top level command
        return command.app.command_manager.find_command(name)
    raise ValueError("command must be either multiplexer or top-level command")

