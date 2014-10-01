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
Defines command class used to nest multiple commands under one.
"""

from docopt import docopt

from lmi.scripts.common import get_logger
from lmi.scripts.common.command import base
from lmi.scripts.common.command import meta

LOG = get_logger(__name__)

class LmiCommandMultiplexer(base.LmiBaseCommand):
    """
    Base class for node commands. It consumes just part of command line
    arguments and passes the remainder to one of its subcommands.

    Example usage: ::

        class MyCommand(LmiCommandMultiplexer):
            '''
            My command description.

            Usage: %(cmd)s mycommand (subcmd1 | subcmd2)
            '''
            COMMANDS = {'subcmd1' : Subcmd1, 'subcmd2' : Subcmd2}

    Where ``Subcmd1`` and ``Subcmd2`` are some other ``LmiBaseCommand``
    subclasses. Documentation string must be parseable with ``docopt``.

    Recognized properties:

        ``COMMANDS`` : ``dictionary``
            property will be translated to
            :py:meth:`LmiCommandMultiplexer.child_commands` class method by
            :py:class:`~.meta.MultiplexerMetaClass`.

    Using metaclass: :py:class:`.meta.MultiplexerMetaClass`.
    """
    __metaclass__ = meta.MultiplexerMetaClass

    @classmethod
    def child_commands(cls):
        """
        Abstract class method, that needs to be implemented in subclass.
        This is done by associated meta-class, when defining a command with
        assigned ``COMMANDS`` property.

        :returns: Dictionary of subcommand names with assigned command
            factories.
        :rtype: dictionary
        """
        raise NotImplementedError("child_commands must be implemented in"
                " a subclass")

    @classmethod
    def fallback_command(cls):
        """
        This is overriden by :py:class:`~.meta.MultiplexerMetaClass` when
        the ``FALLBACK_COMMAND`` gets processed.

        :returns: Command factory invoked for missing command on command line.
        :rtype: :py:class:`~.endpoint.LmiEndPointCommand`
        """
        return None

    @classmethod
    def is_end_point(cls):
        return False

    def run_subcommand(self, cmd_name, args):
        """
        Pass control to a subcommand identified by given name.

        :param string cmd_name: Name of direct subcommand, whose
            :py:meth:`~.base.LmiBaseCommand.run` method shall be invoked.
        :param list args: List of arguments for particular subcommand.
        :returns: Application exit code.
        :rtype: integer
        """
        if not isinstance(cmd_name, basestring):
            raise TypeError("cmd_name must be a string, not %s" %
                    repr(cmd_name))
        if not isinstance(args, (list, tuple)):
            raise TypeError("args must be a list, not %s" % repr(args))
        try:
            cmd_cls = self.child_commands()[cmd_name]
            cmd = cmd_cls(self.app, cmd_name, self)
        except KeyError:
            self.app.stderr.write(self.get_usage())
            LOG().critical('Unexpected command "%s".', cmd_name)
            return 1
        return cmd.run(args)

    def run(self, args):
        """
        Handle optional parameters, retrieve desired subcommand name and
        pass the remainder of arguments to it.

        :param list args: List of arguments with at least subcommand name.
        """
        if not isinstance(args, (list, tuple)):
            raise TypeError("args must be a list")
        full_args = self.get_cmd_name_parts(for_docopt=True) + args
        docopt_kwargs = {
            # check the --help ourselves (the default docopt behaviour checks
            # also for --version)
            'help' : False,
            # let's ignore options following first command for generated
            # usage string and when a height of this branch is > 2
            'options_first' : not self.has_own_usage()
                    or any(   not cmd.is_end_point()
                          for cmd in self.child_commands().values()
                          if  not args or args[0] not in self.child_commands()
                              or self.child_commands()[args[0]] is cmd)
        }
        options = docopt(self.get_usage(), full_args, **docopt_kwargs)
        if options.pop('--help', False) or (args and args[0] == '--help'):
            self.app.stdout.write(self.get_usage(proper=True))
            return 0
        if (   self.fallback_command() is not None
           and (not args or args[0] not in self.child_commands())):
            cmd_cls = self.fallback_command()
            cmd = cmd_cls(self.app, self.cmd_name, self.parent)
            return cmd.run(args)
        return self.run_subcommand(args[0], args[1:])
