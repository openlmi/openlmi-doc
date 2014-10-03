.. _CIM-IPProtocolEndpoint:

CIM_IPProtocolEndpoint
----------------------

Class reference
===============
Subclass of :ref:`CIM_ProtocolEndpoint <CIM-ProtocolEndpoint>`

A ProtocolEndpoint that is dedicated to running IP.


Key properties
^^^^^^^^^^^^^^

| :ref:`CreationClassName <CIM-ServiceAccessPoint-CreationClassName>`
| :ref:`SystemName <CIM-ServiceAccessPoint-SystemName>`
| :ref:`Name <CIM-ServiceAccessPoint-Name>`
| :ref:`SystemCreationClassName <CIM-ServiceAccessPoint-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-IPProtocolEndpoint-AddressType:

``uint16`` **AddressType**

    An enumeration that describes the format of the Address property. It is deprecated since it is not needed, as the class contains both IPv4 and v6 addresses).

    
    ======== =======
    ValueMap Values 
    ======== =======
    0        Unknown
    1        IPv4   
    2        IPv6   
    ======== =======
    
.. _CIM-IPProtocolEndpoint-OtherAddressPrefixOriginDescription:

``string`` **OtherAddressPrefixOriginDescription**

    Description of the AddressPrefixOrigin when the AddressPrefixOrigin property has a value of "other"

    
.. _CIM-IPProtocolEndpoint-IPv6Address:

``string`` **IPv6Address**

    The IPv6 address that this ProtocolEndpoint represents.

    
.. _CIM-IPProtocolEndpoint-Address:

``string`` **Address**

    The IP address that this ProtocolEndpoint represents, formatted according to the appropriate convention as defined in the AddressType property of this class (e.g., 171.79.6.40). This single property is deprecated to replace it by specific IPv4 and v6 addresses.

    
.. _CIM-IPProtocolEndpoint-SubnetMask:

``string`` **SubnetMask**

    The mask for the IPv4 address of this ProtocolEndpoint, if one is defined.

    
.. _CIM-IPProtocolEndpoint-IPv6AddressType:

``uint16`` **IPv6AddressType**

    IPv6AddressType indentified the type of address found in the IPv6Address property. The values of this property shall be interpreted according to RFC4291, Section 2.4

    
    ============ =====================
    ValueMap     Values               
    ============ =====================
    2            Unspecified          
    3            Loopback             
    4            Multicast            
    5            Link Local Unicast   
    6            Global Unicast       
    7            Embedded IPv4 Address
    8            Site Local Unicast   
    ..           DMTF Reserved        
    32768..65535 Vendor Reserved      
    ============ =====================
    
.. _CIM-IPProtocolEndpoint-OtherAddressSuffixOriginDescription:

``string`` **OtherAddressSuffixOriginDescription**

    Description of the AddressSuffixOrigin when the AddressSuffixOrigin property has a value of "other".

    
.. _CIM-IPProtocolEndpoint-ProtocolIFType:

``uint16`` **ProtocolIFType**

    ProtocolIFType's enumeration is limited to IP-related and reserved values for this subclass of ProtocolEndpoint.

    
    =========== ===============
    ValueMap    Values         
    =========== ===============
    1           Other          
    225..4095   IANA Reserved  
    4096        IPv4           
    4097        IPv6           
    4098        IPv4/v6        
    4301..32767 DMTF Reserved  
    32768..     Vendor Reserved
    =========== ===============
    
.. _CIM-IPProtocolEndpoint-IPv6SubnetPrefixLength:

``uint16`` **IPv6SubnetPrefixLength**

    IPv6SubnetPrefixLength is used to identify the prefix length of the IPv6Address property that is used to specify a subnet

    
.. _CIM-IPProtocolEndpoint-AddressPrefixOrigin:

``uint16`` **AddressPrefixOrigin**

    An enumeration of subnet prefix origin for the IP Address. Refer IpAddressPrefixOriginTC from RFC 4293.

    A value of 1 "other" indicate none of the other values is applicable.

    A value of 2 "manual" indicate that the prefix is manually assigned.

    A value of 3 "wellknown" indicate that prefix is a well known prefix.

    A value of 4 "dhcp" indicate that prefix is from dhcp.

    A value of 5 "routeradv" indicate that prefix is from router advertisement.

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    1        other          
    2        manual         
    3        wellknown      
    4        dhcp           
    5        routeradv      
    ..       DMTF Reserved  
    32768..  Vendor Reserved
    ======== ===============
    
.. _CIM-IPProtocolEndpoint-AddressSuffixOrigin:

``uint16`` **AddressSuffixOrigin**

    An enumeration of suffix origin for the IP Address. Refer IpAddressOriginTC from RFC 4293.

    A value of 1 "other" indicate none of the other values is applicable.

    A value of 2 "manual" indicate that the suffix is manually assigned.

    A value of 3 "wellknown" indicate that suffix is a well known suffix.

    A value of 4 "dhcp" indicate that suffix is from dhcp.

    A value of 5 "linklayer" indicate that suffix is from IPv6 stateless auto-configuration.

    A value of 6 "random" indicate that suffix is chosen randomly.

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    1        other          
    2        manual         
    3        wellknown      
    4        dhcp           
    5        linklayer      
    6        random         
    ..       DMTF Reserved  
    32768..  Vendor Reserved
    ======== ===============
    
.. _CIM-IPProtocolEndpoint-IPv4Address:

``string`` **IPv4Address**

    The IPv4 address that this ProtocolEndpoint represents.

    
.. _CIM-IPProtocolEndpoint-IPVersionSupport:

``uint16`` **IPVersionSupport**

    This property explicitly defines support for different versions of the IP protocol, for this Endpoint. It is deprecated since the ProtocolIFType also provides this functionality by describing an endpoint as IPv4 only (value=4096), IPv6 only (value=4097), or IPv4/v6 (value=4098).

    
    ======== ==================
    ValueMap Values            
    ======== ==================
    0        Unknown           
    1        IPv4 Only         
    2        IPv6 Only         
    3        Both IPv4 and IPv6
    ======== ==================
    
.. _CIM-IPProtocolEndpoint-AddressOrigin:

``uint16`` **AddressOrigin**

    AddressOrigin identifies the method by which the IP Address, Subnet Mask, and Gateway were assigned to the IPProtocolEndpoint.A value of 3 "Static" shall indicate the values were assigned manually. A value of 4 "DHCP" shall indicate the values were assigned utilizing the Dynamic Host Configuration Protocol. See RFC 2131 and related. 

    A value of 5 "BOOTP" shall indicate the values were assigned utilizing BOOTP. See RFC 951 and related. 

    A value of 6 "IPv4 Link Local" shall indicate the values were assigned using the IPv4 Link Local protocol. See RFC 3927.

    A value of 7 "DHCPv6" shall indicate the values were assigned using DHCPv6. See RFC 3315. 

    A value of 8 "IPv6 AutoConfig" shall indicate the values were assinged using the IPv6 AutoConfig Protocol. See RFC 4862. 

    A value of 9 "Stateless" shall indicate Stateless values were assigned. 

    A value of 10 "Link Local" shall indicate Link Local values were assigned.

    
    ============ ===============
    ValueMap     Values         
    ============ ===============
    0            Unknown        
    1            Other          
    2            Not Applicable 
    3            Static         
    4            DHCP           
    5            BOOTP          
    6            IPv4 Link Local
    7            DHCPv6         
    8            IPv6AutoConfig 
    9            Stateless      
    10           Link Local     
    ..           DMTF Reserved  
    32768..65535 Vendor Reserved
    ============ ===============
    
.. _CIM-IPProtocolEndpoint-PrefixLength:

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
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`NameFormat <CIM-ProtocolEndpoint-NameFormat>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`EnabledState <CIM-ProtocolEndpoint-EnabledState>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`Name <CIM-ProtocolEndpoint-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``string`` :ref:`OtherTypeDescription <CIM-ProtocolEndpoint-OtherTypeDescription>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``string`` :ref:`Description <CIM-ProtocolEndpoint-Description>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
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

