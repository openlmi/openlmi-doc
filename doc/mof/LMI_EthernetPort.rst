.. _LMI-EthernetPort:

LMI_EthernetPort
----------------

Class reference
===============
Subclass of :ref:`CIM_EthernetPort <CIM-EthernetPort>`

Capabilities and management of an EthernetPort.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-EthernetPort-MaxSpeed:

``uint64`` **MaxSpeed**

    The maximum bandwidth of the Port in Bits per Second.

    
.. _LMI-EthernetPort-ElementName:

``string`` **ElementName**

    A user-friendly name for the object.

    
.. _LMI-EthernetPort-LinkTechnology:

``uint16`` **LinkTechnology**

    An enumeration of the types of links. When set to 1 ("Other"), the related property OtherLinkTechnology contains a string description of the type of link.

    
    ======== ============
    ValueMap Values      
    ======== ============
    0        Unknown     
    1        Other       
    2        Ethernet    
    3        IB          
    4        FC          
    5        FDDI        
    6        ATM         
    7        Token Ring  
    8        Frame Relay 
    9        Infrared    
    10       BlueTooth   
    11       Wireless LAN
    ======== ============
    
.. _LMI-EthernetPort-NetworkAddresses:

``string[]`` **NetworkAddresses**

    Ethernet/802.3 MAC addresses formatted as twelve hexadecimal digits (for example, ``010203040506``), with each pair representing one of the six octets of the MAC address in ``canonical`` bit order. (Therefore, the Group address bit is found in the low order bit of the first character of the string.)

    
.. _LMI-EthernetPort-PermanentAddress:

``string`` **PermanentAddress**

    PermanentAddress defines the network address that is hardcoded into a port. This 'hardcoded' address can be changed using a firmware upgrade or a software configuration. When this change is made, the field should be updated at the same time. PermanentAddress should be left blank if no 'hardcoded' address exists for the NetworkAdapter.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string`` :ref:`OtherNetworkPortType <CIM-NetworkPort-OtherNetworkPortType>`
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``string[]`` :ref:`OtherIdentifyingInfo <CIM-LogicalDevice-OtherIdentifyingInfo>`
| ``uint16[]`` :ref:`Capabilities <CIM-EthernetPort-Capabilities>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint64`` :ref:`SupportedMaximumTransmissionUnit <CIM-NetworkPort-SupportedMaximumTransmissionUnit>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``string[]`` :ref:`IdentifyingDescriptions <CIM-LogicalDevice-IdentifyingDescriptions>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``boolean`` :ref:`ErrorCleared <CIM-LogicalDevice-ErrorCleared>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`PoEPowerEntityType <CIM-EthernetPort-PoEPowerEntityType>`
| ``uint16`` :ref:`PVID <CIM-EthernetPort-PVID>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`PortNumber <CIM-NetworkPort-PortNumber>`
| ``string`` :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16`` :ref:`LocationIndicator <CIM-LogicalDevice-LocationIndicator>`
| ``uint32`` :ref:`MaxDataSize <CIM-EthernetPort-MaxDataSize>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``uint16[]`` :ref:`EnabledCapabilities <CIM-EthernetPort-EnabledCapabilities>`
| ``uint64`` :ref:`PowerOnHours <CIM-LogicalDevice-PowerOnHours>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``uint16[]`` :ref:`AdditionalAvailability <CIM-LogicalDevice-AdditionalAvailability>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16`` :ref:`StatusInfo <CIM-LogicalDevice-StatusInfo>`
| ``string[]`` :ref:`CapabilityDescriptions <CIM-EthernetPort-CapabilityDescriptions>`
| ``string[]`` :ref:`PortDiscriminator <CIM-EthernetPort-PortDiscriminator>`
| ``uint16[]`` :ref:`PowerManagementCapabilities <CIM-LogicalDevice-PowerManagementCapabilities>`
| ``uint16`` :ref:`PortType <CIM-EthernetPort-PortType>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``boolean`` :ref:`FullDuplex <CIM-NetworkPort-FullDuplex>`
| ``uint64`` :ref:`MaxQuiesceTime <CIM-LogicalDevice-MaxQuiesceTime>`
| ``uint64`` :ref:`TotalPowerOnHours <CIM-LogicalDevice-TotalPowerOnHours>`
| ``string`` :ref:`ErrorDescription <CIM-LogicalDevice-ErrorDescription>`
| ``uint16`` :ref:`UsageRestriction <CIM-LogicalPort-UsageRestriction>`
| ``string`` :ref:`OtherPortType <CIM-LogicalPort-OtherPortType>`
| ``uint64`` :ref:`RequestedSpeed <CIM-LogicalPort-RequestedSpeed>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint32`` :ref:`LastErrorCode <CIM-LogicalDevice-LastErrorCode>`
| ``uint64`` :ref:`ActiveMaximumTransmissionUnit <CIM-NetworkPort-ActiveMaximumTransmissionUnit>`
| ``boolean`` :ref:`AutoSense <CIM-NetworkPort-AutoSense>`
| ``string`` :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| ``string`` :ref:`OtherLinkTechnology <CIM-NetworkPort-OtherLinkTechnology>`
| ``uint64`` :ref:`Speed <CIM-NetworkPort-Speed>`
| ``uint16`` :ref:`Availability <CIM-LogicalDevice-Availability>`
| ``string`` :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`
| ``string[]`` :ref:`OtherEnabledCapabilities <CIM-EthernetPort-OtherEnabledCapabilities>`

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

