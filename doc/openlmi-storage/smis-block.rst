SMI-S Block Services Package
============================

This package is core of SMI-S. It describes how devices (disks) are grouped
together into pools with different capabilities and even hierarchy of pools can
be built.

    A StoragePool is a storage element; its storage capacity has a given set
    of capabilities. Those ‘StorageCapabilities’ indicate the 'Quality of
    Service' requirements that can be applied to objects created from the
    StoragePool.

Storage on Linux does not use pool concept except Volume Groups, therefore we
allow to create storage devices directly from other storage devices, e.g.
create MD RAID from partitions.

Primordial pool
---------------
At the lowest level of hierarchy of SMI-S storage pools are primordial devices
and pools.

    A primordial StoragePool is a type of StoragePool that contains
    unformatted, unprepared, or unassigned capacity. Storage capacity is drawn
    from the primordial StoragePool to create concrete StoragePools. A
    primordial StoragePool aggregates storage capacity not assigned to a
    concrete StoragePool. StorageVolumes and LogicalDisks are allocated from
    concrete StoragePools.

    At least one primordial StoragePool shall always exists on the block
    storage system to represent the unallocated storage on the storage device.

OpenLMI-Storage uses raw disk as primordial. Everything else (partitions, RAIDs,
logical volumes, ...) are not primordial.

Logical disks
-------------
In SMI-S, only LogicalDisks instances can be used by the OS. I.e. if an admin
wants to build a filesystem e.g. on RAIDCompositeExtent, in SMI-S it's
necessary to allocate a LogicalDisk from it.

We find this approach useless and we don't allocate LogicalDisks for devices,
which can be used by the OS. In fact, any block device can be used by the OS,
therefore it would make sense to make ``LMI_StorageExtent`` as subclass of
``CIM_LogicalDisk``.

Implementation
--------------

Classes
^^^^^^^

Implemented SMI-S classes:

* :ref:`LMI_VGAssociatedComponentExtent <LMI-VGAssociatedComponentExtent>`

* :ref:`LMI_MDRAIDBasedOn <LMI-MDRAIDBasedOn>`

* :ref:`LMI_LVBasedOn <LMI-LVBasedOn>`

* :ref:`LMI_LVAllocatedFromStoragePool <LMI-LVAllocatedFromStoragePool>`

* :ref:`LMI_LVElementCapabilities <LMI-LVElementCapabilities>`

* :ref:`LMI_VGElementCapabilities <LMI-VGElementCapabilities>`

* :ref:`LMI_MDRAIDElementCapabilities <LMI-MDRAIDElementCapabilities>`

* :ref:`LMI_MDRAIDElementSettingData <LMI-MDRAIDElementSettingData>`

* :ref:`LMI_LVElementSettingData <LMI-LVElementSettingData>`

* :ref:`LMI_VGElementSettingData <LMI-VGElementSettingData>`

* :ref:`LMI_StorageExtent <LMI-StorageExtent>`

* :ref:`LMI_LVStorageExtent <LMI-LVStorageExtent>`

* :ref:`LMI_MDRAIDStorageExtent <LMI-MDRAIDStorageExtent>`

* :ref:`LMI_StorageConfigurationService <LMI-StorageConfigurationService>`

* :ref:`LMI_VGStoragePool <LMI-VGStoragePool>`

* :ref:`LMI_VGStorageCapabilities <LMI-VGStorageCapabilities>`

* :ref:`LMI_LVStorageCapabilities <LMI-LVStorageCapabilities>`

* :ref:`LMI_MDRAIDStorageCapabilities <LMI-MDRAIDStorageCapabilities>`

* :ref:`LMI_VGStorageSetting <LMI-VGStorageSetting>`

* :ref:`LMI_MDRAIDStorageSetting <LMI-MDRAIDStorageSetting>`

* :ref:`LMI_LVStorageSetting <LMI-LVStorageSetting>`

Methods
^^^^^^^

Implemented:

* :ref:`CreateOrModifyStoragePool <LMI-StorageConfigurationService-CreateOrModifyStoragePool>`
  (creates Volume Group from list of block devices).

* :ref:`CreateOrModifyElementFromElements <LMI-StorageConfigurationService-CreateOrModifyElementFromElements>`
  (creates MD RAID from list of block devices).

* :ref:`CreateOrModifyElementFromStoragePool <LMI-StorageConfigurationService-CreateOrModifyElementFromStoragePool>`
  (creates logical Volumes from a Volume Group).

* :ref:`CreateOrModifyMDRAID <LMI-StorageConfigurationService-CreateOrModifyMDRAID>`

* :ref:`CreateOrModifyVG <LMI-StorageConfigurationService-CreateOrModifyVG>`

* :ref:`CreateOrModifyLV <LMI-StorageConfigurationService-CreateOrModifyLV>`

.. warning:: Mandatory indications are **not** implemented.

