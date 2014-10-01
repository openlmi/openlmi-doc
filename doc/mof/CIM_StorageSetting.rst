.. _CIM-StorageSetting:

CIM_StorageSetting
------------------

Class reference
===============
Subclass of :ref:`CIM_SettingData <CIM-SettingData>`

StorageSetting is roughly equivalent to a Service Level Agreement (SLA) It defines the characteristics, qualities of service and goals when used in a CreateOrModifyElement FromStoragePool or CreateOrModifyStoragePool method in the StorageConfigurationService. It specifies a series of properties with Maximum and Minimum values that define the (inclusive) bounds that the object should maintain. Note that the setting is associated to a StorageVolume or LogicalDisk, using ElementSetting. 

The use of these properties differs depending on whether the StorageSetting instance is being used as a goal for a configuration operation or being used as a Service Level Agreement for a created Volume. In addition the properties fall into two categories: The QOS properties(PackageRedundancy, Data Redundancy, & NoSinglePointOfFailure) and the Detailed RAID properties(ExtentStripeLength, ParityLayout, and UserDataStripeDepth). In a Setting used as a goal, the QOS properties are required as a set; The Detailed RAID properties(if supported as indicated by the scoping StorageCapabilities instance) may be used optionally in any combination. The implementation MUST supply it's own best practice in the case where one or more supported RAID properties are not supplied. In this situation the use of StorageSettingWithHints can be useful to provide direction to the implementation. 

In a Setting used as a service agreement for a Volume, the QOS properties reflect the Service Level Agreement, with goal, min, & max. The actual current service level is exposed by corresponding values in StorageExtent. 

The Detailed RAID properties, by contrast, reflect specific values that reflect the RAID construction of the Volume. Only the primary values are meaningful; Min and Max are set to match. 

Certain StorageSetting instances may be classed as "Fixed", by using the "ChangeableType" property, indicating the setting is preset. Such settings are used when the possible setting variations are low enough to be instantiated in their entirety. The StorageCapabilities "CreateSetting" method MAY NOT be used to return settings that are not changeable. 

Other StorageSetting instances are created using the "CreateSetting" method. If the capabilities specifies ranges, then the setting can be used by a client to narrow the range to particular values within the range. In other words, the capabilities MAY be broad, but the related setting MUST be as capable or less capable, that is more narrowly defined, before it is used to create or modify resources. 

These created StorageSetting instances MUST have their "ChangeableType" property = 1, "Changeable - Transient". 

GeneratedSettings MAY not remain after the restart or reset of the implementation. They may be deleted by implementation at any time. A reasonable minimal time to retain the generated transient settings is five minutes, although there is no minimal retention time.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-StorageSetting-InterconnectSpeed:

``uint64`` **InterconnectSpeed**

    The speed of disk interconnection wanted. Value of 0 means don't care. Values are in bits/second

    
.. _CIM-StorageSetting-InterconnectType:

``uint16`` **InterconnectType**

    Enumeration indicating the type of disk interconnection wanted.

    
    ======== ==========
    ValueMap Values    
    ======== ==========
    0        don't care
    1        other     
    2        SAS       
    3        SATA      
    4        SAS/SATA  
    5        FC        
    6        SOP       
    ======== ==========
    
.. _CIM-StorageSetting-DeltaReservationGoal:

``uint8`` **DeltaReservationGoal**

    DeltaReservationGoal is a number between 1 (1%) and a 100 (100%) which specifies the desired amount of space that should be reserved in a replica for caching changes. For a complete copy this would be 100%. The bounds (max and min) for the reservation are defined using the properties, DeltaReservationMax and DeltaReservationMin.

    
.. _CIM-StorageSetting-DataRedundancyMin:

``uint16`` **DataRedundancyMin**

    DataRedundancyMin describes the minimum number of complete copies of data to be maintained. Examples would be RAID 5 where 1 copy is maintained and RAID 1 where 2 or more copies are maintained. Possible values are 1 to n. The desired redundancy is specified using DataRedundancyGoal, while the maximum is defined by DataRedundancyMax.

    
.. _CIM-StorageSetting-UseReplicationBuffer:

