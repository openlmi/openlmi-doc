.. _command_classes:

Command classes
===============
Before reading this, please make sure you're familiar with
:ref:`command_wrappers_overview`.

.. _end-point_commands:

End-point commands
------------------
Were already introduced before (see :ref:`end-point_commands_introduction`).
We'll dive into details here.

Every end-point command allows to verify and transform options parsed by
docopt_ before they are passed to associated function. This can happen in
methods:

``verify_options(self, options)``
    Taking pre-processed options dictionary as a first argument.
    Properties affecting this pre-processing can be found in
    :ref:`pre_processing_properties`. This method shall check option values or
    their combinations and raise
    :py:exc:`~lmi.scripts.common.errors.LmiInvalidOptions` if any inconsistency
    is discovered.

    Example usage: ::

        class FileLister(command.LmiInstanceLister):
            DYNAMIC_PROPERTIES = True

            def verify_options(self, options):
                file_types = { 'all', 'file', 'directory', 'symlink'
                             , 'fifo', 'device'}
                if (   options['--type'] is not None
                   and options['--type'] not in file_types):
                    raise errors.LmiInvalidOptions(
                            'Invalid file type given, must be one of %s' %
                                 file_types)

    .. seealso::
        API documentation on
        :py:meth:`~lmi.scripts.common.command.endpoint.LmiEndPointCommand.verify_options`

``transform_options(self, options)``
    Takes verified options dictionary which it modifies in place.

    Example usage: ::

        class Lister(command.LmiLister):
            COLUMNS = ('Device', 'Name', "ElementName", "Type")

            def transform_options(self, options):
                """
                Rename 'device' option to 'devices' parameter name for better
                readability.
                """
                options['<devices>'] = options.pop('<device>')

    .. seealso::
        API documentation on
        :py:meth:`~lmi.scripts.common.command.endpoint.LmiEndPointCommand.transform_options`

Above methods can be used to process options in a way that any script library
function can be called. In case we need more control over what is called or
when we want to decide at runtime which function shall be called, we may override
:py:meth:`~lmi.scripts.common.command.endpoint.LmiEndPointCommand.execute` method
instead. Example of this may be found at :ref:`associating_a_function`.

.. _lmi_check_result:

``LmiCheckResult``
~~~~~~~~~~~~~~~~~~
This command invokes associated function on hosts in session, collects results
from them and compares them to an expected value. It does not produce any
output, when all returned values are expected.

This command class is very useful when wrapping up some CIM class's method
such as ``LMI_Service::StartService()``. Example can be seen in
:ref:`property_descriptions`.

Its specific properties are listed in :ref:`lmi_check_result_properties`.

.. seealso::
    API documentation on
    :py:class:`~lmi.scripts.common.command.checkresult.LmiCheckResult`

.. _lmi_lister:

``LmiLister``
~~~~~~~~~~~~~
Prints tablelike data. It expects associated function to return its result
in form: ::

    [row1, row2, ...]

