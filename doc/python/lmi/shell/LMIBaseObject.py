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

# Base class for classes, that are used for tab-completion.
# Used due to deprecated methods since python 2.2.


class LMIWrapperBaseObject(object):
    """
    Base class for all LMI wrapper classes, such as :py:class:`.LMINamespace`,
    :py:class:`.LMIClass`, :py:class:`.LMIInstanceName`,
    :py:class:`.LMIInstance`, :py:class:`.LMIMethod`.

    :param LMIConnection conn: connection object
    """
    def __init__(self, conn):
        super(LMIWrapperBaseObject, self).__init__()
        self._conn = conn

    @property
    def connection(self):
        """
        Property returning :class:`.LMIConnection` object.

        :returns: connection object
        :rtype: :py:class:`.LMIConnection`
        """
        return self._conn
