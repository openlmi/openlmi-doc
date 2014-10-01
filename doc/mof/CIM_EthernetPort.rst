.. _CIM-EthernetPort:

CIM_EthernetPort
----------------

Class reference
===============
Subclass of :ref:`CIM_NetworkPort <CIM-NetworkPort>`

Capabilities and management of an EthernetPort.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-EthernetPort-Capabilities:

``uint16[]`` **Capabilities**

    Capabilities of the EthernetPort. For example, the Device might support AlertOnLan, WakeOnLan, Load Balancing, or FailOver. If failover or load balancing capabilities are listed, a SpareGroup (failover) or ExtraCapacityGroup (load balancing) should also be defined to completely describe the capability. LLDP indicates that this Ethernet Port is capable of supporting Link Layer Discovery Protocol (LLDP) communications. PoE indicates that this Ethernet Port is capable of supporting Power over Ethernet (PoE). EEE indicates that this Ethernet Port is capable of supporting Energy Efficient Ethernet (EEE). DCE indicates that this Ethernet Port is capable of supporting Data Center Ethernet. Data Center Ethernet requires support for Prioritiy-Based Flow Control (PFC), Enhanced Transmission Selection (ETS), and Data Center Bridging eXchange (DCBX) protocol. VDP indicates that this Ethernet Port is capable of supporting Virtual Station Interface (VSI) Discovery Protocol. S-Channel indicates that this Ethernet Port is capable of supporting S-Channel.

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Unknown      
    1        Other        
    2        AlertOnLan   
    3        WakeOnLan    
    4        FailOver     
    5        LoadBalancing
    6        LLDP         
    7        PoE          
    8        EEE          
    9        DCE          
    10       VDP          
    11       S-Channel    
    ..       DMTF Reserved
    ======== =============
    
.. _CIM-EthernetPort-PoEPowerEntityType:

``uint16`` **PoEPowerEntityType**

    This property indicates the Power over Ethernet power entity type.

    
    ======== ========================
    ValueMap Values                  
    ======== ========================
    0        None                    
    1        Other                   
    2        Power Sourcing Equipment
    3        Powered Device          
    ..       DMTF Reserved           
    ======== ========================
    
.. _CIM-EthernetPort-PVID:

``uint16`` **PVID**

    Each ethernet port on an ethernet switch has a VLAN ID that is called Port VLAN ID (PVID). The PVID will be applied to the frames which are untagged or tagged with priority ( vid = 0 ). This property indicates the PVID of the Ethernet port.

    
.. _CIM-EthernetPort-MaxDataSize:

``uint32`` **MaxDataSize**

    The maximum size of the INFO (non-MAC) field that will be received or transmitted.

    
.. _CIM-EthernetPort-EnabledCapabilities:

``uint16[]`` **EnabledCapabilities**

    Specifies which capabilities are enabled from the list of all supported ones, which are defined in the Capabilities array. For details on each capability, see the description of each capability in the description of property Capabilities.

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Unknown      
    1        Other        
    2        AlertOnLan   
    3        WakeOnLan    
    4        FailOver     
    5        LoadBalancing
    6        LLDP         
    7        PoE          
    8        EEE          
    9        DCE          
    10       VDP          
    11       S-Channel    
    ..       DMTF Reserved
    ======== =============
    
.. _CIM-EthernetPort-NetworkAddresses:

``string[]`` **NetworkAddresses**

    Ethernet/802.3 MAC addresses formatted as twelve hexadecimal digits (for example, "010203040506"), with each pair representing one of the six octets of the MAC address in "canonical" bit order. (Therefore, the Group address bit is found in the low order bit of the first character of the string.)

    
.. _CIM-EthernetPort-CapabilityDescriptions:

``string[]`` **CapabilityDescriptions**

    An array of free-form strings that provides more detailed explanations for any of the EthernetPort features that are indicated in the Capabilities array. Note, each entry of this array is related to the entry in the Capabilities array that is located at the same index.

    
