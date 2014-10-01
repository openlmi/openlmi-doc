.. _CIM-StoragePool:

CIM_StoragePool
---------------

Class reference
===============
Subclass of :ref:`CIM_ResourcePool <CIM-ResourcePool>`

A StoragePool is a conglomeration of storage capacity for the purpose of assignment and allocation based on service characteristics, such as location, available space or other criteria (for example, cost per megabyte or hardware ownership). A StoragePool is managed within the scope of a particular System. StoragePools may consist of component StoragePools or StorageExtents. StorageExtents that belong to the StoragePool have a Component relationship to the StoragePool. StorageExtents/StoragePools that are elements of a pool have their available space aggregated into the pool. StoragePools, StorageVolumes and LogicalDisks may be created from StoragePools. This is indicated by the AllocatedFromStoragePool association. StoragePool is scoped to a system by the HostedStoragePool association.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ResourcePool-InstanceID>`
| :ref:`InstanceID <CIM-ResourcePool-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-StoragePool-CapacityInMigratingSource:

``uint64`` **CapacityInMigratingSource**

    The total capacity of extents in migrating out from this storage pool

    
.. _CIM-StoragePool-InstanceID:

``string`` **InstanceID**

    Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. In order to ensure uniqueness within the NameSpace, the value of InstanceID SHOULD be constructed using the following 'preferred' algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon ':', and where <OrgID> MUST include a copyrighted, trademarked or otherwise unique name that is owned by the business entity creating/defining the InstanceID, or is a registered ID that is assigned to the business entity by a recognized global authority (This is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness <OrgID> MUST NOT contain a colon (':'). When using this algorithm, the first colon to appear in InstanceID MUST appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and SHOULD not be re-used to identify different underlying (real-world) elements. If the above 'preferred' algorithm is not used, the defining entity MUST assure that the resultant InstanceID is not re-used across any InstanceIDs produced by this or other providers for this instance's NameSpace. 

    For DMTF defined instances, the 'preferred' algorithm MUST be used with the <OrgID> set to 'CIM'.

    
.. _CIM-StoragePool-ClientSettableUsage:

``uint16[]`` **ClientSettableUsage**

    Indicates which values from the "Usage" valuemap can be manipulated by a client using the method "StorageConfigurationService.RequestUsageChange".

    
.. _CIM-StoragePool-Primordial:

``boolean`` **Primordial**

    If true, "Primordial" indicates that this StoragePool is the base from which storage capacity is drawn and returned in the activity of storage management. Being primordial means that this StoragePool shall not be created or deleted by consumers of this model. However, other actions, modeled or not, may affect the characteristics or size of primordial StoragePools. If false, "Primordial" indicated that the StoragePool, a concrete Storage Pool, is subject to storage services functions. This distinction is important because higher-level StoragePools may be assembled using the Component or AllocatedFromStoragePool associations. Although the higher-level abstractions can be created and deleted, the most basic, (i.e. primordial), hardware-based StoragePools cannot. They are physically realized as part of the System, or are actually managed by some other System and imported as if they were physically realized.

    
.. _CIM-StoragePool-Usage:

``uint16`` **Usage**

    Indicates the intended usage or any restrictions that may have been imposed on the usage of this component. For example, a storage pool may be reserved for use by the block server. In that case the Usage of the storage pool is marked as "Reserved for the ComputerSystem". In the case of "Other", see OtherUsageDescription for more information.

    
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
    
.. _CIM-StoragePool-CapacityInMigratingTarget:

``uint64`` **CapacityInMigratingTarget**

    The total capacity of extents in migrating into this storage pool

    
.. _CIM-StoragePool-PoolID:

``string`` **PoolID**

    A unique name in the context of the System that identifies this pool.

    
.. _CIM-StoragePool-LowSpaceWarningThreshold:

``uint16`` **LowSpaceWarningThreshold**

    LowSpaceWarningThreshold simplifies the creation of a pool specific Indication based on RemainingManagedSpace <= 

    (TotalManagedSpace*LowSpaceWarningThreshold)/100. One example client for an Indication based on this property is a delta copy implementation where the pool enables continuous, variable space consumption for the delta storage. Another example client for an Indication based on this property is a provisioning manager implementing a policy for adding storage to a pool when it becomes low.

    
.. _CIM-StoragePool-TotalManagedSpace:

``uint64`` **TotalManagedSpace**

    The total amount of capacity usable for the allocation of StorageVolumes, LogicalDisks, or child Storage Pools. 

    For primordial Storage Pools, this capacity reflects the usable capacity of Disk Drives or LUNs, for example, to the owning storage device or application. For example, in storage array, a primordial Storage Pool's TotalManagedSpace does not include metadata such as the disk label area and absolute disk drive capacity lost in disk formatting. 

    For concrete Storage Pools, the same applies, but the metadata not included in TotalManagedSpace is consumed in virtualization like RAID and concatenation. Concrete Storage Pool may also be simple reserve of capacity. In such a case, no capacity may be lost in formation of the Storage Pool. 

    Conceptually TotalManagedSpace is the sum of all storage known via AssociatedComponentExtent associations to underlying StorageExtents. However, note some of these underlying storage may not be modeled by the instrumentation.

    
.. _CIM-StoragePool-OtherUsageDescription:

``string`` **OtherUsageDescription**

    Populated when "Usage" has the value of "Other".

    
.. _CIM-StoragePool-SpaceLimitDetermination:

``uint16`` **SpaceLimitDetermination**

    This property is the Subsystem ID if the array or virtualizer supports Subsystem IDs. If they are supported they would be required on volume creation.

    
    ======== =========
    ValueMap Values   
    ======== =========
    2        Allocated
    3        Quote    
    4        Limitless
    ======== =========
    
.. _CIM-StoragePool-RemainingManagedSpace:

``uint64`` **RemainingManagedSpace**

    The remaining usable capacity after the allocation of StorageVolumes, LogicalDisks, or child Storage Pools. This property is maintained here to provide efficient access to this information. However, note that it is possible to compute RemainingManagedSpace as (TotalManagedSpace minus the sum of SpaceConsumed from all of the AllocatedFromStoragePool references from this StoragePool). Note that SpaceConsumed remains useful to determine the amount of capacity consumed by a particular allocated element.

    
.. _CIM-StoragePool-ReservedSpace:

``uint64`` **ReservedSpace**

    The amount of capacity used by the storage pool to store information about the configuration of the storage pool. The space is not included in the TotalManagedSpace of the storage pool.

    
.. _CIM-StoragePool-SpaceLimit:

``uint64`` **SpaceLimit**

    The capacity of the storage allocated to the pool when SpaceLimitDetermination has the value 3 (Quota) or 4 (Limitless) or is set to the value of TotalManagedSpace if SpaceLimitDetermination has the value 2 (Allocated).

    
.. _CIM-StoragePool-ThinProvisionMetaDataSpace:

``uint64`` **ThinProvisionMetaDataSpace**

    The size of metadata consumed by this storage pool. Only defined if the pool is thin provisioned.

    
.. _CIM-StoragePool-ElementsShareSpace:

``boolean`` **ElementsShareSpace**

    If true, it indicates elements allocated from the storage pool are sharing space from the storage pool. For example, multiple snapshots "allocated" from a storage pool, point to the same blocks of the storage pool. As another example, elements utilizing de-duplication technology refer to a shared copy of the data stored in the storage pool.

    

Local methods
^^^^^^^^^^^^^

    .. _CIM-StoragePool-GetSupportedSizes:

``uint32`` **GetSupportedSizes** (``uint16`` ElementType, :ref:`CIM_StorageSetting <CIM-StorageSetting>` Goal, ``uint64[]`` Sizes)

    For pools that that support a range of sizes for volume or pool creation, this method can be used to retrieve the supported range. Note that different pool implementations may support either or both the GetSupportedSizes and GetSupportedSizeRanges methods at different times, depending on Pool configuration. Also note that the advertised sizes may change after the call due to requests from other clients. If the pool currently only supports discrete sizes, then the return value will be set to 1.

    
    ======== =============================
    ValueMap Values                       
    ======== =============================
    0        Method completed OK          
    1        Method not supported         
    2        Use GetSupportedSizes instead
    3        Invalid Element Type         
    ======== =============================
    
    **Parameters**
    
        *IN* ``uint16`` **ElementType**
            The type of element for which supported sizes are reported. The Thin Provision values are only supported when the Thin Provisioning Profile is supported; the resulting StorageVolues/LogicalDisk shall have ThinlyProvisioned set to true.

            
            ======== =============================
            ValueMap Values                       
            ======== =============================
            2        Storage Pool                 
            3        Storage Volume               
            4        Logical Disk                 
            5        Thin Provisioned Volume      
            6        Thin Provisioned Logical Disk
            ======== =============================
            
        
        *IN* :ref:`CIM_StorageSetting <CIM-StorageSetting>` **Goal**
            The StorageSetting for which supported sizes should be reported for.

            
        
        *IN*, *OUT* ``uint64[]`` **Sizes**
            List of supported sizes for a Volume/Pool creation or modification.

            
        
    
    .. _CIM-StoragePool-GetSupportedSizeRange:

``uint32`` **GetSupportedSizeRange** (``uint16`` ElementType, :ref:`CIM_StorageSetting <CIM-StorageSetting>` Goal, ``uint64`` MinimumVolumeSize, ``uint64`` MaximumVolumeSize, ``uint64`` VolumeSizeDivisor)

    For pools that that support a range of sizes for volume or pool creation, this method can be used to retrieve the supported range. Note that different pool implementations may support either or both the GetSupportedSizes and GetSupportedSizeRanges methods at different times, depending on Pool configuration. Also note that the advertised sizes may change after the call due to requests from other clients. If the pool currently only supports discrete sizes, then the return value will be set to 1.

    
    ======== =============================
    ValueMap Values                       
    ======== =============================
    0        Method completed OK          
    1        Method not supported         
    2        Use GetSupportedSizes instead
    3        Invalid Element Type         
    ======== =============================
    
    **Parameters**
    
        *IN* ``uint16`` **ElementType**
            The type of element for which supported size ranges are reported. The Thin Provision values are only supported when the Thin Provisioning Profile is supported; the resulting StorageVolues/LogicalDisk shall have ThinlyProvisioned set to true.

            
            ======== =============================
            ValueMap Values                       
            ======== =============================
            2        Storage Pool                 
            3        Storage Volume               
            4        Logical Disk                 
            5        Thin Provisioned Volume      
            6        Thin Provisioned Logical Disk
            ======== =============================
            
        
        *IN* :ref:`CIM_StorageSetting <CIM-StorageSetting>` **Goal**
            The StorageSetting for which supported size ranges should be reported for.

            
        
        *IN*, *OUT* ``uint64`` **MinimumVolumeSize**
            The minimum size for a volume/pool in bytes.

            
        
        *IN*, *OUT* ``uint64`` **MaximumVolumeSize**
            The maximum size for a volume/pool in bytes.

            
        
        *IN*, *OUT* ``uint64`` **VolumeSizeDivisor**
            A volume/pool size must be a multiple of this value which is specified in bytes.

            
        
    
    .. _CIM-StoragePool-GetAvailableExtents:

``uint32`` **GetAvailableExtents** (:ref:`CIM_StorageSetting <CIM-StorageSetting>` Goal, :ref:`CIM_StorageExtent[] <CIM-StorageExtent>` AvailableExtents)

    This method can be used to retrieve a list of available Extents that may be used in the creation or modification of a StoragePool, StorageVolume, or LogicalDisk. The GetAvailableExtents method MUST return the Extents from the set of Component Extents of the Pool on which the method is being invoked. The returned Extents are available at the time the method returns. There is no guarantee that the same Extents will be available later. This method MUST return the Extents that are not being used as supporting capacity for any other Pools, Volumes, or LogicalDisks that have been allocated from this Pool. The Extent returned MUST be a component Extent of the Pool or subdivisions of a component Extent, the subdivisions themselves represented as Extents.

    
    ============ =======================
    ValueMap     Values                 
    ============ =======================
    0            Completed with No Error
    1            Not Supported          
    2            Unknown                
    3            Timeout                
    4            Failed                 
    5            Invalid Parameter      
    6            In Use                 
    ..           DMTF Reserved          
    4098..32767  Method Reserved        
    32768..65535 Vendor Specific        
    ============ =======================
    
    **Parameters**
    
        *IN* :ref:`CIM_StorageSetting <CIM-StorageSetting>` **Goal**
            The StorageSetting (Goal) for which supported extents should be retrieved as available. 

            If a NULL is passed for the Goal, the method will return all available extents, regardless of the goal. There exists a possibility of error in creating a Pool, Volume, or LogicalDisk retrieved in this manner.

            
        
        *OUT* :ref:`CIM_StorageExtent[] <CIM-StorageExtent>` **AvailableExtents**
            List of references to available StorageExtents, or subclass instances.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``uint64`` :ref:`Capacity <CIM-ResourcePool-Capacity>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`ResourceSubType <CIM-ResourcePool-ResourceSubType>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``uint64`` :ref:`CurrentlyConsumedResource <CIM-ResourcePool-CurrentlyConsumedResource>`
| ``uint64`` :ref:`MaxConsumableResource <CIM-ResourcePool-MaxConsumableResource>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`ResourceType <CIM-ResourcePool-ResourceType>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`AllocationUnits <CIM-ResourcePool-AllocationUnits>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string`` :ref:`OtherResourceType <CIM-ResourcePool-OtherResourceType>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint64`` :ref:`Reserved <CIM-ResourcePool-Reserved>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``string`` :ref:`ConsumedResourceUnits <CIM-ResourcePool-ConsumedResourceUnits>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

