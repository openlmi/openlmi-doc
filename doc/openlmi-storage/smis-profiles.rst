.. _smis-profiles:

SMI-S profiles
==============

This chapter lists SMI-S profiles implemented by OpenLMI-Storage. The
implementation does not follow SMI-S strictly and deviates from it where SMI-S
model cannot be used. Each such deviation is appropriately marked.

OpenLMI-Storage implements following profiles:

.. toctree::
   :maxdepth: 2

   smis-partitions
   smis-block
   smis-composition
   smis-filesystem
   smis-jobs
   smis-block-performance

The OpenLMI-Storage CIM API follows following principles:

- Each block device is represented by exactly one
  :ref:`CIM_StorageExtent<CIM-StorageExtent>`.

 - For example RAID devices are created using
   :ref:`LMI_StorageConfigurationService <LMI-StorageConfigurationService>`.
   :ref:`CreateOrModifyElementFromElements <LMI-StorageConfigurationService-CreateOrModifyElementFromElements>`,
   without any pool being involved.

 - No :ref:`CIM_LogicalDisk <CIM-LogicalDisk>` is created for devices
   consumed by the OS, i.e. when there is a filesystem on them.

  - Actually, all block devices can be used by the OS and it might be useful
    to have :ref:`LMI_StorageExtent<LMI-StorageExtent>` as subclass of
    :ref:`CIM_LogicalDisk <CIM-LogicalDisk>`.

.. warning:: This violates SMI-S, each block device should have **both** a
   StorageExtent + LogicalDisk associated from it to be usable by the OS.

- :ref:`CIM_StoragePool <CIM-StoragePool>` is used only for real pool
  objects - volume groups.

- PrimordialPool is not present. It might be added in future to track unused
  disk drives and partitions.

The implementation is not complete, e.g. mandatory Server Profile is not
implemented at all. The list will get updated.
