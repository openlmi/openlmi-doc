.. _CIM-BIOSFeature:

CIM_BIOSFeature
---------------

Class reference
===============
Subclass of :ref:`CIM_SoftwareFeature <CIM-SoftwareFeature>`

BIOSFeature represents the capabilities of the low-level software that is used to bring up and configure a Computer System.


Key properties
^^^^^^^^^^^^^^

| :ref:`Version <CIM-SoftwareFeature-Version>`
| :ref:`Vendor <CIM-SoftwareFeature-Vendor>`
| :ref:`Name <CIM-SoftwareFeature-Name>`
| :ref:`IdentifyingNumber <CIM-SoftwareFeature-IdentifyingNumber>`
| :ref:`ProductName <CIM-SoftwareFeature-ProductName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-BIOSFeature-CharacteristicDescriptions:

``string[]`` **CharacteristicDescriptions**

    An array of free-form strings providing more detailed explanations for any of the BIOS features indicated in the Characteristics array. Note, each entry of this array is related to the entry in the Characteristics array that is located at the same index.

    
.. _CIM-BIOSFeature-Characteristics:

``uint16[]`` **Characteristics**

    An array of integers that specify the features supported by the BIOS. For example, one can specify that PnP capabilities are provided (value=9) or that infrared devices are supported (21). Values specified in the enumeration are taken from both DMI and SMBIOS (the Type 0 structure, the BIOS Characteristics and BIOS Characteristics Extension Bytes attributes.

    
    ======== ============================
    ValueMap Values                      
    ======== ============================
    1        Other                       
    2        Unknown                     
    3        Undefined                   
    4        ISA Support                 
    5        MCA Support                 
    6        EISA Support                
    7        PCI Support                 
    8        PCMCIA Support              
    9        PnP Support                 
    10       APM Support                 
    11       Upgradeable BIOS            
    12       BIOS Shadowing Allowed      
    13       VL VESA Support             
    14       ESCD Support                
    15       LS-120 Boot Support         
    16       ACPI Support                
    17       I2O Boot Support            
    18       USB Legacy Support          
    19       AGP Support                 
    20       PC Card                     
    21       IR                          
    22       1394                        
    23       I2C                         
    24       Smart Battery               
    25       ATAPI ZIP Drive Boot Support
    26       1394 Boot Support           
    27       Boot from CD                
    28       Selectable Boot             
    29       BIOS ROM is Socketed        
    30       Boot from PCMCIA            
    31       EDD Specification Support   
    160      PC-98                       
    ======== ============================
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`Vendor <CIM-SoftwareFeature-Vendor>`
| ``string`` :ref:`Name <CIM-SoftwareFeature-Name>`
| ``string`` :ref:`IdentifyingNumber <CIM-SoftwareFeature-IdentifyingNumber>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`ProductName <CIM-SoftwareFeature-ProductName>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`Version <CIM-SoftwareFeature-Version>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

