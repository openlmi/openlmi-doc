.. _CIM-ProtocolEndpoint:

CIM_ProtocolEndpoint
--------------------

Class reference
===============
Subclass of :ref:`CIM_ServiceAccessPoint <CIM-ServiceAccessPoint>`

A communication point from which data can be sent or received. ProtocolEndpoints link system or computer interfaces to LogicalNetworks.


Key properties
^^^^^^^^^^^^^^

| :ref:`CreationClassName <CIM-ServiceAccessPoint-CreationClassName>`
| :ref:`SystemName <CIM-ServiceAccessPoint-SystemName>`
| :ref:`Name <CIM-ServiceAccessPoint-Name>`
| :ref:`SystemCreationClassName <CIM-ServiceAccessPoint-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-ProtocolEndpoint-TimeOfLastStateChange:

``datetime`` **TimeOfLastStateChange**

    The date or time when the EnabledState of the element last changed. If the state of the element has not changed and this property is populated, then it must be set to a 0 interval value. If a state change was requested, but rejected or not yet processed, the property must not be updated.

    
.. _CIM-ProtocolEndpoint-Description:

``string`` **Description**

    The Description property provides a textual description of the object.

    
.. _CIM-ProtocolEndpoint-NameFormat:

``string`` **NameFormat**

    NameFormat contains the naming heuristic that is selected to ensure that the value of the Name property is unique. For example, you might choose to prepend the name of the port or interface with the Type of ProtocolEndpoint (for example, IPv4) of this instance followed by an underscore.

    
.. _CIM-ProtocolEndpoint-Name:

``string`` **Name**

    A string that identifies this ProtocolEndpoint with either a port or an interface on a device. To ensure uniqueness, the Name property should be prepended or appended with information from the Type or OtherTypeDescription properties. The method selected is described in the NameFormat property of this class.

    
.. _CIM-ProtocolEndpoint-ProtocolIFType:

``uint16`` **ProtocolIFType**

    ProtocolIFType is an enumeration that is synchronized with the IANA ifType MIB. The ifType MIB is maintained at the URL, http://www.iana.org/assignments/ianaiftype-mib. Also, additional values defined by the DMTF are included. The property is used to categorize and classify instances of the ProtocolEndpoint class. Note that if the ProtocolIFType is set to 1 (Other), then the type information should be provided in the OtherTypeDescription string property.

    
    ========= ========================================================
    ValueMap  Values                                                  
    ========= ========================================================
    0         Unknown                                                 
    1         Other                                                   
    2         Regular 1822                                            
    3         HDH 1822                                                
    4         DDN X.25                                                
    5         RFC877 X.25                                             
    6         Ethernet CSMA/CD                                        
    7         ISO 802.3 CSMA/CD                                       
    8         ISO 802.4 Token Bus                                     
    9         ISO 802.5 Token Ring                                    
    10        ISO 802.6 MAN                                           
    11        StarLAN                                                 
    12        Proteon 10Mbit                                          
    13        Proteon 80Mbit                                          
    14        HyperChannel                                            
    15        FDDI                                                    
    16        LAP-B                                                   
    17        SDLC                                                    
    18        DS1                                                     
    19        E1                                                      
    20        Basic ISDN                                              
    21        Primary ISDN                                            
    22        Proprietary Point-to-Point Serial                       
    23        PPP                                                     
    24        Software Loopback                                       
    25        EON                                                     
    26        Ethernet 3Mbit                                          
    27        NSIP                                                    
    28        SLIP                                                    
    29        Ultra                                                   
    30        DS3                                                     
    31        SIP                                                     
    32        Frame Relay                                             
    33        RS-232                                                  
    34        Parallel                                                
    35        ARCNet                                                  
    36        ARCNet Plus                                             
    37        ATM                                                     
    38        MIO X.25                                                
    39        SONET                                                   
    40        X.25 PLE                                                
    41        ISO 802.211c                                            
    42        LocalTalk                                               
    43        SMDS DXI                                                
    44        Frame Relay Service                                     
    45        V.35                                                    
    46        HSSI                                                    
    47        HIPPI                                                   
    48        Modem                                                   
    49        AAL5                                                    
    50        SONET Path                                              
    51        SONET VT                                                
    52        SMDS ICIP                                               
    53        Proprietary Virtual/Internal                            
    54        Proprietary Multiplexor                                 
    55        IEEE 802.12                                             
    56        Fibre Channel                                           
    57        HIPPI Interface                                         
    58        Frame Relay Interconnect                                
    59        ATM Emulated LAN for 802.3                              
    60        ATM Emulated LAN for 802.5                              
    61        ATM Emulated Circuit                                    
    62        Fast Ethernet (100BaseT)                                
    63        ISDN                                                    
    64        V.11                                                    
    65        V.36                                                    
    66        G703 at 64K                                             
    67        G703 at 2Mb                                             
    68        QLLC                                                    
    69        Fast Ethernet 100BaseFX                                 
    70        Channel                                                 
    71        IEEE 802.11                                             
    72        IBM 260/370 OEMI Channel                                
    73        ESCON                                                   
    74        Data Link Switching                                     
    75        ISDN S/T Interface                                      
    76        ISDN U Interface                                        
    77        LAP-D                                                   
    78        IP Switch                                               
    79        Remote Source Route Bridging                            
    80        ATM Logical                                             
    81        DS0                                                     
    82        DS0 Bundle                                              
    83        BSC                                                     
    84        Async                                                   
    85        Combat Net Radio                                        
    86        ISO 802.5r DTR                                          
    87        Ext Pos Loc Report System                               
    88        AppleTalk Remote Access Protocol                        
    89        Proprietary Connectionless                              
    90        ITU X.29 Host PAD                                       
    91        ITU X.3 Terminal PAD                                    
    92        Frame Relay MPI                                         
    93        ITU X.213                                               
    94        ADSL                                                    
    95        RADSL                                                   
    96        SDSL                                                    
    97        VDSL                                                    
    98        ISO 802.5 CRFP                                          
    99        Myrinet                                                 
    100       Voice Receive and Transmit                              
    101       Voice Foreign Exchange Office                           
    102       Voice Foreign Exchange Service                          
    103       Voice Encapsulation                                     
    104       Voice over IP                                           
    105       ATM DXI                                                 
    106       ATM FUNI                                                
    107       ATM IMA                                                 
    108       PPP Multilink Bundle                                    
    109       IP over CDLC                                            
    110       IP over CLAW                                            
    111       Stack to Stack                                          
    112       Virtual IP Address                                      
    113       MPC                                                     
    114       IP over ATM                                             
    115       ISO 802.5j Fibre Token Ring                             
    116       TDLC                                                    
    117       Gigabit Ethernet                                        
    118       HDLC                                                    
    119       LAP-F                                                   
    120       V.37                                                    
    121       X.25 MLP                                                
    122       X.25 Hunt Group                                         
    123       Transp HDLC                                             
    124       Interleave Channel                                      
    125       FAST Channel                                            
    126       IP (for APPN HPR in IP Networks)                        
    127       CATV MAC Layer                                          
    128       CATV Downstream                                         
    129       CATV Upstream                                           
    130       Avalon 12MPP Switch                                     
    131       Tunnel                                                  
    132       Coffee                                                  
    133       Circuit Emulation Service                               
    134       ATM SubInterface                                        
    135       Layer 2 VLAN using 802.1Q                               
    136       Layer 3 VLAN using IP                                   
    137       Layer 3 VLAN using IPX                                  
    138       Digital Power Line                                      
    139       Multimedia Mail over IP                                 
    140       DTM                                                     
    141       DCN                                                     
    142       IP Forwarding                                           
    143       MSDSL                                                   
    144       IEEE 1394                                               
    145       IF-GSN/HIPPI-6400                                       
    146       DVB-RCC MAC Layer                                       
    147       DVB-RCC Downstream                                      
    148       DVB-RCC Upstream                                        
    149       ATM Virtual                                             
    150       MPLS Tunnel                                             
    151       SRP                                                     
    152       Voice over ATM                                          
    153       Voice over Frame Relay                                  
    154       ISDL                                                    
    155       Composite Link                                          
    156       SS7 Signaling Link                                      
    157       Proprietary P2P Wireless                                
    158       Frame Forward                                           
    159       RFC1483 Multiprotocol over ATM                          
    160       USB                                                     
    161       IEEE 802.3ad Link Aggregate                             
    162       BGP Policy Accounting                                   
    163       FRF .16 Multilink FR                                    
    164       H.323 Gatekeeper                                        
    165       H.323 Proxy                                             
    166       MPLS                                                    
    167       Multi-Frequency Signaling Link                          
    168       HDSL-2                                                  
    169       S-HDSL                                                  
    170       DS1 Facility Data Link                                  
    171       Packet over SONET/SDH                                   
    172       DVB-ASI Input                                           
    173       DVB-ASI Output                                          
    174       Power Line                                              
    175       Non Facility Associated Signaling                       
    176       TR008                                                   
    177       GR303 RDT                                               
    178       GR303 IDT                                               
    179       ISUP                                                    
    180       Proprietary Wireless MAC Layer                          
    181       Proprietary Wireless Downstream                         
    182       Proprietary Wireless Upstream                           
    183       HIPERLAN Type 2                                         
    184       Proprietary Broadband Wireless Access Point to Mulipoint
    185       SONET Overhead Channel                                  
    186       Digital Wrapper Overhead Channel                        
    187       ATM Adaptation Layer 2                                  
    188       Radio MAC                                               
    189       ATM Radio                                               
    190       Inter Machine Trunk                                     
    191       MVL DSL                                                 
    192       Long Read DSL                                           
    193       Frame Relay DLCI Endpoint                               
    194       ATM VCI Endpoint                                        
    195       Optical Channel                                         
    196       Optical Transport                                       
    197       Proprietary ATM                                         
    198       Voice over Cable                                        
    199       Infiniband                                              
    200       TE Link                                                 
    201       Q.2931                                                  
    202       Virtual Trunk Group                                     
    203       SIP Trunk Group                                         
    204       SIP Signaling                                           
    205       CATV Upstream Channel                                   
    206       Econet                                                  
    207       FSAN 155Mb PON                                          
    208       FSAN 622Mb PON                                          
    209       Transparent Bridge                                      
    210       Line Group                                              
    211       Voice E&M Feature Group                                 
    212       Voice FGD EANA                                          
    213       Voice DID                                               
    214       MPEG Transport                                          
    215       6To4                                                    
    216       GTP                                                     
    217       Paradyne EtherLoop 1                                    
    218       Paradyne EtherLoop 2                                    
    219       Optical Channel Group                                   
    220       HomePNA                                                 
    221       GFP                                                     
    222       ciscoISLvlan                                            
    223       actelisMetaLOOP                                         
    224       Fcip                                                    
    225..4095 IANA Reserved                                           
    4096      IPv4                                                    
    4097      IPv6                                                    
    4098      IPv4/v6                                                 
    4099      IPX                                                     
    4100      DECnet                                                  
    4101      SNA                                                     
    4102      CONP                                                    
    4103      CLNP                                                    
    4104      VINES                                                   
    4105      XNS                                                     
    4106      ISDN B Channel Endpoint                                 
    4107      ISDN D Channel Endpoint                                 
    4108      BGP                                                     
    4109      OSPF                                                    
    4110      UDP                                                     
    4111      TCP                                                     
    4112      802.11a                                                 
    4113      802.11b                                                 
    4114      802.11g                                                 
    4115      802.11h                                                 
    4200      NFS                                                     
    4201      CIFS                                                    
    4202      DAFS                                                    
    4203      WebDAV                                                  
    4204      HTTP                                                    
    4205      FTP                                                     
    4300      NDMP                                                    
    4400      Telnet                                                  
    4401      SSH                                                     
    4402      SM CLP                                                  
    4403      SMTP                                                    
    4404      LDAP                                                    
    4405      RDP                                                     
    4406      HTTPS                                                   
    ..        DMTF Reserved                                           
    32768..   Vendor Reserved                                         
    ========= ========================================================
    
.. _CIM-ProtocolEndpoint-EnabledState:

``uint16`` **EnabledState**

    EnabledState is an integer enumeration that indicates the enabled and disabled states of an element. It can also indicate the transitions between these requested states. For example, shutting down (value=4) and starting (value=10) are transient states between enabled and disabled. The following text briefly summarizes the various enabled and disabled states: 

    Enabled (2) indicates that the element is or could be executing commands, will process any queued commands, and queues new requests. 

    Disabled (3) indicates that the element will not execute commands and will drop any new requests. 

    Shutting Down (4) indicates that the element is in the process of going to a Disabled state. 

    Not Applicable (5) indicates the element does not support being enabled or disabled. 

    Enabled but Offline (6) indicates that the element might be completing commands, and will drop any new requests. 

    Test (7) indicates that the element is in a test state. 

    Deferred (8) indicates that the element might be completing commands, but will queue any new requests. 

    Quiesce (9) indicates that the element is enabled but in a restricted mode.

    Starting (10) indicates that the element is in the process of going to an Enabled state. New requests are queued.

    
    ============ ===================
    ValueMap     Values             
    ============ ===================
    0            Unknown            
    1            Other              
    2            Enabled            
    3            Disabled           
    4            Shutting Down      
    5            Not Applicable     
    6            Enabled but Offline
    7            In Test            
    8            Deferred           
    9            Quiesce            
    10           Starting           
    11..32767    DMTF Reserved      
    32768..65535 Vendor Reserved    
    ============ ===================
    
.. _CIM-ProtocolEndpoint-OtherTypeDescription:

``string`` **OtherTypeDescription**

    A string that describes the type of ProtocolEndpoint when the Type property of this class (or any of its subclasses) is set to 1 (Other). This property should be set to null when the Type property is any value other than 1.

    
.. _CIM-ProtocolEndpoint-BroadcastResetSupported:

``boolean`` **BroadcastResetSupported**

    A boolean indicating whether the instrumentation supports the BroadcastReset method.

    
.. _CIM-ProtocolEndpoint-ProtocolType:

``uint16`` **ProtocolType**

    **Deprecated!** 
    Note: This property is deprecated in lieu of the ProtocolIFType enumeration. This deprecation was done to have better alignment between the IF-MIB of the IETF and this CIM class. 

    Deprecated description: ProtocolType is an enumeration that provides information to categorize and classify different instances of this class. For most instances, information in this enumeration and the definition of the subclass overlap. However, there are several cases where a specific subclass of ProtocolEndpoint is not required (for example, there is no Fibre Channel subclass of ProtocolEndpoint). Therefore, this property is needed to define the type of Endpoint.

    
    ======== =======================
    ValueMap Values                 
    ======== =======================
    0        Unknown                
    1        Other                  
    2        IPv4                   
    3        IPv6                   
    4        IPX                    
    5        AppleTalk              
    6        DECnet                 
    7        SNA                    
    8        CONP                   
    9        CLNP                   
    10       VINES                  
    11       XNS                    
    12       ATM                    
    13       Frame Relay            
    14       Ethernet               
    15       TokenRing              
    16       FDDI                   
    17       Infiniband             
    18       Fibre Channel          
    19       ISDN BRI Endpoint      
    20       ISDN B Channel Endpoint
    21       ISDN D Channel Endpoint
    22       IPv4/v6                
    23       BGP                    
    24       OSPF                   
    25       MPLS                   
    26       UDP                    
    27       TCP                    
    ======== =======================
    
.. _CIM-ProtocolEndpoint-OperationalStatus:

``uint16[]`` **OperationalStatus**

    Indicates the current statuses of the element. Various operational statuses are defined. Many of the enumeration's values are self-explanatory. However, a few are not and are described here in more detail. 

    "Stressed" indicates that the element is functioning, but needs attention. Examples of "Stressed" states are overload, overheated, and so on. 

    "Predictive Failure" indicates that an element is functioning nominally but predicting a failure in the near future. 

    "In Service" describes an element being configured, maintained, cleaned, or otherwise administered. 

    "No Contact" indicates that the monitoring system has knowledge of this element, but has never been able to establish communications with it. 

    "Lost Communication" indicates that the ManagedSystem Element is known to exist and has been contacted successfully in the past, but is currently unreachable. 

    "Stopped" and "Aborted" are similar, although the former implies a clean and orderly stop, while the latter implies an abrupt stop where the state and configuration of the element might need to be updated. 

    "Dormant" indicates that the element is inactive or quiesced. 

    "Supporting Entity in Error" indicates that this element might be "OK" but that another element, on which it is dependent, is in error. An example is a network service or endpoint that cannot function due to lower-layer networking problems. 

    "Completed" indicates that the element has completed its operation. This value should be combined with either OK, Error, or Degraded so that a client can tell if the complete operation Completed with OK (passed), Completed with Error (failed), or Completed with Degraded (the operation finished, but it did not complete OK or did not report an error). 

    "Power Mode" indicates that the element has additional power model information contained in the Associated PowerManagementService association. 

    "Relocating" indicates the element is being relocated.

    OperationalStatus replaces the Status property on ManagedSystemElement to provide a consistent approach to enumerations, to address implementation needs for an array property, and to provide a migration path from today's environment to the future. This change was not made earlier because it required the deprecated qualifier. Due to the widespread use of the existing Status property in management applications, it is strongly recommended that providers or instrumentation provide both the Status and OperationalStatus properties. Further, the first value of OperationalStatus should contain the primary status for the element. When instrumented, Status (because it is single-valued) should also provide the primary status of the element.

    
    ======== ==========================
    ValueMap Values                    
    ======== ==========================
    0        Unknown                   
    1        Other                     
    2        OK                        
    3        Degraded                  
    4        Stressed                  
    5        Predictive Failure        
    6        Error                     
    7        Non-Recoverable Error     
    8        Starting                  
    9        Stopping                  
    10       Stopped                   
    11       In Service                
    12       No Contact                
    13       Lost Communication        
    14       Aborted                   
    15       Dormant                   
    16       Supporting Entity in Error
    17       Completed                 
    18       Power Mode                
    19       Relocating                
    ..       DMTF Reserved             
    0x8000.. Vendor Reserved           
    ======== ==========================
    

Local methods
^^^^^^^^^^^^^

    .. _CIM-ProtocolEndpoint-BroadcastReset:

``uint32`` **BroadcastReset** ()

    Send a broadcast reset. A broadcast reset is a request that peers perform a reset. Examples include a parallel SCSI Bus Reset and a Fibre Channel LIP.

    
    ============== =================
    ValueMap       Values           
    ============== =================
    0              Success          
    1              Not_Supported    
    2              Unspecified Error
    3              Timeout          
    4              Failed           
    5..0x0FFF      DMTF_Reserved    
    0x1000..0x7777 Method_Reserved  
    0x8000..       Vendor_Reserved  
    ============== =================
    
    **Parameters**
    
*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`SystemName <CIM-ServiceAccessPoint-SystemName>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`CreationClassName <CIM-ServiceAccessPoint-CreationClassName>`
| ``string`` :ref:`SystemCreationClassName <CIM-ServiceAccessPoint-SystemCreationClassName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`

