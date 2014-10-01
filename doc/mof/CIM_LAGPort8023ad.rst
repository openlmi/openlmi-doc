.. _CIM-LAGPort8023ad:

CIM_LAGPort8023ad
-----------------

Class reference
===============
Subclass of :ref:`CIM_ProtocolEndpoint <CIM-ProtocolEndpoint>`

LAGPort8023ad contains the configuration information for a port (LANEndpoint) which is a member of a link aggregation. This port aspect is associated to LANEndpoint using the ConcreteIdentity relationship. A port may be attached to an instance of LinkAggregator8023ad. This is described using the BindsTo association. The latter is described in the IEEE 802.3ad document, Subclause 30.7.2.1.13, and maps the information in MIB.IEEE|IEEE8023-LAG-MIB.dot3adAggPortAttachedAggID.


Key properties
^^^^^^^^^^^^^^

| :ref:`CreationClassName <CIM-ServiceAccessPoint-CreationClassName>`
| :ref:`SystemName <CIM-ServiceAccessPoint-SystemName>`
| :ref:`Name <CIM-ServiceAccessPoint-Name>`
| :ref:`SystemCreationClassName <CIM-ServiceAccessPoint-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-LAGPort8023ad-ActorSystemID:

``string`` **ActorSystemID**

    A 6-octet MAC address value that defines the value of the System ID for the System that contains this Aggregation Port. For more information, refer to the IEEE 802.3 document, Subclause 30.7.2.1.3. Note that the MAC address is formatted as twelve hexadecimal digits (e.g., "010203040506"), with each pair representing one of the six octets of the MAC address in "canonical" bit order according to RFC 2469.

    
.. _CIM-LAGPort8023ad-ActorPort:

``uint16`` **ActorPort**

    The port number locally assigned to the Aggregation Port. The port number is communicated in LACPDUs as the Actor_Port. For more information, refer to the IEEE 802.3 document, Subclause 30.7.2.1.14.

    
.. _CIM-LAGPort8023ad-ActorPortPriority:

``uint16`` **ActorPortPriority**

    The priority value locally assigned to this Aggregation Port. For more information, refer to the IEEE 802.3 document, Subclause 30.7.2.1.15.

    
.. _CIM-LAGPort8023ad-ActorAdminState:

``uint16[]`` **ActorAdminState**

    An enumerated array allowing administrator control of the Port's state (described in the IEEE 802.3ad document, Subclause 30.7.2.1.20, and transmitted by the Actor in LACPDUs).

    
    ======== =================
    ValueMap Values           
    ======== =================
    0        Unknown/Undefined
    2        LACP_Activity    
    3        LACP_Timeout     
    4        Aggregation      
    5        Synchronization  
    6        Collecting       
    7        Distributing     
    8        Defaulted        
    9        Expired          
    ======== =================
    
.. _CIM-LAGPort8023ad-ActorSystemPriority:

``uint16`` **ActorSystemPriority**

    A 2-octet value used to define the priority value associated with the Actor's System ID. For more information, refer to the IEEE 802.3 document, Subclause 30.7.2.1.2.

    
.. _CIM-LAGPort8023ad-RepresentsAggregate:

``boolean`` **RepresentsAggregate**

    A Boolean value indicating whether the Aggregation Port is able to Aggregate (`TRUE') or is only able to operate as an Individual link ('FALSE'). For more information, refer to the IEEE 802.3 document, Subclause 30.7.2.1.24.

    
.. _CIM-LAGPort8023ad-SelectedAggID:

``uint32`` **SelectedAggID**

    The identifier value of the Aggregator that this Aggregation Port has currently selected. Zero indicates that the Aggregation Port has not selected an Aggregator, either because it is in the process of detaching from an Aggregator or because there is no suitable Aggregator available for it to select. For more information, refer to the IEEE 802.3ad document, Subclause 30.7.2.1.12.

    
.. _CIM-LAGPort8023ad-ActorOperKey:

``uint16`` **ActorOperKey**

    The current operational value of the 16-bit Key for the Aggregation Port. The meaning of particular Key values is of local significance. For more information, refer to the IEEE 802.3 document, Subclause 30.7.2.1.5.

    
.. _CIM-LAGPort8023ad-ActorOperState:

``uint16[]`` **ActorOperState**

    An enumerated array corresponding to the currentoperational values of Actor_State as transmitted by the Actor in LACPDUs and described in the IEEE 802.3ad document, Subclause 30.7.2.1.21.

    
    ======== =================
    ValueMap Values           
    ======== =================
    0        Unknown/Undefined
    2        LACP_Activity    
    3        LACP_Timeout     
    4        Aggregation      
    5        Synchronization  
    6        Collecting       
    7        Distributing     
    8        Defaulted        
    9        Expired          
    ======== =================
    

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
| ``string`` :ref:`SystemName <CIM-ServiceAccessPoint-SystemName>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-ProtocolEndpoint-TimeOfLastStateChange>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ProtocolEndpoint-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`NameFormat <CIM-ProtocolEndpoint-NameFormat>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`Name <CIM-ProtocolEndpoint-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`ProtocolIFType <CIM-ProtocolEndpoint-ProtocolIFType>`
| ``uint16`` :ref:`EnabledState <CIM-ProtocolEndpoint-EnabledState>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`OtherTypeDescription <CIM-ProtocolEndpoint-OtherTypeDescription>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``boolean`` :ref:`BroadcastResetSupported <CIM-ProtocolEndpoint-BroadcastResetSupported>`
| ``uint16`` :ref:`ProtocolType <CIM-ProtocolEndpoint-ProtocolType>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ProtocolEndpoint-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`CreationClassName <CIM-ServiceAccessPoint-CreationClassName>`
| ``string`` :ref:`SystemCreationClassName <CIM-ServiceAccessPoint-SystemCreationClassName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`BroadcastReset <CIM-ProtocolEndpoint-BroadcastReset>`
| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`

