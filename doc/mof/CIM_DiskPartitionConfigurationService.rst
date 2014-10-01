.. _CIM-DiskPartitionConfigurationService:

CIM_DiskPartitionConfigurationService
-------------------------------------

Class reference
===============
Subclass of :ref:`CIM_Service <CIM-Service>`

DiskPartitionConfigurationService provides methods for clients 

to configure DiskPartitions. 



The instrumentation MUST NOT instantiate instances of partitions (such as hidden, maintenance, or zero-length partitions) that are not intended for use by applications (filesystems, databases, ...). There are two reasons for this constraint. There are different system-specific ways to indicate whether or not a partition is hidden, in some cases, the starting/ending block information is invalid, but ignored. If these properties are exposed, clients will not have a way to determine which blocks are in use. The other reason is that typically the number of partitions is fixed in the underlying data structures (or grows by large, fixed-size chunks). Common practice is to have a one (or a few) partition per disk with many hidden partitions. Instantiating a lot of hidden partitions clutters up the model without value add. The methods of this service and the properties of DiskPartitionConfigurationCapabilities provide a view of partitions actually in use without requiring clients to understand system-specific details.


Key properties
^^^^^^^^^^^^^^

| :ref:`Name <CIM-Service-Name>`
| :ref:`SystemName <CIM-Service-SystemName>`
| :ref:`SystemCreationClassName <CIM-Service-SystemCreationClassName>`
| :ref:`CreationClassName <CIM-Service-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-DiskPartitionConfigurationService-PartitioningSchemes:

``uint16`` **PartitioningSchemes**

    Describes the partitioning schemes supported by the platform. AIX and HP_UX do not allow partitions. Linux allows volumes with and without partitions, Solaris requires Partitions. No more than a single instance of this class MAY be instantiated on a system. If set to 'No partitions allowed' then the methods of this service are not available.

    
    ======== ==============================================
    ValueMap Values                                        
    ======== ==============================================
    2        No partitions allowed                         
    3        Volumes may be partitioned or treated as whole
    4        Volumes must be partitioned                   
    ======== ==============================================
    

Local methods
^^^^^^^^^^^^^

    .. _CIM-DiskPartitionConfigurationService-CreateOrModifyPartition:

``uint32`` **CreateOrModifyPartition** (:ref:`CIM_StorageExtent <CIM-StorageExtent>` extent, ``uint64`` StartingAddress, ``uint64`` EndingAddress, ``string`` DeviceFileName, :ref:`CIM_GenericDiskPartition <CIM-GenericDiskPartition>` Partition)

    This method creates a new partition if the Partition parameter is null or modifies the partition specified. If the starting and ending address parameters are null, the resulting partition will occupy the entire underlying extent. If the starting address is non-null and the ending address is null, the resulting partition will extend to the end of the underlying extent. 

    

    If a partition is being created, a LogicalDisk instance is also created BasedOn the partition. The NumberOfBlocks and ComsumableBlocks properties MUST be the same value and MUST be common to the partition and LogicalDisk (since partition metadata is part of the partition table, not part of partitions). The StartingAddress of the LogicalDisk MUST be 0, the ConsumableBlocks of the LogicalDisk and partition MUST be the same, and the difference between the StartingAddress and EndingAddress of the partition and LogicalDisk must be the same - one less than ConsumableBlocks/NumberOfBlocks. 

    

    The underlying extent MUST be associated to a capabilities class describing the installed partition style (partition table); this association is established using SetPartitionStyle().

    
    ======== ================================================
    ValueMap Values                                          
    ======== ================================================
    0        Success                                         
    1        Not Supported                                   
    2        Unknown                                         
    3        Timeout                                         
    4        Failed                                          
    5        Invalid Parameter                               
    ..       DMTF Reserved                                   
    0x1000   Overlap Not Supported                           
    0x1001   No Available Partitions                         
    0x1002   Specified partition not on specified extent     
    0x1003   Device File Name not valid                      
    0x1004   LogicalDisk with different DeviceFileName exists
    ..       Method Reserved                                 
    0x8000.. Vendor Specific                                 
    ======== ================================================
    
    **Parameters**
    
        *IN* :ref:`CIM_StorageExtent <CIM-StorageExtent>` **extent**
            A reference to the underlying extent the partition is base on.

            
        
        *IN* ``uint64`` **StartingAddress**
            The starting block number.

            
        
        *IN* ``uint64`` **EndingAddress**
            The ending block number.

            
        
        *IN* ``string`` **DeviceFileName**
            The platform-specific special file name to be assigned to the LogicalDisk instance BasedOn the new DiskPartition instance.

            
        
        *IN*, *OUT* :ref:`CIM_GenericDiskPartition <CIM-GenericDiskPartition>` **Partition**
            A reference an existing partition instance to modify or null to request a new partition.

            
        
    
    .. _CIM-DiskPartitionConfigurationService-SetPartitionStyle:

``uint32`` **SetPartitionStyle** (:ref:`CIM_StorageExtent <CIM-StorageExtent>` Extent, :ref:`CIM_DiskPartitionConfigurationCapabilities <CIM-DiskPartitionConfigurationCapabilities>` PartitionStyle)

    This method installs a partition table on an extent of the specified partition style; creating an association between the extent and that capabilities instances referenced as method parameters. As a side effect, the consumable block size of the underlying extent is reduced by the block size of the metadata reserved by the partition table and associated metadata. This size is in the PartitionTableSize property of the associated DiskPartitionConfigurationCapabilities instance.

    
    ======== ==================================
    ValueMap Values                            
    ======== ==================================
    0        Success                           
    1        Not Supported                     
    2        Unknown                           
    3        Timeout                           
    4        Failed                            
    5        Invalid Parameter                 
    ..       DMTF Reserved                     
    0x1000   Extent already has partition table
    0x1001   Requested Extent too large        
    0x1002   Style not supported by Service    
    ..       Method Reserved                   
    0x8000.. Vendor Specific                   
    ======== ==================================
    
    **Parameters**
    
        *IN* :ref:`CIM_StorageExtent <CIM-StorageExtent>` **Extent**
            A reference to the extent (volume or partition) where this style (partition table) will be installed.

            
        
        *IN* :ref:`CIM_DiskPartitionConfigurationCapabilities <CIM-DiskPartitionConfigurationCapabilities>` **PartitionStyle**
            A reference to the DiskPartitionConfigurationCapabilities instance describing the desired partition style.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`SystemName <CIM-Service-SystemName>`
| ``string`` :ref:`LoSID <CIM-Service-LoSID>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``boolean`` :ref:`Started <CIM-Service-Started>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`Name <CIM-Service-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``string`` :ref:`LoSOrgID <CIM-Service-LoSOrgID>`
| ``string`` :ref:`PrimaryOwnerContact <CIM-Service-PrimaryOwnerContact>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`StartMode <CIM-Service-StartMode>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`SystemCreationClassName <CIM-Service-SystemCreationClassName>`
| ``string`` :ref:`CreationClassName <CIM-Service-CreationClassName>`
| ``string`` :ref:`PrimaryOwnerName <CIM-Service-PrimaryOwnerName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`
| :ref:`StopService <CIM-Service-StopService>`
| :ref:`ChangeAffectedElementsAssignedSequence <CIM-Service-ChangeAffectedElementsAssignedSequence>`
| :ref:`StartService <CIM-Service-StartService>`

