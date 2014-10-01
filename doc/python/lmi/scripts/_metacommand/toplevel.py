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
Module defining the root command (``lmi`` binary).
"""

USAGE_STRING = \
"""
OpenLMI command line interface for CIM providers. It's functionality is
composed of registered subcommands, operating on top of simple libraries,
interfacing with particular OpenLMI profile providers.
Works also in interactive mode which is entered, when <command> argument is
omitted.

Usage:
    %(cmd)s [options] [(--trace | --notrace)] [-v]... [-h <host>]...
        <command> [<args> ...]
    %(cmd)s [options] [(--trace | --notrace)] [-v]... [-h <host>]...
    %(cmd)s (--help | --version)

Options:
    -c --config-file <config>  Path to a user configuration file. Options
                               specified here override any settings of global
                               configuration file.
    -h --host <host>           Hostname of target system.
    --hosts-file <hosts>       Path to a file containing target hostnames.
                               Each hostname must be listed on a single line.
    --user <user>              Username used in connection to any target host.
    --same-credentials         Use the first credentials given for all hosts.
    -n --noverify              Do not verify cimom's ssl certificate.
    -v                         Increase verbosity of output.
    --trace                    Show tracebacks on errors.
    --notrace                  Suppress tracebacks for exceptions.
    -q --quiet                 Supress output except for errors.
    --log-file <log_file>      Output file for logging messages.
    --namespace <namespace>    Default CIM namespace to use.
    -N --no-headings           Don't print table headings.
    -H --human-friendly        Print large values in human friendly units (i.e.
                               MB, GB, TB etc.)
    -L --lister-format (table | csv)
                               Print output of lister commands in CSV or table
                               format. CSV format is more suitable for machine
                               processing. Defaults to table.
    --help                     Show this text and quit.
    --version                  Print version of '%(cmd)s' in use and quit.

Handling hosts:
    If no --host or --hosts-file are given, the "localhost" will be tried. When
    running under root with Pegasus CIMOM, this results in a connection over
    unix socket (no need to supply credentials).

    Hosts may contain embedded credentials e.g.:
        http://user:passwd@hostname:5988
    Avoid supplying them on command line though. Always prefer the --hosts-file
    option.
"""

import docopt

from lmi.scripts._metacommand import exit
from lmi.scripts._metacommand import util
from lmi.scripts._metacommand import Interactive
from lmi.scripts.common import get_logger
from lmi.scripts.common import errors
from lmi.scripts.common.command import base

LOG = get_logger(__name__)

class TopLevelCommand(base.LmiBaseCommand):
    """
    Top level (instance, without any parent) command handling application
    parameters and passing work to registered subcommands.
    """

    @classmethod
    def has_own_usage(cls):
        return True

    @classmethod
    def child_commands(cls):
        return []

    @classmethod
    def is_end_point(cls):
        return False

    def __init__(self, app, cmd_name='lmi'):
        base.LmiBaseCommand.__init__(self, app, cmd_name)

    def get_usage(self, proper=False):
        return USAGE_STRING[1:] % { 'cmd' : " ".join(self.cmd_name_parts) }

    def run_subcommand(self, cmd_name, args):
        """
        Finds a command factory, instantiates it and passes the control.
        """
        cmd_factory = self.app.command_manager[cmd_name]
        cmd = cmd_factory(self.app, cmd_name, parent=self)
        return cmd.run(args)

    def start_interactive_mode(self):
        """ Run the command line loop of interactive application. """
        self.app.command_manager.add_command("exit", exit.Exit)
        iapp = Interactive(self)
        while True:
            try:
                ret = iapp.cmdloop()
                break
            except errors.LmiTerminate as err:
                ret = err.args[0]
                break
            except KeyboardInterrupt as err:
                LOG().debug('%s: %s', err.__class__.__name__, str(err))
                self.app.stdout.write('\n')
        iapp.save_history()
        return ret

    def run(self, args):
        """
        Handle program arguments, set up the application and call
        a subcommand or enter interactive mode. Return exit code.

        :param args: (``list``) Arguments without the binary name.
        """
        if not isinstance(args, (tuple, list)):
            raise TypeError("args must be a list")
        try:
            options = docopt.docopt(self.get_usage(), args,
                    version=util.get_version(), help=False, options_first=True)
        except docopt.DocoptLanguageError as exc:
            self.app.stderr.write("%s\n" % str(exc))
            return exit.EXIT_CODE_FAILURE
        if options.pop('--help', False):
            self.app.stdout.write(self.get_usage())
            self.app.stdout.write("\nCommands:\n")
            self.app.stdout.write("    %s\n" % " ".join(
                n for n in sorted(self.app.command_manager)))
            return exit.EXIT_CODE_SUCCESS
        if options.pop('--version', False):
            self.app.print_version()
            return exit.EXIT_CODE_SUCCESS
        self.app.setup(options)
        if options['<command>'] is None:
            return self.start_interactive_mode()

        try:
            LOG().debug('Running command "%s".', options['<command>'])
            return self.run_subcommand(options['<command>'], options['<args>'])
        except docopt.DocoptExit as err:
            if '--help' in args:
                cmd_args = options['<args>']
                cmd_args = cmd_args[:cmd_args.index('--help')]
                return self.run_subcommand(
                        'help', [options['<command>']] + cmd_args)
            raise


