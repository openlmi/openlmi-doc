.. _LMI-PVFormat:

LMI_PVFormat
------------

Class reference
===============
Subclass of :ref:`LMI_DataFormat <LMI-DataFormat>`

This class represents Physical Volume metadata present on a StorageExtent. The StorageExtent can be member of existing Volume Group or its Volume Group has been destroyed.


Key properties
^^^^^^^^^^^^^^

| :ref:`Name <LMI-DataFormat-Name>`
| :ref:`CSName <LMI-DataFormat-CSName>`
| :ref:`CSCreationClassName <LMI-DataFormat-CSCreationClassName>`
| :ref:`CreationClassName <LMI-DataFormat-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-PVFormat-UUID:

``string`` **UUID**

    UUID of the Physical Volume.

    

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
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``uint16`` :ref:`FormatType <LMI-DataFormat-FormatType>`
| ``string`` :ref:`Name <LMI-DataFormat-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`CSCreationClassName <LMI-DataFormat-CSCreationClassName>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`CreationClassName <LMI-DataFormat-CreationClassName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`

