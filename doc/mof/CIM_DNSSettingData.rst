.. _CIM-DNSSettingData:

CIM_DNSSettingData
------------------

Class reference
===============
Subclass of :ref:`CIM_IPAssignmentSettingData <CIM-IPAssignmentSettingData>`

DNSSettingData defines the DNSconfiguration settings for a single IP network connection. With the exception of the the DNSServerAddresses and the hostname in use, the configuration of a DNSProtocolEndpoint is indicated by the properties of an associated instance of DNSSettingData.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-DNSSettingData-DomainName:

``string`` **DomainName**

    The domain to use for this client connection.

    
.. _CIM-DNSSettingData-RegisterThisConnectionsAddress:

``boolean`` **RegisterThisConnectionsAddress**

    Whether or not this connection's address should be registered in DNS.

    
.. _CIM-DNSSettingData-DHCPOptionsToUse:

``uint16[]`` **DHCPOptionsToUse**

    One or more DHCP options that the DNS client should utilise if they are returned during a DHCP bind operation.

    
    ============ ==================
    ValueMap     Values            
    ============ ==================
    8            Domain Name Server
    14           Host Name         
    17           Domain Name       
    18..32767    DMTF Reserved     
    32768..65535 Vendor Reserved   
    ============ ==================
    
.. _CIM-DNSSettingData-DNSServerAddresses:

``string[]`` **DNSServerAddresses**

    The DNS servers to contact. The array ordering correlates to the order in which the DNS servers will be contacted. The RemoteServiceAccessPoints associated with the DNSProtocolEndpoint with the value of the AccessContext property being "DNS Server" represent the actual DNS Servers being utilized by the DNS client.

    
.. _CIM-DNSSettingData-UseSuffixWhenRegistering:

``boolean`` **UseSuffixWhenRegistering**

    Whether or not the suffix should be appended before registering the client name with the DNS server.

    
.. _CIM-DNSSettingData-RequestedHostname:

``string`` **RequestedHostname**

    The Hostname requested for this client connection.

    
.. _CIM-DNSSettingData-AddressOrigin:

``uint16`` **AddressOrigin**

    AddressOrigin identifies the method by which the IP Address, Subnet Mask, and Gateway were assigned to the IPProtocolEndpoint. This is independent of the DNS configuration, thus this property has the value of 2 ("Not Applicable")

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    0..1     DMTF Reserved  
    2        Not Applicable 
    3..32767 DMTF Reserved  
    32768..  Vendor Reserved
    ======== ===============
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`InstanceID <CIM-SettingData-InstanceID>`
| ``string`` :ref:`ElementName <CIM-SettingData-ElementName>`
| ``string`` :ref:`OtherAddressPrefixOriginDescription <CIM-IPAssignmentSettingData-OtherAddressPrefixOriginDescription>`
| ``string`` :ref:`ConfigurationName <CIM-SettingData-ConfigurationName>`
| ``string`` :ref:`SoOrgID <CIM-SettingData-SoOrgID>`
| ``string`` :ref:`OtherAddressSuffixOriginDescription <CIM-IPAssignmentSettingData-OtherAddressSuffixOriginDescription>`
| ``uint16`` :ref:`ProtocolIFType <CIM-IPAssignmentSettingData-ProtocolIFType>`
| ``uint16`` :ref:`AddressPrefixOrigin <CIM-IPAssignmentSettingData-AddressPrefixOrigin>`
| ``uint16`` :ref:`AddressSuffixOrigin <CIM-IPAssignmentSettingData-AddressSuffixOrigin>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`SoID <CIM-SettingData-SoID>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16`` :ref:`ChangeableType <CIM-SettingData-ChangeableType>`
| ``string[]`` :ref:`ComponentSetting <CIM-SettingData-ComponentSetting>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

