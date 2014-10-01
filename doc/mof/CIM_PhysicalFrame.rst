.. _CIM-PhysicalFrame:

CIM_PhysicalFrame
-----------------

Class reference
===============
Subclass of :ref:`CIM_PhysicalPackage <CIM-PhysicalPackage>`

PhysicalFrame is a superclass of Rack, Chassis and other frame enclosures, as they are defined in extension classes. Properties like visible or audible alarm, and data related to security breaches are in this superclass.


Key properties
^^^^^^^^^^^^^^

| :ref:`Tag <CIM-PhysicalElement-Tag>`
| :ref:`CreationClassName <CIM-PhysicalElement-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-PhysicalFrame-SecurityBreach:

``uint16`` **SecurityBreach**

    SecurityBreach is an enumerated, integer-valued property indicating whether a physical breach of the Frame was attempted but unsuccessful (value=4) or attempted and successful (5). Also, the values, "Unknown", "Other" or "No Breach", can be specified.

    
    ======== =================
    ValueMap Values           
    ======== =================
    1        Other            
    2        Unknown          
    3        No Breach        
    4        Breach Attempted 
    5        Breach Successful
    ======== =================
    
.. _CIM-PhysicalFrame-AudibleAlarm:

``boolean`` **AudibleAlarm**

    Boolean indicating whether the Frame is equipped with an audible alarm.

    
.. _CIM-PhysicalFrame-LockPresent:

``boolean`` **LockPresent**

    Boolean indicating whether the Frame is protected with a lock.

    
.. _CIM-PhysicalFrame-BreachDescription:

``string`` **BreachDescription**

    BreachDescription is a free-form string providing more information if the SecurityBreach property indicates that a breach or some other security-related event occurred.

    
.. _CIM-PhysicalFrame-ServiceDescriptions:

``string[]`` **ServiceDescriptions**

    An array of free-form strings providing more detailed explanations for any of the entries in the Service Philosophy array. Note, each entry of this array is related to the entry in ServicePhilosophy that is located at the same index.

    
.. _CIM-PhysicalFrame-VisibleAlarm:

``boolean`` **VisibleAlarm**

    Boolean indicating that the equipment includes a visible alarm.

    
.. _CIM-PhysicalFrame-ServicePhilosophy:

``uint16[]`` **ServicePhilosophy**

    ServicePhilosophy is an enumerated, integer-valued array that indicates whether the Frame is serviced from the top (value=2), front (3), back (4) or side (5), whether it has sliding trays (6) or removable sides (7), and/or whether the Frame is moveable (8), for example, having rollers.

    
    ======== ==================
    ValueMap Values            
    ======== ==================
    0        Unknown           
    1        Other             
    2        Service From Top  
    3        Service From Front
    4        Service From Back 
    5        Service From Side 
    6        Sliding Trays     
    7        Removable Sides   
    8        Moveable          
    ======== ==================
    
.. _CIM-PhysicalFrame-IsLocked:

``boolean`` **IsLocked**

    Boolean indicating that the Frame is currently locked.

    
.. _CIM-PhysicalFrame-CableManagementStrategy:

``string`` **CableManagementStrategy**

    CableManagementStrategy is a free-form string that contains information on how the various cables are connected and bundled for the Frame. With many networking, storage-related and power cables, cable management can be a complex and challenging endeavor. This string property contains information to aid in assembly and service of the Frame.

    

Local methods
^^^^^^^^^^^^^

*None*

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
| ``boolean`` :ref:`Removable <CIM-PhysicalPackage-Removable>`
| ``string`` :ref:`PartNumber <CIM-PhysicalElement-PartNumber>`
| ``uint16`` :ref:`RemovalConditions <CIM-PhysicalPackage-RemovalConditions>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-PhysicalElement-ElementName>`
| ``boolean`` :ref:`CanBeFRUed <CIM-PhysicalElement-CanBeFRUed>`
| ``string`` :ref:`Description <CIM-PhysicalElement-Description>`
| ``boolean`` :ref:`Replaceable <CIM-PhysicalPackage-Replaceable>`
| ``string`` :ref:`Tag <CIM-PhysicalElement-Tag>`
| ``string[]`` :ref:`VendorCompatibilityStrings <CIM-PhysicalPackage-VendorCompatibilityStrings>`
| ``string`` :ref:`Manufacturer <CIM-PhysicalElement-Manufacturer>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`OtherIdentifyingInfo <CIM-PhysicalElement-OtherIdentifyingInfo>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``boolean`` :ref:`PoweredOn <CIM-PhysicalElement-PoweredOn>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``real32`` :ref:`Depth <CIM-PhysicalPackage-Depth>`
| ``uint16`` :ref:`PackageType <CIM-PhysicalPackage-PackageType>`
| ``string`` :ref:`Model <CIM-PhysicalElement-Model>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``real32`` :ref:`Weight <CIM-PhysicalPackage-Weight>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``real32`` :ref:`Height <CIM-PhysicalPackage-Height>`
| ``string`` :ref:`Version <CIM-PhysicalElement-Version>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`CreationClassName <CIM-PhysicalElement-CreationClassName>`
| ``string`` :ref:`OtherPackageType <CIM-PhysicalPackage-OtherPackageType>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`IsCompatible <CIM-PhysicalPackage-IsCompatible>`

