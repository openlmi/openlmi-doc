MD RAID
=======

MD RAID devices are represented by
:ref:`LMI_MDRAIDStorageExtent <LMI-MDRAIDStorageExtent>` class.

Configuration of a MD RAID device is represented by instance of
:ref:`LMI_MDRAIDStorageSetting <LMI-MDRAIDStorageSetting>` associated to it.
Currently this instance is there only for compatibility with SMI-S, but in
future it may be extended to allow detailed configuration of the RAID.

Members of the MD RAID are associated to the
:ref:`LMI_MDRAIDStorageExtent <LMI-MDRAIDStorageExtent>` instance by
:ref:`LMI_MDRAIDBasedOn <LMI-MDRAIDBasedOn>` association.

.. _diagram:

Following instance diagram shows RAID5 ``/dev/md/myRAID`` with three devices:

.. figure:: pic/raid5-instance.svg
   :target: ../_images/raid5-instance.svg

Note the :ref:`Level <LMI-MDRAIDStorageExtent-Level>` property in
:ref:`LMI_MDRAIDStorageExtent <LMI-MDRAIDStorageExtent>`, which was added to
simplify RAID level calculation, in SMI-S the data redundancy and striping is
determined by :ref:`DataRedundancy <CIM-StorageExtent-DataRedundancy>`,
:ref:`ExtentStripeLength <CIM-StorageExtent-ExtentStripeLength>` and
:ref:`PackageRedundancy <CIM-StorageExtent-PackageRedundancy>` properties.

Currently the MD RAID support is limited to creation and removal of RAIDs. It is
not possible to modify existing RAID, e.g. add or remove devices to/from it
and/or manage RAID spares.

Useful methods
--------------

:ref:`CreateOrModifyMDRAID <LMI-StorageConfigurationService-CreateOrModifyMDRAID>`
  Creates a MD RAID of given level with given devices. Optionally, RAID name
  can be specified and in future also more detailed RAID configuration.

:ref:`CreateOrModifyElementFromElements <LMI-StorageConfigurationService-CreateOrModifyElementFromElements>`
  Creates a MD RAID in SMI-S way. It is necessary to provide correct Goal
  setting, which can be calculated e.g. by
  :ref:`CreateMDRAIDStorageSetting <LMI-MDRAIDStorageCapabilities-CreateMDRAIDStorageSetting>`

:ref:`CreateMDRAIDStorageSetting <LMI-MDRAIDStorageCapabilities-CreateMDRAIDStorageSetting>`
  This is helper method to calculate
  :ref:`LMI_StorageSetting <LMI-StorageSetting>` for given list of devices and
  given RAID level for
  :ref:`CreateOrModifyElementFromElements <LMI-StorageConfigurationService-CreateOrModifyElementFromElements>`.

:ref:`DeleteMDRAID <LMI-StorageConfigurationService-DeleteMDRAID>`
  Destroys a MD RAID. There is no SMI-S function for this.


Use cases
---------

.. _example-create-mdraid:

Create MD RAID
^^^^^^^^^^^^^^

Use
:ref:`CreateOrModifyMDRAID <LMI-StorageConfigurationService-CreateOrModifyMDRAID>`
method. Following example creates MD RAID level 5 named '/dev/md/myRAID' with
three members::

    # Connect to the remote system and prepare some local variables
    connection = connect("remote.host.org", "root", "opensesame")
    ns = connection.root.cimv2  # ns as NameSpace
    storage_service = ns.LMI_StorageConfigurationService.first_instance()

    # Find the devices we want to add to MD RAID
    # (filtering one CIM_StorageExtent.instances()
    # call would be faster, but this is easier to read)
    sda1 = ns.CIM_StorageExtent.first_instance({"Name": "/dev/sda1"})
    sdb1 = ns.CIM_StorageExtent.first_instance({"Name": "/dev/sdb1"})
    sdc1 = ns.CIM_StorageExtent.first_instance({"Name": "/dev/sdc1"})

    # Create the RAID
    (ret, outparams, err) = storage_service.SyncCreateOrModifyMDRAID(
            ElementName = "myRAID",
            InExtents= [sda1, sdb1, sdc1],
            Level=storage_service.CreateOrModifyMDRAID.LevelValues.RAID5)
    raid = outparams['TheElement'].to_instance()
    print "RAID", raid.DeviceID, \
            "level", raid.Level, \
            "of size", raid.BlockSize * raid.NumberOfBlocks, \
            "created"

