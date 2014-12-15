Usage
=====

OpenLMI-Hardware exposes hardware information, it does not
implement any methods. List of provided information divided by DMTF profiles
can be found below.

.. _usage-cpu-profile:

CPU Profile
-----------
CPU Profile provides information about CPU and associated cache:

* :ref:`Processor <lmi-processor>`

  - Number of :ref:`CPUs <lmi-processor>`, :ref:`Cores <lmi-processorcapabilities-numberofprocessorcores>` and :ref:`Threads <lmi-processorcapabilities-numberofhardwarethreads>`

    + Every CPU has its own :ref:`LMI_Processor <lmi-processor>` class. Number of instances of this class represents number of CPUs in the system.
      Number of cores and threads of CPU can be found in the associated :ref:`LMI_ProcessorCapabilities <lmi-processorcapabilities>` class.

  - :ref:`Model Name <lmi-processor-name>`
  - :ref:`Current <lmi-processor-currentclockspeed>` and :ref:`Maximum <lmi-processor-maxclockspeed>` Clock Speed
  - :ref:`FSB Speed <lmi-processor-externalbusclockspeed>`
  - :ref:`Data <lmi-processor-datawidth>` and :ref:`Address <lmi-processor-addresswidth>` Width
  - :ref:`Architecture <lmi-processor-architecture>`
  - :ref:`Flags <lmi-processor-flags>`
  - :ref:`Family <lmi-processor-family>`
  - :ref:`Stepping <lmi-processor-stepping>`
  - :ref:`FRU Data <lmi-processorchip>` (:ref:`Manufacturer <lmi-processorchip-manufacturer>`, :ref:`Serial Number <lmi-processorchip-serialnumber>`, :ref:`Part Number <lmi-processorchip-partnumber>`)

* :ref:`Processor Cache <lmi-processorcachememory>`

  - :ref:`Level <lmi-processorcachememory-name>`
  - Size (must be counted as :ref:`BlockSize <lmi-processorcachememory-blocksize>` * :ref:`NumberOfBlocks <lmi-processorcachememory-numberofblocks>`)
  - :ref:`Type <lmi-processorcachememory-name>` (Data / Instruction / Unified) (if available, this information is part of the :ref:`Name <lmi-processorcachememory-name>`)

Used Resources
^^^^^^^^^^^^^^
* dmidecode program *[from dmidecode package]*
* lscpu program *[from util-linux package]*
* /proc/cpuinfo file
* /sys/devices/system/cpu/\* files

.. _usage-system-memory-profile:

System Memory Profile
---------------------
System Memory Profile provides information about system memory and slots:

* :ref:`Memory <lmi-memory>`

  - Size (must be counted as :ref:`BlockSize <lmi-memory-blocksize>` * :ref:`NumberOfBlocks <lmi-memory-numberofblocks>`)
  - :ref:`Size of Standard Memory Page <lmi-memory-standardmemorypagesize>`
  - :ref:`All Supported Sizes of Huge Pages <lmi-memory-supportedhugememorypagesizes>`
  - :ref:`Current State of Transparent Huge Pages <lmi-memory-transparenthugememorypagestatus>` [Unsupported, Never, Madvise, Always]
  - :ref:`Detection of NUMA Layout <lmi-memory-hasnuma>`

* Memory :ref:`Slots <lmi-memoryslot>` + :ref:`Modules <lmi-physicalmemory>`

  - Number of :ref:`Slots <lmi-memoryslot>` and :ref:`Modules <lmi-physicalmemory>`
  - :ref:`LMI_MemoryPhysicalPackageInConnector <lmi-memoryphysicalpackageinconnector>` Association between Modules and Slots
  - :ref:`Size <lmi-physicalmemory-capacity>` of Modules
  - Speed of Modules (in both :ref:`MHz <lmi-physicalmemory-configuredmemoryclockspeed>` and :ref:`ns <lmi-physicalmemory-speed>`)
  - :ref:`Data <lmi-physicalmemory-datawidth>` and :ref:`Total <lmi-physicalmemory-totalwidth>` Width
  - :ref:`Module Type <lmi-physicalmemory-memorytype>` and :ref:`Form Factor <lmi-physicalmemory-formfactor>`
  - :ref:`FRU Data <lmi-physicalmemory>`

