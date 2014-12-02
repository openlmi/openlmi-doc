.. _openlmi-hardware-provider:

Hardware Provider
=================

.. rubric:: Overview

OpenLMI-Hardware is a CIM provider which exposes hardware information.
It exposes remotely accessible object-oriented API using
WBEM set of protocols and technologies.

.. rubric:: Clients

The API can be accessed by any WBEM-capable client. OpenLMI already provides:

* Command line tool: :ref:`LMI metacommand <lmi_metacommand>`, with
  :ref:`'hardware' <openlmi-scripts-hardware-cmd>` subcommand.

.. rubric:: Features

OpenLMI-Hardware exposes information about:

* Processor
* System Memory
* PCI Devices
* Chassis
* Baseboard
* BIOS
* Disks
* Battery

.. rubric:: Examples

OpenLMI-Hardware provides only information about current hardware,
it does not implement any methods, what makes usage of this agent pretty
straightforward. For example, to determine basic CPU info, run in
:ref:`LMIShell <lmi_shell>`, after creating the connection::

   > cpu = c.root.cimv2.LMI_Processor.first_instance()
   > cpu_cap = cpu.associators(ResultClass="LMI_ProcessorCapabilities")[0]
   > print cpu.Name
   Intel(R) Core(TM) i7-3520M CPU @ 2.90GHz
   > print cpu_cap.NumberOfProcessorCores
   2
   > print cpu_cap.NumberOfHardwareThreads
   4

To list memory modules, run::

   > mem = c.root.cimv2.LMI_Memory.first_instance()
   > for i in mem.associators(ResultClass="LMI_PhysicalMemory"):
   ...     print i.Name
   8 GB Memory Module
   4 GB Memory Module

Chassis information can be found in :ref:`LMI_Chassis <lmi-chassis>` class::

   > chassis = c.root.cimv2.LMI_Chassis.first_instance()
   > print chassis.Manufacturer
   LENOVO
   > print chassis.Model
   ThinkPad T530

Listing PCI devices is also simple::

   > for pci in c.root.cimv2.LMI_PCIDevice.instances():
   ...     print pci.Name
   Centrino Ultimate-N 6300
   PCIe SDXC/MMC Host Controller
   7 Series/C210 Series Chipset Family SMBus Controller
   ...

.. rubric:: Documentation

The provider is partially implementing DMTF Computer System Profile with
addition of multiple hardware related profiles. For more information see
:ref:`DMTF profiles <hardware-dmtf-profiles>`.

.. rubric:: Table of contents

.. toctree::
   :maxdepth: 2

   dmtf-profiles
   info
