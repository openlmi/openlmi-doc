.. _CIM-SwitchService:

CIM_SwitchService
-----------------

Class reference
===============
Subclass of :ref:`CIM_ForwardingService <CIM-ForwardingService>`

Generic switch (bridging) service class. Additional switching functions are incorporated as subordinate services related to this class via ServiceComponent associations.


Key properties
^^^^^^^^^^^^^^

| :ref:`Name <CIM-Service-Name>`
| :ref:`SystemName <CIM-Service-SystemName>`
| :ref:`SystemCreationClassName <CIM-Service-SystemCreationClassName>`
| :ref:`CreationClassName <CIM-Service-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-SwitchService-BridgeType:

``uint8`` **BridgeType**

    Indicates what type of switching service can be performed.

    
    ======== ================
    ValueMap Values          
    ======== ================
    1        Unknown         
    2        Transparent-only
    3        SourceRoute-only
    4        SRT             
    ======== ================
    
.. _CIM-SwitchService-BridgeAddressType:

``uint16`` **BridgeAddressType**

    BridgeAddressType defines the type of addressing scheme used for this Bridge and its BridgeAddress property.

    
    ======== ============================
    ValueMap Values                      
    ======== ============================
    1        Other                       
    2        IPv4                        
    3        IPv6                        
    4        MAC                         
    5        MAC + Spanning Tree Priority
    ======== ============================
    
.. _CIM-SwitchService-NumPorts:

``uint16`` **NumPorts**

    The number of switch ports controlled by this switching service.

    
.. _CIM-SwitchService-BridgeAddress:

``string`` **BridgeAddress**

    Address used by this SwitchService when it must be uniquely identified. For an ethernet bridge, the MAC Address serves as the BridgeAddress. When concatenated with a SpanningTreeService Priority, a unique bridge identifier results. The MAC address is formatted as twelve hexadecimal digits (e.g., "010203040506"), with each pair representing one of the six octets of the MAC address in "canonical" bit order according to RFC 2469. In other scenarios, like Ipv6, the address is formatted as "ffff:ffff:ffff:ffff".

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`SystemName <CIM-Service-SystemName>`
| ``string`` :ref:`LoSID <CIM-Service-LoSID>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``boolean`` :ref:`Started <CIM-Service-Started>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`Name <CIM-Service-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``string`` :ref:`LoSOrgID <CIM-Service-LoSOrgID>`
| ``string`` :ref:`PrimaryOwnerContact <CIM-Service-PrimaryOwnerContact>`
| ``string[]`` :ref:`StartupConditions <CIM-NetworkService-StartupConditions>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`StartMode <CIM-Service-StartMode>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``string[]`` :ref:`StartupParameters <CIM-NetworkService-StartupParameters>`
| ``uint16`` :ref:`ProtocolType <CIM-ForwardingService-ProtocolType>`
| ``string`` :ref:`OtherProtocolType <CIM-ForwardingService-OtherProtocolType>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`SystemCreationClassName <CIM-Service-SystemCreationClassName>`
| ``string`` :ref:`ServiceURL <CIM-NetworkService-ServiceURL>`
| ``string[]`` :ref:`Keywords <CIM-NetworkService-Keywords>`
| ``string`` :ref:`CreationClassName <CIM-Service-CreationClassName>`
| ``string`` :ref:`PrimaryOwnerName <CIM-Service-PrimaryOwnerName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`
| :ref:`StartService <CIM-Service-StartService>`
| :ref:`StopService <CIM-Service-StopService>`
| :ref:`ChangeAffectedElementsAssignedSequence <CIM-Service-ChangeAffectedElementsAssignedSequence>`

