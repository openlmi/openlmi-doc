.. _LMI-DataFormat:

LMI_DataFormat
--------------

Class reference
===============
Subclass of :ref:`CIM_EnabledLogicalElement <CIM-EnabledLogicalElement>`

Base class for all content formats.


Key properties
^^^^^^^^^^^^^^

| :ref:`Name <LMI-DataFormat-Name>`
| :ref:`CSName <LMI-DataFormat-CSName>`
| :ref:`CSCreationClassName <LMI-DataFormat-CSCreationClassName>`
| :ref:`CreationClassName <LMI-DataFormat-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-DataFormat-CSName:

``string`` **CSName**

    The scoping System's Name. Note that this class was originally defined in the scope of a ComputerSystem, and was later allowed to be scoped by any System (for example, a computer or application system). Unfortunately, the property name, CSName, could not be changed (for example, to SystemName) without deprecating the class. This change was not deemed critical to the semantics and therefore did not merit deprecation. So, the property name remains.

    
.. _LMI-DataFormat-FormatTypeDescription:

``string`` **FormatTypeDescription**

    Textual description of the data format.

    
.. _LMI-DataFormat-FormatType:

``uint16`` **FormatType**

    Type of the data format.

    
    ======== ================
    ValueMap Values          
    ======== ================
    1        Swap            
    2        MD RAID member  
    3        Physical Volume 
    4        LUKS            
    5        BIOS Boot       
    6        DM RAID member  
    7        Multipath member
    8        PPC PReP Boot   
    65535    Other           
    ======== ================
    
.. _LMI-DataFormat-Name:

``string`` **Name**

    The inherited Name serves as key of a FileSystem instance within a ComputerSystem.

    
.. _LMI-DataFormat-CSCreationClassName:

``string`` **CSCreationClassName**

    The scoping System's CreationClassName. Note that this class was originally defined in the scope of a ComputerSystem, and was later allowed to be scoped by any System (for example, a computer or application system). Unfortunately, the property name, CSCreationClassName, could not be changed (for example, to SystemCreationClass Name) without deprecating the class. This change was not deemed critical to the semantics and therefore did not merit deprecation. So, the property name remains.

    
.. _LMI-DataFormat-CreationClassName:

``string`` **CreationClassName**

    CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`

