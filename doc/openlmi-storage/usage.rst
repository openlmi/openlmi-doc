Usage
=====

Block devices cannot be directly manipulated using intrinsic or extrinsic
methods of :ref:`CIM_StorageExtent<CIM-StorageExtent>` or
:ref:`LMI_VGStoragePool<LMI-VGStoragePool>`. Please use appropriate
``ConfigurationService`` to create, modify or delete devices
or volume groups.

.. _storage-shell-setup:

.. rubric:: lmishell setup

All examples in this documentation are written for :ref:`lmishell <lmi_shell>`.
The examples assume that ``connection`` and ``ns`` variables were initialized
in this way::

    # Connect to the remote system
    connection = connect("remote.host.org", "root", "opensesame")

    # Use 'ns' (NameSpace) as reference (shortcut) to 'connection.root.cimv2'
    # to save some typing
    ns = connection.root.cimv2

.. rubric:: Table of contents

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
