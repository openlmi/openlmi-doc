Usage
=====

OpenLMI-Hardware exposes hardware information, it does not
implement any methods. List of provided information divided by DMTF profiles
can be found below.

CPU Profile
-----------
CPU Profile provides information about CPU and associated cache:

* Processor

  - Number of CPUs, cores, threads
  - Model
  - Clock and FSB speeds
  - Data and Address width
  - Architecture
  - Flags
  - Family
  - Stepping
  - FRU data (Manufacturer, Model, Serial Number, Part Number)

* Processor Cache

  - Level
  - Size
  - Type (Data / Instruction / Unified)

Used Resources
^^^^^^^^^^^^^^
* dmidecode program *[from dmidecode package]*
* lscpu program *[from util-linux package]*
* /proc/cpuinfo file
* /sys/devices/system/cpu/\* files

System Memory Profile
---------------------
System Memory Profile provides information about system memory and slots:

* Memory

  - Size
  - Speed (in both MHz and ns)
  - Size of standard memory page
  - All supported sizes of huge pages
  - Current state of transparent huge pages [Unsupported, Never, Madvise, Always]
  - Detection of NUMA layout

* Memory slots + modules

  - Number of slots and modules
  - In which slots are modules plugged in
  - Size of modules
  - Speed of modules
  - Data and Total width
  - Module type and form factor
  - FRU data

Used Resources
^^^^^^^^^^^^^^
* dmidecode program *[from dmidecode package]*
* /proc/meminfo file
* /sys/devices/system/node/\* files
* /sys/kernel/mm/hugepages/\* files
* /sys/kernel/mm/transparent_hugepage/\* files

PCI Device Profile
------------------
PCI Device Profile provides information about PCI devices:

* PCI Devices:

  - Bus Number
  - Device Number
  - Function Number
  - PCI Device ID
  - PCI Device Name
  - Vendor ID
  - Vendor Name
  - Subsystem ID
  - Subsystem Name
  - Subsystem Vendor ID
  - Subsystem Vendor Name
  - Revision ID
  - Base Address
  - Cache Line Size
  - Capabilities
  - Class Code
  - Command Register
  - Device Select Timing
  - Interrupt Pin
  - Latency Timer
  - Expansion ROM Base Address

* PCI Bridges (all of the above, plus):

  - Bridge Type
  - Primary Bus Number
  - Secondary Bus Number
  - Subordinate Bus Number
  - Secondary Latency Timer
  - IO Base
  - IO Limit
  - Memory Base
  - Memory Limit
  - Prefetch Memory Base
  - Prefetch Memory Limit

* PCI bus modelled with :ref:`LMI_PCIPortGroup <lmi-pciportgroup>`

Used Resources
^^^^^^^^^^^^^^
* libpci library *[from pciutils package, pci/pci.h header file]*

Physical Asset Profile
----------------------
Physical Asset Profile provides basic information about physical assets
in system, usually with FRU data, currently for following hardware
(with associations):

* System chassis
* Baseboard (motherboard)
* Chassis ports (USB, LAN, VGA..)
* Chassis slots (Media card slot, Express card slot..)
* Pointing devices on chassis (Touch pad, Track point..)

Used Resources
^^^^^^^^^^^^^^
* dmidecode program *[from dmidecode package]*

BIOS Profile
------------
BIOS Profile provides information about BIOS:

* Version
* Manufacturer
* BIOS Release
* Embedded Controller Firmware Release
* Release Date
* Current Language
* Available languages
* Characteristics

Used Resources
^^^^^^^^^^^^^^
* dmidecode program *[from dmidecode package]*

Disk Drive Profile
------------------
Disk Drive Profile provides information about disk drives:

* Overall S.M.A.R.T. status
* Temperature
* Capacity
* Manufacturer
* Model
* Serial Number
* Firmware version
* Form Factor (disk size: 2.5", 3.5"..)
* RPM
* Port Type (ATA/SATA/SATA2)
* Max Port Speed
* Current Port Speed
* Disk Type (HDD/SSD)

Used Resources
^^^^^^^^^^^^^^
* lsblk program *[from util-linux package]*
* smartctl program *[from smartmontools package]*
* /sys/class/block/\*/device/vendor file
* /sys/class/block/\*/queue/rotational file

Battery Profile
---------------
Battery Profile provides information about battery:

* Capacity
* Voltage
* Chemistry
* FRU data
* Battery Status
* Charging Status
* Estimated Run Time
* Estimated Time to Full Charge
* Remaining Health Percentage

Used Resources
^^^^^^^^^^^^^^
* dmidecode program *[from dmidecode package]*
* /sys/class/power_supply/BAT\*/\* files
