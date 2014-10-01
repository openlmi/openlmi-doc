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
Module defining base command class for all possible commands of ``lmi``
meta-command.
"""

import abc
import re

# regular expression matching leading whitespaces not until the first line
# containing non-white-spaces
RE_LSPACES = re.compile(r'\A(\s*$.)*', re.DOTALL | re.MULTILINE)

#: Default formatting options overriden by options passed onc ommand-line and
#: set in configuration file.
DEFAULT_FORMATTER_OPTIONS = {
    'no_headings'    : False,
    'padding'        : 0,
    'human_friendly' : False,
}

class LmiBaseCommand(object):
    """
    Abstract base class for all commands handling command line arguments.
    Instances of this class are organized in a tree with root element being the
    ``lmi`` meta-command (if not running in interactive mode). Each such
    instance can have more child commands if its
    :py:meth:`LmiBaseCommand.is_multiplexer` method return ``True``. Each has
    one parent command except for the top level one, whose :py:attr:`parent`
    property returns ``None``.

    Set of commands is organized in a tree, where each command (except for the
    root) has its own parent. :py:meth:`is_end_point` method distinguishes
    leaves from nodes. The path from root command to the leaf is a sequence of
    commands passed to command line.

    There is also a special command called selector. Its :py:meth:`is_selector`
    method returns ``True``. It selects proper command that shall be passed all
    the arguments based on expression with profile requirements. It shares its
    name and parent with selected child.

    If the :py:meth:`LmiBaseCommand.has_own_usage` returns ``True``, the parent
    command won't process the whole command line and the remainder will be
    passed as a second argument to the :py:meth:`LmiBaseCommand.run` method.

    :param app: Main application object.
    :param string cmd_name: Name of command.
    :param parent: Parent command.
    :type parent: :py:class:`LmiBaseCommand`
    """

    __metaclass__ = abc.ABCMeta

    @classmethod
    def get_description(cls):
        """
        Return description for this command. This is usually a first line
        of documentation string of a class.

        :rtype: string
        """
        if cls.__doc__ is None:
            return ""
        return cls.__doc__.strip().split("\n", 1)[0]

    @classmethod
    def is_end_point(cls):
        """
        :returns: ``True``, if this command parses the rest of command line and
            can not have any child subcommands.
        :rtype: boolean
        """
        return True

    @classmethod
    def is_multiplexer(cls):
        """
        Is this command a multiplexer? Note that only one of
        :py:meth:`is_end_point`, :py:meth:`is_selector` and this method can
        evaluate to``True``.

        :returns: ``True`` if this command is not an end-point command and it's
            a multiplexer. It contains one or more subcommands. It consumes the
            first argument from command-line arguments and passes the rest to
            one of its subcommands.
        :rtype: boolean
        """
        return not cls.is_end_point()

    @classmethod
    def is_selector(cls):
        """
        Is this command a selector?

        :returns: ``True`` if this command is a subclass of
            :py:class:`lmi.scripts.common.command.select.LmiSelectCommand`.
        :rtype: boolean
        """
        return not cls.is_end_point() and not cls.is_multiplexer()

    @classmethod
    def has_own_usage(cls):
        """
        :returns: ``True``, if this command has its own usage string, which is
            returned by :py:meth:`LmiBaseCommand.get_description`. Otherwise
            the parent command must be queried.
        :rtype: boolean
        """
        return False

    @classmethod
    def child_commands(cls):
        """
        Abstract class method returning dictionary of child commands with
        structure: ::

            { "command-name" : cmd_factory, ... }

        Dictionary contains just a direct children (commands, which
        may immediately follow this particular command on command line).
        """
        raise NotImplementedError("child_commands() method must be overriden"
                " in a subclass")

    def __init__(self, app, cmd_name, parent=None):
        if not isinstance(cmd_name, basestring):
            raise TypeError('cmd_name must be a string')
        if parent is not None and not isinstance(parent, LmiBaseCommand):
            raise TypeError('parent must be an LmiBaseCommand instance')
        self._app = app
        self._cmd_name = cmd_name.strip()
        self._parent = parent

    @property
    def app(self):
        """ Return application object. """
        return self._app

    @property
    def parent(self):
        """ Return parent command. """
        return self._parent

    @property
    def cmd_name(self):
        """ Name of this subcommand as a single word. """
        return self._cmd_name

    @property
    def cmd_name_parts(self):
        """
        Convenience property calling :py:meth:`get_cmd_name_parts` to obtain
        command path as a list of all preceding command names.

        :rtype: list
        """
        return self.get_cmd_name_parts()

    @property
    def format_options(self):
        """
        Compose formatting options. Parent commands are queried for defaults. If
        command has no parent, default options will be taken from
        :py:attr:`DEFAULT_FORMATTER_OPTIONS` which are overriden by config
        settings.

        :returns: Arguments passed to formatter factory when formatter is
            for current command is constructed.
        :rtype: dictionary
        """
        if self.parent is None:
            options = DEFAULT_FORMATTER_OPTIONS.copy()
            options['no_headings'] = self.app.config.no_headings
            options['human_friendly'] = self.app.config.human_friendly
        else:
            options = self.parent.format_options
        return options

    @property
    def session(self):
        """
        :returns: Session object. Session for command and all of its children
            may be overriden with a call to :py:meth:`set_session_proxy`.
        :rtype: :py:class:`lmi.scripts.common.session.Session`
        """
        proxy = getattr(self, '_session_proxy', None)
        if proxy:
            return proxy
        if self.parent is not None:
            return self.parent.session
        return self.app.session

    def get_cmd_name_parts(self, all_parts=False, demand_own_usage=True,
            for_docopt=False):
        """
        Get name of this command as a list composed of names of all preceding
        commands since the top level one. When in interactive mode, only
        commands following the active one will be present.

        :param boolean full: Take no heed to the active command or interactive
            mode. Return all command names since top level node inclusive. This
            is overriden with *for_docopt* flag.
        :param boolean demand_own_usage: Wether to continue the upward
            traversal through command hieararchy past the active command until
            the command with its own usage is found. This is the default behaviour.
        :param boolean for_docopt: Docopt parser needs to be given arguments list
            without the first item compared to command names in usage string
            it receives. Thus this option causes skipping the first item that would
            be otherwise included.
        :returns: Command path. Returned list will always contain at least the
            name of this command.
        :rtype: list
        """
        parts = [self.cmd_name]
        cmd = self
        own_usage = cmd.has_own_usage()
        while (   cmd.parent is not None
              and (all_parts or self.app.active_command not in (cmd, cmd.parent))
              or  (demand_own_usage and not own_usage)):
            cmd = cmd.parent
            parts.append(cmd.cmd_name)
            own_usage = own_usage or cmd.has_own_usage()
        if for_docopt and parts:
            parts.pop()
        return list(reversed(parts))

    def get_usage(self, proper=False):
        """
        Get command usage. Return value of this function is used by docopt
        parser as usage string. Command tree is traversed upwards until command
        with defined usage string is found. End point commands (leaves) require
        manually written usage, so the first command in the sequence of parents
        with own usage string is obtained and its usage returned. For nodes
        missing own usage string this can be generated based on its
        subcommands.

        :param boolean proper: Says, whether the usage string written
            manually is required or not. It applies only to node (not a leaf)
            commands without its own usage string.
        """
        if self.is_end_point() or self.has_own_usage() or proper:
            # get proper (manually written) usage, also referred as *own*
            cmd = self
            while not cmd.has_own_usage() and cmd.parent is not None:
                cmd = cmd.parent
            if cmd.__doc__ is None:
                docstr = "Usage: %s\n" % " ".join(self.cmd_name_parts)
            else:
                docstr = ( ( cmd.__doc__.rstrip()
                           % {'cmd' : " ".join(cmd.cmd_name_parts)}
                           ))

                match = RE_LSPACES.match(docstr)
                if match:   # strip leading newlines
                    docstr = docstr[match.end(0):]

                match = re.match(r'^ +', docstr)
                if match:   # unindent help message
                    re_lspaces = re.compile(r'^ {%s}' % match.end(0))
                    docstr = "\n".join(re_lspaces.sub('', l)
                                for l in docstr.splitlines())
                docstr += "\n"

        else:
            # generate usage string from what is known, applies to nodes
            # without own usage
            hlp = []
            if self.get_description():
                hlp.append(self.get_description())
                hlp.append("")
            hlp.append("Usage:")
            hlp.append("    %s <command> [<args> ...]"
                    % " ".join(self.cmd_name_parts))
            hlp.append("")
            hlp.append("Commands:")
            cmd_max_len = max(len(c) for c in self.child_commands())
            for name, cmd in sorted(self.child_commands().items()):
                hlp.append(("  %%-%ds %%s" % cmd_max_len)
                        % (name, cmd.get_description()))
            docstr = "\n".join(hlp) + "\n"

        return docstr

    @abc.abstractmethod
    def run(self, args):
        """
        Handle the command line arguments. If this is not an end point
        command, it will pass the unhandled arguments to one of it's child
        commands. So the arguments are processed recursively by the instances
        of this class.

        :param list args: Arguments passed to the command line that were
            not yet parsed. It's the contents of ``sys.argv`` (if in
            non-interactive mode) from the current command on.
        :returns: Exit code of application. This maybe also be a boolean value
            or ``None``. ``None`` and ``True`` are treated as a success causing
            exit code to be 0.
        :rtype: integer
        """
        raise NotImplementedError("run method must be overriden in subclass")

    def set_session_proxy(self, session):
        """
        Allows to override session object. This is useful for especially for
        conditional commands (subclasses of
        :py:class:`~lmi.scripts.common.command.select.LmiSelectCommand`) that devide
        connections to groups satisfying particular expression. These groups
        are turned into session proxies containing just a subset of connections
        in global session object.

        :param session: Session object.
        """
        self._session_proxy = session
