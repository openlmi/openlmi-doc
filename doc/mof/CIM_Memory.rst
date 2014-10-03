.. _CIM-Memory:

CIM_Memory
----------

Class reference
===============
Subclass of :ref:`CIM_StorageExtent <CIM-StorageExtent>`

Capabilities and management of Memory-related LogicalDevices.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-Memory-ErrorResolution:

``uint64`` **ErrorResolution**

    Specifies the range, in bytes, to which the last error can be resolved. For example, if error addresses are resolved to bit 11 (ie, on a typical page basis), then errors can be resolved to 4K boundaries and this property is set to 4000. If the ErrorInfo property is equal to 3, "OK", then this property has no meaning.

    
.. _CIM-Memory-ErrorAccess:

``uint16`` **ErrorAccess**

    **Deprecated!** 
    An integer enumeration indicating the memory access operation that caused the last error. The type of error is described by the ErrorInfo property. If the ErrorInfo property is equal to 3, "OK", then this property has no meaning.

    
    ======== =============
    ValueMap Values       
    ======== =============
    1        Other        
    2        Unknown      
    3        Read         
    4        Write        
    5        Partial Write
    ======== =============
    
.. _CIM-Memory-Volatile:

``boolean`` **Volatile**

    Volatile is a property that indicates whether this memory is volatile or not.

    
.. _CIM-Memory-CorrectableError:

``boolean`` **CorrectableError**

    **Deprecated!** 
    Boolean indicating that the most recent error was correctable. If the ErrorInfo property is equal to 3, "OK", then this property has no meaning.

    
.. _CIM-Memory-AdditionalErrorData:

``uint8[]`` **AdditionalErrorData**

    **Deprecated!** 
    An array of octets holding additional error information. An example is ECC Syndrome or the return of the check bits if a CRC-based ErrorMethodology is used. In the latter case, if a single bit error is recognized and the CRC algorithm is known, it is possible to determine the exact bit that failed. This type of data (ECC Syndrome, Check Bit or Parity Bit data, or other vendor supplied information) is included in this field. If the ErrorInfo property is equal to 3, "OK", then AdditionalErrorData has no meaning.

    
.. _CIM-Memory-SystemLevelAddress:

``boolean`` **SystemLevelAddress**

    **Deprecated!** 
    Boolean indicating whether the address information in the property, ErrorAddress, is a system-level address (TRUE) or a physical address (FALSE). If the ErrorInfo property is equal to 3, "OK", then this property has no meaning.

    
.. _CIM-Memory-ErrorDataOrder:

``uint16`` **ErrorDataOrder**

    **Deprecated!** 
    The ordering for data stored in the ErrorData property. "Least Significant Byte First" (value=1) or "Most Significant Byte First" (2) can be specified. If ErrorTransferSize is 0, then this property has no meaning.

    
    ======== ============================
    ValueMap Values                      
    ======== ============================
    0        Unknown                     
    1        Least Significant Byte First
    2        Most Significant Byte First 
    ======== ============================
    
.. _CIM-Memory-ErrorTransferSize:

``uint32`` **ErrorTransferSize**

    The size of the data transfer in bits that caused the last error. 0 indicates no error. If the ErrorInfo property is equal to 3, "OK", then this property should be set to 0.

    
.. _CIM-Memory-ErrorAddress:

``uint64`` **ErrorAddress**

    **Deprecated!** 
    Specifies the address of the last memory error. The type of error is described by the ErrorInfo property. If the ErrorInfo property is equal to 3, "OK", then this property has no meaning.

    
.. _CIM-Memory-ErrorData:

``uint8[]`` **ErrorData**

    Data captured during the last erroneous mebmory access. The data occupies the first n octets of the array necessary to hold the number of bits specified by the ErrorTransferSize property. If ErrorTransferSize is 0, then this property has no meaning.

    
.. _CIM-Memory-EndingAddress:

``uint64`` **EndingAddress**

    The ending address, referenced by an application or operating system and mapped by a memory controller, for this Memory object. The ending address is specified in KBytes.

    
.. _CIM-Memory-OtherErrorDescription:

``string`` **OtherErrorDescription**

    **Deprecated!** 
    Free form string providing more information if the Error Type property is set to 1, "Other". If not set to 1, this string has no meaning.

    
.. _CIM-Memory-ErrorInfo:

``uint16`` **ErrorInfo**

    **Deprecated!** 
    An integer enumeration describing the type of error that occurred most recently. For example, single (value=6) or double bit errors (7) can be specified using this property. The values, 12-14, are undefined in the CIM Schema since in DMI, they mix the semantics of the type of error and whether it was correctable or not. The latter is indicated in the property, CorrectableError.

    
    ======== ================
    ValueMap Values          
    ======== ================
    1        Other           
    2        Unknown         
    3        OK              
    4        Bad Read        
    5        Parity Error    
    6        Single-Bit Error
    7        Double-Bit Error
    8        Multi-Bit Error 
    9        Nibble Error    
    10       Checksum Error  
    11       CRC Error       
    12       Undefined       
    13       Undefined       
    14       Undefined       
    ======== ================
    
.. _CIM-Memory-ErrorTime:

``datetime`` **ErrorTime**

    The time that the last memory error occurred. The type of error is described by the ErrorInfo property. If the Error Info property is equal to 3, "OK", then this property has no meaning.

    
.. _CIM-Memory-ErrorMethodology:

