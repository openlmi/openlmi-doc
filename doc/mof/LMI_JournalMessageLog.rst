.. _LMI-JournalMessageLog:

LMI_JournalMessageLog
---------------------

Class reference
===============
Subclass of :ref:`CIM_MessageLog <CIM-MessageLog>`

MessageLog represents any type of event, error or informational register or chronicle. The object describes the existence of the log and its characteristics. Several methods are defined for retrieving, writing and deleting log entries, and maintaining the log. This type of log uses iterators to access the log records, whereas its peer class, RecordLog, uses more abstracted access mechanisms.


Key properties
^^^^^^^^^^^^^^

| :ref:`CreationClassName <CIM-MessageLog-CreationClassName>`
| :ref:`Name <CIM-MessageLog-Name>`
| :ref:`Name <CIM-MessageLog-Name>`
| :ref:`CreationClassName <CIM-MessageLog-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-JournalMessageLog-Capabilities:

``uint16[]`` **Capabilities**

    An array of integers indicating the Log capabilities. Information such as "Write Record Supported" (value= 2) or "Variable Length Records Supported" (8) is specified in this property.

    
    ======== ============================================
    ValueMap Values                                      
    ======== ============================================
    0        Unknown                                     
    1        Other                                       
    2        Write Record Supported                      
    3        Delete Record Supported                     
    4        Can Move Backward in Log                    
    5        Freeze Log Supported                        
    6        Clear Log Supported                         
    7        Supports Addressing by Ordinal Record Number
    8        Variable Length Records Supported           
    9        Variable Formats for Records                
    10       Can Flag Records for Overwrite              
    ======== ============================================
    
.. _LMI-JournalMessageLog-TimeOfLastChange:

``datetime`` **TimeOfLastChange**

    When a change is made to the Log, the date/time of that modification is captured. This property could be used to event against any update to the MessageLog.

    
.. _LMI-JournalMessageLog-Name:

``string`` **Name**

    The inherited Name serves as part of the key (a unique identifier) for the MessageLog instance.

    
.. _LMI-JournalMessageLog-CreationClassName:

``string`` **CreationClassName**

    CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

    

Local methods
^^^^^^^^^^^^^

    .. _LMI-JournalMessageLog-PositionToLastRecord:

``uint32`` **PositionToLastRecord** (``string`` IterationIdentifier)

    Requests that an iteration of the MessageLog be established and that the iterator be set to the last entry in the Log. An identifier for the iterator is returned as an output parameter of the method. 

    

    The return value from PositionToFirstRecord is 0 if the request was successfully executed, 1 if the request is not supported and some other value if an error occurred.

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Success      
    1        Not supported
    2        Failed       
    ======== =============
    
    **Parameters**
    
        *OUT* ``string`` **IterationIdentifier**
            An identifier for the iterator.

            
        
    
    .. _LMI-JournalMessageLog-GetRecord:

``uint32`` **GetRecord** (``string`` IterationIdentifier, ``boolean`` PositionToNext, ``uint64`` RecordNumber, ``uint8[]`` RecordData)

    Requests that the record indicated by the IterationIdentifier be retrieved from the MessageLog. After retrieval, the IterationIdentifier may be advanced to the next record by setting the PositionToNext input parameter to TRUE. Two output parameters are defined for the method - RecordData which holds the contents of the Log entry (as an array of bytes that can be recast to an appropriate format), and RecordNumber which returns the current record number addressed via the Iteration Identifier. The RecordNumber parameter is only defined/valid when the Capabilities array indicates that ordinal record number addressing is supported (a value of 7). For LMI_JournalMessageLog, this stays unset.

    

    IterationIdentifier is defined as an Input/Output method parameter to allow the Log to embed state information in the Identifier and potentially let the identifier be maintained by the using application. 

    

    The return value from GetRecord is 0 if the request was successfully executed, 1 if the request is not supported, and some other value if an error occurred.

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Success      
    1        Not supported
    2        Failed       
    ======== =============
    
    **Parameters**
    
        *IN*, *OUT* ``string`` **IterationIdentifier**
            An identifier for the iterator.

            
        
        *IN* ``boolean`` **PositionToNext**
            Boolean indicating that the Iteration Identifier should be advanced to the next record, after retrieving the current Log entry.

            
        
        *OUT* ``uint64`` **RecordNumber**
            The record number, unused in LMI_JournalMessageLog.

            
        
        *OUT* ``uint8[]`` **RecordData**
            The record data. This array carries a UTF-8 encoded string in array of uint8 as defined by the model. Users are supposed to recast this free-form data to get a readable representation.

            
        
    
    .. _LMI-JournalMessageLog-CancelIteration:

``uint32`` **CancelIteration** (``string`` IterationIdentifier)

    Requests that an iteration of the Log, identified by the IterationIdentifier input parameter, be stopped. The return value from CancelIteration is 0 if the request was successfully executed, 1 if the request is not supported and some other value if an error occurred.

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Success      
    1        Not supported
    2        Failed       
    ======== =============
    
    **Parameters**
    
        *IN* ``string`` **IterationIdentifier**
            An identifier for the iterator.

            
        
    
    .. _LMI-JournalMessageLog-PositionAtRecord:

``uint32`` **PositionAtRecord** (``string`` IterationIdentifier, ``boolean`` MoveAbsolute, ``sint64`` RecordNumber)

    Requests that the Log's iteration identifier be advanced or retreated a specific number of records, or set to the entry at a specified numeric location. These two different behaviors are accomplished using the input parameters of the method. Advancing or retreating is achieved by setting the MoveAbsolute boolean to FALSE, and then specifying the number of entries to advance or retreat as positive or negative values in the RecordNumber parameter. Moving to a specific record number is accomplished by setting the MoveAbsolute input parameter to TRUE, and then placing the record number into the RecordNumber parameter. This can only be done if the Capabilities array includes a value of 7, "Supports Addressing by Ordinal Record Number". 

    

    After the method completes and if ordinal record numbers are supported (the Capabilities array includes a 7), the current record number is returned in the RecordNumber output parameter. Otherwise, the value of the parameter is undefined. 

    Note that only relative movement is supported in LMI_JournalMessageLog for the moment.

    

    IterationIdentifier is defined as an Input/Output method parameter to allow the Log to embed state information in the Identifier and potentially let the identifier be maintained by the using application. 

    

    The return value from PositionAtRecord is 0 if the request was successfully executed, 1 if the request is not supported and some other value if an error occurred. If the request is not supported, check the Capabilities array regarding support for ordinal record number addressing and backward movement in the Log (values 7 and 4, respectively).

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Success      
    1        Not supported
    2        Failed       
    ======== =============
    
    **Parameters**
    
        *IN*, *OUT* ``string`` **IterationIdentifier**
            An identifier for the iterator.

            
        
        *IN* ``boolean`` **MoveAbsolute**
            Advancing or retreating the IterationIdentifier is achieved by setting the MoveAbsolute boolean to FALSE, and specifying the number of entries to advance or retreat as positive or negative values in the RecordNumber parameter. Moving to a specific record number is accomplished by setting the MoveAbsolute parameter to TRUE, and placing the record number into the RecordNumber parameter.For LMI_JournalMessageLog, the only supported value is FALSE.

            
        
        *IN*, *OUT* ``sint64`` **RecordNumber**
            The relative or absolute record number.

            
        
    
    .. _LMI-JournalMessageLog-PositionToFirstRecord:

``uint32`` **PositionToFirstRecord** (``string`` IterationIdentifier)

    Requests that an iteration of the MessageLog be established and that the iterator be set to the first entry in the Log. An identifier for the iterator is returned as an output parameter of the method. 

    

    Regarding iteration, you have 2 choices: 1) Embed iteration data in the method call, and allow implementations to track/ store this data manually; or, 2) Iterate using a separate object (for example, class ActiveIterator) as an iteration agent. The first approach is used here for interoperability. The second requires an instance of the Iterator object for EACH iteration in progress. 2's functionality could be implemented underneath 1.

    

    The return value from PositionToFirstRecord is 0 if the request was successfully executed, 1 if the request is not supported and some other value if an error occurred.

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Success      
    1        Not supported
    2        Failed       
    ======== =============
    
    **Parameters**
    
        *OUT* ``string`` **IterationIdentifier**
            An identifier for the iterator.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string`` :ref:`RecordHeaderFormat <CIM-MessageLog-RecordHeaderFormat>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``uint64`` :ref:`MaxNumberOfRecords <CIM-Log-MaxNumberOfRecords>`
