.. _LMI-DNSSettingData:

LMI_DNSSettingData
------------------

Class reference
===============
Subclass of :ref:`CIM_DNSSettingData <CIM-DNSSettingData>`

DNSSettingData defines the DNSconfiguration settings for a single IP network connection. With the exception of the the DNSServerAddresses and the hostname in use, the configuration of a DNSProtocolEndpoint is indicated by the properties of an associated instance of DNSSettingData.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-DNSSettingData-ProtocolIFType:

``uint16`` **ProtocolIFType**

    An enumeration that describes the IP version.

    
    ======== ======
    ValueMap Values
    ======== ======
    4096     IPv4  
    4097     IPv6  
    ======== ======
    
.. _LMI-DNSSettingData-DNSServerAddresses:

``string[]`` **DNSServerAddresses**

    The DNS servers to contact. The array ordering correlates to the order in which the DNS servers will be contacted. If using DHCP, DNS servers obtained from DHCP will be prepended to this array.

    The RemoteServiceAccessPoints associated with the DNSProtocolEndpoint with the value of the AccessContext property being ``DNS Server`` represent the actual DNS Servers being utilized by the DNS client.

    
.. _LMI-DNSSettingData-DNSSearchDomains:

``string[]`` **DNSSearchDomains**

    The DNS search domains. The array ordering correlates to the order in which the search domains will be used. If using DHCP, DNS search domains obtained from DHCP will be prepended to this array.

    

    
.. _LMI-DNSSettingData-AddressOrigin:

``uint16`` **AddressOrigin**

    AddressOrigin identifies the method by which the IP Address, Subnet Mask, and Gateway were assigned to the IPProtocolEndpoint. This is independent of the DNS configuration, thus this property has the value of 2 (``Not Applicable``).

    
    ======== ==============
    ValueMap Values        
    ======== ==============
    2        Not Applicable
    ======== ==============
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`DomainName <CIM-DNSSettingData-DomainName>`
| ``string`` :ref:`InstanceID <CIM-SettingData-InstanceID>`
| ``string`` :ref:`ElementName <CIM-SettingData-ElementName>`
| ``string`` :ref:`OtherAddressPrefixOriginDescription <CIM-IPAssignmentSettingData-OtherAddressPrefixOriginDescription>`
| ``string`` :ref:`ConfigurationName <CIM-SettingData-ConfigurationName>`
| ``boolean`` :ref:`RegisterThisConnectionsAddress <CIM-DNSSettingData-RegisterThisConnectionsAddress>`
| ``string`` :ref:`SoOrgID <CIM-SettingData-SoOrgID>`
| ``uint16[]`` :ref:`DHCPOptionsToUse <CIM-DNSSettingData-DHCPOptionsToUse>`
| ``string`` :ref:`OtherAddressSuffixOriginDescription <CIM-IPAssignmentSettingData-OtherAddressSuffixOriginDescription>`
| ``uint16`` :ref:`AddressPrefixOrigin <CIM-IPAssignmentSettingData-AddressPrefixOrigin>`
| ``uint16`` :ref:`AddressSuffixOrigin <CIM-IPAssignmentSettingData-AddressSuffixOrigin>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`SoID <CIM-SettingData-SoID>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16`` :ref:`ChangeableType <CIM-SettingData-ChangeableType>`
| ``string[]`` :ref:`ComponentSetting <CIM-SettingData-ComponentSetting>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`RequestedHostname <CIM-DNSSettingData-RequestedHostname>`
| ``boolean`` :ref:`UseSuffixWhenRegistering <CIM-DNSSettingData-UseSuffixWhenRegistering>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

