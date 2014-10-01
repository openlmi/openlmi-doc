.. _LMI-Memory:

LMI_Memory
----------

Class reference
===============
Subclass of :ref:`CIM_Memory <CIM-Memory>`

Capabilities and management of Memory-related LogicalDevices.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-Memory-Access:

``uint16`` **Access**

    Access describes whether the media is readable (value=1), writeable (value=2), or both (value=3). "Unknown" (0) and "Write Once" (4) can also be defined.

    
    ======== ====================
    ValueMap Values              
    ======== ====================
    0        Unknown             
    1        Readable            
    2        Writeable           
    3        Read/Write Supported
    4        Write Once          
    ======== ====================
    
.. _LMI-Memory-StartingAddress:

``uint64`` **StartingAddress**

    The beginning address, referenced by an application or operating system and mapped by a memory controller, for this Memory object. The starting address is specified in KBytes.

    
.. _LMI-Memory-Name:

``string`` **Name**

    A unique identifier for the Extent.

    
.. _LMI-Memory-TransparentHugeMemoryPageStatus:

``uint16`` **TransparentHugeMemoryPageStatus**

    Current state of the transparent huge memory pages. The state can be "Unsupported", what means that the feature is not available on the system, "Never" when the feature is disabled, "Madvise" when huge pages are used only in marked memory area or "Always" when this feature is used all the time. 

    
    ======== ===========
    ValueMap Values     
    ======== ===========
    0        Unsupported
    1        Never      
    2        Madvise    
    3        Always     
    ======== ===========
    
.. _LMI-Memory-EnabledState:

``uint16`` **EnabledState**

    EnabledState is an integer enumeration that indicates the enabled and disabled states of an element. It can also indicate the transitions between these requested states. For example, shutting down (value=4) and starting (value=10) are transient states between enabled and disabled. The following text briefly summarizes the various enabled and disabled states: 

    Enabled (2) indicates that the element is or could be executing commands, will process any queued commands, and queues new requests. 

    Disabled (3) indicates that the element will not execute commands and will drop any new requests. 

    Shutting Down (4) indicates that the element is in the process of going to a Disabled state. 

    Not Applicable (5) indicates the element does not support being enabled or disabled. 

    Enabled but Offline (6) indicates that the element might be completing commands, and will drop any new requests. 

    Test (7) indicates that the element is in a test state. 

    Deferred (8) indicates that the element might be completing commands, but will queue any new requests. 

    Quiesce (9) indicates that the element is enabled but in a restricted mode.

    Starting (10) indicates that the element is in the process of going to an Enabled state. New requests are queued.

    
    ============ ===================
    ValueMap     Values             
    ============ ===================
    0            Unknown            
    1            Other              
    2            Enabled            
    3            Disabled           
    4            Shutting Down      
    5            Not Applicable     
    6            Enabled but Offline
    7            In Test            
    8            Deferred           
    9            Quiesce            
    10           Starting           
    11..32767    DMTF Reserved      
    32768..65535 Vendor Reserved    
    ============ ===================
    
.. _LMI-Memory-EndingAddress:

``uint64`` **EndingAddress**

    The ending address, referenced by an application or operating system and mapped by a memory controller, for this Memory object. The ending address is specified in KBytes.

    
.. _LMI-Memory-NumberOfBlocks:

``uint64`` **NumberOfBlocks**

    Total number of logically contiguous blocks, of size Block Size, which form this Extent. The total size of the Extent can be calculated by multiplying BlockSize by NumberOfBlocks. If the BlockSize is 1, this property is the total size of the Extent.

    
.. _LMI-Memory-IsCompressed:

``boolean`` **IsCompressed**

    The IsCompressed property indicates whether or not the data in the storage extent is compressed. When set to "true" the data is compressed. When set to "false" the data is not compressed.

    
.. _LMI-Memory-Volatile:

``boolean`` **Volatile**

    Volatile is a property that indicates whether this memory is volatile or not.

    
.. _LMI-Memory-ElementName:

