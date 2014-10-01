.. _CIM-SoftwareIdentityResource:

CIM_SoftwareIdentityResource
----------------------------

Class reference
===============
Subclass of :ref:`CIM_RemoteServiceAccessPoint <CIM-RemoteServiceAccessPoint>`

SoftwareIdentityResource describes the URL of a file or other resource that contains all or part of of a SoftwareIdentity for use by the SoftwareInstallationService. For example, a CIM_SoftwareIdentity might consist of a meta data file, a binary executable file, and a installability checker file for some software on a system. This class allows a management client to selectively access the constituents of the install package to perform a check function, or retrieve some meta data information for the install package represented by the SoftwareIdentity class without downloading the entire package. SoftwareIdentityResources will be related to the SoftwareIdentity using the SAPAvailableForElement association.


Key properties
^^^^^^^^^^^^^^

| :ref:`CreationClassName <CIM-ServiceAccessPoint-CreationClassName>`
| :ref:`SystemName <CIM-ServiceAccessPoint-SystemName>`
| :ref:`Name <CIM-ServiceAccessPoint-Name>`
| :ref:`SystemCreationClassName <CIM-ServiceAccessPoint-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-SoftwareIdentityResource-ExtendedResourceType:

``uint16`` **ExtendedResourceType**

    A enumerated integer that provides further information for ResourceType. It will set to 2 ('Not Applicable') if there is no extended information available.

    
    ============== ====================
    ValueMap       Values              
    ============== ====================
    0              Unknown             
    2              Not Applicable      
    3              Linux RPM           
    4              HP-UX Depot         
    5              Windows MSI         
    6              Solaris Package     
    7              Macintosh Disk Image
    8              Debian linux Package
    11             HP Smart Component  
    101..200       Vendor Reserved     
    201            HTML                
    202            PDF                 
    203            Text File           
    ..             DMTF Reserved       
    0x8000..0xFFFF Vendor Reserved     
    ============== ====================
    
.. _CIM-SoftwareIdentityResource-ResourceType:

``uint16`` **ResourceType**

    An enumerated integer that specifies the type of resource referenced by the RemoteServiceAccessPoint.AccessInfo property.

    
    ============== =======================
    ValueMap       Values                 
    ============== =======================
    0              Unknown                
    1              Other                  
    2              Installer and Payload  
    3              Installer              
    4              Payload                
    5              Installability checker 
    6              Security Advisory      
    7              Engineering Advisory   
    9              Technical release notes
    10             Change notification    
    11             Whitepaper             
    12             Marketing Documentation
    ..             DMTF Reserved          
    0x8000..0xFFFF Vendor Reserved        
    ============== =======================
    
.. _CIM-SoftwareIdentityResource-OtherResourceType:

``string`` **OtherResourceType**

    A string describing the file type when the instance's ResourceType property is 1 ("Other").

    
.. _CIM-SoftwareIdentityResource-InfoFormat:

``uint16`` **InfoFormat**

    A SoftwareIdentityResource will always be a URL.

    
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
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string`` :ref:`AccessInfo <CIM-RemoteServiceAccessPoint-AccessInfo>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`SystemName <CIM-ServiceAccessPoint-SystemName>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``uint16`` :ref:`AccessContext <CIM-RemoteServiceAccessPoint-AccessContext>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`Name <CIM-ServiceAccessPoint-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`OtherInfoFormatDescription <CIM-RemoteServiceAccessPoint-OtherInfoFormatDescription>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`OtherAccessContext <CIM-RemoteServiceAccessPoint-OtherAccessContext>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`CreationClassName <CIM-ServiceAccessPoint-CreationClassName>`
| ``string`` :ref:`SystemCreationClassName <CIM-ServiceAccessPoint-SystemCreationClassName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`

