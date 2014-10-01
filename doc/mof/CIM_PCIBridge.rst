.. _CIM-PCIBridge:

CIM_PCIBridge
-------------

Class reference
===============
Subclass of :ref:`CIM_PCIDevice <CIM-PCIDevice>`

Capabilities and management of a PCI controller that provide bridge-to-bridge capability.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-PCIBridge-MemoryBase:

``uint16`` **MemoryBase**

    Base address of the memory supported by the bus. The upper 12 bits of this property specify the address bits, AD[31::20], of a 32-bit memory address. Each of the remaining 20 bits of the address are assumed to be 0.

    
.. _CIM-PCIBridge-IOLimit:

``uint8`` **IOLimit**

    End address of the I/O addresses supported by the bus. The upper 4 bits of this property specify the address bits, AD[15::12], of the I/O address. Each of the remaining 12 bits of the I/O address are assumed to be 1.

    
.. _CIM-PCIBridge-IOBase:

``uint8`` **IOBase**

    Base address of I/O addresses supported by the bus. The upper 4 bits of this property specify the address bits, AD[15::12], of the I/O address. Each of the remaining 12 bits of the I/O address are assumed to be 0.

    
.. _CIM-PCIBridge-IOBaseUpper16:

``uint16`` **IOBaseUpper16**

    Upper 16 bits of the supported I/O base address when 32-bit I/O addressing is used. The lower 16 bits are assumed to be 0.

    
.. _CIM-PCIBridge-PrefetchLimitUpper32:

``uint32`` **PrefetchLimitUpper32**

    Upper 32 bits of the supported prefetch end address when 64-bit addressing is used. The lower 32 bits are each assumed to be 1.

    
.. _CIM-PCIBridge-BridgeType:

``uint16`` **BridgeType**

    The type of bridge. Except for "Host" (value=0) and "PCIe-to-PCI" (value=10), the type of bridge is PCI-to-<value>. For type "Host", the device is a Host-to-PCI bridge. For type "PCIe-to-PCI", the device is a PCI Express-to-PCI bridge.

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Host         
    1        ISA          
    2        EISA         
    3        Micro Channel
    4        PCI          
    5        PCMCIA       
    6        NuBus        
    7        CardBus      
    8        RACEway      
    9        AGP          
    10       PCIe         
    11       PCIe-to-PCI  
    128      Other        
    ..       DMTF Reserved
    ======== =============
    
.. _CIM-PCIBridge-SecondaryBusDeviceSelectTiming:

``uint16`` **SecondaryBusDeviceSelectTiming**

    The slowest device-select timing for a target device on the secondary bus.

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Unknown      
    1        Other        
    2        Fast         
    3        Medium       
    4        Slow         
    5        DMTF Reserved
    ======== =============
    
.. _CIM-PCIBridge-SecondayBusNumber:

``uint8`` **SecondayBusNumber**

    The number of the PCI bus segment to which the secondary interface of the bridge is connected.

    
.. _CIM-PCIBridge-SecondaryStatusRegister:

``uint16`` **SecondaryStatusRegister**

    The contents of the SecondaryStatusRegister of the Bridge. For more information on the contents of this register, refer to the PCI-to-PCI Bridge Architecture Specification.

    
.. _CIM-PCIBridge-PrefetchMemoryBase:

``uint16`` **PrefetchMemoryBase**

    Base address of the memory that can be prefetched by the bus. The upper 12 bits of this property specify the address bits, AD[31::20], of a 32-bit memory address. Each of the remaining 20 bits of the address are assumed to be 0.

    
.. _CIM-PCIBridge-PrimaryBusNumber:

``uint8`` **PrimaryBusNumber**

    The number of the PCI bus segment to which the primary interface of the bridge is connected.

    
.. _CIM-PCIBridge-IOLimitUpper16:

``uint16`` **IOLimitUpper16**

    Upper 16 bits of the supported I/O end address when 32-bit I/O addressing is used. The lower 16 bits are each assumed to be 1.

    
.. _CIM-PCIBridge-SecondaryLatencyTimer:

``uint8`` **SecondaryLatencyTimer**

    The timeslice for the secondary interface when the bridge is acting as an initiator. A 0 value indicates no requirement.

    
.. _CIM-PCIBridge-PrefetchMemoryLimit:

``uint16`` **PrefetchMemoryLimit**

    End address of the memory that can be prefetched by the bus. The upper 12 bits of this property specify the address bits, AD[31::20], of a 32-bit memory address. Each of the remaining 20 bits of the address are assumed to be 1.

    
.. _CIM-PCIBridge-SubordinateBusNumber:

``uint8`` **SubordinateBusNumber**

    The number of the highest numbered bus that exists behind the bridge.

    
