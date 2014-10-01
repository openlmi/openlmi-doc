.. _LMI-DiskPartition:

LMI_DiskPartition
-----------------

Class reference
===============
Subclass of :ref:`CIM_DiskPartition <CIM-DiskPartition>`

This class represents primary, extended and logical partitions on devices with MS-DOS (MBR) style partition tables.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-DiskPartition-InstanceID:

``string`` **InstanceID**

    InstanceID is an optional property that may be used to opaquely and uniquely identify an instance of this class within the scope of the instantiating Namespace. Various subclasses of this class may override this property to make it required, or a key. Such subclasses may also modify the preferred algorithms for ensuring uniqueness that are defined below.

    To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon (:), and where <OrgID> must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness, <OrgID> must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If not null and the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance. 

    If not set to null for DMTF-defined instances, the "preferred" algorithm must be used with the <OrgID> set to CIM.

    
.. _LMI-DiskPartition-ExtentStripeLength:

``uint64`` **ExtentStripeLength**

    If not null, then IsComposite shall be true. Number of contiguous underlying StorageExtents counted before looping back to the first underlying StorageExtent of the current stripe. It is the number of StorageExtents forming the user data stripe.

    
.. _LMI-DiskPartition-Primordial:

``boolean`` **Primordial**

    If true, "Primordial" indicates that the containing System does not have the ability to create or delete this operational element. This is important because StorageExtents are assembled into higher-level abstractions using the BasedOn association. Although the higher-level abstractions can be created and deleted, the most basic, (i.e. primordial), hardware-based storage entities cannot. They are physically realized as part of the System, or are actually managed by some other System and imported as if they were physically realized. In other words, a Primordial StorageExtent exists in, but is not created by its System and conversely a non-Primordial StorageExtent is created in the context of its System. For StorageVolumes, this property will generally be false. One use of this property is to enable algorithms that aggregate StorageExtent.ConsumableSpace across all, StorageExtents but that also want to distinquish the space that underlies Primordial StoragePools. Since implementations are not required to surface all Component StorageExtents of a StoragePool, this information is not accessible in any other way.

    
.. _LMI-DiskPartition-NoSinglePointOfFailure:

``boolean`` **NoSinglePointOfFailure**

    Indicates whether or not there exists no single point of failure.

    
.. _LMI-DiskPartition-DeviceBusType:

``string`` **DeviceBusType**

    Name of bus, used to connect the block device, such as USB, SCSI or ATA. This property is available mostly for disk block devices, not for their descendants like partitions, logical volumes and so on. Note that the list of values may not be complete and is not guaranteed to be stable.

    
.. _LMI-DiskPartition-ElementName:

``string`` **ElementName**

    A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. 

    Note that the Name property of ManagedSystemElement is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. Note that if there is an associated instance of CIM_EnabledLogicalElementCapabilities, restrictions on this properties may exist as defined in ElementNameMask and MaxElementNameLen properties defined in that class.

    
.. _LMI-DiskPartition-NameNamespace:

``uint16`` **NameNamespace**

    DiskPartition names MUST use OS Device Namespace.

    
    ======== ===================
    ValueMap Values             
    ======== ===================
    1        Other              
    8        OS Device Namespace
    ======== ===================
    
.. _LMI-DiskPartition-NameFormat:

``uint16`` **NameFormat**

    DiskPartition names MUST use OS Device Name format. In cases where the partition names can not be used by applications programmatically (for example, open()) the NameFormat SHOULD be 'Other'.

    
    ======== ==============
    ValueMap Values        
    ======== ==============
    1        Other         
    12       OS Device Name
    ======== ==============
    
.. _LMI-DiskPartition-PrimaryPartition:

``boolean`` **PrimaryPartition**

    Boolean indicating that the DiskPartition is labelled as the primary partition for a ComputerSystem.

    
.. _LMI-DiskPartition-PartitionType:

``uint16`` **PartitionType**

    The type of Partition.

    
    ======== ========
    ValueMap Values  
    ======== ========
    0        Unknown 
    1        Primary 
    2        Extended
    3        Logical 
    ======== ========
    
