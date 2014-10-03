.. _CIM-NetworkPort:

CIM_NetworkPort
---------------

Class reference
===============
Subclass of :ref:`CIM_LogicalPort <CIM-LogicalPort>`

NetworkPort is the logical representation of network communications hardware such as a physical connector and the setup or operation of the network chips, at the lowest layers of a network stack.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-NetworkPort-OtherNetworkPortType:

``string`` **OtherNetworkPortType**

    **Deprecated!** 
    Note: The use of this property is deprecated in lieu of CIM_LogicalPort.PortType. 

    Deprecated description: The type of module, when PortType is set to 1 ("Other".)

    
.. _CIM-NetworkPort-SupportedMaximumTransmissionUnit:

``uint64`` **SupportedMaximumTransmissionUnit**

    The maximum transmission unit (MTU) that can be supported.

    
.. _CIM-NetworkPort-LinkTechnology:

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
    
.. _CIM-NetworkPort-PortNumber:

``uint16`` **PortNumber**

    NetworkPorts are often numbered relative to either a logical module or a network element.

    
.. _CIM-NetworkPort-NetworkAddresses:

``string[]`` **NetworkAddresses**

    An array of strings that indicates the network addresses for the port.

    
.. _CIM-NetworkPort-PermanentAddress:

``string`` **PermanentAddress**

    PermanentAddress defines the network address that is hardcoded into a port. This 'hardcoded' address can be changed using a firmware upgrade or a software configuration. When this change is made, the field should be updated at the same time. PermanentAddress should be left blank if no 'hardcoded' address exists for the NetworkAdapter.

    
.. _CIM-NetworkPort-FullDuplex:

``boolean`` **FullDuplex**

    Boolean that indicates that the port is operating in full duplex mode.

    
.. _CIM-NetworkPort-ActiveMaximumTransmissionUnit:

``uint64`` **ActiveMaximumTransmissionUnit**

    The active or negotiated maximum transmission unit (MTU) that can be supported.

    
.. _CIM-NetworkPort-AutoSense:

``boolean`` **AutoSense**

    A Boolean that indicates whether the NetworkPort is capable of automatically determining the speed or other communications characteristics of the attached network media.

    
.. _CIM-NetworkPort-OtherLinkTechnology:

``string`` **OtherLinkTechnology**

    A string value that describes LinkTechnology when it is set to 1, "Other".

    
.. _CIM-NetworkPort-Speed:

``uint64`` **Speed**

    The current bandwidth of the Port in Bits per Second. For ports that vary in bandwidth or for those where no accurate estimation can be made, this property should contain the nominal bandwidth.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``uint64`` :ref:`MaxSpeed <CIM-LogicalPort-MaxSpeed>`
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
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
| ``uint16`` :ref:`PortType <CIM-LogicalPort-PortType>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`MaxQuiesceTime <CIM-LogicalDevice-MaxQuiesceTime>`
| ``uint64`` :ref:`TotalPowerOnHours <CIM-LogicalDevice-TotalPowerOnHours>`
| ``string`` :ref:`ErrorDescription <CIM-LogicalDevice-ErrorDescription>`
| ``uint16`` :ref:`UsageRestriction <CIM-LogicalPort-UsageRestriction>`
| ``string`` :ref:`OtherPortType <CIM-LogicalPort-OtherPortType>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint32`` :ref:`LastErrorCode <CIM-LogicalDevice-LastErrorCode>`
| ``string`` :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| ``uint16`` :ref:`Availability <CIM-LogicalDevice-Availability>`
| ``string`` :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`
| ``uint64`` :ref:`RequestedSpeed <CIM-LogicalPort-RequestedSpeed>`

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

