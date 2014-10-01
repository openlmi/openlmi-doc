.. _LMI-BatteryPhysicalPackage:

LMI_BatteryPhysicalPackage
--------------------------

Class reference
===============
Subclass of :ref:`CIM_PhysicalPackage <CIM-PhysicalPackage>`

The PhysicalPackage class represents PhysicalElements that contain or host other components. Examples are a Rack enclosure or an adapter Card.


Key properties
^^^^^^^^^^^^^^

| :ref:`Tag <CIM-PhysicalElement-Tag>`
| :ref:`CreationClassName <CIM-PhysicalElement-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-BatteryPhysicalPackage-InstanceID:

``string`` **InstanceID**

    InstanceID is an optional property that may be used to opaquely and uniquely identify an instance of this class within the scope of the instantiating Namespace. Various subclasses of this class may override this property to make it required, or a key. Such subclasses may also modify the preferred algorithms for ensuring uniqueness that are defined below.

    To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon (:), and where <OrgID> must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness, <OrgID> must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If not null and the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance. 

    If not set to null for DMTF-defined instances, the "preferred" algorithm must be used with the <OrgID> set to CIM.

    
.. _LMI-BatteryPhysicalPackage-SerialNumber:

``string`` **SerialNumber**

    A manufacturer-allocated number used to identify the Physical Element.

    
.. _LMI-BatteryPhysicalPackage-ManufactureDate:

``datetime`` **ManufactureDate**

    The date that this PhysicalElement was manufactured.

    
.. _LMI-BatteryPhysicalPackage-Version:

``string`` **Version**

    A string that indicates the version of the PhysicalElement.

    
.. _LMI-BatteryPhysicalPackage-ElementName:

``string`` **ElementName**

    A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. 

    Note that the Name property of ManagedSystemElement is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. Note that if there is an associated instance of CIM_EnabledLogicalElementCapabilities, restrictions on this properties may exist as defined in ElementNameMask and MaxElementNameLen properties defined in that class.

    
.. _LMI-BatteryPhysicalPackage-Description:

``string`` **Description**

    A textual description of the PhysicalElement.

    
.. _LMI-BatteryPhysicalPackage-Manufacturer:

``string`` **Manufacturer**

    The name of the organization responsible for producing the PhysicalElement. This organization might be the entity from whom the Element is purchased, but this is not necessarily true. The latter information is contained in the Vendor property of CIM_Product.

    
.. _LMI-BatteryPhysicalPackage-Name:

``string`` **Name**

    The Name property defines the label by which the object is known. When subclassed, the Name property can be overridden to be a Key property.

    
.. _LMI-BatteryPhysicalPackage-Caption:

``string`` **Caption**

    The Caption property is a short textual description (one- line string) of the object.

    
.. _LMI-BatteryPhysicalPackage-PackageType:

``uint16`` **PackageType**

    Enumeration defining the type of the PhysicalPackage. Note that this enumeration expands on the list in the Entity MIB (the attribute, entPhysicalClass). The numeric values are consistent with CIM's enum numbering guidelines, but are slightly different than the MIB's values.

    Unknown - indicates that the package type is not known.

    Other - The package type does not correspond to an existing enumerated value. The value is specified using the OtherPackageType property.

    The values "Rack" through "Port/Connector" are defined per the Entity-MIB (where the semantics of rack are equivalent to the MIB's 'stack' value). The other values (for battery, processor, memory, power source/generator and storage media package) are self-explanatory.

    A value of "Blade" should be used when the PhysicalPackage contains the operational hardware aspects of a ComputerSystem, without the supporting mechanicals such as power and cooling. For example, a Blade Server includes processor(s) and memory, and relies on the containing chassis to supply power and cooling. In many respects, a Blade can be considered a "Module/Card". However, it is tracked differently by inventory systems and differs in terms of service philosophy. For example, a Blade is intended to be hot-plugged into a hosting enclosure without requiring additional cabling, and does not require a cover to be removed from the enclosure for installation. Similarly, a "Blade Expansion" has characteristics of a "Blade" and a "Module/Card". However, it is distinct from both due to inventory tracking and service philosophy, and because of its hardware dependence on a Blade. A Blade Expansion must be attached to a Blade prior to inserting the resultant assembly into an enclosure.

    
    ======== ================================================
    ValueMap Values                                          
    ======== ================================================
    0        Unknown                                         
    1        Other                                           
    2        Rack                                            
    3        Chassis/Frame                                   
    4        Cross Connect/Backplane                         
    5        Container/Frame Slot                            
    6        Power Supply                                    
    7        Fan                                             
    8        Sensor                                          
    9        Module/Card                                     
    10       Port/Connector                                  
    11       Battery                                         
    12       Processor                                       
    13       Memory                                          
    14       Power Source/Generator                          
    15       Storage Media Package (e.g., Disk or Tape Drive)
    16       Blade                                           
    17       Blade Expansion                                 
    ======== ================================================
    
.. _LMI-BatteryPhysicalPackage-Tag:

``string`` **Tag**

    An arbitrary string that uniquely identifies the Physical Element and serves as the key of the Element. The Tag property can contain information such as asset tag or serial number data. The key for PhysicalElement is placed very high in the object hierarchy in order to independently identify the hardware or entity, regardless of physical placement in or on Cabinets, Adapters, and so on. For example, a hotswappable or removable component can be taken from its containing (scoping) Package and be temporarily unused. The object still continues to exist and can even be inserted into a different scoping container. Therefore, the key for Physical Element is an arbitrary string and is defined independently of any placement or location-oriented hierarchy.

    
.. _LMI-BatteryPhysicalPackage-CreationClassName:

``string`` **CreationClassName**

    CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``boolean`` :ref:`HotSwappable <CIM-PhysicalPackage-HotSwappable>`
| ``string`` :ref:`SKU <CIM-PhysicalElement-SKU>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`UserTracking <CIM-PhysicalElement-UserTracking>`
| ``string`` :ref:`VendorEquipmentType <CIM-PhysicalElement-VendorEquipmentType>`
| ``real32`` :ref:`Width <CIM-PhysicalPackage-Width>`
| ``boolean`` :ref:`Removable <CIM-PhysicalPackage-Removable>`
| ``string`` :ref:`PartNumber <CIM-PhysicalElement-PartNumber>`
| ``uint16`` :ref:`RemovalConditions <CIM-PhysicalPackage-RemovalConditions>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``boolean`` :ref:`CanBeFRUed <CIM-PhysicalElement-CanBeFRUed>`
| ``boolean`` :ref:`Replaceable <CIM-PhysicalPackage-Replaceable>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``string[]`` :ref:`VendorCompatibilityStrings <CIM-PhysicalPackage-VendorCompatibilityStrings>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`OtherIdentifyingInfo <CIM-PhysicalElement-OtherIdentifyingInfo>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``boolean`` :ref:`PoweredOn <CIM-PhysicalElement-PoweredOn>`
| ``real32`` :ref:`Depth <CIM-PhysicalPackage-Depth>`
| ``string`` :ref:`Model <CIM-PhysicalElement-Model>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``real32`` :ref:`Weight <CIM-PhysicalPackage-Weight>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``real32`` :ref:`Height <CIM-PhysicalPackage-Height>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`OtherPackageType <CIM-PhysicalPackage-OtherPackageType>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`IsCompatible <CIM-PhysicalPackage-IsCompatible>`

