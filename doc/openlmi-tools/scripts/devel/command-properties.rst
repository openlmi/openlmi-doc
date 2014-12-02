.. _command_properties:

Command properties
==================

As noted before in :ref:`end-point_commands`, command at first tries to
process input arguments, calls an associated function and then renders its
result. We'll now introduce properties affecting this process.

Command class properties are written in their bodies and handled by their
metaclasses. After being processed, they are removed from class. So they are
not accessible as class attributes or from their instances.

.. _pre_processing_properties:

Options pre-processing
----------------------
Influencing properties:

    * ``OPT_NO_UNDERSCORES`` (opt_no_underscores_)
    * ``ARG_ARRAY_SUFFIX``   (arg_array_suffix_)
    * ``OWN_USAGE``          (own_usage_)

docopt_ will make a dictionary of options based on usage string such
as the one above (:ref:`usage_string`). Options dictionary matching this
example looks like this: ::

    { 'list'       : bool    #  Usage:
    , '--all'      : bool    #      %(cmd)s list [--all | --disabled]
    , '--disabled' : bool    #      %(cmd)s start <service>
    , 'start'      : bool    #  
    , '<service>'  : str     #  Options:
    }                        #      --all       List all services available.
                             #      --disabled  List only disabled services.

Values of this dictionary are passed to an associated function as arguments
with names created out of matching keys. Since argument names can not contain
characters such as ``<, >, -,`` etc., these need to be replaced.
Process of renaming of these options can be described by the following pseudo
algorithm:

.. _options_transform_algorithm:

    1. arguments enclosed in brackets are un-surrounded -- brackets get
       removed ::

        "<service>" -> "service"

    2. arguments written in upper case are made lower cased ::

        "FILE" -> "file"

    3. prefix of short and long options made of dashes shall be replaced with
       single underscore ::

        "-a"    -> "_a"
        "--all" -> "_all"

    4. any non-empty sequence of characters not allowed in python's identitier
       shall be replaced with a single underscore ::

        "_long-option"     -> "_long_option"
        "special--cmd-#2"  -> "special_cmd_2"

Points 3 and 4 could be merged into one. But we separate them due to effects
of ``OPT_NO_UNDERSCORES`` property described below.

.. seealso::
    Notes in :ref:`end-point_commands` for method
    :py:meth`lmi.scripts.common.command.endpoint.LmiEndPointCommand.transform_options`
    which is issued before the above algorithm is run.

Treating dashes
~~~~~~~~~~~~~~~
Single dash and double dash are special cases of commands.

Double dash in usage string allows to pass option-like argument to a script
e.g.: ::

    lmi file show -- --file-prefix-with-double-dash

Without the ``'--'`` argument prefixing the file, docopt_ would throw an error
because of ``--file-prefix-with-double-dash`` being treated as an unknown
option. This way it's correctly treated as an argument ``<file>`` given the
usage string: ::

    Usage: %(cmd)s file show [--] <file>

Double dash isn't passed to an associated function.

Single dash on a command line is commonly used to specify ``stdout`` or
``stdint``. For example in the following snippet: ::

    Usage: %(cmd)s file copy (- | <file>) <dest>

``'-'`` stands for standard input which will be read instead of a file if the
user wishes to.

Property descriptions
~~~~~~~~~~~~~~~~~~~~~
.. _opt_no_underscores:

``OPT_NO_UNDERSCORES`` : ``bool`` (defaults to ``False``)
    Modifies point 3 of options pre-processing. It causes the prefix of dashes
    to be completely removed with no replacement: ::

        "--long-options" -> "long-option"

    This may not be save if there is a command with the same name as the
    option being removed. Setting this property to ``True`` will cause
    overwriting the command with a value of option. A warning shall be
    echoed if such a case occurs.

.. _arg_array_suffix:

``ARG_ARRAY_SUFFIX`` : ``str`` (defaults to ``""``)
    Adds additional point (5) to `options_transform_algorithm`_. All
    repeatable arguments, resulting in a ``list`` of items, are renamed to
    ``<original_name><suffix>`` [#]_. Repeatable argument in usage string
    looks like this: ::

        """
        Usage: %(cmd)s start <service> ...
        """

    Causing all of the ``<service>`` arguments being loaded into a ``list``
    object.

.. _own_usage:

``OWN_USAGE`` : ``bool`` (defaults to ``False``)
    Says whether the documentation string of this class is a usage string.
    Each command in hierarchy can have its own usage string.

    This can also be assigned a usage string directly: ::

        class MySubcommand(LmiCheckResult):
            """
            Class doc string.
            """
            OWN_USAGE = "Usage: %(cmd)s --opt1 --opt1 <file> <args> ..."
            EXPECT = 0

    But using a boolean value is more readable: ::

        class MySubcommand(LmiCheckResult):
            """
            Usage: %(cmd)s --opt1 --opt1 <file> <args> ...
            """
            OWN_USAGE = True
            EXPECT = 0

    .. note::

        Using own usage strings in end-point commands is not
        recommended. It brings a lot of redundancy and may prove problematic
        to modify while keeping consistency among hierarchically nested
        usages.

        It's more readable to put your usage strings in your command
        multiplexers and put each of them in its own module.

        .. seealso::
            :ref:`command_multiplexers`

.. _associating_a_function:

Associating a function
----------------------
Influencing properties:

    * ``CALLABLE`` (callable_)

When command is invoked, its method
:py:meth:`~lmi.scripts.common.command.endpoint.LmiEndPointCommand.execute` will
get verified and transformed options as positional and keyword arguments.
This method shall pass them to an associated function residing in script
library and return its result on completion.

One way to associate a function is to use ``CALLABLE`` property. The other
is to define very own ``execute()`` method like this: ::

    class Lister(command.LmiInstanceLister):
        PROPERTIES = ('Name', "Started", 'Status')

        def execute(self, ns, _all, _disabled, _oneshot):
            kind = 'enabled'
            if _all:
                kind = 'all'
            elif _disabled:
                kind = 'disabled'
            elif _oneshot:
                kind = 'oneshot'
            for service_inst in service.list_services(ns, kind):
                yield service_inst

This may come handy if the application object [#]_ needs to be accessed or
if we need to decide which function to call based on command line options.

.. _property_descriptions:

Property descriptions
~~~~~~~~~~~~~~~~~~~~~
.. _callable:

``CALLABLE`` : ``str`` (defaults to ``None``)
    This is a mandatory option if
    :py:meth:`~lmi.scripts.common.command.endpoint.LmiEndPointCommand.execute`
    method is not overriden. It may be a string composed of a full path of
    module and its callable delimited with ``':'``: ::

        CALLABLE = 'lmi.scripts.service:start'

    Causes function ``start()`` of ``'lmi.scripts.service'`` module to be
    associated with command.

    Callable may also be assigned directly like this: ::

        from lmi.scripts import service
        class Start(command.LmiCheckResult):
            CALLABLE = service.start
            EXPECT = 0

    The first variant (by assigning string) comes handy if the particular
    module of associated function is not yet imported. Thus delaying the import
    until the point of function's invocation - if the execution comes to this
    point at all. In short it speeds up execution of *LMI metacommand* by
    reducing number of module imports that are not needed.

.. _function_invocation:

Function invocation
-------------------
Influencing properties:

    * ``NAMESPACE`` (namespace_)
    * ``CONNECTION_TIMEOUT`` (timeout_)

Property descriptions
~~~~~~~~~~~~~~~~~~~~~

.. _namespace:

``NAMESPACE`` : ``str`` (defaults to ``None``)
    This property affects the first argument passed to an associated function.
    Various values have different impact:

    +-----------+---------------------------------------+---------------------------------------------------+
    | Value     | Value of first argument.              | Its type                                          |
    +===========+=======================================+===================================================+
    | ``None``  | Same impact as value ``"root/cimv2"`` | :py:class:`lmi.shell.LMINamespace.LMINamespace`   |
    +-----------+---------------------------------------+---------------------------------------------------+
    | ``False`` | Raw connection object                 | :py:class:`lmi.shell.LMIConnection.LMIConnection` |                    
    +-----------+---------------------------------------+---------------------------------------------------+
    | any path  | Namespace object with given path      | :py:class:`lmi.shell.LMINamespace.LMINamespace`   |
    +-----------+---------------------------------------+---------------------------------------------------+

    This usually won't need any modification. Sometimes perhaps associated
    function might want to access more than one namespace, in that case an
    instance of :py:class:`~lmi.shell.LMIConnection.LMIConnection` might prove more useful.

    Namespace can also be overriden globally in a configuration file or with
    an option on command line.

.. _timeout:

``CONNECTION_TIMEOUT`` : ``int`` (defaults to ``None``)
    Specifies maximum number of seconds we should wait for broker's reply. If
    reached, :py:class:`~lmi.shell.LMIExceptions.ConnectionError` will be
    raised. The default value is provided by underlying library [#]_.

Output rendering
----------------
All these options begin with ``FMT_`` which is a shortcut for *formatter* as
they become options to formatter objects. These can be defined not only in
end-point commands but also in multiplexers. In the latter case they set the
defaults for all their direct and indirect child commands.

.. note::
    These options override configuration settings and command line options.
    Therefor use them with care.

They are:

.. _fmt_no_headings:

``FMT_NO_HEADINGS`` : ``bool`` (defaults to ``False``)
    Allows to suppress headings (column or row names) in the output.

    .. note::
        With :ref:`lmi_lister` command it's preferable to set the *COLUMNS*
        property to empty list instead. Otherwise associated function is
        expected to return column headers as a first row in its result.

.. _fmt_human_friendly:

``FMT_HUMAN_FRIENDLY`` : ``bool`` (defaults to ``False``)
    Forces the output to be more pleasant to read by human beings.

.. _specifying_requirements:

Command specific properties
---------------------------
Each command class can have its own specific properties. Let's take a look on
them.

``LmiCommandMultiplexer``
~~~~~~~~~~~~~~~~~~~~~~~~~
.. _commands:

``COMMANDS`` : ``dict`` (mandatory)
    Dictionary assigning subcommands to their names listed in usage string.
    Example follows: ::

        class MyCommand(LmiCommandMultiplexer):
            '''
            My command description.

            Usage: %(cmd)s mycommand (subcmd1 | subcmd2)
            '''
            COMMANDS = {'subcmd1' : Subcmd1, 'subcmd2' : Subcmd2}
            OWN_USAGE = True

    Where ``Subcmd1`` and ``Subcmd2`` are some other ``LmiBaseCommand``
    subclasses. Documentation string must be parseable with docopt_.

    ``COMMANDS`` property will be translated to
    :py:meth:`~lmi.scripts.common.command.multiplexer.LmiCommandMultiplexer.child_commands`
    class method by
    :py:class:`~lmi.scripts.common.command.meta.MultiplexerMetaClass`.

``FALLBACK_COMMAND`` : :py:class:`lmi.scripts.common.command.endpoint.LmiEndPointCommand`
    Command class used when no command defined in ``COMMANDS`` dictionary is
    passed on command line.

    Take for example this usage string: ::

        """
        Display hardware information.

        Usage:
            %(cmd)s [all]
            %(cmd)s system
            %(cmd)s chassis
        """

    This suggests there are tree commands defined taking care of listing
    hardware informations. Entry point definition could look like this: ::

        class Hardware(command.LmiCommandMultiplexer):
            OWN_USAGE = __doc__     # usage string from above
            COMMANDS  = { 'all'     : All
                        , 'system'  : System
                        , 'chassis' : Chassis
                        }
            FALLBACK_COMMAND = All

    Without the ``FALLBACK_COMMAND`` property, the multiplexer would not
    handle the case when ``'all'`` argument is omitted as is suggested in
    the usage string. Adding it to command properties causes this multiplexer
    to behave exactly as ``All`` subcommand in case that no command
    is given on command line.

.. _lmi_select_command_properties:

``LmiSelectCommand`` properties
-------------------------------
Following properties allow to define profile and class requirements for
commands.

.. _select:

``SELECT`` : ``list`` (mandatory)
    Is a list of pairs ``(condition, command)`` where ``condition`` is an
    expression in *LMIReSpL* language. And ``command`` is either a string with
    absolute path to command that shall be loaded or the command class itself.

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
    ``openlmi-hardware`` package older than ``0.4.2``. Use the ``HwCmd``
    anywhere else where also the ``LMI_Chassis`` CIM class in version ``0.3.0``
    is available.

    First matching condition wins and assigned command will be passed all the
    arguments. If no condition can be satisfied and no default command is set,
    an exception will be raised.

    .. seealso::
        Definition of *LMIReSpL* mini-language:
        :py:mod:`~lmi.scripts.common.versioncheck.parser`

.. _default:

``DEFAULT`` : ``string`` or reference to command class
    Defines fallback command used in case no condition in ``SELECT`` can be
    satisfied.

.. _lmi_lister_properties:

``LmiLister`` properties
~~~~~~~~~~~~~~~~~~~~~~~~
.. _columns:

``COLUMNS`` : ``tuple``
    Column names. It's a tuple with name for each column. Each row of data
    shall then contain the same number of items as this tuple. If omitted,
    associated function is expected to provide them in the first row of
    returned list. It's translated to
    :py:meth:`~lmi.scripts.common.command.lister.LmiBaseListerCommand.get_columns`
    class method.

    If set to empty list, no column headers will be printed. Every item of
    returned list of associated function will be treated as data. Note that
    setting this to empty list makes the *FMT_NO_HEADINGS* property
    redundant.

.. _lmi_instance_commands_properties:
.. _lmi_show_instance_properties:
.. _lmi_instance_lister_properties:

``LmiShowInstance`` and ``LmiInstanceLister`` properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
These two classes expect, as a result of their associated function, an instance
or a list of instances of some CIM class. They take care of rendering them to
standard output. Thus their properties affect the way how their properties
are rendered.

.. _properties:

``PROPERTIES`` : ``tuple``
    Property names in the same order as the properties shall be listed. Items
    of this tuple can take multiple forms:

    Property Name : ``str``
        Will be used for the name of column/property in output table and the
        same name will be used when obtaining the value from instance. Thus
        this form may be used only if the property name of instance can appear
        as a name of column.

    (Column Name, Property Name) : ``(str, str)``
        This pair allows to render value of property under different name
        (*Column Name*).

    (Column Name, getter) : ``(str, callable)``
        This way allows the value to be arbitrarily computed. The second
        item is a callable taking one and only argument -- the instance of
        class to be rendered.

    Example below shows different ways of rendering attributes for instances
    of ``LMI_Service`` CIM class: ::

        class Show(command.LmiShowInstance):
            CALLABLE = 'lmi.scripts.service:get_instance'
            PROPERTIES = (
                    'Name',
                    ('Enabled', lambda i: i.EnabledDefault == 2),
                    ('Active', 'Started'))

    First property will be shown with the same label as the name of property.
    Second one modifies the value of ``EnabledDefault`` from ``int`` to
    ``bool`` representing enabled state. The last one uses different label for
    property name ``Started``.

.. _dynamic_properties:

``DYNAMIC_PROPERTIES`` : ``bool`` (defaults to ``False``)
    Whether the associated function is expected to return the properties tuple
    itself. If ``True``, the result of associated function must be in form: ::

        (properties, data)

    Where ``properties`` have the same inscription and meaning as a
    ``PROPERTIES`` property of class.

    Otherwise, only the ``data`` is expected.

    .. note::
        Both :py:class:`~lmi.scripts.common.command.show.LmiShowInstance`
        and :py:class:`~lmi.scripts.common.command.lister.LmiInstanceLister`
        expect different ``data`` to be returned. See :ref:`lmi_show_instance`
        and :ref:`lmi_instance_lister` for more information.

.. note::

    Omitting both ``PROPERTIES`` and ``DYNAMIC_PROPERTIES`` makes the
    ``LmiShowInstance`` render all attributes of instance. For
    ``LmiInstanceLister`` this is not allowed, either ``DYNAMIC_PROPERTIES``
    must be ``True`` or ``PROPERTIES`` must be filled.


.. _lmi_check_result_properties:

``LmiCheckResult`` properties
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This command typically does not produce any output if operation succeeds. The
operation succeeds if the result of associated function is expected. There are
more ways how to say what is an expected result. One way is to use ``EXPECT``
property. The other is to provide very own implementation of
:py:class:`~lmi.scripts.common.command.checkresult.LmiCheckResult.check_result`
method.

.. _expect:

``EXPECT``: (mandatory)
    Any value can be assigned to this property. This value is then expected
    to be returned by associated function. Unexpected result is treated
    as an error.

    A callable object assigned here has special meaning. This object must
    accept exactly two parameters:

        1. options - Dictionary with parsed command line options returned by
           docopt_ after being processed by
           :py:meth:`~lmi.scripts.common.command.endpoint.LmiEndPointCommand.transform_options`.
        2. result - Return value of associated function.

    If the associated function does not return an expected result, an error
    such as: ::

        There was 1 error:
        host kvm-fedora-20
            0 != 1

    will be presented to user which is not much helpful. To improve user
    experience, the
    :py:class:`~lmi.scripts.common.command.checkresult.LmiCheckResult.check_result`
    method could be implemented instead. Note the example: ::

        class Update(command.LmiCheckResult):
            ARG_ARRAY_SUFFIX = '_array'

            def check_result(self, options, result):
                """
                :param list result: List of packages successfuly installed
                    that were passed as an ``<package_array>`` arguments.
                """
                if options['<package_array>'] != result:
                    return (False, ('failed to update packages: %s' %
                            ", ".join( set(options['<package_array>'])
                                     - set(result))))
                return True

    The ``execute()`` method is not listed to make the listing shorter. This
    command could be used with usage string such as: ::

        %(cmd)s update [--force] [--repoid <repository>] <package> ...

    In case of a failure, this would produce output like this one: ::

        $ lmi sw update wt wt-doc unknownpackage
        There was 1 error:
        host kvm-fedora-20
            failed to update packages: unknownpackage

.. seealso::

    Docopt_ home page and its git: http://github.org/docopt/docopt.

-------------------------------------------------------------------------------

.. [#] Angle brackets here just mark the boundaries of name components. They
       have nothing to do with arguments.
.. [#] Application object is accessible through ``app`` property of each
       command instance.
.. [#] *lmiwbem*'s default timeout is 1 minute as of now.

.. ****************************************************************************

.. _CIM:            http://dmtf.org/standards/cim
.. _OpenLMI:        http://fedorahosted.org/openlmi/
.. _openlmi-tools:  http://fedorahosted.org/openlmi/wiki/shell
.. _docopt:         http://docopt.org/
.. _docopt-git:     http://github.org/docopt