.. _LMI-DiskPartition-Name:

``string`` **Name**

    A unique identifier for the Extent.

    
.. _LMI-DiskPartition-BlockSize:

``uint64`` **BlockSize**

    Size in bytes of the blocks which form this StorageExtent. If variable block size, then the maximum block size in bytes should be specified. If the block size is unknown or if a block concept is not valid (for example, for AggregateExtents, Memory or LogicalDisks), enter a 1.

    
.. _LMI-DiskPartition-ExtentDiscriminator:

``string[]`` **ExtentDiscriminator**

    An array of strings used to discriminate the association context in which this StorageExtent is instantiated. Each element of the array should be prefixed by a well known organization name followed by a colon and followed by a string defined by that organization. For example, SNIA SMI-S compliant instances might contain one or more of the following values: 

    'SNIA:Pool Component' - A StorageExtent (or CompositeExtent) that represents storage of a StoragePool and has an AssociatedComponentExtent to its StoragePool, but is not a remaining extent. 

    'SNIA:Remaining' - A StorageExtent that has an AssociatedRemainingExtent to a StoragePool (representing free storage in the StoragePool). 

    'SNIA:Intermediate' - A StorageExtent (or CompositeExtent) that is neither a Pool Component nor a Remaining Extent (it does not represent storage in the pool, remaining or otherwise). 

    'SNIA:Composite' - A StorageExtent that is a CompositeExtent. 

    'SNIA:DiskDrive' - A StorageExtent that is the media on a Disk Drive. 

    'SNIA:Imported' - A StorageExtent that is imported from an external source. 

    'SNIA:Allocated' - A StorageExtent that is subclassed to StorageVolume or LogicalDisk, and has an AllocatedFromStoragePool association from a Concrete StoragePool. 

    'SNIA:Shadow' - A StorageExtent (or subclass) that represents a StorageExtent in another autonomous profile (e.g., the StorageVirtualizer has StorageVolumes (Shadow) that represent StorageVolumes exported by Arrays). 

    'SNIA:Spare' - A StorageExtent that acts as a spare for other StorageExtents (and has the IsSpare association). 

    'SNIA:Reserved' - A StorageExtent that is reserved for some system use within the autonomous profile (e.g., in NAS profiles, an Allocated LogicalDisk is reserved for holding Filesystems).

    
.. _LMI-DiskPartition-PackageRedundancy:

``uint16`` **PackageRedundancy**

    How many physical packages can currently fail without data loss. For example, in the storage domain, this might be disk spindles.

    
.. _LMI-DiskPartition-DataRedundancy:

``uint16`` **DataRedundancy**

    Number of complete copies of data currently maintained.

    
.. _LMI-DiskPartition-NumberOfBlocks:

``uint64`` **NumberOfBlocks**

    Total number of logically contiguous blocks, of size Block Size, which form this Extent. The total size of the Extent can be calculated by multiplying BlockSize by NumberOfBlocks. If the BlockSize is 1, this property is the total size of the Extent.

    
.. _LMI-DiskPartition-OperationalStatus:

``uint16[]`` **OperationalStatus**

    Indicates the current statuses of the element. Various operational statuses are defined. Many of the enumeration's values are self-explanatory. However, a few are not and are described here in more detail. 

    "Stressed" indicates that the element is functioning, but needs attention. Examples of "Stressed" states are overload, overheated, and so on. 

    "Predictive Failure" indicates that an element is functioning nominally but predicting a failure in the near future. 

    "In Service" describes an element being configured, maintained, cleaned, or otherwise administered. 

    "No Contact" indicates that the monitoring system has knowledge of this element, but has never been able to establish communications with it. 

    "Lost Communication" indicates that the ManagedSystem Element is known to exist and has been contacted successfully in the past, but is currently unreachable. 

    "Stopped" and "Aborted" are similar, although the former implies a clean and orderly stop, while the latter implies an abrupt stop where the state and configuration of the element might need to be updated. 

    "Dormant" indicates that the element is inactive or quiesced. 

    "Supporting Entity in Error" indicates that this element might be "OK" but that another element, on which it is dependent, is in error. An example is a network service or endpoint that cannot function due to lower-layer networking problems. 

    "Completed" indicates that the element has completed its operation. This value should be combined with either OK, Error, or Degraded so that a client can tell if the complete operation Completed with OK (passed), Completed with Error (failed), or Completed with Degraded (the operation finished, but it did not complete OK or did not report an error). 

    "Power Mode" indicates that the element has additional power model information contained in the Associated PowerManagementService association. 

    "Relocating" indicates the element is being relocated.

    OperationalStatus replaces the Status property on ManagedSystemElement to provide a consistent approach to enumerations, to address implementation needs for an array property, and to provide a migration path from today's environment to the future. This change was not made earlier because it required the deprecated qualifier. Due to the widespread use of the existing Status property in management applications, it is strongly recommended that providers or instrumentation provide both the Status and OperationalStatus properties. Further, the first value of OperationalStatus should contain the primary status for the element. When instrumented, Status (because it is single-valued) should also provide the primary status of the element.

    
    ======== ==========================
    ValueMap Values                    
    ======== ==========================
    0        Unknown                   
    1        Other                     
    2        OK                        
    3        Degraded                  
    4        Stressed                  
    5        Predictive Failure        
    6        Error                     
    7        Non-Recoverable Error     
    8        Starting                  
    9        Stopping                  
    10       Stopped                   
    11       In Service                
    12       No Contact                
    13       Lost Communication        
    14       Aborted                   
    15       Dormant                   
    16       Supporting Entity in Error
    17       Completed                 
    18       Power Mode                
    19       Relocating                
    ..       DMTF Reserved             
    0x8000.. Vendor Reserved           
    ======== ==========================
    
.. _LMI-DiskPartition-Names:

``string[]`` **Names**

    All names, under which this device is known. All these names are symlinks to one block device.

    
.. _LMI-DiskPartition-ExtentStatus:

``uint16[]`` **ExtentStatus**

    StorageExtents have additional status information beyond that captured in the OperationalStatus and other properties, inherited from ManagedSystemElement. This additional information (for example, "Protection Disabled", value=9) is captured in the ExtentStatus property. 

    'In-Band Access Granted' says that access to data on an extent is granted to some consumer and is only valid when 'Exported' is also set. It is set as a side effect of PrivilegeManagementService.ChangeAccess or equivalent interfaces. 

    'Imported' indicates that the extent is used in the current system, but known to be managed by some other system. For example, a server imports volumes from a disk array. 

    'Exported' indicates the extent is meant to be used by some comsumer. A disk array's logical units are exported. 

    Intermediate composite extents may be neither imported nor exported.

    'Relocating' indicates the extent is being relocated.

    
    ============ ======================
    ValueMap     Values                
    ============ ======================
    0            Other                 
    1            Unknown               
    2            None/Not Applicable   
    3            Broken                
    4            Data Lost             
    5            Dynamic Reconfig      
    6            Exposed               
    7            Fractionally Exposed  
    8            Partially Exposed     
    9            Protection Disabled   
    10           Readying              
    11           Rebuild               
    12           Recalculate           
    13           Spare in Use          
    14           Verify In Progress    
    15           In-Band Access Granted
    16           Imported              
    17           Exported              
    18           Relocating            
    ..           DMTF Reserved         
    32768..65535 Vendor Reserved       
    ============ ======================
    
.. _LMI-DiskPartition-ConsumableBlocks:

``uint64`` **ConsumableBlocks**

    The maximum number of blocks, of size BlockSize, which are available for consumption when layering StorageExtents using the BasedOn association. This property only has meaning when this StorageExtent is an Antecedent reference in a BasedOn relationship. For example, a StorageExtent could be composed of 120 blocks. However, the Extent itself may use 20 blocks for redundancy data. If another StorageExtent is BasedOn this Extent, only 100 blocks would be available to it. This information ('100 blocks is available for consumption') is indicated in the ConsumableBlocks property.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint8`` :ref:`DeltaReservation <CIM-StorageExtent-DeltaReservation>`
| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``boolean`` :ref:`IsBasedOnUnderlyingRedundancy <CIM-StorageExtent-IsBasedOnUnderlyingRedundancy>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``boolean`` :ref:`ErrorCleared <CIM-LogicalDevice-ErrorCleared>`
| ``string`` :ref:`Signature <CIM-MediaPartition-Signature>`
| ``string[]`` :ref:`OtherIdentifyingInfo <CIM-LogicalDevice-OtherIdentifyingInfo>`
| ``uint16`` :ref:`DataOrganization <CIM-StorageExtent-DataOrganization>`
| ``uint16`` :ref:`Access <CIM-StorageExtent-Access>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| ``uint16`` :ref:`CompressionRate <CIM-StorageExtent-CompressionRate>`
| ``uint16`` :ref:`Usage <CIM-StorageExtent-Usage>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``string`` :ref:`SignatureAlgorithm <CIM-MediaPartition-SignatureAlgorithm>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint16`` :ref:`PartitionSubtype <CIM-DiskPartition-PartitionSubtype>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string`` :ref:`OtherNameNamespace <CIM-StorageExtent-OtherNameNamespace>`
| ``string[]`` :ref:`IdentifyingDescriptions <CIM-LogicalDevice-IdentifyingDescriptions>`
| ``uint64`` :ref:`ExtentInterleaveDepth <CIM-StorageExtent-ExtentInterleaveDepth>`
| ``string`` :ref:`OtherNameFormat <CIM-StorageExtent-OtherNameFormat>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``boolean`` :ref:`IsConcatenated <CIM-StorageExtent-IsConcatenated>`
| ``string`` :ref:`Purpose <CIM-StorageExtent-Purpose>`
| ``uint16[]`` :ref:`ClientSettableUsage <CIM-StorageExtent-ClientSettableUsage>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16`` :ref:`LocationIndicator <CIM-LogicalDevice-LocationIndicator>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``boolean`` :ref:`Extendable <CIM-MediaPartition-Extendable>`
| ``boolean`` :ref:`IsCompressed <CIM-StorageExtent-IsCompressed>`
| ``uint16[]`` :ref:`PowerManagementCapabilities <CIM-LogicalDevice-PowerManagementCapabilities>`
| ``boolean`` :ref:`Bootable <CIM-MediaPartition-Bootable>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``boolean`` :ref:`SequentialAccess <CIM-StorageExtent-SequentialAccess>`
| ``uint16[]`` :ref:`AdditionalAvailability <CIM-LogicalDevice-AdditionalAvailability>`
| ``uint16`` :ref:`CompressionState <CIM-StorageExtent-CompressionState>`
| ``string`` :ref:`OtherUsageDescription <CIM-StorageExtent-OtherUsageDescription>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``boolean`` :ref:`IsComposite <CIM-StorageExtent-IsComposite>`
| ``uint16`` :ref:`StatusInfo <CIM-LogicalDevice-StatusInfo>`
| ``string`` :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| ``uint64`` :ref:`PowerOnHours <CIM-LogicalDevice-PowerOnHours>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`MaxQuiesceTime <CIM-LogicalDevice-MaxQuiesceTime>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint64`` :ref:`TotalPowerOnHours <CIM-LogicalDevice-TotalPowerOnHours>`
| ``string`` :ref:`ErrorDescription <CIM-LogicalDevice-ErrorDescription>`
| ``boolean`` :ref:`Allocatable <CIM-MediaPartition-Allocatable>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint32`` :ref:`LastErrorCode <CIM-LogicalDevice-LastErrorCode>`
| ``string`` :ref:`ErrorMethodology <CIM-StorageExtent-ErrorMethodology>`
| ``string`` :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| ``string`` :ref:`SignatureState <CIM-MediaPartition-SignatureState>`
| ``uint16`` :ref:`Availability <CIM-LogicalDevice-Availability>`
| ``string`` :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

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

