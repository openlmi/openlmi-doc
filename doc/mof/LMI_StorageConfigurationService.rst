.. _LMI-StorageConfigurationService:

LMI_StorageConfigurationService
-------------------------------

Class reference
===============
Subclass of :ref:`CIM_StorageConfigurationService <CIM-StorageConfigurationService>`

This service allows the active management of a Storage Server. It allows jobs to be started for the creation, modification and deletion of storage objects (StoragePools, StorageVolumes and LogicalDisks).



For now, it supports Volume Group creation and modification (CreateOrModifyStoragePool), allocation/modification of Logical Volume (CreateOrModifyElementFromStoragePool), Creation of MD RAID array () and destruction of all this (DeleteStoragePool, ReturnToStoragePool, ). 

In future, it may support creation of MD RAID containers (i.e. another kind of storage pools), allocation of MD RAIDs from these containers, snapshots of Logical Volumes (AttachReplica), advanced Logical Volumes (for example with RAID characteristics), thin pools and this Logical Volumes and so on.


Key properties
^^^^^^^^^^^^^^

| :ref:`Name <CIM-Service-Name>`
| :ref:`SystemName <CIM-Service-SystemName>`
| :ref:`SystemCreationClassName <CIM-Service-SystemCreationClassName>`
| :ref:`CreationClassName <CIM-Service-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-StorageConfigurationService-HealthState:

``uint16`` **HealthState**

    Indicates the current health of the element. This attribute expresses the health of this element but not necessarily that of its subcomponents. The possible values are 0 to 30, where 5 means the element is entirely healthy and 30 means the element is completely non-functional. The following continuum is defined: 

    "Non-recoverable Error" (30) - The element has completely failed, and recovery is not possible. All functionality provided by this element has been lost. 

    "Critical Failure" (25) - The element is non-functional and recovery might not be possible. 

    "Major Failure" (20) - The element is failing. It is possible that some or all of the functionality of this component is degraded or not working. 

    "Minor Failure" (15) - All functionality is available but some might be degraded. 

    "Degraded/Warning" (10) - The element is in working order and all functionality is provided. However, the element is not working to the best of its abilities. For example, the element might not be operating at optimal performance or it might be reporting recoverable errors. 

    "OK" (5) - The element is fully functional and is operating within normal operational parameters and without error. 

    "Unknown" (0) - The implementation cannot report on HealthState at this time. 

    DMTF has reserved the unused portion of the continuum for additional HealthStates in the future.

    
    ============ =====================
    ValueMap     Values               
    ============ =====================
    0            Unknown              
    5            OK                   
    10           Degraded/Warning     
    15           Minor failure        
    20           Major failure        
    25           Critical failure     
    30           Non-recoverable error
    ..           DMTF Reserved        
    32768..65535 Vendor Specific      
    ============ =====================
    
.. _LMI-StorageConfigurationService-Started:

``boolean`` **Started**

    Started is a Boolean that indicates whether the Service has been started (TRUE), or stopped (FALSE).

    
.. _LMI-StorageConfigurationService-PrimaryStatus:

``uint16`` **PrimaryStatus**

    PrimaryStatus provides a high level status value, intended to align with Red-Yellow-Green type representation of status. It should be used in conjunction with DetailedStatus to provide high level and detailed health status of the ManagedElement and its subcomponents. 

    PrimaryStatus consists of one of the following values: Unknown, OK, Degraded or Error. "Unknown" indicates the implementation is in general capable of returning this property, but is unable to do so at this time. 

    "OK" indicates the ManagedElement is functioning normally. 

    "Degraded" indicates the ManagedElement is functioning below normal. 

    "Error" indicates the ManagedElement is in an Error condition.

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    0        Unknown        
    1        OK             
    2        Degraded       
    3        Error          
    ..       DMTF Reserved  
    0x8000.. Vendor Reserved
    ======== ===============
    
.. _LMI-StorageConfigurationService-EnabledDefault:

``uint16`` **EnabledDefault**

    An enumerated value indicating an administrator's default or startup configuration for the Enabled State of an element. By default, the element is "Enabled" (value=2).

    
    ============ ===================
    ValueMap     Values             
    ============ ===================
    2            Enabled            
    3            Disabled           
    5            Not Applicable     
    6            Enabled but Offline
    7            No Default         
    9            Quiesce            
    ..           DMTF Reserved      
    32768..65535 Vendor Reserved    
    ============ ===================
    
.. _LMI-StorageConfigurationService-EnabledState:

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
    
.. _LMI-StorageConfigurationService-StartMode:

``string`` **StartMode**

    **Deprecated!** 
    Note: The use of this element is deprecated in lieu of the EnabledDefault property that is inherited from EnabledLogicalElement. The EnabledLogicalElement addresses the same semantics. The change to a uint16 data type was discussed when CIM V2.0 was defined. However, existing V1.0 implementations used the string property. To remain compatible with those implementations, StartMode was grandfathered into the schema. Use of the deprecated qualifier allows the maintenance of the existing property but also permits an improved, clarified definition using EnabledDefault. 

    Deprecated description: StartMode is a string value that indicates whether the Service is automatically started by a System, an Operating System, and so on, or is started only upon request.

    
.. _LMI-StorageConfigurationService-OperationalStatus:

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
    

Local methods
^^^^^^^^^^^^^

    .. _LMI-StorageConfigurationService-DeleteMDRAID:

``uint32`` **DeleteMDRAID** (:ref:`LMI_MDRAIDStorageExtent <LMI-MDRAIDStorageExtent>` TheElement, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job)

    Delete MD RAID array. All members are detached from the array and all RAID metadata are erased.

    
    ============ =======================================
    ValueMap     Values                                 
    ============ =======================================
    0            Completed with No Error                
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
    
        *IN* :ref:`LMI_MDRAIDStorageExtent <LMI-MDRAIDStorageExtent>` **TheElement**
            The MD RAID device to destroy.

            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
    
    .. _LMI-StorageConfigurationService-DeleteLV:

``uint32`` **DeleteLV** (:ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`LMI_LVStorageExtent <LMI-LVStorageExtent>` TheElement)

    Start a job to delete a  Logical Volume. If 0 is returned, the function completed successfully and no ConcreteJob was required. If 4096/0x1000 is returned, a ConcreteJob will be started to delete the element. A reference to the Job is returned in the Job parameter.

    This method is alias of ReturnToStoragePool().

    
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
    4097..32767  Method Reserved                        
    32768..65535 Vendor Specific                        
    ============ =======================================
    
    **Parameters**
    
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *IN* :ref:`LMI_LVStorageExtent <LMI-LVStorageExtent>` **TheElement**
            Reference to the element to return to the StoragePool.

            
        
    
    .. _LMI-StorageConfigurationService-CreateOrModifyThinPool:

``uint32`` **CreateOrModifyThinPool** (``string`` ElementName, :ref:`LMI_VGStorageSetting <LMI-VGStorageSetting>` Goal, :ref:`LMI_VGStoragePool <LMI-VGStoragePool>` InPool, :ref:`LMI_VGStoragePool <LMI-VGStoragePool>` Pool, ``uint64`` Size, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job)

    Create or modify Thin Pool. This method is shortcut to CreateOrModifyStoragePool with the right Goal. Lazy applications can use this method to create or modify thin pools, without calculation of the Goal setting.

    
    ======== =======================================
    ValueMap Values                                 
    ======== =======================================
    0        Job Completed with No Error            
    1        Not Supported                          
    2        Unknown                                
    3        Timeout                                
    4        Failed                                 
    5        Invalid Parameter                      
    6        In Use                                 
    4096     Method Parameters Checked - Job Started
    4097     Size Not Supported                     
    ======== =======================================
    
    **Parameters**
    
        *IN* ``string`` **ElementName**
            Name of the thin pool. If this parameter is not provided, implementation will choose on its own when creating the device.

            
        
        *IN* :ref:`LMI_VGStorageSetting <LMI-VGStorageSetting>` **Goal**
            Currently not supported.

            
        
        *IN* :ref:`LMI_VGStoragePool <LMI-VGStoragePool>` **InPool**
            The volume group from which the thin pool should be allocated.

            
        
        *IN*, *OUT* :ref:`LMI_VGStoragePool <LMI-VGStoragePool>` **Pool**
            On input: thin pool to modify. Do not use this parameter when creating a thin pool.

            On output: the created or modified thin pool.

            
        
        *IN*, *OUT* ``uint64`` **Size**
            Physical size of the thin pool. The pool can store at most Size bytes of data.

            On input, only used when creating a ThinPool.

            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
    
    .. _LMI-StorageConfigurationService-ReturnToStoragePool:

``uint32`` **ReturnToStoragePool** (:ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`CIM_LogicalElement <CIM-LogicalElement>` TheElement)

    Start a job to delete an element previously created from a StoragePool. The freed space is returned to the source StoragePool. If 0 is returned, the function completed successfully and no ConcreteJob was required. If 4096/0x1000 is returned, a ConcreteJob will be started to delete the element. A reference to the Job is returned in the Job parameter.

    
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
    4097..32767  Method Reserved                        
    32768..65535 Vendor Specific                        
    ============ =======================================
    
    **Parameters**
    
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *IN* :ref:`CIM_LogicalElement <CIM-LogicalElement>` **TheElement**
            Reference to the element to return to the StoragePool.

            
        
    
    .. _LMI-StorageConfigurationService-CreateOrModifyVG:

``uint32`` **CreateOrModifyVG** (``string`` ElementName, :ref:`LMI_VGStorageSetting <LMI-VGStorageSetting>` Goal, :ref:`CIM_StorageExtent[] <CIM-StorageExtent>` InExtents, :ref:`LMI_VGStoragePool <LMI-VGStoragePool>` Pool, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, ``uint64`` Size)

    Create or modify Volume Group. This method is shortcut to CreateOrModifyStoragePool with the right Goal. Lazy applications can use this method to create or modify VGs, without calculation of the Goal setting.

    
    ======== =======================================
    ValueMap Values                                 
    ======== =======================================
    0        Job Completed with No Error            
    1        Not Supported                          
    2        Unknown                                
    3        Timeout                                
    4        Failed                                 
    5        Invalid Parameter                      
    6        In Use                                 
    4096     Method Parameters Checked - Job Started
    4097     Size Not Supported                     
    ======== =======================================
    
    **Parameters**
    
        *IN* ``string`` **ElementName**
            Requested volume group name. If this parameter is not provided, implementation will choose on its own when creating the device.

            When modifying a Volume Group, the VG will be renamed to this name.

            
        
        *IN* :ref:`LMI_VGStorageSetting <LMI-VGStorageSetting>` **Goal**
            Only for advanced use, simple application should not set this parameter.

            
        
        *IN* :ref:`CIM_StorageExtent[] <CIM-StorageExtent>` **InExtents**
            List of all Physical Volumes of the VG.

            When creating a VG, these devices will be PVs of the VG.

            When modifying a VG, this is new list of PVs of the VG. Any existing PVs, which are not listed in InExtents, will be removed from the VG. Any devices, which are listed in InExtents and are not PVs of the VG will be added to the VG.

            
        
        *IN*, *OUT* :ref:`LMI_VGStoragePool <LMI-VGStoragePool>` **Pool**
            On input: VG to modify. Do not use this parameter when creating a VG.

            On output: the created or modified VG.

            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *OUT* ``uint64`` **Size**
            Size of the volume group.

            
        
    
    .. _LMI-StorageConfigurationService-CreateOrModifyLV:

``uint32`` **CreateOrModifyLV** (``string`` ElementName, ``uint64`` Size, :ref:`LMI_VGStoragePool <LMI-VGStoragePool>` InPool, :ref:`LMI_LVStorageSetting <LMI-LVStorageSetting>` Goal, :ref:`LMI_LVStorageExtent <LMI-LVStorageExtent>` TheElement, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job)

    Create or modify Logical Volume. This method is shortcut to CreateOrModifyElementFromStoragePool with the right Goal. Lazy applications can use this method to create or modify LVs, without calculation of the Goal setting.

    
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
    
        *IN* ``string`` **ElementName**
            Requested Logical Volume name. If this parameter is not provided, implementation will choose on its own when creating the device.

            When modifying a LV, the LV will be renamed to this name.

            
        
        *IN*, *OUT* ``uint64`` **Size**
            Requested LV size. It will be rounded to multiples of VG's ExtentSize.

            When used when modifying a LV, this LV will be resized to this size.

            Only growing of LVs is supported, shrinking is not supported now.

            
        
        *IN* :ref:`LMI_VGStoragePool <LMI-VGStoragePool>` **InPool**
            Used only when creating a LV. This parameter specifies from which VG should be the LV allocated.

            
        
        *IN* :ref:`LMI_LVStorageSetting <LMI-LVStorageSetting>` **Goal**
            Only for advanced use, simple application should not set this parameter.

            
        
        *IN*, *OUT* :ref:`LMI_LVStorageExtent <LMI-LVStorageExtent>` **TheElement**
            On input: LV to modify. Do not use this parameter when creating a LV.

            On output: the created or modified LV.

            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
    
    .. _LMI-StorageConfigurationService-CreateOrModifyElementFromStoragePool:

``uint32`` **CreateOrModifyElementFromStoragePool** (``string`` ElementName, ``uint16`` ElementType, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`CIM_ManagedElement <CIM-ManagedElement>` Goal, ``uint64`` Size, :ref:`CIM_StoragePool <CIM-StoragePool>` InPool, :ref:`CIM_LogicalElement <CIM-LogicalElement>` TheElement)

    Start a job to create (or modify) a Logical Volume from a LMI_StoragePool. One of the parameters for this method is Size. As an input parameter, Size specifies the desired size of the element. As an output parameter, it specifies the size achieved. The Size is rounded to extent size of the Volume Group. Space is taken from the input StoragePool. The desired settings for the element are specified by the Goal parameter. If the requested size cannot be created, no action will be taken, and the Return Value will be 4097/0x1001. Also, the output value of Size is set to the nearest possible size. 

    This method supports renaming or resizing of a Logical Volume.

    If 0 is returned, the function completed successfully and no ConcreteJob instance was required. If 4096/0x1000 is returned, a ConcreteJob will be started to create the element. The Job's reference will be returned in the output parameter Job.

    
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
    
        *IN* ``string`` **ElementName**
            A end user relevant name for the element being created, i.e. name of the Logical Volume. If NULL, then a system supplied default name can be used. The value will be stored in the 'ElementName' property for the created element. If not NULL, this parameter will supply a new name when modifying an existing element.

            
        
        *IN* ``uint16`` **ElementType**
            Enumeration indicating the type of element being created or modified. 

            Only StorageExtent and ThinlyProvisionedStorageVolume are supported now. 

            If the input parameter TheElement is specified when the operation is a 'modify', this type value must match the type of that instance.

            
            ============ ==============================
            ValueMap     Values                        
            ============ ==============================
            0            Unknown                       
            1            Reserved                      
            2            StorageVolume                 
            3            StorageExtent                 
            4            LogicalDisk                   
            5            ThinlyProvisionedStorageVolume
            6            ThinlyProvisionedLogicalDisk  
            ..           DMTF Reserved                 
            32768..65535 Vendor Specific               
            ============ ==============================
            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *IN* :ref:`CIM_ManagedElement <CIM-ManagedElement>` **Goal**
            The requirements for the element to maintain. If set to a null value, the default configuration from the source pool will be used. This parameter should be a reference to a Setting or Profile appropriate to the element being created. If not NULL, this parameter will supply a new Goal when modifying an existing element.

            As we support only Volume Groups and simple Logical Volumes for now, no redundancy or stripping may be specified. Null is the safest option here.

            
        
        *IN*, *OUT* ``uint64`` **Size**
            As an input parameter Size specifies the desired size. The Size will be rounded to extent size of the Volume Group. If not NULL, this parameter will supply a new size when modifying an existing element. As an output parameter Size specifies the size achieved.

            
        
        *IN* :ref:`CIM_StoragePool <CIM-StoragePool>` **InPool**
            The Pool from which to create the element. This parameter must be set to null if the input parameter TheElement is specified (in the case of a 'modify' operation).

            
        
        *IN*, *OUT* :ref:`CIM_LogicalElement <CIM-LogicalElement>` **TheElement**
            As an input parameter: if null, creates a new element. If not null, then the method modifies the specified element. As an output parameter, it is a reference to the resulting element.

            
        
    
    .. _LMI-StorageConfigurationService-CreateOrModifyStoragePool:

``uint32`` **CreateOrModifyStoragePool** (``string`` ElementName, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`CIM_StorageSetting <CIM-StorageSetting>` Goal, ``uint64`` Size, ``string[]`` InPools, ``string[]`` InExtents, :ref:`CIM_StoragePool <CIM-StoragePool>` Pool)

    Starts a job to create (or modify) a StoragePool.Only Volume Groups can be created or modified using this method.

    LMI supports only creation of pools from whole StorageExtents, it is not possible to allocate only part of an StorageExtent.

    One of the parameters for this method is Size. As an input parameter, Size specifies the desired size of the pool. It must match sum of all input extent sizes. Error will be returned if not, with correct Size output parameter value. 

    Any InPools as parameter will result in error.

    The capability requirements that the Pool must support are defined using the Goal parameter. 

    This method supports renaming of a Volume Group and adding and removing StorageExtents to/from a Volume Group. 

    If a device is being removed from a Volume Group, all its data are automatically moved to any free Physical Volume automatically. This can be lengthy operation! Error is reported if there is no space for safe removal of the device. No data is lost when removing a device from Volume Group.

    If 0 is returned, then the task completed successfully and the use of ConcreteJob was not required. If the task will take some time to complete, a ConcreteJob will be created and its reference returned in the output parameter Job. 

    This method automatically formats the StorageExtents added to a Volume Group as Physical Volumes.

    
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
    
        *IN* ``string`` **ElementName**
            A end user relevant name for the pool being created.

            If a Volume Group is being created or modified, it is used as the Volume Group name.

            If null, then a system supplied default name will be used. The value will be stored in the 'ElementName' property for the created pool. If not null, this parameter will supply a new name when modifying an existing pool.

            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *IN* :ref:`CIM_StorageSetting <CIM-StorageSetting>` **Goal**
            Reference to an instance of StorageSetting that defines the desired capabilities of the StoragePool. If set to a null value, the default configuration from the source pool will be used. If not NULL, this parameter will supply a new Goal setting when modifying an existing pool.

            As only simple Volume Groups are supported now, no redundancy or stripping may be used. Null is the safest option here. 

            
        
        *IN*, *OUT* ``uint64`` **Size**
            As an input parameter this specifies the desired pool size in bytes. If provided, it must match sum of sizes of all input StorageExtents. 

            As an output parameter this specifies the size achieved.

            
        
        *IN* ``string[]`` **InPools**
            This parameter is not supported by LMI and must be null.

            
        
        *IN* ``string[]`` **InExtents**
            Array of strings containing representations of references to CIM_StorageExtent instances, that are used to create the Pool. 

            If a pool is being modified using this method, these StorageExtent instances are interpreted as requested members of the Volume Groups. All StorageExtents, which are members of the Volume Groups and are not listed in InExtents parameter are removed from the Volume Group. All Storage Extents, which are not members of the Volume Group and are listed in InExtents parameter are added to the Volume Group.

            If null, no extents are removed and/or added to to Volume Group.

            
        
        *IN*, *OUT* :ref:`CIM_StoragePool <CIM-StoragePool>` **Pool**
            As an input parameter: if null, creates a new StoragePool. If not null, modifies the referenced Pool. When returned, it is a reference to the resulting StoragePool.

            
        
    
    .. _LMI-StorageConfigurationService-CreateOrModifyMDRAID:

``uint32`` **CreateOrModifyMDRAID** (``uint16`` Level, ``string`` ElementName, :ref:`CIM_StorageExtent[] <CIM-StorageExtent>` InExtents, :ref:`LMI_MDRAIDStorageSetting <LMI-MDRAIDStorageSetting>` Goal, :ref:`LMI_MDRAIDStorageExtent <LMI-MDRAIDStorageExtent>` TheElement, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, ``uint64`` Size)

    Create or modify MD RAID array. This method is shortcut to CreateOrModifyElementFromElements with the right Goal. Lazy applications can use this method to create or modify MD RAID with the right level, without calculation of the Goal setting.

    Either Level or Goal must be specified. If both are specified, they must match.

    RAID modification is not yet supported.

    
    ============ =======================================
    ValueMap     Values                                 
    ============ =======================================
    0            Completed with No Error                
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
    
        *IN* ``uint16`` **Level**
            Requested RAID level.

            
            ======== ======
            ValueMap Values
            ======== ======
            0        RAID0 
            1        RAID1 
            4        RAID4 
            5        RAID5 
            6        RAID6 
            10       RAID10
            ======== ======
            
        
        *IN* ``string`` **ElementName**
            Requested MD RAID name, i.e. if /dev/md/my_name is created, the ElementName should be set to "my_name". If this parameter is not provided, implementation will choose on its own when creating the device.

            
        
        *IN* :ref:`CIM_StorageExtent[] <CIM-StorageExtent>` **InExtents**
            List of CIM_StorageExtents which should be part of the RAID. Any data of these devices will be destroyed.

            
        
        *IN* :ref:`LMI_MDRAIDStorageSetting <LMI-MDRAIDStorageSetting>` **Goal**
            Requested MD RAID setting. It's only for very advanced settings, simple applications should use Level parameter.

            
        
        *IN*, *OUT* :ref:`LMI_MDRAIDStorageExtent <LMI-MDRAIDStorageExtent>` **TheElement**
            On input: MD RAID device to modify. Do not use this parameter when creating new array.

            On output: the created MD RAID.

            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *OUT* ``uint64`` **Size**
            Size of the RAID device.

            
        
    
    .. _LMI-StorageConfigurationService-CreateOrModifyElementFromElements:

``uint32`` **CreateOrModifyElementFromElements** (``string`` ElementName, ``uint16`` ElementType, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`CIM_ManagedElement <CIM-ManagedElement>` Goal, ``uint64`` Size, :ref:`CIM_StorageExtent[] <CIM-StorageExtent>` InElements, :ref:`CIM_LogicalElement <CIM-LogicalElement>` TheElement)

    Start a job to create (or modify) a MD RAID from specified input StorageExtents. Only whole StorageExtents can be added to a RAID.

    As an input parameter, Size specifies the desired size of the element and must match size of all input StorageVolumes combined in the RAID. Use null to avoid this calculation. As an output parameter, it specifies the size achieved. 

    The desired Settings for the element are specified by the Goal parameter. 

    If 0 is returned, the function completed successfully and no ConcreteJob instance was required. If 4096/0x1000 is returned, a ConcreteJob will be started to create the element. The Job's reference will be returned in the output parameter Job.

    This method does not support MD RAID modification for now.

    
    ============ =======================================
    ValueMap     Values                                 
    ============ =======================================
    0            Completed with No Error                
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
    
        *IN* ``string`` **ElementName**
            A end user relevant name for the MD RAID, i.e. /dev/md/<ElementName>. If NULL, then a system-supplied default name can be used. The value will be stored in the 'ElementName' property for the created element. If not NULL, this parameter will supply a new name when modifying an existing element.

            
        
        *IN* ``uint16`` **ElementType**
            Enumeration indicating the type of element being created or modified. 

            Only StorageExtent is supported now.

            If the input parameter TheElement is specified when the operation is a 'modify', this type value must match the type of that instance. The actual CIM class of the created TheElement can be vendor-specific, but it must be a derived class of the appropriate CIM class -- i.e., CIM_StorageVolume, CIM_StorageExtent, CIM_LogicalDisk, or CIM_StoragePool.

            
            ============ ==============================
            ValueMap     Values                        
            ============ ==============================
            0            Unknown                       
            1            Reserved                      
            2            Storage Volume                
            3            Storage Extent                
            4            Storage Pool                  
            5            Logical Disk                  
            6            ThinlyProvisionedStorageVolume
            7            ThinlyProvisionedLogicalDisk  
            ..           DMTF Reserved                 
            32768..65535 Vendor Specific               
            ============ ==============================
            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *IN* :ref:`CIM_ManagedElement <CIM-ManagedElement>` **Goal**
            The requirements for the element to maintain. If set to a null value, the default configuration associated with the Service will be used. This parameter should be a reference to a Setting, SettingData, or Profile appropriate to the element being created. If not NULL, this parameter will supply a new Goal when modifying an existing element.

            
        
        *IN*, *OUT* ``uint64`` **Size**
            As an input parameter Size specifies the desired size. If not NULL, this parameter  must match resulting size of  the RAID. As an output parameter Size specifies the size achieved.

            
        
        *IN* :ref:`CIM_StorageExtent[] <CIM-StorageExtent>` **InElements**
            Array of references to storage element instances that are used to create or modify TheElement.

            
        
        *IN*, *OUT* :ref:`CIM_LogicalElement <CIM-LogicalElement>` **TheElement**
            As an input parameter: if null, creates a new element. If not null, then the method modifies the specified element. As an output parameter, it is a reference to the resulting element.

            
        
    
    .. _LMI-StorageConfigurationService-CreateOrModifyThinLV:

``uint32`` **CreateOrModifyThinLV** (``string`` ElementName, :ref:`LMI_VGStoragePool <LMI-VGStoragePool>` ThinPool, :ref:`LMI_LVStorageExtent <LMI-LVStorageExtent>` TheElement, ``uint64`` Size, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job)

    **Parameters**
    
        *IN* ``string`` **ElementName**
            Requested Thin Logical Volume name. If this parameter is not provided, implementation will choose on it's own when creating the device.

            
        
        *IN* :ref:`LMI_VGStoragePool <LMI-VGStoragePool>` **ThinPool**
            Used only when creating a thin volume. This parameter specifies from which thinpool should be the thin volume allocated.

            
        
        *IN*, *OUT* :ref:`LMI_LVStorageExtent <LMI-LVStorageExtent>` **TheElement**
            On input: LV to modify. Do not use this parameter when creating a LV.

            On output: the created or modified LV.

            
        
        *IN*, *OUT* ``uint64`` **Size**
            Requested thin LV size. It will be rounded to multiples of VG's ExtentSize.

            In contrast to the size of a thin pool, this size is logical. It can be much higher than the physical size of the underlying storage.

            Modification is not supported.

            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
    
    .. _LMI-StorageConfigurationService-DeleteVG:

``uint32`` **DeleteVG** (:ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`CIM_StoragePool <CIM-StoragePool>` Pool)

    Start a job to delete a Volume Group. If 0 is returned, the function completed successfully, and no ConcreteJob was required. If 4096/0x1000 is returned, a ConcreteJob will be started to delete the StoragePool. A reference to the Job is returned in the Job parameter.

    
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
    4097..32767  Method Reserved                        
    32768..65535 Vendor Specific                        
    ============ =======================================
    
    **Parameters**
    
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *IN* :ref:`CIM_StoragePool <CIM-StoragePool>` **Pool**
            Reference to the pool to delete.

            
        
    
    .. _LMI-StorageConfigurationService-DeleteStoragePool:

``uint32`` **DeleteStoragePool** (:ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`CIM_StoragePool <CIM-StoragePool>` Pool)

    Start a job to delete a StoragePool. The freed space is returned source StoragePools (indicated by AllocatedFrom StoragePool) or back to underlying storage extents. If 0 is returned, the function completed successfully, and no ConcreteJob was required. If 4096/0x1000 is returned, a ConcreteJob will be started to delete the StoragePool. A reference to the Job is returned in the Job parameter.

    
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
    4097..32767  Method Reserved                        
    32768..65535 Vendor Specific                        
    ============ =======================================
    
    **Parameters**
    
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *IN* :ref:`CIM_StoragePool <CIM-StoragePool>` **Pool**
            Reference to the pool to delete.

            
        
    
    .. _LMI-StorageConfigurationService-LMI-ScsiScan:

``uint32`` **LMI_ScsiScan** (:ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job)

    This method requests that the system rescan SCSI devices for changes in their configuration. This method may also be used on a storage appliance to force rescanning of attached SCSI devices. 

    

    This operation can be disruptive.

    

    The method is LMI version of DMTF's ScsiScan(), just with '4096' as 'Method Parameters Checked - Job Started' return value. Also, the method parameters were trimmed, we may extend it to support complete DMTF ScsiScan parameters.

    
    ============ ========================================
    ValueMap     Values                                  
    ============ ========================================
    0            Success                                 
    1            Not Supported                           
    2            Unknown                                 
    3            Timeout                                 
    4            Failed                                  
    5            Invalid Parameter                       
    6..4095      DMTF Reserved                           
    4096         Method Parameters Checked - Job Started 
    4097         Invalid Initiator                       
    4098         No matching target found                
    4099         No matching LUs found                   
    4100         Prohibited by name binding configuration
    ..           DMTF Reserved                           
    32768..65535 Vendor Specific                         
    ============ ========================================
    
    **Parameters**
    
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`SystemName <CIM-Service-SystemName>`
| ``string`` :ref:`LoSID <CIM-Service-LoSID>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`Name <CIM-Service-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string`` :ref:`LoSOrgID <CIM-Service-LoSOrgID>`
| ``string`` :ref:`PrimaryOwnerContact <CIM-Service-PrimaryOwnerContact>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`SystemCreationClassName <CIM-Service-SystemCreationClassName>`
| ``string`` :ref:`CreationClassName <CIM-Service-CreationClassName>`
| ``string`` :ref:`PrimaryOwnerName <CIM-Service-PrimaryOwnerName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`AttachReplica <CIM-StorageConfigurationService-AttachReplica>`
| :ref:`CreateOrModifyReplicationPipe <CIM-StorageConfigurationService-CreateOrModifyReplicationPipe>`
| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`
| :ref:`AttachOrModifyReplica <CIM-StorageConfigurationService-AttachOrModifyReplica>`
| :ref:`CreateElementsFromStoragePools <CIM-StorageConfigurationService-CreateElementsFromStoragePools>`
| :ref:`ScsiScan <CIM-StorageConfigurationService-ScsiScan>`
| :ref:`StopService <CIM-Service-StopService>`
| :ref:`CreateReplicationBuffer <CIM-StorageConfigurationService-CreateReplicationBuffer>`
| :ref:`GetElementsBasedOnUsage <CIM-StorageConfigurationService-GetElementsBasedOnUsage>`
| :ref:`StartService <CIM-Service-StartService>`
| :ref:`CreateReplica <CIM-StorageConfigurationService-CreateReplica>`
| :ref:`ChangeAffectedElementsAssignedSequence <CIM-Service-ChangeAffectedElementsAssignedSequence>`
| :ref:`AssignStorageResourceAffinity <CIM-StorageConfigurationService-AssignStorageResourceAffinity>`
| :ref:`CreateElementsFromStoragePool <CIM-StorageConfigurationService-CreateElementsFromStoragePool>`
| :ref:`ReturnElementsToStoragePool <CIM-StorageConfigurationService-ReturnElementsToStoragePool>`
| :ref:`ModifySynchronization <CIM-StorageConfigurationService-ModifySynchronization>`
| :ref:`RequestUsageChange <CIM-StorageConfigurationService-RequestUsageChange>`

