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

import collections

from lmi.shell.compat import *

_RValue = collections.namedtuple('RValue', ["rval", "rparams", "errorstr"])


class LMIReturnValue(_RValue):
    """
    Class representing a return value, which holds 3 main types of attributes:

    :param rval: return value
    :param dictionary rparams: returned parameters of e.g. method call
    :param string errorstr: error string
    """
    def __repr__(self):
        """
        :returns: pretty string
        """
        return "LMIReturnValue(rval=%r, rparams=%r, errorstr=%r)" % self

    def __new__(self, rval, rparams=None, errorstr=None):
        rparams = rparams if rparams else {}
        if not isinstance(rparams, wbem.NocaseDict):
            rparams = wbem.NocaseDict(rparams)
        errorstr = errorstr if errorstr else ""
        return _RValue.__new__(
            self, rval=rval, rparams=rparams, errorstr=errorstr)
