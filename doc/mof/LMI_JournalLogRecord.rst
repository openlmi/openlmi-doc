.. _LMI-JournalLogRecord:

LMI_JournalLogRecord
--------------------

Class reference
===============
Subclass of :ref:`CIM_LogRecord <CIM-LogRecord>`

The LogRecord object can describe the definitional format for entries in a MessageLog, or can be used to instantiate the actual records in the Log. The latter approach provides a great deal more semantic definition and management control over the individual entries in a MessageLog, than do the record manipulation methods of the Log class. It is recommended that the data in individual Log entries be modeled using subclasses of LogRecord, to avoid the creation of LogRecords with one property (such as RecordData) without semantics. 

Definitional formats for LogRecords could be specified by establishing a naming convention for the RecordID and Message Timestamp key properties.


Key properties
^^^^^^^^^^^^^^

| :ref:`LogCreationClassName <CIM-LogRecord-LogCreationClassName>`
| :ref:`MessageTimestamp <CIM-LogRecord-MessageTimestamp>`
| :ref:`RecordID <CIM-LogRecord-RecordID>`
| :ref:`LogName <CIM-LogRecord-LogName>`
| :ref:`CreationClassName <CIM-LogRecord-CreationClassName>`
| :ref:`LogCreationClassName <CIM-LogRecord-LogCreationClassName>`
| :ref:`MessageTimestamp <CIM-LogRecord-MessageTimestamp>`
| :ref:`RecordID <CIM-LogRecord-RecordID>`
| :ref:`LogName <CIM-LogRecord-LogName>`
| :ref:`CreationClassName <CIM-LogRecord-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-JournalLogRecord-ProcessID:

``uint64`` **ProcessID**

    Denotes numerical ID of the process that sent the message.

    
.. _LMI-JournalLogRecord-UserID:

``uint64`` **UserID**

    Denotes numerical effective user ID of the process that sent the message. This ID is system specific and usually maps to a local POSIX account.

    
.. _LMI-JournalLogRecord-SystemdUnit:

``string`` **SystemdUnit**

    The systemd unit name, not set when message has not been logged natively through journald (i.e. through syslog transport).

    
.. _LMI-JournalLogRecord-LogCreationClassName:

``string`` **LogCreationClassName**

    The scoping Log's CreationClassName.

    
.. _LMI-JournalLogRecord-MessageTimestamp:

``datetime`` **MessageTimestamp**

    A LogRecord's key structure includes a timestamp for the entry. If the timestamp for the entry is unknown, the value 99990101000000.000000+000 SHOULD be used.

    
.. _LMI-JournalLogRecord-SyslogSeverity:

``uint16`` **SyslogSeverity**

    A syslog severity level of the message, defined by RFC 5424.

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Emergency    
    1        Alert        
    2        Critical     
    3        Error        
    4        Warning      
    5        Notice       
    6        Informational
    7        Debug        
    ======== =============
    
.. _LMI-JournalLogRecord-HostName:

``string`` **HostName**

    Hostname of the system where the log record has been sent from.

    
.. _LMI-JournalLogRecord-GroupID:

``uint64`` **GroupID**

    Denotes numerical effective group ID of the process that sent the message. This ID is system specific and usually maps to a local POSIX account.

    
.. _LMI-JournalLogRecord-LogName:

``string`` **LogName**

    The scoping Log's Name.

    
.. _LMI-JournalLogRecord-SyslogIdentifier:

``string`` **SyslogIdentifier**

    A syslog identifier string, usually carrying process name that logged the message.

    
.. _LMI-JournalLogRecord-SyslogFacility:

``uint16`` **SyslogFacility**

    A syslog facility level specifying what type of program is logging the message. Values are defined by RFC 3164.

    
    ======== ========
    ValueMap Values  
    ======== ========
    0        kern    
    1        user    
    2        mail    
    3        daemon  
    4        auth    
    5        syslog  
    6        lpr     
    7        news    
    8        uucp    
    9        clock   
    10       authpriv
    11       ftp     
    12       ntp     
    13       audit   
    14       alert   
    15       cron    
    16       local0  
    17       local1  
    18       local2  
    19       local3  
    20       local4  
    21       local5  
    22       local6  
    23       local7  
    ======== ========
    
.. _LMI-JournalLogRecord-DataFormat:

``string`` **DataFormat**

    **Deprecated!** 
    A free-form string describing the LogRecord's data structure.

    
.. _LMI-JournalLogRecord-PerceivedSeverity:

``uint16`` **PerceivedSeverity**

    An enumerated value that describes the severity of the Indication from the notifier's point of view: 

    1 - Other, by CIM convention, is used to indicate that the Severity's value can be found in the OtherSeverity property. 

    3 - Degraded/Warning should be used when its appropriate to let the user decide if action is needed. 

    4 - Minor should be used to indicate action is needed, but the situation is not serious at this time. 

    5 - Major should be used to indicate action is needed NOW. 

    6 - Critical should be used to indicate action is needed NOW and the scope is broad (perhaps an imminent outage to a critical resource will result). 

    7 - Fatal/NonRecoverable should be used to indicate an error occurred, but it's too late to take remedial action. 

    2 and 0 - Information and Unknown (respectively) follow common usage. Literally, the Indication is purely informational or its severity is simply unknown.

    
    ======== ====================
    ValueMap Values              
    ======== ====================
    0        Unknown             
    1        Other               
    2        Information         
    3        Degraded/Warning    
    4        Minor               
    5        Major               
    6        Critical            
    7        Fatal/NonRecoverable
    ======== ====================
    
.. _LMI-JournalLogRecord-RecordID:

``string`` **RecordID**

    RecordID, with the MessageTimestamp property, serve to uniquely identify the LogRecord within a MessageLog. Note that this property is different than the RecordNumber parameters of the MessageLog methods. The latter are ordinal values only, useful to track position when iterating through a Log. On the other hand, RecordID is truly an identifier for an instance of LogRecord. It may be set to the record's ordinal position, but this is not required.

    
.. _LMI-JournalLogRecord-CreationClassName:

``string`` **CreationClassName**

    CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`RecordFormat <CIM-RecordForLog-RecordFormat>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`RecordData <CIM-RecordForLog-RecordData>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`Locale <CIM-RecordForLog-Locale>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