.. _CIM-EthernetPort-PortDiscriminator:

``string[]`` **PortDiscriminator**

    A string array used to discriminate the supported context of this EthernetPort. The following strings are currently defined: 

    'SNIA:None' - indicates this EthernetPort does not provide support for any specific function.

    'SNIA:iSCSI' - indicates this EthernetPort provides support for iSCSI.

    'SNIA:FCoE' - indicates that this EthernetPort provides support for FC over Ethernet - FCoE.

    
.. _CIM-EthernetPort-PortType:

``uint16`` **PortType**

    The specific mode that is currently enabled for the Port. When set to 1 ("Other"), the related property OtherPortType contains a string description of the type of port.

    
    ============ ========================
    ValueMap     Values                  
    ============ ========================
    0            Unknown                 
    1            Other                   
    50           10BaseT                 
    51           10-100BaseT             
    52           100BaseT                
    53           1000BaseT               
    54           2500BaseT               
    55           10GBaseT                
    56           10GBase-CX4             
    57           1000Base-KX             
    58           10GBase-KX4             
    59           10GBase-KR              
    60           1000-10GBase-KX         
    61           1000Base-KX10GBase-KX4KR
    62           10-100-1000BaseT        
    63           100-1000-10GBaseT       
    100          100Base-FX              
    101          100Base-SX              
    102          1000Base-SX             
    103          1000Base-LX             
    104          1000Base-CX             
    105          10GBase-SR              
    106          10GBase-SW              
    107          10GBase-LX4             
    108          10GBase-LR              
    109          10GBase-LW              
    110          10GBase-ER              
    111          10GBase-EW              
    112          10GBase-LRM             
    200          40GBase-KR4             
    201          40GBase-CR4             
    202          40GBase-SR4             
    203          40GBase-FR              
    204          40GBase-LR4             
    300          100GBase-CR10           
    301          100GBase-SR10           
    302          100GBase-LR4            
    303          100GBase-ER4            
    304          100GBase-KR4            
    305          100GBase-CR4            
    306          100GBase-KP4            
    16000..65535 Vendor Reserved         
    ============ ========================
    
.. _CIM-EthernetPort-OtherEnabledCapabilities:

``string[]`` **OtherEnabledCapabilities**

    An array of free-form strings that provides more detailed explanations for any of the enabled capabilities that are specified as 'Other'.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``uint64`` :ref:`MaxSpeed <CIM-LogicalPort-MaxSpeed>`
| ``string`` :ref:`OtherNetworkPortType <CIM-NetworkPort-OtherNetworkPortType>`
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``string[]`` :ref:`OtherIdentifyingInfo <CIM-LogicalDevice-OtherIdentifyingInfo>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint64`` :ref:`SupportedMaximumTransmissionUnit <CIM-NetworkPort-SupportedMaximumTransmissionUnit>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint16`` :ref:`LinkTechnology <CIM-NetworkPort-LinkTechnology>`
| ``string[]`` :ref:`IdentifyingDescriptions <CIM-LogicalDevice-IdentifyingDescriptions>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``boolean`` :ref:`ErrorCleared <CIM-LogicalDevice-ErrorCleared>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`PortNumber <CIM-NetworkPort-PortNumber>`
| ``string`` :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16`` :ref:`LocationIndicator <CIM-LogicalDevice-LocationIndicator>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``uint64`` :ref:`PowerOnHours <CIM-LogicalDevice-PowerOnHours>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``uint16[]`` :ref:`AdditionalAvailability <CIM-LogicalDevice-AdditionalAvailability>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16`` :ref:`StatusInfo <CIM-LogicalDevice-StatusInfo>`
| ``uint16[]`` :ref:`PowerManagementCapabilities <CIM-LogicalDevice-PowerManagementCapabilities>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``string`` :ref:`PermanentAddress <CIM-NetworkPort-PermanentAddress>`
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

