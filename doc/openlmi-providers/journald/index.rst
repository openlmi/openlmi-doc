.. _openlmi-journald-provider:

Journald Provider
=================

OpenLMI Journald is a CIM provider exposing `systemd <http://freedesktop.org/wiki/Software/systemd/>`_
journald log records and basic means of iteration and log writing.

Journald is a daemon working with journals. Journal is a log, a set of log
records, chronologically ordered. Records are structured, able to carry multiple
(custom) data fields. By implementation, journald is able to work with multiple
(separate) journals but we use the mixed way for the moment, which is typical
in production use.

Classes used by the provider were chosen to mimic the sblim-cmpi-syslog provider
set of classes allowing drop-in replacement in production tools. We haven't been
able to find a profile it conforms to though. There's a related DMTF profile
`DSP1010 "Record Log Profile" <http://www.dmtf.org/sites/default/files/standards/documents/DSP1010_2.0.0.pdf>`_
which may be subject to extension of this provider in the future.
As a benefit, by using the parent classes (e.g. :ref:`CIM_LogRecord<CIM-LogRecord>`), one is able
to mix log records from orthodox syslog and journald together.


*Provider features*

This is a short list of provider features:
 * log records reading
 * log record iteration using persistent iterators
 * new records indication
 * writing new log records

For the moment, global journal is used, all journal files are mixed together.

The provider also comes with a test suite covering most of its functionality.


*Contents*

.. toctree::
   :maxdepth: 2

   caveats
   usage
