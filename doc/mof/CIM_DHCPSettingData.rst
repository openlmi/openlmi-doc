.. _CIM-DHCPSettingData:

CIM_DHCPSettingData
-------------------

Class reference
===============
Subclass of :ref:`CIM_IPAssignmentSettingData <CIM-IPAssignmentSettingData>`

This class represents the desired configuration settings for the DHCPProtocolEndpoint (i.e. DHCP client configuration.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-DHCPSettingData-RequestedLeaseTime:

``uint32`` **RequestedLeaseTime**

    This property is used in a client request (DHCPREQUEST) to allow the client to request a lease time for the IP address. The value shall be specified as an interval at a granularity of seconds. This value corresponds to the value for code 51 as defined in RFC2132.

    
.. _CIM-DHCPSettingData-IPv6RequestedOptions:

``uint16[]`` **IPv6RequestedOptions**

    The list of requested DHCP options which the client is capable of interpreting but not necessarily required for the client to operate properly. This list of DHCP options is for IPv6. The values of this property shall be the opcodes specified in RFC3315, Section 22.

    
.. _CIM-DHCPSettingData-RequiredOptions:

``uint16[]`` **RequiredOptions**

    The list of DHCP options required for the client to operate properly. This list of DHCP options is for IPv4.

    
    ============ ================================================
    ValueMap     Values                                          
    ============ ================================================
    0            Unknown                                         
    1            Other                                           
    2            Pad                                             
    3            Subnet Mask                                     
    4            Time Offset                                     
    5            Router Option                                   
    6            Time Server                                     
    7            Name Server                                     
    8            Domain Name Server                              
    9            Log Server                                      
    10           Cookie Server                                   
    11           LPR Server                                      
    12           Impress Server                                  
    13           Resource Location Server                        
    14           Host Name                                       
    15           Boot File Size                                  
    16           Merit Dump File                                 
    17           Domain Name                                     
    18           Swap Server                                     
    19           Root Path                                       
    20           Extensions Path                                 
    21           IP Forwarding Enable/Disable                    
    22           Non-Local Source Routing Enable/Disable         
    23           Policy Filter                                   
    24           Maximum Datagram Reassembly Size                
    25           Default IP Time-to-live                         
    26           Path MTU Aging Timeout                          
    27           Path MTU Plateau Table                          
    28           Interface MTU                                   
    29           All Subnets are Local                           
    30           Broadcast Address                               
    31           Perform Subnet Mask Discovery                   
    32           Mask Supplier                                   
    33           Perform Router Discovery                        
    34           Router Solicitation Address                     
    35           Static Route                                    
    36           Trailer Encapsulation                           
    37           ARP Cache Timeout                               
    38           Ethernet Encapsulation                          
    39           TCP Default TTL                                 
    40           TCP Keepalive Interval                          
    41           TCP Keepalive Garbage                           
    42           Network Information Service Domain              
    43           Network Information Servers                     
    44           Network Time Protocol Servers                   
    45           Vendor Specific Information                     
    46           NetBIOS over TCP/IP Name Server                 
    47           NetBIOS over TCP/IP Datagram Distribution Server
    48           NetBIOS over TCP/IP Node Type                   
    49           NetBIOS over TCP/IP Scope                       
    50           X Window System Font Server                     
    51           X Window System Display Manager                 
    52           Requested IP Address                            
    53           Lease Time                                      
    54           Option Overload                                 
    55           Message Type                                    
    56           Server Identifier                               
    57           Parameter Request List                          
    58           Error Message                                   
    59           Maximum Message Size                            
    60           Renewal (T1) Time                               
    61           Rebinding (T2) Time                             
    62           Vendor Class Identifier                         
    63           Client Identifier                               
    64           DMTF Reserved                                   
    65           DMTF Reserved                                   
    66           Network Information Service+ Domain             
    67           Network Information Service+ Servers            
    68           TFTP Server Name                                
    69           Bootfile Name                                   
    70           Mobile IP Home Agent                            
    71           Simple Mail Transport Protocol (SMTP) Server    
    72           Post Office Protocol (POP3) Server              
    73           Network News Transport Protocol (NNTP) Server   
    74           Default World Wide Web (WWW) Server             
    75           Default Finger Server                           
    76           Default Internet Relay Chat (IRC) Server        
    77           StreetTalk Server                               
    78           StreetTalk Directory Assistance (STDA) Server   
    79           User Class                                      
    80           SLP Directory Agent                             
    81           SLP Service Scope                               
    82..83       DMTF Reserved                                   
    84           Relay Agent Information                         
    85..118      DMTF Reserved                                   
    119          Name Service Search                             
    120          Subnet Selection                                
    121..122     DMTF Reserved                                   
    123          Classless Route                                 
    124..256     DMTF Reserved                                   
    257          End                                             
    258..32767   DMTF Reserved                                   
    32768..65535 Vendor Reserved                                 
    ============ ================================================
    
.. _CIM-DHCPSettingData-IPv6RequiredOptions:

``uint16[]`` **IPv6RequiredOptions**

    The list of DHCP required for the client to operate properly. This list of options is for IPv6. The values of this property shall be the option-codes specified in RFC3315, Section 22.

    
.. _CIM-DHCPSettingData-RequestedIPv6Address:

``string`` **RequestedIPv6Address**

    The IPv6Address that this DHCPSettingData is requesting.

    
.. _CIM-DHCPSettingData-VendorClassIdentifier:

``string`` **VendorClassIdentifier**

    This property is used by DHCP clients to optionally identify the vendor type and configuration of a DHCP client. This corresponds to DHCP Option Code 60 as defined in RFC2132. While this is value is an option and therefore could be expressed using the RequestedOption property, it differs from other properties in that it includes a value when specified from the client.

    
.. _CIM-DHCPSettingData-RequestedOptions:

``uint16[]`` **RequestedOptions**

    The list of requested DHCP options which the client is capable of interpreting but not necessarily required for the client to operate properly. This list of DHCP options is for IPv4.

    
    ============ ================================================
    ValueMap     Values                                          
    ============ ================================================
    0            Unknown                                         
    1            Other                                           
    2            Pad                                             
    3            Subnet Mask                                     
    4            Time Offset                                     
    5            Router Option                                   
    6            Time Server                                     
    7            Name Server                                     
    8            Domain Name Server                              
    9            Log Server                                      
    10           Cookie Server                                   
    11           LPR Server                                      
    12           Impress Server                                  
    13           Resource Location Server                        
    14           Host Name                                       
    15           Boot File Size                                  
    16           Merit Dump File                                 
    17           Domain Name                                     
    18           Swap Server                                     
    19           Root Path                                       
    20           Extensions Path                                 
    21           IP Forwarding Enable/Disable                    
    22           Non-Local Source Routing Enable/Disable         
    23           Policy Filter                                   
    24           Maximum Datagram Reassembly Size                
    25           Default IP Time-to-live                         
    26           Path MTU Aging Timeout                          
    27           Path MTU Plateau Table                          
    28           Interface MTU                                   
    29           All Subnets are Local                           
    30           Broadcast Address                               
    31           Perform Subnet Mask Discovery                   
    32           Mask Supplier                                   
    33           Perform Router Discovery                        
    34           Router Solicitation Address                     
    35           Static Route                                    
    36           Trailer Encapsulation                           
    37           ARP Cache Timeout                               
    38           Ethernet Encapsulation                          
    39           TCP Default TTL                                 
    40           TCP Keepalive Interval                          
    41           TCP Keepalive Garbage                           
    42           Network Information Service Domain              
    43           Network Information Servers                     
    44           Network Time Protocol Servers                   
    45           Vendor Specific Information                     
    46           NetBIOS over TCP/IP Name Server                 
    47           NetBIOS over TCP/IP Datagram Distribution Server
    48           NetBIOS over TCP/IP Node Type                   
    49           NetBIOS over TCP/IP Scope                       
    50           X Window System Font Server                     
    51           X Window System Display Manager                 
    52           Requested IP Address                            
    53           Lease Time                                      
    54           Option Overload                                 
    55           Message Type                                    
    56           Server Identifier                               
    57           Parameter Request List                          
    58           Error Message                                   
    59           Maximum Message Size                            
    60           Renewal (T1) Time                               
    61           Rebinding (T2) Time                             
    62           Vendor Class Identifier                         
    63           Client Identifier                               
    64           DMTF Reserved                                   
    65           DMTF Reserved                                   
    66           Network Information Service+ Domain             
    67           Network Information Service+ Servers            
    68           TFTP Server Name                                
    69           Bootfile Name                                   
    70           Mobile IP Home Agent                            
    71           Simple Mail Transport Protocol (SMTP) Server    
    72           Post Office Protocol (POP3) Server              
    73           Network News Transport Protocol (NNTP) Server   
    74           Default World Wide Web (WWW) Server             
    75           Default Finger Server                           
    76           Default Internet Relay Chat (IRC) Server        
    77           StreetTalk Server                               
    78           StreetTalk Directory Assistance (STDA) Server   
    79           User Class                                      
    80           SLP Directory Agent                             
    81           SLP Service Scope                               
    82..83       DMTF Reserved                                   
    84           Relay Agent Information                         
    85..118      DMTF Reserved                                   
    119          Name Service Search                             
    120          Subnet Selection                                
    121..122     DMTF Reserved                                   
    123          Classless Route                                 
    124..256     DMTF Reserved                                   
    257          End                                             
    258..32767   DMTF Reserved                                   
    32768..65535 Vendor Reserved                                 
    ============ ================================================
    
.. _CIM-DHCPSettingData-ClientIdentifier:

``string`` **ClientIdentifier**

    This property is used by DHCP clients to specify their unique identifier. DHCP servers use this value to index their database of address bindings. This value is expected to be unique for all clients in an administrative domain. This corresponds to DHCP Option Code 61 as defined in RFC2132. 

    While this value is an option and therefore could be expressed using the RequestedOption property, it differs from other properties in that it includes a value when specified from the client.

    
.. _CIM-DHCPSettingData-RequestedIPv4Address:

``string`` **RequestedIPv4Address**

    A previously allocated IPv4 address for which the client is requesting re-allocation. This property is used in a client request (DHCPREQUEST) as the value of the ciaddr field. For AddressOrigin other than 4, this property shall be NULL.

    
.. _CIM-DHCPSettingData-AddressOrigin:

``uint16`` **AddressOrigin**

    AddressOrigin identifies the method by which the IP Address, Subnet Mask, and Gateway were assigned to the IPProtocolEndpoint. 

    A value of 4 indicates that the values will be assigned via DHCP. See RFC 2131 and related. 

    A value of 7 "DHCPv6" shall indicate the values will be assigned using DHCPv6. See RFC 3315.

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    4        DHCP           
    7        DHCPv6         
    ..       DMTF Reserved  
    32768..  Vendor Reserved
    ======== ===============
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`InstanceID <CIM-SettingData-InstanceID>`
| ``string`` :ref:`OtherAddressPrefixOriginDescription <CIM-IPAssignmentSettingData-OtherAddressPrefixOriginDescription>`
| ``string`` :ref:`ConfigurationName <CIM-SettingData-ConfigurationName>`
| ``string`` :ref:`SoOrgID <CIM-SettingData-SoOrgID>`
| ``string`` :ref:`OtherAddressSuffixOriginDescription <CIM-IPAssignmentSettingData-OtherAddressSuffixOriginDescription>`
| ``uint16`` :ref:`ProtocolIFType <CIM-IPAssignmentSettingData-ProtocolIFType>`
| ``string`` :ref:`ElementName <CIM-SettingData-ElementName>`
| ``uint16`` :ref:`AddressPrefixOrigin <CIM-IPAssignmentSettingData-AddressPrefixOrigin>`
| ``uint16`` :ref:`AddressSuffixOrigin <CIM-IPAssignmentSettingData-AddressSuffixOrigin>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`SoID <CIM-SettingData-SoID>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16`` :ref:`ChangeableType <CIM-SettingData-ChangeableType>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string[]`` :ref:`ComponentSetting <CIM-SettingData-ComponentSetting>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

