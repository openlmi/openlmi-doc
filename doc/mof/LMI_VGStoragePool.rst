.. _LMI-VGStoragePool:

LMI_VGStoragePool
-----------------

Class reference
===============
Subclass of :ref:`CIM_StoragePool <CIM-StoragePool>`

This class represents Volume Groups. Space in Volume Groups can be allocated in units called 'extents'. Only whole extents can be allocated, no partial allocation is allowed.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ResourcePool-InstanceID>`
| :ref:`InstanceID <CIM-ResourcePool-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-VGStoragePool-InstanceID:

``string`` **InstanceID**

    Unique ID of the Volume Group. It is unique in scope of CIM namespace. To ensure uniqueness, the ID has following format: LMI:VG:<VG name>.

    
.. _LMI-VGStoragePool-Primordial:

``boolean`` **Primordial**

    If true, "Primordial" indicates that this StoragePool is the base from which storage capacity is drawn and returned in the activity of storage management. Being primordial means that this StoragePool shall not be created or deleted by consumers of this model. However, other actions, modeled or not, may affect the characteristics or size of primordial StoragePools. If false, "Primordial" indicated that the StoragePool, a concrete Storage Pool, is subject to storage services functions. This distinction is important because higher-level StoragePools may be assembled using the Component or AllocatedFromStoragePool associations. Although the higher-level abstractions can be created and deleted, the most basic, (i.e. primordial), hardware-based StoragePools cannot. They are physically realized as part of the System, or are actually managed by some other System and imported as if they were physically realized.

    
.. _LMI-VGStoragePool-ElementName:

``string`` **ElementName**

    A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. 

    Note that the Name property of ManagedSystemElement is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. Note that if there is an associated instance of CIM_EnabledLogicalElementCapabilities, restrictions on this properties may exist as defined in ElementNameMask and MaxElementNameLen properties defined in that class.

    
.. _LMI-VGStoragePool-PoolID:

``string`` **PoolID**

    Name of the Volume Group.

    
.. _LMI-VGStoragePool-TotalManagedSpace:

``uint64`` **TotalManagedSpace**

    The total amount of capacity usable for the allocation of StorageVolumes, LogicalDisks, or child Storage Pools. 

    For primordial Storage Pools, this capacity reflects the usable capacity of Disk Drives or LUNs, for example, to the owning storage device or application. For example, in storage array, a primordial Storage Pool's TotalManagedSpace does not include metadata such as the disk label area and absolute disk drive capacity lost in disk formatting. 

    For concrete Storage Pools, the same applies, but the metadata not included in TotalManagedSpace is consumed in virtualization like RAID and concatenation. Concrete Storage Pool may also be simple reserve of capacity. In such a case, no capacity may be lost in formation of the Storage Pool. 

    Conceptually TotalManagedSpace is the sum of all storage known via AssociatedComponentExtent associations to underlying StorageExtents. However, note some of these underlying storage may not be modeled by the instrumentation.

    
.. _LMI-VGStoragePool-Name:

``string`` **Name**

    Path of the volume group in /dev filesystem

    
.. _LMI-VGStoragePool-RemainingExtents:

``uint64`` **RemainingExtents**

    Number of available extents in this Volume Group.

    
.. _LMI-VGStoragePool-ExtentSize:

``uint64`` **ExtentSize**

    Volume group extent size.

    
.. _LMI-VGStoragePool-RemainingManagedSpace:

``uint64`` **RemainingManagedSpace**

    The remaining usable capacity after the allocation of StorageVolumes, LogicalDisks, or child Storage Pools. This property is maintained here to provide efficient access to this information. However, note that it is possible to compute RemainingManagedSpace as (TotalManagedSpace minus the sum of SpaceConsumed from all of the AllocatedFromStoragePool references from this StoragePool). Note that SpaceConsumed remains useful to determine the amount of capacity consumed by a particular allocated element.

    
.. _LMI-VGStoragePool-UUID:

``string`` **UUID**

    UUID of the Volume Group.

    
.. _LMI-VGStoragePool-TotalExtents:

``uint64`` **TotalExtents**

    Total number of extents in this Volume Group.

    

Local methods
^^^^^^^^^^^^^

    .. _LMI-VGStoragePool-GetSupportedSizes:

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

            
        
    
    .. _LMI-VGStoragePool-GetSupportedSizeRange:

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

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``uint64`` :ref:`CapacityInMigratingSource <CIM-StoragePool-CapacityInMigratingSource>`
| ``uint64`` :ref:`Capacity <CIM-ResourcePool-Capacity>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``uint16[]`` :ref:`ClientSettableUsage <CIM-StoragePool-ClientSettableUsage>`
| ``string`` :ref:`ResourceSubType <CIM-ResourcePool-ResourceSubType>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``uint16`` :ref:`Usage <CIM-StoragePool-Usage>`
| ``uint64`` :ref:`CurrentlyConsumedResource <CIM-ResourcePool-CurrentlyConsumedResource>`
| ``uint64`` :ref:`MaxConsumableResource <CIM-ResourcePool-MaxConsumableResource>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``uint16`` :ref:`SpaceLimitDetermination <CIM-StoragePool-SpaceLimitDetermination>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`ResourceType <CIM-ResourcePool-ResourceType>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16`` :ref:`LowSpaceWarningThreshold <CIM-StoragePool-LowSpaceWarningThreshold>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`AllocationUnits <CIM-ResourcePool-AllocationUnits>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string`` :ref:`OtherUsageDescription <CIM-StoragePool-OtherUsageDescription>`
| ``string`` :ref:`OtherResourceType <CIM-ResourcePool-OtherResourceType>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint64`` :ref:`CapacityInMigratingTarget <CIM-StoragePool-CapacityInMigratingTarget>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint64`` :ref:`ReservedSpace <CIM-StoragePool-ReservedSpace>`
| ``uint64`` :ref:`Reserved <CIM-ResourcePool-Reserved>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint64`` :ref:`SpaceLimit <CIM-StoragePool-SpaceLimit>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint64`` :ref:`ThinProvisionMetaDataSpace <CIM-StoragePool-ThinProvisionMetaDataSpace>`
| ``boolean`` :ref:`ElementsShareSpace <CIM-StoragePool-ElementsShareSpace>`
| ``string`` :ref:`ConsumedResourceUnits <CIM-ResourcePool-ConsumedResourceUnits>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`GetAvailableExtents <CIM-StoragePool-GetAvailableExtents>`

