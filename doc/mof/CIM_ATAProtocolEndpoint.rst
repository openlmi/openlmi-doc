.. _CIM-ATAProtocolEndpoint:

CIM_ATAProtocolEndpoint
-----------------------

Class reference
===============
Subclass of :ref:`CIM_ProtocolEndpoint <CIM-ProtocolEndpoint>`

An ATAProtocolEndpoint represents the protocol (command) aspects of a logical ATA port, independent of the connection/transport. ATAProtocolEndpoint is either directly or indirectly associated to one or more instances of LogicalPort depending on the underlying transport.


Key properties
^^^^^^^^^^^^^^

| :ref:`CreationClassName <CIM-ServiceAccessPoint-CreationClassName>`
| :ref:`SystemName <CIM-ServiceAccessPoint-SystemName>`
| :ref:`Name <CIM-ServiceAccessPoint-Name>`
| :ref:`SystemCreationClassName <CIM-ServiceAccessPoint-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-ATAProtocolEndpoint-Name:

``string`` **Name**

    The ATA identifier for the target or initiator device, in the format appropriate for the ConnectionType. If a ConnectionType specific subclass is defined, the subclass may override Name to define the format. For other ConnectionTypes, the format (and content) should match that of PermanentAddress of the corresponding port if the port is is subclassed from NetworkPort.

    
.. _CIM-ATAProtocolEndpoint-ConnectionType:

``uint16`` **ConnectionType**

    The supported connection type for this endpoint. The connection type may be needed before the port(s) are associated and also is used in some ATA commands.

    
    ======== ======
    ValueMap Values
    ======== ======
    1        Other 
    2        ATA   
    3        SATA  
    ======== ======
    
.. _CIM-ATAProtocolEndpoint-OtherConnectionType:

``string`` **OtherConnectionType**

    The connection type, if ConnectionType is "Other".

    
.. _CIM-ATAProtocolEndpoint-Role:

``uint16`` **Role**

    This property indicates which role this ProtocolEndpoint implements.

    
    ======== =========================
    ValueMap Values                   
    ======== =========================
    0        Unknown                  
    2        Initiator                
    3        Target                   
    4        Both Initiator and Target
    ======== =========================
    

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
| ``string`` :ref:`NameFormat <CIM-ProtocolEndpoint-NameFormat>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ProtocolEndpoint-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-ProtocolEndpoint-TimeOfLastStateChange>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`ProtocolIFType <CIM-ProtocolEndpoint-ProtocolIFType>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-ProtocolEndpoint-EnabledState>`
| ``string`` :ref:`CreationClassName <CIM-ServiceAccessPoint-CreationClassName>`
| ``string`` :ref:`OtherTypeDescription <CIM-ProtocolEndpoint-OtherTypeDescription>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``boolean`` :ref:`BroadcastResetSupported <CIM-ProtocolEndpoint-BroadcastResetSupported>`
| ``uint16`` :ref:`ProtocolType <CIM-ProtocolEndpoint-ProtocolType>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ProtocolEndpoint-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`SystemCreationClassName <CIM-ServiceAccessPoint-SystemCreationClassName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`BroadcastReset <CIM-ProtocolEndpoint-BroadcastReset>`
| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`

