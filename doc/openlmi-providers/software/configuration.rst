Configuration
=============
This section documents additional configuration options of OpenLMI-Software
not covered by :ref:`common-configuration`.

.. note::
    All additional options listed here are specific to python implementation. C
    provider ignores them.

Apart from main configuration file ``/etc/openlmi/openlmi.conf``, all
software related settings are also read from ::

    /etc/openlmi/software/software.conf

They take precedence over the settings from main configuration file.

Options
-------
Follows a list of valid options with sections enclosed in square brackets.

*yum* options
~~~~~~~~~~~~~
Options related to the use of `yum`_ API and its configuration.

    ``[Yum] LockWaitInterval`` : defaults to 0.5
        Number of seconds to wait before next try to lock yum package database.
        This applies, when yum database is locked by another process.

    ``[Yum] FreeDatabaseTimeout = 60`` : defaults to 60
        Number of seconds to keep package cache in memory after the last use
        (caused by user request). Package cache takes up a lot of memory.

*Log* options
~~~~~~~~~~~~~

    ``[Yum] FileConfig`` : defaults to empty string
        This option overrides any other logging option. It provides complete
        control over what is logged, when and where. It's a path to a logging
        configuration file with format specified in `Configuration File Format
        <http://docs.python.org/2/library/logging.config.html#configuration-file-format>`_.
        Path can be absolute or relative. In the latter case it's relative to a
        directory of this configuration file.

*YumWorkerLog* options
~~~~~~~~~~~~~~~~~~~~~~
This section is targeted mostly on developers of OpenLMI-Software provider.
`yum`_ API is accessed exclusively from separated process called ``YumWorker``.
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

.. ****************************************************************************
.. _yum: http://yum.baseurl.org/
