.. _LMI-PhysicalMemory:

LMI_PhysicalMemory
------------------

Class reference
===============
Subclass of :ref:`CIM_PhysicalMemory <CIM-PhysicalMemory>`

PhysicalMemory is a subclass of CIM_Chip, representing low level memory devices - SIMMS, DIMMs, raw memory chips, etc.


Key properties
^^^^^^^^^^^^^^

| :ref:`Tag <CIM-PhysicalElement-Tag>`
| :ref:`CreationClassName <CIM-PhysicalElement-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-PhysicalMemory-Capacity:

``uint64`` **Capacity**

    The total capacity of this PhysicalMemory, in bytes.

    
.. _LMI-PhysicalMemory-InstanceID:

``string`` **InstanceID**

    InstanceID is an optional property that may be used to opaquely and uniquely identify an instance of this class within the scope of the instantiating Namespace. Various subclasses of this class may override this property to make it required, or a key. Such subclasses may also modify the preferred algorithms for ensuring uniqueness that are defined below.

    To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon (:), and where <OrgID> must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness, <OrgID> must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If not null and the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance. 

    If not set to null for DMTF-defined instances, the "preferred" algorithm must be used with the <OrgID> set to CIM.

    
.. _LMI-PhysicalMemory-SerialNumber:

``string`` **SerialNumber**

    A manufacturer-allocated number used to identify the Physical Element.

    
.. _LMI-PhysicalMemory-PartNumber:

``string`` **PartNumber**

    The part number assigned by the organization that is responsible for producing or manufacturing the PhysicalElement.

    
.. _LMI-PhysicalMemory-ElementName:

``string`` **ElementName**

    A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. 

    Note that the Name property of ManagedSystemElement is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. Note that if there is an associated instance of CIM_EnabledLogicalElementCapabilities, restrictions on this properties may exist as defined in ElementNameMask and MaxElementNameLen properties defined in that class.

    
.. _LMI-PhysicalMemory-BankLabel:

``string`` **BankLabel**

    A string identifying the physically labeled bank where the Memory is located - for example, 'Bank 0' or 'Bank A'.

    
.. _LMI-PhysicalMemory-Manufacturer:

``string`` **Manufacturer**

    The name of the organization responsible for producing the PhysicalElement. This organization might be the entity from whom the Element is purchased, but this is not necessarily true. The latter information is contained in the Vendor property of CIM_Product.

    
.. _LMI-PhysicalMemory-FormFactor:

``uint16`` **FormFactor**

    The implementation form factor for the Chip. For example, values such as SIMM (7), TSOP (9) or PGA (10) can be specified.

    
    ======== ===========
    ValueMap Values     
    ======== ===========
    0        Unknown    
    1        Other      
    2        SIP        
    3        DIP        
    4        ZIP        
    5        SOJ        
    6        Proprietary
    7        SIMM       
    8        DIMM       
    9        TSOP       
    10       PGA        
    11       RIMM       
    12       SODIMM     
    13       SRIMM      
    14       SMD        
    15       SSMP       
    16       QFP        
    17       TQFP       
    18       SOIC       
    19       LCC        
    20       PLCC       
    21       BGA        
    22       FPBGA      
    23       LGA        
    ======== ===========
    
.. _LMI-PhysicalMemory-Name:

``string`` **Name**

    The Name property defines the label by which the object is known. When subclassed, the Name property can be overridden to be a Key property.

    
.. _LMI-PhysicalMemory-Caption:

``string`` **Caption**

    The Caption property is a short textual description (one- line string) of the object.

    
.. _LMI-PhysicalMemory-MemoryType:

``uint16`` **MemoryType**

    The type of PhysicalMemory. Synchronous DRAM is also known as SDRAM Cache DRAM is also known as CDRAM CDRAM is also known as Cache DRAM SDRAM is also known as Synchronous DRAM BRAM is also known as Block RAM

    
    ============ ================
    ValueMap     Values          
    ============ ================
    0            Unknown         
    1            Other           
    2            DRAM            
    3            Synchronous DRAM
    4            Cache DRAM      
    5            EDO             
    6            EDRAM           
    7            VRAM            
    8            SRAM            
    9            RAM             
    10           ROM             
    11           Flash           
    12           EEPROM          
    13           FEPROM          
    14           EPROM           
    15           CDRAM           
    16           3DRAM           
    17           SDRAM           
    18           SGRAM           
    19           RDRAM           
    20           DDR             
    21           DDR-2           
    22           BRAM            
    23           FB-DIMM         
    24           DDR3            
    25           FBD2            
    26           DDR4            
    27..32567    DMTF Reserved   
    32568..65535 Vendor Reserved 
    ============ ================
    
.. _LMI-PhysicalMemory-DataWidth:

``uint16`` **DataWidth**

    Data width of the PhysicalMemory, in bits. A data width of 0 and a TotalWidth of 8 would indicate that the Memory is solely used to provide error correction bits.

    
.. _LMI-PhysicalMemory-TotalWidth:

``uint16`` **TotalWidth**

    Total width, in bits, of the PhysicalMemory, including check or error correction bits. If there are no error correction bits, the value in this property should match that specified for DataWidth.

    
.. _LMI-PhysicalMemory-Description:

``string`` **Description**

    A textual description of the PhysicalElement.

    
.. _LMI-PhysicalMemory-ConfiguredMemoryClockSpeed:

``uint32`` **ConfiguredMemoryClockSpeed**

    The configured clock speed (in MHz) of PhysicalMemory.

    
.. _LMI-PhysicalMemory-Tag:

``string`` **Tag**

    An arbitrary string that uniquely identifies the Physical Element and serves as the key of the Element. The Tag property can contain information such as asset tag or serial number data. The key for PhysicalElement is placed very high in the object hierarchy in order to independently identify the hardware or entity, regardless of physical placement in or on Cabinets, Adapters, and so on. For example, a hotswappable or removable component can be taken from its containing (scoping) Package and be temporarily unused. The object still continues to exist and can even be inserted into a different scoping container. Therefore, the key for Physical Element is an arbitrary string and is defined independently of any placement or location-oriented hierarchy.

    
.. _LMI-PhysicalMemory-CreationClassName:

``string`` **CreationClassName**

    CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

    
.. _LMI-PhysicalMemory-Speed:

``uint32`` **Speed**

    The speed of the PhysicalMemory, in nanoseconds.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``boolean`` :ref:`HotSwappable <CIM-PhysicalComponent-HotSwappable>`
| ``string`` :ref:`SKU <CIM-PhysicalElement-SKU>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`UserTracking <CIM-PhysicalElement-UserTracking>`
| ``string`` :ref:`VendorEquipmentType <CIM-PhysicalElement-VendorEquipmentType>`
| ``uint32`` :ref:`InterleavePosition <CIM-PhysicalMemory-InterleavePosition>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`Version <CIM-PhysicalElement-Version>`
| ``boolean`` :ref:`Removable <CIM-PhysicalComponent-Removable>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``boolean`` :ref:`CanBeFRUed <CIM-PhysicalElement-CanBeFRUed>`
| ``boolean`` :ref:`Replaceable <CIM-PhysicalComponent-Replaceable>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``boolean`` :ref:`IsSpeedInMhz <CIM-PhysicalMemory-IsSpeedInMhz>`
| ``string`` :ref:`OtherIdentifyingInfo <CIM-PhysicalElement-OtherIdentifyingInfo>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``boolean`` :ref:`PoweredOn <CIM-PhysicalElement-PoweredOn>`
| ``uint32`` :ref:`MaxMemorySpeed <CIM-PhysicalMemory-MaxMemorySpeed>`
| ``string`` :ref:`Model <CIM-PhysicalElement-Model>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``datetime`` :ref:`ManufactureDate <CIM-PhysicalElement-ManufactureDate>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint16`` :ref:`RemovalConditions <CIM-PhysicalComponent-RemovalConditions>`
| ``uint32`` :ref:`PositionInRow <CIM-PhysicalMemory-PositionInRow>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