Used Resources
^^^^^^^^^^^^^^
* dmidecode program *[from dmidecode package]*
* /proc/meminfo file
* /sys/devices/system/node/\* files
* /sys/kernel/mm/hugepages/\* files
* /sys/kernel/mm/transparent_hugepage/\* files

.. _usage-pci-device-profile:

PCI Device Profile
------------------
PCI Device Profile provides information about PCI devices:

* :ref:`PCI Devices <lmi-pcidevice>`:

  - :ref:`Bus Number <lmi-pcidevice-busnumber>`
  - :ref:`Device Number <lmi-pcidevice-devicenumber>`
  - :ref:`Function Number <lmi-pcidevice-functionnumber>`
  - :ref:`PCI Device ID <lmi-pcidevice-pcideviceid>`
  - :ref:`PCI Device Name <lmi-pcidevice-pcidevicename>`
  - :ref:`Vendor ID <lmi-pcidevice-vendorid>`
  - :ref:`Vendor Name <lmi-pcidevice-vendorname>`
  - :ref:`Subsystem ID <lmi-pcidevice-subsystemid>`
  - :ref:`Subsystem Name <lmi-pcidevice-subsystemname>`
  - :ref:`Subsystem Vendor ID <lmi-pcidevice-subsystemvendorid>`
  - :ref:`Subsystem Vendor Name <lmi-pcidevice-subsystemvendorname>`
  - :ref:`Revision ID <lmi-pcidevice-revisionid>`
  - :ref:`Base Address <lmi-pcidevice-baseaddress>`
  - :ref:`Cache Line Size <lmi-pcidevice-cachelinesize>`
  - :ref:`Capabilities <lmi-pcidevice-capabilities>`
  - :ref:`Class Code <lmi-pcidevice-classcode>`
  - :ref:`Command Register <lmi-pcidevice-commandregister>`
  - :ref:`Device Select Timing <lmi-pcidevice-deviceselecttiming>`
  - :ref:`Interrupt Pin <lmi-pcidevice-interruptpin>`
  - :ref:`Latency Timer <lmi-pcidevice-latencytimer>`
  - :ref:`Expansion ROM Base Address <lmi-pcidevice-expansionrombaseaddress>`

* :ref:`PCI Bridges <lmi-pcibridge>` (all of the above, plus):

  - :ref:`Bridge Type <lmi-pcibridge-bridgetype>`
  - :ref:`Primary Bus Number <lmi-pcibridge-primarybusnumber>`
  - :ref:`Secondary Bus Number <lmi-pcibridge-secondaybusnumber>`
  - :ref:`Subordinate Bus Number <lmi-pcibridge-subordinatebusnumber>`
  - :ref:`Secondary Latency Timer <lmi-pcibridge-secondarylatencytimer>`
  - :ref:`IO Base <lmi-pcibridge-iobase>`
  - :ref:`IO Limit <lmi-pcibridge-iolimit>`
  - :ref:`Memory Base <lmi-pcibridge-memorybase>`
  - :ref:`Memory Limit <lmi-pcibridge-memorylimit>`
  - :ref:`Prefetch Memory Base <lmi-pcibridge-prefetchmemorybase>`
  - :ref:`Prefetch Memory Limit <lmi-pcibridge-prefetchmemorylimit>`

* PCI bus modelled with :ref:`LMI_PCIPortGroup <lmi-pciportgroup>`

Used Resources
^^^^^^^^^^^^^^
* libpci library *[from pciutils package, pci/pci.h header file]*

.. _usage-physical-asset-profile:

Physical Asset Profile
----------------------
Physical Asset Profile provides basic information about physical assets
in system, usually with FRU data, currently for following hardware
(with associations):