The result is the same as shown in diagram_ above.

Create MD RAID in SMI-S way
^^^^^^^^^^^^^^^^^^^^^^^^^^^

SMI-S applications can use
:ref:`CreateOrModifyElementFromElements <LMI-StorageConfigurationService-CreateOrModifyElementFromElements>`
method. Following example creates MD RAID level 5 named '/dev/md/myRAID' with
three members::

    # Connect to the remote system and prepare some local variables
    connection = connect("remote.host.org", "root", "opensesame")
    ns = connection.root.cimv2  # ns as NameSpace
    storage_service = ns.LMI_StorageConfigurationService.first_instance()

    # Find the devices we want to add to MD RAID
    # (filtering one CIM_StorageExtent.instances()
    # call would be faster, but this is easier to read)
    sda1 = ns.CIM_StorageExtent.first_instance({"Name": "/dev/sda1"})
    sdb1 = ns.CIM_StorageExtent.first_instance({"Name": "/dev/sdb1"})
    sdc1 = ns.CIM_StorageExtent.first_instance({"Name": "/dev/sdc1"})

    # Calculate LMI_StorageSetting, e.g. using our helper method
    # (SMI-S application can of course use standard caps.CreateSetting()
    # and edit it manually)
    caps = ns.LMI_MDRAIDStorageCapabilities.first_instance()
    (ret, outparams, err) = caps.CreateMDRAIDStorageSetting(
            InExtents=[sda1, sdb1, sdc1],
            Level=caps.CreateMDRAIDStorageSetting.LevelValues.RAID5)
    setting = outparams ['Setting'].to_instance()

    # Create the RAID
    (ret, outparams, err) = storage_service.SyncCreateOrModifyElementFromElements(
            InElements=[sda1, sdb1, sdc1],
            Goal=setting,
            ElementType = storage_service.CreateOrModifyElementFromElements.ElementTypeValues.StorageExtent)
    raid = outparams['TheElement'].to_instance()
    print "RAID", raid.DeviceID, \
            "level", raid.Level, \
            "of size", raid.BlockSize * raid.NumberOfBlocks, \
            "created"

List members of MD RAID
^^^^^^^^^^^^^^^^^^^^^^^

Enumerate :ref:`LMI_MDRAIDBasedOn <LMI-MDRAIDBasedOn>` associations of the MD
RAID extent.

Following code lists all members od ``/dev/md/myRAID``::

    # Connect to the remote system and prepare some local variables
    connection = connect("remote.host.org", "root", "opensesame")
    ns = connection.root.cimv2  # ns as NameSpace

    # Find the disk
    md = ns.LMI_StorageExtent.first_instance({"Name": "/dev/md/myRAID"})

    devices = md.associators(AssocClass="LMI_MDRAIDBasedOn")
    for dev in devices:
        print "Found device", dev.DeviceID

Delete MD RAID
^^^^^^^^^^^^^^

Call :ref:`DeleteMDRAID <LMI-StorageConfigurationService-DeleteMDRAID>` method::

    # Connect to the remote system and prepare some local variables
    connection = connect("remote.host.org", "root", "opensesame")
    ns = connection.root.cimv2  # ns as NameSpace
    storage_service = ns.LMI_StorageConfigurationService.first_instance()

    md = ns.LMI_MDRAIDStorageExtent.first_instance({"Name": "/dev/md/myRAID"})
    (ret, outparams, err) = storage_service.SyncDeleteMDRAID(TheElement=md)

Future direction
----------------

In future, we might implement:

* Modification of existing MD RAIDs, for example adding/removing devices.

* Management of spare devices.

* Detailed information of device status, synchronization progress etc.

* Indications of various events, like RAID failed member, synchronization
  errors etc.

