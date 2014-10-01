Device identification
=====================

On modern Linux, block devices can be identified in number of ways. Some of them
are stable across reboots, some other are nice to remeber and it is also
possible to configure block device names using udev rules.

For example, all these paths refer to the same block device:

  * ``/dev/disk/by-id/ata-Samsung_SSD_840_Series_S19MNSAD500335K``
  * ``/dev/disk/by-id/wwn-0x50025385a0031e7c``
  * ``/dev/sda``
  * ``/dev/systemdisk`` (using an udev rule)

OpenLMI does not assume any site policy, it's up to system administrator
to write udev rules if default /dev/sdX and /dev/disk/by-id/XYZ is not
sufficient.

As many things in Linux are configurable and tunable, term *SHOULD* below
means *unless explicitly reconfigured*.

CIM_StorageExtent
-----------------

When OpenLMI builds :ref:`CIM_StorageExtent<CIM-StorageExtent>` for a block
device, it fills following properties:

:ref:`DeviceID<cim-logicaldevice-deviceid>`

    OpenLMI internal identifier of a block device. Even if it looks like
    a device path, it should be opaque for applications and applications should
    not parse it / interpret it in any way. Its format may change in
    future versions of OpenLMI.


    This is the primary key how to identify a
    :ref:`CIM_StorageExtent<CIM-StorageExtent>`.

    * Guaranteed to be unique in the managed system.

    * SHOULD be persistent across reboots.

:ref:`InstanceID<lmi-storageextent-instanceid>`

    OpenLMI internal identifier of a block device group.
    This property has been added to have the same way how to identify
    :ref:`CIM_StorageExtent<CIM-StorageExtent>` and
    :ref:`LMI_VGStoragePool<LMI-VGStoragePool>`.

    * Guaranteed to be unique in the managed system.

    * SHOULD be persistent across reboots.

:ref:`Name<cim-storageextent-name>`

    Canonical path to the device, such as as ``/dev/sda``,
    ``/dev/mapper/test-test1``, ``/dev/md/blivet00``.
    This is the Linux default device name.

    * Guaranteed to be unique in the managed system.

    * Not persistent across reboots.

:ref:`ElementName<cim-managedelement-elementname>`

    Name of the block device, logical volume, RAID etc, such as as ``sda``
    for disk, ``test1`` for logical volume, ``blivet00`` for MD RAID.

    * Not unique in the managed system.

    * Not persistent across reboots.

    * Usually assigned by system administrator when the device is created
      (logical volume, MD RAID, ...)

:ref:`Names<lmi-storageextent-names>`

    Array of all paths, under which this device is known in the system.
    All these paths are links to one block device.
    For disk from the example above, it's content would be::

        [
            '/dev/disk/by-id/ata-Samsung_SSD_840_Series_S19MNSAD500335K',
            '/dev/disk/by-id/wwn-0x50025385a0031e7c',
            '/dev/sda',
            '/dev/systemdisk;
        ]

Applications can use any of these properties to find a block device (using
CQL or WQL).

.. note::

    OpenLMI tries as hard as possible to have
    :ref:`DeviceID<cim-logicaldevice-deviceid>` and
    :ref:`InstanceID<lmi-storageextent-instanceid>` properties really stable
    across reboots. Unfortunately, some hardware does not provide unique
    identifier for disks - typically in virtualized environment, there may be
    cases where DeviceID may be just ``/dev/vda`` and it may change when the
    virtual machine reorders the virtual disks after reconfiguration.


LMI_VGStoragePool
-----------------

Although volume groups are not exactly block devices, there are several ways how
to identify :ref:`LMI_VGStoragePool<LMI-VGStoragePool>` instances:

:ref:`InstanceID<cim-resourcepool-instanceid>`

    OpenLMI internal identifier of a volume group. It should
    be opaque for applications, i.e. applications should not parse it /
    interpret it in any way.

    * Guaranteed to be unique in the managed system.

    * SHOULD be persistent across reboots.

:ref:`PoolID<lmi-vgstoragepool-poolid>`,
:ref:`ElementName<cim-managedelement-elementname>`

    Name of the volume group.

    * Guaranteed to be unique among all volume groups on the managed system.
      However, there can be other ManagedElements, such as logical volumes,
      with the same ElementName.

    * SHOULD be persistent across reboots.

:ref:`Name<lmi-vgstoragepool-name>`

    Canonical path to the volume group, such as as ``/dev/mapper/mygroup``.
    This property has been added to have the same way how to identify
    :ref:`CIM_StorageExtent<CIM-StorageExtent>` and
    :ref:`LMI_VGStoragePool<LMI-VGStoragePool>`.

    * Guaranteed to be unique in the managed system.

    * Not persistent across reboots.
