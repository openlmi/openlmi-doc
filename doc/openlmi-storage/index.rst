.. _openlmi-storage-provider:

Storage Provider
================

.. rubric:: Overview

OpenLMI-Storage is a CIM provider which manages storage on a Linux machine.
It exposes remotely accessible object-oriented API using
`WBEM <http://www.openlmi.org/node/1785>`_ set of protocols and technologies.

.. rubric:: Clients

The API can be accessed by any WBEM-capable client. OpenLMI already provides:

* Python module :ref:`lmi.scripts.storage <openlmi-scripts-storage-python>`,
  part of
  :ref:`OpenLMI scripts <openlmi-scripts-python>`.

* Command line tool: :ref:`LMI metacommand <lmi_metacommand>`, with
  :ref:`'storage' <openlmi-scripts-storage-cmd>` subcommand.

.. rubric:: Features

* Enumerate all block devices.
* Partition a block device.
* Manage MD RAID and LVM.
* Format a block device with a filesystem (xfs, ext2/3/4, ...)
* Manage mounts.

Currently, OpenLMI-Storage manages local block devices, i.e. block devices
which are present in ``/dev/`` directory. This includes also attached iSCSI, FC
and FCoE devices, as long as appropriate block device is present.

In future, it may include configuration of iSCSI and FC initiators,
multipath and other remote-storage management.

.. rubric:: Examples

There is plenty of examples how to use OpenLMI-Storage provider remotely
from `LMIShell <http://pythonhosted.org/openlmi-tools/index.html#lmishell>`_:

* :ref:`Create a partition table on a device<example-create-partition-table>`.
* :ref:`Create a new partition<example-create-partition>`.
* :ref:`Create software RAID5 with 3 devices<example-create-mdraid>`.
* :ref:`Format a device with ext3 filesystem<example-create-filesystem>`.
* :ref:`Mount a filesystem<example-create-mount>`.

.. rubric:: Documentation

The provider is inspired by `SNIA <http://www.snia.org/>`_
`SMI-S <http://www.snia.org/forums/smi>`_, but it differers in several
important areas. Application developers who are familiar with SMI-S should
read :ref:`SMI-S profiles <smis-profiles>` chapter.

Application developers and/or sysadmins should skip whole SMI-S chapter
and start at :ref:`OpenLMI-Storage concept <openlmi-concept>`.


.. rubric:: Table of contents

.. toctree::
   :maxdepth: 2

   smis-profiles
   concept
   usage
   admin-config

.. ifconfig:: includeClasses

   OpenLMI Storage CIM classes:

   .. toctree::
      :maxdepth: 2

      classes
