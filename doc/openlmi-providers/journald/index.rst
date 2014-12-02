.. _openlmi-journald-provider:

Journald Provider
=================

.. rubric:: Overview

OpenLMI Journald is a CIM provider which manages
`systemd <http://freedesktop.org/wiki/Software/systemd/>`_
journald log records and basic means of iteration and log writing.
It exposes remotely accessible object-oriented API using
`WBEM <http://www.openlmi.org/node/1785>`_ set of protocols and technologies.

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

For the moment, global journal is used, all journal files are mixed together.

.. rubric:: Clients

The API can be accessed by any WBEM-capable client. OpenLMI already provides:

* Python module :ref:`lmi.scripts.journald <openlmi-scripts-journald-python>`,
  part of :ref:`OpenLMI scripts <openlmi-scripts-python>`.

* Command line tool: :ref:`LMI metacommand <lmi_metacommand>`, with
  :ref:`'journald' <openlmi-scripts-journald-cmd>` subcommand.

.. rubric:: Features

* Log records reading.
* Log record iteration using persistent iterators.
* New records indication.
* Writing new log records.

.. rubric:: Examples

Following :ref:`LMIShell <lmi_shell>` example prints last 1000 entries in the system log::

    c = connect("localhost", "pegasus", "mypassword")
    for rec in c.root.cimv2.LMI_JournalMessageLog.first_instance().associators():
        print "%s %s %s" % (rec.MessageTimestamp.datetime.ctime(), rec.HostName, rec.DataFormat)


More examples can be found in the :ref:`Usage <journald-usage>` chapter.

.. rubric:: Table of Contents

.. toctree::
   :maxdepth: 2

   caveats
   usage
