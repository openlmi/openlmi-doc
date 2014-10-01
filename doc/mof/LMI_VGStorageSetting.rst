.. _LMI-VGStorageSetting:

LMI_VGStorageSetting
--------------------

Class reference
===============
Subclass of :ref:`LMI_StorageSetting <LMI-StorageSetting>`

This class defines characteristics of LMI_VGStoragePool which is created or modified by CreateOrModifyStoragePool method in the LMI_StorageConfigurationService.

Currently only ExtentSize property is supported.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-VGStorageSetting-ExtentSize:

``uint64`` **ExtentSize**

    Size of extents of the Volume Group. The default is 4 MiB and it must be at least 1 MiB and a power of 2. Once this value has been set, it is difficult to change it without recreating the volume group which would involve backing up and restoring data on any logical volumes. 

    If the volume group metadata uses lvm1 format, extents can vary in size from 8KB to 16GB and there is a limit of 65534 extents in each logical volume.  The default of 4 MiB leads to a maximum logical volume size of around 256GiB.

    If the volume group metadata uses lvm2 format those restrictions do not apply, but having a large number of extents will slow down the tools but have no impact on I/O performance to the logical volume.  The smallest PE is 1KiB.

    

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
| ``string`` :ref:`SoID <CIM-SettingData-SoID>`
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