.. _CIM-PCIBridge-MemoryLimit:

``uint16`` **MemoryLimit**

    End address of the memory supported by the bus. The upper 12 bits of this property specify the address bits, AD[31::20], of a 32-bit memory address. Each of the remaining 20 bits of the address are assumed to be 1.

    
.. _CIM-PCIBridge-PrefetchBaseUpper32:

``uint32`` **PrefetchBaseUpper32**

    Upper 32 bits of the supported prefetch base address when 64-bit addressing is used. The lower 32 bits are assumed to be 0.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`VendorID <CIM-PCIDevice-VendorID>`
| ``uint16`` :ref:`PCIDeviceID <CIM-PCIDevice-PCIDeviceID>`
| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16[]`` :ref:`Capabilities <CIM-PCIController-Capabilities>`
| ``boolean`` :ref:`SelfTestEnabled <CIM-PCIController-SelfTestEnabled>`
| ``string`` :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`Availability <CIM-LogicalDevice-Availability>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``uint32`` :ref:`ExpansionROMBaseAddress <CIM-PCIController-ExpansionROMBaseAddress>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``uint8`` :ref:`DeviceNumber <CIM-PCIDevice-DeviceNumber>`
| ``uint8`` :ref:`RevisionID <CIM-PCIDevice-RevisionID>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint8`` :ref:`LatencyTimer <CIM-PCIController-LatencyTimer>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`SubsystemVendorID <CIM-PCIDevice-SubsystemVendorID>`
| ``uint16`` :ref:`DeviceSelectTiming <CIM-PCIController-DeviceSelectTiming>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``uint8`` :ref:`FunctionNumber <CIM-PCIDevice-FunctionNumber>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string[]`` :ref:`OtherIdentifyingInfo <CIM-LogicalDevice-OtherIdentifyingInfo>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint8`` :ref:`MaxLatency <CIM-PCIDevice-MaxLatency>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``uint16[]`` :ref:`AdditionalAvailability <CIM-LogicalDevice-AdditionalAvailability>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16`` :ref:`InterruptPin <CIM-PCIController-InterruptPin>`
| ``uint16`` :ref:`CommandRegister <CIM-PCIController-CommandRegister>`
| ``uint16`` :ref:`StatusInfo <CIM-LogicalDevice-StatusInfo>`
| ``string[]`` :ref:`CapabilityDescriptions <CIM-PCIController-CapabilityDescriptions>`
| ``datetime`` :ref:`TimeOfLastReset <CIM-Controller-TimeOfLastReset>`
| ``uint16[]`` :ref:`PowerManagementCapabilities <CIM-LogicalDevice-PowerManagementCapabilities>`
| ``uint32`` :ref:`MaxNumberControlled <CIM-Controller-MaxNumberControlled>`
| ``uint16`` :ref:`SubsystemID <CIM-PCIDevice-SubsystemID>`
| ``uint64`` :ref:`PowerOnHours <CIM-LogicalDevice-PowerOnHours>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint8`` :ref:`CacheLineSize <CIM-PCIController-CacheLineSize>`
| ``uint16`` :ref:`ProtocolSupported <CIM-Controller-ProtocolSupported>`
| ``uint8`` :ref:`BusNumber <CIM-PCIDevice-BusNumber>`
| ``uint64`` :ref:`MaxQuiesceTime <CIM-LogicalDevice-MaxQuiesceTime>`
| ``uint64`` :ref:`TotalPowerOnHours <CIM-LogicalDevice-TotalPowerOnHours>`
| ``uint8`` :ref:`ClassCode <CIM-PCIController-ClassCode>`
| ``string`` :ref:`ErrorDescription <CIM-LogicalDevice-ErrorDescription>`
| ``string`` :ref:`ProtocolDescription <CIM-Controller-ProtocolDescription>`
| ``uint64[]`` :ref:`BaseAddress64 <CIM-PCIDevice-BaseAddress64>`
| ``string[]`` :ref:`IdentifyingDescriptions <CIM-LogicalDevice-IdentifyingDescriptions>`
| ``uint16`` :ref:`LocationIndicator <CIM-LogicalDevice-LocationIndicator>`
| ``boolean`` :ref:`ErrorCleared <CIM-LogicalDevice-ErrorCleared>`
| ``uint32`` :ref:`LastErrorCode <CIM-LogicalDevice-LastErrorCode>`
| ``string`` :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``string`` :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| ``uint32[]`` :ref:`BaseAddress <CIM-PCIDevice-BaseAddress>`
| ``uint8`` :ref:`MinGrantTime <CIM-PCIDevice-MinGrantTime>`
| ``string`` :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`

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

