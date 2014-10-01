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
Meta classes simplifying declaration of user commands.

Each command is defined as a class with a set of properties. Some are
mandatory, the others have some default values. Each of them is transformed by
metaclasse to some function, class method or other property depending on
command type and semantic of property. Property itself is removed from
resulting class after being processed by meta class.
"""

import abc
import inspect
import re

from lmi.scripts.common import Configuration
from lmi.scripts.common import get_logger
from lmi.scripts.common import errors
from lmi.scripts.common.command import base
from lmi.scripts.common.command import util
from lmi.shell import LMIInstance
from lmi.shell.LMIReturnValue import LMIReturnValue

RE_CALLABLE = re.compile(
        r'^(?P<module>[a-z_]+(?:\.[a-z_]+)*):(?P<func>[a-z_]+)$',
        re.IGNORECASE)
RE_ARRAY_SUFFIX = re.compile(r'^(?:[a-z_]+[a-z0-9_]*)?$', re.IGNORECASE)
RE_OPTION = re.compile(r'^-+(?P<name>[^-+].*)$')
RE_MODULE_PATH = re.compile(r'([a-zA-z_]\w+\.)+[a-zA-z_]\w+')

FORMAT_OPTIONS = ('no_headings', 'human_friendly')

LOG = get_logger(__name__)

def _handle_usage(name, bases, dcl):
    """
    Take care of ``OWN_USAGE`` property. Supported values:

        `True`` :
            Means that documentation string of class is a usage string.
        ``False`` :
            No usage string for this command is defined.
        ``"usage string"`` :
            This property is a usage string.

    Defaults to ``False``.

    Usage string is an input parameter to ``docopt`` command-line options
    parser.

    :param string name: Name o command class.
    :param dictionary dcl: Class dictionary, which is modified by this
        function.
    """
    has_own_usage = False
    hlp = dcl.pop('OWN_USAGE', False)
    if hlp is True:
        if dcl['__doc__'] is None:
            raise errors.LmiCommandInvalidProperty(dcl['__module__'], name,
                    "OWN_USAGE set to True, but no __doc__ string present!")
        has_own_usage = True
    elif isinstance(hlp, basestring):
        if not '__doc__' in dcl:
            dcl['__doc__'] = hlp
        else:
            if not 'get_usage' in dcl:
                def _new_get_usage(_self, proper=False):
                    """ Get the usage string for ``doctopt`` parser. """
                    return hlp
                dcl['get_usage'] = _new_get_usage
        has_own_usage = True
    elif (   dcl.get('__node__', None) is None
         and any(getattr(b, 'has_own_usage', lambda: False)() for b in bases)):
        # inherit doc string of base class
        dcl['__doc__'] = (  b.__doc__ for b in bases
                         if getattr(b, 'has_own_usage', lambda: False)()).next()
        has_own_usage = True
    if has_own_usage:
        if not 'has_own_usage' in dcl:
            dcl['has_own_usage'] = classmethod(lambda _cls: True)

def _make_execute_method(bases, dcl, func):
    """
    Creates ``execute()`` method of a new end point command.

    :param tuple bases: Base classes of new command.
    :param dictionary dcl: Class dictionary being modified by this method.
    :param callable func: A callable wrapped by this new command. It's usually
        being referred to as *associated function*. If ``None``, no function
        will be created -- ``dcl`` won't be modified.
    """
    if func is not None and util.is_abstract_method(
            bases, 'execute', missing_is_abstract=True):
        del dcl['CALLABLE']
        def _execute(__self__, __connection__, *args, **kwargs):
            """ Invokes associated function with given arguments. """
            return func(__connection__, *args, **kwargs)
        _execute.dest = func
        dcl['execute'] = _execute

def _handle_namespace(dcl):
    """
    Overrides ``cim_namespace()`` class method if ``NAMESPACE`` property
    is given.

    :param dictionary dcl: Class dictionary being modified by this method.
    """
    if 'NAMESPACE' in dcl:
        namespace = dcl.pop('NAMESPACE')
        def _new_cim_namespace(_cls):
            """ Returns cim namespace used to modify connection object. """
            return namespace
        dcl['cim_namespace'] = classmethod(_new_cim_namespace)

def _handle_callable(name, bases, dcl):
    """
    Process the ``CALLABLE`` property of end-point command. Create the
    ``execute()`` method based on it.

    :param string name: Name of command class to create.
    :param tuple bases: Base classes of new command.
    :param dictionary dcl: Class dictionary being modified by this method.
    """
    try:
        func = dcl.get('CALLABLE')
        if isinstance(func, basestring):
            match = RE_CALLABLE.match(func)
            if not match:
                raise errors.LmiCommandInvalidCallable(
                        dcl['__module__'], name,
                        'Callable "%s" has invalid format (\':\' expected)'
                        % func)
            mod_name = match.group('module')
            try:
                func = getattr(__import__(mod_name, globals(), locals(),
                        [match.group('func')], 0),
                        match.group('func'))
            except (ImportError, AttributeError):
                raise errors.LmiImportCallableFailed(
                        dcl['__module__'], name, func)
    except KeyError:
        raise errors.LmiCommandMissingCallable(dcl['__module__'], name)
    if func is not None and not callable(func):
        raise errors.LmiCommandInvalidCallable(
            '"%s" is not a callable object or function.' % (
                func.__module__ + '.' + func.__name__))

    _make_execute_method(bases, dcl, func)

def _make_render_all_properties(bases):
    """
    Creates ``render()`` method, rendering all properties of instance.

    :param tuple bases: Base classes of new command class.
    :returns: Rendering method taking CIM instance as an
        argument.
    :rtype: function
    """
    if util.is_abstract_method(bases, 'render', missing_is_abstract=True):
        def _render(_self, inst):
            """
            Return tuple of ``(column_names, values)`` ready for output by
            formatter.
            """
            column_names, values = [], []
            for prop_name, value in sorted(inst.properties_dict().iteritems()):
                column_names.append(prop_name)
                if value is None:
                    value = ''
                values.append(value)
            return (column_names, values)

        return _render

def _make_render_with_properties(properties, target_formatter_lister=False):
    """
    Creates ``render()`` method, rendering given instance properties.

    :param properties: (``list``) List of properties to render.
    :param target_formatter_lister: (``bool``) Whether the output is targeted
        for Show command or Lister. The former expects a pair of column_names
        and values. The latter expects just values.
    :rtype: (``function``) Rendering method taking CIM instance as an
        argument.
    """
    def _process_property(prop, inst):
        """
        Takes a single property and instance. Returns computed value.

        :rtype: ``(str, any)`` A pair of property name and value.
        """
        if isinstance(prop, basestring):
            prop_name = prop
            if not prop in inst.properties():
                LOG().warn('Property "%s" not present in instance of "%s".',
                        prop, inst.path)
                value = "UNKNOWN"
            else:
                value = getattr(inst, prop)
        else:
            if not isinstance(prop, (tuple, list)):
                raise TypeError("prop must be a string or tuple, not %s" %
                        repr(prop))
            prop_name = prop[0]
            try:
                if callable(prop[1]):
                    value = prop[1](inst)
                else:
                    value = getattr(inst, prop[1])
            except Exception as exc:
                LOG().exception('Failed to render property "%s": %s',
                        prop[0], exc)
                value = "ERROR"
        if value is None:
            value = ''
        return prop_name, value

    if target_formatter_lister:
        def _render(self, inst):
            """
            Renders a limited set of properties and returns a row for instance
            table composed of property values.
            """
            if not isinstance(inst, LMIInstance):
                raise errors.LmiUnexpectedResult(
                        self.__class__, 'LMIInstance object', inst)
            return tuple(_process_property(p, inst)[1] for p in properties)

    else:
        def _render(self, inst):
            """
            Renders a limited set of properties and returns a pair of
            column names and values.
            """
            if not isinstance(inst, LMIInstance):
                raise errors.LmiUnexpectedResult(
                        self.__class__, 'LMIInstance object', inst)
            column_names, values = [], []
            for prop in properties:
                prop_name, value = _process_property(prop, inst)
                column_names.append(prop_name)
                values.append(value)
            return (column_names, values)

    return _render

def _check_render_properties(name, dcl, props):
    """
    Make sanity check for ``PROPERTIES`` class property. Exception will be
    raised when any flaw discovered.

    :param string name: Name of class to be created.
    :param dictionary dcl: Class dictionary.
    :param list props: List of properties or ``None``.
    """
    if props is not None:
        for prop in props:
            if not isinstance(prop, (basestring, tuple, list)):
                raise errors.LmiCommandInvalidProperty(
                        dcl['__module__'], name,
                        'PROPERTIES must be a list of strings or tuples')
            if isinstance(prop, (tuple, list)):
                if (  len(prop) != 2
                   or not isinstance(prop[0], basestring)
                   or (   not callable(prop[1])
                      and not isinstance(prop[1], basestring))):
                    raise errors.LmiCommandInvalidProperty(
                            dcl['__module__'], name,
                        'tuples in PROPERTIES must be: ("name",'
                        ' callable or property_name)')

def _handle_render_properties(name, bases, dcl, target_formatter_lister=False):
    """
    Process properties related to rendering function for commands operating
    on CIM instances. Result of this function a ``render()`` and
    ``get_columns()`` functions being added to class's dictionary with
    regard to handled properties.

    Currently handled properties are:

        ``DYNAMIC_PROPERTIES`` : ``bool``
            Whether the associated function itself provides list of
            properties. Optional property.
        ``PROPERTIES`` : ``bool``
            List of instance properties to print. Optional property.

    :param string name: Name of class to be created.
    :param tuple bases: Base classes of new command.
    :param dictionary dcl: Class dictionary being modified by this method.
    :param boolean target_formatter_lister: Whether the output is targeted
        for *Show* command or *Lister*. The former expects a pair of
        column_names and values. The latter expects just values.
    """
    dynamic_properties = dcl.pop('DYNAMIC_PROPERTIES', False)
    if dynamic_properties and 'PROPERTIES' in dcl:
        raise errors.LmiCommandError(
                dcl['__module__'], name,
                'DYNAMIC_PROPERTIES and PROPERTIES are mutually exclusive')

    properties = dcl.pop('PROPERTIES', None)
    _check_render_properties(name, dcl, properties)

    renderer = None
    get_columns = lambda cls: None
    if properties is None and not dynamic_properties:
        if (   target_formatter_lister
           and dcl.get('__metaclass__', None) is not InstanceListerMetaClass):
            raise errors.LmiCommandError(dcl['__module__'], name,
                    "either PROPERTIES must be declared or"
                    " DYNAMIC_PROPERTIES == True for InstanceLister"
                    " commands")
        renderer = _make_render_all_properties(bases)
    elif properties is None and dynamic_properties:
        def _render_dynamic(self, return_value):
            """ Renderer of dynamic properties. """
            properties, inst = return_value
            return _make_render_with_properties(properties,
                    target_formatter_lister)(self, inst)
        renderer = _render_dynamic
    elif properties is not None:
        renderer = _make_render_with_properties(properties,
                target_formatter_lister)
        get_columns = (lambda cls:
                    tuple((p[0] if isinstance(p, tuple) else p)
                for p in properties))
    if renderer is not None:
        dcl['render'] = classmethod(renderer)
    if target_formatter_lister:
        dcl['get_columns'] = get_columns

def _handle_opt_preprocess(name, dcl):
    """
    Process properties, that cause modification of parsed argument names before
    passing them to ``verify_options()`` or ``transform_options()``. If any of
    handled properties is supplied, it causes ``_preprocess_options()`` to be
    overriden, where all of desired name modifications will be made.
    Currently handled properties are:

        ``OPT_NO_UNDERSCORES`` : ``bool``
            When making a function's parameter name out of option, the leading
            dashes are replaced with underscore. If this property is True,
            dashes will be removed completely with no replacement.
        ``ARG_ARRAY_SUFFIX`` : ``bool``
            Add given suffix to all arguments resulting in list objects.

    :param string name: Command class name.
    :param dictionary dcl: Class dictionary being modified by this method.
    """
    if (   dcl.get('__metaclass__', None) is not EndPointCommandMetaClass
       and '_preprocess_options' in dcl):
        raise errors.LmiCommandError(dcl['__module__'], name,
                '_preprocess_options() method must not be overriden in the'
                'body of command class; use transform_options() instead')
    arr_suffix = dcl.pop('ARG_ARRAY_SUFFIX', '')
    if (  not isinstance(arr_suffix, str)
       or not RE_ARRAY_SUFFIX.match(arr_suffix)):
        raise errors.LmiCommandInvalidProperty(dcl['__module__'], name,
                'ARG_ARRAY_SUFFIX must be a string matching regular'
                ' expression "%s"' % RE_ARRAY_SUFFIX.pattern)
    opt_no_underscores = dcl.pop('OPT_NO_UNDERSCORES', False)
    if arr_suffix or opt_no_underscores:
        def _new_preprocess_options(_self, options):
            """ Modify (in-place) given options dictionary by renaming keys. """
            for do_it, cond, transform in (
                    ( arr_suffix
                    , lambda _, v: isinstance(v, list)
                    , lambda n   :
                              ('<' + util.RE_OPT_BRACKET_ARGUMENT.match(n)
                                    .group(1) + arr_suffix + '>')
                        if   util.RE_OPT_BRACKET_ARGUMENT.match(n)
                        else (n + arr_suffix))
                  , ( opt_no_underscores
                    , lambda n, _: RE_OPTION.match(n)
                    , lambda n   : RE_OPTION.match(n).group('name'))
                  ):
                if not do_it:
                    continue
                to_rename = (  name for name, value in options.items()
                            if cond(name, value))
                for name in to_rename:
                    new_name = transform(name)
                    LOG().debug('Renaming option "%s" to "%s".', name, new_name)
                    if new_name in options:
                        LOG().warn(
                            'Existing option named "%s" replaced with "%s".',
                                new_name, name)
                    options[new_name] = options.pop(name)

        dcl['_preprocess_options'] = _new_preprocess_options

def _handle_fallback_command(name, bases, dcl):
    """
    Process ``FALLBACK_COMMAND`` property of multiplexer command. It's turned
    into a :py:meth:`~.multiplexer.LmiCommandMultiplexer.fallback_command`
    class method. It needs to be called after the usage string is handled.

    .. seealso::
        :py:func:`_handle_usage`
    """
    fallback = dcl.pop('FALLBACK_COMMAND', None)
    if fallback is not None:
        if not issubclass(type(fallback), EndPointCommandMetaClass):
            raise errors.LmiCommandInvalidProperty(dcl['__module__'], name,
                    "FALLBACK_COMMAND must be a command class"
                    " (subclass of LmiEndPointCommand) not %s" % repr(fallback))
        if not fallback.has_own_usage():
            usage_string = dcl.get('__doc__', None)
            if not usage_string:
                for base_cls in bases:
                    if not issubclass(base_cls, base.LmiBaseCommand):
                        continue
                    cmd = base_cls
                    while not cmd.has_own_usage() and cmd.parent is not None:
                        cmd = cmd.parent
                    usage_string = cmd.__doc__
            if not usage_string:
                errors.LmiCommandError(dcl['__module__'], name,
                        "Missing usage string.")
            fallback.__doc__ = usage_string
            fallback.has_own_usage = lambda cls: True
        dcl['fallback_command'] = staticmethod(lambda: fallback)

def _handle_format_options(name, bases, dcl):
    """
    Process any ``FMT_*`` properties. This overrides ``format_options``
    property which returns dictionary of arguments passed to formatter factory.

    These properties are removed from class' dictionary.
    """
    format_options = {}
    for key, value in dcl.items():
        if key.startswith("FMT_"):
            opt_name = key[4:].lower()
            if opt_name not in FORMAT_OPTIONS:
                raise errors.LmiCommandInvalidProperty(
                        dcl['__module__'], name,
                        'Formatting option "%s" is not supported.' %
                        opt_name)
            if (   opt_name in ('no_headings', 'human_friendly')
               and not isinstance(value, bool)):
                raise errors.LmiCommandInvalidProperty(
                        dcl['__module__'], name,
                        '"%s" property must be a boolean')
            format_options[opt_name] = value

    if format_options:
        def _new_format_options(self):
            """ :returns: Dictionary of options for formatter object. """
            basecls = [b for b in bases if issubclass(b, base.LmiBaseCommand)][0]
            opts = basecls.format_options.fget(self)
            opts.update(format_options)
            return opts
        if 'format_options' in dcl:
            raise errors.LmiCommandError(dcl['__module__'], name,
                    'can not define both FMT_ options and "format_options" in'
                    ' the same class, choose just one of them')
        dcl['format_options'] = property(_new_format_options)

    for key in format_options:
        dcl.pop('FMT_' + key.upper())

def _handle_select(name, dcl):
    """
    Process properties of :py:class:`.select.LmiSelectCommand`.
    Currently handled properties are:

        ``SELECT`` : ``list``
            Is a list of pairs ``(condition, command)`` where ``condition`` is
            an expression in *LMIReSpL* language. And ``command`` is either a
            string with absolute path to command that shall be loaded or the
            command class itself.

            Small example: ::

                SELECT = [
                      ( 'OpenLMI-Hardware < 0.4.2'
                      , 'lmi.scripts.hardware.pre042.PreCmd'
                      )
                    , ('OpenLMI-Hardware >= 0.4.2 & class LMI_Chassis == 0.3.0'
                      , HwCmd
                      )
                ]

            It says: Let the ``PreHwCmd`` command do the job on brokers having
            ``openlmi-hardware`` package older than ``0.4.2``. Use the
            ``HwCmd`` anywhere else where also the ``LMI_Chassis`` CIM class in
            version ``0.3.0`` is available.

            First matching condition wins and assigned command will be passed
            all the arguments.

        ``DEFAULT`` : ``str`` or :py:class:`~.base.LmiBaseCommand`
            Defines fallback command used in case no condition can be
            satisfied.

    They will be turned into ``get_conditionals()`` method.
    """
    module_name = dcl.get('__module__', name)
    if not 'SELECT' in dcl:
        raise errors.LmiCommandError(module_name, name,
                "Missing SELECT property.")
    def inv_prop(msg, *args):
        return errors.LmiCommandInvalidProperty(module_name, name, msg % args)
    expressions = dcl.pop('SELECT')
    if not isinstance(expressions, (list, tuple)):
        raise inv_prop('SELECT must be list or tuple.')
    if len(expressions) < 1:
        raise inv_prop('SELECT must contain at least one condition!')
    for index, item in enumerate(expressions):
        if not isinstance(item, tuple):
            raise inv_prop('Items of SELECT must be tuples, not %s!' %
                    getattr(type(item), '__name__', 'UNKNOWN'))
        if len(item) != 2:
            raise inv_prop('Expected pair in SELECT on index %d!' % index)
        expr, cmd = item
        if not isinstance(expr, basestring):
            raise inv_prop('Expected expression string on index %d'
                    ' in SELECT!' % index)
        if isinstance(cmd, basestring) and not RE_MODULE_PATH.match(cmd):
            raise inv_prop('Second item of conditional pair on index %d'
                    ' in SELECT does not look as an importable path!' % cmd)
        if (   not isinstance(cmd, basestring)
           and not issubclass(cmd, (basestring, base.LmiBaseCommand))):
            raise inv_prop('Expected subclass of LmiBaseCommand (or its import'
                    ' path) as a second item of a pair on index %d in SELECT!'
                    % index)

    default = dcl.pop('DEFAULT', None)
    if isinstance(default, basestring) and not RE_MODULE_PATH.match(default):
        raise inv_prop('DEFAULT "%s" does not look as an importable path!'
            % default)
    if (   default is not None and not isinstance(default, basestring)
       and not issubclass(default, (basestring, base.LmiBaseCommand))):
        raise inv_prop('Expected subclass of LmiBaseCommand'
                ' (or its import path) as a value of DEFAULT!')
    def _new_get_conditionals(self):
        return expressions, default

    dcl['get_conditionals'] = _new_get_conditionals

class EndPointCommandMetaClass(abc.ABCMeta):
    """
    End point command does not have any subcommands. It's a leaf of
    command tree. It wraps some function in command library being
    referred to as an *associated function*. It handles following class
    properties:

        ``CALLABLE`` : ``str`` or callable
            An associated function. Mandatory property.
        ``OWN_USAGE`` : ``bool`` or ``str``
            Usage string. Optional property.
        ``ARG_ARRAY_SUFFIX`` : ``str``
            Suffix added to argument names containing array of values.
            Optional property.
        ``FMT_NO_HEADINGS`` : ``bool``
            Allows to force printing of table headers on and off for
            this command. Default is to print them.
        ``FMT_HUMAN_FRIENDLY`` : ``bool``
            Tells formatter to make the output more human friendly. The result
            is dependent on the type of formatter used.
    """

    def __new__(mcs, name, bases, dcl):
        _handle_usage(name, bases, dcl)
        _handle_callable(name, bases, dcl)
        _handle_opt_preprocess(name, dcl)
        _handle_format_options(name, bases, dcl)

        cls = super(EndPointCommandMetaClass, mcs).__new__(
                mcs, name, bases, dcl)

        # make additional check for arguments count
        dest = getattr(cls.execute, "dest", cls.execute)
        argspec = inspect.getargspec(dest)
        if (   not argspec.varargs
           and len(argspec.args) < cls.dest_pos_args_count()):
            raise errors.LmiCommandInvalidCallable(
                    dcl['__module__'], name,
                    'Callable must accept at least %d positional arguments' %
                    cls.dest_pos_args_count())

        return cls

class SessionCommandMetaClass(EndPointCommandMetaClass):
    """
    Meta class for commands operating upon a session object.
    All associated functions take as first argument an namespace abstraction
    of type ``lmi.shell``.

    Handles following class properties:

        ``NAMESPACE`` : ``str``
            CIM namespace abstraction that will be passed to associated
            function. Defaults to ``"root/cimv2"``. If ``False``, raw
            :py:class:`lmi.shell.LMIConnection` object will be passed to
            associated function.
    """
    def __new__(mcs, name, bases, dcl):
        _handle_usage(name, bases, dcl)
        _handle_namespace(dcl)
        _handle_callable(name, bases, dcl)

        return EndPointCommandMetaClass.__new__(mcs, name, bases, dcl)

class ListerMetaClass(SessionCommandMetaClass):
    """
    Meta class for end-point lister commands. Handles following class
    properties:

        ``COLUMNS`` : ``tuple``
            List of column names. Optional property. There are special values
            such as:

                ``None`` or omitted
                    Associated function provides column names in a first row of
                    returned list or generator.

                empty list, empty tuple or ``False``
                    They mean that no headers shall be printed. It is simalar
                    to using ``FMT_NO_HEADINGS = True``. But in this case all
                    the rows returned from associated functions are treated as
                    data.
    """

    def __new__(mcs, name, bases, dcl):
        cols = dcl.pop('COLUMNS', None)
        if cols is not None:
            if not isinstance(cols, (list, tuple)):
                raise errors.LmiCommandInvalidProperty(dcl['__module__'], name,
                        'COLUMNS class property must be either list or tuple')
            if len(cols) < 1 or cols is False:
                dcl['FMT_NO_HEADINGS'] = True
                cols = tuple()
            elif not all(isinstance(c, basestring) for c in cols):
                raise errors.LmiCommandInvalidProperty(dcl['__module__'], name,
                        'COLUMNS must contain just column names as strings')
            def _new_get_columns(_cls):
                """ Return column names. """
                return cols
            dcl['get_columns'] = classmethod(_new_get_columns)

        return super(ListerMetaClass, mcs).__new__(mcs, name, bases, dcl)

class ShowInstanceMetaClass(SessionCommandMetaClass):
    """
    Meta class for end-point show instance commands. Additional handled
    properties:

        ``DYNAMIC_PROPERTIES`` : ``bool``
            Whether the associated function itself provides list of
            properties. Optional property.
        ``PROPERTIES`` : ``tuple``
            List of instance properties to print. Optional property.

    These are translated in a :py:meth:`~.show.LmiShowInstance.render`, which
    should be marked as abstract in base lister class.
    """

    def __new__(mcs, name, bases, dcl):
        _handle_render_properties(name, bases, dcl)

        return super(ShowInstanceMetaClass, mcs).__new__(
                mcs, name, bases, dcl)

class InstanceListerMetaClass(SessionCommandMetaClass):
    """
    Meta class for instance lister command handling the same properties
    as :py:class:`ShowInstanceMetaClass`.
    """

    def __new__(mcs, name, bases, dcl):
        _handle_render_properties(name, bases, dcl, True)

        return super(InstanceListerMetaClass, mcs).__new__(
                mcs, name, bases, dcl)

class CheckResultMetaClass(SessionCommandMetaClass):
    """
    Meta class for end-point command "check result". Additional handled
    properties:

        ``EXPECT`` :
            Value to compare against the return value. Mandatory property.

    ``EXPECT`` property is transformed into a
    :py:meth:`.checkresult.LmiCheckResult.check_result` method taking two
    arguments ``(options, result)`` and returning a boolean.
    """

    def __new__(mcs, name, bases, dcl):
        try:
            expect = dcl['EXPECT']
            if callable(expect):
                def _new_expect(_self, options, result):
                    """
                    Comparison function testing return value with *expect*
                    function.
                    """
                    if isinstance(result, LMIReturnValue):
                        result = result.rval
                    passed = expect(options, result)
                    if not passed:
                        LOG().info('Got unexpected result "%s".')
                    return passed
            else:
                def _new_expect(_self, _options, result):
                    """ Comparison function testing by equivalence. """
                    if isinstance(result, LMIReturnValue):
                        result = result.rval
                    passed = expect == result
                    if not passed:
                        LOG().info('Expected "%s", got "%s".', expect, result)
                        return (False, '%s != %s' % (expect, result))
                    return passed
                _new_expect.expected = expect
            del dcl['EXPECT']
            dcl['check_result'] = _new_expect
        except KeyError:
            # EXPECT might be defined in some subclass
            pass

        return super(CheckResultMetaClass, mcs).__new__(mcs, name, bases, dcl)

class MultiplexerMetaClass(abc.ABCMeta):
    """
    Meta class for node command (not an end-point command). It handles
    following class properties:

        ``COMMANDS`` : ``dict``
            Command names with assigned command classes. Each of them is a
            direct subcommands of command with this property. Mandatory
            property.

        ``FALLBACK_COMMAND`` : :py:class:`~.endpoint.LmiEndPointCommand`
            Command factory to use in case that no command is passed on command
            line.

    Formatting options (starting with ``FMT_`` are also accepted, and may used
    to set defaults for all subcommands.
    """

    def __new__(mcs, name, bases, dcl):
        if dcl.get('__metaclass__', None) is not MultiplexerMetaClass:
            module_name = dcl.get('__module__', name)
            # check COMMANDS property and make it a classmethod
            if not 'COMMANDS' in dcl:
                raise errors.LmiCommandError(module_name, name,
                        'Missing COMMANDS property.')
            cmds = dcl.pop('COMMANDS')
            if not isinstance(cmds, dict):
                raise errors.LmiCommandInvalidProperty(module_name, name,
                        'COMMANDS must be a dictionary')
            if not all(isinstance(c, basestring) for c in cmds.keys()):
                raise errors.LmiCommandInvalidProperty(module_name, name,
                        'Keys of COMMANDS dictionary must contain command'
                        ' names as strings.')
            for cmd_name, cmd in cmds.items():
                if not util.RE_COMMAND_NAME.match(cmd_name):
                    raise errors.LmiCommandInvalidName(
                            module_name, name, cmd_name)
                if not issubclass(cmd, base.LmiBaseCommand):
                    raise errors.LmiCommandError(module_name, name,
                            'COMMANDS dictionary must be composed of'
                            ' LmiBaseCommand subclasses, failed class: "%s"'
                            % cmd.__name__)
                if cmd.is_multiplexer() and not cmd.has_own_usage():
                    LOG().warn('Command "%s.%s" is missing usage string.'
                            ' It will be inherited from parent command.',
                            cmd.__module__, cmd.__name__)
                    cmd.__doc__ = dcl['__doc__']
            def _new_child_commands(_cls):
                """ Returns list of subcommands. """
                return cmds
            dcl['child_commands'] = classmethod(_new_child_commands)

            _handle_usage(name, bases, dcl)
            _handle_fallback_command(name, bases, dcl)
            _handle_format_options(name, bases, dcl)

        return super(MultiplexerMetaClass, mcs).__new__(mcs, name, bases, dcl)

class SelectMetaClass(abc.ABCMeta):
    """
    Meta class for select commands with guarded commands. Additional handled
    properties:

        ``SELECT`` : ``list``
            List of commands guarded with expressions representing requirements
            on server's side that need to be met.
        ``DEFAULT`` : ``str`` or :py:class:`~.base.LmiBaseCommand`
            Defines fallback command used in case no condition can is
            satisfied.
    """

    def __new__(mcs, name, bases, dcl):
        if dcl.get('__metaclass__', None) is not SelectMetaClass:
            module_name = dcl.get('__module__', name)
            if not '__doc__' in dcl:
                LOG().warn('Command selector "%s.%s" is missing short'
                    ' description string (__doc__).',
                        module_name, name)
                default = dcl.get('DEFAULT', None)
                if (    default is not None
                        and issubclass(default, base.LmiBaseCommand)
                        and getattr(dcl['DEFAULT'], '__doc__', None)):
                    LOG().warn('Using __doc__ string from default command for'
                        ' selector "%s.%s".', module_name, name)
                    dcl['__doc__'] = dcl['DEFAULT'].__doc__
            _handle_select(name, dcl)
        return super(SelectMetaClass, mcs).__new__(mcs, name, bases, dcl)

