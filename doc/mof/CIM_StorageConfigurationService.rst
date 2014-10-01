.. _CIM-StorageConfigurationService:

CIM_StorageConfigurationService
-------------------------------

Class reference
===============
Subclass of :ref:`CIM_Service <CIM-Service>`

This service allows the active management of a Storage Server. It allows jobs to be started for the creation, modification and deletion of storage objects (StoragePools, StorageVolumes and LogicalDisks).


Key properties
^^^^^^^^^^^^^^

| :ref:`Name <CIM-Service-Name>`
| :ref:`SystemName <CIM-Service-SystemName>`
| :ref:`SystemCreationClassName <CIM-Service-SystemCreationClassName>`
| :ref:`CreationClassName <CIM-Service-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

*None*

Local methods
^^^^^^^^^^^^^

    .. _CIM-StorageConfigurationService-AttachReplica:

``uint32`` **AttachReplica** (:ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`CIM_ManagedElement <CIM-ManagedElement>` SourceElement, :ref:`CIM_ManagedElement <CIM-ManagedElement>` TargetElement, ``uint16`` CopyType)

    Create (or start a job to create) a StorageSynchronized relationship between two existing storage objects. Note that using the input parameter, CopyType, this function can be used to to create an ongoing association between the source and replica. If 0 is returned, the function completed successfully and no ConcreteJob instance is created. If 0x1000 is returned, a ConcreteJob is started, a reference to which is returned in the Job output parameter. A return value of 1 indicates the method is not supported. All other values indicate some type of error condition.

    
    ============== =======================================
    ValueMap       Values                                 
    ============== =======================================
    0              Job Completed with No Error            
    1              Not Supported                          
    2              Unspecified Error                      
    3              Timeout                                
    4              Failed                                 
    5              Invalid Parameter                      
    6              In Use                                 
    ..             DMTF Reserved                          
    0x1000         Method Parameters Checked - Job Started
    0x1001..0x7FFF Method Reserved                        
    0x8000..0xFFFF Vendor Specific                        
    ============== =======================================
    
    **Parameters**
    
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if the task completed).

            
        
        *IN* :ref:`CIM_ManagedElement <CIM-ManagedElement>` **SourceElement**
            The source storage object which may be a StorageVolume or other storage object.

            
        
        *IN* :ref:`CIM_ManagedElement <CIM-ManagedElement>` **TargetElement**
            Reference to the target storage element (i.e., the replica).

            
        
        *IN* ``uint16`` **CopyType**
            CopyType describes the type of Synchronized relationship that will be created. Values are: 

            Async: Create and maintain an asynchronous copy of the source. 

            Sync: Create and maintain a synchronized copy of the source. 

            UnSyncAssoc: Create an unsynchronized copy and maintain an association to the source. 

            UnSyncUnAssoc: Create unassociated copy of the source element.

            
            ============== ===============
            ValueMap       Values         
            ============== ===============
            2              Async          
            3              Sync           
            4              UnSyncAssoc    
            5              UnSyncUnAssoc  
            ..             DMTF Reserved  
            0x8000..0xFFFF Vendor Specific
            ============== ===============
            
        
    
    .. _CIM-StorageConfigurationService-ReturnToStoragePool:

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

            
        
    
    .. _CIM-StorageConfigurationService-CreateOrModifyReplicationPipe:

``uint32`` **CreateOrModifyReplicationPipe** (``string`` PipeElementName, :ref:`CIM_ComputerSystem <CIM-ComputerSystem>` SourceSystem, :ref:`CIM_ComputerSystem <CIM-ComputerSystem>` TargetSystem, :ref:`CIM_ProtocolEndpoint[] <CIM-ProtocolEndpoint>` SourceEndpoint, :ref:`CIM_ProtocolEndpoint[] <CIM-ProtocolEndpoint>` TargetEndpoint, ``string`` Goal, :ref:`CIM_NetworkPipe <CIM-NetworkPipe>` ReplicationPipe)

    This method establishes a peer-to-peer connection identified by a NetworkPipe element and two ProtocolEndpoint elements created by the method provider. The NetworkPipe is associated to a special peer-to-peer Network element. The provider will verify that two systems are capable of a peer relationship. If endpoints are assigned to the pipe, the same number of source and target endpoints must be supplied by the client to form a set of endpoint pairs. If ReplicationPipe is not supplied as an input parameter, a new pipe is created. If a pipe is supplied, a new set of endpoints is assigned to the existing pipe. 

    

    If Success (0) is returned, the function completed successfully. 

    

    A return value of Not Supported (1) indicates the method is not supported. 

    

    A return value of Busy (0x1000) indicates the method is not supported. 

    

    All other values indicate some type of error condition.

    
    ============== =================
    ValueMap       Values           
    ============== =================
    0              Success          
    1              Not Supported    
    2              Unspecified Error
    3              Timeout          
    4              Failed           
    5              Invalid Parameter
    ..             DMTF Reserved    
    0x1000         Busy             
    0x1001..0x7FFF Method Reserved  
    0x8000..0xFFFF Vendor Specific  
    ============== =================
    
    **Parameters**
    
        *IN* ``string`` **PipeElementName**
            A user-friendly name for the element created.

            
        
        *IN* :ref:`CIM_ComputerSystem <CIM-ComputerSystem>` **SourceSystem**
            One of the two peer systems participating in the established peer-to-peer connection. If the provider supports uni-directional connections, this must identify the system hosting replica source elements.

            
        
        *IN* :ref:`CIM_ComputerSystem <CIM-ComputerSystem>` **TargetSystem**
            One of the two peer systems participating in the established peer-to-peer connection. If the provider supports uni-directional connections, this must identify the system hosting replica target elements.

            
        
        *IN* :ref:`CIM_ProtocolEndpoint[] <CIM-ProtocolEndpoint>` **SourceEndpoint**
            References to source system endpoints/ports assigned to the pipe. If a new pipe is created, this is the initial set of endpoints assigned. If an existing pipe is modified, this set replaces the previous set. The list must be null if a provider does not allow the client to manage port assignment.

            
        
        *IN* :ref:`CIM_ProtocolEndpoint[] <CIM-ProtocolEndpoint>` **TargetEndpoint**
            References to target system endpoints/ports assigned to the pipe. If a new pipe is created, this is the initial set of endpoints assigned. If an existing pipe is modified, this set replaces the previous set. The list must be null if a provider does not allow the client to manage port assignment.

            
        
        *IN* ``string`` **Goal**
            The setting properties to be maintained for the peer-to-peer connection.

            
        
        *IN*, *OUT* :ref:`CIM_NetworkPipe <CIM-NetworkPipe>` **ReplicationPipe**
            Reference to the created or modified NetworkPipe.

            
        
    
    .. _CIM-StorageConfigurationService-AttachOrModifyReplica:

``uint32`` **AttachOrModifyReplica** (:ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`CIM_ManagedElement <CIM-ManagedElement>` SourceElement, :ref:`CIM_ManagedElement <CIM-ManagedElement>` TargetElement, ``uint16`` CopyType, ``string`` Goal, :ref:`CIM_NetworkPipe <CIM-NetworkPipe>` ReplicationPipe)

    Create (or start a job to create) a StorageSynchronized mirror relationship between two storage elements. The target element may be a local or a remote storage element. A remote mirror pair may be scoped by a peer-to-peer connection modeled as a NetworkPipe between peers. 

    

    If Job Completed with No Error (0) is returned, the function completed successfully and a ConcreteJob instance is not created. 

    

    If Method Parameters Checked - Job Started (0x1000) is returned, a ConcreteJob is started, a reference to which is returned in the Job output parameter. 

    

    A return value of Not Supported (1) indicates the method is not supported. 

    

    All other values indicate some type of error condition.

    
    ============== =======================================
    ValueMap       Values                                 
    ============== =======================================
    0              Job Completed with No Error            
    1              Not Supported                          
    2              Unspecified Error                      
    3              Timeout                                
    4              Failed                                 
    5              Invalid Parameter                      
    6              In Use                                 
    ..             DMTF Reserved                          
    0x1000         Method Parameters Checked - Job Started
    0x1001..0x7FFF Method Reserved                        
    0x8000..0xFFFF Vendor Specific                        
    ============== =======================================
    
    **Parameters**
    
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if the task completed).

            
        
        *IN* :ref:`CIM_ManagedElement <CIM-ManagedElement>` **SourceElement**
            The source storage element which may be a StorageVolume, StorageExtent, LogicalFile, FileSystem, CommonDatabase, or any other storage object. For this reason, the type is made very generic.

            
        
        *IN* :ref:`CIM_ManagedElement <CIM-ManagedElement>` **TargetElement**
            Reference to the target storage element (i.e., the replica). The target storage element which may be a StorageVolume, StorageExtent, LogicalFile, FileSystem, CommonDatabase, or any other storage object. For this reason, the type is made very generic.

            
        
        *IN* ``uint16`` **CopyType**
            CopyType describes the type of Synchronized relationship that will be created. Values are: Async: Create and maintain an asynchronous copy of the source. Sync: Create and maintain a synchronized copy of the source. UnSyncAssoc: Create an unsynchronized copy and maintain an association to the source element. 

            UnSyncUnAssoc: Create an unassociated copy of the source element. 

            UnSyncAssoc and UnSyncUnAssoc are not supported for remote mirror replicas.

            
            ============== ===============
            ValueMap       Values         
            ============== ===============
            2              Async          
            3              Sync           
            4              UnSyncAssoc    
            5              UnSyncUnAssoc  
            6..4095        DMTF Reserved  
            0x1000..0xFFFF Vendor Specific
            ============== ===============
            
        
        *IN* ``string`` **Goal**
            The StorageSetting properties to be created or modified for the target element.

            
        
        *IN* :ref:`CIM_NetworkPipe <CIM-NetworkPipe>` **ReplicationPipe**
            The NetworkPipe element that scopes the remote mirror pair. If the value is null, remote mirrors do not require a pre-established connection.

            
        
    
    .. _CIM-StorageConfigurationService-CreateElementsFromStoragePools:

``uint32`` **CreateElementsFromStoragePools** (``string[]`` ElementNames, ``uint16`` ElementType, ``uint64`` ElementCount, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`CIM_SettingData <CIM-SettingData>` Goal, ``uint64`` Size, :ref:`CIM_StoragePool[] <CIM-StoragePool>` InPools, :ref:`CIM_LogicalElement[] <CIM-LogicalElement>` TheElements)

    Start a job to create (or modify) a specified elements (for example StorageVolumes or StorageExtents) from StoragePools. One of the parameters for this method is Size. As an input parameter, Size specifies the desired size of the element. As an output parameter, it specifies the size achieved. Space is taken from the input StoragePool. The desired settings for the element are specified by the Goal parameter. If the requested size cannot be created, no action will be taken, and the Return Value will be 4097/0x1001. Also, the output value of Size is set to the nearest possible size. If 0 is returned, the function completed successfully and no ConcreteJob instance was required. If 4096/0x1000 is returned, a ConcreteJob will be started to create the element. The Job's reference will be returned in the output parameter Job. If the number of elements created is less than the number of elements requested, the return value will be 4098/0x1002.

    
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
    4098         Partially Completed Operation          
    4099..32767  Method Reserved                        
    32768..65535 Vendor Specific                        
    ============ =======================================
    
    **Parameters**
    
        *IN* ``string[]`` **ElementNames**
            One or more user relevant names for the element being created. If NULL, then system supplied default names may be used. The value will be stored in the "ElementName" property for the created element.

            
        
        *IN* ``uint16`` **ElementType**
            Enumeration indicating the type of element being created. With ElementType of "2" and "3", the implementation decides the provisioning of the element.

            
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
            7            FullyProvisionedStorageVolume 
            8            FullyProvisionedLogicalDisk   
            ..           DMTF Reserved                 
            32768..65535 Vendor Specific               
            ============ ==============================
            
        
        *IN* ``uint64`` **ElementCount**
            Count of elements to create. If null, it defaults to one element.

            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *IN* :ref:`CIM_SettingData <CIM-SettingData>` **Goal**
            The requirements for the element to maintain. If set to a null value, the default configuration from the source pool will be used. This parameter should be a reference to a Setting or Profile appropriate to the element being created.

            
        
        *IN*, *OUT* ``uint64`` **Size**
            As an input parameter Size specifies the desired size for each element created. As an output parameter Size specifies the size achieved.

            
        
        *IN* :ref:`CIM_StoragePool[] <CIM-StoragePool>` **InPools**
            The Pools from which to create the elements. If not supplied, system locates the appropriate pools.

            
        
        *OUT* :ref:`CIM_LogicalElement[] <CIM-LogicalElement>` **TheElements**
            Reference to the resulting elements.

            
        
    
    .. _CIM-StorageConfigurationService-CreateOrModifyElementFromStoragePool:

``uint32`` **CreateOrModifyElementFromStoragePool** (``string`` ElementName, ``uint16`` ElementType, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`CIM_ManagedElement <CIM-ManagedElement>` Goal, ``uint64`` Size, :ref:`CIM_StoragePool <CIM-StoragePool>` InPool, :ref:`CIM_LogicalElement <CIM-LogicalElement>` TheElement)

    Start a job to create (or modify) a specified element (for example a StorageVolume or StorageExtent) from a StoragePool. One of the parameters for this method is Size. As an input parameter, Size specifies the desired size of the element. As an output parameter, it specifies the size achieved. Space is taken from the input StoragePool. The desired settings for the element are specified by the Goal parameter. If the requested size cannot be created, no action will be taken, and the Return Value will be 4097/0x1001. Also, the output value of Size is set to the nearest possible size. If 0 is returned, the function completed successfully and no ConcreteJob instance was required. If 4096/0x1000 is returned, a ConcreteJob will be started to create the element. The Job's reference will be returned in the output parameter Job.

    
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
            A end user relevant name for the element being created. If NULL, then a system supplied default name can be used. The value will be stored in the 'ElementName' property for the created element. If not NULL, this parameter will supply a new name when modifying an existing element.

            
        
        *IN* ``uint16`` **ElementType**
            Enumeration indicating the type of element being created or modified. If the input parameter TheElement is specified when the operation is a 'modify', this type value must match the type of that instance. With ElementType of "2" and "3", the implementation decides the provisioning of the element.

            
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
            7            FullyProvisionedStorageVolume 
            8            FullyProvisionedLogicalDisk   
            ..           DMTF Reserved                 
            32768..65535 Vendor Specific               
            ============ ==============================
            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *IN* :ref:`CIM_ManagedElement <CIM-ManagedElement>` **Goal**
            The requirements for the element to maintain. If set to a null value, the default configuration from the source pool will be used. This parameter should be a reference to a Setting or Profile appropriate to the element being created. If not NULL, this parameter will supply a new Goal when modifying an existing element.

            
        
        *IN*, *OUT* ``uint64`` **Size**
            As an input parameter Size specifies the desired size. If not NULL, this parameter will supply a new size when modifying an existing element. As an output parameter Size specifies the size achieved.

            
        
        *IN* :ref:`CIM_StoragePool <CIM-StoragePool>` **InPool**
            The Pool from which to create the element. This parameter must be set to null if the input parameter TheElement is specified (in the case of a 'modify' operation).

            
        
        *IN*, *OUT* :ref:`CIM_LogicalElement <CIM-LogicalElement>` **TheElement**
            As an input parameter: if null, creates a new element. If not null, then the method modifies the specified element. As an output parameter, it is a reference to the resulting element.

            
        
    
    .. _CIM-StorageConfigurationService-CreateOrModifyStoragePool:

``uint32`` **CreateOrModifyStoragePool** (``string`` ElementName, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`CIM_StorageSetting <CIM-StorageSetting>` Goal, ``uint64`` Size, ``string[]`` InPools, ``string[]`` InExtents, :ref:`CIM_StoragePool <CIM-StoragePool>` Pool)

    Starts a job to create (or modify) a StoragePool. The StoragePool will be (or must be) scoped to the same System as this Service. One of the parameters for this method is Size. As an input parameter, Size specifies the desired size of the pool. As an output parameter, it specifies the size achieved. Space is taken from either or both of the specified input StoragePools and StorageExtents (InPools and InExtents). The capability requirements that the Pool must support are defined using the Goal parameter. If the requested pool size cannot be created, no action will be taken, the Return Value will be 4097/0x1001, and the output value of Size will be set to the nearest possible size. If 0 is returned, then the task completed successfully and the use of ConcreteJob was not required. If the task will take some time to complete, a ConcreteJob will be created and its reference returned in the output parameter Job.

    
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
            A end user relevant name for the pool being created. If NULL, then a system supplied default name can be used. The value will be stored in the 'ElementName' property for the created pool. If not NULL, this parameter will supply a new name when modifying an existing pool.

            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *IN* :ref:`CIM_StorageSetting <CIM-StorageSetting>` **Goal**
            Reference to an instance of StorageSetting that defines the desired capabilities of the StoragePool. If set to a null value, the default configuration from the source pool will be used. If not NULL, this parameter will supply a new Goal setting when modifying an existing pool.

            
        
        *IN*, *OUT* ``uint64`` **Size**
            As an input parameter this specifies the desired pool size in bytes. As an output parameter this specifies the size achieved.

            
        
        *IN* ``string[]`` **InPools**
            Array of strings containing representations of references to CIM_StoragePool instances, that are used to create the Pool or modify the source pools.

            
        
        *IN* ``string[]`` **InExtents**
            Array of strings containing representations of references to CIM_StorageExtent instances, that are used to create the Pool or modify the source extents.

            
        
        *IN*, *OUT* :ref:`CIM_StoragePool <CIM-StoragePool>` **Pool**
            As an input parameter: if null, creates a new StoragePool. If not null, modifies the referenced Pool. When returned, it is a reference to the resulting StoragePool.

            
        
    
    .. _CIM-StorageConfigurationService-ScsiScan:

``uint32`` **ScsiScan** (:ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, ``uint16`` ConnectionType, ``string`` OtherConnectionType, :ref:`CIM_SCSIProtocolEndpoint[] <CIM-SCSIProtocolEndpoint>` Initiators, ``string[]`` Targets, ``string[]`` LogicalUnits)

    This method requests that the system rescan SCSI devices for changes in their configuration. If called on a general-purpose host, the changes are reflected in the list of devices available to applications (for example, the UNIX 'device tree'. This method may also be used on a storage appliance to force rescanning of attached SCSI devices. 

    

    This operation can be disruptive; optional parameters allow the caller to limit the scan to a single or set of SCSI device elements. All parameters are optional; if parameters other Job are passed in as null, a full scan is invoked.

    
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
    4096         Invalid connection type                 
    4097         Invalid Initiator                       
    4098         No matching target found                
    4099         No matching LUs found                   
    4100         Prohibited by name binding configuration
    ..           DMTF Reserved                           
    32768..65535 Vendor Specific                         
    ============ ========================================
    
    **Parameters**
    
        *IN*, *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *IN* ``uint16`` **ConnectionType**
            The type of connection, constrains the scan to initiator ports of this type. Only used if the Initiators parameter is null.

            
            ======== =============
            ValueMap Values       
            ======== =============
            1        Other        
            2        Fibre Channel
            3        Parallel SCSI
            4        SSA          
            5        IEEE 1394    
            6        RDMA         
            7        iSCSI        
            8        SAS          
            9        ADT          
            ======== =============
            
        
        *IN* ``string`` **OtherConnectionType**
            The connection type, if the ConnectionType parameter is "Other".

            
        
        *IN* :ref:`CIM_SCSIProtocolEndpoint[] <CIM-SCSIProtocolEndpoint>` **Initiators**
            A list of references to initiators. Scanning will be limited to SCSI targets attached to these initiators. If this parameter is null and connection is specified, all initiators of that connection type are scanned. If this parameter and ConnectionType are null, all targets on all system initiators are probed.

            
        
        *IN* ``string[]`` **Targets**
            A list of names or numbers for targets. These should be formatted to match the appropriate connection type, For example, PortWWNs would be specified for Fibre Channel targets.

            
        
        *IN* ``string[]`` **LogicalUnits**
            A list of SCSI logical unit numbers representing logical units hosted on the targets specified in the Targets argument.

            
        
    
    .. _CIM-StorageConfigurationService-CreateOrModifyElementFromElements:

``uint32`` **CreateOrModifyElementFromElements** (``string`` ElementName, ``uint16`` ElementType, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`CIM_ManagedElement <CIM-ManagedElement>` Goal, ``uint64`` Size, :ref:`CIM_StorageExtent[] <CIM-StorageExtent>` InElements, :ref:`CIM_LogicalElement <CIM-LogicalElement>` TheElement)

    Start a job to create (or modify) a specified storage element from specified input StorageExtents. The created or modified storage element can be a StorageExtent, StorageVolume, LogicalDisk, or StoragePool. An input list of InElements must be specified. The GetAvailableExtents method can be used to get a list of valid extents that can be used to achieve a desired goal. Validity of the extents is determined by the implementation. As an input parameter, Size specifies the desired size of the element. As an output parameter, it specifies the size achieved. Space is taken from the input InElements. The desired Settings for the element are specified by the Goal parameter. If the size of Extents passed is less than the size requested, then the capacity is drawn from the extents in the order, left to right, that the Extents were specified. The partial consumption of an Extent is represented by an Extent for the capacity used and an Extent for the capacity not used. If the Size is NULL, then a configuration using all Extents passed will be attempted. If the requested size cannot be created, no action will be taken, and the Return Value will be 4097/0x1001. Also, the output value of Size is set to the nearest possible size. If 0 is returned, the function completed successfully and no ConcreteJob instance was required. If 4096/0x1000 is returned, a ConcreteJob will be started to create the element. The Job's reference will be returned in the output parameter Job.

    
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
            A end user relevant name for the element being created. If NULL, then a system-supplied default name can be used. The value will be stored in the 'ElementName' property for the created element. If not NULL, this parameter will supply a new name when modifying an existing element.

            
        
        *IN* ``uint16`` **ElementType**
            Enumeration indicating the type of element being created or modified. If the input parameter TheElement is specified when the operation is a 'modify', this type value must match the type of that instance. The actual CIM class of the created TheElement can be vendor-specific, but it must be a derived class of the appropriate CIM class -- i.e., CIM_StorageVolume, CIM_StorageExtent, CIM_LogicalDisk, or CIM_StoragePool.

            
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
            As an input parameter Size specifies the desired size. If not NULL, this parameter will supply a new size when modifying an existing element. As an output parameter Size specifies the size achieved.

            
        
        *IN* :ref:`CIM_StorageExtent[] <CIM-StorageExtent>` **InElements**
            Array of references to storage element instances that are used to create or modify TheElement.

            
        
        *IN*, *OUT* :ref:`CIM_LogicalElement <CIM-LogicalElement>` **TheElement**
            As an input parameter: if null, creates a new element. If not null, then the method modifies the specified element. As an output parameter, it is a reference to the resulting element.

            
        
    
    .. _CIM-StorageConfigurationService-CreateReplicationBuffer:

``uint32`` **CreateReplicationBuffer** (:ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`CIM_ManagedElement <CIM-ManagedElement>` Host, :ref:`CIM_StorageExtent <CIM-StorageExtent>` TargetElement, :ref:`CIM_StoragePool <CIM-StoragePool>` TargetPool, :ref:`CIM_Memory <CIM-Memory>` ReplicaBuffer)

    Create (or start a job to create) a replication buffer that buffers asynchronous write operations for remote mirror pairs. The buffer is an instance of CIM_Memory with an AssociatedMemory association to a hosting system or to a replication network pipe. The buffer element may be created based on a StorageExtent, in a pool or in a manner opaque to a client. If 0 is returned, the function completed successfully and no ConcreteJob instance is created. If 0x1000 is returned, a ConcreteJob is started, a reference to which is returned in the Job output parameter. A return value of 1 indicates the method is not supported. All other values indicate some type of error condition. 

    

    If Job Completed with No Error (0) is returned, the function completed successfully and a ConcreteJob instance is not created. 

    

    If Method Parameters Checked - Job Started (0x1000) is returned, a ConcreteJob is started, a reference to which is returned in the Job output parameter. 

    

    A return value of Not Supported (1) indicates the method is not supported. 

    

    All other values indicate some type of error condition.

    
    ============== =======================================
    ValueMap       Values                                 
    ============== =======================================
    0              Job Completed with No Error            
    1              Not Supported                          
    2              Unspecified Error                      
    3              Timeout                                
    4              Failed                                 
    5              Invalid Parameter                      
    6              In Use                                 
    ..             DMTF Reserved                          
    0x1000         Method Parameters Checked - Job Started
    0x1001..0x7FFF Method Reserved                        
    0x8000..0xFFFF Vendor Specific                        
    ============== =======================================
    
    **Parameters**
    
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if the task completed).

            
        
        *IN* :ref:`CIM_ManagedElement <CIM-ManagedElement>` **Host**
            The hosting system or replication pipe that will be antecedent to the created buffer.

            
        
        *IN* :ref:`CIM_StorageExtent <CIM-StorageExtent>` **TargetElement**
            Reference to a component extent for the buffer element.

            
        
        *IN* :ref:`CIM_StoragePool <CIM-StoragePool>` **TargetPool**
            Reference to a container pool for the buffer element.

            
        
        *OUT* :ref:`CIM_Memory <CIM-Memory>` **ReplicaBuffer**
            Reference to the created replica buffer element.

            
        
    
    .. _CIM-StorageConfigurationService-GetElementsBasedOnUsage:

``uint32`` **GetElementsBasedOnUsage** (``uint16`` ElementType, ``uint16`` Usage, ``uint16`` Criteria, :ref:`CIM_StoragePool <CIM-StoragePool>` ThePool, :ref:`CIM_ManagedSystemElement[] <CIM-ManagedSystemElement>` TheElements)

    Allows retrieving elements that meet the specified Usage. The criteria can be "available only", "in use only", or both.

    
    ============ =======================
    ValueMap     Values                 
    ============ =======================
    0            Completed with No Error
    1            Not Supported          
    2            Unknown                
    3            Timeout                
    4            Failed                 
    5            Invalid Parameter      
    ..           DMTF Reserved          
    32768..65535 Vendor Specific        
    ============ =======================
    
    **Parameters**
    
        *IN* ``uint16`` **ElementType**
            Enumeration indicating the type of elements to get.

            
            ============ ===============
            ValueMap     Values         
            ============ ===============
            0            Unknown        
            2            StorageVolume  
            3            StorageExtent  
            4            StoragePool    
            5            Logical Disk   
            ..           DMTF Reserved  
            32768..65535 Vendor Specific
            ============ ===============
            
        
        *IN* ``uint16`` **Usage**
            The specific Usage to be retrieved.

            
        
        *IN* ``uint16`` **Criteria**
            Specifies whether to retrieve all elements, available elements only, or the elements that are in use.

            
            ============ ===============
            ValueMap     Values         
            ============ ===============
            0            Unknown        
            2            All            
            3            Available Only 
            4            In Use Only    
            ..           DMTF Reserved  
            32768..65535 Vendor Specific
            ============ ===============
            
        
        *IN* :ref:`CIM_StoragePool <CIM-StoragePool>` **ThePool**
            Limit the search for the elements that satisfy the criteria to this StoragePool only. If null, all appropriate StoragePools will be considered.

            
        
        *OUT* :ref:`CIM_ManagedSystemElement[] <CIM-ManagedSystemElement>` **TheElements**
            Array of references to storage element instances retrieved.

            
        
    
    .. _CIM-StorageConfigurationService-CreateReplica:

``uint32`` **CreateReplica** (``string`` ElementName, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`CIM_LogicalElement <CIM-LogicalElement>` SourceElement, :ref:`CIM_LogicalElement <CIM-LogicalElement>` TargetElement, :ref:`CIM_StorageSetting <CIM-StorageSetting>` TargetSettingGoal, :ref:`CIM_StoragePool <CIM-StoragePool>` TargetPool, ``uint16`` CopyType)

    Start a job to create a new storage object which is a replica of the specified source storage object. (SourceElement). Note that using the input paramter, CopyType, this function can be used to instantiate the replica, and to create an ongoing association between the source and replica. If 0 is returned, the function completed successfully and no ConcreteJob instance is created. If 4096/0x1000 is returned, a ConcreteJob is started, a reference to which is returned in the Job output parameter.

    
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
    
        *IN* ``string`` **ElementName**
            A end user relevant name for the element being created. If NULL, then a system supplied default name can be used. The value will be stored in the 'ElementName' property for the created element.

            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *IN* :ref:`CIM_LogicalElement <CIM-LogicalElement>` **SourceElement**
            The source storage object which may be a StorageVolume or storage object.

            
        
        *OUT* :ref:`CIM_LogicalElement <CIM-LogicalElement>` **TargetElement**
            Reference to the created target storage element (i.e., the replica).

            
        
        *IN* :ref:`CIM_StorageSetting <CIM-StorageSetting>` **TargetSettingGoal**
            The definition for the StorageSetting to be maintained by the target storage object (the replica).

            
        
        *IN* :ref:`CIM_StoragePool <CIM-StoragePool>` **TargetPool**
            The underlying storage for the target element (the replica) will be drawn from TargetPool if specified, otherwise the allocation is implementation specific.

            
        
        *IN* ``uint16`` **CopyType**
            CopyType describes the type of copy that will be made. Values are: 

            Async: Create and maintain an asynchronous copy of the source. 

            Sync: Create and maintain a synchronized copy of the source. 

            UnSyncAssoc: Create an unsynchronized copy and maintain an association to the source. 

            UnSyncUnAssoc: Create unassociated copy of the source element.

            
            ============ ===============
            ValueMap     Values         
            ============ ===============
            2            Async          
            3            Sync           
            4            UnSyncAssoc    
            5            UnSyncUnAssoc  
            ..           DMTF Reserved  
            32768..65535 Vendor Specific
            ============ ===============
            
        
    
    .. _CIM-StorageConfigurationService-AssignStorageResourceAffinity:

``uint32`` **AssignStorageResourceAffinity** (``uint16`` ResourceType, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`CIM_ComputerSystem <CIM-ComputerSystem>` StorageProcessor, :ref:`CIM_LogicalElement[] <CIM-LogicalElement>` StorageResources)

    Start a job to assign affinity of a StoragePool(s) or StorageVolume(s) to a storage processor. At the conclusion of the operation, the resource will be a member of the StorageResourceLoadGroup with the primary affinity for the specified storage processor. Support for this method is indicated by the presence of an instance of StorageServerAsymmetryCapabilites in which the property StorageResourceAffinityAssignable is 'true'. If 0 is returned, the function completed successfully and no ConcreteJob instance was required. If 4096/0x1000 is returned, a job will be started to assign the element. The Job's reference will be returned in the output parameter Job.

    
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
    
        *IN* ``uint16`` **ResourceType**
            Enumeration indicating the type of resource being assigned or modified. .

            
            ======== =============
            ValueMap Values       
            ======== =============
            2        StorageVolume
            3        StoragePool  
            ======== =============
            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *IN*, *OUT* :ref:`CIM_ComputerSystem <CIM-ComputerSystem>` **StorageProcessor**
            Reference to the storage processor to which to assign the resource.

            
        
        *IN* :ref:`CIM_LogicalElement[] <CIM-LogicalElement>` **StorageResources**
            Array of references to storage resource instances to be assigned.

            
        
    
    .. _CIM-StorageConfigurationService-CreateElementsFromStoragePool:

``uint32`` **CreateElementsFromStoragePool** (``string[]`` ElementNames, ``uint16`` ElementType, ``uint64`` ElementCount, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`CIM_ManagedElement <CIM-ManagedElement>` Goal, ``uint64`` Size, :ref:`CIM_StoragePool <CIM-StoragePool>` InPool, :ref:`CIM_LogicalElement[] <CIM-LogicalElement>` TheElements)

    Start a job to create (or modify) a specified elements (for example StorageVolumes or StorageExtents) from a StoragePool. One of the parameters for this method is Size. As an input parameter, Size specifies the desired size of the element. As an output parameter, it specifies the size achieved. Space is taken from the input StoragePool. The desired settings for the element are specified by the Goal parameter. If the requested size cannot be created, no action will be taken, and the Return Value will be 4097/0x1001. Also, the output value of Size is set to the nearest possible size. If 0 is returned, the function completed successfully and no ConcreteJob instance was required. If 4096/0x1000 is returned, a ConcreteJob will be started to create the element. The Job's reference will be returned in the output parameter Job. If the number of elements created is less than the number of elements requested, the return value will be 4098/0x1002.

    
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
    4098         Partially Completed Operation          
    4099..32767  Method Reserved                        
    32768..65535 Vendor Specific                        
    ============ =======================================
    
    **Parameters**
    
        *IN* ``string[]`` **ElementNames**
            One or more user relevant names for the element being created. If NULL, then system supplied default names may be used. The value will be stored in the "ElementName" property for the created element.

            
        
        *IN* ``uint16`` **ElementType**
            Enumeration indicating the type of element being created.

            
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
            
        
        *IN* ``uint64`` **ElementCount**
            Count of elements to create.

            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *IN* :ref:`CIM_ManagedElement <CIM-ManagedElement>` **Goal**
            The requirements for the element to maintain. If set to a null value, the default configuration from the source pool will be used. This parameter should be a reference to a Setting or Profile appropriate to the element being created.

            
        
        *IN*, *OUT* ``uint64`` **Size**
            As an input parameter Size specifies the desired size for each element created. As an output parameter Size specifies the size achieved.

            
        
        *IN* :ref:`CIM_StoragePool <CIM-StoragePool>` **InPool**
            The Pool from which to create the elements. If not supplied, system locates an appropriate pool.

            
        
        *OUT* :ref:`CIM_LogicalElement[] <CIM-LogicalElement>` **TheElements**
            Reference to the resulting elements.

            
        
    
    .. _CIM-StorageConfigurationService-DeleteStoragePool:

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

            
        
    
    .. _CIM-StorageConfigurationService-ReturnElementsToStoragePool:

``uint32`` **ReturnElementsToStoragePool** (``uint16`` Options, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`CIM_LogicalElement[] <CIM-LogicalElement>` TheElements)

    Start a job to delete elements previously created from StoragePools. The freed space is returned to the source StoragePool. If 0 is returned, the function completed successfully and no ConcreteJob was required. If 4096/0x1000 is returned, a ConcreteJob will be started to delete the element. A reference to the Job is returned in the Job parameter.

    
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
    
        *IN* ``uint16`` **Options**
            Additional options. 

            Continue on nonexistent element: if the method encounters a non-existent element in the list of elements supplied, the method continues to delete the remaining elements. Return error on nonexistent element: if the method encounters a non-existent element in the list of elements supplied, the method returns an error.

            
            ============ ===================================
            ValueMap     Values                             
            ============ ===================================
            2            Continue on nonexistent element    
            3            Return error on nonexistent element
            ..           DMTF Reserved                      
            32768..65535 Vendor Specific                    
            ============ ===================================
            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *IN* :ref:`CIM_LogicalElement[] <CIM-LogicalElement>` **TheElements**
            References to the elements to return to the StoragePool.

            
        
    
    .. _CIM-StorageConfigurationService-ModifySynchronization:

``uint32`` **ModifySynchronization** (``uint16`` Operation, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`CIM_StorageSynchronized <CIM-StorageSynchronized>` Synchronization)

    Modify (or start a job to modify) the synchronization association between two storage objects. If 0 is returned, the function completed successfully and no ConcreteJob instance was created. If 0x1000 is returned, a ConcreteJob was started and a reference to this Job is returned in the Job output parameter. A return value of 1 indicates the method is not supported. All other values indicate some type of error condition.

    
    ============== =======================================
    ValueMap       Values                                 
    ============== =======================================
    0              Job Completed with No Error            
    1              Not Supported                          
    2              Unspecified Error                      
    3              Timeout                                
    4              Failed                                 
    5              Invalid Parameter                      
    6              In Use                                 
    ..             DMTF Reserved                          
    0x1000         Method Parameters Checked - Job Started
    0x1001..0x7FFF Method Reserved                        
    0x8000..0xFFFF Vendor Specific                        
    ============== =======================================
    
    **Parameters**
    
        *IN* ``uint16`` **Operation**
            Operation describes the type of modification to be made to the replica. Values are: 

            Detach: 'Forget' the synchronization between two storage objects. Start to treat the objects as independent. 

            Fracture: Suspend the synchronization between two storage objects using Sync or Async replication. 

            The association and (typically) changes are remembered to allow a fast resynchronization. This may be used during a backup cycle to allow one of the objects to be copied while the other remains in production. 

            Resync Replica: Re-establish the synchronization of a Sync or Async replication. This will negate the action of a previous Fracture operation. Recreate a Point In Time image for an UnSyncAssoc replication. 

            Restore from Replica: Renew the contents of the original storage object from a replica. 

            Prepare: Get the link ready for a Resync operation to take place. Some implementations will require this operation to be invoked to keep the Resync operation as fast as possible. May start the copy engine. 

            Unprepare: Clear a prepared state if a Prepare is not to be followed by a Resync operation. 

            Quiesce: Some applications require notification so that they can ready the link for an operation. For example flush any cached data or buffered changes. The copy engine is stopped for UnSyncAssoc replications. 

            Unquiesce: Take the link from the quiesced state (without executing the intended operation. 

            Start Copy: initiate a full background copy of the source to the UnSyncAssoc replica. Replica enters Frozen state when copy operation is completed. 

            Stop Copy: stop the background copy previously started. Reset To Sync: Change the CopyType of the association to Sync (e.g., from the Async CopyType). 

            Reset To Async: Change the CopyType of the association to Async (e.g., from the Sync CopyType).

            
            ============== ====================
            ValueMap       Values              
            ============== ====================
            0              DMTF Reserved       
            1              DMTF Reserved       
            2              Detach              
            3              Fracture            
            4              Resync Replica      
            5              Restore from Replica
            6              Prepare             
            7              Unprepare           
            8              Quiesce             
            9              Unquiesce           
            10             Reset To Sync       
            11             Reset To Async      
            12             Start Copy          
            13             Stop Copy           
            ..             DMTF Reserved       
            0x8000..0xFFFF Vendor Specific     
            ============== ====================
            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if the task completed).

            
        
        *IN* :ref:`CIM_StorageSynchronized <CIM-StorageSynchronized>` **Synchronization**
            The referenced to the StorageSynchronized association describing the storage source/replica relationship.

            
        
    
    .. _CIM-StorageConfigurationService-RequestUsageChange:

``uint32`` **RequestUsageChange** (``uint16`` Operation, ``uint16`` UsageValue, ``string`` OtherUsageDescription, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`CIM_LogicalElement <CIM-LogicalElement>` TheElement)

    Allows a client to request the Usage to be set if the client has access to the element supplied and the request is valid.

    
    ============ =======================================
    ValueMap     Values                                 
    ============ =======================================
    0            Completed with No Error                
    1            Not Supported                          
    2            Unknown                                
    3            Timeout                                
    4            Failed                                 
    5            Invalid Parameter                      
    6            Not Authorized                         
    ..           DMTF Reserved                          
    4096         Method Parameters Checked - Job Started
    4097..32767  Method Reserved                        
    32768..65535 Vendor Specific                        
    ============ =======================================
    
    **Parameters**
    
        *IN* ``uint16`` **Operation**
            The action to perform.

            
            ============ ===============================
            ValueMap     Values                         
            ============ ===============================
            2            Set                            
            3            Modify "Other" description only
            ..           DMTF Reserved                  
            32768..65535 Vendor Specific                
            ============ ===============================
            
        
        *IN* ``uint16`` **UsageValue**
            Applicable requested usage/restriction -- see the appropriate Usage ValueMap.

            
        
        *IN* ``string`` **OtherUsageDescription**
            New description text. Applicable when the usage value includes "Other".

            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *IN* :ref:`CIM_LogicalElement <CIM-LogicalElement>` **TheElement**
            The storage element to modify.

            
        
    

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
| :ref:`StartService <CIM-Service-StartService>`
| :ref:`ChangeAffectedElementsAssignedSequence <CIM-Service-ChangeAffectedElementsAssignedSequence>`

