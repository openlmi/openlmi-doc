.. _CIM-RemoteServiceAccessPoint:

CIM_RemoteServiceAccessPoint
----------------------------

Class reference
===============
Subclass of :ref:`CIM_ServiceAccessPoint <CIM-ServiceAccessPoint>`

RemoteServiceAccessPoint describes access or addressing information or a combination of this information for a remote connection that is known to a local network element. This information is scoped or contained by the local network element, because this is the context in which the connection is remote. 

The relevance of the remote access point and information on its use are described by subclassing RemoteServiceAccessPoint or by associating to it.


Key properties
^^^^^^^^^^^^^^

| :ref:`CreationClassName <CIM-ServiceAccessPoint-CreationClassName>`
| :ref:`SystemName <CIM-ServiceAccessPoint-SystemName>`
| :ref:`Name <CIM-ServiceAccessPoint-Name>`
| :ref:`SystemCreationClassName <CIM-ServiceAccessPoint-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-RemoteServiceAccessPoint-AccessInfo:

``string`` **AccessInfo**

    Access or addressing information or a combination of this information for a remote connection. This information can be a host name, network address, or similar information.

    
.. _CIM-RemoteServiceAccessPoint-AccessContext:

``uint16`` **AccessContext**

    The AccessContext property identifies the role this RemoteServiceAccessPoint is playing in the hosting system.

    
    ============ ====================================
    ValueMap     Values                              
    ============ ====================================
    0            Unknown                             
    1            Other                               
    2            Default Gateway                     
    3            DNS Server                          
    4            SNMP Trap Destination               
    5            MPLS Tunnel Destination             
    6            DHCP Server                         
    7            SMTP Server                         
    8            LDAP Server                         
    9            Network Time Protocol (NTP) Server  
    10           Management Service                  
    11           internet Storage Name Service (iSNS)
    ..           DMTF Reserved                       
    32768..65535 Vendor Reserved                     
    ============ ====================================
    
.. _CIM-RemoteServiceAccessPoint-OtherInfoFormatDescription:

``string`` **OtherInfoFormatDescription**

    Describes the format when the property InfoFormat is set to 1 (Other).

    
.. _CIM-RemoteServiceAccessPoint-InfoFormat:

``uint16`` **InfoFormat**

    An enumerated integer that describes the format and interpretation of the AccessInfo property.

    206'Parameterized URL'- a URL containing ${parameterName} strings. Those strings are intended to be replaced in their entirety by the value of the named parameter. The interpretation of such parameters is not defined by this subclass. 

    As an example use: If a parameter named 'CompanyURL' has a value of 'www.DMTF.org' and the value of AccessInfo was 'http:\${CompanyURL}', then the resultant URL is intended to be 'http:\www.dmtf.org'.

    
    ============ ========================
    ValueMap     Values                  
    ============ ========================
    1            Other                   
    2            Host Name               
    3            IPv4 Address            
    4            IPv6 Address            
    5            IPX Address             
    6            DECnet Address          
    7            SNA Address             
    8            Autonomous System Number
    9            MPLS Label              
    10           IPv4 Subnet Address     
    11           IPv6 Subnet Address     
    12           IPv4 Address Range      
    13           IPv6 Address Range      
    100          Dial String             
    101          Ethernet Address        
    102          Token Ring Address      
    103          ATM Address             
    104          Frame Relay Address     
    200          URL                     
    201          FQDN                    
    202          User FQDN               
    203          DER ASN1 DN             
    204          DER ASN1 GN             
    205          Key ID                  
    206          Parameterized URL       
    ..           DMTF Reserved           
    32768..65535 Vendor Reserved         
    ============ ========================
    
.. _CIM-RemoteServiceAccessPoint-OtherAccessContext:

``string`` **OtherAccessContext**

    When the AccessContext property contains a value of 1, "Other" then this is a free form string providing more information about the role of RemoteServiceAccessPoint in the hosting system.

    

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
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`Name <CIM-ServiceAccessPoint-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`CreationClassName <CIM-ServiceAccessPoint-CreationClassName>`
| ``string`` :ref:`SystemCreationClassName <CIM-ServiceAccessPoint-SystemCreationClassName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`

