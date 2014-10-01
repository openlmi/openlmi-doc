.. _CIM-PhysicalConnector:

CIM_PhysicalConnector
---------------------

Class reference
===============
Subclass of :ref:`CIM_PhysicalElement <CIM-PhysicalElement>`

The PhysicalConnector class represents any PhysicalElement that is used to connect to other Elements. Any object that can be used to connect and transmit signals or power between two or more PhysicalElements is a descendant (or member) of this class. For example, Slots and D-shell connectors are types of PhysicalConnectors.


Key properties
^^^^^^^^^^^^^^

| :ref:`Tag <CIM-PhysicalElement-Tag>`
| :ref:`CreationClassName <CIM-PhysicalElement-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-PhysicalConnector-OtherElectricalCharacteristics:

``string[]`` **OtherElectricalCharacteristics**

    A string describing the connector's electrical characteristics - used when the ConnectorElectricalCharacteristics property contains an entry of 1 (Other). OtherElectricalCharacteristics should be set to NULL when ConnectorElectricalCharacteristics does not contain an value of 1.

    
.. _CIM-PhysicalConnector-ConnectorGender:

``uint16`` **ConnectorGender**

    Describes the gender of the connector.

    
    ======== =======
    ValueMap Values 
    ======== =======
    0        Unknown
    2        Male   
    3        Female 
    ======== =======
    
.. _CIM-PhysicalConnector-ConnectorDescription:

``string`` **ConnectorDescription**

    A string describing the Connector - used when the ConnectorLayout property is set to 1 ("Other"). Connector Description should be set to NULL when ConnectorLayout is any value other than 1.

    
.. _CIM-PhysicalConnector-ConnectorLayout:

``uint16`` **ConnectorLayout**

    Describes the type of packaging normally associated with this type of connector.16 (PCI) - describes the generic PCI connector layout. 17 (PCI-X) - describes the PCI Extended connector layout. 18 (PCI-E) - describes the PCI Express connector layout, where the actual layout as far as the length is concerned is unknown. 19 - 25 (PCI-E xN) - describes the PCI Express connector layout, where N is the lane count that appropriately descirbes the length of the PCI-E connector.

    
    ============ =================
    ValueMap     Values           
    ============ =================
    0            Unknown          
    1            Other            
    2            RS232            
    3            BNC              
    4            RJ11             
    5            RJ45             
    6            DB9              
    7            Slot             
    8            SCSI High Density
    9            SCSI Low Density 
    10           Ribbon           
    11           AUI              
    12           Fiber SC         
    13           Fiber ST         
    14           FDDI-MIC         
    15           Fiber-RTMJ       
    16           PCI              
    17           PCI-X            
    18           PCI-E            
    19           PCI-E x1         
    20           PCI-E x2         
    21           PCI-E x4         
    22           PCI-E x8         
    23           PCI-E x16        
    24           PCI-E x32        
    25           PCI-E x64        
    26..32567    DMTF Reserved    
    32568..65535 Vendor Reserved  
    ============ =================
    
.. _CIM-PhysicalConnector-ConnectorElectricalCharacteristics:

``uint16[]`` **ConnectorElectricalCharacteristics**

    Describes the electrical characteristic for this connector.

    
    ======== ========================
    ValueMap Values                  
    ======== ========================
    0        Unknown                 
    1        Other                   
    2        Single Ended            
    3        Differential            
    4        Low Voltage Differential
    5        Optical                 
    6        Copper                  
    7        Shielded                
    8        Unshielded              
    ======== ========================
    
.. _CIM-PhysicalConnector-ConnectorType:

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
    
.. _CIM-PhysicalConnector-OtherTypeDescription:

``string`` **OtherTypeDescription**

    A string describing the Connector - used when the ConnectorType property is set to 1 ("Other"). OtherType Description should be set to NULL when ConnectorType is any value other than 1. 

    The use of this property is deprecated in lieu of Connector Description.

    
.. _CIM-PhysicalConnector-NumPhysicalPins:

``uint32`` **NumPhysicalPins**

    Describes the number of physical pins (male/female) that are present on this connector.

    
.. _CIM-PhysicalConnector-ConnectorPinout:

``string`` **ConnectorPinout**

    A free-form string describing the pin configuration and/or signal usage of a PhysicalConnector.

    

Local methods
^^^^^^^^^^^^^

*None*

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
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
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
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`Tag <CIM-PhysicalElement-Tag>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`CreationClassName <CIM-PhysicalElement-CreationClassName>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

