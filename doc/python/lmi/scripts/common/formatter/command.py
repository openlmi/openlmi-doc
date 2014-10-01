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
Contains command classes used to control formatters from inside of command
execution functions.
"""

class FormatterCommand(object):
    """
    Base class for formatter commands.
    """
    pass

class NewHostCommand(FormatterCommand):
    """
    Command for formatter to finish current table (if any), print header for
    new host and (if there are any data) print table header.

    :param string hostname: Name of host appearing at the front of new table.
    """
    def __init__(self, hostname):
        self.hostname = hostname

class NewTableCommand(FormatterCommand):
    """
    Command for formatter to finish current table (if any), print the **title**
    and (if there are any data) print table header.

    :param string title: Optional title for new table.
    """
    def __init__(self, title=None):
        self.title = title

class NewTableHeaderCommand(FormatterCommand):
    """
    Command for formatter to finish current table (if any), store new table
    header and (if there are any data) print the table header.
    The table header will be printed in all subsequent tables, until
    new instance of this class arrives.

    :param tuple columns: Array of column names.
    """
    def __init__(self, columns=None):
        self.columns = columns