``string`` **ElementName**

    A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. 

    Note that the Name property of ManagedSystemElement is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. Note that if there is an associated instance of CIM_EnabledLogicalElementCapabilities, restrictions on this properties may exist as defined in ElementNameMask and MaxElementNameLen properties defined in that class.

    
.. _LMI-Memory-DeviceID:

``string`` **DeviceID**

    An address or other identifying information used to uniquely name the LogicalDevice.

    
.. _LMI-Memory-SystemCreationClassName:

``string`` **SystemCreationClassName**

    The CreationClassName of the scoping system.

    
.. _LMI-Memory-InstanceID:

``string`` **InstanceID**

    InstanceID is an optional property that may be used to opaquely and uniquely identify an instance of this class within the scope of the instantiating Namespace. Various subclasses of this class may override this property to make it required, or a key. Such subclasses may also modify the preferred algorithms for ensuring uniqueness that are defined below.

    To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon (:), and where <OrgID> must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness, <OrgID> must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If not null and the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance. 

    If not set to null for DMTF-defined instances, the "preferred" algorithm must be used with the <OrgID> set to CIM.

    
.. _LMI-Memory-SystemName:

``string`` **SystemName**

    The System Name of the scoping system.

    
.. _LMI-Memory-Description:

``string`` **Description**

    The Description property provides a textual description of the object.

    
.. _LMI-Memory-SupportedHugeMemoryPageSizes:

``uint32[]`` **SupportedHugeMemoryPageSizes**

    All supported huge memory page sizes in currently running kernel in kB.

    
.. _LMI-Memory-StandardMemoryPageSize:

``uint32`` **StandardMemoryPageSize**

    Standard memory page size in kB.

    
.. _LMI-Memory-Purpose:

``string`` **Purpose**

    A free form string describing the media and/or its use.

    
.. _LMI-Memory-BlockSize:

``uint64`` **BlockSize**

    Size in bytes of the blocks which form this StorageExtent. If variable block size, then the maximum block size in bytes should be specified. If the block size is unknown or if a block concept is not valid (for example, for AggregateExtents, Memory or LogicalDisks), enter a 1.

    
.. _LMI-Memory-Caption:

``string`` **Caption**

    The Caption property is a short textual description (one- line string) of the object.

    
.. _LMI-Memory-HasNUMA:

``boolean`` **HasNUMA**

    Indicates whether memory has NUMA layout.

    
.. _LMI-Memory-CreationClassName:

``string`` **CreationClassName**

    CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

    
.. _LMI-Memory-ConsumableBlocks:

``uint64`` **ConsumableBlocks**

    The maximum number of blocks, of size BlockSize, which are available for consumption when layering StorageExtents using the BasedOn association. This property only has meaning when this StorageExtent is an Antecedent reference in a BasedOn relationship. For example, a StorageExtent could be composed of 120 blocks. However, the Extent itself may use 20 blocks for redundancy data. If another StorageExtent is BasedOn this Extent, only 100 blocks would be available to it. This information ('100 blocks is available for consumption') is indicated in the ConsumableBlocks property.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`Usage <CIM-StorageExtent-Usage>`