| ``uint8`` :ref:`PercentageNearFull <CIM-MessageLog-PercentageNearFull>`
| ``string`` :ref:`OtherPolicyDescription <CIM-MessageLog-OtherPolicyDescription>`
| ``uint16`` :ref:`LogState <CIM-Log-LogState>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``uint64`` :ref:`MaxRecordSize <CIM-MessageLog-MaxRecordSize>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint64`` :ref:`SizeOfHeader <CIM-MessageLog-SizeOfHeader>`
| ``string`` :ref:`HeaderFormat <CIM-MessageLog-HeaderFormat>`
| ``uint16`` :ref:`CharacterSet <CIM-MessageLog-CharacterSet>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint64`` :ref:`CurrentNumberOfRecords <CIM-Log-CurrentNumberOfRecords>`
| ``datetime`` :ref:`TimeWhenOutdated <CIM-MessageLog-TimeWhenOutdated>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``uint64`` :ref:`SizeOfRecordHeader <CIM-MessageLog-SizeOfRecordHeader>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``boolean`` :ref:`IsFrozen <CIM-MessageLog-IsFrozen>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint16`` :ref:`OverwritePolicy <CIM-MessageLog-OverwritePolicy>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint64`` :ref:`RecordLastChanged <CIM-MessageLog-RecordLastChanged>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16`` :ref:`LastChange <CIM-MessageLog-LastChange>`
| ``string[]`` :ref:`CapabilitiesDescriptions <CIM-MessageLog-CapabilitiesDescriptions>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint64`` :ref:`MaxLogSize <CIM-MessageLog-MaxLogSize>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`
| :ref:`DeleteRecord <CIM-MessageLog-DeleteRecord>`
| :ref:`ClearLog <CIM-Log-ClearLog>`
| :ref:`FreezeLog <CIM-MessageLog-FreezeLog>`
| :ref:`FlagRecordForOverwrite <CIM-MessageLog-FlagRecordForOverwrite>`
| :ref:`WriteRecord <CIM-MessageLog-WriteRecord>`

