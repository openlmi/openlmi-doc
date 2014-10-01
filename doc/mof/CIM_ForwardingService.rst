.. _CIM-ForwardingService:

CIM_ForwardingService
---------------------

Class reference
===============
Subclass of :ref:`CIM_NetworkService <CIM-NetworkService>`

This class represents the functions used in forwarding network traffic. Its instances act on packets received from one or more ProtocolEndpoints or Services, and drop (discard), or send those packets to one or more other ProtocolEndpoints or Services. The explicit Endpoints being forwarded between, are described using the ForwardsAmong association (or one of its subclasses). Generally, the Endpoints are at the same protocol layer and are usually of similar types, or of the same type. ForwardingService is different than RouteCalculation Service in that it represents the function of forwarding traffic independent of calculating routing information. 



Examining the ForwardingService class definition, note that its superclass NetworkService is deprecated. Therefore, NetworkService's properties need not be implemented in an instance of ForwardingService. Unfortunately, NetworkService cannot be removed from the object hierarchy without a major Schema release. When/if this occurs, the NetworkService superclass will be removed, and ForwardingService will subclass from CIM_Service directly. Also note that there are a large number of additional protocols that are not currently modeled. These will be added over time.


Key properties
^^^^^^^^^^^^^^

| :ref:`Name <CIM-Service-Name>`
| :ref:`SystemName <CIM-Service-SystemName>`
| :ref:`SystemCreationClassName <CIM-Service-SystemCreationClassName>`
| :ref:`CreationClassName <CIM-Service-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-ForwardingService-ProtocolType:

``uint16`` **ProtocolType**

    This defines the type of protocol that is being forwarded.

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Unknown      
    1        Other        
    2        IPv4         
    3        IPv6         
    4        IPv4/IPv6    
    5        IPX          
    6        AppleTalk    
    7        DECnet       
    8        SNA          
    9        CONP         
    10       CLNP         
    11       VINES        
    12       XNS          
    13       ATM          
    14       Frame Relay  
    15       Ethernet     
    16       TokenRing    
    17       FDDI         
    18       Infiniband   
    19       Fibre Channel
    ======== =============
    
.. _CIM-ForwardingService-OtherProtocolType:

``string`` **OtherProtocolType**

    This defines the type of protocol that is being forwarded when the value of the ProtocolType attribute is 1 (i.e., "Other"). This provides for future extensibility.

    

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

