.. _CIM-ResourcePool:

CIM_ResourcePool
----------------

Class reference
===============
Subclass of :ref:`CIM_LogicalElement <CIM-LogicalElement>`

A ResourcePool is a logical entity (with associated controls)provided by the host system for the purpose of allocation and assignment of resources. A given ResourcePool may be used to allocate resources of a specific type. Hierarchies of ResourcePools may be created to provide administrative control over allocations. In the cases where resources are subdivided, multiple resource pools may exist (e.g. nodal boundaries in NUMA-like systems). In systems that support over commitment, pools represent the reservable capacity, not an upper bound or limit on the maximum amount that can be allocated. Admission control during power on may detect and prevent systems from powering due to resource exhaustion. For example, over commitment on a ResourcePool with ResourceType=Memory would require that sufficient space be available in some backing-store, that may be managed through a storage ResourcePool.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ResourcePool-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-ResourcePool-Capacity:

``uint64`` **Capacity**

    This property represents the maximum amount (in units of AllocationUnits) of reservations that the ResourcePool can support.

    
.. _CIM-ResourcePool-InstanceID:

``string`` **InstanceID**

    Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon (:), and where <OrgID> must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness, <OrgID> must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If the above "preferred" algorithm is not used, the defining entity must ensure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance. 

    For DMTF-defined instances, the "preferred" algorithm must be used with the <OrgID> set to CIM.

    
.. _CIM-ResourcePool-Primordial:

``boolean`` **Primordial**

    If true, "Primordial" indicates that this ResourcePool is a base from which resources are drawn and returned in the activity of resource management. Being primordial means that this ResourcePool shall not be created or deleted by consumers of this model. However, other actions, modeled or not, may affect the characteristics or size of primordial ResourcePools. If false, "Primordial" indicates that the ResourcePool, a concrete Resource Pool, is subject to resource allocation services functions. This distinction is important because higher-level ResourcePools may be assembled using the Component or ElementAllocatedFromPool associations. Although the higher-level abstractions can be created and deleted, the most basic, (i.e. primordial), hardware-based ResourcePools cannot. They are physically realized as part of the System, or are actually managed by some other System and imported as if they were physically realized.

    
.. _CIM-ResourcePool-CurrentlyConsumedResource:

``uint64`` **CurrentlyConsumedResource**

    This property specifies the amount of resource that the resource pool currently presents to consumers.

    This property is different from the Reserved property in that it describes the consumers view of the resource while the Reserved property describes the producers view of the resource.

    
.. _CIM-ResourcePool-MaxConsumableResource:

``uint64`` **MaxConsumableResource**

    This property specifies the maximum of amount of consumable resource that the resource pool can present to consumers.

    This property is different from the Capacity property in that it describes the consumers view of the resource while the Capacity property describes the producers view of the resource.

    
.. _CIM-ResourcePool-ResourceType:

``uint16`` **ResourceType**

    The type of resource this ResourcePool may allocate.

    
    ============== =======================
    ValueMap       Values                 
    ============== =======================
    1              Other                  
    2              Computer System        
    3              Processor              
    4              Memory                 
    5              IDE Controller         
    6              Parallel SCSI HBA      
    7              FC HBA                 
    8              iSCSI HBA              
    9              IB HCA                 
    10             Ethernet Adapter       
    11             Other Network Adapter  
    12             I/O Slot               
    13             I/O Device             
    14             Floppy Drive           
    15             CD Drive               
    16             DVD drive              
    17             Disk Drive             
    18             Tape Drive             
    19             Storage Extent         
    20             Other storage device   
    21             Serial port            
    22             Parallel port          
    23             USB Controller         
    24             Graphics controller    
    25             IEEE 1394 Controller   
    26             Partitionable Unit     
    27             Base Partitionable Unit
    28             Power                  
    29             Cooling Capacity       
    30             Ethernet Switch Port   
    31             Logical Disk           
    32             Storage Volume         
    33             Ethernet Connection    
    ..             DMTF reserved          
    0x8000..0xFFFF Vendor Reserved        
    ============== =======================
    
.. _CIM-ResourcePool-PoolID:

``string`` **PoolID**

    An opaque identifier for the pool. This property is used to provide correlation across save and restore of configuration data to underlying persistent storage.

    
.. _CIM-ResourcePool-AllocationUnits:

``string`` **AllocationUnits**

    This property specifies the units of allocation used by the Reservation and Limit properties. For example, when ResourceType=Processor, AllocationUnits may be set to hertz*10^6 or percent. When ResourceType=Memory, AllocationUnits may be set to bytes*10^3. The value of this property shall be a legal value of the Programmatic Units qualifier as defined in Appendix C.1 of DSP0004 V2.4 or later.

    
.. _CIM-ResourcePool-OtherResourceType:

``string`` **OtherResourceType**

    A string that describes the resource type when a well defined value is not available and ResourceType is set to 0 for Other.

    
.. _CIM-ResourcePool-Reserved:

``uint64`` **Reserved**

    This property represents the current reservations (in units of AllocationUnits) spread across all active allocations from this pool. In a hierarchical configuration, this represents the sum of all descendant ResourcePool current reservations.

    
.. _CIM-ResourcePool-ResourceSubType:

``string`` **ResourceSubType**

    A string describing an implementation specific sub-type for this pool. For example, this may be used to distinguish different models of the same resource type.

    
.. _CIM-ResourcePool-ConsumedResourceUnits:

``string`` **ConsumedResourceUnits**

    This property specifies the units for the MaxConsumable and the Consumed properties.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

