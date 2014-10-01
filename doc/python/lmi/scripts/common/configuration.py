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
Module for Configuration class.
"""

import os
from lmi.base.BaseConfiguration import BaseConfiguration

LISTER_FORMATS = ['csv', 'table']

#: Default format string to use in stderr handlers.
DEFAULT_FORMAT_STRING = "%(cseq)s%(levelname_)-8s:%(creset)s %(message)s"

class Configuration(BaseConfiguration):
    """
    Configuration class specific to software providers.
    *OpenLMI* configuration file should reside in: ::

        /etc/openlmi/scripts/lmi.conf

    :param string user_config_file_path: Path to the user configuration
        options.
    """

    USER_CONFIG_FILE_PATH = "~/.lmirc"
    HISTORY_FILE = "~/.lmi_history"

    OUTPUT_SILENT  = -1
    OUTPUT_WARNING = 0
    OUTPUT_INFO    = 1
    OUTPUT_DEBUG   = 2

    # indexes to LISTER_FORMATS
    LISTER_FORMAT_CSV = 0
    LISTER_FORMAT_TABLE = 1

    def __init__(self, user_config_file_path=USER_CONFIG_FILE_PATH, **kwargs):
        self._user_config_file_path = os.path.expanduser(user_config_file_path)
        BaseConfiguration.__init__(self, **kwargs)
        self._verbosity = None
        self._trace = None
        self._verify_server_cert = None
        self._cim_namespace = None
        self._human_friendly = None
        self._lister_format = None
        self._no_headings = None
        self._log_file = None
        self._history_max_length = None

    @classmethod
    def provider_prefix(cls):
        return "scripts"

    @classmethod
    def default_options(cls):
        """
        :returns: Dictionary of default values.
        :rtype: dictionary
        """
        defaults = BaseConfiguration.default_options().copy()
        # [Main] options
        defaults["CommandNamespace"] = 'lmi.scripts.cmd'
        defaults["Trace"] = "False"
        defaults["Verbosity"] = "0"
        defaults["HistoryMaxLength"] = "4000"
        # [Log] options
        defaults['ConsoleFormat'] = DEFAULT_FORMAT_STRING
        defaults['ConsoleInfoFormat'] = '%(message)s'
        defaults['FileFormat'] = \
                "%(asctime)s:%(levelname)-8s:%(name)s:%(lineno)d - %(message)s"
        defaults['LogToConsole'] = 'True'
        defaults['OutputFile'] = ''
        # [SSL] options
        defaults['VerifyServerCertificate'] = 'True'
        # [Format] options
        defaults['HumanFriendly'] = 'False' # be ugly by default
        defaults['ListerFormat'] = 'table'
        defaults['NoHeadings'] = 'False'
        return defaults

    @classmethod
    def mandatory_sections(cls):
        sects = set(BaseConfiguration.mandatory_sections())
        sects.add('Main')
        sects.add('SSL')
        sects.add('Format')
        return list(sects)

    def load(self):
        """ Read additional user configuration file if it exists. """
        BaseConfiguration.load(self)
        self.config.read(self._user_config_file_path)

    # *************************************************************************
    # [CIM] options
    # *************************************************************************
    @property
    def namespace(self):
        if self._cim_namespace is None:
            return BaseConfiguration.namespace.fget(self)
        return self._cim_namespace
    @namespace.setter
    def namespace(self, namespace):
        if not isinstance(namespace, basestring) and namespace is not None:
            raise TypeError("namespace must be a string")
        self._cim_namespace = namespace

    # *************************************************************************
    # [Main] options
    # *************************************************************************
    @property
    def history_file(self):
        """ Path to a file with history of interactive mode. """
        return os.path.expanduser(self.HISTORY_FILE)

    @property
    def history_max_length(self):
        """ Maximum number of lines kept in history file. """
        return self.get_safe('Main', 'HistoryMaxLength', int)

    @property
    def silent(self):
        """ Whether to suppress all output messages except for errors. """
        return self.verbosity <= self.OUTPUT_SILENT

    @property
    def trace(self):
        """ Whether the tracebacks shall be printed upon errors. """
        if self._trace is not None:
            return self._trace
        return self.get_safe('Main', 'Trace', bool)

    @trace.setter
    def trace(self, trace):
        """ Allow to override configuration option Trace. """
        if trace is not None:
            trace = bool(trace)
        self._trace = trace

    @property
    def verbose(self):
        """ Whether to output more details. """
        return self.verbosity >= self.OUTPUT_INFO

    @property
    def verbosity(self):
        """ Return integer indicating verbosity level of output to console. """
        if self._verbosity is None:
            return self.get_safe('Main', 'Verbosity', int)
        return self._verbosity

    @verbosity.setter
    def verbosity(self, level):
        """ Allow to set verbosity without modifying configuration values. """
        if not isinstance(level, (long, int)) and level is not None:
            raise TypeError("level must be integer")
        if level is not None:
            if level < self.OUTPUT_SILENT:
                level = self.OUTPUT_SILENT
            elif level > self.OUTPUT_DEBUG:
                level = self.OUTPUT_DEBUG
        self._verbosity = level

    # *************************************************************************
    # [Log] options
    # *************************************************************************
    @property
    def log_file(self):
        """ Path to a file, where logging messages shall be written. """
        if self._log_file is None:
            return self.get_safe('Log', 'OutputFile')
        return self._log_file
    @log_file.setter
    def log_file(self, log_file):
        """ Override logging file path. """
        if log_file is not None and not isinstance(log_file, basestring):
            raise TypeError("log_file must be a string")
        self._log_file = log_file

    # *************************************************************************
    # [SSL] options
    # *************************************************************************
    @property
    def verify_server_cert(self):
        """
        Return boolean saying, whether the server-side certificate should be
        checked.
        """
        if self._verify_server_cert is None:
            return self.get_safe('SSL', 'VerifyServerCertificate', bool)
        return self._verify_server_cert
    @verify_server_cert.setter
    def verify_server_cert(self, value):
        """ Allows to override configuration option value. """
        if value is not None:
            value = bool(value)
        self._verify_server_cert = value

    # *************************************************************************
    # [Format] options
    # *************************************************************************
    @property
    def human_friendly(self):
        """ Whether to print human-friendly values. """
        if self._human_friendly is None:
            return self.get_safe('Format', 'HumanFriendly', bool)
        return self._human_friendly
    @human_friendly.setter
    def human_friendly(self, value):
        """ Allows to override configuration option value. """
        if value is not None:
            value = bool(value)
        self._human_friendly = value

    @property
    def lister_format(self):
        """
        Output format used for lister commands. Returns one of
            * LISTER_FORMAT_CSV
            * LISTER_FORMAT_TABLE

        :rtype: integer
        """
        if self._lister_format is None:
            value = self.get_safe('Format', 'ListerFormat')
            try:
                return LISTER_FORMATS.index(value.lower())
            except ValueError:
                value = self.default_options()['ListerFormat']
                return LISTER_FORMATS.index(value.lower())
        return self._lister_format
    @lister_format.setter
    def lister_format(self, value):
        """
        Allows to override configuration option.

        :param value: One of items from ``LISTER_FORMATS`` array or an index
            to it.
        :type value: integer or string
        """
        if (   value is not None
           and (  not isinstance(value, int)
               or (value < 0 or value >= len(LISTER_FORMATS)))
           and (  not isinstance(value, basestring)
               or value.lower() not in LISTER_FORMATS)) :
            raise TypeError("value must be an integer or one of: %s" %
                    LISTER_FORMATS)
        if isinstance(value, basestring):
            value = LISTER_FORMATS.index(value.lower())
        self._lister_format = value

    @property
    def no_headings(self):
        """ Whether to print headings of tables. """
        if self._no_headings is None:
            return self.get_safe('Format', 'NoHeadings', bool)
        return self._no_headings
    @no_headings.setter
    def no_headings(self, value):
        """ Allows to override configuration option. """
        if value is not None:
            value = bool(value)
        self._no_headings = value

# There were some path changes in BaseConfiguration after 0.2.0 release.
# Let's fallback to older variable name when the new one is not present.
if hasattr(BaseConfiguration, 'CONFIG_DIRECTORY_TEMPLATE_PROVIDER'):
    setattr( Configuration
           , 'CONFIG_FILE_PATH_TEMPLATE_PROVIDER'
           , getattr(BaseConfiguration, 'CONFIG_DIRECTORY_TEMPLATE_PROVIDER')
                + 'lmi.conf')
else:   # fallback
    setattr( Configuration
           , 'CONFIG_FILE_PATH_TEMPLATE'
           , getattr(BaseConfiguration, 'CONFIG_DIRECTORY_TEMPLATE')
                + 'lmi.conf')
