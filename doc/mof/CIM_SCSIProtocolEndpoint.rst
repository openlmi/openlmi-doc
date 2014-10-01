.. _CIM-SCSIProtocolEndpoint:

CIM_SCSIProtocolEndpoint
------------------------

Class reference
===============
Subclass of :ref:`CIM_ProtocolEndpoint <CIM-ProtocolEndpoint>`

A SCSIProtocolEndpoint represents the protocol (command) aspects of a logical SCSI port, independent of the connection/transport. SCSIProtocolEndpoint is either directly or indirectly associated to one or more instances of LogicalPort (via DeviceSAPImplementation) depending on the underlying transport. Indirect associations aggregate one or more LogicalPorts using intermediate ProtocolEndpoints (iSCSI, etc). SCSIProtocolEndpoint is also associated to a SCSIProtocolController, representing the SCSI device.


Key properties
^^^^^^^^^^^^^^

| :ref:`CreationClassName <CIM-ServiceAccessPoint-CreationClassName>`
| :ref:`SystemName <CIM-ServiceAccessPoint-SystemName>`
| :ref:`Name <CIM-ServiceAccessPoint-Name>`
| :ref:`SystemCreationClassName <CIM-ServiceAccessPoint-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-SCSIProtocolEndpoint-TargetRelativePortNumber:

``uint32`` **TargetRelativePortNumber**

    For ports on a target device, the port number, relative to the storage system. 0 is reserved by T10, 1 is port A, 2 is port B, etc. These numbers are used in SCSI commands that operate on target port groups.

    
.. _CIM-SCSIProtocolEndpoint-Name:

``string`` **Name**

    The SCSI identifier for the target or initiator device, in the format appropriate for the ConnectionType. If a ConnectionType specific subclass is defined, the subclass may override Name to define the format. For other ConnectionTypes, the format (and content) should match that of PermamnentAddress of the corresponding LogicalPort.

    
.. _CIM-SCSIProtocolEndpoint-ConnectionType:

``uint16`` **ConnectionType**

    The supported connection type for this endpoint. The connection type may be needed before the port(s) are associated and also is used in some SCSI commands.

    
    ======== =============
    ValueMap Values       
    ======== =============
    1        Other        
    2        Fibre Channel
    3        Parallel SCSI
    4        SSA          
    5        IEEE 1394    
    6        RDMA         
    7        iSCSI        
    8        SAS          
    9        ADT          
    ======== =============
    
.. _CIM-SCSIProtocolEndpoint-OtherConnectionType:

``string`` **OtherConnectionType**

    The connection type, if ConnectionType is "Other".

    
.. _CIM-SCSIProtocolEndpoint-Role:

``uint16`` **Role**

    For iSCSI, each SCSIProtocolEndpoint MUST act as either a target or an initiator endpoint. Other transports allow a SCSI PE to act as both an initiator and target endpoint. This property indicates which role this ProtocolEndpoint implements.

    
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

