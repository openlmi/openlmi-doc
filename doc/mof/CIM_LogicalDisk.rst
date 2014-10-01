.. _CIM-LogicalDisk:

CIM_LogicalDisk
---------------

Class reference
===============
Subclass of :ref:`CIM_StorageExtent <CIM-StorageExtent>`

A LogicalDisk is a presentation of a contiguous range of logical blocks that is identifiable by applications such as filesystems via the Name field. (DeviceID (key) may use the same name or some other unique text such as a UUID.) For example in a Windows environment, the Name field may contain a drive letter. In a Unix environment, it may contain the access path (for example, '/dev/...'); and in a NetWare environment, may contain the volume name. LogicalDisks are typically built on a DiskPartition or other LogicalDisks (for instance, those exposed by a software volume manager). However, it can be based on other StorageExtents, like CIM_Memory, in the case of a RAM disk. 



LogicalDisks SHOULD set the 'Exported' value in ExtentStatus[] if they are intended for application use.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-LogicalDisk-ClientSettableUsage:

``uint16[]`` **ClientSettableUsage**

    Indicates which values from the "Usage" value map can be manipulated by a client using the method"StorageConfigurationService.RequestUsageChange".

    
.. _CIM-LogicalDisk-Usage:

``uint16`` **Usage**

    Indicates the intended usage or any restrictions that may have been imposed on the usage of this component. All ValueMap/Values entries are defined in CIM_StorageExtent. To promote interoperability across subclasses, all new entries for this class shall be defined there.

    
    ============ ==================================================
    ValueMap     Values                                            
    ============ ==================================================
    1            Other                                             
    2            Unrestricted                                      
    3            Reserved for ComputerSystem (the block server)    
    4            Reserved by Replication Services                  
    5            Reserved by Migration Services                    
    6            Local Replica Source                              
    7            Remote Replica Source                             
    8            Local Replica Target                              
    9            Remote Replica Target                             
    10           Local Replica Source or Target                    
    11           Remote Replica Source or Target                   
    12           Delta Replica Target                              
    13           Element Component                                 
    14           Reserved to be Unrestricted Pool Contributor      
    15           Composite Volume Member                           
    16           Composite LogicalDisk Member                      
    17           Reserved for Sparing                              
    18           In use as Unrestricted Pool Contributor           
    19           Reserved to be Delta Replica Pool Contributor     
    20           Reserved to be Local Replication Pool Contributor 
    21           Reserved to be Remote Replication Pool Contributor
    22           In use as Delta Replica Pool Contributor          
    23           In use as Local Replication Pool Contributor      
    24           In use as Remote Replication Pool Contributor     
    ..           DMTF Reserved                                     
    32768..65535 Vendor Reserved                                   
    ============ ==================================================
    
.. _CIM-LogicalDisk-NumExtentsMigrating:

``uint64`` **NumExtentsMigrating**

    The number of Extents in the process of migrating for this logical disk when the logical disk relocation is on going.

    
.. _CIM-LogicalDisk-NameFormat:

``uint16`` **NameFormat**

    LogicalDisk names shall use OS Device Name format.

    
    ======== ==============
    ValueMap Values        
    ======== ==============
    1        Other         
    12       OS Device Name
    ======== ==============
    
.. _CIM-LogicalDisk-OtherUsageDescription:

``string`` **OtherUsageDescription**

    Populated when "Usage" has the value of "Other".

    
.. _CIM-LogicalDisk-ThinlyProvisioned:

``boolean`` **ThinlyProvisioned**

    True if the logical disk is thinly provisioned.

    
.. _CIM-LogicalDisk-NameNamespace:

``uint16`` **NameNamespace**

    LogicalDisk names shall use OS Device Namespace.

    
    ======== ===================
    ValueMap Values             
    ======== ===================
    1        Other              
    8        OS Device Namespace
    ======== ===================
    

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
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``boolean`` :ref:`IsCompressed <CIM-StorageExtent-IsCompressed>`
| ``uint16`` :ref:`DataOrganization <CIM-StorageExtent-DataOrganization>`
| ``uint16`` :ref:`Access <CIM-StorageExtent-Access>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``boolean`` :ref:`Primordial <CIM-StorageExtent-Primordial>`
| ``string`` :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| ``uint16`` :ref:`CompressionRate <CIM-StorageExtent-CompressionRate>`
| ``boolean`` :ref:`NoSinglePointOfFailure <CIM-StorageExtent-NoSinglePointOfFailure>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint64`` :ref:`PowerOnHours <CIM-LogicalDevice-PowerOnHours>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string`` :ref:`OtherNameNamespace <CIM-StorageExtent-OtherNameNamespace>`
| ``uint64`` :ref:`ExtentInterleaveDepth <CIM-StorageExtent-ExtentInterleaveDepth>`
| ``string[]`` :ref:`IdentifyingDescriptions <CIM-LogicalDevice-IdentifyingDescriptions>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`OtherNameFormat <CIM-StorageExtent-OtherNameFormat>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``boolean`` :ref:`ErrorCleared <CIM-LogicalDevice-ErrorCleared>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`CompressionState <CIM-StorageExtent-CompressionState>`
| ``uint64`` :ref:`ExtentStripeLength <CIM-StorageExtent-ExtentStripeLength>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16`` :ref:`LocationIndicator <CIM-LogicalDevice-LocationIndicator>`
| ``string`` :ref:`Purpose <CIM-StorageExtent-Purpose>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string[]`` :ref:`OtherIdentifyingInfo <CIM-LogicalDevice-OtherIdentifyingInfo>`
| ``string`` :ref:`Name <CIM-StorageExtent-Name>`
| ``uint16[]`` :ref:`PowerManagementCapabilities <CIM-LogicalDevice-PowerManagementCapabilities>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint64`` :ref:`BlockSize <CIM-StorageExtent-BlockSize>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``boolean`` :ref:`SequentialAccess <CIM-StorageExtent-SequentialAccess>`
| ``uint16[]`` :ref:`AdditionalAvailability <CIM-LogicalDevice-AdditionalAvailability>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``boolean`` :ref:`IsComposite <CIM-StorageExtent-IsComposite>`
| ``uint16`` :ref:`StatusInfo <CIM-LogicalDevice-StatusInfo>`
| ``string`` :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| ``string[]`` :ref:`ExtentDiscriminator <CIM-StorageExtent-ExtentDiscriminator>`
| ``uint16`` :ref:`PackageRedundancy <CIM-StorageExtent-PackageRedundancy>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint16`` :ref:`DataRedundancy <CIM-StorageExtent-DataRedundancy>`
| ``uint64`` :ref:`NumberOfBlocks <CIM-StorageExtent-NumberOfBlocks>`
| ``uint64`` :ref:`MaxQuiesceTime <CIM-LogicalDevice-MaxQuiesceTime>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint64`` :ref:`TotalPowerOnHours <CIM-LogicalDevice-TotalPowerOnHours>`
| ``string`` :ref:`ErrorDescription <CIM-LogicalDevice-ErrorDescription>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``boolean`` :ref:`IsConcatenated <CIM-StorageExtent-IsConcatenated>`
| ``uint32`` :ref:`LastErrorCode <CIM-LogicalDevice-LastErrorCode>`
| ``string`` :ref:`ErrorMethodology <CIM-StorageExtent-ErrorMethodology>`
| ``string`` :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
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

