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
Meta-command utility module.
"""

import logging
import logging.config
import os
import pkg_resources
import platform
import re
import socket
import sys
import urlparse

from lmi.scripts.common import Configuration
from lmi.scripts.common import get_logger
from lmi.scripts.common import lmi_logging

PYTHON_EGG_NAME = "openlmi-tools"
#: Service name identifying tcp port used to connect to CIMOM.
DEFAULT_BROKER_SERVICE_NAME = 'wbem-https'

RE_NETLOC = re.compile(r'^((?P<username>[^:@]+)(:(?P<password>[^@]+))?@)?'
        r'(?P<hostname>[^:]+)(:(?P<port>\d+))?$')

VERBOSITY_2_LOG_LEVEL = {
    Configuration.OUTPUT_SILENT  : logging.ERROR,
    Configuration.OUTPUT_WARNING : logging.WARNING,
    Configuration.OUTPUT_INFO    : logging.INFO,
    Configuration.OUTPUT_DEBUG   : logging.DEBUG,
}

DEFAULT_LOGGING_CONFIG = {
    'version' : 1,
    'disable_existing_loggers': True,
    'formatters' : {
        'console' : {
            "()" : "lmi.scripts.common.lmi_logging.LevelDispatchingFormatter",
            "formatters" : {
                logging.INFO :
                    Configuration.default_options()['ConsoleInfoFormat']
            },
            'default': Configuration.default_options()['ConsoleFormat'],
            'datefmt' : '%Y-%m-%d %H:%M:%S'
        },
        'file' : {
            'format' : Configuration.default_options()['FileFormat'],
            'datefmt' : '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers' : {
        'console': {
            'class' : "logging.StreamHandler",
            'level' : logging.ERROR,
            'formatter': 'console',
        },
        'console_shell': {
            'class' : "logging.StreamHandler",
            'level' : logging.CRITICAL,
            'formatter': 'console',
        },
        'file' : {
            'class' : "logging.FileHandler",
            'level' : Configuration.default_options()['Level'].upper(),
            'formatter': 'file',
        }
    },
    'loggers' : {
        'lmi.shell' : {
            'handlers' : ['console_shell'],
            'level' : logging.DEBUG,
            'propagate' : False
        }
    },
    'root' : {
        'level' : logging.DEBUG,
        'handlers' : ['console']
    }
}

LOG = get_logger(__name__)

def setup_logging(app_config, stderr=sys.stderr):
    """
    Setup logging to console and optionally to the file.

    :param app_config: (``lmi.scripts.common.Configuration``)
        Configuration object.
    :param stderr: (``file``) Output stream, where console handler should
        dispatch logging messages.
    """
    cfg = DEFAULT_LOGGING_CONFIG.copy()

    # Set up logging to a file
    if app_config.log_file:
        cfg['handlers']['file']['filename'] = app_config.log_file
        cfg['formatters']['file']['format'] = app_config.get_safe(
                'Log', 'FileFormat', raw=True)
        try:
            cfg['handlers']['file']['level'] = \
                    getattr(logging, app_config.logging_level.upper())
        except KeyError:
            LOG().error('Unsupported logging level: "%s".',
                    app_config.logging_level)
        cfg['root']['handlers'].append('file')
        cfg['loggers']['lmi.shell']['handlers'].append('file')
    else:
        del cfg['formatters']['file']
        del cfg['handlers']['file']

    if app_config.get_safe('Log', "LogToConsole", bool):
        # Set up logging to console
        if stderr is not sys.stderr:
            cfg['handlers']['console']['stream'] = stderr
        cfg['handlers']['console']['level'] = \
                VERBOSITY_2_LOG_LEVEL[app_config.verbosity]

        # make the verbosity of lmi shell one level less
        lmi_shell_verbosity = app_config.verbosity
        if (   app_config.verbosity < app_config.OUTPUT_DEBUG
           and app_config.verbosity > app_config.OUTPUT_SILENT):
            lmi_shell_verbosity -= 1
        cfg['handlers']['console_shell']['level'] = \
                VERBOSITY_2_LOG_LEVEL[lmi_shell_verbosity]

        # use ConsoleInfoFormat for INFO and less severe levels
        cfg['formatters']['console']['formatters'] = {
            logging.INFO :
                    app_config.get_safe('Log', 'ConsoleInfoFormat', raw=True)
        }
        # use ConsoleFormat for any other level
        cfg['formatters']['console']['default'] = app_config.get_safe(
                'Log', 'ConsoleFormat', raw=True)
    else:
        cfg['root']['handlers'].remove('console')
        cfg['loggers']['lmi.shell']['handlers'].remove('console_shell')
        del cfg['handlers']['console']
        del cfg['handlers']['console_shell']

    use_colors = platform.system() != 'Windows' and stderr.isatty()
    lmi_logging.setup_logger(use_colors = use_colors)
    logging.config.dictConfig(cfg)

def get_version(egg_name=PYTHON_EGG_NAME):
    """
    Gets version string of any python egg. Defaults to the egg of current
    application.
    """
    return pkg_resources.get_distribution(egg_name).version

def get_hosts_credentials(hostnames):
    """
    Parse list of hostnames, get credentials out of them and return
    ``(hostnames, creds)``, where ``hostnames`` is a list of ``hostnames``
    with credentials removed and ``creds`` is a dictionary with a pair
    ``(username, password)`` for every hostname, that supplied it.

    :param hostnames: (``list``) List of hostnames with optional credentials.
        For example: ``http://root:password@hostname:5988``.
    """
    if not hasattr(hostnames, '__iter__'):
        raise TypeError("hostnames must be a list of hosts")
    new_hostnames = []
    credentials = {}
    for hostname in hostnames:
        parsed = urlparse.urlparse(hostname)
        if not parsed.netloc and parsed.path:
            # got something like [user[:pass]@]hostname[:port] (no scheme)
            match = RE_NETLOC.match(hostname)
            if match:
                hostname = match.group('hostname')
                if match.group('port'):
                    hostname += ':' + match.group('port')
                if match.group('username') or match.group('password'):
                    credentials[hostname] = (
                        match.group('username'), match.group('password'))
        elif parsed.username or parsed.password:
            hostname = parsed.scheme
            if parsed.scheme:
                hostname += "://"
            hostname += parsed.hostname
            if parsed.port:
                hostname += ":" + str(parsed.port)
            hostname += parsed.path
            credentials[hostname] = (parsed.username, parsed.password)
        new_hostnames.append(hostname)
    return (new_hostnames, credentials)

def parse_hosts_file(hosts_file):
    """
    Parse file with hostnames to connect to. Return list of parsed hostnames.

    :param hosts_file: (``file``) File object openned for read.
        It containes hostnames. Each hostname occupies single line.
    :rtype: (``tuple``) A pair of ``(hosts, creds)``, where ``hosts`` is a list
        of string with hostnames and ``creds`` is a dictionary mapping
        ``(username, password)`` to each hostname if supplied.
    """
    hostnames = []
    for line in hosts_file.readlines():
        hostnames.append(line.strip())
    return get_hosts_credentials(hostnames)

def get_default_hostname(port=None):
    """
    Choose default hostname to connect to. If logged as root, this will default
    to localhost, which results in unix socket being used for connection.
    Otherwise use full qualified domain name and hostname will be tried in this
    order. If they are not address-resolvable, '127.0.0.1' is returned.

    This function shall be used only if no uri is specified on command line.

    :param port: Port of desired service running on host (CIMOM broker).
        This defaults to :py:attr:`DEFAULT_BROKER_SERVICE_NAME`
    :type port: string or int
    """
    if port is None:
        port = DEFAULT_BROKER_SERVICE_NAME
    # Functions used to get hostname. first resolvable result will be used.
    name_getters = []
    if os.getuid() != 0:
        # Use non-'localhost' name only if we'are not logged in as root
        # for it prevents the use of unix socket.
        name_getters.extend([socket.getfqdn, socket.gethostname])
    name_getters.append(lambda: 'localhost')
    for name_func in name_getters:
        try:
            hostname = name_func()
            socket.getaddrinfo(hostname, port)
            break
        except socket.gaierror:
            pass
    else:
        hostname = '127.0.0.1'
    return hostname