Where ``rowX`` is a tuple containing row values. Each such row is ``list`` or
``tuple`` of the same length. There is a property ``COLUMNS`` defining column
names [#]_ (see :ref:`lmi_lister_properties`). Generator is preferred over
a ``list`` of rows. ::

    class RaidList(command.LmiLister):
        COLUMNS = ('Name', "Level", "Nr. of members")

        def execute(self, ns):
            """
            Implementation of 'raid list' command.
            """
            for r in raid.get_raids(ns):
                members = raid.get_raid_members(ns, r)
                yield (r.ElementName, r.Level, len(members))

            # Could also be written as:
            #return [  (r.ElementName, r.Level, len(raid.get_raid_members(ns, r)))
            #       for r in raid.get_raids(ns)]

produces: ::

    $ lmi -h $HOST storage raid list
    Name  Level Nr. of members
    raid5 5     3

If ``COLUMNS`` property is omitted, returned value shall take the following
form instead: ::

    (columns, data)

Where ``columns`` has the same meaning as ``COLUMNS`` as a class property and
``data`` is the result of previous case [#]_.

::

    def get_thin_pools(ns, verbose):
        for vg in lvm.get_tps(ns):
            extent_size = size2str(vg.ExtentSize, self.app.config.human_friendly)
            if verbose:
                total_space = size2str(vg.TotalManagedSpace,
                        self.app.config.human_friendly)
                yield (vg.ElementName, extent_size, total_space)
            else:
                yield (vg.ElementName, extent_size)

    class ThinPoolList(command.LmiLister):

        def execute(self, ns):
            """
            Implementation of 'thinpool list' command.
            """
            columns = ['ElementName', "ExtentSize"]
            if self.app.config.verbose:
                columns.extend(["Total space"])
            return (columns, get_thin_pools(ns, self.app.config.verbose))

Produces: ::

    $ lmi -H -h $HOST storage thinpool list
    ElementName ExtentSize
    tp1         4M
    $ # The same with increased verbosity
    $ lmi -v -H -h $HOST storage thinpool list
    ElementName ExtentSize Total space
    tp1         4M         1024M

.. seealso::
    API documentation on
    :py:class:`~lmi.scripts.common.command.lister.LmiLister`

.. _lmi_instance_lister:

``LmiInstanceLister``
~~~~~~~~~~~~~~~~~~~~~
Is a variant of ``LmiLister``. Instead of rows being tuples, here they are
instances of some CIM class. Instead of using ``COLUMNS`` property for
specifying columns labels, ``PROPERTIES`` is used for the same purpose here.
Its primary use is in specifying which properties of instances shall be
rendered in which column. This is described in detail in
:ref:`lmi_instance_lister_properties`.

The expected output of associated function is therefore: ::

    [instance1, instance2, ...]

Again, usage of generators is preferred.

.. seealso::
    API documentation on
    :py:class:`~lmi.scripts.common.command.lister.LmiInstanceLister`

.. _lmi_show_instance:

``LmiShowInstance``
~~~~~~~~~~~~~~~~~~~
Renders a single instance of some CIM class. It's rendered in a form of
two-column table, where the first column contains property names and
the second their corresponding values. Rendering is controlled in the same
way as for ``LmiInstanceLister`` (see :ref:`lmi_show_instance_properties`).

.. seealso::
    API documentation on
    :py:class:`~lmi.scripts.common.command.show.LmiShowInstance`

.. _command_multiplexers:

Command multiplexers
--------------------
Group a list of commands under one. They were introduced
:ref:`earlier <command_multiplexers_introduction>`. Their children
can be end-point commands as well as multiplexers. Thus arbitrary tall command
trees can be constructed - though not being very practical.

Multiplexer works like this

    1. it consumes one argument from command line
    2. selects one of its subcommands based on consumed argument
    3. passes the rest of arguments to selected subcommand and executes it
    4. returns the result to a caller

For example consider following list of arguments: ::

    storage raid create --name raid5 5 /dev/vdb /dev/vdc /dev/vdd

*LMI metacommand* consumes ``storage`` command multiplexer and passes the rest
to it: ::

    Storage().run(["raid", "create", "--name", "raid5",  "5", "/dev/vdb",
            "/dev/vdc", "/dev/vdd"])

``Storage``, which can be defined like this: ::

    Storage = command.register_subcommands(
            'storage', __doc__,
            { 'tree'     : Tree,
              'partition': lmi.scripts.storage.cmd.partition.Partition,
              'fs'       : lmi.scripts.storage.cmd.fs.FS,
              'raid'     : lmi.scripts.storage.cmd.raid.Raid,
            },
        )

, consumes the first argument and passes the rest to the ``raid`` command which
is again a multiplexer defined like this: ::

    class Raid(command.LmiCommandMultiplexer):
        OWN_USAGE = __doc__
        COMMANDS = {
                'list'    : RaidList,
                'create'  : RaidCreate,
                'delete'  : RaidDelete,
                'show'    : RaidShow,
        }

``create`` end-point command will then be invoked with: ::

    ["--name", "raid5",  "5", "/dev/vdb", "/dev/vdc", "/dev/vdd"]

.. note::
    Each above multiplexer is defined in its own module with usage string at
    its top. It is far more legible than having couple of multiplexers sharing
    single module.

Splitting usage string
~~~~~~~~~~~~~~~~~~~~~~
Multiplexers delegating work to children multiplexers, like in the example above,
need to be given a special usage string.

Every multiplexer subcommand in the usage string must be followed with: ::

    <cmd> [<args> ...]

Like in the usage of ``Storage`` above: ::

    """
    Basic storage device information.

    Usage:
        %(cmd)s tree [ <device> ]
        %(cmd)s partition <cmd> [<args> ...]
        %(cmd)s fs <cmd> [<args> ...]
        %(cmd)s raid <cmd> [<args> ...]
    """

``cmd`` and ``args`` may be renamed to your liking. Only the form matters.
It ensures that anything after the ``cmd`` won't be inspected by this
multiplexer -- the work is delegated to the children.

As you can see, end-point and multiplexer commands may be freely mixed. The
``tree`` end-point command does not have its own usage string because all its
arguments are parsed by ``Storage``.

-------------------------------------------------------------------------------

.. seealso::

    General and class specific properties in :ref:`command_properties`.

-------------------------------------------------------------------------------

.. [#] Having the same length as each row in returned data.
.. [#] Generator or a ``list`` of rows.

.. ****************************************************************************

.. _CIM:            http://dmtf.org/standards/cim
.. _OpenLMI:        http://fedorahosted.org/openlmi/
.. _openlmi-tools:  http://fedorahosted.org/openlmi/wiki/shell
.. _docopt:         http://docopt.org/

