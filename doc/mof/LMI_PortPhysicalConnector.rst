.. _LMI-PortPhysicalConnector:

LMI_PortPhysicalConnector
-------------------------

Class reference
===============
Subclass of :ref:`CIM_PhysicalConnector <CIM-PhysicalConnector>`

The PhysicalConnector class represents any PhysicalElement that is used to connect to other Elements. Any object that can be used to connect and transmit signals or power between two or more PhysicalElements is a descendant (or member) of this class. For example, Slots and D-shell connectors are types of PhysicalConnectors.


Key properties
^^^^^^^^^^^^^^

| :ref:`Tag <CIM-PhysicalElement-Tag>`
| :ref:`CreationClassName <CIM-PhysicalElement-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-PortPhysicalConnector-InstanceID:

``string`` **InstanceID**

    InstanceID is an optional property that may be used to opaquely and uniquely identify an instance of this class within the scope of the instantiating Namespace. Various subclasses of this class may override this property to make it required, or a key. Such subclasses may also modify the preferred algorithms for ensuring uniqueness that are defined below.

    To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon (:), and where <OrgID> must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness, <OrgID> must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If not null and the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance. 

    If not set to null for DMTF-defined instances, the "preferred" algorithm must be used with the <OrgID> set to CIM.

    
.. _LMI-PortPhysicalConnector-ConnectorGender:

``uint16`` **ConnectorGender**

    Describes the gender of the connector.

    
    ======== =======
    ValueMap Values 
    ======== =======
    0        Unknown
    2        Male   
    3        Female 
    ======== =======
    
.. _LMI-PortPhysicalConnector-ConnectorDescription:

``string`` **ConnectorDescription**

    A string describing the Connector - used when the ConnectorLayout property is set to 1 ("Other"). Connector Description should be set to NULL when ConnectorLayout is any value other than 1.

    
.. _LMI-PortPhysicalConnector-ElementName:

``string`` **ElementName**

    A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. 

    Note that the Name property of ManagedSystemElement is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. Note that if there is an associated instance of CIM_EnabledLogicalElementCapabilities, restrictions on this properties may exist as defined in ElementNameMask and MaxElementNameLen properties defined in that class.

    
.. _LMI-PortPhysicalConnector-ConnectorLayout:

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
    
.. _LMI-PortPhysicalConnector-Description:

``string`` **Description**

    A textual description of the PhysicalElement.

    
.. _LMI-PortPhysicalConnector-Name:

``string`` **Name**

    The Name property defines the label by which the object is known. When subclassed, the Name property can be overridden to be a Key property.

    
.. _LMI-PortPhysicalConnector-Caption:

``string`` **Caption**

    The Caption property is a short textual description (one- line string) of the object.

    
.. _LMI-PortPhysicalConnector-Tag:

``string`` **Tag**

    An arbitrary string that uniquely identifies the Physical Element and serves as the key of the Element. The Tag property can contain information such as asset tag or serial number data. The key for PhysicalElement is placed very high in the object hierarchy in order to independently identify the hardware or entity, regardless of physical placement in or on Cabinets, Adapters, and so on. For example, a hotswappable or removable component can be taken from its containing (scoping) Package and be temporarily unused. The object still continues to exist and can even be inserted into a different scoping container. Therefore, the key for Physical Element is an arbitrary string and is defined independently of any placement or location-oriented hierarchy.

    
.. _LMI-PortPhysicalConnector-CreationClassName:

``string`` **CreationClassName**

    CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

    

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
| ``string`` :ref:`VendorEquipmentType <CIM-PhysicalElement-VendorEquipmentType>`
| ``string`` :ref:`SerialNumber <CIM-PhysicalElement-SerialNumber>`
| ``datetime`` :ref:`ManufactureDate <CIM-PhysicalElement-ManufactureDate>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`Version <CIM-PhysicalElement-Version>`
| ``string`` :ref:`PartNumber <CIM-PhysicalElement-PartNumber>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``boolean`` :ref:`CanBeFRUed <CIM-PhysicalElement-CanBeFRUed>`
| ``uint16[]`` :ref:`ConnectorElectricalCharacteristics <CIM-PhysicalConnector-ConnectorElectricalCharacteristics>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16[]`` :ref:`ConnectorType <CIM-PhysicalConnector-ConnectorType>`
| ``string`` :ref:`Manufacturer <CIM-PhysicalElement-Manufacturer>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`OtherIdentifyingInfo <CIM-PhysicalElement-OtherIdentifyingInfo>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``boolean`` :ref:`PoweredOn <CIM-PhysicalElement-PoweredOn>`
| ``string`` :ref:`OtherTypeDescription <CIM-PhysicalConnector-OtherTypeDescription>`
| ``string`` :ref:`Model <CIM-PhysicalElement-Model>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint32`` :ref:`NumPhysicalPins <CIM-PhysicalConnector-NumPhysicalPins>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`ConnectorPinout <CIM-PhysicalConnector-ConnectorPinout>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

