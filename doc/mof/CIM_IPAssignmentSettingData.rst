.. _CIM-IPAssignmentSettingData:

CIM_IPAssignmentSettingData
---------------------------

Class reference
===============
Subclass of :ref:`CIM_SettingData <CIM-SettingData>`

This class and its sub-classes represents Internet Protocol (IP) related settings. When used as an accumulation of settings (AddressOrigin set to 11 "cumulative configuration"), this SettingData instance is the aggregation point identifying an IP configuration. Multiple IP configurations could exist for a target. Each configuration is represented with an instance of IPAssignmentSettingData. The details of the IP configuration are defined by instances of sub-classes of this class (i.e. StaticIPAssignmentSettingData, DHCPSettingData, DNSSettingData). These instances are associated with the IPAssignmentSettingData instance using the OrderedComponent or ConcreteComponent associations. For example, a static IP configuration would be represented by an instance of IPAssignmentSettingData and an instance of StaticIPAssignmentSettingData associated via an instance of ConcreteComponent. A static IP configuration including DNS would be modeled using an instance of IPAssignmentSettingData, DNSSettingData, and StaticIPAssignmentSettingData. The DNSSettingData and StaticIPAssignmentSettingData instance would be associated with the IPAssignmentSettingData using instances of ConcreteComponent.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-IPAssignmentSettingData-OtherAddressSuffixOriginDescription:

``string`` **OtherAddressSuffixOriginDescription**

    Description of the AddressSuffixOrigin when the AddressSuffixOrigin property has a value of "other".

    
.. _CIM-IPAssignmentSettingData-OtherAddressPrefixOriginDescription:

``string`` **OtherAddressPrefixOriginDescription**

    Description of the AddressPrefixOrigin when the AddressPrefixOrigin property has a value of "other".

    
.. _CIM-IPAssignmentSettingData-ProtocolIFType:

``uint16`` **ProtocolIFType**

    An enumeration that describes the IP version.

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    0        Unknown        
    ..       DMTF Reserved  
    4096     IPv4           
    4097     IPv6           
    32768..  Vendor Reserved
    ======== ===============
    
.. _CIM-IPAssignmentSettingData-AddressPrefixOrigin:

``uint16`` **AddressPrefixOrigin**

    An enumeration of subnet prefix origin for the IP Address assigned by this setting instance. Refer IpAddressPrefixOriginTC from RFC 4293.

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
    
.. _CIM-IPAssignmentSettingData-AddressSuffixOrigin:

``uint16`` **AddressSuffixOrigin**

    An enumeration of suffix origin for the IP Address assigned by this setting instance. Refer IpAddressOriginTC from RFC 4293.

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
    
.. _CIM-IPAssignmentSettingData-AddressOrigin:

``uint16`` **AddressOrigin**

    AddressOrigin identifies the method by which the IP Address, Subnet Mask for IPv4 or Prefix Length for IPv6, and Gateway shall be assigned to the IPProtocolEndpoint. 

    A value of 3 "Static" shall indicate the values will be assigned manually. 

    A value of 4 "DHCP" shall indicate the values will be assigned utilizing the Dynamic Host Configuration Protocol. See RFC 2131 and related. 

    A value of 5 "BOOTP" shall indicate the values will be assigned utilizing BOOTP. See RFC 951 and related. 

    A value of 6 "IPv4 Link Local" shall indicate the values will be assigned using the IPv4 Link Local protocol. See RFC 3927.

    A value of 7 "DHCPv6" shall indicate the values will be assigned using DHCPv6. See RFC 3315. 

    A value of 8 "IPv6 AutoConfig " shall indicate the values will be assigned using the IPv6 AutoConfig. See RFC 4862. 

    A value of 9 "Stateless" shall indicate Stateless will be assigned. 

    A value of 10 "Link Local" shall indicate Link Local values will be assigned.

    A value of 11 "cumulative configuration" shall indicate an accumulation of settings is used. This instance of CIM_IPAssignmentSettingData should be associated with other instances of CIM_IPAssignmentSettingData or its subclasses to represent the detailed IP settings.

    
    ======== ========================
    ValueMap Values                  
    ======== ========================
    0        Unknown                 
    1        Other                   
    2        Not Applicable          
    3        Static                  
    4        DHCP                    
    5        BOOTP                   
    6        IPv4 Link Local         
    7        DHCPv6                  
    8        IPv6AutoConfig          
    9        Stateless               
    10       Link Local              
    11       cumulative configuration
    ..       DMTF Reserved           
    32768..  Vendor Reserved         
    ======== ========================
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`SoOrgID <CIM-SettingData-SoOrgID>`
| ``string`` :ref:`SoID <CIM-SettingData-SoID>`
| ``string`` :ref:`ElementName <CIM-SettingData-ElementName>`
| ``uint16`` :ref:`ChangeableType <CIM-SettingData-ChangeableType>`
| ``string`` :ref:`InstanceID <CIM-SettingData-InstanceID>`
| ``string[]`` :ref:`ComponentSetting <CIM-SettingData-ComponentSetting>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`ConfigurationName <CIM-SettingData-ConfigurationName>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

