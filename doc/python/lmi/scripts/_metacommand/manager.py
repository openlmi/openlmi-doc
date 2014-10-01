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
Manager module for direct subcommands of lmi metacommand. Most of them are
loaded from entry_points of installed python eggs.
"""

import pkg_resources

from lmi.scripts.common import Configuration
from lmi.scripts.common import errors
from lmi.scripts.common import get_logger
from lmi.scripts.common.command import base
from lmi.scripts.common.command import util

LOG = get_logger(__name__)

class _CustomCommandWrapper(object):
    """
    Provide an interface mocking an entry_point object for custom commands
    added by lmi metacommand application.

    :param name: (``str``) Name of command.
    :param cmd_class: (``LmiBaseCommand``) Factory for custom commands.
    """

    def __init__(self, name, cmd_class):
        if not isinstance(name, basestring):
            raise TypeError("name must be a string")
        if not issubclass(cmd_class, base.LmiBaseCommand):
            raise TypeError("cmd_class must be a LmiBaseCommand")
        self._name = name
        self._cmd_class = cmd_class

    @property
    def name(self):
        """ Return command name. """
        return self._name

    def load(self):
        """ Return command class. """
        return self._cmd_class

class CommandManager(object):
    """
    Manager of direct subcommands of lmi metacommand. It manages commands
    registered with entry_points under particular namespace installed by
    python eggs. Custom commands may also be added.

    :param namespace: (``str``) Namespace, where commands are registered.
        For example ``lmi.scripts.cmd``.
    """

    def __init__(self, namespace=None):
        if namespace is not None and not isinstance(namespace, basestring):
            raise TypeError("namespace must be a string")
        if namespace is None:
            namespace = Configuration.get_instance().get_safe(
                    "Main", "CommandNamespace")
        self._namespace = namespace
        self._commands = {}
        self._load_commands()

    @property
    def command_names(self):
        """ Returns list of command names. """
        return self._commands.keys()

    def __len__(self):
        return len(self._commands)

    def __iter__(self):
        """ Yields command names. """
        return iter(self._commands)

    def __getitem__(self, cmd_name):
        """ Gets command factory for name. """
        return self.find_command(cmd_name)

    def _load_commands(self):
        """ Loads commands from entry points under provided namespace. """
        def _add_entry_point(epoint):
            """
            Convenience function taking an entry point, making some name
            checks and adding it to registered commands.
            """
            if not util.RE_COMMAND_NAME.match(epoint.name):
                LOG().error('Invalid command name: %s, ignoring.', epoint.name)
                return
            if epoint.name in self._commands:
                LOG().warn('Command "%s" already registered, ignoring.',
                        epoint.name)
            else:
                LOG().debug('Found registered command "%s".', epoint.name)
                self._commands[epoint.name] = epoint

        for entry_point in pkg_resources.iter_entry_points(self._namespace):
            if isinstance(entry_point, dict):
                for epoint in entry_point.values():
                    _add_entry_point(epoint)
            else:
                _add_entry_point(entry_point)


    def add_command(self, name, cmd_class):
        """
        Registers custom command. May be used for example for *help* command.

        :param name: (``str``) Name of command.
        :param cmd_class: (``LmiBaseCommand``) Factory for commands.
        """
        if not isinstance(name, basestring):
            raise TypeError("name must be a string")
        if not issubclass(cmd_class, base.LmiBaseCommand):
            raise TypeError("cmd_class must be a LmiBaseCommand")
        if not util.RE_COMMAND_NAME.match(name):
            raise errors.LmiCommandInvalidName(
                    cmd_class.__module__, cmd_class.__class__.__name__, name)
        if name in self._commands:
            LOG().warn('Command "%s" already managed, overwriting with "%s:%s".',
                    name, cmd_class.__module__, cmd_class.__name__)
        self._commands[name] = _CustomCommandWrapper(name, cmd_class)

    def find_command(self, cmd_name):
        """
        Loads a command associated with given name and returns it.

        :param cmd_name: (``str``) Name of command to load.
        :rtype: (``LmiBaseCommand``) Factory for commands.
        """
        try:
            return self._commands[cmd_name].load()
        except KeyError:
            raise errors.LmiCommandNotFound(cmd_name)
        except ImportError as err:
            LOG().debug('Failed to import command "%s".', cmd_name, exc_info=err)
            raise errors.LmiCommandImportError(
                    cmd_name, self._commands[cmd_name].module_name, err)

    def reload_commands(self, keep_custom=True):
        """
        Flushes all commands and reloads entry points.

        :param keep_custom: (``bool``) Custom commands -- not loaded from
            entry points -- are preserved.
        """
        if keep_custom:
            keep = dict((n, c) for n, c in self._commands.items()
                   if isinstance(c, _CustomCommandWrapper))
        else:
            keep = {}
        self._commands = {}
        self._load_commands()
        self._commands.update(keep)

