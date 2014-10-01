.. _LMI-DHCPSettingData:

LMI_DHCPSettingData
-------------------

Class reference
===============
Subclass of :ref:`CIM_DHCPSettingData <CIM-DHCPSettingData>`

This class represents the desired configuration settings for the DHCPProtocolEndpoint (i.e. DHCP client configuration.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-DHCPSettingData-AddressOrigin:

``uint16`` **AddressOrigin**

    AddressOrigin identifies the method by which the IP Address, Subnet Mask, and Gateway were assigned to the IPProtocolEndpoint. 

    A value of 4 ``DHCP`` indicates that the values will be assigned via DHCP. See RFC 2131 and related. 

    A value of 7 ``DHCPv6`` shall indicate the values will be assigned using DHCPv6. See RFC 3315.

    
    ======== ======
    ValueMap Values
    ======== ======
    4        DHCP  
    7        DHCPv6
    ======== ======
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint32`` :ref:`RequestedLeaseTime <CIM-DHCPSettingData-RequestedLeaseTime>`
| ``string`` :ref:`InstanceID <CIM-SettingData-InstanceID>`
| ``uint16[]`` :ref:`IPv6RequestedOptions <CIM-DHCPSettingData-IPv6RequestedOptions>`
| ``uint16[]`` :ref:`RequiredOptions <CIM-DHCPSettingData-RequiredOptions>`
| ``uint16[]`` :ref:`IPv6RequiredOptions <CIM-DHCPSettingData-IPv6RequiredOptions>`
| ``string`` :ref:`RequestedIPv6Address <CIM-DHCPSettingData-RequestedIPv6Address>`
| ``string`` :ref:`VendorClassIdentifier <CIM-DHCPSettingData-VendorClassIdentifier>`
| ``string`` :ref:`OtherAddressPrefixOriginDescription <CIM-IPAssignmentSettingData-OtherAddressPrefixOriginDescription>`
| ``string`` :ref:`ConfigurationName <CIM-SettingData-ConfigurationName>`
| ``string`` :ref:`SoOrgID <CIM-SettingData-SoOrgID>`
| ``uint16[]`` :ref:`RequestedOptions <CIM-DHCPSettingData-RequestedOptions>`
| ``string`` :ref:`OtherAddressSuffixOriginDescription <CIM-IPAssignmentSettingData-OtherAddressSuffixOriginDescription>`
| ``uint16`` :ref:`ProtocolIFType <CIM-IPAssignmentSettingData-ProtocolIFType>`
| ``string`` :ref:`ElementName <CIM-SettingData-ElementName>`
| ``uint16`` :ref:`AddressPrefixOrigin <CIM-IPAssignmentSettingData-AddressPrefixOrigin>`
| ``uint16`` :ref:`AddressSuffixOrigin <CIM-IPAssignmentSettingData-AddressSuffixOrigin>`
| ``string`` :ref:`ClientIdentifier <CIM-DHCPSettingData-ClientIdentifier>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`SoID <CIM-SettingData-SoID>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16`` :ref:`ChangeableType <CIM-SettingData-ChangeableType>`
| ``string`` :ref:`RequestedIPv4Address <CIM-DHCPSettingData-RequestedIPv4Address>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string[]`` :ref:`ComponentSetting <CIM-SettingData-ComponentSetting>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

