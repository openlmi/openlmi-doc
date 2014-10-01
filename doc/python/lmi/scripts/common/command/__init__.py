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
This subpackage defines base classes and utility functions for declaring
commands. These serve as wrappers for functions in libraries specific to
particular provider.

Tree of these commands build a command line interface for this library.
"""

from lmi.scripts.common.command.base import LmiBaseCommand
from lmi.scripts.common.command.checkresult import LmiCheckResult
from lmi.scripts.common.command.endpoint import LmiEndPointCommand
from lmi.scripts.common.command.lister import LmiInstanceLister
from lmi.scripts.common.command.lister import LmiLister
from lmi.scripts.common.command.multiplexer import LmiCommandMultiplexer
from lmi.scripts.common.command.session import LmiSessionCommand
from lmi.scripts.common.command.select import LmiSelectCommand
from lmi.scripts.common.command.show import LmiShowInstance

from lmi.scripts.common.command.helper import make_list_command
from lmi.scripts.common.command.helper import register_subcommands
from lmi.scripts.common.command.helper import select_command
