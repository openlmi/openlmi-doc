.. _LMI-DiskPartitionConfigurationService:

LMI_DiskPartitionConfigurationService
-------------------------------------

Class reference
===============
Subclass of :ref:`CIM_DiskPartitionConfigurationService <CIM-DiskPartitionConfigurationService>`

DiskPartitionConfigurationService provides methods for clients to configure DiskPartitions. 

Any CIM_StorageExtent can be partitioned, but it's strongly recommended to partition only disks.

Several partition styles are supported, see LMI_DiskPartitionConfigurationCapabilities instances. GPT partition style is strongly recommended. While MS-DOS (MBR) style partitions are fully supported, creation and modification of logical partitions require non-trivial calculations and should be avoided unless the application really knows what it is doing.


Key properties
^^^^^^^^^^^^^^

| :ref:`Name <CIM-Service-Name>`
| :ref:`SystemName <CIM-Service-SystemName>`
| :ref:`SystemCreationClassName <CIM-Service-SystemCreationClassName>`
| :ref:`CreationClassName <CIM-Service-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-DiskPartitionConfigurationService-PartitioningSchemes:

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

    .. _LMI-DiskPartitionConfigurationService-CreateOrModifyPartition:

``uint32`` **CreateOrModifyPartition** (:ref:`CIM_StorageExtent <CIM-StorageExtent>` extent, ``uint64`` StartingAddress, ``uint64`` EndingAddress, ``string`` DeviceFileName, :ref:`CIM_GenericDiskPartition <CIM-GenericDiskPartition>` Partition)

    This method creates a new partition if the Partition parameter is null or modifies the partition specified. If the starting and ending address parameters are null, the resulting partition will occupy the entire underlying extent. If the starting address is non-null and the ending address is null, the resulting partition will extend to the end of the underlying extent.

    

    In contradiction to SMI-S, no LogicalDisk will be created on the partition.

    This methods is only for compatibility with SMI-S.Applications should use LMI_CreateOrModifyPartition instead.

    If logical partition is being created, it's start/end sector must include space for partition metadata and any alignment sectors. ConsumableSpace of the logical partition will be reduced by these metadata and alignment sectors.

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
            The starting block number. If null when creating a partition, the first block is used.If null when modifying a partition, the partition start won't be chnaged.

            
        
        *IN* ``uint64`` **EndingAddress**
            The ending block number. If null when creating a partition, the last block of the device will be used. If null when modifying a partition, the partition end won't be chnaged.

            
        
        *IN* ``string`` **DeviceFileName**
            The platform-specific special file name to be assigned to the LogicalDisk instance BasedOn the new DiskPartition instance.

            
        
        *IN*, *OUT* :ref:`CIM_GenericDiskPartition <CIM-GenericDiskPartition>` **Partition**
            A reference an existing partition instance to modify or null to request a new partition.

            
        
    
    .. _LMI-DiskPartitionConfigurationService-LMI-DeletePartition:

``uint32`` **LMI_DeletePartition** (:ref:`CIM_GenericDiskPartition <CIM-GenericDiskPartition>` Partition, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job)

    Delete partition.

    
    ============ =======================================
    ValueMap     Values                                 
    ============ =======================================
    0            Job Completed with No Error            
    1            Not Supported                          
    2            Unknown                                
    3            Timeout                                
    4            Failed                                 
    5            Invalid Parameter                      
    6            In Use                                 
    ..           DMTF Reserved                          
    4096         Method Parameters Checked - Job Started
    4097         Size Not Supported                     
    4098..32767  Method Reserved                        
    32768..65535 Vendor Specific                        
    ============ =======================================
    
    **Parameters**
    
        *IN* :ref:`CIM_GenericDiskPartition <CIM-GenericDiskPartition>` **Partition**
            A reference an existing partition instance to delete.

            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            A reference to started job (may be null if job is completed).

            
        
    
    .. _LMI-DiskPartitionConfigurationService-SetPartitionStyle:

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

            
        
    
    .. _LMI-DiskPartitionConfigurationService-LMI-CreateOrModifyPartition:

``uint32`` **LMI_CreateOrModifyPartition** (:ref:`CIM_StorageExtent <CIM-StorageExtent>` extent, ``uint64`` Size, :ref:`CIM_GenericDiskPartition <CIM-GenericDiskPartition>` Partition, :ref:`LMI_DiskPartitionConfigurationSetting <LMI-DiskPartitionConfigurationSetting>` Goal, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job)

    Create new partition on given extent.Partition modification is not yet supported.The implementation will select the best space to fit the partition, with all alignment rules etc. 

    If no Size parameter is provided, the largest possible partition is created.

    The Goal parameter is not supported for now, the behavior below applies.

    If no Goal is provided and GPT partition is requested, normal partition is created. If no Goal is provided and MS-DOS partition is requested and there is extended partition already on the device, a logical partition is created. If there is no extended partition on the device and there are at most two primary partitions on the device, primary partition is created. If there is no extended partition and three primary partitions already exist, new extended partition with all remaining space is created and a logical partition with requested size is created.

    
    ============ =======================================
    ValueMap     Values                                 
    ============ =======================================
    0            Job Completed with No Error            
    1            Not Supported                          
    2            Unknown                                
    3            Timeout                                
    4            Failed                                 
    5            Invalid Parameter                      
    6            In Use                                 
    ..           DMTF Reserved                          
    4096         Method Parameters Checked - Job Started
    4097         Size Not Supported                     
    4098..32767  Method Reserved                        
    32768..65535 Vendor Specific                        
    ============ =======================================
    
    **Parameters**
    
        *IN* :ref:`CIM_StorageExtent <CIM-StorageExtent>` **extent**
            A reference to the underlying extent the partition is base on.

            
        
        *IN*, *OUT* ``uint64`` **Size**
            Requested size of the partition to create. If null when creating a partition, the larges possible partition is created.On output, the achieved size is returned.

            
        
        *IN*, *OUT* :ref:`CIM_GenericDiskPartition <CIM-GenericDiskPartition>` **Partition**
            A reference an existing partition instance to modify or null to request a new partition.

            
        
        *IN* :ref:`LMI_DiskPartitionConfigurationSetting <LMI-DiskPartitionConfigurationSetting>` **Goal**
            Setting to be applied to created/modified partition.

            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            A reference to started job (may be null if job is completed).

            
        
    

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

