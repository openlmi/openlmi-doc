.. _CIM-LogRecord:

CIM_LogRecord
-------------

Class reference
===============
Subclass of :ref:`CIM_RecordForLog <CIM-RecordForLog>`

The LogRecord object can describe the definitional format for entries in a MessageLog, or can be used to instantiate the actual records in the Log. The latter approach provides a great deal more semantic definition and management control over the individual entries in a MessageLog, than do the record manipulation methods of the Log class. It is recommended that the data in individual Log entries be modeled using subclasses of LogRecord, to avoid the creation of LogRecords with one property (such as RecordData) without semantics. 

Definitional formats for LogRecords could be specified by establishing a naming convention for the RecordID and Message Timestamp key properties.


Key properties
^^^^^^^^^^^^^^

| :ref:`LogCreationClassName <CIM-LogRecord-LogCreationClassName>`
| :ref:`MessageTimestamp <CIM-LogRecord-MessageTimestamp>`
| :ref:`RecordID <CIM-LogRecord-RecordID>`
| :ref:`LogName <CIM-LogRecord-LogName>`
| :ref:`CreationClassName <CIM-LogRecord-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-LogRecord-LogCreationClassName:

``string`` **LogCreationClassName**

    The scoping Log's CreationClassName.

    
.. _CIM-LogRecord-MessageTimestamp:

``datetime`` **MessageTimestamp**

    A LogRecord's key structure includes a timestamp for the entry. If the timestamp for the entry is unknown, the value 99990101000000.000000+000 SHOULD be used.

    
.. _CIM-LogRecord-RecordID:

``string`` **RecordID**

    RecordID, with the MessageTimestamp property, serve to uniquely identify the LogRecord within a MessageLog. Note that this property is different than the RecordNumber parameters of the MessageLog methods. The latter are ordinal values only, useful to track position when iterating through a Log. On the other hand, RecordID is truly an identifier for an instance of LogRecord. It may be set to the record's ordinal position, but this is not required.

    
.. _CIM-LogRecord-DataFormat:

``string`` **DataFormat**

    **Deprecated!** 
    A free-form string describing the LogRecord's data structure.

    
.. _CIM-LogRecord-LogName:

``string`` **LogName**

    The scoping Log's Name.

    
.. _CIM-LogRecord-CreationClassName:

``string`` **CreationClassName**

    CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`RecordFormat <CIM-RecordForLog-RecordFormat>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Locale <CIM-RecordForLog-Locale>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`PerceivedSeverity <CIM-RecordForLog-PerceivedSeverity>`
| ``string`` :ref:`RecordData <CIM-RecordForLog-RecordData>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

