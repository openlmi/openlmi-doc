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


class LMIDeletedObjectError(Exception):
    """
    Raised, when there is an attempt to access properties on deleted
    :py:class:`.LMIInstance` object.
    """


class LMIUnknownParameterError(Exception):
    """
    Raised, when there is a method call issued and unknown method parameter is
    provided.
    """


class LMIUnknownPropertyError(Exception):
    """
    Raised, when there is an attempt to create instance with unknown property
    provided.
    """


class LMIMethodCallError(Exception):
    """
    Raised, when an error occurs within method call.
    """


class LMISynchroMethodCallError(Exception):
    """
    Raised, when an error occurs within synchronized method call.
    """


class LMISynchroMethodCallFilterError(Exception):
    """
    Raised, when the LMIShell can not find necessary static filter for
    synchronous method call.
    """


class LMINoPagerError(Exception):
    """
    Raised, when there is no default pager like less or more.
    """


class LMIIndicationError(Exception):
    """
    Raised, if an error occurs while subscribing to/removing an indication.
    """


class LMIIndicationListenerError(Exception):
    """
    Raised, if there is an error while starting/stopping indication listener.
    """


class LMIHandlerNamePatternError(Exception):
    """
    Raised when the pattern string does not contain minimum replaceable
    characters.
    """


class LMIFilterError(Exception):
    """
    Raised, when a filter error occurs, mostly when filter object is missing.
    """


class LMIClassNotFound(AttributeError):
    """
    Raised, when trying to access missing class in LMINamespace.

    :param string namespace: namespace name
    :param string classname: class name, which was not found in **namespace**
    """
    def __init__(self, namespace, class_name):
        AttributeError.__init__(
            self, 'no such class "%s" in "%s" namespace' %
            (class_name, namespace))


class LMINamespaceNotFound(AttributeError):
    """
    Raised, when trying to access not existing namespace from connection or
    namespace object.

    :param string namespace: namespace which was not found
    :param args: other positional arguments
    """
    def __init__(self, namespace, *args):
        AttributeError.__init__(self, 'no such namespace "%s"' %
                                "/".join([namespace] + list(args)))


class LMINotSupported(Exception):
    """
    Raised, when non-WSMAN method is about to be called.
    """


class CIMError(Exception):
    """
    LMIShell's exception for CIM errors.
    """
    def __init__(self, *args):
        super(CIMError, self).__init__()
        if len(args) == 1 and isinstance(args[0], Exception):
            self.args = args[0].args
        else:
            self.args = args

class ConnectionError(Exception):
    """
    LMIShell's exception for Connection errors.
    """
    def __init__(self, *args):
        super(ConnectionError, self).__init__()
        if len(args) == 1 and isinstance(args[0], Exception):
            self.args = args[0].args
        else:
            self.args = args