``uint16`` **UseReplicationBuffer**

    "Not Applicable" indicates that this property is not applicable to the associated storage element. Other values indicate whether or not remote mirror pair created with SynchronizationType "Async" is allowed to use a write buffer for asynchronous buffering. These other values are defined as: 

    - "Not Managed": use or not of the buffer is up to the implementation. 

    - "Use Buffer": use of a buffer for logging is required. 

    - "Do Not Use Buffer": a buffer for logging shall not be used.

    
    ======== =================
    ValueMap Values           
    ======== =================
    0        Not Applicable   
    1        Not Managed      
    2        Use Buffer       
    3        Do Not Use Buffer
    ..       DMTF Reserved    
    0x8000.. Vendor Specific  
    ======== =================
    
.. _CIM-StorageSetting-LowSpaceWarningThreshold:

``uint16`` **LowSpaceWarningThreshold**

    LowSpaceWarningThreshold simplifies the creation of a pool specific Indication based on RemainingManagedSpace <= 

    (TotalManagedSpace*LowSpaceWarningThreshold)/100. One example client for an Indication based on this property is a delta copy implementation where the pool enables continuous, variable space consumption for the delta storage. Another example client for an Indication based on this property is a provisioning manager implementing a policy for adding storage to a pool when it becomes low.

    
.. _CIM-StorageSetting-DiskType:

``uint16`` **DiskType**

    Enumeration indicating the type of DiskDrives which may be available.

    
    ======== =================
    ValueMap Values           
    ======== =================
    0        Do Not Care      
    1        Other            
    2        Hard Disk Drive  
    3        Solid State Drive
    4        Hybrid           
    ======== =================
    
.. _CIM-StorageSetting-NoSinglePointOfFailure:

``boolean`` **NoSinglePointOfFailure**

    Indicates the desired value for No Single Point of Failure. Possible values are false = single point of failure, and true = no single point of failure.

    
.. _CIM-StorageSetting-PortType:

``uint16`` **PortType**

    Enumeration indicating the type of disk interfaces which may be available.

    
    ======== ===========
    ValueMap Values     
    ======== ===========
    0        Do Not Care
    1        other      
    2        SAS        
    3        SATA       
    4        SAS/SATA   
    5        FC         
    ======== ===========
    
.. _CIM-StorageSetting-ParityLayout:

``uint16`` **ParityLayout**

    ParityLayout specifies whether a parity-based storage organization is using rotated or non-rotated parity. When used in a goal setting instance, ParityLayout is the desired value. It MUST be set to NULL if the scoping StorageCapablities indicates that it is not supported in this context. If the property is supported, and is part of StorageSettingWithHints it MAY be set to NULL. If used it will constrain the effects of Hint selections. When used in a Setting instance associated to a Volume, this property indicates the specific value that the Volume was created with.

    
    ======== ==================
    ValueMap Values            
    ======== ==================
    1        Non-rotated Parity
    2        Rotated Parity    
    ======== ==================
    
.. _CIM-StorageSetting-DataOrganization:

``uint16`` **DataOrganization**

    Type of data organization used.

    
    ======== ==============
    ValueMap Values        
    ======== ==============
    0        Other         
    1        Unknown       
    2        Fixed Block   
    3        Variable Block
    4        Count Key Data
    ======== ==============
    
.. _CIM-StorageSetting-PackageRedundancyMax:

``uint16`` **PackageRedundancyMax**

    PackageRedundancyMax describes the maximum number of redundant packages to be used. For example, in the storage domain, package redundancy describes how many disk spindles can fail without data loss including, at most, one spare. An example would be RAID5 with a spare disk which would have a PackageRedundancy of 2. Possible values are 0 to n. The desired redundancy is specified using PackageRedundancyGoal, while the minimum is defined by PackageRedundancyMin.

    
.. _CIM-StorageSetting-UserDataStripeDepthMin:

