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
import argparse

from lmi.shell.LMIShellVersion import __version__


class LMIShellOptionsHelpWithVersionFormatter(argparse.HelpFormatter):
    """
    Helper class used for help message formatting.
    """
    def _format_usage(self, usage, actions, groups, prefix):
        """
        Returns a string with pre-formatted LMIShell usage. This method
        prepends LMIShell version to the usage message.
        """
        return argparse.HelpFormatter._format_usage(
            self, usage, actions, groups, "LMIShell v%s\n\n" % __version__)


class LMIShellOptionParser(argparse.ArgumentParser):
    """
    Helper class for CLI option parsing.
    """
    def error(self, msg):
        """
        Prints help message, error message and exits with erro code 2.
        """
        self.print_help()
        self.exit(2, "\n%s: error: %s\n" % (self.prog, msg))


class LMIShellOptions(object):
    """
    Class representing a LMIShell command line options. In the constructor, all
    command line options before a script name are passed to the LMIShell. First
    position argument belongs to the script and the rest of command line
    options is passed to the script run under the LMIShell.

    :param list argv: CLI arguments
    """
    _LOG_DEFAULT, \
        _LOG_VERBOSE, \
        _LOG_MORE_VERBOSE, \
        _LOG_QUIET = range(4)

    def __init__(self, argv):
        # Create a option parser
        parser = LMIShellOptionParser(
            usage="%(prog)s [options] script [script-options]",
            formatter_class=LMIShellOptionsHelpWithVersionFormatter)
        parser.add_argument(
            "-i", "--interact", dest="interact", action="store_true",
            default=False, help="inspect interactively after running a script")
        parser.add_argument(
            "-v", "--verbose", dest="verbose", action="store_true",
            default=False, help="print log messages to stderr")
        parser.add_argument(
            "-m", "--more-verbose", dest="more_verbose", action="store_true",
            default=False, help="print all log messages to stderr")
        parser.add_argument(
            "-q", "--quiet", dest="quiet", action="store_true", default=False,
            help="do not print any log messages to stderr")
        parser.add_argument(
            "-n", "--noverify", dest="verifycert", action="store_false",
            default=True, help="do not verify CIMOM SSL certificate")
        parser.add_argument(
            "--cwd-first-in-path", dest="cwd_first_in_path",
            action="store_true", default=False,
            help="prepend CWD in sys.path instead of appending it")

        # Split CLI arguments into LMIShell ones and script ones. LMIShell
        # arguments are those, which are before the first positional argument.
        # Other CLI arguments are passed to the interpreted script.
        try:
            dmap = map(lambda arg: not arg.startswith("-"), argv[1:])
            delimiter = dmap.index(True) + 1
        except ValueError, e:
            delimiter = len(argv)
        self._script_argv = argv[delimiter:]
        self._script_name = self._script_argv[0] if self._script_argv else ""

        # Parse CLI options
        shell_argv = argv[1:delimiter]
        options = parser.parse_args(shell_argv)

        # Store CLI options
        self._interact = options.interact
        self._verifycert = options.verifycert
        self._cwd_first_in_path = options.cwd_first_in_path
        self._log = LMIShellOptions._LOG_DEFAULT
        if options.verbose:
            self._log = LMIShellOptions._LOG_VERBOSE
        if options.more_verbose:
            self._log = LMIShellOptions._LOG_MORE_VERBOSE
        if options.quiet:
            self._log = LMIShellOptions._LOG_QUIET

        # Check for errors
        verbose_options = (
            options.verbose,
            options.more_verbose,
            options.quiet)
        if verbose_options.count(True) > 1:
            parser.error("Options -v, -m and -q are mutually exclusive")

    @property
    def interactive(self):
        """
        :returns: flag, which tells if the LMIShell should be initially run in
            the interactive mode
        :rtype: bool
        """
        return not self._script_argv

    @property
    def interact(self):
        """
        :returns: flag, which indicates, if the LMIShell should enter an
            interactive mode, after executing a provided script. The behavior
            is similar to python interpreter
        :rtype: bool
        """
        return self._interact

    @property
    def script_name(self):
        """
        :returns: script name, which is about to be run under the LMIShell
        :rtype: string
        """
        return self._script_name

    @property
    def script_argv(self):
        """
        :returns: list of command line arguments of the interpreted script
        """
        return self._script_argv

    @property
    def log(self):
        """
        :returns: log level
        :rtype: int

        Log level can be one of the following:

            * ``_LOG_DEFAULT``
            * ``_LOG_VERBOSE``
            * ``_LOG_MORE_VERBOSE``
            * ``_LOG_QUIET``
        """
        return self._log

    @property
    def verify_server_cert(self):
        """
        :returns: flag, which indicates, if LMIShell should verify server side
            certificate, if SSL used
        :rtype: bool
        """
        return self._verifycert

    @property
    def cwd_first_in_path(self):
        """
        :returns: True, if CWD should be prepended in sys.path; False if
            appended
        """
        return self._cwd_first_in_path
