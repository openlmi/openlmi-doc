.. _CIM-Card:

CIM_Card
--------

Class reference
===============
Subclass of :ref:`CIM_PhysicalPackage <CIM-PhysicalPackage>`

The Card class represents a type of physical container that can be plugged into another Card or HostingBoard, or is itself a HostingBoard/Motherboard in a Chassis. The CIM_Card class includes any package capable of carrying signals and providing a mounting point for PhysicalComponents, such as Chips, or other PhysicalPackages, such as other Cards.


Key properties
^^^^^^^^^^^^^^

| :ref:`Tag <CIM-PhysicalElement-Tag>`
| :ref:`CreationClassName <CIM-PhysicalElement-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-Card-OperatingVoltages:

``sint16[]`` **OperatingVoltages**

    Operating voltages required by the Card.

    
.. _CIM-Card-HostingBoard:

``boolean`` **HostingBoard**

    Boolean indicating that this Card is a Motherboard or, more generically, a baseboard in a Chassis.

    
.. _CIM-Card-RequirementsDescription:

``string`` **RequirementsDescription**

    A free-form string describing the way(s) in which this Card is physically unique from other Cards. This property only has meaning when the corresponding boolean property, SpecialRequirements, is set to TRUE.

    
.. _CIM-Card-SlotLayout:

``string`` **SlotLayout**

    SlotLayout is a free-form string that describes the slot positioning, typical usage, restrictions, individual slot spacings or any other pertinent information for the slots on a Card.

    
.. _CIM-Card-SpecialRequirements:

``boolean`` **SpecialRequirements**

    Boolean indicating that this Card is physically unique from other Cards of the same type and therefore requires a special Slot. For example, a double-wide Card requires two Slots. Another example is where a certain Card may be used for the same general function as other Cards but requires a special Slot (e.g., extra long), whereas the other Cards can be placed in any available Slot. If set to TRUE, then the corresponding property, RequirementsDescription, should specify the nature of the uniqueness or purpose of the Card.

    
.. _CIM-Card-RequiresDaughterBoard:

``boolean`` **RequiresDaughterBoard**

    Boolean indicating that at least one daughterboard or auxiliary Card is required in order to function properly.

    

Local methods
^^^^^^^^^^^^^

    .. _CIM-Card-ConnectorPower:

``uint32`` **ConnectorPower** (:ref:`CIM_PhysicalConnector <CIM-PhysicalConnector>` Connector, ``boolean`` PoweredOn)

    This method manipulates the power to a PhysicalConnector on a Card. It is intended to be used by a Card (especially by a motherboard - i.e., HostingBoard=TRUE) to turn the power on and off for a specific PhysicalConnector located on it. For example, in a personal computer, a system slot does not know how to turn itself on and off. However, the motherboard hosting this slot may have that capability. This is important in order to support hot swapping of an adapter card in a system slot. The method should return 0 if successful, 1 if the request is not supported, and some other value if any other error occurred. In a subclass, the set of possible return codes could be specified, using a ValueMap qualifier on the method. The strings to which the ValueMap contents are 'translated' may also be specified in the subclass as a Values array qualifier.

    
    **Parameters**
    
        *IN* :ref:`CIM_PhysicalConnector <CIM-PhysicalConnector>` **Connector**
            The connector to change the power setting for.

            
        
        *IN* ``boolean`` **PoweredOn**
            If TRUE, turn power on for the connector. If FALSE, turn power off.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``boolean`` :ref:`HotSwappable <CIM-PhysicalPackage-HotSwappable>`
| ``string`` :ref:`SKU <CIM-PhysicalElement-SKU>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`UserTracking <CIM-PhysicalElement-UserTracking>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``string`` :ref:`VendorEquipmentType <CIM-PhysicalElement-VendorEquipmentType>`
| ``string`` :ref:`SerialNumber <CIM-PhysicalElement-SerialNumber>`
| ``datetime`` :ref:`ManufactureDate <CIM-PhysicalElement-ManufactureDate>`
| ``real32`` :ref:`Width <CIM-PhysicalPackage-Width>`
| ``string`` :ref:`Version <CIM-PhysicalElement-Version>`
| ``boolean`` :ref:`Removable <CIM-PhysicalPackage-Removable>`
| ``string`` :ref:`PartNumber <CIM-PhysicalElement-PartNumber>`
| ``uint16`` :ref:`RemovalConditions <CIM-PhysicalPackage-RemovalConditions>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-PhysicalElement-ElementName>`
| ``boolean`` :ref:`CanBeFRUed <CIM-PhysicalElement-CanBeFRUed>`
| ``string`` :ref:`Description <CIM-PhysicalElement-Description>`
| ``boolean`` :ref:`Replaceable <CIM-PhysicalPackage-Replaceable>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``string[]`` :ref:`VendorCompatibilityStrings <CIM-PhysicalPackage-VendorCompatibilityStrings>`
| ``string`` :ref:`Manufacturer <CIM-PhysicalElement-Manufacturer>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`OtherIdentifyingInfo <CIM-PhysicalElement-OtherIdentifyingInfo>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``boolean`` :ref:`PoweredOn <CIM-PhysicalElement-PoweredOn>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``real32`` :ref:`Depth <CIM-PhysicalPackage-Depth>`
| ``uint16`` :ref:`PackageType <CIM-PhysicalPackage-PackageType>`
| ``string`` :ref:`Model <CIM-PhysicalElement-Model>`
| ``real32`` :ref:`Weight <CIM-PhysicalPackage-Weight>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``real32`` :ref:`Height <CIM-PhysicalPackage-Height>`
| ``string`` :ref:`Tag <CIM-PhysicalElement-Tag>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`CreationClassName <CIM-PhysicalElement-CreationClassName>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string`` :ref:`OtherPackageType <CIM-PhysicalPackage-OtherPackageType>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`IsCompatible <CIM-PhysicalPackage-IsCompatible>`