``uint64`` **UserDataStripeDepthMin**

    UserDataStripeDepth describes the number of bytes forming a strip in common striping-based storage organizations. The strip is defined as the size of the portion of a stripe that lies on one extent. Thus, ExtentStripeLength * UserDataStripeDepth will yield the size of one stripe of user data. When used in a goal setting instance, UserDataStripeDepthMin is the minimum acceptable value. The desired Stripe Depth is specified using UserDataStripeDepth, while the maximum is defined by UserDataStripeDepthMax. UserDataStripeDepthMin MUST be set to NULL if the scoping StorageCapablities indicates that it is not supported in this context. If the property is supported, and is part of StorageSettingWithHints it MAY be set to NULL. If used it will constrain the effects of Hint selections. When used in a Setting instance associated to a Volume, this property is set to the specific value of UserDataStripeDepth.

    
.. _CIM-StorageSetting-EmulatedDevice:

``string`` **EmulatedDevice**

    Specifies the specific device (e.g., 3380 or 3390) that is emulated by the volume.

    
.. _CIM-StorageSetting-CompressionRate:

``uint16`` **CompressionRate**

    Indicates the desired compression for a storage element. The possible values are "None", "High", "Medium", "Low" or "Implementation Decides". If CompressedElement is set to "false", then this property should be set to 1 (None).

    
    ============ ======================
    ValueMap     Values                
    ============ ======================
    1            None                  
    2            High                  
    3            Medium                
    4            Low                   
    5            Implementation Decides
    ..           DMTF Reserved         
    32768..65535 Vendor Specific       
    ============ ======================
    
.. _CIM-StorageSetting-ThinProvisionedPoolType:

``uint16`` **ThinProvisionedPoolType**

    The type of thin provisioned pool used when StorageSetting is used as a goal for creating a thin provisioned pool. In other contexts, this property is undefined. The possibles values match the appropriate values in StorageConfigrationCapabilities.SupportedStorageElementTypes.

    
    ============= =====================================
    ValueMap      Values                               
    ============= =====================================
    7             ThinlyProvisionedAllocatedStoragePool
    8             ThinlyProvisionedQuotaStoragePool    
    9             ThinlyProvisionedLimitlessStoragePool
    ..            DMTF Reserved                        
    0x800..0xFFFF Vendor Specific                      
    ============= =====================================
    
.. _CIM-StorageSetting-FormFactorType:

``uint16`` **FormFactorType**

    Enumeration indicating the type of form factors which may be available.

    
    ======== ============
    ValueMap Values      
    ======== ============
    0        Do Not Care 
    1        Other       
    2        Not Reported
    3        5.25 inch   
    4        3.5 inch    
    5        2.5 inch    
    6        1.8 inch    
    ======== ============
    
.. _CIM-StorageSetting-PackageRedundancyGoal:

``uint16`` **PackageRedundancyGoal**

    PackageRedundancyGoal describes the desired number of redundant packages to be used. For example, in the storage domain, package redundancy describes how many disk spindles can fail without data loss including, at most, one spare. An example would be RAID5 with a spare disk which would have a PackageRedundancy of 2. Possible values are 0 to n. The bounds (max and min) for redundancy are defined using the properties, PackageRedundancyMax and PackageRedundancyMin.

    
.. _CIM-StorageSetting-SpaceLimitWarningThreshold:

``uint16`` **SpaceLimitWarningThreshold**

    If the associated storage element may dynamically consume an increasing amount of space and a space limit is enforced on the element, then a non-zero warning threshold percentage indicates when a warning indication should be generated based on the total amount of space consumed being >= (SpaceLimit*SpaceLimitWarningThreshold)/100.

    
.. _CIM-StorageSetting-RPM:

``uint32`` **RPM**

    The rotational speed of disk media wanted. a value of 0xffffffff means don't care. Values are in revolutions per minute. SSD devices shall report 0.

    
.. _CIM-StorageSetting-PersistentReplica:

``boolean`` **PersistentReplica**

    True indicates the associated replicas persist during power off or system reset. False indicates replicas lost during these events.

    
.. _CIM-StorageSetting-InitialSynchronization:

