.. _CIM-PhysicalElement:

CIM_PhysicalElement
-------------------

Class reference
===============
Subclass of :ref:`CIM_ManagedSystemElement <CIM-ManagedSystemElement>`

Subclasses of CIM_PhysicalElement define any component of a System that has a distinct physical identity. Instances of this class can be defined as an object that can be seen or touched. All Processes, Files, and LogicalDevices are considered not to be Physical Elements. For example, it is not possible to touch the functionality of a 'modem.' You can touch only the card or package that implements the modem. The same card could also implement a LAN adapter. PhysicalElements are tangible ManagedSystemElements that have a physical manifestation of some sort. 



Note that the properties of PhysicalElement describe a hardware entity. Possible replacement (FRU) information is defined by following the ElementFRU association to one or more instances of the ReplacementFRU class. This definition allows a client to determine what hardware can be replaced (FRUed) and what 'spare' parts might be required by a customer or engineer doing the replacement. If it can be instrumented or manually determined that an element actually replaced (FRUed) another, then this can be described in the model using the ElementHasBeenFRUed association.


Key properties
^^^^^^^^^^^^^^

| :ref:`Tag <CIM-PhysicalElement-Tag>`
| :ref:`CreationClassName <CIM-PhysicalElement-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-PhysicalElement-SKU:

``string`` **SKU**

    The stock-keeping unit number for this PhysicalElement.

    
.. _CIM-PhysicalElement-UserTracking:

``string`` **UserTracking**

    User-assigned and writeable asset-tracking identifier for the PhysicalElement.

    
.. _CIM-PhysicalElement-VendorEquipmentType:

``string`` **VendorEquipmentType**

    A vendor-specific hardware type for the PhysicalElement. It describes the specific equipment type for the element, as defined by the vendor or manufacturer.

    
.. _CIM-PhysicalElement-SerialNumber:

``string`` **SerialNumber**

    A manufacturer-allocated number used to identify the Physical Element.

    
.. _CIM-PhysicalElement-ManufactureDate:

``datetime`` **ManufactureDate**

    The date that this PhysicalElement was manufactured.

    
.. _CIM-PhysicalElement-Version:

``string`` **Version**

    A string that indicates the version of the PhysicalElement.

    
.. _CIM-PhysicalElement-PartNumber:

``string`` **PartNumber**

    The part number assigned by the organization that is responsible for producing or manufacturing the PhysicalElement.

    
.. _CIM-PhysicalElement-ElementName:

``string`` **ElementName**

    A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. 

    Note that the Name property of ManagedSystemElement is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. Note that if there is an associated instance of CIM_EnabledLogicalElementCapabilities, restrictions on this properties may exist as defined in ElementNameMask and MaxElementNameLen properties defined in that class.

    
.. _CIM-PhysicalElement-CanBeFRUed:

``boolean`` **CanBeFRUed**

    Boolean that indicates whether this PhysicalElement can be FRUed (TRUE) or not (FALSE).

    
.. _CIM-PhysicalElement-Description:

``string`` **Description**

    A textual description of the PhysicalElement.

    
.. _CIM-PhysicalElement-Manufacturer:

``string`` **Manufacturer**

    The name of the organization responsible for producing the PhysicalElement. This organization might be the entity from whom the Element is purchased, but this is not necessarily true. The latter information is contained in the Vendor property of CIM_Product.

    
.. _CIM-PhysicalElement-OtherIdentifyingInfo:

``string`` **OtherIdentifyingInfo**

    OtherIdentifyingInfo captures data in addition to Tag information. This information could be used to identify a Physical Element. One example is bar code data associated with an Element that also has an asset tag. Note that if only bar code data is available and is unique or able to be used as an Element key, this property would be null and the bar code data would be used as the class key, in the Tag property.

    
.. _CIM-PhysicalElement-PoweredOn:

``boolean`` **PoweredOn**

    Boolean that indicates whether the PhysicalElement is powered on (TRUE) or is currently off (FALSE).

    
.. _CIM-PhysicalElement-Model:

``string`` **Model**

    The name by which the PhysicalElement is generally known.

    
.. _CIM-PhysicalElement-Tag:

``string`` **Tag**

    An arbitrary string that uniquely identifies the Physical Element and serves as the key of the Element. The Tag property can contain information such as asset tag or serial number data. The key for PhysicalElement is placed very high in the object hierarchy in order to independently identify the hardware or entity, regardless of physical placement in or on Cabinets, Adapters, and so on. For example, a hotswappable or removable component can be taken from its containing (scoping) Package and be temporarily unused. The object still continues to exist and can even be inserted into a different scoping container. Therefore, the key for Physical Element is an arbitrary string and is defined independently of any placement or location-oriented hierarchy.

    
.. _CIM-PhysicalElement-CreationClassName:

``string`` **CreationClassName**

    CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

