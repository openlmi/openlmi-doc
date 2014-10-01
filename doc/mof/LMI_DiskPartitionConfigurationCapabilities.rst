.. _LMI-DiskPartitionConfigurationCapabilities:

LMI_DiskPartitionConfigurationCapabilities
------------------------------------------

Class reference
===============
Subclass of :ref:`CIM_DiskPartitionConfigurationCapabilities <CIM-DiskPartitionConfigurationCapabilities>`

DiskPartitionConfigurationCapabilities instances describe a partition style supported by the platform. An instance of this class is associated with a volume (or partition) when a partition table is installed (see DiskPartitionConfigurationService.SetPartitionStyle.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-DiskPartitionConfigurationCapabilities-SupportedSettings:

``uint16[]`` **SupportedSettings**

    List of supported properties in LMI_DiskPartitionConfigurationSetting. Different partition tables support different properties.

    
    ======== ==============
    ValueMap Values        
    ======== ==============
    1        Partition Type
    2        Bootable      
    3        Hidden        
    ======== ==============
    
.. _LMI-DiskPartitionConfigurationCapabilities-ElementName:

``string`` **ElementName**

    The user friendly name for this instance of Capabilities. In addition, the user friendly name can be used as a index property for a search of query. (Note: Name does not have to be unique within a namespace.)

    
.. _LMI-DiskPartitionConfigurationCapabilities-PartitionTableSize:

``uint32`` **PartitionTableSize**

    The number of block occupied by the partition table and other metadata. The effective block size for partitions is the StorageExtent's ConsumableBlocks minus this size.

    
.. _LMI-DiskPartitionConfigurationCapabilities-PartitionStyle:

``uint16`` **PartitionStyle**

    The partition style (i.e partition table type) associated with this capabilities instance. 

    LMI introduces additional partition styles.

    
    ======== ======
    ValueMap Values
    ======== ======
    2        MBR   
    3        GPT   
    4        VTOC  
    4097     PC98  
    4098     SUN   
    4099     MAC   
    4100     EMBR  
    ======== ======
    
.. _LMI-DiskPartitionConfigurationCapabilities-InstanceID:

``string`` **InstanceID**

    Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. In order to ensure uniqueness within the NameSpace, the value of InstanceID SHOULD be constructed using the following 'preferred' algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon ':', and where <OrgID> MUST include a copyrighted, trademarked or otherwise unique name that is owned by the business entity creating/defining the InstanceID, or is a registered ID that is assigned to the business entity by a recognized global authority (This is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness <OrgID> MUST NOT contain a colon (':'). When using this algorithm, the first colon to appear in InstanceID MUST appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and SHOULD not be re-used to identify different underlying (real-world) elements. If the above 'preferred' algorithm is not used, the defining entity MUST assure that the resultant InstanceID is not re-used across any InstanceIDs produced by this or other providers for this instance's NameSpace. 

    For DMTF defined instances, the 'preferred' algorithm MUST be used with the <OrgID> set to 'CIM'.

    
.. _LMI-DiskPartitionConfigurationCapabilities-Caption:

``string`` **Caption**

    The Caption property is a short textual description (one- line string) of the object.

    
.. _LMI-DiskPartitionConfigurationCapabilities-ValidSubPartitionStyles:

``uint16[]`` **ValidSubPartitionStyles**

    Some partitions can act as a container for other partitions. If sub partitions are not supported, this should be set to NULL.

    
    ======== ======
    ValueMap Values
    ======== ======
    1        Other 
    2        MBR   
    3        VTOC  
    4        GPT   
    4100     EMBR  
    ======== ======
    
.. _LMI-DiskPartitionConfigurationCapabilities-OverlapAllowed:

``boolean`` **OverlapAllowed**

    The platform supports partitions with overlapping address ranges.

    
.. _LMI-DiskPartitionConfigurationCapabilities-MaxNumberOfPartitions:

``uint16`` **MaxNumberOfPartitions**

    The maximum number of partitions that can be BasedOn the Underlying extent.

    
.. _LMI-DiskPartitionConfigurationCapabilities-SupportedSynchronousActions:

``uint16[]`` **SupportedSynchronousActions**

    Enumeration indicating what operations will be executed synchronously. If an operation is included in this property then the underlying implementation is indicating that it supports the operation without the creation of a job.

    
    ======== =======================
    ValueMap Values                 
    ======== =======================
    2        SetPartitionStyle      
    3        CreateOrModifyPartition
    ..       DMTF Reserved          
    0x8000.. Vendor Reserved        
    ======== =======================
    
.. _LMI-DiskPartitionConfigurationCapabilities-MaxCapacity:

``uint64`` **MaxCapacity**

    The largest partition size (in blocks) of this style supported on this platform.

    

Local methods
^^^^^^^^^^^^^

    .. _LMI-DiskPartitionConfigurationCapabilities-GetAlignment:

``uint32`` **GetAlignment** (:ref:`CIM_StorageExtent <CIM-StorageExtent>` Extent, ``uint64`` Alignment)

    Return allignment unit for given StorageExtent (in blocks). New partitions and metadata sectors should be aligned to this unit.

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Success      
    1        Not Supported
    4        Failed       
    ======== =============
    
    **Parameters**
    
        *IN* :ref:`CIM_StorageExtent <CIM-StorageExtent>` **Extent**
            The StorageExtent to get alignment for.

            
        
        *OUT* ``uint64`` **Alignment**
            Suggested alignment, in nr. of blocks.

            
        
    
    .. _LMI-DiskPartitionConfigurationCapabilities-FindPartitionLocation:

``uint32`` **FindPartitionLocation** (:ref:`CIM_StorageExtent <CIM-StorageExtent>` Extent, ``uint64`` Size, ``uint64`` StartingAddress, ``uint64`` EndingAddress)

    This method finds the best place for partition of given size.

    
    ======== =====================
    ValueMap Values               
    ======== =====================
    0        Success              
    1        Not Supported        
    4        Failed               
    100      Not Enough Free Space
    ======== =====================
    
    **Parameters**
    
        *IN* :ref:`CIM_StorageExtent <CIM-StorageExtent>` **Extent**
            The StorageExtent, on which the partition should be created.

            
        
        *IN*, *OUT* ``uint64`` **Size**
            On input, the requested size of the partition. On output, the achieeved size. It can be rounded to nearest block size or due to alignment.

            If null, location of the largest possible partition will be returned.

            
        
        *OUT* ``uint64`` **StartingAddress**
            Suggested starting block number of the partition. It already includes any metadata and alignment sectors.

            
        
        *OUT* ``uint64`` **EndingAddress**
            Suggested ending block number of the partition. 

            
        
    
    .. _LMI-DiskPartitionConfigurationCapabilities-CreateSetting:

``uint32`` **CreateSetting** (:ref:`LMI_DiskPartitionConfigurationSetting <LMI-DiskPartitionConfigurationSetting>` Setting)

    Create LMI_DiskPartitionConfigurationSetting applicable to this partition table. All properties its will have default values.

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Success      
    1        Not Supported
    4        Failed       
    ======== =============
    
    **Parameters**
    
        *OUT* :ref:`LMI_DiskPartitionConfigurationSetting <LMI-DiskPartitionConfigurationSetting>` **Setting**
            Created setting.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`Version <CIM-DiskPartitionConfigurationCapabilities-Version>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string[]`` :ref:`OtherValidSubPartitionStyles <CIM-DiskPartitionConfigurationCapabilities-OtherValidSubPartitionStyles>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`CreateGoalSettings <CIM-Capabilities-CreateGoalSettings>`