``uint16`` **InitialSynchronization**

    Not Applicable indicates that this property is not applicable to the associated storage element. Other values indicate whether or not a source element should be fully copied to a target element at the time the replication is initiated. The provider does not have to comply with the client request. These other values are defined as: 

    - "Not Managed": to start or not at initiation is up to the implementation. 

    - "Start": start replication on initiation. 

    - "Do Not Start": do not start replication on initiation.

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    0        Not Applicable 
    1        Not Managed    
    2        Start          
    3        Do Not Start   
    ..       DMTF Reserved  
    0x8000.. Vendor Specific
    ======== ===============
    
.. _CIM-StorageSetting-Encryption:

``uint16`` **Encryption**

    This property reflects support of the encryption feature implemented by some disk drives.

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Do Not Care  
    1        Not Supported
    2        Supported    
    ======== =============
    
.. _CIM-StorageSetting-StorageExtentInitialUsage:

``uint16`` **StorageExtentInitialUsage**

    The Usage value to be used when creating a new element that is derived from a StorageExtent.

    

    "Reserved to be Unrestricted Pool Contributor": Indicates the element is available and it is intended to be used as an Unrestricted Pool Contributor. Once such element is in use, the elements Usage value will change to "In use as Unrestricted Pool Contributor".

    
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
    
.. _CIM-StorageSetting-ExtentStripeLengthMin:

``uint16`` **ExtentStripeLengthMin**

    ExtentStripeLength describes the number of underlying StorageExtents across which data is striped in the common striping-based storage organizations. This is also known as the number of 'members' or 'columns'. When used in a goal setting instance, ExtentStripeLengthMin is the minimum acceptable value. The desired Stripe Length is specified using ExtentStripeLength, while the maximum is defined by ExtentStripeLengthMax. ExtentStripeLengthMin MUST be set to NULL if the scoping StorageCapablities indicates that it is not supported in this context. If the property is supported, and is part of StorageSettingWithHints it MAY be set to NULL. If used it will constrain the effects of Hint selections. When used in a Setting instance associated to a Volume, this property is set to the specific value of ExtentStripeLength.

    
.. _CIM-StorageSetting-ThinProvisionedInitialReserve:

``uint64`` **ThinProvisionedInitialReserve**

    The initial reserve being requested by the client when StorageConfigurationCapabilities is used as a parameter for creating volumes or logical disks.

    
.. _CIM-StorageSetting-DataRedundancyGoal:

``uint16`` **DataRedundancyGoal**

    DataRedundancyGoal describes the desired number of complete copies of data to be maintained. Examples would be RAID 5 where 1 copy is maintained and RAID 1 where 2 or more copies are maintained. Possible values are 1 to n. The bounds (max and min) for redundancy are defined using the properties, DataRedundancyMax and DataRedundancyMin.

    
.. _CIM-StorageSetting-ExtentStripeLength:

``uint16`` **ExtentStripeLength**

    ExtentStripeLength describes the number of underlying StorageExtents across which data is striped in the common striping-based storage organizations. This is also known as the number of 'members' or 'columns'. When used in a goal setting instance, ExtentStripeLength is the optimal desired value. The bounds (max and min) for Stripe Length are defined using the properties ExtentStripeLengthMax and ExtentStripeLengthMin. ExtentStripeLength MUST be set to NULL if the scoping StorageCapablities indicates that it is not supported in this context. ExtentStripeLength can be used in conjunction with CreateOrModifyElementFromELements to explicitly configure storage. An example would be RAID 0+1 with mirroring two stripe sets, each set being three wide. In this case CreateOrModifyElementFromElements would be passed a goal setting with DataRedundancy = 2 and ExtentStripeLength = 3. The size of the InElements array would be 6 and would contain the StorageExtents to be used to construct the StorageElement as a RAID 0+1. ExtentStripeLengthMin and ExtentStripeLengthMax are meaningless and wouldbe set to NULL. If the property is supported, and is part of StorageSettingWithHints it MAY be set to NULL. If used it will constrain the effects of Hint selections. When used in a Setting instance associated to a Volume, this property indicates the specific value that the Volume was created with, and ExtentStripeLengthMin and ExtentStripeLengthMax will be set to the same specific value.

    
.. _CIM-StorageSetting-SubsystemID:

