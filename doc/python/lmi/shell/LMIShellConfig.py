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


class LMIShellConfig(object):
    """
    Class representing the shell's configuration. The class is responsible for
    loading the configuration from the file and provides a unified API to
    access these settings.

    Constructs a :py:class:`.LMIShellConfig` object and loads the configuration
    from the file. If there is no such file, the shell's configuration
    properties are set to default values. Configuration file uses python
    syntax. If there is a syntax error in the configuration file, the
    properties are set to default values, as well.
    """
    DEFAULT_CONFIG_FILE = "~/.lmishellrc"
    DEFAULT_HISTORY_FILE = "~/.lmishell_history"
    DEFAULT_HISTORY_LENGTH = -1
    DEFAULT_USE_CACHE = True
    DEFAULT_USE_EXCEPTIONS = False
    DEFAULT_LISTENER_CERT_FILE = ""
    DEFAULT_LISTENER_KEY_FILE = ""

    def __init__(self):
        try:
            conf = {}
            execfile(os.path.expanduser(
                LMIShellConfig.DEFAULT_CONFIG_FILE), conf)
            self._history_file = os.path.expanduser(
                conf.get("history_file",
                         LMIShellConfig.DEFAULT_HISTORY_FILE))
            self._history_length = conf.get(
                "history_length", LMIShellConfig.DEFAULT_HISTORY_LENGTH)
            self._use_cache = conf.get(
                "use_cache", LMIShellConfig.DEFAULT_USE_CACHE)
            self._use_exceptions = conf.get(
                "use_exceptions", LMIShellConfig.DEFAULT_USE_EXCEPTIONS)
            self._indication_cert_file = conf.get(
                "indication_cert_file",
                LMIShellConfig.DEFAULT_LISTENER_CERT_FILE)
            self._indication_key_file = conf.get(
                "indication_key_file",
                LMIShellConfig.DEFAULT_LISTENER_KEY_FILE)
        except (SyntaxError, IOError), e:
            if isinstance(e, SyntaxError):
                sys.stderr.write("Error: %s\n" % e)
            self._history_file = os.path.expanduser(
                LMIShellConfig.DEFAULT_HISTORY_FILE)
            self._history_length = LMIShellConfig.DEFAULT_HISTORY_LENGTH
            self._use_cache = LMIShellConfig.DEFAULT_USE_CACHE
            self._use_exceptions = LMIShellConfig.DEFAULT_USE_EXCEPTIONS
            self._indication_cert_file = \
                LMIShellConfig.DEFAULT_LISTENER_CERT_FILE
            self._indication_key_file = \
                LMIShellConfig.DEFAULT_LISTENER_KEY_FILE

    @property
    def history_file(self):
        """
        Property returning a string containing the shell's history file.

        :returns: history file
        :rtype: string
        """
        return self._history_file

    @property
    def history_length(self):
        """
        Property returning a number with the shell's history file length.

        :returns: history file length
        :rtype: int
        """
        return self._history_length

    @property
    def use_cache(self):
        """
        Property returning a bool flag, if the shell should use cache for class
        retrieval.

        :returns: flag, if the shell should use a cache
        :rtype: bool
        """
        return self._use_cache

    @property
    def use_exceptions(self):
        """
        Property returning a bool flag, if the shell should throw the
        exceptions away, or if they should be propagated further.

        :returns: flag, if the shell should use exceptions, or throw them away
        :rtype: bool
        """
        return self._use_exceptions

    @property
    def cert_file(self):
        """
        Property returning a file name containing x509 certificate. This
        is used for :py:class:`.LMIIndicationListener`.

        :returns: x509 certificate file name
        :rtype: string
        """
        return self._indication_cert_file

    @property
    def key_file(self):
        """
        Property returning a file name containing x509 certificate private key.
        This is used for :py:class:`.LMIIndicationListener`.

        :returns: x509 certificate private key
        :rtype: string
        """
        return self._indication_key_file
