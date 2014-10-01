Usage
=====

Block devices cannot be directly manipulated using intrinsic or extrinsic
methods of :ref:`CIM_StorageExtent<CIM-StorageExtent>` or
:ref:`LMI_VGStoragePool<LMI-VGStoragePool>`.

Please use appropriate ``ConfigurationService`` to create, modify or delete devices
or volume groups.


.. toctree::
   :maxdepth: 2

   usage-partitioning
   usage-raid
   usage-lvm
   usage-fs
   usage-block-performance
   usage-mounting
   usage-luks


.. note::

   Previous releases allowed to use ``DeleteInstance`` intrinsic method to
   delete various ``CIM_StorageExtents``. This method is now deprecated and
   will be removed from future releases of OpenLMI-Storage. The reason is that
   ``DeleteInstance`` cannot be asynchronous and could block the whole provider
   for a long time.
