.. _LMI-LUKSFormat:

LMI_LUKSFormat
--------------

Class reference
===============
Subclass of :ref:`LMI_EncryptionFormat <LMI-EncryptionFormat>`

Class representing LUKS data on a block device.


Key properties
^^^^^^^^^^^^^^

| :ref:`Name <LMI-DataFormat-Name>`
| :ref:`CSName <LMI-DataFormat-CSName>`
| :ref:`CSCreationClassName <LMI-DataFormat-CSCreationClassName>`
| :ref:`CreationClassName <LMI-DataFormat-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-LUKSFormat-UUID:

``string`` **UUID**

    UUID of the LUKS format.

    
.. _LMI-LUKSFormat-SlotStatus:

``uint16[]`` **SlotStatus**

    Represents status of each key slot in LUKS header.

    
    ======== ======
    ValueMap Values
    ======== ======
    0        Free  
    1        Used  
    ======== ======
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``string`` :ref:`CSName <LMI-DataFormat-CSName>`
| ``string`` :ref:`FormatTypeDescription <LMI-DataFormat-FormatTypeDescription>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``uint16`` :ref:`FormatType <LMI-DataFormat-FormatType>`
| ``string`` :ref:`Name <LMI-DataFormat-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``string`` :ref:`CSCreationClassName <LMI-DataFormat-CSCreationClassName>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`CreationClassName <LMI-DataFormat-CreationClassName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`

