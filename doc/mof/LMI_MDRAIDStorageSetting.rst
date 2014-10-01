.. _LMI-MDRAIDStorageSetting:

LMI_MDRAIDStorageSetting
------------------------

Class reference
===============
Subclass of :ref:`LMI_StorageSetting <LMI-StorageSetting>`

This class defines characteristics of LMI_MDRAIDStorageExtent which is created or modified by CreateOrModifyElementFromElements method in the LMI_StorageConfigurationService.

Currently no additional properties are necessary in this class, redundancy and stripping is defined by DataRedundancy, PackageRedundancy and ExtentStripeLength.

In future, this class may introduce MD RAID properties like metadata format, additional parity layouts etc.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

*None*

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint64`` :ref:`InterconnectSpeed <CIM-StorageSetting-InterconnectSpeed>`
| ``uint16`` :ref:`InterconnectType <CIM-StorageSetting-InterconnectType>`
| ``uint8`` :ref:`DeltaReservationGoal <CIM-StorageSetting-DeltaReservationGoal>`
| ``uint16`` :ref:`DataRedundancyMin <LMI-StorageSetting-DataRedundancyMin>`
| ``uint16`` :ref:`UseReplicationBuffer <CIM-StorageSetting-UseReplicationBuffer>`
| ``string`` :ref:`InstanceID <CIM-SettingData-InstanceID>`
| ``uint16`` :ref:`LowSpaceWarningThreshold <CIM-StorageSetting-LowSpaceWarningThreshold>`
| ``uint16`` :ref:`DiskType <CIM-StorageSetting-DiskType>`
| ``boolean`` :ref:`NoSinglePointOfFailure <LMI-StorageSetting-NoSinglePointOfFailure>`
| ``string`` :ref:`SubsystemID <CIM-StorageSetting-SubsystemID>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`ParityLayout <LMI-StorageSetting-ParityLayout>`
| ``uint16`` :ref:`DataOrganization <CIM-StorageSetting-DataOrganization>`
| ``uint16`` :ref:`PackageRedundancyMax <LMI-StorageSetting-PackageRedundancyMax>`
| ``uint64`` :ref:`UserDataStripeDepthMin <CIM-StorageSetting-UserDataStripeDepthMin>`
| ``string`` :ref:`EmulatedDevice <CIM-StorageSetting-EmulatedDevice>`
| ``uint16`` :ref:`CompressionRate <CIM-StorageSetting-CompressionRate>`
| ``uint16`` :ref:`ThinProvisionedPoolType <CIM-StorageSetting-ThinProvisionedPoolType>`
| ``uint16`` :ref:`FormFactorType <CIM-StorageSetting-FormFactorType>`
| ``string`` :ref:`ConfigurationName <CIM-SettingData-ConfigurationName>`
| ``uint16`` :ref:`ExtentStripeLength <LMI-StorageSetting-ExtentStripeLength>`
| ``boolean`` :ref:`CompressedElement <CIM-StorageSetting-CompressedElement>`
| ``string`` :ref:`CUImage <CIM-StorageSetting-CUImage>`
| ``string`` :ref:`SoOrgID <CIM-SettingData-SoOrgID>`
| ``boolean`` :ref:`PersistentReplica <CIM-StorageSetting-PersistentReplica>`
| ``uint16`` :ref:`InitialSynchronization <CIM-StorageSetting-InitialSynchronization>`
| ``uint16`` :ref:`Encryption <CIM-StorageSetting-Encryption>`
| ``uint16`` :ref:`StorageExtentInitialUsage <CIM-StorageSetting-StorageExtentInitialUsage>`
| ``uint16`` :ref:`ExtentStripeLengthMin <LMI-StorageSetting-ExtentStripeLengthMin>`
| ``string`` :ref:`ElementName <CIM-SettingData-ElementName>`
| ``uint64`` :ref:`ThinProvisionedInitialReserve <CIM-StorageSetting-ThinProvisionedInitialReserve>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16`` :ref:`DataRedundancyGoal <LMI-StorageSetting-DataRedundancyGoal>`
| ``uint16`` :ref:`PortType <CIM-StorageSetting-PortType>`
| ``boolean`` :ref:`IncrementalDeltas <CIM-StorageSetting-IncrementalDeltas>`
| ``uint16`` :ref:`StoragePoolInitialUsage <CIM-StorageSetting-StoragePoolInitialUsage>`
| ``string`` :ref:`SoID <CIM-SettingData-SoID>`
| ``uint16`` :ref:`ReplicationPriority <CIM-StorageSetting-ReplicationPriority>`
| ``uint16`` :ref:`ChangeableType <LMI-StorageSetting-ChangeableType>`
| ``uint8`` :ref:`DeltaReservationMin <CIM-StorageSetting-DeltaReservationMin>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint32`` :ref:`RPM <CIM-StorageSetting-RPM>`
| ``uint64`` :ref:`UserDataStripeDepthMax <CIM-StorageSetting-UserDataStripeDepthMax>`
| ``uint64`` :ref:`SpaceLimit <CIM-StorageSetting-SpaceLimit>`
| ``uint16`` :ref:`SpaceLimitWarningThreshold <CIM-StorageSetting-SpaceLimitWarningThreshold>`
| ``uint16`` :ref:`ExtentStripeLengthMax <LMI-StorageSetting-ExtentStripeLengthMax>`
| ``string[]`` :ref:`ComponentSetting <CIM-SettingData-ComponentSetting>`
| ``uint16`` :ref:`PackageRedundancyGoal <LMI-StorageSetting-PackageRedundancyGoal>`
| ``uint8`` :ref:`DeltaReservationMax <CIM-StorageSetting-DeltaReservationMax>`
| ``uint16`` :ref:`DataRedundancyMax <LMI-StorageSetting-DataRedundancyMax>`
| ``uint64`` :ref:`UserDataStripeDepth <CIM-StorageSetting-UserDataStripeDepth>`
| ``uint16`` :ref:`PackageRedundancyMin <LMI-StorageSetting-PackageRedundancyMin>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`CloneSetting <LMI-StorageSetting-CloneSetting>`

