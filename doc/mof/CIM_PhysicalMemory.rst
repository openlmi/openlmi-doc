.. _CIM-PhysicalMemory:

CIM_PhysicalMemory
------------------

Class reference
===============
Subclass of :ref:`CIM_Chip <CIM-Chip>`

PhysicalMemory is a subclass of CIM_Chip, representing low level memory devices - SIMMS, DIMMs, raw memory chips, etc.


Key properties
^^^^^^^^^^^^^^

| :ref:`Tag <CIM-PhysicalElement-Tag>`
| :ref:`CreationClassName <CIM-PhysicalElement-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-PhysicalMemory-Capacity:

``uint64`` **Capacity**

    The total capacity of this PhysicalMemory, in bytes.

    
.. _CIM-PhysicalMemory-InterleavePosition:

``uint32`` **InterleavePosition**

    The position of this PhysicalMemory in an interleave. 0 indicates non-interleaved. 1 indicates the first position, 2 the second position and so on. For example, in a 2:1 interleave, a value of '1' would indicate that the Memory is in the 'even' position.

    
.. _CIM-PhysicalMemory-MaxMemorySpeed:

``uint32`` **MaxMemorySpeed**

    The maximum speed (in MHz) of PhysicalMemory.

    
.. _CIM-PhysicalMemory-BankLabel:

``string`` **BankLabel**

    A string identifying the physically labeled bank where the Memory is located - for example, 'Bank 0' or 'Bank A'.

    
.. _CIM-PhysicalMemory-IsSpeedInMhz:

``boolean`` **IsSpeedInMhz**

    The IsSpeedInMHz property is used to indicate if the Speed property or the MaxMemorySpeed contains the value of the memory speed. A value of TRUE shall indicate that the speed is represented by the MaxMemorySpeed property. A value of FALSE shall indicate that the speed is represented by the Speed property.

    
.. _CIM-PhysicalMemory-FormFactor:

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
    
.. _CIM-PhysicalMemory-MemoryType:

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
    
.. _CIM-PhysicalMemory-DataWidth:

``uint16`` **DataWidth**

    Data width of the PhysicalMemory, in bits. A data width of 0 and a TotalWidth of 8 would indicate that the Memory is solely used to provide error correction bits.

    
.. _CIM-PhysicalMemory-TotalWidth:

``uint16`` **TotalWidth**

    Total width, in bits, of the PhysicalMemory, including check or error correction bits. If there are no error correction bits, the value in this property should match that specified for DataWidth.

    
.. _CIM-PhysicalMemory-ConfiguredMemoryClockSpeed:

``uint32`` **ConfiguredMemoryClockSpeed**

    The configured clock speed (in MHz) of PhysicalMemory.

    
.. _CIM-PhysicalMemory-PositionInRow:

``uint32`` **PositionInRow**

    Specifies the position of the PhysicalMemory in a 'row'. For example, if it takes two 8-bit memory devices to form a 16- bit row, then a value of '2'means that this Memory is the second device. 0 is an invalid value for this property.

    
.. _CIM-PhysicalMemory-Speed:

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
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``string`` :ref:`VendorEquipmentType <CIM-PhysicalElement-VendorEquipmentType>`
| ``string`` :ref:`SerialNumber <CIM-PhysicalElement-SerialNumber>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`Version <CIM-PhysicalElement-Version>`
| ``boolean`` :ref:`Removable <CIM-PhysicalComponent-Removable>`
| ``string`` :ref:`PartNumber <CIM-PhysicalElement-PartNumber>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``boolean`` :ref:`CanBeFRUed <CIM-PhysicalElement-CanBeFRUed>`
| ``boolean`` :ref:`Replaceable <CIM-PhysicalComponent-Replaceable>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``string`` :ref:`Manufacturer <CIM-PhysicalElement-Manufacturer>`
| ``string`` :ref:`OtherIdentifyingInfo <CIM-PhysicalElement-OtherIdentifyingInfo>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``boolean`` :ref:`PoweredOn <CIM-PhysicalElement-PoweredOn>`
| ``string`` :ref:`ElementName <CIM-PhysicalElement-ElementName>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`Model <CIM-PhysicalElement-Model>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``string`` :ref:`Description <CIM-PhysicalElement-Description>`
| ``datetime`` :ref:`ManufactureDate <CIM-PhysicalElement-ManufactureDate>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint16`` :ref:`RemovalConditions <CIM-PhysicalComponent-RemovalConditions>`
| ``string`` :ref:`Tag <CIM-PhysicalElement-Tag>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`CreationClassName <CIM-PhysicalElement-CreationClassName>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

