.. _LMI-LAGPort8023ad:

LMI_LAGPort8023ad
-----------------

Class reference
===============
Subclass of :ref:`CIM_LAGPort8023ad <CIM-LAGPort8023ad>`

LAGPort8023ad contains the configuration information for a port (LANEndpoint) which is a member of a link aggregation. This port aspect is associated to LANEndpoint using the LinkAggregationConcreteIdentity relationship. A port may be attached to an instance of LinkAggregator8023ad. This is described using the LinkAggregationBindsTo association. The latter is described in the IEEE 802.3ad document, Subclause 30.7.2.1.13, and maps the information in MIB.IEEE|IEEE8023-LAG-MIB.dot3adAggPortAttachedAggID.


Key properties
^^^^^^^^^^^^^^

| :ref:`CreationClassName <CIM-ServiceAccessPoint-CreationClassName>`
| :ref:`SystemName <CIM-ServiceAccessPoint-SystemName>`
| :ref:`Name <CIM-ServiceAccessPoint-Name>`
| :ref:`SystemCreationClassName <CIM-ServiceAccessPoint-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

*None*

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
| ``string`` :ref:`ActorSystemID <CIM-LAGPort8023ad-ActorSystemID>`
| ``string`` :ref:`SystemName <CIM-ServiceAccessPoint-SystemName>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-ProtocolEndpoint-TimeOfLastStateChange>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ProtocolEndpoint-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`NameFormat <CIM-ProtocolEndpoint-NameFormat>`
| ``uint16`` :ref:`ActorPort <CIM-LAGPort8023ad-ActorPort>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``uint16`` :ref:`ActorPortPriority <CIM-LAGPort8023ad-ActorPortPriority>`
| ``string`` :ref:`Name <CIM-ProtocolEndpoint-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`ProtocolIFType <CIM-ProtocolEndpoint-ProtocolIFType>`
| ``uint16[]`` :ref:`ActorAdminState <CIM-LAGPort8023ad-ActorAdminState>`
| ``uint16`` :ref:`EnabledState <CIM-ProtocolEndpoint-EnabledState>`
| ``uint16`` :ref:`ActorSystemPriority <CIM-LAGPort8023ad-ActorSystemPriority>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``boolean`` :ref:`RepresentsAggregate <CIM-LAGPort8023ad-RepresentsAggregate>`
| ``string`` :ref:`OtherTypeDescription <CIM-ProtocolEndpoint-OtherTypeDescription>`
| ``uint32`` :ref:`SelectedAggID <CIM-LAGPort8023ad-SelectedAggID>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``boolean`` :ref:`BroadcastResetSupported <CIM-ProtocolEndpoint-BroadcastResetSupported>`
| ``uint16`` :ref:`ProtocolType <CIM-ProtocolEndpoint-ProtocolType>`
| ``uint16`` :ref:`ActorOperKey <CIM-LAGPort8023ad-ActorOperKey>`
| ``uint16[]`` :ref:`ActorOperState <CIM-LAGPort8023ad-ActorOperState>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ProtocolEndpoint-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`CreationClassName <CIM-ServiceAccessPoint-CreationClassName>`
| ``string`` :ref:`SystemCreationClassName <CIM-ServiceAccessPoint-SystemCreationClassName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`BroadcastReset <CIM-ProtocolEndpoint-BroadcastReset>`
| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`

