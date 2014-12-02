.. _CIM-PhysicalPackage:

CIM_PhysicalPackage
-------------------

Class reference
===============
Subclass of :ref:`CIM_PhysicalElement <CIM-PhysicalElement>`

The PhysicalPackage class represents PhysicalElements that contain or host other components. Examples are a Rack enclosure or an adapter Card.


Key properties
^^^^^^^^^^^^^^

| :ref:`Tag <CIM-PhysicalElement-Tag>`
| :ref:`CreationClassName <CIM-PhysicalElement-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-PhysicalPackage-HotSwappable:

``boolean`` **HotSwappable**

    **Deprecated!** 
    The use of this property is being deprecated. Instead RemovalConditions should be used. The RemovalConditions property addresses whether a PhysicalPackage is removable with or without power being applied. 

    

    A PhysicalPackage is HotSwappable if it is possible to replace the Element with a physically different but equivalent one while the containing Package has power applied to it (ie, is 'on'). For example, a disk drive Package inserted using SCA connectors is both Removable and HotSwappable. All HotSwappable packages are inherently Removable and Replaceable.

    
.. _CIM-PhysicalPackage-Width:

``real32`` **Width**

    The width of the PhysicalPackage in inches.

    
.. _CIM-PhysicalPackage-Removable:

``boolean`` **Removable**

    **Deprecated!** 
    The use of this property is being deprecated. Instead RemovalConditions should be used. The RemovalConditions property addresses whether a PhysicalPackage is removable with or without power being applied. 

    A PhysicalPackage is Removable if it is designed to be taken in and out of the physical container in which it is normally found, without impairing the function of the overall packaging. A Package can still be Removable if power must be 'off' in order to perform the removal. If power can be 'on' and the Package removed, then the Element is both Removable and HotSwappable. For example, an extra battery in a laptop is Removable, as is a disk drive Package inserted using SCA connectors. However, the latter is also HotSwappable. A laptop's display is not Removable, nor is a non-redundant power supply. Removing these components would impact the function of the overall packaging or is impossible due to the tight integration of the Package.

    
.. _CIM-PhysicalPackage-RemovalConditions:

``uint16`` **RemovalConditions**

    The RemovalCapabilites property is used to describe the conditions under which a PhysicalPackage can be removed. Since all PhysicalPackages are not removable, this property defaults to 2, 'Not Applicable'.

    
    ======== ========================
    ValueMap Values                  
    ======== ========================
    0        Unknown                 
    2        Not Applicable          
    3        Removable when off      
    4        Removable when on or off
    ======== ========================
    
.. _CIM-PhysicalPackage-Replaceable:

``boolean`` **Replaceable**

    **Deprecated!** 
    The use of this property is being deprecated because it is redundant with the FRU class and its associations. A PhysicalPackage is Replaceable if it is possible to replace (FRU or upgrade) the Element with a physically different one. For example, some ComputerSystems allow the main Processor chip to be upgraded to one of a higher clock rating. In this case, the Processor is said to be Replaceable. Another example is a power supply Package mounted on sliding rails. All Removable packages are inherently Replaceable.

    
.. _CIM-PhysicalPackage-VendorCompatibilityStrings:

``string[]`` **VendorCompatibilityStrings**

    An array of strings that identify the component that is compatible with, and can be inserted in a slot that reports this string as one of the array element in the VendorCompatibilityStrings This allows system administrators to determine whether it is appropriateto insert a package into a slot 

    In order to ensure uniqueness within the NameSpace, each value defined by the vendor for use in the VendorCompatibilityStrings property SHOULD be constructed using the following 'preferred' algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon ':', and where <OrgID> MUST include a copyrighted, trademarked or otherwise unique name that is owned by the business entity creating/defining the InstanceID, or is a registered ID that is assigned to the business entity by a recognized global authority (This is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness <OrgID> MUST NOT contain a colon (':'). When using this algorithm, the first colon to appear in InstanceID MUST appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and SHOULD not be re-used to identify different underlying (real-world) elements.

    
.. _CIM-PhysicalPackage-Depth:

``real32`` **Depth**

    The depth of the PhysicalPackage in inches.

    
.. _CIM-PhysicalPackage-PackageType:

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
    
.. _CIM-PhysicalPackage-Weight:

``real32`` **Weight**

    The weight of the PhysicalPackage in pounds.

    
.. _CIM-PhysicalPackage-Height:

``real32`` **Height**

    The height of the PhysicalPackage in inches.

    
.. _CIM-PhysicalPackage-OtherPackageType:

``string`` **OtherPackageType**

    A string describing the package when the instance's PackageType property is 1 ("Other").

    

Local methods
^^^^^^^^^^^^^

    .. _CIM-PhysicalPackage-IsCompatible:

``uint32`` **IsCompatible** (:ref:`CIM_PhysicalElement <CIM-PhysicalElement>` ElementToCheck)

    This method is being deprecated. A PhysicalPackage cannot determine if it is compatible with another object. The IsCompatible method verifies whether the referenced PhysicalElement may be contained by or inserted into the PhysicalPackage. The return value should be 0 if the request was successfully executed, 1 if the request is not supported and some other value if an error occurred. In a subclass, the set of possible return codes could be specified, using a ValueMap qualifier on the method. The strings to which the ValueMap contents are 'translated' may also be specified in the subclass as a Values array qualifier.

    
    **Parameters**
    
        *IN* :ref:`CIM_PhysicalElement <CIM-PhysicalElement>` **ElementToCheck**
            The element to check for compatibility with this one.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`SKU <CIM-PhysicalElement-SKU>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`UserTracking <CIM-PhysicalElement-UserTracking>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``string`` :ref:`VendorEquipmentType <CIM-PhysicalElement-VendorEquipmentType>`
| ``string`` :ref:`SerialNumber <CIM-PhysicalElement-SerialNumber>`
| ``datetime`` :ref:`ManufactureDate <CIM-PhysicalElement-ManufactureDate>`
| ``string`` :ref:`Version <CIM-PhysicalElement-Version>`
| ``string`` :ref:`PartNumber <CIM-PhysicalElement-PartNumber>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-PhysicalElement-ElementName>`
| ``boolean`` :ref:`CanBeFRUed <CIM-PhysicalElement-CanBeFRUed>`
| ``string`` :ref:`Description <CIM-PhysicalElement-Description>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``string`` :ref:`Manufacturer <CIM-PhysicalElement-Manufacturer>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`OtherIdentifyingInfo <CIM-PhysicalElement-OtherIdentifyingInfo>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``boolean`` :ref:`PoweredOn <CIM-PhysicalElement-PoweredOn>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`Model <CIM-PhysicalElement-Model>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`Tag <CIM-PhysicalElement-Tag>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`CreationClassName <CIM-PhysicalElement-CreationClassName>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

