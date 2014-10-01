Basics
======
This provides a general overview on what script is, how is it written
and is interfaced with.

Prerequisities
--------------
Reader should be familiar with a CIM_ (Common Information Model). He should
have a general idea about, what OpenLMI_ is and what it does. He should get
familiar with LMIShell_, which is a python binary shipped with
:ref:`openlmi-tools`.

Also user should be familiar with standard \*nix command line
utilities [#]_.

Introduction
------------
By a *script* in this document we mean:

  * Python library utilizing LMIShell_ for instrumenting CIM providers through
    a CIMOM broker. It resides in ``lmi.scripts.<script_name>`` package. Where
    ``<script_name>`` usually corresponds to some *LMI* profile name.
  * Command wrappers for this library as a set of classes inheriting from
    :py:class:`~lmi.scripts.common.command.base.LmiBaseCommand`. These may
    create a tree-like hierarchy of commands. They are the entry points of
    *LMI metacommand* to the wrapped functionality of library.

Command wrappers are part of the library usually grouped in a single
module named after the ``lmi`` command or ``cmd``: ::

    lmi.scripts.<script_name>.cmd

Writing a library
-----------------
Library shall consist of a set of functions taking a :ref:`namespace
<namespaces>` or connection object as a first argument. There are no special
requirements on how to divide these functions into submodules. Use common
sense. Smaller scripts can have all functionality in
``lmi/scripts/<script_name>/__init__.py`` module. With wrappers usually
contained in ``lmi/scripts/<script_name>/cmd.py``.

Library should be written with an ease of use in mind. Functions should
represent possible use cases of what can be done with particular
providers instead of wrapping 1-to-1 a CIM class's methods in python
functions.

Any function that shall be called by a command wrapper and communicates with a
CIMOM must accept a namespace object named as ``ns``. It's an instance of
:py:class:`~lmi.shell.LMINamespace.LMINamespace` providing quick access to
represented CIM namespace [#]_ and its classes. It's also possible to specify
that function shall be passed a raw
:py:class:`~lmi.shell.LMIConnection.LMIConnection` object. For details see
:ref:`function_invocation`.

Service example
~~~~~~~~~~~~~~~
Suppose we have a service profile in need of ython interface. Real provider
implementation can be found at ``src/service`` directory in upstream git [#]_.
For more information please refer to `service description`_.

As you may see, this implements single CIM class ``LMI_Service`` with a few
useful methods such as:

    * ``StartService()``
    * ``StopService()``

We'd like to provide a way how to list system services, get a details for one
of them and allow to start, stop and restart them.

Simplified [#]_ version of some of these functions may look like this: ::

    def list_services(ns, kind='enabled'):
        for service in sorted(ns.LMI_Service.instances(),
                    key=lambda i: i.Name):
            if kind == 'disabled' and service.EnabledDefault != \
                    ns.LMI_Service.EnabledDefaultValues.Disabled:
                continue
            if kind == 'enabled' and service.EnabledDefault != \
                    ns.LMI_Service.EnabledDefaultValues.Enabled:
                # list only enabled
                continue
            yield service

It yields instances of ``LMI_Service`` cim class. We prefer to use ``yield``
instead of ``return`` when enumerating instances because of memory usage
reduction. For example when the user limits the number of instances listed.
With ``yield`` the number of iterations will be reduced automatically.

::

    from lmi.shell import LMIInstanceName
    from lmi.scripts.common import get_logger
    from lmi.scripts.common.errors import LmiFailed

    LOG = get_logger(__name__)

    def start_service(ns, service):
        if isinstance(service, basestring):
            # let's accept service as a string
            inst = ns.LMI_Service.first_instance(key="Name", value=service)
            name = service
        else:   # or as LMIInstance or LMIInstanceName
            inst = service
            name = inst.path['Name']
        if inst is None:
            raise LmiFailed('No such service "%s".' % name)
        if isinstance(inst, LMIInstanceName):
            # we need LMIInstance
            inst = inst.to_instance()
        res = inst.StartService()
        if res == 0:
            LOG().debug('Started service "%s" on hostname "%s".',
                        name, ns.hostname)
        return res

In similar fashion, ``stop_service``, ``restart_service`` and others could be
written.

``ns`` argument typically represents ``root/cimv2`` namespace which is the
main implementation namespace for ``OpenLMI`` providers. One could also make
these functions act upon a connection object like this: ::

    def get_instance(c, service):
        inst = c.root.cimv2.LMI_Service.first_instance(
                    key="Name", value=service)
        if inst is None:
            raise LmiFailed('No such service "%s".' % service)
        return inst

User can then easily access any other namespace he may need. Command classes
need to be informed about an object type the wrapped function expects (see
:ref:`function_invocation`).

The ``LOG`` variable provides access to the logger of this module. Messages
logged in this way end up in a log file [#]_ and console. Implicitly only
warnings and higher priority messages are logged into a console. This can
be changed with metacommand's parameteres.

If operation fails due to some unexpected error, please raise
:py:class:`~lmi.scripts.common.errors.LmiFailed` exception with human readable
description.

.. seealso::
    Exceptions_ for conventions on using exceptions.

    `Upstream git`_ for more *real world* examples.


.. _command_wrappers_overview:

Command wrappers overview
-------------------------
They are a set of command classes wrapping up library's functionality. They are
structured in a tree-like hierarchy where the root [#]_ command appears in a
help message of *LMI metacommand*. All commands are subclasses of
:py:class:`~lmi.scripts.common.command.base.LmiBaseCommand`.

Behaviour of commands is controlled by class properties such as these: ::

    class Show(command.LmiShowInstance):
        CALLABLE = 'lmi.scripts.service:get_instance'
        PROPERTIES = (
                'Name',
                'Caption',
                ('Enabled', lambda i: i.EnabledDefault == 2),
                ('Active', 'Started'),
                'Status')

Example above contains definition of ``Show`` command wrapper for instances of
``LMI_Service``. Its associated function is ``get_instance()`` located in
``lmi.scripts.service`` module [#]_. Properties used will be described
in detail :ref:`later <lmi_instance_commands_properties>`. Let's just say,
that ``PROPERTIES`` specify a way how the instance is rendered.

.. _top-level-commands:

Top-level commands
~~~~~~~~~~~~~~~~~~
Are entry points of a script library. They are direct subcommands of ``lmi``.
For example: ::

    $ lmi help
    $ lmi service list
    $ lmi sw show openlmi-providers

``help``, ``service`` and ``sw`` are top-level commands. One script (such as
``service`` above) can provide one or more of them. They need to be listed in a
``setup.py`` script in ``entry_points`` argument of ``setup()`` function. More
details will be noted later in `Setup script`_.

They contain usage string which is a documentation and prescription of
command-line arguments in one string. This string is printed when user
requests command's help: ::

    $ lmi help service

.. _usage_string:

Usage string
^^^^^^^^^^^^
looks like this: ::

    """
    System service management.

    Usage:
        %(cmd)s list [--all | --disabled]
        %(cmd)s start <service>

    Options:
        --all       List all services available.
        --disabled  List only disabled services.
    """

Format of this string is very important. It's parsed by a docopt_ command line
parser which uses it for parsing command-line arguments. Please refer to its
documentation for details.

.. note::

    There is one deviation to *common* usage string. It's the use of
    ``%(cmd)s`` formatting mark. It is replaced with full command's name.
    Full name means that all subcommands and binary name prefixing current
    command on command line are part of it. So for example full name of
    command **list** in a following string passed to command line: ::

        lmi sw list pkgs

    is ``lmi sw list``.

    If parsing **sw** usage, it is just ``lmi sw``.

    The formatting mark is mandatory.

Options and arguments given on command-line are :ref:`pre-processed
<pre_processing_properties>` before they are passed to *end-point command*. You
should get familier with it before writing your own usage strings.

.. _end-point_commands_introduction:

End-point commands
~~~~~~~~~~~~~~~~~~
Are associated with one or more function of script library. They handle the
following:

    1. call docopt_ parser on command line arguments
    2. make some name pre-processing on them (see
       :ref:`pre_processing_properties`)
    3. verify them (see :ref:`end-point_commands`)
    4. transform them (see :ref:`end-point_commands`)
    5. pass them to associated function
    6. collect results
    7. render them and print them

Developper of command wrappers needs to be familiar with each step. We will
describe them later in details.

There are following end-point commands available for subclassing:

    * ``LmiCheckResult``    (see :ref:`lmi_check_result`)
    * ``LmiLister``         (see :ref:`lmi_lister`)
    * ``LmiInstanceLister`` (see :ref:`lmi_instance_lister`)
    * ``LmiShowInstance``   (see :ref:`lmi_show_instance`)

They differ in how they render the result obtained from associated function.

These are documented in depth in :ref:`end-point_commands`.

.. _command_multiplexers_introduction:

Command multiplexers
~~~~~~~~~~~~~~~~~~~~
Provide a way how to group multiple commands under one. Suppose you want to
list packages, repositories and files. All of these use cases need different
arguments, and render different information thus they should be represented by
independent end-point commands. What binds them together is the user's intent
to *list* something. He may wish to do other operation like *show*, *add*,
*remove* etc. with the same subject. Having all combination of these intents
and subjects would generate a lot of commands under the top-level one. Let's
instead group them under particular *intent* like this:

    * ``sw list packages``
    * ``sw list repositories``
    * ``sw list files``
    * ``sw show package``

To reflect it in our commands hierarchy, we need to use
:py:class:`~lmi.scripts.common.command.multiplexer.LmiCommandMultiplexer`
command.

::

    class Lister(command.LmiCommandMultiplexer):
        """ List information about packages, repositories or files. """
        COMMANDS = {
                'packages'     : PkgLister,
                'repositories' : RepoLister,
                'files'        : FileLister
        }

Where ``COMMANDS`` property maps command classes to their names. Each command
multiplexer consumes one command argument from command line, denoting its
direct subcommand and passes the rest of options to it. In this way we can
create arbitrarily tall command trees.

Top-level command is nothing else than a subclass of ``LmiCommandMultiplexer``.

Specifying profile and class requirements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Most commands require some provider installed on managed machine to work
properly. Each such provider should be represented by an instance of
``CIM_RegisteredProfile`` on remote broker. This instance looks like
this (in MOF syntax): ::

    instance of CIM_RegisteredProfile {
        InstanceID = "OpenLMI+OpenLMI-Software+0.4.2";
        RegisteredOrganization = 1;
        OtherRegisteredOrganization = "OpenLMI";
        RegisteredVersion = "0.4.2";
        AdvertiseTypes = [2];
        RegisteredName = "OpenLMI-Software";
    };

We are interested just in ``RegisteredName`` and ``RegisteredVersion``
properties that we'll use for requirement specification.

Requirement is written in *LMIReSpL* language. For its formal definition
refer to documentation of :py:mod:`~lmi.scripts.common.versioncheck.parser`.
Since the language is quite simple, few examples should suffice:

    ``'OpenLMI-Software < 0.4.2'``
        Requires OpenLMI Software provider to be installed in version lower
        than ``0.4.2``.
    ``'OpenLMI-Hardware == 0.4.2 & Openlmi-Software >= 0.4.2'``
        Requires both hardware and software providers to be installed in
        particular version. Short-circuit evaluation is utilized here. It
        means that in this example OpenLMI Software won't be queried unless
        OpenLMI Hardware is installed and having desired version.
    ``'profile "OpenLMI-Logical File" > 0.4.2'``
        If you have spaces in the name of profile, surround it in double
        quotes. ``profile`` keyword is optional. It could be also present in
        previous examples.

Version requirements are not limited to profiles only. CIM classes may be
specified as well:

    ``'class LMI_SoftwareIdentity >= 0.3.0 & OpenLMI-LogicalFile'``
        In case of class requirements the ``class`` keyword is mandatory. As
        you can see, version requirement is optional.
    ``'! (class LMI_SoftwareIdentity | class LMI_UnixFile)'``
        Complex expressions can be created with the use of brackets and other
        operators.

One requirement is evaluated in these steps:

    Profile requirement
        1. Query ``CIM_RegisteredProfile`` for instances with
           ``RegisteredName`` matching given name. If found, go to 2. Otherwise
           query ``CIM_RegisteredSubProfile`` [#subprof]_ for instances with
           ``RegisteredName`` matching given name. If not found return
           ``False``.
        2. Select the (sub)profile with highest version and go to 3.
        3. If the requirement has version specification then compare it to the
           value of ``RegisteredVersion`` using given operator. If the relation
           does not apply, return ``False``.
        4. Return ``True``.

    Class requirement
        1. Get specified class. If not found, return ``False``.
        2. If the requirement has version specification then compare it to the
           value of ``Version`` [#missing_version]_ qualifier of
           obtained class using given operator. And if the relation
           does not apply, return ``False``.
        3. Return ``True``.

Now let's take a look, where these requirements can be specified.
There is a special select command used to specify which command to load
for particular version on remote broker. It can be written like this: ::

    from lmi.scripts.common.command import LmiSelectCommand

    class SoftwareCMD(LmiSelectCommand):

        SELECT = [
              ( 'OpenLMI-Software >= 0.4.2 & OpenLMI-LogicalFile'
              , 'lmi.scripts.software.current.SwLFCmd')
            , ( 'OpenLMI-Software >= 0.4.2'
              , 'lmi.scripts.software.current.SwCmd')
            , ('OpenLMI-Software', 'lmi.scripts.software.pre042.SwCmd')
        ]

It says to load ``SwLFCmd`` command in case both OpenLMI Software and
OpenLMI LogicalFile providers are installed. If not, load the ``SwCMD`` from
``current`` module for OpenLMI Software with recent version and fallback to
``SwCmd`` for anything else. If the OpenLMI Software provider is not available
at all, no command will be loaded and exception will be raised.

Previous command could be used as an entry point in your ``setup.py`` script
(see the :ref:`entry_points`). There is also a utility that makes it look
better: ::

    from lmi.scripts.common.command import select_command

    SoftwareCMD = select_command('SoftwareCMD',
          ( 'OpenLMI-Software >= 0.4.2 & OpenLMI-LogicalFile'
          , 'lmi.scripts.software.current.SwLFCmd'),
          ( 'OpenLMI-Software >= 0.4.2', 'lmi.scripts.software.current.SwCmd'),
          ('OpenLMI-Software', 'lmi.scripts.software.pre042.SwCmd')
    )

.. seealso::
    Documentation of
    :py:class:`~lmi.scripts.common.command.select.LmiSelectCommand` and
    :py:class:`~lmi.scripts.common.command.helper.select_command`.

    And also notes on related :ref:`lmi_select_command_properties`.

Command wrappers module
~~~~~~~~~~~~~~~~~~~~~~~
Usually consists of:

    1. license header
    2. usage dostring - parseable by docopt_
    3. end-point command wrappers
    4. single top-level command

The top-level command is usally defined like this: ::

    Service = command.register_subcommands(
            'Service', __doc__,
            { 'list'    : Lister
            , 'show'    : Show
            , 'start'   : Start
            , 'stop'    : Stop
            , 'restart' : Restart
            },
        )

Where the ``__doc__`` is a `usage string`_ and module's doc string at the same
time. It's  mentioned in point 2. ``Service`` is a name, which will be listed
in ``entry_points`` dictionary described :ref:`below <entry_points>`. The
global variable's name we assign to should be the same as the value of the
first argument to
:py:func:`~lmi.scripts.common.command.helper.register_subcommands`. The last
argument here is the dictionary mapping all subcommands of **service** to their
names [#]_.

Egg structure
~~~~~~~~~~~~~
Script library is distributed as a python egg, making it easy to distribute
and install either to system or user directory.

Following tree shows directory structure of *service* egg residing in
`upstream git`_:

.. only:: not latex

    ::

        commands/service
        ├── lmi
        │   ├── __init__.py
        │   └── scripts
        │       ├── __init__.py
        │       └── service
        │           ├── cmd.py
        │           └── __init__.py
        ├── Makefile
        ├── README.md
        ├── setup.cfg
        └── setup.py.skel

.. raw:: latex

    \begin{center}
        \begin{tikzpicture}[dirtree]
            \node {commands/service}
                child { node {lmi}
                    child { node {\_\_init\_\_.py} }
                    child { node {scripts}
                        child { node {\_\_init\_\_.py} }
                        child { node {service}
                            child { node {cmd.py} }
                            child { node {\_\_init\_\_.py} }
                        }
                    }
                }
                child { node {Makefile} }
                child { node {README.md} }
                child { node {setup.cfg} }
                child { node {setup.py.skel} };
        \end{tikzpicture} \\
    \end{center}

This library then can be imported with: ::

    from lmi.scripts import service

``commands/service/lmi/scripts/service`` must be a package (directory with
``__init__.py``) because ``lmi.scripts`` is a namespace package. It
can have arbitrary number of modules and subpackages. The care should be taken
to make the API easy to use and learn though.

Use provided ``commands/make_new.py`` script to
:ref:`generated it <making_script_structure>`.

Setup script
------------
Follows a minimal example of ``setup.py.skel`` script for service library. ::

    from setuptools import setup, find_packages
    setup(
        name="openlmi-scripts-service",
        version="@@VERSION@@",
        description='LMI command for system service administration.',
        url='https://github.com/openlmi/openlmi-scripts',
        platforms=['Any'],
        license="BSD",
        install_requires=['openlmi-scripts'],
        namespace_packages=['lmi', 'lmi.scripts'],
        packages=['lmi', 'lmi.scripts', 'lmi.scripts.service'],

        entry_points={
            'lmi.scripts.cmd': [
                'service = lmi.scripts.service.cmd:Service',
                ],
            },
        )

It's a template with just one variable ``@@VERSION@@`` being replaced with
recent scripts version by running ``make setup`` command.

.. _entry_points:

Entry points
~~~~~~~~~~~~
The most notable argument here is ``entry_points`` which is a dictionary
containing python namespaces where plugins are registered. In this case, we
register single :ref:`top-level command <top-level-commands>` called
``service`` in ``lmi.scripts.cmd`` namespace. This particular namespace is used
by *LMI metacommand* when searching for registered user commands. ``Service`` is
a command multiplexer, created with a call to
:py:func:`~lmi.scripts.common.command.helper.register_subcommands` grouping
end-point commands together.

Next example shows set up with more top-level commands [#]_: ::

    entry_points={
        'lmi.scripts.cmd': [
            'fs = lmi.scripts.storage.fs_cmd:Fs',
            'partition = lmi.scripts.storage.partition_cmd:Partition',
            'raid = lmi.scripts.storage.raid_cmd:Raid',
            'lv = lmi.scripts.storage.lv_cmd:Lv',
            'vg = lmi.scripts.storage.vg_cmd:Vg',
            'storage = lmi.scripts.storage.storage_cmd:Storage',
            'mount = lmi.scripts.storage.mount_cmd:Mount',
        ],
    },

Conventions
-----------
There are several conventions you should try to follow in your shiny scripts.

Logging messages
~~~~~~~~~~~~~~~~
In each module where logging facilities are going to be used, define global
varibale ``LOG`` like this: ::

    from lmi.scripts.common import get_logger

    LOG = get_logger(__name__)

It's a callable used throughout particular module in this way: ::

    LOG().warn('All the data of "%s" will be lost!', partition)

Each message should be a whole sentence. It shall begin with an upper case
letter and end with a dot or other sentence terminator.

Bad example: ::

    LOG().info('processing %s', card)

Exceptions
~~~~~~~~~~
Again all the exceptions should be initialized with messages forming
a whole sentence.

They will be catched and printed on ``stderr`` by *LMI metacommand*. If the
*Trace* option in :ref:`sect_main` is on, traceback will be printed. There is
just one exception. If the exception inherits from
:py:class:`~lmi.scripts.common.errors.LmiError`, traceback won't be printed
unless verbosity level is the highest one as well: ::

    # self refers to some command
    self.app.config.verbosity == self.app.config.OUTPUT_DEBUG

This is a feature allowing for common error use-cases to be gracefully
handled. In your scripts you should stick to using
:py:class:`~lmi.scripts.common.errors.LmiFailed` for such exceptions.

Following is an example of such a common error-case, where printing traceback
does not add any interesting information: ::

    iname = ns.LMI_Service.new_instance_name({
        "Name": service,
        "CreationClassName" : "LMI_Service",
        "SystemName" : cs.Name,
        "SystemCreationClassName" : cs.CreationClassName
    })
    inst = iname.to_instance()
    if inst is None:
        raise errors.LmiFailed('No such service "%s".' % service)
    # process the service instance

``service`` is a name provided by user. If such a service is not found,
``inst`` will be assigned ``None``. In this case we don't want to continue in
script's execution thus we raise an exception. We provide very clear message
that needs no other comment. We don't want any traceback to be printed, thus
the use of :py:class:`~lmi.scripts.common.errors.LmiFailed`.

Debugging
---------
To hunt down problems of your script during its development, metacommand
comes with few options to assist you:

    ``--trace``
        This option turns on logging of tracebacks. Any exception but
        :py:exc:`~lmi.scripts.common.errors.LmiError` will be logged with
        traceback to ``stderr`` unless ``--quite`` option is on.
        :py:exc:`~lmi.scripts.common.errors.LmiError` will be logged with
        traceback if the verbosity (``-v``) is highest as well.
    ``-v``
        Raise a verbosity. Pass it twice to make the verbosity highest. That
        will cause a lot of messages being produced to ``stderr``. It also
        turns on logging of tracebacks for
        :py:exc:`~lmi.scripts.common.errors.LmiError` if ``--trace`` option is
        on as well.
    ``--log-file``
        Allows to specify output file, where logging takes place. Logging level
        is not affected by ``-v`` option. It can be specified in configuration
        file.

While you debug it's convenient to put above in your configuration file
``~/.lmirc``::

    [Main]
    # Print tracebacks.
    Trace = True

    [Log]
    OutputFile = /tmp/lmi.log
    # Logging level for OutputFile.
    Level = DEBUG

.. seealso::

    :ref:`configuration`

-------------------------------------------------------------------------------

.. seealso::

    Docopt_ documentation, :ref:`command_classes` and :ref:`command_properties`.

-------------------------------------------------------------------------------

.. [#] Described by a POSIX.
.. [#] Default namespace is ``"root/cimv2"``.
.. [#] view: https://fedorahosted.org/openlmi/browser/openlmi-providers
       git: ``ssh://git.fedorahosted.org/git/openlmi-providers.git/``
.. [#] Simplified here means that there are no documentation strings
       and no type checking.
.. [#] If logging to a file is enabled in configuration.
.. [#] Also called a top-level command.
.. [#] Precisely in an ``__init__.py`` module of this package.
.. [#] Taken from older version of storage script.
.. [#] These names must exactly match the names in usage strings.

.. [#subprof] This is a subclass of ``CIM_RegisteredProfile`` thus it has the
              same properties.
.. [#missing_version] If the Version qualifier is missing, -1 will be used
                      for comparison instead of empty string.

.. ****************************************************************************

.. _CIM:            http://dmtf.org/standards/cim
.. _OpenLMI:        http://openlmi.org
.. _docopt:         http://docopt.org/
.. _`service description`: https://fedorahosted.org/openlmi/wiki/service
.. _`upstream git`: https://github.com/openlmi/openlmi-scripts
.. _LMIShell: http://www.openlmi.org/using_lmishell
