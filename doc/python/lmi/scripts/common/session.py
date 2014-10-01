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
Module for session object representing all connection to remote hosts.
"""

from collections import defaultdict

from lmi.scripts.common import errors
from lmi.scripts.common import get_logger
from lmi.scripts.common.util import FilteredDict
from lmi.shell.LMIConnection import connect

LOG = get_logger(__name__)

class Session(object):
    """
    Session object keeps connection objects to remote hosts. Their are
    associated with particular hostnames. It also caches credentials for them.
    Connections are made as they are needed. When credentials are missing
    for connection to be made, the user is asked to supply them from
    standard input.

    :param app: Instance of main application.
    :param list hosts: List of hostname strings.
    :param dictionary credentials: Mapping assigning a pair
        ``(user, password)`` to each hostname.
    :param boolean same_credentials: Use the same credentials for all
        hosts in session. The first credentials given will be used.
    """

    def __init__(self, app, hosts, credentials=None, same_credentials=False):
        self._app = app
        self._connections = dict((h, None) for h in hosts)
        # { hostname : (username, password, verified), ... }
        # where verified is a flag saying, whether these credentials
        # were successfuly used for logging in
        self._credentials = defaultdict(lambda: ('', '', False))
        self._same_credentials = same_credentials
        if credentials is not None:
            if not isinstance(credentials, dict):
                raise TypeError("credentials must be a dictionary")
            for hostname, creds in credentials.items():
                credentials[hostname] = (creds[0], creds[1], False)
            self._credentials.update(credentials)

    def __getitem__(self, hostname):
        """
        :rtype: (``LMIConnection``) Connection object to remote host.
            ``None`` if connection can not be made.
        """
        if self._connections[hostname] is None:
            try:
                self._connections[hostname] = self._connect(
                        hostname, interactive=True)
            except Exception as exc:
                LOG().error('Failed to make a connection to "%s": %s',
                        hostname, exc)
        return self._connections[hostname]

    def __len__(self):
        """ Get the number of hostnames in session. """
        return len(self._connections)

    def __contains__(self, uri):
        return uri in self._connections

    def __iter__(self):
        """ Yields connection objects. """
        successful_connections = 0
        for hostname in self._connections:
            connection = self[hostname]
            if connection is not None:
                yield connection
                successful_connections += 1
        if successful_connections == 0:
            raise errors.LmiNoConnections('No successful connection made.')

    def _connect(self, hostname, interactive=False):
        """
        Makes the connection to host.

        :param string hostname: Name of host.
        :param boolean interactive: Whether we can interact with user
            and expect a reply from him.
        :returns: Connection to remote host or ``None``.
        :rtype: :py:class:`lmi.shell.LMIConnection` or ``None``
        """
        username, password = self.get_credentials(hostname)
        kwargs = {
                'verify_server_cert' : self._app.config.verify_server_cert,
                'interactive'        : interactive
        }
        if len(self._connections) > 1:
            kwargs['prompt_prefix'] = '[%s] ' % hostname
        connection = connect(hostname, username, password, **kwargs)
        if connection is not None:
            tp = connection.client._cliconn.creds
            if tp is None:
                tp = ('', '')
            self._credentials[hostname] = (tp[0], tp[1], True)
        else:
            LOG().error('Failed to connect to host "%s".', hostname)
        return connection

    @property
    def hostnames(self):
        """
        List of hostnames in session.

        :rtype: list
        """
        return self._connections.keys()

    def get_credentials(self, hostname):
        """
        :param string hostname: Name of host to get credentials for.
        :returns: Pair of ``(username, password)`` for given hostname. If no
            credentials were given for this host, ``('', '')`` is returned.
        :rtype: tuple
        """
        username, password, verified = self._credentials[hostname]
        if (   not verified
           and (not username or not password)
           and self._same_credentials):
            for tp in self._credentials.values():
                if tp[2]:
                    username, password = tp[0], tp[1]
                    break
        return username, password

    def get_unconnected(self):
        """
        :returns:  List of hostnames, which do not have associated connection
            yet.
        :rtype: list
        """
        return [h for h, c in self._connections.items() if c is None]

class SessionProxy(Session):
    """
    Behaves like a session. But it just encapsulates other session object and
    provides access to a subset of its items.

    :param session: Session object or even another session proxy.
    :param list uris: Subset of uris in encapsulated session object.
    """

    def __init__(self, session, uris):
        uris = set(uris)
        if not all(isinstance(uri, basestring) for uri in uris):
            raise ValueError("uris must be iterable of uris")
        for uri in uris:
            if not uri in session:
                raise ValueError('uri "%s" needs to belong to given session'
                        % uri)
        Session.__init__(self, session._app, uris, session._credentials,
                session._same_credentials)
        self._origin = session
        self._connections = FilteredDict(uris, session._connections)
        # let the credentials propagage to original session
        self._credentials = session._credentials

