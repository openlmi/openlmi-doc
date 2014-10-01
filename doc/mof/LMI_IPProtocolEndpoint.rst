.. _LMI-IPProtocolEndpoint:

LMI_IPProtocolEndpoint
----------------------

Class reference
===============
Subclass of :ref:`CIM_IPProtocolEndpoint <CIM-IPProtocolEndpoint>`

Instance of LMI_IPProtocolEndpoint represents one IP address.


Key properties
^^^^^^^^^^^^^^

| :ref:`CreationClassName <CIM-ServiceAccessPoint-CreationClassName>`
| :ref:`SystemName <CIM-ServiceAccessPoint-SystemName>`
| :ref:`Name <CIM-ServiceAccessPoint-Name>`
| :ref:`SystemCreationClassName <CIM-ServiceAccessPoint-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-IPProtocolEndpoint-IPv6Address:

``string`` **IPv6Address**

    The IPv6 address that this ProtocolEndpoint represents.

    
.. _LMI-IPProtocolEndpoint-SubnetMask:

``string`` **SubnetMask**

    The mask for the IPv4 address of this ProtocolEndpoint, if one is defined.

    
.. _LMI-IPProtocolEndpoint-ProtocolIFType:

``uint16`` **ProtocolIFType**

    This property explicitly defines support for different versions of the IP protocol.

    
    ======== ======
    ValueMap Values
    ======== ======
    4096     IPv4  
    4097     IPv6  
    ======== ======
    
.. _LMI-IPProtocolEndpoint-IPv4Address:

``string`` **IPv4Address**

    The IPv4 address that this ProtocolEndpoint represents.

    
.. _LMI-IPProtocolEndpoint-PrefixLength:

``uint8`` **PrefixLength**

    The prefix length for the IPv6 address of this Protocol Endpoint, if one is defined.

    

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
| ``uint16`` :ref:`AddressType <CIM-IPProtocolEndpoint-AddressType>`
| ``string`` :ref:`OtherAddressPrefixOriginDescription <CIM-IPProtocolEndpoint-OtherAddressPrefixOriginDescription>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`NameFormat <CIM-ProtocolEndpoint-NameFormat>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``string`` :ref:`Address <CIM-IPProtocolEndpoint-Address>`
| ``uint16`` :ref:`IPv6AddressType <CIM-IPProtocolEndpoint-IPv6AddressType>`
| ``uint16`` :ref:`EnabledState <CIM-ProtocolEndpoint-EnabledState>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`OtherAddressSuffixOriginDescription <CIM-IPProtocolEndpoint-OtherAddressSuffixOriginDescription>`
| ``string`` :ref:`Name <CIM-ProtocolEndpoint-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`IPv6SubnetPrefixLength <CIM-IPProtocolEndpoint-IPv6SubnetPrefixLength>`
| ``uint16`` :ref:`AddressPrefixOrigin <CIM-IPProtocolEndpoint-AddressPrefixOrigin>`
| ``string`` :ref:`OtherTypeDescription <CIM-ProtocolEndpoint-OtherTypeDescription>`
| ``uint16`` :ref:`AddressSuffixOrigin <CIM-IPProtocolEndpoint-AddressSuffixOrigin>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``string`` :ref:`Description <CIM-ProtocolEndpoint-Description>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``boolean`` :ref:`BroadcastResetSupported <CIM-ProtocolEndpoint-BroadcastResetSupported>`
| ``uint16`` :ref:`ProtocolType <CIM-ProtocolEndpoint-ProtocolType>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16`` :ref:`IPVersionSupport <CIM-IPProtocolEndpoint-IPVersionSupport>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ProtocolEndpoint-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`CreationClassName <CIM-ServiceAccessPoint-CreationClassName>`
| ``uint16`` :ref:`AddressOrigin <CIM-IPProtocolEndpoint-AddressOrigin>`
| ``string`` :ref:`SystemCreationClassName <CIM-ServiceAccessPoint-SystemCreationClassName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`BroadcastReset <CIM-ProtocolEndpoint-BroadcastReset>`
| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`

