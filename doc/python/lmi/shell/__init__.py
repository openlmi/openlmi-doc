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

"""
LMIShell
"""
import sys

# Setup logging format
from lmi.shell.LMIShellLogger import lmi_init_logger
lmi_init_logger()

from lmi.shell.LMIShellVersion import __version__

from lmi.shell.compat import *
from lmi.shell.LMIExceptions import *
from lmi.shell.LMIUtil import LMIPassByRef
from lmi.shell.LMIIndicationListener import LMIIndicationListener
from lmi.shell.LMIReturnValue import LMIReturnValue
from lmi.shell.LMICIMXMLClient import LMICIMXMLClient
from lmi.shell.LMIWSMANClient import LMIWSMANClient
from lmi.shell.LMIShellClient import LMIShellClient
from lmi.shell.LMIShellConfig import LMIShellConfig
from lmi.shell.LMIShellOptions import LMIShellOptions
from lmi.shell.LMISubscription import LMISubscription
from lmi.shell.LMINamespace import LMINamespace
from lmi.shell.LMINamespace import LMINamespaceRoot
from lmi.shell.LMIConstantValues import LMIConstantValues
from lmi.shell.LMIClass import LMIClass
from lmi.shell.LMIInstanceName import LMIInstanceName
from lmi.shell.LMIMethod import LMIMethod
from lmi.shell.LMIInstance import LMIInstance
from lmi.shell.LMIConnection import LMIConnection

from lmi.shell.LMIConnection import connect

# Register LMI wrapper classes into a LMIObjectFactory  to avoid circular
# dependency between those classes.
from lmi.shell.LMIObjectFactory import LMIObjectFactory
LMIObjectFactory().register(LMINamespace)
LMIObjectFactory().register(LMINamespaceRoot)
LMIObjectFactory().register(LMIClass)
LMIObjectFactory().register(LMIInstance)
LMIObjectFactory().register(LMIInstanceName)
LMIObjectFactory().register(LMIMethod)

# LMIConsole depends on LMIObjectFactory and needs to be imported after
# LMIObjectFactory has all wrapper classes registered.
from lmi.shell.LMIConsole import LMIConsole
