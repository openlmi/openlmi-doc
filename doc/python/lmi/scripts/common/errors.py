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
Module with predefined exceptions for use in scripts.
"""

try:
    import lmiwbem as wbem
except ImportError:
    import pywbem as wbem

CIMError = wbem.CIMError

class LmiError(Exception):
    """
    The base Lmi scripts error.
    All the other exceptions inherit from it.
    """
    pass

class LmiFailed(LmiError):
    """
    Raised, when operation on remote host failes.
    It's supposed to be used especially in command libraries.
    """
    pass

class LmiUnsatisfiedDependencies(LmiFailed):
    """
    Raised when no guarded command in
    :py:class:`~.command.select.LmiSelectCommand` can be loaded due to
    unsatisfied requirements.
    """
    def __init__(self, uris):
        LmiFailed.__init__(self, "Profile and class dependencies were not"
                " satisfied for this session (%s)." % ', '.join(uris))

class LmiUnexpectedResult(LmiError):
    """
    Raised, when command's associated function returns something unexpected.
    """
    def __init__(self, command_class, expected, result):
        LmiError.__init__(self,
                'Got unexpected result from associated function of'
                ' "%s.%s", expected "%s", got: "%s".' %
                (command_class.__module__, command_class.__name__,
                    expected, repr(result)))

class LmiInvalidOptions(LmiError):
    """
    Raised in :py:meth:`~.command.endpoint.LmiEndPointCommand.verify_options`
    method if the options given are not valid.
    """
    pass

class LmiCommandNotFound(LmiError):
    """ Raised, when user requests not registered command. """
    def __init__(self, cmd_name):
        LmiError.__init__(self, 'No such command "%s".' % cmd_name)

class LmiNoConnections(LmiError):
    """ Raised, when no connection to remote hosts could be made. """
    pass

class LmiCommandImportError(LmiError):
    """ Exception raised when command can not be imported. """
    def __init__(self, cmd_name, cmd_path, reason):
        LmiError.__init__(self, 'Failed to import command "%s" (%s): %s' % (
                cmd_name, cmd_path, reason))

class LmiCommandError(LmiError):
    """ Generic exception related to command declaration. """
    def __init__(self, module_name, class_name, msg):
        LmiError.__init__(self, 'Wrong declaration of command "%s": %s'
                % (    ".".join([module_name, class_name])
                    if module_name else class_name
                  , msg))

class LmiCommandInvalidName(LmiCommandError):
    """ Raised, when command gets invalid name. """
    def __init__(self, module_name, class_name, cmd_name):
        LmiCommandError.__init__(self, module_name, class_name,
                'Invalid command name "%s".' % cmd_name)

class LmiCommandMissingCallable(LmiCommandError):
    """ Raised, when command declaration is missing callable object. """
    def __init__(self, module_name, class_name):
        LmiCommandError.__init__(self, module_name, class_name,
                'Missing CALLABLE property.')

class LmiCommandInvalidProperty(LmiCommandError):
    """ Raised, when any command property contains unexpected value. """
    pass

class LmiImportCallableFailed(LmiCommandInvalidProperty):
    """ Raised, when callable object of command could not be imported. """
    def __init__(self, module_name, class_name, callable_prop):
        LmiCommandInvalidProperty.__init__(self, module_name, class_name,
            'Failed to import callable "%s".' % callable_prop)

class LmiCommandInvalidCallable(LmiCommandInvalidProperty):
    """ Raised, when given callback is not callable. """
    def __init__(self, module_name, class_name, msg):
        LmiCommandInvalidProperty.__init__(self, module_name, class_name, msg)

class LmiBadSelectExpression(LmiCommandError):
    """
    Raised, when expression of :py:class:`~.command.select.LmiSelectCommand`
    could not be evaluated.
    """
    def __init__(self, module_name, class_name, expr):
        LmiCommandError.__init__(self, module_name, class_name,
                "Bad select expression: %s" % expr)

class LmiTerminate(Exception):
    """
    Raised to cleanly terminate interavtive shell.
    """
    def __init__(self, exit_code=0):
        Exception.__init__(self, exit_code)
