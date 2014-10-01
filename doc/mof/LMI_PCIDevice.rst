.. _LMI-PCIDevice:

LMI_PCIDevice
-------------

Class reference
===============
Subclass of :ref:`CIM_PCIDevice <CIM-PCIDevice>`

Capabilities and management of a PCI device controller on an adapter card.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-PCIDevice-VendorID:

``uint16`` **VendorID**

    Register that contains a value assigned by the PCI SIG used to identify the manufacturer of the device.

    
.. _LMI-PCIDevice-InterruptPin:

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
    
.. _LMI-PCIDevice-SubsystemVendorName:

``string`` **SubsystemVendorName**

    Name of the subsystem vendor

    
.. _LMI-PCIDevice-PCIDeviceID:

``uint16`` **PCIDeviceID**

    Register that contains a value assigned by the device manufacturer used to identify the type of device.

    
.. _LMI-PCIDevice-InstanceID:

``string`` **InstanceID**

    InstanceID is an optional property that may be used to opaquely and uniquely identify an instance of this class within the scope of the instantiating Namespace. Various subclasses of this class may override this property to make it required, or a key. Such subclasses may also modify the preferred algorithms for ensuring uniqueness that are defined below.

    To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon (:), and where <OrgID> must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness, <OrgID> must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If not null and the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance. 

    If not set to null for DMTF-defined instances, the "preferred" algorithm must be used with the <OrgID> set to CIM.

    
.. _LMI-PCIDevice-Capabilities:

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
    
.. _LMI-PCIDevice-SubsystemName:

``string`` **SubsystemName**

    Name of the subsystem

    
.. _LMI-PCIDevice-SystemName:

``string`` **SystemName**

    The System Name of the scoping system.

    
.. _LMI-PCIDevice-BaseAddress64:

``uint64[]`` **BaseAddress64**

    Array of doubleword base-memory addresses for 64 bit addresses

    
.. _LMI-PCIDevice-ElementName:

``string`` **ElementName**

    A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. 

    Note that the Name property of ManagedSystemElement is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. Note that if there is an associated instance of CIM_EnabledLogicalElementCapabilities, restrictions on this properties may exist as defined in ElementNameMask and MaxElementNameLen properties defined in that class.

    
.. _LMI-PCIDevice-RevisionID:

``uint8`` **RevisionID**

    Register that contains a value assigned by the device manufacturer used to identify the revision number of the device.

    
.. _LMI-PCIDevice-LatencyTimer:

``uint8`` **LatencyTimer**

    Defines the minimum amount of time, in PCI clock cycles, that the bus master can retain ownership of the bus.

    
.. _LMI-PCIDevice-SubsystemVendorID:

``uint16`` **SubsystemVendorID**

    Subsystem vendor ID. ID information is reported from a PCIDevice through protocol-specific requests. The correct place in the CIM Schema for this information is in CIM_Physical Element (the Manufacturer property) for hardware, and CIM_Product (the Vendor property) if the information is related to Product acquisition. This data is also reported here, because it is part of the standard output from the Device and is an optimization.

    
.. _LMI-PCIDevice-FunctionNumber:

``uint8`` **FunctionNumber**

    The function number for this PCI device.

    
.. _LMI-PCIDevice-Name:

``string`` **Name**

    The Name property defines the label by which the object is known. When subclassed, the Name property can be overridden to be a Key property.

    
.. _LMI-PCIDevice-Caption:

``string`` **Caption**

    The Caption property is a short textual description (one- line string) of the object.

    
.. _LMI-PCIDevice-CommandRegister:

``uint16`` **CommandRegister**

    Current contents of the register that provides basic control over the ability of the device to respond to or perform PCI accesses.

    
.. _LMI-PCIDevice-DeviceSelectTiming:

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
    
.. _LMI-PCIDevice-PCIDeviceName:

``string`` **PCIDeviceName**

    Name of the device

    
.. _LMI-PCIDevice-SubsystemID:

``uint16`` **SubsystemID**

    Subsystem identifier code.

    
.. _LMI-PCIDevice-ExpansionROMBaseAddress:

``uint32`` **ExpansionROMBaseAddress**

    Doubleword Expansion ROM-base memory address.

    
.. _LMI-PCIDevice-VendorName:

``string`` **VendorName**

    Name of the vendor

    
.. _LMI-PCIDevice-CacheLineSize:

``uint8`` **CacheLineSize**

    Specifies the system cache line size in doubleword increments (for example, a 486-based system would store the value 04h, indicating a cache line size of four doublewords.

    
.. _LMI-PCIDevice-BusNumber:

``uint8`` **BusNumber**

    The bus number where this PCI device resides.

    
.. _LMI-PCIDevice-ClassCode:

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
    
.. _LMI-PCIDevice-DeviceNumber:

``uint8`` **DeviceNumber**

    The device number assigned to this PCI device for this bus.

    
.. _LMI-PCIDevice-CreationClassName:

``string`` **CreationClassName**

    CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

    
.. _LMI-PCIDevice-BaseAddress:

``uint32[]`` **BaseAddress**

    Array of doubleword base-memory addresses.

    
.. _LMI-PCIDevice-SystemCreationClassName:

``string`` **SystemCreationClassName**

    The CreationClassName of the scoping system.

    
.. _LMI-PCIDevice-DeviceID:

``string`` **DeviceID**

    An address or other identifying information used to uniquely name the LogicalDevice.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``boolean`` :ref:`SelfTestEnabled <CIM-PCIController-SelfTestEnabled>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`Availability <CIM-LogicalDevice-Availability>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``boolean`` :ref:`ErrorCleared <CIM-LogicalDevice-ErrorCleared>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``string[]`` :ref:`CapabilityDescriptions <CIM-PCIController-CapabilityDescriptions>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string[]`` :ref:`OtherIdentifyingInfo <CIM-LogicalDevice-OtherIdentifyingInfo>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint8`` :ref:`MaxLatency <CIM-PCIDevice-MaxLatency>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``uint16[]`` :ref:`AdditionalAvailability <CIM-LogicalDevice-AdditionalAvailability>`
| ``uint16`` :ref:`StatusInfo <CIM-LogicalDevice-StatusInfo>`
| ``uint16[]`` :ref:`PowerManagementCapabilities <CIM-LogicalDevice-PowerManagementCapabilities>`
| ``uint32`` :ref:`MaxNumberControlled <CIM-Controller-MaxNumberControlled>`
| ``uint64`` :ref:`PowerOnHours <CIM-LogicalDevice-PowerOnHours>`
| ``uint16`` :ref:`ProtocolSupported <CIM-Controller-ProtocolSupported>`
| ``uint64`` :ref:`MaxQuiesceTime <CIM-LogicalDevice-MaxQuiesceTime>`
| ``uint64`` :ref:`TotalPowerOnHours <CIM-LogicalDevice-TotalPowerOnHours>`
| ``string`` :ref:`ErrorDescription <CIM-LogicalDevice-ErrorDescription>`
| ``string`` :ref:`ProtocolDescription <CIM-Controller-ProtocolDescription>`
| ``datetime`` :ref:`TimeOfLastReset <CIM-Controller-TimeOfLastReset>`
| ``string[]`` :ref:`IdentifyingDescriptions <CIM-LogicalDevice-IdentifyingDescriptions>`
| ``uint16`` :ref:`LocationIndicator <CIM-LogicalDevice-LocationIndicator>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint32`` :ref:`LastErrorCode <CIM-LogicalDevice-LastErrorCode>`
| ``uint8`` :ref:`MinGrantTime <CIM-PCIDevice-MinGrantTime>`

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