``string`` **ErrorMethodology**

    ErrorMethodology for Memory is a string property that indicates whether parity or CRC algorithms, ECC or other mechanisms are used. Details on the algorithm can also be supplied.

    
.. _CIM-Memory-StartingAddress:

``uint64`` **StartingAddress**

    The beginning address, referenced by an application or operating system and mapped by a memory controller, for this Memory object. The starting address is specified in KBytes.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint8`` :ref:`DeltaReservation <CIM-StorageExtent-DeltaReservation>`
| ``boolean`` :ref:`IsBasedOnUnderlyingRedundancy <CIM-StorageExtent-IsBasedOnUnderlyingRedundancy>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``uint16[]`` :ref:`ClientSettableUsage <CIM-StorageExtent-ClientSettableUsage>`
| ``string`` :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| ``uint16`` :ref:`DataOrganization <CIM-StorageExtent-DataOrganization>`
| ``uint16`` :ref:`Access <CIM-StorageExtent-Access>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``boolean`` :ref:`Primordial <CIM-StorageExtent-Primordial>`
| ``boolean`` :ref:`ErrorCleared <CIM-LogicalDevice-ErrorCleared>`
| ``boolean`` :ref:`NoSinglePointOfFailure <CIM-StorageExtent-NoSinglePointOfFailure>`
| ``uint16`` :ref:`Usage <CIM-StorageExtent-Usage>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`DataRedundancy <CIM-StorageExtent-DataRedundancy>`
| ``string`` :ref:`Name <CIM-StorageExtent-Name>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string`` :ref:`OtherNameNamespace <CIM-StorageExtent-OtherNameNamespace>`
| ``uint16`` :ref:`CompressionRate <CIM-StorageExtent-CompressionRate>`
| ``string[]`` :ref:`IdentifyingDescriptions <CIM-LogicalDevice-IdentifyingDescriptions>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`OtherNameFormat <CIM-StorageExtent-OtherNameFormat>`
| ``uint16`` :ref:`NameFormat <CIM-StorageExtent-NameFormat>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``string`` :ref:`Purpose <CIM-StorageExtent-Purpose>`
| ``uint64`` :ref:`ExtentStripeLength <CIM-StorageExtent-ExtentStripeLength>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16`` :ref:`LocationIndicator <CIM-LogicalDevice-LocationIndicator>`
| ``uint16`` :ref:`CompressionState <CIM-StorageExtent-CompressionState>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string[]`` :ref:`OtherIdentifyingInfo <CIM-LogicalDevice-OtherIdentifyingInfo>`
| ``boolean`` :ref:`IsCompressed <CIM-StorageExtent-IsCompressed>`
| ``uint64`` :ref:`ExtentInterleaveDepth <CIM-StorageExtent-ExtentInterleaveDepth>`
| ``uint16[]`` :ref:`PowerManagementCapabilities <CIM-LogicalDevice-PowerManagementCapabilities>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint64`` :ref:`BlockSize <CIM-StorageExtent-BlockSize>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``boolean`` :ref:`SequentialAccess <CIM-StorageExtent-SequentialAccess>`
| ``uint16[]`` :ref:`AdditionalAvailability <CIM-LogicalDevice-AdditionalAvailability>`
| ``string`` :ref:`OtherUsageDescription <CIM-StorageExtent-OtherUsageDescription>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``boolean`` :ref:`IsComposite <CIM-StorageExtent-IsComposite>`
| ``uint16`` :ref:`StatusInfo <CIM-LogicalDevice-StatusInfo>`
| ``string`` :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| ``string[]`` :ref:`ExtentDiscriminator <CIM-StorageExtent-ExtentDiscriminator>`
| ``uint16`` :ref:`PackageRedundancy <CIM-StorageExtent-PackageRedundancy>`
| ``uint64`` :ref:`PowerOnHours <CIM-LogicalDevice-PowerOnHours>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`NumberOfBlocks <CIM-StorageExtent-NumberOfBlocks>`
| ``uint64`` :ref:`MaxQuiesceTime <CIM-LogicalDevice-MaxQuiesceTime>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint64`` :ref:`TotalPowerOnHours <CIM-LogicalDevice-TotalPowerOnHours>`
| ``string`` :ref:`ErrorDescription <CIM-LogicalDevice-ErrorDescription>`
| ``uint16`` :ref:`NameNamespace <CIM-StorageExtent-NameNamespace>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``boolean`` :ref:`IsConcatenated <CIM-StorageExtent-IsConcatenated>`
| ``uint32`` :ref:`LastErrorCode <CIM-LogicalDevice-LastErrorCode>`
| ``string`` :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| ``uint16[]`` :ref:`ExtentStatus <CIM-StorageExtent-ExtentStatus>`
| ``uint16`` :ref:`Availability <CIM-LogicalDevice-Availability>`
| ``string`` :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`
| ``uint64`` :ref:`ConsumableBlocks <CIM-StorageExtent-ConsumableBlocks>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`Reset <CIM-LogicalDevice-Reset>`
| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`
| :ref:`SetPowerState <CIM-LogicalDevice-SetPowerState>`
| :ref:`QuiesceDevice <CIM-LogicalDevice-QuiesceDevice>`
| :ref:`EnableDevice <CIM-LogicalDevice-EnableDevice>`
| :ref:`OnlineDevice <CIM-LogicalDevice-OnlineDevice>`
| :ref:`SaveProperties <CIM-LogicalDevice-SaveProperties>`
| :ref:`RestoreProperties <CIM-LogicalDevice-RestoreProperties>`

