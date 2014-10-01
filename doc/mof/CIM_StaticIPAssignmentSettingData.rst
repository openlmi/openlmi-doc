.. _CIM-StaticIPAssignmentSettingData:

CIM_StaticIPAssignmentSettingData
---------------------------------

Class reference
===============
Subclass of :ref:`CIM_IPAssignmentSettingData <CIM-IPAssignmentSettingData>`

CIM_StaticIPAssignmentSettingData defines a basic IP configuration which could be statically assigned to an IPProtocolEndpoint. This class defines a partial configuration. Instances are aggregated into an instance of IPAssignmentSettingData which defines a full configuration.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-StaticIPAssignmentSettingData-IPv6Address:

``string`` **IPv6Address**

    The IPv6 address that this ProtocolEndpoint represents.

    
.. _CIM-StaticIPAssignmentSettingData-SubnetMask:

``string`` **SubnetMask**

    The subnet mask for the IPv4 address of this ProtocolEndpoint, if one is defined.

    
.. _CIM-StaticIPAssignmentSettingData-IPv6AddressType:

``uint16`` **IPv6AddressType**

    IPv6AddressType identifies the type of address found in the IPv6Address property of this class. The values of this property shall be interpreted according to RFC4291, Section 2.4

    
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
    
.. _CIM-StaticIPAssignmentSettingData-GatewayIPv4Address:

``string`` **GatewayIPv4Address**

    The IP v4 address of the default gateway.

    
.. _CIM-StaticIPAssignmentSettingData-GatewayIPv6Address:

``string`` **GatewayIPv6Address**

    GatewayIPv6Address is used to identify the IPv6 address of the Gateway

    
.. _CIM-StaticIPAssignmentSettingData-IPv6SubnetPrefixLength:

``uint16`` **IPv6SubnetPrefixLength**

    IPv6SubnetPrefixLength is used to identify the prefix length of the IPv6Address property that is used to specify a subnet

    
.. _CIM-StaticIPAssignmentSettingData-IPv4Address:

``string`` **IPv4Address**

    The IPv4 address that will be assigned to the ProtocolEndpoint.

    
.. _CIM-StaticIPAssignmentSettingData-AddressOrigin:

``uint16`` **AddressOrigin**

    AddressOrigin identifies the method by which the IP Address, Subnet Mask, and Gateway were assigned to the IPProtocolEndpoint. A value of 2 indicates that the application of the IPAssignmentSettingData instance does not affect these properties.

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    0..2     DMTF Reserved  
    3        Static         
    4..32767 DMTF Reserved  
    32768..  Vendor Reserved
    ======== ===============
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`AddressPrefixOrigin <CIM-IPAssignmentSettingData-AddressPrefixOrigin>`
| ``string`` :ref:`InstanceID <CIM-SettingData-InstanceID>`
| ``string`` :ref:`ElementName <CIM-SettingData-ElementName>`
| ``string`` :ref:`OtherAddressPrefixOriginDescription <CIM-IPAssignmentSettingData-OtherAddressPrefixOriginDescription>`
| ``string`` :ref:`ConfigurationName <CIM-SettingData-ConfigurationName>`
| ``string`` :ref:`SoOrgID <CIM-SettingData-SoOrgID>`
| ``string`` :ref:`OtherAddressSuffixOriginDescription <CIM-IPAssignmentSettingData-OtherAddressSuffixOriginDescription>`
| ``uint16`` :ref:`ProtocolIFType <CIM-IPAssignmentSettingData-ProtocolIFType>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16`` :ref:`AddressSuffixOrigin <CIM-IPAssignmentSettingData-AddressSuffixOrigin>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`SoID <CIM-SettingData-SoID>`
| ``uint16`` :ref:`ChangeableType <CIM-SettingData-ChangeableType>`
| ``string[]`` :ref:`ComponentSetting <CIM-SettingData-ComponentSetting>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

