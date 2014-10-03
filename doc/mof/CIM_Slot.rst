.. _CIM-Slot:

CIM_Slot
--------

Class reference
===============
Subclass of :ref:`CIM_PhysicalConnector <CIM-PhysicalConnector>`

The Slot class represents Connectors into which Packages are inserted. For example, a PhysicalPackage that is a DiskDrive may be inserted into an SCA 'Slot'. As another example, a Card (subclass of PhysicalPackage) may be inserted into a 16-, 32-, or 64-bit expansion 'Slot' on a HostingBoard. PCI or PCMCIA Type III Slots are examples of the latter.


Key properties
^^^^^^^^^^^^^^

| :ref:`Tag <CIM-PhysicalElement-Tag>`
| :ref:`CreationClassName <CIM-PhysicalElement-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-Slot-Powered:

``boolean`` **Powered**

    **Deprecated!** 
    A boolean indicating whether the Slot is currently powered (TRUE) or not (FALSE).

    
.. _CIM-Slot-PurposeDescription:

``string`` **PurposeDescription**

    A free-form string describing that this Slot is physically unique and may hold special types of hardware. This property only has meaning when the corresponding boolean property, SpecialPurpose, is set to TRUE.

    
.. _CIM-Slot-SpecialPurpose:

``boolean`` **SpecialPurpose**

    Boolean indicating that this Slot is physically unique and may hold special types of hardware, e.g. a graphics processor slot. If set to TRUE, then the property, Special PurposeDescription (a string), should specify the nature of the uniqueness or purpose of the Slot.

    
.. _CIM-Slot-HeightAllowed:

``real32`` **HeightAllowed**

    Maximum height of an adapter Card that can be inserted into the Slot, in inches.

    
.. _CIM-Slot-MaxDataWidth:

``uint16`` **MaxDataWidth**

    Maximum bus width of adapter Cards that can be inserted into this Slot, in bits. If the value is 'unknown', enter 0. If the value is other than 8, 16, 32, 64 or 128, enter 1.

    
.. _CIM-Slot-OpenSwitch:

``boolean`` **OpenSwitch**

    A boolean indicating whether the switch state of the Slot is currently open (TRUE) or closed (FALSE). This switch state determines whether the contents of the Slot can be hot-plugged.

    
.. _CIM-Slot-ConnectorType:

``uint16[]`` **ConnectorType**

    An array of integers defining the type of PhysicalConnector. An array is specified to allow the description of 'combinations' of Connector information. For example, one array entry could specify RS-232 (value=25), another DB-25 (value=23) and a third entry define the Connector as "Male" (value=2). 

    This single property is being deprecated in lieu of using separate properties to describe the various aspects of the connector. The separation allows for a more generic means of describing the connectors. Obsolete connectors were intentionally removed from the new list.

    
    ======== ===============================
    ValueMap Values                         
    ======== ===============================
    0        Unknown                        
    1        Other                          
    2        Male                           
    3        Female                         
    4        Shielded                       
    5        Unshielded                     
    6        SCSI (A) High-Density (50 pins)
    7        SCSI (A) Low-Density (50 pins) 
    8        SCSI (P) High-Density (68 pins)
    9        SCSI SCA-I (80 pins)           
    10       SCSI SCA-II (80 pins)          
    11       Fibre Channel (DB-9, Copper)   
    12       Fibre Channel (Optical Fibre)  
    13       Fibre Channel SCA-II (40 pins) 
    14       Fibre Channel SCA-II (20 pins) 
    15       Fibre Channel BNC              
    16       ATA 3-1/2 Inch (40 pins)       
    17       ATA 2-1/2 Inch (44 pins)       
    18       ATA-2                          
    19       ATA-3                          
    20       ATA/66                         
    21       DB-9                           
    22       DB-15                          
    23       DB-25                          
    24       DB-36                          
    25       RS-232C                        
    26       RS-422                         
    27       RS-423                         
    28       RS-485                         
    29       RS-449                         
    30       V.35                           
    31       X.21                           
    32       IEEE-488                       
    33       AUI                            
    34       UPT Category 3                 
    35       UPT Category 4                 
    36       UPT Category 5                 
    37       BNC                            
    38       RJ11                           
    39       RJ45                           
    40       Fiber MIC                      
    41       Apple AUI                      
    42       Apple GeoPort                  
    43       PCI                            
    44       ISA                            
    45       EISA                           
    46       VESA                           
    47       PCMCIA                         
    48       PCMCIA Type I                  
    49       PCMCIA Type II                 
    50       PCMCIA Type III                
    51       ZV Port                        
    52       CardBus                        
    53       USB                            
    54       IEEE 1394                      
    55       HIPPI                          
    56       HSSDC (6 pins)                 
    57       GBIC                           
    58       DIN                            
    59       Mini-DIN                       
    60       Micro-DIN                      
    61       PS/2                           
    62       Infrared                       
    63       HP-HIL                         
    64       Access.bus                     
    65       NuBus                          
    66       Centronics                     
    67       Mini-Centronics                
    68       Mini-Centronics Type-14        
    69       Mini-Centronics Type-20        
    70       Mini-Centronics Type-26        
    71       Bus Mouse                      
    72       ADB                            
    73       AGP                            
    74       VME Bus                        
    75       VME64                          
    76       Proprietary                    
    77       Proprietary Processor Card Slot
    78       Proprietary Memory Card Slot   
    79       Proprietary I/O Riser Slot     
    80       PCI-66MHZ                      
    81       AGP2X                          
    82       AGP4X                          
    83       PC-98                          
    84       PC-98-Hireso                   
    85       PC-H98                         
    86       PC-98Note                      
    87       PC-98Full                      
    88       SSA SCSI                       
    89       Circular                       
    90       On Board IDE Connector         
    91       On Board Floppy Connector      
    92       9 Pin Dual Inline              
    93       25 Pin Dual Inline             
    94       50 Pin Dual Inline             
    95       68 Pin Dual Inline             
    96       On Board Sound Connector       
    97       Mini-jack                      
    98       PCI-X                          
    99       Sbus IEEE 1396-1993 32 bit     
    100      Sbus IEEE 1396-1993 64 bit     
    101      MCA                            
    102      GIO                            
    103      XIO                            
    104      HIO                            
    105      NGIO                           
    106      PMC                            
    107      MTRJ                           
    108      VF-45                          
    109      Future I/O                     
    110      SC                             
    111      SG                             
    112      Electrical                     
    113      Optical                        
    114      Ribbon                         
    115      GLM                            
    116      1x9                            
    117      Mini SG                        
    118      LC                             
    119      HSSC                           
    120      VHDCI Shielded (68 pins)       
    121      InfiniBand                     
    122      AGP8X                          
    ======== ===============================
    
.. _CIM-Slot-VendorCompatibilityStrings:

``string[]`` **VendorCompatibilityStrings**

    An array of strings that identify the components that are compatible and can be inserted in a slot. This allows vendors to provide clues to the system administrators by providing sufficient information to request the appropriate hardware that can populate the slot. In order to ensure uniqueness within the NameSpace, each value defined by the vendor for use in the VendorCompatibilityStrings property SHOULD be constructed using the following 'preferred' algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon ':', and where <OrgID> MUST include a copyrighted, trademarked or otherwise unique name that is owned by the business entity creating/defining the InstanceID, or is a registered ID that is assigned to the business entity by a recognized global authority (This is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness <OrgID> MUST NOT contain a colon (':'). When using this algorithm, the first colon to appear in InstanceID MUST appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and SHOULD not be re-used to identify different underlying (real-world) elements.

    
.. _CIM-Slot-SupportsHotPlug:

``boolean`` **SupportsHotPlug**

    Boolean indicating whether the Slot supports hot-plug of adapter Cards.

    
.. _CIM-Slot-VppMixedVoltageSupport:

``uint16[]`` **VppMixedVoltageSupport**

    An array of enumerated integers indicating the Vpp voltage supported by this Slot.

    
    ======== =======
    ValueMap Values 
    ======== =======
    0        Unknown
    1        Other  
    2        3.3V   
    3        5V     
    4        12V    
    ======== =======
    
.. _CIM-Slot-PoweredOn:

``boolean`` **PoweredOn**

    Boolean that indicates whether the PhysicalElement is powered on (TRUE) or is currently off (FALSE).

    
.. _CIM-Slot-ThermalRating:

``uint32`` **ThermalRating**

    Maximum thermal dissipation of the Slot in milliwatts.

    
.. _CIM-Slot-VccMixedVoltageSupport:

``uint16[]`` **VccMixedVoltageSupport**

    An array of enumerated integers indicating the Vcc voltage supported by this Slot.

    
    ======== =======
    ValueMap Values 
    ======== =======
    0        Unknown
    1        Other  
    2        3.3V   
    3        5V     
    ======== =======
    
.. _CIM-Slot-LengthAllowed:

``real32`` **LengthAllowed**

    Maximum length of an adapter Card that can be inserted into the Slot, in inches.

    
.. _CIM-Slot-MaxLinkWidth:

``uint16`` **MaxLinkWidth**

    Maximum link width of a switching bus type, such as Infiniband and PCI Express. The width is expressed in number of communication lines, or lanes, between port and devices. This property dictates the maximum link width, in lanes, of adapter Cards that can be inserted into this Slot. If the value is 'unknown', enter 0.

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Unknown      
    2        x1           
    3        x2           
    4        x4           
    5        x8           
    6        x12          
    7        x16          
    8        x32          
    9..      DMTF Reserved
    ======== =============
    
.. _CIM-Slot-Number:

``uint16`` **Number**

    The Number property indicates the physical slot number, which can be used as an index into a system slot table, whether or not that slot is physically occupied.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string[]`` :ref:`OtherElectricalCharacteristics <CIM-PhysicalConnector-OtherElectricalCharacteristics>`
| ``string`` :ref:`SKU <CIM-PhysicalElement-SKU>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`UserTracking <CIM-PhysicalElement-UserTracking>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``string`` :ref:`VendorEquipmentType <CIM-PhysicalElement-VendorEquipmentType>`
| ``string`` :ref:`OtherIdentifyingInfo <CIM-PhysicalElement-OtherIdentifyingInfo>`
| ``datetime`` :ref:`ManufactureDate <CIM-PhysicalElement-ManufactureDate>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`Version <CIM-PhysicalElement-Version>`
| ``uint16`` :ref:`ConnectorGender <CIM-PhysicalConnector-ConnectorGender>`
| ``string`` :ref:`PartNumber <CIM-PhysicalElement-PartNumber>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ConnectorDescription <CIM-PhysicalConnector-ConnectorDescription>`
| ``boolean`` :ref:`CanBeFRUed <CIM-PhysicalElement-CanBeFRUed>`
| ``uint16`` :ref:`ConnectorLayout <CIM-PhysicalConnector-ConnectorLayout>`
| ``string`` :ref:`Description <CIM-PhysicalElement-Description>`
| ``uint16[]`` :ref:`ConnectorElectricalCharacteristics <CIM-PhysicalConnector-ConnectorElectricalCharacteristics>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``string`` :ref:`Manufacturer <CIM-PhysicalElement-Manufacturer>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`SerialNumber <CIM-PhysicalElement-SerialNumber>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``string`` :ref:`ElementName <CIM-PhysicalElement-ElementName>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`OtherTypeDescription <CIM-PhysicalConnector-OtherTypeDescription>`
| ``string`` :ref:`Model <CIM-PhysicalElement-Model>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint32`` :ref:`NumPhysicalPins <CIM-PhysicalConnector-NumPhysicalPins>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`Tag <CIM-PhysicalElement-Tag>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`CreationClassName <CIM-PhysicalElement-CreationClassName>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string`` :ref:`ConnectorPinout <CIM-PhysicalConnector-ConnectorPinout>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

