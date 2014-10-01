.. _CIM-LinkAggregator8023ad:

CIM_LinkAggregator8023ad
------------------------

Class reference
===============
Subclass of :ref:`CIM_ProtocolEndpoint <CIM-ProtocolEndpoint>`

The LinkAggregator8023ad class represents an instance of an 802.3ad aggregator in a system. The word actor is used in property names to refer to the local entity of an aggregation.


Key properties
^^^^^^^^^^^^^^

| :ref:`CreationClassName <CIM-ServiceAccessPoint-CreationClassName>`
| :ref:`SystemName <CIM-ServiceAccessPoint-SystemName>`
| :ref:`Name <CIM-ServiceAccessPoint-Name>`
| :ref:`SystemCreationClassName <CIM-ServiceAccessPoint-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-LinkAggregator8023ad-ActorSystemID:

``string`` **ActorSystemID**

    A 6-octet MAC address value used as a unique identifier for the System that contains this Aggregator. NOTE: From the perspective of the Link Aggregation mechanisms described in Clause 43 (IEEE 802.3ad), only a single combination of Actor's System ID and System Priority are considered, and no distinction is made between the values of these parameters for an Aggregator and the port(s) that are associated with it; i.e., the protocol is described in terms of the operation of aggregation within a single System. However, the managed objects provided for the Aggregator and the port both allow management of these parameters. The result of this is to permit a single piece of equipment to be configured by management to contain more than one System from the point of view of the operation of Link Aggregation. This may be of particular use in the configuration of equipment that has limited aggregation capability. Note that the MAC address is formatted as twelve hexadecimal digits (e.g., "010203040506"), with each pair representing one of the six octets of the MAC address in "canonical" bit order according to RFC 2469.

    
.. _CIM-LinkAggregator8023ad-ActorAdminKey:

``uint16`` **ActorAdminKey**

    The current administrative value of the 16-bit Key for the Aggregator (Actor). The administrative Key value may differ from the operational Key value for reasons discussed in the IEEE 802.3ad document, Section 43.6.2. The meaning of particular Key values is of local significance.

    
.. _CIM-LinkAggregator8023ad-TimeOfLastOperChange:

``datetime`` **TimeOfLastOperChange**

    This object indicates the time of the most recent change to this aggregator, its list of aggregated ports, or configuration of a aggregation port member.

    
.. _CIM-LinkAggregator8023ad-ProtocolIFType:

``uint16`` **ProtocolIFType**

    ProtocolIFType's enumeration is limited to 802.3 LinkAggregation and reserved values for this subclass of ProtocolEndpoint.

    
    =========== ===============
    ValueMap    Values         
    =========== ===============
    1           Other          
    161         IEEE8023adLAG  
    225..4095   IANA Reserved  
    4301..32767 DMTF Reserved  
    32768..     Vendor Reserved
    =========== ===============
    
.. _CIM-LinkAggregator8023ad-ActorSystemPriority:

``uint16`` **ActorSystemPriority**

    A 2-octet value indicating the priority value associated with the Actor's System ID. The system with the lower value has the higher priority. Guidelines for the use of system and port priorities is given in IEEE 802.3ad document, Section 43.6.

    
.. _CIM-LinkAggregator8023ad-CollectorMaxDelay:

``datetime`` **CollectorMaxDelay**

    The value of this datetime property (expressed using an interval format) defines the maximum delay that may be imposed by the Frame Collector between receiving a frame from an Aggregator Parser, and either delivering the frame to its MAC Client or discarding the frame.

    
.. _CIM-LinkAggregator8023ad-RepresentsAggregate:

``boolean`` **RepresentsAggregate**

    A Boolean value indicating whether the Aggregator represents an Aggregate (TRUE) or an Individual link (FALSE).

    
.. _CIM-LinkAggregator8023ad-MACAddress:

``string`` **MACAddress**

    A 6-octet value carrying the individual MAC address assigned to the Aggregator. Note that the MAC address is formatted as twelve hexadecimal digits (e.g., "010203040506"), with each pair representing one of the six octets of the MAC address in "canonical" bit order according to RFC 2469.

    
.. _CIM-LinkAggregator8023ad-ActorOperKey:

``uint16`` **ActorOperKey**

    The current operational value of the 16-bit Key forthe Aggregator (Actor). The administrative Key value may differ from the operational Key value for reasons discussed in the IEEE 802.3ad document, Section 43.6.2. The meaning of particular Key values is of local significance.

    

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
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`Name <CIM-ProtocolEndpoint-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-ProtocolEndpoint-EnabledState>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`OtherTypeDescription <CIM-ProtocolEndpoint-OtherTypeDescription>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
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

