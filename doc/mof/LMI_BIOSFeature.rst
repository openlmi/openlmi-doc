.. _LMI-BIOSFeature:

LMI_BIOSFeature
---------------

Class reference
===============
Subclass of :ref:`CIM_BIOSFeature <CIM-BIOSFeature>`

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

.. _LMI-BIOSFeature-CharacteristicDescriptions:

``string[]`` **CharacteristicDescriptions**

    An array of free-form strings providing more detailed explanations for any of the BIOS features indicated in the Characteristics array. Note, each entry of this array is related to the entry in the Characteristics array that is located at the same index.

    
.. _LMI-BIOSFeature-ElementName:

``string`` **ElementName**

    A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. 

    Note that the Name property of ManagedSystemElement is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. Note that if there is an associated instance of CIM_EnabledLogicalElementCapabilities, restrictions on this properties may exist as defined in ElementNameMask and MaxElementNameLen properties defined in that class.

    
.. _LMI-BIOSFeature-Vendor:

``string`` **Vendor**

    The scoping Product's supplier.

    
.. _LMI-BIOSFeature-Description:

``string`` **Description**

    The Description property provides a textual description of the object.

    
.. _LMI-BIOSFeature-IdentifyingNumber:

``string`` **IdentifyingNumber**

    The scoping Product's identification.

    
.. _LMI-BIOSFeature-InstanceID:

``string`` **InstanceID**

    InstanceID is an optional property that may be used to opaquely and uniquely identify an instance of this class within the scope of the instantiating Namespace. Various subclasses of this class may override this property to make it required, or a key. Such subclasses may also modify the preferred algorithms for ensuring uniqueness that are defined below.

    To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon (:), and where <OrgID> must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness, <OrgID> must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If not null and the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance. 

    If not set to null for DMTF-defined instances, the "preferred" algorithm must be used with the <OrgID> set to CIM.

    
.. _LMI-BIOSFeature-Characteristics:

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
    
.. _LMI-BIOSFeature-ProductName:

``string`` **ProductName**

    The scoping Product's commonly used name.

    
.. _LMI-BIOSFeature-Caption:

``string`` **Caption**

    The Caption property is a short textual description (one- line string) of the object.

    
.. _LMI-BIOSFeature-Version:

``string`` **Version**

    The scoping Product's version.

    
.. _LMI-BIOSFeature-Name:

``string`` **Name**

    The Name property defines the unique label by which the SoftwareFeature is identified. This label should be a human-readable name that uniquely identifies the element in the context of the element's namespace.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

