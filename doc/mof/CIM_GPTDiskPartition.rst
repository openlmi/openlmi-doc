.. _CIM-GPTDiskPartition:

CIM_GPTDiskPartition
--------------------

Class reference
===============
Subclass of :ref:`CIM_GenericDiskPartition <CIM-GenericDiskPartition>`

GPT is a newer partitioning style that supports volumes larger than the 2 terabyte max of other partition styles. GPT in general is associated with PC X86 architectures, but GPT partitions are OS and platform independent. GPT uses 16 byte GUIDs (Globally Unique IDs) for certain properties. The DeviceId property inherited from LogicalDevice should be a GUID for GPTDiskPartitions; this string property should be formatted as a 32 character string with two text bytes representing each binary byte. GPT specifications call for a Protective MBR table (PMBR) in block 0 followed by an GPT (GUID Partition Table). The MBR must describe a single active partition - the GPT Partition that occupies the rest of the disk. The user only sees the GPT style partitions in this second MBR partition. This could be modelled as two tiers, but since the specification requires this precise behavior with no management at the MBR level, only the GPT style partitions are exposed through the CIM model.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-GPTDiskPartition-PartitionType:

``string`` **PartitionType**

    The PartitionType as defined in the GPT specs and platform specific documentation - GUID format. This string property MUST be formatted with two text bytes representing each binary byte.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint8`` :ref:`DeltaReservation <CIM-StorageExtent-DeltaReservation>`
| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint64`` :ref:`BlockSize <CIM-StorageExtent-BlockSize>`
| ``boolean`` :ref:`Allocatable <CIM-MediaPartition-Allocatable>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``uint16[]`` :ref:`ClientSettableUsage <CIM-StorageExtent-ClientSettableUsage>`
| ``string[]`` :ref:`ExtentDiscriminator <CIM-StorageExtent-ExtentDiscriminator>`
| ``string[]`` :ref:`OtherIdentifyingInfo <CIM-LogicalDevice-OtherIdentifyingInfo>`
| ``uint16`` :ref:`DataOrganization <CIM-StorageExtent-DataOrganization>`
| ``uint16`` :ref:`Access <CIM-StorageExtent-Access>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``boolean`` :ref:`Primordial <CIM-StorageExtent-Primordial>`
| ``string`` :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| ``boolean`` :ref:`ErrorCleared <CIM-LogicalDevice-ErrorCleared>`
| ``boolean`` :ref:`NoSinglePointOfFailure <CIM-StorageExtent-NoSinglePointOfFailure>`
| ``uint16`` :ref:`Usage <CIM-StorageExtent-Usage>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``string`` :ref:`SignatureAlgorithm <CIM-MediaPartition-SignatureAlgorithm>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string`` :ref:`OtherNameNamespace <CIM-StorageExtent-OtherNameNamespace>`
| ``uint64`` :ref:`ExtentInterleaveDepth <CIM-StorageExtent-ExtentInterleaveDepth>`
| ``string[]`` :ref:`IdentifyingDescriptions <CIM-LogicalDevice-IdentifyingDescriptions>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`OtherNameFormat <CIM-StorageExtent-OtherNameFormat>`
| ``uint16`` :ref:`NameFormat <CIM-StorageExtent-NameFormat>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``string`` :ref:`Purpose <CIM-StorageExtent-Purpose>`
| ``uint64`` :ref:`ExtentStripeLength <CIM-StorageExtent-ExtentStripeLength>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``boolean`` :ref:`IsBasedOnUnderlyingRedundancy <CIM-StorageExtent-IsBasedOnUnderlyingRedundancy>`
| ``uint16`` :ref:`LocationIndicator <CIM-LogicalDevice-LocationIndicator>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``boolean`` :ref:`Extendable <CIM-MediaPartition-Extendable>`
| ``boolean`` :ref:`IsCompressed <CIM-StorageExtent-IsCompressed>`
| ``string`` :ref:`Name <CIM-StorageExtent-Name>`
| ``uint16[]`` :ref:`PowerManagementCapabilities <CIM-LogicalDevice-PowerManagementCapabilities>`
| ``boolean`` :ref:`Bootable <CIM-MediaPartition-Bootable>`
| ``uint16`` :ref:`CompressionState <CIM-StorageExtent-CompressionState>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``boolean`` :ref:`SequentialAccess <CIM-StorageExtent-SequentialAccess>`
| ``uint16[]`` :ref:`AdditionalAvailability <CIM-LogicalDevice-AdditionalAvailability>`
| ``string`` :ref:`OtherUsageDescription <CIM-StorageExtent-OtherUsageDescription>`
| ``uint16`` :ref:`NameNamespace <CIM-StorageExtent-NameNamespace>`
| ``boolean`` :ref:`IsComposite <CIM-StorageExtent-IsComposite>`
| ``uint16`` :ref:`StatusInfo <CIM-LogicalDevice-StatusInfo>`
| ``string`` :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| ``string`` :ref:`Signature <CIM-MediaPartition-Signature>`
| ``uint16`` :ref:`PackageRedundancy <CIM-StorageExtent-PackageRedundancy>`
| ``uint64`` :ref:`PowerOnHours <CIM-LogicalDevice-PowerOnHours>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint16`` :ref:`DataRedundancy <CIM-StorageExtent-DataRedundancy>`
| ``uint64`` :ref:`NumberOfBlocks <CIM-StorageExtent-NumberOfBlocks>`
| ``uint64`` :ref:`MaxQuiesceTime <CIM-LogicalDevice-MaxQuiesceTime>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint64`` :ref:`TotalPowerOnHours <CIM-LogicalDevice-TotalPowerOnHours>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`ErrorDescription <CIM-LogicalDevice-ErrorDescription>`
| ``uint16`` :ref:`CompressionRate <CIM-StorageExtent-CompressionRate>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``boolean`` :ref:`IsConcatenated <CIM-StorageExtent-IsConcatenated>`
| ``uint32`` :ref:`LastErrorCode <CIM-LogicalDevice-LastErrorCode>`
| ``string`` :ref:`ErrorMethodology <CIM-StorageExtent-ErrorMethodology>`
| ``string`` :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| ``uint16[]`` :ref:`ExtentStatus <CIM-StorageExtent-ExtentStatus>`
| ``string`` :ref:`SignatureState <CIM-MediaPartition-SignatureState>`
| ``uint16`` :ref:`Availability <CIM-LogicalDevice-Availability>`
| ``string`` :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`
| ``uint64`` :ref:`ConsumableBlocks <CIM-StorageExtent-ConsumableBlocks>`

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

