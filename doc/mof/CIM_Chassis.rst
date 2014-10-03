.. _CIM-Chassis:

CIM_Chassis
-----------

Class reference
===============
Subclass of :ref:`CIM_PhysicalFrame <CIM-PhysicalFrame>`

The Chassis class represents the PhysicalElements that enclose other Elements and provide definable functionality, such as a desktop, processing node, UPS, disk or tape storage, or a combination of these.


Key properties
^^^^^^^^^^^^^^

| :ref:`Tag <CIM-PhysicalElement-Tag>`
| :ref:`CreationClassName <CIM-PhysicalElement-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-Chassis-InputCurrentType:

``uint16`` **InputCurrentType**

    Enumeration indicating whether the input voltage required by the Chassis is:

    Unknown indicates the InputCurrentType is unknown

    Other indicates that InputCurrentType is not one of the enumerated values. OtherInputCurrentType may have more information.

    AC indicates that the InputCurrentType is Alternating Current (AC)

    DC indicates that the InputCurrentType is Direct Current (DC)

    
    ======== =======
    ValueMap Values 
    ======== =======
    0        Unknown
    1        Other  
    2        AC     
    3        DC     
    ======== =======
    
.. _CIM-Chassis-MultipleSystemSupport:

``uint16`` **MultipleSystemSupport**

    MultipleSystemSupport indicates whether or not this chassis supports multiple systems, for example server blades.

    
    ======== =======
    ValueMap Values 
    ======== =======
    0        Unknown
    1        True   
    2        False  
    ======== =======
    
.. _CIM-Chassis-ChassisPackageType:

``uint16`` **ChassisPackageType**

    ChassisPackageType indicates the physical form factor for the type of Chassis. This property may have a value when the PackageType property contains the value 3 "Chassis Frame".

    A value of 28 "Blade Enclosure" shall indicate the Chassis is designed to contain one or more PhysicalPackage(s) of PackageType 16 "Blade" or PackageType 17 "Blade Expansion".

    
    ============== =====================
    ValueMap       Values               
    ============== =====================
    0              Unknown              
    1              Other                
    2              SMBIOS Reserved      
    3              Desktop              
    4              Low Profile Desktop  
    5              Pizza Box            
    6              Mini Tower           
    7              Tower                
    8              Portable             
    9              LapTop               
    10             Notebook             
    11             Hand Held            
    12             Docking Station      
    13             All in One           
    14             Sub Notebook         
    15             Space-Saving         
    16             Lunch Box            
    17             Main System Chassis  
    18             Expansion Chassis    
    19             SubChassis           
    20             Bus Expansion Chassis
    21             Peripheral Chassis   
    22             Storage Chassis      
    23             SMBIOS Reseved       
    24             Sealed-Case PC       
    25             SMBIOS Reserved      
    26             CompactPCI           
    27             AdvancedTCA          
    28             Blade Enclosure      
    ..             DMTF Reserved        
    0x8000..0xFFFF Vendor Reserved      
    ============== =====================
    
.. _CIM-Chassis-ChassisTypeDescription:

``string`` **ChassisTypeDescription**

    A string providing more information on the ChassisPackageType.

    
.. _CIM-Chassis-CurrentRequiredOrProduced:

``sint16`` **CurrentRequiredOrProduced**

    Current required by the Chassis at 120V. If power is provided by the Chassis (as in the case of a UPS), this property may indicate the amperage produced, as a negative number.

    
.. _CIM-Chassis-TypeDescriptions:

``string[]`` **TypeDescriptions**

    **Deprecated!** 
    The use of this property is deprecated in lieu of a single value property, ChassisTypeDescription. 

    An array of free-form strings providing more information on the ChassisTypes array entries. Note, each entry of this array is related to the entry in ChassisTypes that is located at the same index.

    
.. _CIM-Chassis-NumberOfPowerCords:

``uint16`` **NumberOfPowerCords**

    Integer indicating the number of power cords which must be connected to the Chassis, for all the componentry to operate.

    
.. _CIM-Chassis-OtherInputCurrentType:

``string`` **OtherInputCurrentType**

    A string describing the input current type when the value of the instance's InputCurrentType property is ("Other").

    
.. _CIM-Chassis-InputVoltage:

``sint32`` **InputVoltage**

    A signed integer indicating the input voltage required by the Chassis. If the value of this property is unknown, it SHOULD have a value of 0. If the value of InputCurrentType is "Unknown", this property SHOULD have a value of 0.

    
.. _CIM-Chassis-RackMountable:

``uint16`` **RackMountable**

    RackMountable indicates whether or not the chassis is Rack Mountable.

    
    ======== =======
    ValueMap Values 
    ======== =======
    0        Unknown
    1        True   
    2        False  
    ======== =======
    
.. _CIM-Chassis-ChassisTypes:

``uint16[]`` **ChassisTypes**

    The use of this property is deprecated in lieu of ChassisPackageType. A physical package should not have multiple form factors. Therefore, this property is being deprecated in lieu of a single value property. 

    An enumerated, integer-valued array indicating the type of Chassis.

    
    ======== =====================
    ValueMap Values               
    ======== =====================
    1        Other                
    2        Unknown              
    3        Desktop              
    4        Low Profile Desktop  
    5        Pizza Box            
    6        Mini Tower           
    7        Tower                
    8        Portable             
    9        LapTop               
    10       Notebook             
    11       Hand Held            
    12       Docking Station      
    13       All in One           
    14       Sub Notebook         
    15       Space-Saving         
    16       Lunch Box            
    17       Main System Chassis  
    18       Expansion Chassis    
    19       SubChassis           
    20       Bus Expansion Chassis
    21       Peripheral Chassis   
    22       Storage Chassis      
    23       Rack Mount Chassis   
    24       Sealed-Case PC       
    25       Multi-system Chassis 
    ======== =====================
    
.. _CIM-Chassis-HeatGeneration:

``uint16`` **HeatGeneration**

    Amount of heat generated by the Chassis in BTU/hour.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``boolean`` :ref:`HotSwappable <CIM-PhysicalPackage-HotSwappable>`
| ``string`` :ref:`SKU <CIM-PhysicalElement-SKU>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string`` :ref:`UserTracking <CIM-PhysicalElement-UserTracking>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``string`` :ref:`VendorEquipmentType <CIM-PhysicalElement-VendorEquipmentType>`
| ``string`` :ref:`SerialNumber <CIM-PhysicalElement-SerialNumber>`
| ``datetime`` :ref:`ManufactureDate <CIM-PhysicalElement-ManufactureDate>`
| ``real32`` :ref:`Width <CIM-PhysicalPackage-Width>`
| ``boolean`` :ref:`Removable <CIM-PhysicalPackage-Removable>`
| ``uint16`` :ref:`SecurityBreach <CIM-PhysicalFrame-SecurityBreach>`
| ``string`` :ref:`PartNumber <CIM-PhysicalElement-PartNumber>`
| ``uint16`` :ref:`RemovalConditions <CIM-PhysicalPackage-RemovalConditions>`
| ``boolean`` :ref:`AudibleAlarm <CIM-PhysicalFrame-AudibleAlarm>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`ElementName <CIM-PhysicalElement-ElementName>`
| ``boolean`` :ref:`CanBeFRUed <CIM-PhysicalElement-CanBeFRUed>`
| ``string`` :ref:`Description <CIM-PhysicalElement-Description>`
| ``boolean`` :ref:`Replaceable <CIM-PhysicalPackage-Replaceable>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``boolean`` :ref:`LockPresent <CIM-PhysicalFrame-LockPresent>`
| ``string`` :ref:`Tag <CIM-PhysicalElement-Tag>`
| ``string`` :ref:`BreachDescription <CIM-PhysicalFrame-BreachDescription>`
| ``string[]`` :ref:`VendorCompatibilityStrings <CIM-PhysicalPackage-VendorCompatibilityStrings>`
| ``string`` :ref:`Manufacturer <CIM-PhysicalElement-Manufacturer>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`OtherIdentifyingInfo <CIM-PhysicalElement-OtherIdentifyingInfo>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string[]`` :ref:`ServiceDescriptions <CIM-PhysicalFrame-ServiceDescriptions>`
| ``boolean`` :ref:`VisibleAlarm <CIM-PhysicalFrame-VisibleAlarm>`
| ``boolean`` :ref:`PoweredOn <CIM-PhysicalElement-PoweredOn>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``uint16[]`` :ref:`ServicePhilosophy <CIM-PhysicalFrame-ServicePhilosophy>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``boolean`` :ref:`IsLocked <CIM-PhysicalFrame-IsLocked>`
| ``uint16`` :ref:`PackageType <CIM-PhysicalPackage-PackageType>`
| ``string`` :ref:`Model <CIM-PhysicalElement-Model>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``real32`` :ref:`Weight <CIM-PhysicalPackage-Weight>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``real32`` :ref:`Depth <CIM-PhysicalPackage-Depth>`
| ``real32`` :ref:`Height <CIM-PhysicalPackage-Height>`
| ``string`` :ref:`Version <CIM-PhysicalElement-Version>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`CableManagementStrategy <CIM-PhysicalFrame-CableManagementStrategy>`
| ``string`` :ref:`CreationClassName <CIM-PhysicalElement-CreationClassName>`
| ``string`` :ref:`OtherPackageType <CIM-PhysicalPackage-OtherPackageType>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`IsCompatible <CIM-PhysicalPackage-IsCompatible>`

