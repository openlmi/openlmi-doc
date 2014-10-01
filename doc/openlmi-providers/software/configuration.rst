Configuration
=============
There are various options affecting behaviour of *OpenLMI Software* provider.
All of them can be fine-tuned using two configuration files. The main one is
located at: ::

    /etc/openlmi/software/software.conf

The other one is a global configuration file for all providers in *OpenLMI*
project and serves as a fallback, for options not specified in the main one.
It's located in: ::

    /etc/openlmi/openlmi.conf

Since this is a common setup for all *OpenLMI* providers, administator can
specify options common to all in the global configuration file, while the
values specific for particular provider can be overriden in its main one
(``/etc/openlmi/${provider}/${provider}.conf``).

..
    TODO: once we have a stable hosting for all OpenLMI documetation, let's
    just point to top-level Configuration page.

Treating boolean values
-----------------------
Options expecting boolean values treat following strings as valid ``True``
values:

    * ``True``
    * ``1``
    * ``yes``
    * ``on``

While the following are considered ``False``:

    * ``0``
    * ``no``
    * ``False``
    * ``off``

These words are checked in a case-insensitive way. Any other value isn't
considered valid [1]_.

Options
-------
Follows a list of valid options with sections enclosed in square brackets.

*CIM* options
~~~~~~~~~~~~~

    ``[CIM] Namespace`` : defaults to ``root/cimv2``
        Is a *CIM* namespace, where *CIM* classes of this provider are
        registered.

    ``[CIM] SystemClassName`` : defaults to ``PG_ComputerSystem``
        Sets the class name used to refer to computer system. Different cimmoms
        can instrument variously named computer systems and some may not
        instrument any at all. `Sfcb`_ is an example of the later, it needs the
        ``sblim-cmpi-base`` package installed providing the basic set of
        providers containing ``Linux_ComputerSystem``. So in case you run a
        ``Sfcb`` or you preferr to use providers from ``sblim-cmpi-base``
        package, you need to change this to ``Linux_ComputerSystem``.

*YUM* options
~~~~~~~~~~~~~
Options related to the use of *YUM* API and its configuration.

    ``[Yum] LockWaitInterval`` : defaults to 0.5
        Number of seconds to wait before next try to lock yum package database.
        This applies, when yum database is locked by another process.

    ``[Yum] FreeDatabaseTimeout = 60`` : defaults to 60
        Number of seconds to keep package cache in memory after the last use
        (caused by user request). Package cache takes up a lot of memory.

*Log* options
~~~~~~~~~~~~~

    ``[Yum] Level`` : defaults to ``ERROR``
        Can be set to one of the following:

            * ``CRITICAL``
            * ``ERROR``
            * ``WARNING``
            * ``INFO``
            * ``DEBUG``
            * ``TRACE_WARNING``
            * ``TRACE_INFO``
            * ``TRACE_VERBOSE``

        It specifies the minimum severity of messages that shall be logged.
        Messages having ``DEBUG`` or more severe level are sent to *CIMOM*
        using standard function ``CMLogMessage()``. Tracing messages (whose
        level names start with ``TRACE_`` use the ``CMTraceMessage()`` instead.

        Please consult the documentation of your *CIMOM* to see, how these
        messages can be treated and logged to different facilities.

        .. note::
            This does not have any effect if the ``[Log] FileConfig`` option is
            set.

    ``[Yum] Stderr`` : defaults to ``False``
        Whether to enable logging to standard error output. This does not
        affect logging to *CIMOM* which stays enabled independently of this
        option.

        This is mostly usefull when debugging with *CIMOM* running on
        foreground.

        .. note::
            This does not have any effect if the ``[Log] FileConfig`` option is
            set.

        .. seealso::
            Since this accepts boolean values, refer to
            `Treating boolean values`_ for details.

    ``[Yum] FileConfig`` : defaults to empty string
        This option overrides any other logging option. It provides complete
        control over what is logged, when and where. It's a path to a logging
        configuration file with format specified in:
        http://docs.python.org/2/library/logging.config.html#configuration-file-format
        Path can be absolute or relative. In the latter case it's relative to
        a directory of this configuration file.

*YumWorkerLog* options
~~~~~~~~~~~~~~~~~~~~~~
This section is targeted mostly on developpers of *OpenLMI Software* provider.
*YUM* API is accessed exclusively from separated process called ``YumWorker``.
Because separated process can not send its log messages to *CIMOM*, its
logging configuration needs to be configured extra.

    ``[YumWorkerLog] OutputFile`` : defaults to empty string
        This is an absolute or relative path to a file, where the logging
        will be done. Without this option set, logging of ``YumWorker`` is
        disabled (assuming the ``[YumWorkerLog] FileConfig`` option is also
        unset).

    ``[YumWorkerLog] Level`` : defaults to ``DEBUG``
        This has generally the same meaning as ``Level`` in previous section
        (`Log options`_). Except this affects only logging of ``YumWorker``
        process.

    ``[YumWorkerLog] FileConfig`` : defaults to empty string
        Similar to the ``FileConfig`` option in `Log options`_. This overrides
        any other option in this section.

-------------------------------------------------------------------------------

.. [1] Default value will be used as a fallback. This applies also to other
       non-boolean options in case of invalid value.

.. ****************************************************************************
.. _Sfcb: http://sourceforge.net/apps/mediawiki/sblim/index.php?title=Sfcb
