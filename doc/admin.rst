Usage & Troubleshooting
=======================

Installation
------------

Fedora, Red Hat Enterprise Linux & derived Linux distributions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In Fedora Linux, one just needs to install OpenLMI packages:

.. code-block:: bash

    $ yum install openlmi-networking openlmi-storage <any other providers>



From source code
^^^^^^^^^^^^^^^^

Please refer to README of individual providers, either in git
or in released tarballs.


.. _common-configuration:

Configuration files
-------------------

``/etc/openlmi/openlmi.conf`` is OpenLMI master configuration file.

Each provider may introduce additional configuration files, see their
documentation. If a provider uses its own configuration file, the
provider-specific one is parsed first and all missing options are
then read from OpenLMI master configuration file.

Using this approach, administators can set e.g. one namespace for all
providers in ``/etc/openlmi/openlmi.conf`` and different log levels
for some providers in their configuration files.

File format
^^^^^^^^^^^
Configuration files has simple .ini syntax, with ``#`` or ``;`` used for
comments.

Default configuration:

.. code-block:: ini

     [CIM]
     Namespace=root/cimv2
     SystemClassName=PG_ComputerSystem

     [Log]
     Level=ERROR
     Stderr=false

+---------+---------------------+-----------------------+-------------------------------------------------------------------+
| Section | Option name         | Default value         | Description                                                       |
+=========+=====================+=======================+===================================================================+
| ``CIM`` | ``Namespace``       | ``root/cimv2``        | Namespace where OpenLMI providers are registered.                 |
+---------+---------------------+-----------------------+-------------------------------------------------------------------+
| ``CIM`` | ``SystemClassName`` | ``PG_ComputerSystem`` | Name of ``CIM_ComputerSystem`` class, which is used to represent  |
|         |                     |                       | the computer system. It will be used as ``SystemClassName``       |
|         |                     |                       | property value of various classes. Different cimmoms can          |
|         |                     |                       | instrument variously named computer systems and some may not      |
|         |                     |                       | instrument any at all. `Sfcb`_ is an example of the later, it     |
|         |                     |                       | needs the ``sblim-cmpi-base`` package installed providing the     |
|         |                     |                       | basic set of providers containing ``Linux_ComputerSystem``. So in |
|         |                     |                       | case you run a ``Sfcb`` or you preferr to use providers from      |
|         |                     |                       | ``sblim-cmpi-base`` package, you need to change this to           |
|         |                     |                       | ``Linux_ComputerSystem``.                                         |
+---------+---------------------+-----------------------+-------------------------------------------------------------------+
| ``Log`` | ``Level``           | ``ERROR``             | Chooses which messages are logged, either to CIMOM and (if        |
|         |                     |                       | configured) to standard error output. Available levels            |
|         |                     |                       | (sorted by severity) are:                                         |
|         |                     |                       |                                                                   |
|         |                     |                       |    * ``CRITICAL``                                                 |
|         |                     |                       |    * ``ERROR``                                                    |
|         |                     |                       |    * ``WARNING``                                                  |
|         |                     |                       |    * ``INFO``                                                     |
|         |                     |                       |    * ``DEBUG``                                                    |
|         |                     |                       |    * ``TRACE_WARNING``                                            |
|         |                     |                       |    * ``TRACE_INFO``                                               |
|         |                     |                       |    * ``TRACE_VERBOSE``                                            |
|         |                     |                       |                                                                   |
|         |                     |                       | Levels below ``INFO`` (= ``TRACE_WARNING``, ``TRACE_INFO``        |
|         |                     |                       | and ``DEBUG``) are useful mainly for debugging and bug            |
|         |                     |                       | reporting.                                                        |
+---------+---------------------+-----------------------+-------------------------------------------------------------------+
| ``Log`` | ``Stderr``          | ``False``             | Toggles sending of log messages to standard error output of the   |
|         |                     |                       | CIMOM. Accepts boolean value (see the next section).              |
+---------+---------------------+-----------------------+-------------------------------------------------------------------+

Treating boolean values
^^^^^^^^^^^^^^^^^^^^^^^
Options expecting boolean values treat following strings as valid *True*
values: ``true``, ``1``, ``yes`` and ``on``.
While the following are considered *False*: ``false``, ``0``, ``no`` and
``off``.
These words are checked in a case-insensitive way. Any other value isn't
considered valid [1]_.

Logging
-------

If logging is enabled, all log messages with level INFO and above are sent to
CIMOM using standard CMPI ``CMLogMessage`` function. Consult documentation of
your CIMOM how to enable output of these messages into CIMOM logs.

Messages with TRACE_WARNING and below are sent to CIMOM using ``CMTraceMessage``
and should be visible in CIMOM tracing log. Again, please consult your CIMOM
documentation how to enable tracing logs.

With ``Stderr`` configuration option enabled, all logs are sent both to CIMOM
and to the standard error output of the CIMOM.

Logging in Pegasus
^^^^^^^^^^^^^^^^^^

When using Pegasus CIMOM, the easiest way is to let Pegasus daemon run in
foreground and send log messages to its standard error output.

Sample ``/etc/openlmi/openlmi.conf``:

.. code-block:: ini

    [CIM]
    Namespace = root/cimv2
    SystemClassName = PG_ComputerSystem

    [Log]
    Level = TRACE_INFO
    Stderr = True

Run Pegasus in foreground, i.e. with ``stderr`` output sent to terminal:

.. code-block:: bash

    $ /sbin/cimserver daemon=false
    INFO:cimom_entry:get_providers:146 - Provider init.
    INFO:TimerManager:_timer_loop:246 - Started Timer thread.
    Level 8:cmpi_logging:trace_info:126 - Timer: Checking for expired, now=17634.607226.
    Level 8:cmpi_logging:trace_info:126 - Timer: No timers scheduled, waiting forever.
    INFO:cimom_entry:init_anaconda:118 - Initializing Anaconda
    INFO:JobManager:_worker_main:877 - Started Job thread.

Of course, more advanced logging can be configured in runtime to send provider
logs into trace files, see
`Pegasus documentation <http://cvs.opengroup.org/cgi-bin/viewcvs.cgi/*checkout*/pegasus/doc/TracingUserGuide.pdf>`_
for details.

.. note::

    OpenLMI providers will start logging only after they are started, i.e.
    when they are used for the first time. 

-------------------------------------------------------------------------------

.. [1] Default value will be used as a fallback. This applies also to other
       non-boolean options in case of invalid value.

.. ****************************************************************************

.. _Sfcb: http://sourceforge.net/apps/mediawiki/sblim/index.php?title=Sfcb