``string`` **SubsystemID**

    This property is the Subsystem ID if the array or virtualizer supports Subsystem IDs. If they are supported they would be required on volume creation.

    
.. _CIM-StorageSetting-IncrementalDeltas:

``boolean`` **IncrementalDeltas**

    True indicates delta replicas associated with the source element associated with this settingdata are incrementally dependent. Only the oldest replica in the set may be deleted or resynced.

    
.. _CIM-StorageSetting-StoragePoolInitialUsage:

``uint16`` **StoragePoolInitialUsage**

    The Usage value to be used when creating a new StoragePool.

    
    ============ ==============================================
    ValueMap     Values                                        
    ============ ==============================================
    1            Other                                         
    2            Unrestricted                                  
    3            Reserved for ComputerSystem (the block server)
    4            Reserved as a Delta Replica Container         
    5            Reserved for Migration Services               
    6            Reserved for Local Replication Services       
    7            Reserved for Remote Replication Services      
    8            Reserved for Sparing                          
    ..           DMTF Reserved                                 
    32768..65535 Vendor Reserved                               
    ============ ==============================================
    
.. _CIM-StorageSetting-ReplicationPriority:

``uint16`` **ReplicationPriority**

    Not Applicable indicates that this property is not applicable to the associated storage element. Other values indicate the relative priority of background Replication I/O operations relative to host I/O operations. These other values are: 

    - "Low": Replication engine I/O lower priority than host I/O. 

    - "Same": Replication engine I/O has the same priority as host I/O. 

    - "High": Replication engine I/O has higher priority than host I/O.

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    0        Not Applicable 
    1        Not Managed    
    2        Low            
    3        Same           
    4        High           
    ..       DMTF Reserved  
    0x8000.. Vendor Specific
    ======== ===============
    
.. _CIM-StorageSetting-ChangeableType:

``uint16`` **ChangeableType**

    Enumeration indicating the type of setting. "Fixed - Not Changeable" settings are primordial. These setting are defined at the implementor of the class. "Changeable - Transient" is the type of setting produced by the "CreateSetting" method. A client can subsequently request that the implementation persist the generated and potentially modified setting indefinately. Only a "Changeable - Transient" setting SHALL be converted to a "Changeable = Persistent" setting; the setting SHALL NOT be changed back.

    
    ======== =======================
    ValueMap Values                 
    ======== =======================
    0        Fixed - Not Changeable 
    1        Changeable - Transient 
    2        Changeable - Persistent
    ======== =======================
    
.. _CIM-StorageSetting-DeltaReservationMin:

``uint8`` **DeltaReservationMin**

    DeltaReservationMin is a number between 1 (1%) and a 100 (100%) which specifies the minimum amount of space that should be reserved in a replica for caching changes. For a complete copy this would be 100%. The desired reservation is specified using DeltaReservationGoal, while the maximum is defined by DeltaReservationMax.

    
.. _CIM-StorageSetting-CUImage:

``string`` **CUImage**

    This property is the Node Element Descriptor of the Control Unit Image (this property is required for CKD StorageVolume). It is not required for LogicalDisks.

    
.. _CIM-StorageSetting-UserDataStripeDepthMax:

``uint64`` **UserDataStripeDepthMax**

    UserDataStripeDepth describes the number of bytes forming a strip in common striping-based storage organizations. The strip is defined as the size of the portion of a stripe that lies on one extent. Thus, ExtentStripeLength * UserDataStripeDepth will yield the size of one stripe of user data. When used in a goal setting instance, UserDataStripeDepthMax is the maximum acceptable value. The desired Stripe Depth is specified using UserDataStripeDepthGoal, while the minimum is defined by UserDataStripeDepthMin. UserDataStripeDepthMax MUST be set to NULL if the scoping StorageCapablities indicates that it is not supported in this context. If the property is supported, and is part of StorageSettingwWithHints it MAY be set to NULL. If used it will constrain the effects of Hint selections. When used in a Setting instance associated to a Volume, this property is set to the specific value of UserDataStripeDepth.

    
.. _CIM-StorageSetting-SpaceLimit:

