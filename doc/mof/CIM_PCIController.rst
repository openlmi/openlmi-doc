.. _CIM-PCIController:

CIM_PCIController
-----------------

Class reference
===============
Subclass of :ref:`CIM_Controller <CIM-Controller>`

PCIController is a superclass for the PCIBridge and PCIDevice classes. These classes model adapters and bridges on a PCI bus. The properties in PCIController and its subclasses are defined in the various PCI Specifications that are published by the PCI SIG.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-PCIController-InterruptPin:

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
    
.. _CIM-PCIController-Capabilities:

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
    
.. _CIM-PCIController-SelfTestEnabled:

``boolean`` **SelfTestEnabled**

    Reports if the PCI device can perform the self-test function. Returns bit 7 of the BIST register as a Boolean.

    
.. _CIM-PCIController-LatencyTimer:

``uint8`` **LatencyTimer**

    Defines the minimum amount of time, in PCI clock cycles, that the bus master can retain ownership of the bus.

    
.. _CIM-PCIController-DeviceSelectTiming:

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
    
.. _CIM-PCIController-CommandRegister:

``uint16`` **CommandRegister**

    Current contents of the register that provides basic control over the ability of the device to respond to or perform PCI accesses.

    
.. _CIM-PCIController-CapabilityDescriptions:

``string[]`` **CapabilityDescriptions**

    An array of free-form strings that provides more detailed explanations for any of the PCIController features that are indicated in the Capabilities array. Note, each entry of this array is related to the entry in the Capabilities array that is located at the same index.

    
.. _CIM-PCIController-ExpansionROMBaseAddress:

``uint32`` **ExpansionROMBaseAddress**

    Doubleword Expansion ROM-base memory address.

    
.. _CIM-PCIController-CacheLineSize:

``uint8`` **CacheLineSize**

    Specifies the system cache line size in doubleword increments (for example, a 486-based system would store the value 04h, indicating a cache line size of four doublewords.

    
.. _CIM-PCIController-ClassCode:

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
    

Local methods
^^^^^^^^^^^^^

    .. _CIM-PCIController-BISTExecution:

``uint8`` **BISTExecution** ()

    Method to invoke PCI device self-test. This method sets bit 6 of the BIST register. The return result is the lower 4 bits of the BIST register where 0 indicates success and non-zero is a device-dependent failure. Support for this method is optional in the PCI Specification.

    
    **Parameters**
    
*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``datetime`` :ref:`TimeOfLastReset <CIM-Controller-TimeOfLastReset>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``string[]`` :ref:`IdentifyingDescriptions <CIM-LogicalDevice-IdentifyingDescriptions>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``boolean`` :ref:`ErrorCleared <CIM-LogicalDevice-ErrorCleared>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16`` :ref:`LocationIndicator <CIM-LogicalDevice-LocationIndicator>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string[]`` :ref:`OtherIdentifyingInfo <CIM-LogicalDevice-OtherIdentifyingInfo>`
| ``uint64`` :ref:`PowerOnHours <CIM-LogicalDevice-PowerOnHours>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``uint16[]`` :ref:`AdditionalAvailability <CIM-LogicalDevice-AdditionalAvailability>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16`` :ref:`StatusInfo <CIM-LogicalDevice-StatusInfo>`
| ``uint16[]`` :ref:`PowerManagementCapabilities <CIM-LogicalDevice-PowerManagementCapabilities>`
| ``uint32`` :ref:`MaxNumberControlled <CIM-Controller-MaxNumberControlled>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint16`` :ref:`ProtocolSupported <CIM-Controller-ProtocolSupported>`
| ``uint64`` :ref:`MaxQuiesceTime <CIM-LogicalDevice-MaxQuiesceTime>`
| ``uint64`` :ref:`TotalPowerOnHours <CIM-LogicalDevice-TotalPowerOnHours>`
| ``string`` :ref:`ErrorDescription <CIM-LogicalDevice-ErrorDescription>`
| ``string`` :ref:`ProtocolDescription <CIM-Controller-ProtocolDescription>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint32`` :ref:`LastErrorCode <CIM-LogicalDevice-LastErrorCode>`
| ``string`` :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| ``uint16`` :ref:`Availability <CIM-LogicalDevice-Availability>`
| ``string`` :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`
| ``string`` :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`Reset <CIM-LogicalDevice-Reset>`
| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`
| :ref:`SetPowerState <CIM-LogicalDevice-SetPowerState>`
| :ref:`QuiesceDevice <CIM-LogicalDevice-QuiesceDevice>`
| :ref:`EnableDevice <CIM-LogicalDevice-EnableDevice>`
| :ref:`OnlineDevice <CIM-LogicalDevice-OnlineDevice>`
| :ref:`SaveProperties <CIM-LogicalDevice-SaveProperties>`
| :ref:`RestoreProperties <CIM-LogicalDevice-RestoreProperties>`

