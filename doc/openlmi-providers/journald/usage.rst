Usage
=====

The OpenLMI Journald provider depends on running journald daemon. See the `systemd
<http://www.freedesktop.org/software/systemd/man/systemd-journald.service.html>`_
manual for how to enable the journald service.


Listing a log
-------------

This example shows simple enumeration through available :ref:`LMI_JournalLogRecord<LMI-JournalLogRecord>`
instances in classic syslog-like format:

::

    #!/usr/bin/lmishell
    c = connect("localhost", "pegasus", "test")
    for rec in c.root.cimv2.LMI_JournalMessageLog.first_instance().associators():
        print "%s %s %s" % (rec.MessageTimestamp.datetime.ctime(), rec.HostName, rec.DataFormat)

.. note::
   Only a limited number of records are being enumerated and printed out, please
   see the :ref:`inst-enum-limit` remark.


Using WQL query for simple filtering
------------------------------------

From its nature LMIShell can only do simple filtering by matching exact property
values. However there's a posibility of constructing custom CQL or WQL queries
bringing more flexibility in specific test conditions. The result from the query
method call is a list of instances, similar to calling ``".associators()"`` or
``".instances()"``.

The following example uses WQL query to get a list of messages with syslog
severity 3 (error) or higher:

::

    #!/usr/bin/lmishell
    c = connect("localhost", "pegasus", "test")
    for rec in c.root.cimv2.wql("SELECT * FROM LMI_JournalLogRecord WHERE SyslogSeverity <= 3"):
        print "[severity %d] %s" % (rec.SyslogSeverity, rec.DataFormat)


Iterating through the log
-------------------------

This example uses iterator methods of the :ref:`LMI_JournalMessageLog<LMI-JournalMessageLog>`
class to continuously go through the whole journal:

::

    #!/usr/bin/lmishell
    c = connect("localhost", "pegasus", "test")
    inst = c.root.cimv2.LMI_JournalMessageLog.first_instance()
    r = inst.PositionToFirstRecord()
    iter_id = r.rparams['IterationIdentifier']
    while True:
        x = inst.GetRecord(IterationIdentifier=iter_id, PositionToNext=True)
        if x.rval != 0:
            break
        print "".join(map(chr, x.rparams['RecordData']))
        iter_id = x.rparams['IterationIdentifier']


Sending new message to log
--------------------------

Simple example that uses :ref:`LMI_JournalLogRecord.create_instance()<LMI-JournalLogRecord>`
CIM method to send a new message in the log:

::

    #!/usr/bin/lmishell
    c = connect("localhost", "pegasus", "test")
    c.root.cimv2.LMI_JournalLogRecord.create_instance({"CreationClassName": "LMI_JournalLogRecord",
                                                       "LogCreationClassName": "LMI_JournalMessageLog",
                                                       "LogName": "Journal",
                                                       "DataFormat": ""})


Indications
-----------

The Journald provider comes with a
:ref:`LMI_JournalLogRecordInstanceCreationIndication<LMI-JournalLogRecordInstanceCreationIndication>`
class that can be used to receive indications when new log message is logged in
the journal. This way user is notified about system events.

Please see `LMIShell Indications API reference <http://pythonhosted.org/openlmi-tools/shell/indications.html>`_
for an overview how indications work.


Simple indication listener
~~~~~~~~~~~~~~~~~~~~~~~~~~

The following piece of code sets up a simple indication listener and waits for any new messages.
Press Ctrl+C to end the script.

::

    #!/usr/bin/lmishell
    
    from lmi.shell import LMIIndicationListener
    import socket
    import time
    import random
    
    def ind_handler(indication, **kwargs):
        print indication["SourceInstance"]["DataFormat"]
    
    
    c = connect("localhost", "pegasus", "test")
    
    indication_port = random.randint(12000, 13000)
    ind_filter = c.root.interop.CIM_IndicationFilter.first_instance(
                     {"Name": "LMI:LMI_JournalLogRecord:NewErrorMessage"})
    listener = LMIIndicationListener("0.0.0.0", indication_port)
    uniquename = listener.add_handler("journald_watch-XXXXXXXX", ind_handler)
    listener.start()
    
    c.subscribe_indication(
        Name=uniquename,
        Filter=ind_filter,
        Destination="http://%s:%d" % (socket.gethostname(), indication_port)
    )
    
    try:
        while True:
            time.sleep(1)
            pass
    except KeyboardInterrupt:
        pass
    
    c.unsubscribe_indication(uniquename)


The above script makes use of pre-defined indication filters. There are three
indication filters available by default:


New message event filter
~~~~~~~~~~~~~~~~~~~~~~~~

When used in indication subscription this will report all newly logged messages:

::

    SELECT * FROM LMI_JournalLogRecordInstanceCreationIndication WHERE
        SourceInstance ISA LMI_JournalLogRecord

Filter name ``"LMI:LMI_JournalLogRecord:NewMessage"``.


New error message event filter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This filter can be used to report all newly logged messages having syslog
severity value less than 4 ("Error"), meaning error messages including more
critical ones:

::

    SELECT * FROM LMI_JournalLogRecordInstanceCreationIndication WHERE
        SourceInstance ISA LMI_JournalLogRecord AND
        SourceInstance.LMI_JournalLogRecord::SyslogSeverity < 4

Filter name ``"LMI:LMI_JournalLogRecord:NewErrorMessage"``.


New critical message event filter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Similar to the last one except this omits error messages and only reports
critical, alert and emergency messages (see `RFC 5424 <http://tools.ietf.org/html/rfc5424>`_
for syslog severity mapping):

::

    SELECT * FROM LMI_JournalLogRecordInstanceCreationIndication WHERE
        SourceInstance ISA LMI_JournalLogRecord AND "
        SourceInstance.LMI_JournalLogRecord::SyslogSeverity < 3

Filter name ``"LMI:LMI_JournalLogRecord:NewCriticalMessage"``.


Custom event filters
~~~~~~~~~~~~~~~~~~~~

Apart from pre-defined indication filters the Journald provider supports custom
filters. This allows user to construct a very detailed filter to satisfy
specific needs. The following excerpt from the last example will make the
script to report any errors coming from the "sudo" command:

::

    c.subscribe_indication(
        Name=uniquename,
        Query="SELECT * FROM LMI_JournalLogRecordInstanceCreationIndication WHERE "
              "SourceInstance ISA LMI_JournalLogRecord AND "
              "SourceInstance.LMI_JournalLogRecord::SyslogSeverity < 4 AND "
              "SourceInstance.LMI_JournalLogRecord::SyslogIdentifier = 'sudo'",
        Destination="http://%s:%d" % (socket.gethostname(), indication_port)
    )
