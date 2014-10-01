.. _CIM-PCIDevice:

CIM_PCIDevice
-------------

Class reference
===============
Subclass of :ref:`CIM_PCIController <CIM-PCIController>`

Capabilities and management of a PCI device controller on an adapter card.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-PCIDevice-VendorID:

``uint16`` **VendorID**

    Register that contains a value assigned by the PCI SIG used to identify the manufacturer of the device.

    
.. _CIM-PCIDevice-PCIDeviceID:

``uint16`` **PCIDeviceID**

    Register that contains a value assigned by the device manufacturer used to identify the type of device.

    
.. _CIM-PCIDevice-BaseAddress64:

``uint64[]`` **BaseAddress64**

    Array of doubleword base-memory addresses for 64 bit addresses

    
.. _CIM-PCIDevice-RevisionID:

``uint8`` **RevisionID**

    Register that contains a value assigned by the device manufacturer used to identify the revision number of the device.

    
.. _CIM-PCIDevice-SubsystemVendorID:

``uint16`` **SubsystemVendorID**

    Subsystem vendor ID. ID information is reported from a PCIDevice through protocol-specific requests. The correct place in the CIM Schema for this information is in CIM_Physical Element (the Manufacturer property) for hardware, and CIM_Product (the Vendor property) if the information is related to Product acquisition. This data is also reported here, because it is part of the standard output from the Device and is an optimization.

    
.. _CIM-PCIDevice-FunctionNumber:

``uint8`` **FunctionNumber**

    The function number for this PCI device.

    
.. _CIM-PCIDevice-MaxLatency:

``uint8`` **MaxLatency**

    Register that specifies how often the device needs access to the PCI bus in 250ns. A 0 value indicates no requirement.

    
.. _CIM-PCIDevice-SubsystemID:

``uint16`` **SubsystemID**

    Subsystem identifier code.

    
.. _CIM-PCIDevice-BusNumber:

``uint8`` **BusNumber**

    The bus number where this PCI device resides.

    
.. _CIM-PCIDevice-DeviceNumber:

``uint8`` **DeviceNumber**

    The device number assigned to this PCI device for this bus.

    
.. _CIM-PCIDevice-BaseAddress:

``uint32[]`` **BaseAddress**

    Array of doubleword base-memory addresses.

    
.. _CIM-PCIDevice-MinGrantTime:

``uint8`` **MinGrantTime**

    Register that indicates how long the master would like to retain PCI bus ownership whenever it initiates a transaction. A 0 value indicates no requirement.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`InterruptPin <CIM-PCIController-InterruptPin>`
| ``datetime`` :ref:`TimeOfLastReset <CIM-Controller-TimeOfLastReset>`
| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``uint16`` :ref:`DeviceSelectTiming <CIM-PCIController-DeviceSelectTiming>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``boolean`` :ref:`SelfTestEnabled <CIM-PCIController-SelfTestEnabled>`
| ``string`` :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`Availability <CIM-LogicalDevice-Availability>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint8`` :ref:`LatencyTimer <CIM-PCIController-LatencyTimer>`
| ``boolean`` :ref:`ErrorCleared <CIM-LogicalDevice-ErrorCleared>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``string`` :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string[]`` :ref:`OtherIdentifyingInfo <CIM-LogicalDevice-OtherIdentifyingInfo>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint64`` :ref:`PowerOnHours <CIM-LogicalDevice-PowerOnHours>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``uint16[]`` :ref:`AdditionalAvailability <CIM-LogicalDevice-AdditionalAvailability>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16`` :ref:`CommandRegister <CIM-PCIController-CommandRegister>`
| ``uint16`` :ref:`StatusInfo <CIM-LogicalDevice-StatusInfo>`
| ``uint16[]`` :ref:`Capabilities <CIM-PCIController-Capabilities>`
| ``uint16[]`` :ref:`PowerManagementCapabilities <CIM-LogicalDevice-PowerManagementCapabilities>`
| ``uint32`` :ref:`MaxNumberControlled <CIM-Controller-MaxNumberControlled>`
| ``uint32`` :ref:`ExpansionROMBaseAddress <CIM-PCIController-ExpansionROMBaseAddress>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint8`` :ref:`CacheLineSize <CIM-PCIController-CacheLineSize>`
| ``uint16`` :ref:`ProtocolSupported <CIM-Controller-ProtocolSupported>`
| ``uint64`` :ref:`MaxQuiesceTime <CIM-LogicalDevice-MaxQuiesceTime>`
| ``uint64`` :ref:`TotalPowerOnHours <CIM-LogicalDevice-TotalPowerOnHours>`
| ``uint8`` :ref:`ClassCode <CIM-PCIController-ClassCode>`
| ``string`` :ref:`ErrorDescription <CIM-LogicalDevice-ErrorDescription>`
| ``string`` :ref:`ProtocolDescription <CIM-Controller-ProtocolDescription>`
| ``string[]`` :ref:`IdentifyingDescriptions <CIM-LogicalDevice-IdentifyingDescriptions>`
| ``uint16`` :ref:`LocationIndicator <CIM-LogicalDevice-LocationIndicator>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint32`` :ref:`LastErrorCode <CIM-LogicalDevice-LastErrorCode>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``string`` :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| ``string`` :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`
| ``string[]`` :ref:`CapabilityDescriptions <CIM-PCIController-CapabilityDescriptions>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`Reset <CIM-LogicalDevice-Reset>`
| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`
| :ref:`SetPowerState <CIM-LogicalDevice-SetPowerState>`
| :ref:`QuiesceDevice <CIM-LogicalDevice-QuiesceDevice>`
| :ref:`BISTExecution <CIM-PCIController-BISTExecution>`
| :ref:`EnableDevice <CIM-LogicalDevice-EnableDevice>`
| :ref:`OnlineDevice <CIM-LogicalDevice-OnlineDevice>`
| :ref:`SaveProperties <CIM-LogicalDevice-SaveProperties>`
| :ref:`RestoreProperties <CIM-LogicalDevice-RestoreProperties>`