* :ref:`System Chassis <lmi-chassis>`
* :ref:`Baseboard <lmi-baseboard>` (motherboard)
* :ref:`Chassis Ports <lmi-portphysicalconnector>` (USB, LAN, VGA..)
* :ref:`Chassis Slots <lmi-systemslot>` (Media card slot, Express card slot..)
* :ref:`Pointing Devices on Chassis <lmi-pointingdevice>` (Touch pad, Track point..)

Used Resources
^^^^^^^^^^^^^^
* dmidecode program *[from dmidecode package]*

.. _usage-bios-profile:

BIOS Profile
------------
BIOS Profile provides information about :ref:`BIOS <lmi-bioselement>`:

* :ref:`Version <lmi-bioselement-version>`
* :ref:`Manufacturer <lmi-bioselement-manufacturer>`
* BIOS :ref:`Major <lmi-bioselement-systembiosmajorrelease>` and :ref:`Minor <lmi-bioselement-systembiosminorrelease>` Release
* Embedded Controller Firmware :ref:`Major <lmi-bioselement-embeddedcontrollerfirmwaremajorrelease>` and :ref:`Minor <lmi-bioselement-embeddedcontrollerfirmwareminorrelease>` Release
* :ref:`Release Date <lmi-bioselement-releasedate>`
* :ref:`Current Language <lmi-bioselement-currentlanguage>`
* :ref:`Available Languages <lmi-bioselement-listoflanguages>`
* :ref:`Characteristics <lmi-biosfeature-characteristics>`

Used Resources
^^^^^^^^^^^^^^
* dmidecode program *[from dmidecode package]*

.. _usage-disk-drive-profile:

Disk Drive Profile
------------------
Disk Drive Profile provides information about :ref:`disk drives <lmi-diskdrive>`:

* :ref:`Overall S.M.A.R.T. Status <lmi-diskdrive-operationalstatus>`
* :ref:`Temperature <lmi-diskdrive-temperature>`
* :ref:`Capacity <lmi-diskdrive-capacity>`
* :ref:`Manufacturer <lmi-diskphysicalpackage-manufacturer>`
* :ref:`Model <lmi-diskdrive-name>`
* :ref:`Serial Number <lmi-diskphysicalpackage-serialnumber>`
* :ref:`Firmware Version <lmi-diskdrivesoftwareidentity-versionstring>`
* :ref:`Form Factor <lmi-diskdrive-formfactor>` (Disk Size: 2.5", 3.5"..)
* :ref:`RPM <lmi-diskdrive-rpm>`
* :ref:`Port Type <lmi-diskdriveataport-porttype>` (ATA/SATA/SATA2)
* :ref:`Max Port Speed <lmi-diskdriveataport-maxspeed>`
* :ref:`Current Port Speed <lmi-diskdriveataport-speed>`, also can be found as :ref:`Interconnect Speed <lmi-diskdrive-interconnectspeed>`
* :ref:`Disk Type <lmi-diskdrive-disktype>` (HDD/SSD)

Used Resources
^^^^^^^^^^^^^^
* lsblk program *[from util-linux package]*
* smartctl program *[from smartmontools package]*
* /sys/class/block/\*/device/vendor file
* /sys/class/block/\*/queue/rotational file

.. _usage-battery-profile:

Battery Profile
---------------
Battery Profile provides information about :ref:`battery <lmi-battery>`:

* :ref:`Capacity <lmi-battery-capacity>`
* :ref:`Voltage <lmi-battery-designvoltage>`
* :ref:`Chemistry <lmi-battery-chemistry>`
* :ref:`FRU Data <lmi-batteryphysicalpackage>`
* :ref:`Battery Status <lmi-battery-batterystatus>`
* :ref:`Charging Status <lmi-battery-chargingstatus>`
* :ref:`Estimated Run Time <lmi-battery-estimatedruntime>`
* :ref:`Estimated Time to Full Charge <lmi-battery-timetofullcharge>`
* :ref:`Remaining Health Percentage <lmi-battery-healthpercent>`

Used Resources
^^^^^^^^^^^^^^
* dmidecode program *[from dmidecode package]*
* /sys/class/power_supply/BAT\*/\* files
