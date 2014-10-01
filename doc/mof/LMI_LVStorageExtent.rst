.. _LMI-LVStorageExtent:

LMI_LVStorageExtent
-------------------

Class reference
===============
Subclass of :ref:`LMI_StorageExtent <LMI-StorageExtent>`

This class represents Logical Volume devices on the managed system.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-LVStorageExtent-ElementName:

``string`` **ElementName**

    Name of the Logical Volume.

    
.. _LMI-LVStorageExtent-UUID:

``string`` **UUID**

    UUID of the Logical Volume.

    
.. _LMI-LVStorageExtent-ThinlyProvisioned:

``boolean`` **ThinlyProvisioned**

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint8`` :ref:`DeltaReservation <CIM-StorageExtent-DeltaReservation>`
| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``boolean`` :ref:`IsBasedOnUnderlyingRedundancy <CIM-StorageExtent-IsBasedOnUnderlyingRedundancy>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <LMI-StorageExtent-InstanceID>`
| ``uint64`` :ref:`ExtentStripeLength <LMI-StorageExtent-ExtentStripeLength>`
| ``boolean`` :ref:`IsCompressed <CIM-StorageExtent-IsCompressed>`
| ``uint16`` :ref:`DataOrganization <CIM-StorageExtent-DataOrganization>`
| ``uint16`` :ref:`Access <CIM-StorageExtent-Access>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``boolean`` :ref:`Primordial <LMI-StorageExtent-Primordial>`
| ``string`` :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| ``boolean`` :ref:`ErrorCleared <CIM-LogicalDevice-ErrorCleared>`
| ``boolean`` :ref:`NoSinglePointOfFailure <LMI-StorageExtent-NoSinglePointOfFailure>`
| ``uint16`` :ref:`Usage <CIM-StorageExtent-Usage>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint64`` :ref:`PowerOnHours <CIM-LogicalDevice-PowerOnHours>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`DeviceBusType <LMI-StorageExtent-DeviceBusType>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string`` :ref:`OtherNameNamespace <CIM-StorageExtent-OtherNameNamespace>`
| ``uint16`` :ref:`NameNamespace <LMI-StorageExtent-NameNamespace>`
| ``string[]`` :ref:`IdentifyingDescriptions <CIM-LogicalDevice-IdentifyingDescriptions>`
| ``uint64`` :ref:`ExtentInterleaveDepth <CIM-StorageExtent-ExtentInterleaveDepth>`
| ``string`` :ref:`OtherNameFormat <CIM-StorageExtent-OtherNameFormat>`
| ``uint16`` :ref:`NameFormat <LMI-StorageExtent-NameFormat>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``boolean`` :ref:`IsConcatenated <CIM-StorageExtent-IsConcatenated>`
| ``string`` :ref:`Purpose <CIM-StorageExtent-Purpose>`
| ``uint16[]`` :ref:`ClientSettableUsage <CIM-StorageExtent-ClientSettableUsage>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16`` :ref:`LocationIndicator <CIM-LogicalDevice-LocationIndicator>`
| ``uint16`` :ref:`CompressionState <CIM-StorageExtent-CompressionState>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string[]`` :ref:`OtherIdentifyingInfo <CIM-LogicalDevice-OtherIdentifyingInfo>`
| ``string`` :ref:`Name <LMI-StorageExtent-Name>`
| ``uint16[]`` :ref:`PowerManagementCapabilities <CIM-LogicalDevice-PowerManagementCapabilities>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint64`` :ref:`BlockSize <LMI-StorageExtent-BlockSize>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``boolean`` :ref:`SequentialAccess <CIM-StorageExtent-SequentialAccess>`
| ``uint16[]`` :ref:`AdditionalAvailability <CIM-LogicalDevice-AdditionalAvailability>`
| ``string`` :ref:`OtherUsageDescription <CIM-StorageExtent-OtherUsageDescription>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``boolean`` :ref:`IsComposite <LMI-StorageExtent-IsComposite>`
| ``uint16`` :ref:`StatusInfo <CIM-LogicalDevice-StatusInfo>`
| ``string`` :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| ``string[]`` :ref:`ExtentDiscriminator <LMI-StorageExtent-ExtentDiscriminator>`
| ``uint16`` :ref:`PackageRedundancy <LMI-StorageExtent-PackageRedundancy>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint16`` :ref:`DataRedundancy <LMI-StorageExtent-DataRedundancy>`
| ``uint64`` :ref:`NumberOfBlocks <LMI-StorageExtent-NumberOfBlocks>`
| ``uint64`` :ref:`MaxQuiesceTime <CIM-LogicalDevice-MaxQuiesceTime>`
| ``uint64`` :ref:`TotalPowerOnHours <CIM-LogicalDevice-TotalPowerOnHours>`
| ``string`` :ref:`ErrorDescription <CIM-LogicalDevice-ErrorDescription>`
| ``uint16`` :ref:`CompressionRate <CIM-StorageExtent-CompressionRate>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <LMI-StorageExtent-OperationalStatus>`
| ``uint32`` :ref:`LastErrorCode <CIM-LogicalDevice-LastErrorCode>`
| ``string[]`` :ref:`Names <LMI-StorageExtent-Names>`
| ``string`` :ref:`ErrorMethodology <CIM-StorageExtent-ErrorMethodology>`
| ``string`` :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| ``uint16[]`` :ref:`ExtentStatus <LMI-StorageExtent-ExtentStatus>`
| ``uint16`` :ref:`Availability <CIM-LogicalDevice-Availability>`
| ``string`` :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`
| ``uint64`` :ref:`ConsumableBlocks <LMI-StorageExtent-ConsumableBlocks>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`Reset <CIM-LogicalDevice-Reset>`
| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`
| :ref:`SetPowerState <CIM-LogicalDevice-SetPowerState>`
| :ref:`QuiesceDevice <CIM-LogicalDevice-QuiesceDevice>`
| :ref:`EnableDevice <CIM-LogicalDevice-EnableDevice>`
| :ref:`OnlineDevice <CIM-LogicalDevice-OnlineDevice>`
| :ref:`SaveProperties <CIM-LogicalDevice-SaveProperties>`
| :ref:`RestoreProperties <CIM-LogicalDevice-RestoreProperties>`