| ``string`` :ref:`OtherNameFormat <CIM-StorageExtent-OtherNameFormat>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`CompressionState <CIM-StorageExtent-CompressionState>`
| ``uint16`` :ref:`ErrorDataOrder <CIM-Memory-ErrorDataOrder>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint32`` :ref:`ErrorTransferSize <CIM-Memory-ErrorTransferSize>`
| ``string`` :ref:`OtherUsageDescription <CIM-StorageExtent-OtherUsageDescription>`
| ``boolean`` :ref:`IsComposite <CIM-StorageExtent-IsComposite>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`MaxQuiesceTime <CIM-LogicalDevice-MaxQuiesceTime>`
| ``uint64`` :ref:`TotalPowerOnHours <CIM-LogicalDevice-TotalPowerOnHours>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16`` :ref:`Availability <CIM-LogicalDevice-Availability>`
| ``uint8`` :ref:`DeltaReservation <CIM-StorageExtent-DeltaReservation>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``uint16[]`` :ref:`ClientSettableUsage <CIM-StorageExtent-ClientSettableUsage>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``boolean`` :ref:`Primordial <CIM-StorageExtent-Primordial>`
| ``uint16`` :ref:`NameFormat <CIM-StorageExtent-NameFormat>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16[]`` :ref:`AdditionalAvailability <CIM-LogicalDevice-AdditionalAvailability>`
| ``uint16`` :ref:`StatusInfo <CIM-LogicalDevice-StatusInfo>`
| ``uint64`` :ref:`ErrorAddress <CIM-Memory-ErrorAddress>`
| ``string[]`` :ref:`ExtentDiscriminator <CIM-StorageExtent-ExtentDiscriminator>`
| ``uint16`` :ref:`PackageRedundancy <CIM-StorageExtent-PackageRedundancy>`
| ``uint16`` :ref:`DataRedundancy <CIM-StorageExtent-DataRedundancy>`
| ``string`` :ref:`ErrorDescription <CIM-LogicalDevice-ErrorDescription>`
| ``uint32`` :ref:`LastErrorCode <CIM-LogicalDevice-LastErrorCode>`
| ``string`` :ref:`ErrorMethodology <CIM-Memory-ErrorMethodology>`
| ``uint16[]`` :ref:`ExtentStatus <CIM-StorageExtent-ExtentStatus>`
| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``boolean`` :ref:`NoSinglePointOfFailure <CIM-StorageExtent-NoSinglePointOfFailure>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`OtherNameNamespace <CIM-StorageExtent-OtherNameNamespace>`
| ``uint16`` :ref:`NameNamespace <CIM-StorageExtent-NameNamespace>`
| ``string[]`` :ref:`IdentifyingDescriptions <CIM-LogicalDevice-IdentifyingDescriptions>`
| ``boolean`` :ref:`ErrorCleared <CIM-LogicalDevice-ErrorCleared>`
| ``uint8[]`` :ref:`AdditionalErrorData <CIM-Memory-AdditionalErrorData>`
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``uint64`` :ref:`ExtentStripeLength <CIM-StorageExtent-ExtentStripeLength>`
| ``string`` :ref:`OtherErrorDescription <CIM-Memory-OtherErrorDescription>`
| ``uint16`` :ref:`LocationIndicator <CIM-LogicalDevice-LocationIndicator>`
| ``string[]`` :ref:`OtherIdentifyingInfo <CIM-LogicalDevice-OtherIdentifyingInfo>`
| ``uint8[]`` :ref:`ErrorData <CIM-Memory-ErrorData>`
| ``boolean`` :ref:`IsBasedOnUnderlyingRedundancy <CIM-StorageExtent-IsBasedOnUnderlyingRedundancy>`
| ``datetime`` :ref:`ErrorTime <CIM-Memory-ErrorTime>`
| ``boolean`` :ref:`SystemLevelAddress <CIM-Memory-SystemLevelAddress>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint64`` :ref:`ErrorResolution <CIM-Memory-ErrorResolution>`
| ``uint16`` :ref:`ErrorAccess <CIM-Memory-ErrorAccess>`
| ``boolean`` :ref:`CorrectableError <CIM-Memory-CorrectableError>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``uint16`` :ref:`CompressionRate <CIM-StorageExtent-CompressionRate>`
| ``uint16`` :ref:`DataOrganization <CIM-StorageExtent-DataOrganization>`
| ``uint64`` :ref:`PowerOnHours <CIM-LogicalDevice-PowerOnHours>`
| ``boolean`` :ref:`SequentialAccess <CIM-StorageExtent-SequentialAccess>`
| ``uint16[]`` :ref:`PowerManagementCapabilities <CIM-LogicalDevice-PowerManagementCapabilities>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint64`` :ref:`ExtentInterleaveDepth <CIM-StorageExtent-ExtentInterleaveDepth>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``boolean`` :ref:`IsConcatenated <CIM-StorageExtent-IsConcatenated>`
| ``uint16`` :ref:`ErrorInfo <CIM-Memory-ErrorInfo>`

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

