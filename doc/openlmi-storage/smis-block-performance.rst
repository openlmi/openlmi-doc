SMI-S Block Server Performance Subprofile
=========================================

This profile provides I/O statistics for various
:ref:`CIM_StorageExtent<CIM-StorageExtent>` subclasses.

OpenLMI-Storage implements the Block Server Performance Subprofile with these
adjustments:

* Applications cannot create custom manifests, i.e.
  :ref:`LMI_BlockStatisticsService.AddOrModifyManifest<CIM-BlockStatisticsService-AddOrModifyManifest>`
  is  not implemented.

* We provide
  :ref:`LMI_BlockStorageStatisticalData<LMI-BlockStorageStatisticalData>` for
  *every* :ref:`CIM_StorageExtent<CIM-StorageExtent>` subclass and not only for
  disk drives.
  :ref:`LMI_BlockStorageStatisticalData.ElementType<LMI-BlockStorageStatisticalData-ElementType>`
  property is always set to ``9``, i.e. ``Extent``.

* There is no sampling interval. OpenLMI always reports current values when
  returning
  :ref:`LMI_BlockStorageStatisticalData<LMI-BlockStorageStatisticalData>`
  instance.


.. note::

   Even though properties in
   :ref:`LMI_BlockStorageStatisticalData<LMI-BlockStorageStatisticalData>`
   are 64-bit, they are tracked as 32-bit on systems with 32-bit kernel.
   They can wrap pretty quickly on modern hardware.

   For example, on i686 with iSCSI drive on 10Gb/s link, the KBytesRead counter
   can wrap in approximately 27 minutes.

   With 64-bit kernels, these counters are tracked in 64-bits and they wrap once
   in a few years.

Implementation
--------------

All mandatory classes and methods are implemented.

Classes
^^^^^^^

Implemented SMI-S classes:

* :ref:`LMI_BlockStorageStatisticalData<LMI-BlockStorageStatisticalData>`

* :ref:`LMI_StorageElementStatisticalData<LMI-StorageElementStatisticalData>`

* :ref:`LMI_StorageStatisticsCollection<LMI-StorageStatisticsCollection>`

* :ref:`LMI_MemberOfStorageStatisticsCollection<LMI-MemberOfStorageStatisticsCollection>`

* :ref:`LMI_HostedStorageStatisticsCollection<LMI-HostedStorageStatisticsCollection>`

* :ref:`LMI_BlockStatisticsService<LMI-BlockStatisticsService>`

* :ref:`LMI_BlockStatisticsCapabilities<LMI-BlockStatisticsCapabilities>`

* :ref:`LMI_BlockStatisticsManifest<LMI-BlockStatisticsManifest>`

* :ref:`LMI_BlockStatisticsManifestCollection<LMI-BlockStatisticsManifestCollection>`

* :ref:`LMI_MemberOfBlockStatisticsManifestCollection<LMI-MemberOfBlockStatisticsManifestCollection>`

* :ref:`LMI_AssociatedBlockStatisticsManifestCollection<LMI-AssociatedBlockStatisticsManifestCollection>`

Methods
^^^^^^^

Implemented methods:

* :ref:`LMI_BlockStatisticsService.GetStatisticsCollection<LMI-BlockStatisticsService-GetStatisticsCollection>`

