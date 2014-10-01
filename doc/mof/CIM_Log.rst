.. _CIM-Log:

CIM_Log
-------

Class reference
===============
Subclass of :ref:`CIM_EnabledLogicalElement <CIM-EnabledLogicalElement>`

Log represents any type of event, error or informational register or chronicle. The object describes the existence of the log and its characteristics. Log does not dictate the form of the data represented or how records/messages are stored in the log and/or accessed. Subclasses will define the appropriate methods and behavior.


Key properties
^^^^^^^^^^^^^^


Local properties
^^^^^^^^^^^^^^^^

.. _CIM-Log-MaxNumberOfRecords:

``uint64`` **MaxNumberOfRecords**

    Maximum number of records that can be captured in the Log. If undefined, a value of zero should be specified.

    
.. _CIM-Log-CurrentNumberOfRecords:

``uint64`` **CurrentNumberOfRecords**

    Current number of records in the Log.

    
.. _CIM-Log-LogState:

``uint16`` **LogState**

    LogState is an integer enumeration that indicates the current state of a log represented by CIM_Log subclasses. LogState is to be used in conjunction with the EnabledState property to fully describe the current state of the log. The following text briefly summarizes the various log states: 

    Unknown (0) indicates the state of the log is unknown. 

    Normal (2) indicates that the log is or could be executing logging commands, will process any queued log entries, and will queue new logging requests. 

    Erasing (3) indicates that the log is being erased. 

    Not Applicable (4) indicates the log does not support representing a log state.

    
    ============ ===============
    ValueMap     Values         
    ============ ===============
    0            Unknown        
    2            Normal         
    3            Erasing        
    4            Not Applicable 
    ..           DMTF Reserved  
    32768..65535 Vendor Reserved
    ============ ===============
    
.. _CIM-Log-OverwritePolicy:

``uint16`` **OverwritePolicy**

    OverwritePolicy is an integer enumeration that indicates whether the log, represented by the CIM_Log subclasses, can overwrite its entries.Unknown (0) indicates the log's overwrite policy is unknown. 

    Wraps when Full (2) indicates that the log overwrites its entries with new entries when the log has reached its maximum capacity. 

    Never Overwrites (7) indicates that the log never overwrites its entries by the new entries.

    Archives (8) indicates that the logging is never interupted, and the log archives old entries using an algorithm such as reaching a specific threshold on number of entries to archive a specific number of old ones to free space for new entries. The archived entries may not be readily retreived through the enumeration of log entries.

    
    ============ ================
    ValueMap     Values          
    ============ ================
    0            Unknown         
    2            Wraps When Full 
    7            Never Overwrites
    8            Archives        
    ..           DMTF Reserved   
    32768..65535 Vendor Reserved 
    ============ ================
    

Local methods
^^^^^^^^^^^^^

    .. _CIM-Log-ClearLog:

``uint32`` **ClearLog** ()

    Requests that the Log be cleared of all entries. 

    The return value should be 0 if the request was successfully executed, 1 if the request is not supported, and some other value, as indicated by the ValueMap/Values qualifiers, if an error occurred.

    
    ============== =======================
    ValueMap       Values                 
    ============== =======================
    0              Completed with no error
    1              Not Supported          
    2              Unspecified Error      
    3              Timeout                
    4              Failed                 
    5              Invalid Parameter      
    6..0x0FFF      DMTF_Reserved          
    0x1000..0x7FFF Method_Reserved        
    0x8000..       Vendor_Reserved        
    ============== =======================
    
    **Parameters**
    
*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`

