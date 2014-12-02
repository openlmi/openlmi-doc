.. _LMI-PCIBridge:

LMI_PCIBridge
-------------

Class reference
===============
Subclass of :ref:`CIM_PCIBridge <CIM-PCIBridge>`

Capabilities and management of a PCI controller that provide bridge-to-bridge capability.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-PCIBridge-VendorID:

``uint16`` **VendorID**

    Register that contains a value assigned by the PCI SIG used to identify the manufacturer of the device.

    
.. _LMI-PCIBridge-InterruptPin:

``uint16`` **InterruptPin**

    Defines the PCI interrupt request pin (INTA# to INTD#) to which a PCI functional device is connected.

    
    ======== =======
    ValueMap Values 
    ======== =======
    0        None   
    1        INTA#  
    2        INTB#  
    3        INTC#  
    4        INTD#  
    5        Unknown
    ======== =======
    
.. _LMI-PCIBridge-SubsystemVendorName:

``string`` **SubsystemVendorName**

    Name of the subsystem vendor

    
.. _LMI-PCIBridge-IOLimit:

``uint8`` **IOLimit**

    End address of the I/O addresses supported by the bus. The upper 4 bits of this property specify the address bits, AD[15::12], of the I/O address. Each of the remaining 12 bits of the I/O address are assumed to be 1.

    
.. _LMI-PCIBridge-BaseAddress64:

``uint64[]`` **BaseAddress64**

    Array of doubleword base-memory addresses for 64 bit addresses

    
.. _LMI-PCIBridge-SecondayBusNumber:

``uint8`` **SecondayBusNumber**

    The number of the PCI bus segment to which the secondary interface of the bridge is connected.

    
.. _LMI-PCIBridge-SubsystemID:

``uint16`` **SubsystemID**

    Subsystem identifier code.

    
.. _LMI-PCIBridge-DeviceNumber:

``uint8`` **DeviceNumber**

    The device number assigned to this PCI device for this bus.

    
.. _LMI-PCIBridge-BaseAddress:

``uint32[]`` **BaseAddress**

    Array of doubleword base-memory addresses.

    
.. _LMI-PCIBridge-BridgeType:

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
    
.. _LMI-PCIBridge-PrefetchMemoryBase:

``uint16`` **PrefetchMemoryBase**

    Base address of the memory that can be prefetched by the bus. The upper 12 bits of this property specify the address bits, AD[31::20], of a 32-bit memory address. Each of the remaining 20 bits of the address are assumed to be 0.

    
.. _LMI-PCIBridge-MemoryLimit:

``uint16`` **MemoryLimit**

    End address of the memory supported by the bus. The upper 12 bits of this property specify the address bits, AD[31::20], of a 32-bit memory address. Each of the remaining 20 bits of the address are assumed to be 1.

    
.. _LMI-PCIBridge-LatencyTimer:

``uint8`` **LatencyTimer**

    Defines the minimum amount of time, in PCI clock cycles, that the bus master can retain ownership of the bus.

    
.. _LMI-PCIBridge-CommandRegister:

``uint16`` **CommandRegister**

    Current contents of the register that provides basic control over the ability of the device to respond to or perform PCI accesses.

    
.. _LMI-PCIBridge-BusNumber:

``uint8`` **BusNumber**

    The bus number where this PCI device resides.

    
.. _LMI-PCIBridge-SystemCreationClassName:

``string`` **SystemCreationClassName**

    The CreationClassName of the scoping system.

    
.. _LMI-PCIBridge-MemoryBase:

``uint16`` **MemoryBase**

    Base address of the memory supported by the bus. The upper 12 bits of this property specify the address bits, AD[31::20], of a 32-bit memory address. Each of the remaining 20 bits of the address are assumed to be 0.

    
.. _LMI-PCIBridge-IOBase:

``uint8`` **IOBase**

    Base address of I/O addresses supported by the bus. The upper 4 bits of this property specify the address bits, AD[15::12], of the I/O address. Each of the remaining 12 bits of the I/O address are assumed to be 0.

    
.. _LMI-PCIBridge-IOBaseUpper16:

``uint16`` **IOBaseUpper16**

    Upper 16 bits of the supported I/O base address when 32-bit I/O addressing is used. The lower 16 bits are assumed to be 0.

    
.. _LMI-PCIBridge-Capabilities:

``uint16[]`` **Capabilities**

    An array of integers that indicates controller capabilities. Information such as "Supports 66MHz" (value=2) is specified in this property. The data in the Capabilities array is gathered from the PCI Status Register and the PCI Capabilities List as defined in the PCI Specification.

    
    ============ =======================================
    ValueMap     Values                                 
    ============ =======================================
    0            Unknown                                
    1            Other                                  
    2            Supports 66MHz                         
    3            Supports User Definable Features       
    4            Supports Fast Back-to-Back Transactions
    5            PCI-X Capable                          
    6            PCI Power Management Supported         
    7            Message Signaled Interrupts Supported  
    8            Parity Error Recovery Capable          
    9            AGP Supported                          
    10           Vital Product Data Supported           
    11           Provides Slot Identification           
    12           Hot Swap Supported                     
    13           Supports PCIe                          
    14           Supports PCIe Gen 2                    
    15           Supports PCIe Gen 3                    
    16..32767    DMTF Reserved                          
    32768..65535 Vendor Reserved                        
    ============ =======================================
    
.. _LMI-PCIBridge-SecondaryLatencyTimer:

``uint8`` **SecondaryLatencyTimer**

    The timeslice for the secondary interface when the bridge is acting as an initiator. A 0 value indicates no requirement.

    
.. _LMI-PCIBridge-ElementName:

``string`` **ElementName**

    A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. 

    Note that the Name property of ManagedSystemElement is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. Note that if there is an associated instance of CIM_EnabledLogicalElementCapabilities, restrictions on this properties may exist as defined in ElementNameMask and MaxElementNameLen properties defined in that class.

    
.. _LMI-PCIBridge-SubsystemName:

``string`` **SubsystemName**

    Name of the subsystem

    
.. _LMI-PCIBridge-SecondaryStatusRegister:

``uint16`` **SecondaryStatusRegister**

    The contents of the SecondaryStatusRegister of the Bridge. For more information on the contents of this register, refer to the PCI-to-PCI Bridge Architecture Specification.

    
.. _LMI-PCIBridge-PrimaryBusNumber:

``uint8`` **PrimaryBusNumber**

    The number of the PCI bus segment to which the primary interface of the bridge is connected.

    
.. _LMI-PCIBridge-IOLimitUpper16:

``uint16`` **IOLimitUpper16**

    Upper 16 bits of the supported I/O end address when 32-bit I/O addressing is used. The lower 16 bits are each assumed to be 1.

    
.. _LMI-PCIBridge-DeviceID:

``string`` **DeviceID**

    An address or other identifying information used to uniquely name the LogicalDevice.

    
.. _LMI-PCIBridge-PCIDeviceName:

``string`` **PCIDeviceName**

    Name of the device

    
.. _LMI-PCIBridge-CacheLineSize:

``uint8`` **CacheLineSize**

    Specifies the system cache line size in doubleword increments (for example, a 486-based system would store the value 04h, indicating a cache line size of four doublewords.

    
.. _LMI-PCIBridge-PrefetchMemoryLimit:

``uint16`` **PrefetchMemoryLimit**

    End address of the memory that can be prefetched by the bus. The upper 12 bits of this property specify the address bits, AD[31::20], of a 32-bit memory address. Each of the remaining 20 bits of the address are assumed to be 1.

    
.. _LMI-PCIBridge-VendorName:

``string`` **VendorName**

    Name of the vendor

    
.. _LMI-PCIBridge-PCIDeviceID:

``uint16`` **PCIDeviceID**

    Register that contains a value assigned by the device manufacturer used to identify the type of device.

    
.. _LMI-PCIBridge-InstanceID:

``string`` **InstanceID**

    InstanceID is an optional property that may be used to opaquely and uniquely identify an instance of this class within the scope of the instantiating Namespace. Various subclasses of this class may override this property to make it required, or a key. Such subclasses may also modify the preferred algorithms for ensuring uniqueness that are defined below.

    To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon (:), and where <OrgID> must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness, <OrgID> must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If not null and the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance. 

    If not set to null for DMTF-defined instances, the "preferred" algorithm must be used with the <OrgID> set to CIM.

    
.. _LMI-PCIBridge-DeviceSelectTiming:

``uint16`` **DeviceSelectTiming**

    The slowest device-select timing for a target device.

    
    ======== ========
    ValueMap Values  
    ======== ========
    0        Unknown 
    1        Other   
    2        Fast    
    3        Medium  
    4        Slow    
    5        Reserved
    ======== ========
    
.. _LMI-PCIBridge-PrefetchLimitUpper32:

``uint32`` **PrefetchLimitUpper32**

    Upper 32 bits of the supported prefetch end address when 64-bit addressing is used. The lower 32 bits are each assumed to be 1.

    
.. _LMI-PCIBridge-SystemName:

``string`` **SystemName**

    The System Name of the scoping system.

    
.. _LMI-PCIBridge-SecondaryBusDeviceSelectTiming:

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
    
.. _LMI-PCIBridge-Description:

``string`` **Description**

    The Description property provides a textual description of the object.

    
.. _LMI-PCIBridge-RevisionID:

``uint8`` **RevisionID**

    Register that contains a value assigned by the device manufacturer used to identify the revision number of the device.

    
.. _LMI-PCIBridge-SubsystemVendorID:

``uint16`` **SubsystemVendorID**

    Subsystem vendor ID. ID information is reported from a PCIDevice through protocol-specific requests. The correct place in the CIM Schema for this information is in CIM_Physical Element (the Manufacturer property) for hardware, and CIM_Product (the Vendor property) if the information is related to Product acquisition. This data is also reported here, because it is part of the standard output from the Device and is an optimization.

    
.. _LMI-PCIBridge-FunctionNumber:

``uint8`` **FunctionNumber**

    The function number for this PCI device.

    
.. _LMI-PCIBridge-Name:

``string`` **Name**

    The Name property defines the label by which the object is known. When subclassed, the Name property can be overridden to be a Key property.

    
.. _LMI-PCIBridge-Caption:

``string`` **Caption**

    The Caption property is a short textual description (one- line string) of the object.

    
.. _LMI-PCIBridge-ExpansionROMBaseAddress:

``uint32`` **ExpansionROMBaseAddress**

    Doubleword Expansion ROM-base memory address.

    
.. _LMI-PCIBridge-ClassCode:

``uint8`` **ClassCode**

    Register of 8 bits that identifies the basic function of the PCI device. This property is only the upper byte (offset 0Bh) of the 3-byte ClassCode field. Note that the ValueMap array of the property specifies the decimal representation of this information.

    
    ======== ======================================
    ValueMap Values                                
    ======== ======================================
    0        Pre 2.0                               
    1        Mass Storage                          
    2        Network                               
    3        Display                               
    4        Multimedia                            
    5        Memory                                
    6        Bridge                                
    7        Simple Communications                 
    8        Base Peripheral                       
    9        Input                                 
    10       Docking Station                       
    11       Processor                             
    12       Serial Bus                            
    13       Wireless                              
    14       Intelligent I/O                       
    15       Satellite Communication               
    16       Encryption/Decryption                 
    17       Data Acquisition and Signal Processing
    18..254  PCI Reserved                          
    255      Other                                 
    ======== ======================================
    
.. _LMI-PCIBridge-SubordinateBusNumber:

``uint8`` **SubordinateBusNumber**

    The number of the highest numbered bus that exists behind the bridge.

    
.. _LMI-PCIBridge-CreationClassName:

``string`` **CreationClassName**

    CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

    
.. _LMI-PCIBridge-PrefetchBaseUpper32:

``uint32`` **PrefetchBaseUpper32**

    Upper 32 bits of the supported prefetch base address when 64-bit addressing is used. The lower 32 bits are assumed to be 0.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint64`` :ref:`MaxQuiesceTime <CIM-LogicalDevice-MaxQuiesceTime>`
| ``uint64`` :ref:`TotalPowerOnHours <CIM-LogicalDevice-TotalPowerOnHours>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16`` :ref:`Availability <CIM-LogicalDevice-Availability>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``uint8`` :ref:`MaxLatency <CIM-PCIDevice-MaxLatency>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``uint16[]`` :ref:`AdditionalAvailability <CIM-LogicalDevice-AdditionalAvailability>`
| ``uint16`` :ref:`StatusInfo <CIM-LogicalDevice-StatusInfo>`
| ``string[]`` :ref:`CapabilityDescriptions <CIM-PCIController-CapabilityDescriptions>`
| ``uint32`` :ref:`MaxNumberControlled <CIM-Controller-MaxNumberControlled>`
| ``string`` :ref:`ErrorDescription <CIM-LogicalDevice-ErrorDescription>`
| ``uint32`` :ref:`LastErrorCode <CIM-LogicalDevice-LastErrorCode>`
| ``uint8`` :ref:`MinGrantTime <CIM-PCIDevice-MinGrantTime>`
| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``boolean`` :ref:`SelfTestEnabled <CIM-PCIController-SelfTestEnabled>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string[]`` :ref:`IdentifyingDescriptions <CIM-LogicalDevice-IdentifyingDescriptions>`
| ``boolean`` :ref:`ErrorCleared <CIM-LogicalDevice-ErrorCleared>`
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``uint16`` :ref:`LocationIndicator <CIM-LogicalDevice-LocationIndicator>`
| ``string[]`` :ref:`OtherIdentifyingInfo <CIM-LogicalDevice-OtherIdentifyingInfo>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``datetime`` :ref:`TimeOfLastReset <CIM-Controller-TimeOfLastReset>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint16[]`` :ref:`PowerManagementCapabilities <CIM-LogicalDevice-PowerManagementCapabilities>`
| ``uint64`` :ref:`PowerOnHours <CIM-LogicalDevice-PowerOnHours>`
| ``uint16`` :ref:`ProtocolSupported <CIM-Controller-ProtocolSupported>`
| ``string`` :ref:`ProtocolDescription <CIM-Controller-ProtocolDescription>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`

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

