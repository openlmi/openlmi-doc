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
Module with convenient function for defining user commands.
"""

from lmi.scripts.common.command import LmiLister
from lmi.scripts.common.command import LmiCommandMultiplexer
from lmi.scripts.common.command import LmiSelectCommand
from lmi.scripts.common.command import util

def make_list_command(func,
        name=None,
        columns=None,
        verify_func=None,
        transform_func=None):
    """
    Create a command subclassed from :py:class:`~.lister.LmiLister`. Please
    refer to this class for detailed usage.

    :param func: Contents of ``CALLABLE`` property.
    :type func: string or callable
    :param string name: Optional name of resulting class. If not given,
        it will be made from the name of associated function.
    :param tuple columns: Contents of ``COLUMNS`` property.
    :param callable verify_func: Callable overriding
        py:meth:`~.endpoint.LmiEndPointCommand.verify_options` method.
    :param callable transform_func: Callable overriding
        :py:meth:`~.endpoint.LmiEndPointCommand.transform_options` method.
    :returns:  Subclass of :py:class:`~.lister.LmiLister`.
    :rtype: type
    """
    if name is None:
        if isinstance(func, basestring):
            name = func.split('.')[-1]
        else:
            name = func.__name__
        if not name.startswith('_'):
            name = '_' + name.capitalize()
    props = { 'COLUMNS' : columns
            , 'CALLABLE' : func
            , '__module__' : util.get_module_name() }
    if verify_func:
        props['verify_options'] = verify_func
    if transform_func:
        props['transform_options'] = transform_func
    return LmiLister.__metaclass__(name, (LmiLister, ), props)

def register_subcommands(command_name, usage, command_map,
        fallback_command=None):
    """
    Create a multiplexer command (a node in a tree of commands).

    :param string command_name: Name of created command. The same as will
        be given on a command line.
    :param string usage: Usage string parseable by ``docopt``.
    :param dictionary command_map: Dictionary of subcommands. Associates
        command names to their factories. It's assigned to ``COMMANDS``
        property.
    :param fallback_command: Command factory used when no command is given
        on command line.
    :type fallback_command: :py:class:`~.endpoint.LmiEndPointCommand`
    :returns: Subclass of :py:class:`~.multiplexer.LmiCommandMultiplexer`.
    :rtype: type
    """
    props = { 'COMMANDS'         : command_map
            , 'OWN_USAGE'        : True
            , '__doc__'          : usage
            , '__module__'       : util.get_module_name()
            , 'FALLBACK_COMMAND' : fallback_command }
    return LmiCommandMultiplexer.__metaclass__(command_name,
            (LmiCommandMultiplexer, ), props)

def select_command(command_name, *args, **kwargs):
    """
    Create command selector that loads command whose requirements are met.

    Example of invocation: ::

        Hardware = select_command('Hardware',
            ("Openlmi-Hardware >= 0.4.2", "lmi.scripts.hardware.current.Cmd"),
            ("Openlmi-Hardware < 0.4.2" , "lmi.scripts.hardware.pre042.Cmd"),
            default=HwMissing
        )

    Above example checks remote broker for OpenLMI-Hardware provider. If it is
    installed and its version is equal or higher than 0.4.2, command from
    ``current`` module will be used. For older registered versions command
    contained in ``pre042`` module will be loaded. If hardware provider is not
    available, HwMissing command will be loaded instead.

    .. seealso::
        Check out the grammer describing language used in these conditions at
        :py:mod:`lmi.scripts.common.versioncheck.parser`.

    :param args: List of pairs ``(condition, command)`` that are inspected in
        given order until single condition is satisfied. Associated command is
        then loaded. Command is either a reference to command class or path to
        it given as string. In latter case last dot divides module's import
        path and command name.
    :param default: This command will be loaded when no condition from *args*
        is satisfied.
    """
    props = { 'SELECT'         : args
            , 'DEFAULT'        : kwargs.get('default', None)
            , '__module__'     : util.get_module_name()
            }
    return LmiSelectCommand.__metaclass__(command_name,
            (LmiSelectCommand, ), props)

