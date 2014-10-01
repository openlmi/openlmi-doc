Caveats
=======

There are some specifics when working with journald and OpenLMI journald
provider.

.. _inst-enum-limit:

Number of LMI_JournalLogRecord instances enumerated limitation
--------------------------------------------------------------

Testing the provider showed up an issue with enumeration of :ref:`LMI_JournalLogRecord<LMI-JournalLogRecord>`
instances. On the testing machine there was 199583 journal records, which is
simply too much for the CIMOM, exceeding memory and the resulting XML reply
limits.

An artificial limit has been set, currently to 1000 most recent records. This
limit is defined by the ``JOURNAL_MAX_INSTANCES_NUM`` define in ``Journal.h``
source file. Please use iterators instead to get access to all records.


Iteration and iterators
-----------------------

Iteration is a different way of getting data through the log records. Comparing
to the usual instance enumeration, this is a sequential-like access with ability
to seek back and forth in the journal. Retrieving individual records might be
slower than direct random access though memory consumption is kept on a low
level.

Please check the :ref:`LMI_JournalMessageLog<LMI-JournalMessageLog>` class
reference for detailed description of available iterator-related methods.
Implemented iterator methods are :ref:`PositionToFirstRecord()<LMI-JournalMessageLog-PositionToFirstRecord>`,
:ref:`PositionAtRecord()<LMI-JournalMessageLog-PositionAtRecord>`,
:ref:`GetRecord()<LMI-JournalMessageLog-GetRecord>` and
:ref:`CancelIteration()<LMI-JournalMessageLog-CancelIteration>`. Only relative movement
is supported by the :ref:`PositionAtRecord()<LMI-JournalMessageLog-PositionAtRecord>` method.

A key element of the iteration process is the iteration identifier that is
typically passed in the methods listed above. Only the :ref:`PositionToFirstRecord()<LMI-JournalMessageLog-PositionToFirstRecord>`
method is able to create new iteration identifier without the need of specifying
one.

Iteration identifiers are specific to the provider and are opaque. They're are
persistent to some extent, surviving unexpected CIMOM runtime cleanup. The only
requirement for persistency to work is the journal record the iterator identifier
previously pointed to to be available at the time the iterator is reused.
I.e. it won't survive log rotation.

A remark for the :ref:`LMI_JournalMessageLog.GetRecord()<LMI-JournalMessageLog-GetRecord>`
method: the outgoing RecordData argument carries string data encoded in an array
of uint8 elements as defined by the model. This is quite limiting and also still
very free-form on the other hand. To conform the definition, we put UTF-8 encoded
string split by characters in the array and is up to clients to decode it back
to a readable form.


New log records writing security concerns
-----------------------------------------

The provider has an ability to send new messages to the log. This may be percieved
as a security issue in someone's eyes as long as you can specify custom message
format that is sent to the log. The only obstacle preventing anyone in sending
spoof messages is the rather weak CIM authentication model.

However, as long as journald is a structured logging system, further information
is stored along every log record. Messages sent through the OpenLMI Journald
provider may be identified by supplemental fields such as ``_COMM`` and ``_EXE``,
pointing to a CIMOM that had been running the provider code or even the ``CODE_FUNC``
field, pointing to a specific function that invoked the journald library code.


Potential indications endless loop
----------------------------------

Just a note for implementing a system processing the indications. Having no
specific filter for the indication subscription and performing an action
within the indication handler that involves a message being sent to syslog
may result in an endless loop as long such action generates another indication
for the fresh syslog message. Even a CIMOM in certain situations (i.e. debugging
in verbose mode) may generate additional messages while sending an indication
that in turn will generate another one.
