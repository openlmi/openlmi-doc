.. _CIM-DiskPartitionConfigurationCapabilities:

CIM_DiskPartitionConfigurationCapabilities
------------------------------------------

Class reference
===============
Subclass of :ref:`CIM_Capabilities <CIM-Capabilities>`

DiskPartitionConfigurationCapabilities instances describe a partition style supported by the platform. An instance of this class is associated with a volume (or partition) when a partition table is installed (see DiskPartitionConfigurationService.SetPartitionStyle.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-DiskPartitionConfigurationCapabilities-PartitionTableSize:

``uint32`` **PartitionTableSize**

    The number of block occupied by the partition table and other metadata. The effective block size for partitions is the StorageExtent's ConsumableBlocks minus this size.

    
.. _CIM-DiskPartitionConfigurationCapabilities-PartitionStyle:

``uint16`` **PartitionStyle**

    The partition style (i.e partition table type) associated with this capabilities instance.

    
    ======== ======
    ValueMap Values
    ======== ======
    2        MBR   
    3        GPT   
    4        VTOC  
    ======== ======
    
.. _CIM-DiskPartitionConfigurationCapabilities-ValidSubPartitionStyles:

``uint16[]`` **ValidSubPartitionStyles**

    Some partitions can act as a container for other partitions. If sub partitions are not supported, this should be set to NULL.

    
    ======== ======
    ValueMap Values
    ======== ======
    1        Other 
    2        MBR   
    3        VTOC  
    4        GPT   
    ======== ======
    
.. _CIM-DiskPartitionConfigurationCapabilities-OverlapAllowed:

``boolean`` **OverlapAllowed**

    The platform supports partitions with overlapping address ranges.

    
.. _CIM-DiskPartitionConfigurationCapabilities-MaxNumberOfPartitions:

``uint16`` **MaxNumberOfPartitions**

    The maximum number of partitions that can be BasedOn the Underlying extent.

    
.. _CIM-DiskPartitionConfigurationCapabilities-Version:

``uint16`` **Version**

    The version number associated with this partition style.

    
.. _CIM-DiskPartitionConfigurationCapabilities-SupportedSynchronousActions:

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
    
.. _CIM-DiskPartitionConfigurationCapabilities-MaxCapacity:

``uint64`` **MaxCapacity**

    The largest partition size (in blocks) of this style supported on this platform.

    
.. _CIM-DiskPartitionConfigurationCapabilities-OtherValidSubPartitionStyles:

``string[]`` **OtherValidSubPartitionStyles**

    A string describing the partition style if the corresponding entry in ValidSubPartitionStyles is 'Other'.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`ElementName <CIM-Capabilities-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`InstanceID <CIM-Capabilities-InstanceID>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`CreateGoalSettings <CIM-Capabilities-CreateGoalSettings>`

