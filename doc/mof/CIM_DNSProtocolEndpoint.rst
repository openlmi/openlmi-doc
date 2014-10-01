.. _CIM-DNSProtocolEndpoint:

CIM_DNSProtocolEndpoint
-----------------------

Class reference
===============
Subclass of :ref:`CIM_ProtocolEndpoint <CIM-ProtocolEndpoint>`

A class derived from CIM_ProtocolEndpoint which represents the DNS client and DNS configuration for a single IP endpoint. The DNS server addresses can be determined by querying the AccessInfo property of associated CIM_RemoteServiceAccessPoint instances which have an AccessContext of "DNS Server". The order in which the DNS servers will be queried can be determined by the relative values of the OrderOfAccess property on each CIM_RemoteAccessAvailableToElement association which associated the CIM_RemoteServiceAccessPoint with the CIM_DNSProtocolEndpoint.


Key properties
^^^^^^^^^^^^^^

| :ref:`CreationClassName <CIM-ServiceAccessPoint-CreationClassName>`
| :ref:`SystemName <CIM-ServiceAccessPoint-SystemName>`
| :ref:`Name <CIM-ServiceAccessPoint-Name>`
| :ref:`SystemCreationClassName <CIM-ServiceAccessPoint-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-DNSProtocolEndpoint-AppendParentSuffixes:

``boolean`` **AppendParentSuffixes**

    Whether or not the client appends the parent domain suffix to target names prior to attempting to resolve.

    
.. _CIM-DNSProtocolEndpoint-DomainName:

``string`` **DomainName**

    The domain to use for this client connection.

    
.. _CIM-DNSProtocolEndpoint-Hostname:

``string`` **Hostname**

    The Hostname actually in use for this client connection.

    
.. _CIM-DNSProtocolEndpoint-RegisterThisConnectionsAddress:

``boolean`` **RegisterThisConnectionsAddress**

    Whether or not the client attempted to register this connection's address in DNS.

    
.. _CIM-DNSProtocolEndpoint-DHCPOptionsToUse:

``uint16[]`` **DHCPOptionsToUse**

    One or more DHCP options that the DNS client is utilizing if they were returned during a DHCP bind operation.

    
    ============ ==================
    ValueMap     Values            
    ============ ==================
    8            Domain Name Server
    14           Host Name         
    17           Domain Name       
    18..32767    DMTF Reserved     
    32768..65535 Vendor Reserved   
    ============ ==================
    
.. _CIM-DNSProtocolEndpoint-AppendPrimarySuffixes:

``boolean`` **AppendPrimarySuffixes**

    Whether or not the client appends the primary domain suffix to target names prior to attempting to resolve.

    
.. _CIM-DNSProtocolEndpoint-DNSSuffixesToAppend:

``string[]`` **DNSSuffixesToAppend**

    The DNS suffixes to append when attempting to resolve a hostname.

    
.. _CIM-DNSProtocolEndpoint-UseSuffixWhenRegistering:

``boolean`` **UseSuffixWhenRegistering**

    Whether or not the suffix is appended before registering the client name with the DNS server.

    

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
| ``uint16`` :ref:`ProtocolIFType <CIM-ProtocolEndpoint-ProtocolIFType>`
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

