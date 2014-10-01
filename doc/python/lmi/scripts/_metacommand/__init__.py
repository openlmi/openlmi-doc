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
Subpackage containing functionality of lmi meta-command.
"""

import argparse
import logging
import sys

from lmi.scripts import common
from lmi.scripts.common import errors
from lmi.scripts._metacommand import util
from lmi.scripts._metacommand import exit
from lmi.scripts._metacommand.help import Help
from lmi.scripts._metacommand.manager import CommandManager
from lmi.scripts._metacommand.interactive import Interactive
from lmi.scripts._metacommand.toplevel import TopLevelCommand
from lmi.scripts.common.command import LmiCommandMultiplexer, LmiBaseCommand
from lmi.scripts.common.configuration import Configuration
from lmi.scripts.common.session import Session
from lmi.shell import LMIUtil

LOG = common.get_logger(__name__)

# write errors to stderr until logging is configured
logging.getLogger('').addHandler(logging.StreamHandler())

class MetaCommand(object):
    """
    Main application class. It instantiates configuration object, logging and
    then it passes control to commands.

    Example usage:

        MetaCommand().run()
    """

    def __init__(self):
        # allow exceptions in lmi shell
        LMIUtil.lmi_set_use_exceptions(True)
        # instance of CommandManager, created when first needed
        self._command_manager = None
        self.stdout = sys.stdout
        self.stderr = sys.stderr
        self.stdin = sys.stdin
        # instance of Session, created when needed
        self._session = None
        # instance of Configuration, created in setup()
        self.config = None
        # dictionary of not yet processed options, it's created in setup()
        self._options = None
        self._active_command = None

    def _configure_logging(self):
        """
        Setup logging. It expects Configuration object to be already
        initialized.

        Logging can be tuned in various ways:

            * In configuration file with options:
                * [Main] Verbosity
                * [Log] OutputFile
                * [Log] FileFormat
                * [Log] ConsoleFormat
                * [Log] ConsoleInfoFormat
                * [Log] LogToConsole
            * With command line options:
                ``-v`` flags :
                    Each such flag increases logging level of what is logged
                    into console. This overrides `[Main] Verbosity` option.
                ``-q`` :
                    Causes supression of any output made to stdout except for
                    error messages. This overrides ``[Main] Verbosity``.
                    option and ``-v`` flags.
                ``--log-file`` :
                    Output file for logging messages. This overrides ``[Log]
                    OutputFile`` option.

        Implicitly only warnings and errors are logged to the standard error
        stream without any tracebacks.
        """
        util.setup_logging(self.config, self.stderr)

    @property
    def command_manager(self):
        """
        Return instance of ``CommandManager``. It's initialized when first
        needed.

        :rtype: (``CommandManager``)
        """
        if self._command_manager is None:
            self._command_manager = CommandManager()
            self._command_manager.add_command('help', Help)
        return self._command_manager

    @property
    def session(self):
        """
        Return instance of Session. Instantiated when first needed.

        :rtype: (``Session``)
        """
        if self._session is None:
            if (   not self._options['--host']
               and not self._options['--hosts-file']):
                self._options['--host'] = [util.get_default_hostname()]
                LOG().info('No hosts given, using "%s".',
                        self._options['--host'][0])
            hostnames = []
            # credentials loaded from file
            credentials = {}
            def add_hosts(hosts, creds):
                """ Update hostnames and credentials for new data. """
                hostnames.extend(hosts)
                credentials.update(creds)
            if self._options['--hosts-file']:
                hosts_path = self._options['--hosts-file']
                try:
                    with open(hosts_path, 'r') as hosts_file:
                        add_hosts(*util.parse_hosts_file(hosts_file))
                except (OSError, IOError) as err:
                    LOG().critical('Could not read hosts file "%s": %s',
                            hosts_path, err)
                    sys.exit(1)
            add_hosts(*util.get_hosts_credentials(self._options['--host']))
            if self._options['--user']:
                credentials.update(
                        # credentials in file has precedence over --user option
                        dict((h, credentials.get(h, (self._options['--user'], '')))
                    for h in hostnames if h not in credentials
                ))
            self._session = Session(self, hostnames, credentials,
                    same_credentials=self._options['--same-credentials'])
        return self._session

    @property
    def active_command(self):
        return self._active_command
    @active_command.setter
    def active_command(self, cmd):
        if not isinstance(cmd, LmiBaseCommand):
            raise TypeError("cmd must be an instance of LmiBaseCommand")
        self._active_command = cmd

    def print_version(self):
        """ Print version of this egg to stdout. """
        self.stdout.write("%s\n" % util.get_version())

    def setup(self, options):
        """
        Initialise global Configuration object and set up logging.

        :param options: (``dict``) Dictionary of options parsed from command
            line by docopt.
        """
        conf_kwargs = {}
        if options['--config-file']:
            conf_kwargs['user_config_file_path'] = options.pop('--config-file')
        self.config = Configuration.get_instance(**conf_kwargs)
        # two mutually exclusive options
        if options['--trace'] or options['--notrace']:
            self.config.trace = bool(options['--trace'])
        if options.pop('--quiet', False):
            self.config.verbosity = Configuration.OUTPUT_SILENT
        elif options['-v'] and options['-v'] > 0:
            self.config.verbosity = options['-v']
        if options.pop('--noverify', False):
            self.config.verify_server_cert = False
        self.config.log_file = options.pop('--log-file', None)
        self._configure_logging()
        del options['--trace']
        del options['--notrace']
        del options['-v']
        self.config.namespace = options.pop('--namespace', None)
        self.config.human_friendly = options.pop('--human-friendly', None)
        self.config.no_headings = options.pop('--no-headings', None)
        self.config.lister_format = options.pop('--lister-format', None)
        # unhandled options may be used later (for session creation),
        # so let's save them
        self._options = options

    def run(self, argv):
        """
        Equivalent to the main program for the application.

        :param argv: (``list``) Input arguments and options.
            Contains all arguments but the application name.
        """
        retval = exit.EXIT_CODE_FAILURE
        cmd = TopLevelCommand(self)
        try:
            retval = cmd.run(argv)
        except Exception as exc:
            if isinstance(exc, errors.LmiUnsatisfiedDependencies):
                retval = exit.EXIT_CODE_UNSATISFIED_DEPENDENCIES
            LOG().exception(str(exc))
        if isinstance(retval, bool) or not isinstance(retval, (int, long)):
            return (    exit.EXIT_CODE_SUCCESS if bool(retval) or retval is None
                   else exit.EXIT_CODE_FAILURE)

        return retval

def main(argv=sys.argv[1:]):
    """
    Main entry point function. It just passes arguments to instantiated
    ``MetaCommand``.
    """
    return MetaCommand().run(argv)