``uint64`` **SpaceLimit**

    SpaceLimit is the consumption limit for the allocated storage element from all associated StoragePools. If asserted, then the assumption is that the storage element can grow, (for instance an element representing the storage for a delta replica). 

    If SpaceLimit is greater than zero, the space consumed by the storage element shall not exceed the value of SpaceLimit. 

    If SpaceLimit = 0 (the default) then no limits are asserted on the amount of space consumed.

    
.. _CIM-StorageSetting-ExtentStripeLengthMax:

``uint16`` **ExtentStripeLengthMax**

    ExtentStripeLength describes the number of underlying StorageExtents across which data is striped in the common striping-based storage organizations. This is also known as the number of 'members' or 'columns'. When used in a goal setting instance, ExtentStripeLengthMax is the maximum acceptable value. The desired Stripe Length is specified using ExtentStripeLength, while the minimum is defined by ExtentStripeLengthMin. ExtentStripeLengthMax MUST be set to NULL if the scoping StorageCapablities indicates that it is not supported in this context. If the property is supported, and is part of StorageSettingWithHints it MAY be set to NULL. If used it will constrain the effects of Hint selections. When used in a Setting instance associated to a Volume, this property is set to the specific value of ExtentStripeLength.

    
.. _CIM-StorageSetting-CompressedElement:

``boolean`` **CompressedElement**

    The CompressedElement property indicates whether or not compression of the element is being requested. When set to true, compression is being requested. When set to false, compression is not being requested.

    
.. _CIM-StorageSetting-DeltaReservationMax:

``uint8`` **DeltaReservationMax**

    DeltaReservationMax is a number between 1 (1%) and a 100 (100%) which specifies the maximum amount of space that should be reserved in a replica for caching changes. For a complete copy this would be 100%. The desired reservation is specified using DeltaReservationGoal, while the minimum is defined by DeltaReservationMin.

    
.. _CIM-StorageSetting-DataRedundancyMax:

``uint16`` **DataRedundancyMax**

    DataRedundancyMax describes the maximum number of complete copies of data to be maintained. Examples would be RAID 5 where 1 copy is maintained and RAID 1 where 2 or more copies are maintained. Possible values are 1 to n. The desired redundancy is specified using DataRedundancyGoal, while the minimum is defined by DataRedundancyMin.

    
.. _CIM-StorageSetting-UserDataStripeDepth:

``uint64`` **UserDataStripeDepth**

    UserDataStripeDepth describes the number of bytes forming a strip in common striping-based storage organizations. The strip is defined as the size of the portion of a stripe that lies on one extent. Thus, ExtentStripeLength * UserDataStripeDepth will yield the size of one stripe of user data. When used in a goal setting instance, UserDataStripeDepth is the optimal desired value. The bounds (max and min) for Stripe Depth are defined using the properties UserDataStripeDepthMax and UserDataStripeDepthMin. UserDataStripeDepth MUST be set to NULL if the scoping StorageCapablities indicates that it is not supported in this context. If the property is supported, and is part of StorageSettingWithHints it MAY be set to NULL. If used it will constrain the effects of Hint selections. When used in a Setting instance associated to a Volume, this property indicates the specific value that the Volume was created with, and UserDataStripeDepthMin and UserDataStripeDepthMax will be set to the same specific value.

    
.. _CIM-StorageSetting-PackageRedundancyMin:

``uint16`` **PackageRedundancyMin**

    PackageRedundancyMin describes the minimum number of redundant packages to be used. For example, in the storage domain, package redundancy describes how many disk spindles can fail without data loss including, at most, one spare. An example would be RAID5 with a spare disk which would have a PackageRedundancy of 2. Possible values are 0 to n. The desired redundancy is specified using PackageRedundancyGoal, while the maximum is defined by PackageRedundancyMax.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`InstanceID <CIM-SettingData-InstanceID>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`ConfigurationName <CIM-SettingData-ConfigurationName>`
| ``string`` :ref:`SoOrgID <CIM-SettingData-SoOrgID>`
| ``string`` :ref:`ElementName <CIM-SettingData-ElementName>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`SoID <CIM-SettingData-SoID>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string[]`` :ref:`ComponentSetting <CIM-SettingData-ComponentSetting>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

