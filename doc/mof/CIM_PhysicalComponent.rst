.. _CIM-PhysicalComponent:

CIM_PhysicalComponent
---------------------

Class reference
===============
Subclass of :ref:`CIM_PhysicalElement <CIM-PhysicalElement>`

The PhysicalComponent class represents any low-level or basic Component within a Package. A Component object either can not or does not need to be decomposed into its constituent parts. For example, an ASIC (or Chip) can not be further decomposed. A tape for data storage (PhysicalMedia) does not need to be decomposed. Any PhysicalElement that is not a Link, Connector, or Package is a descendent (or member) of this class. For example, the UART chipset on an internal modem Card would be a subclass (if additional properties or associations are defined) or an instance of PhysicalComponent.


Key properties
^^^^^^^^^^^^^^

| :ref:`Tag <CIM-PhysicalElement-Tag>`
| :ref:`CreationClassName <CIM-PhysicalElement-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-PhysicalComponent-HotSwappable:

``boolean`` **HotSwappable**

    The use of this property is being deprecated. Instead RemovalConditions should be used. The RemovalConditions property addresses whether a PhysicalComponent is removable with or without power being applied. 

    

    A PhysicalComponent is HotSwappable if it is possible to replace the Element with a physically different but equivalent one while the containing Package has power applied to it (ie, is 'on'). For example, a fan Component may be designed to be HotSwappable. All HotSwappable Components are inherently Removable and Replaceable.

    
.. _CIM-PhysicalComponent-Removable:

``boolean`` **Removable**

    The use of this property is being deprecated. Instead RemovalConditions should be used. The RemovalConditions property addresses whether a PhysicalComponent is removable with or without power being applied. 

    

    A PhysicalComponent is Removable if it is designed to be taken in and out of the physical container in which it is normally found, without impairing the function of the overall packaging. A Component can still be Removable if power must be 'off' in order to perform the removal. If power can be 'on' and the Component removed, then the Element is both Removable and HotSwappable. For example, an upgradeable Processor chip is Removable.

    
.. _CIM-PhysicalComponent-Replaceable:

``boolean`` **Replaceable**

    **Deprecated!** 
    The use of this property is being deprecated because it is redundant with the FRU class and its associations. A PhysicalComponent is Replaceable if it is possible to replace (FRU or upgrade) the Element with a physically different one. For example, some ComputerSystems allow the main Processor chip to be upgraded to one of a higher clock rating. In this case, the Processor is said to be Replaceable. All Removable Components are inherently Replaceable.

    
.. _CIM-PhysicalComponent-RemovalConditions:

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

