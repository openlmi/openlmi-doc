.. _CIM-Controller:

CIM_Controller
--------------

Class reference
===============
Subclass of :ref:`CIM_LogicalDevice <CIM-LogicalDevice>`

Controller is a superclass for grouping the miscellaneous control-related Devices that provide a classic bus master interface. Examples of Controllers are USBControllers, SerialControllers, and so on. The Controller class is an abstraction for Devices with a single protocol stack, which exist to control communications (data, control, and reset) to downstream devices. Note that a new abstract class (ProtocolController) has been created to model more complex interface controllers such as SCSI.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-Controller-TimeOfLastReset:

``datetime`` **TimeOfLastReset**

    Time of last reset of the Controller.

    
.. _CIM-Controller-MaxNumberControlled:

``uint32`` **MaxNumberControlled**

    Maximum number of directly addressable entities that are supported by this Controller. A value of 0 should be used if the number is unknown or unlimited.

    
.. _CIM-Controller-ProtocolSupported:

``uint16`` **ProtocolSupported**

    The protocol used by the Controller to access controlled Devices.

    
    ======== =================================
    ValueMap Values                           
    ======== =================================
    1        Other                            
    2        Unknown                          
    3        EISA                             
    4        ISA                              
    5        PCI                              
    6        ATA/ATAPI                        
    7        Flexible Diskette                
    8        1496                             
    9        SCSI Parallel Interface          
    10       SCSI Fibre Channel Protocol      
    11       SCSI Serial Bus Protocol         
    12       SCSI Serial Bus Protocol-2 (1394)
    13       SCSI Serial Storage Architecture 
    14       VESA                             
    15       PCMCIA                           
    16       Universal Serial Bus             
    17       Parallel Protocol                
    18       ESCON                            
    19       Diagnostic                       
    20       I2C                              
    21       Power                            
    22       HIPPI                            
    23       MultiBus                         
    24       VME                              
    25       IPI                              
    26       IEEE-488                         
    27       RS232                            
    28       IEEE 802.3 10BASE5               
    29       IEEE 802.3 10BASE2               
    30       IEEE 802.3 1BASE5                
    31       IEEE 802.3 10BROAD36             
    32       IEEE 802.3 100BASEVG             
    33       IEEE 802.5 Token-Ring            
    34       ANSI X3T9.5 FDDI                 
    35       MCA                              
    36       ESDI                             
    37       IDE                              
    38       CMD                              
    39       ST506                            
    40       DSSI                             
    41       QIC2                             
    42       Enhanced ATA/IDE                 
    43       AGP                              
    44       TWIRP (two-way infrared)         
    45       FIR (fast infrared)              
    46       SIR (serial infrared)            
    47       IrBus                            
    48       Serial ATA                       
    ======== =================================
    
.. _CIM-Controller-ProtocolDescription:

``string`` **ProtocolDescription**

    A free-form string that provides more information that is related to the ProtocolSupported by the Controller.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
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
| ``string`` :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| ``uint16[]`` :ref:`PowerManagementCapabilities <CIM-LogicalDevice-PowerManagementCapabilities>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`MaxQuiesceTime <CIM-LogicalDevice-MaxQuiesceTime>`
| ``uint64`` :ref:`TotalPowerOnHours <CIM-LogicalDevice-TotalPowerOnHours>`
| ``string`` :ref:`ErrorDescription <CIM-LogicalDevice-ErrorDescription>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint32`` :ref:`LastErrorCode <CIM-LogicalDevice-LastErrorCode>`
| ``string`` :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| ``uint16`` :ref:`Availability <CIM-LogicalDevice-Availability>`
| ``string`` :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

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

