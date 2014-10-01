.. _LMI-SoftwareIdentityResource:

LMI_SoftwareIdentityResource
----------------------------

Class reference
===============
Subclass of :ref:`CIM_SoftwareIdentityResource <CIM-SoftwareIdentityResource>`

SoftwareIdentityResource describes the URL of a file or other resource that contains all or part of of a SoftwareIdentity for use by the SoftwareInstallationService. For example, a CIM_SoftwareIdentity might consist of a meta data file, a binary executable file, and a installability checker file for some software on a system. This class allows a management client to selectively access the constituents of the install package to perform a check function, or retrieve some meta data information for the install package represented by the SoftwareIdentity class without downloading the entire package. SoftwareIdentityResources will be related to the SoftwareIdentity using the SAPAvailableForElement association.


Key properties
^^^^^^^^^^^^^^

| :ref:`CreationClassName <CIM-ServiceAccessPoint-CreationClassName>`
| :ref:`SystemName <CIM-ServiceAccessPoint-SystemName>`
| :ref:`Name <CIM-ServiceAccessPoint-Name>`
| :ref:`SystemCreationClassName <CIM-ServiceAccessPoint-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-SoftwareIdentityResource-RequestedState:

``uint16`` **RequestedState**

    RequestedState is an integer enumeration that indicates the last requested or desired state for the element, irrespective of the mechanism through which it was requested. The actual state of the element is represented by EnabledState. This property is provided to compare the last requested and current enabled or disabled states. Note that when EnabledState is set to 5 ("Not Applicable"), then this property has no meaning. Refer to the EnabledState property description for explanations of the values in the RequestedState enumeration. 

    "Unknown" (0) indicates the last requested state for the element is unknown.

    Note that the value "No Change" (5) has been deprecated in lieu of indicating the last requested state is "Unknown" (0). If the last requested or desired state is unknown, RequestedState should have the value "Unknown" (0), but may have the value "No Change" (5).Offline (6) indicates that the element has been requested to transition to the Enabled but Offline EnabledState. 

    It should be noted that there are two new values in RequestedState that build on the statuses of EnabledState. These are "Reboot" (10) and "Reset" (11). Reboot refers to doing a "Shut Down" and then moving to an "Enabled" state. Reset indicates that the element is first "Disabled" and then "Enabled". The distinction between requesting "Shut Down" and "Disabled" should also be noted. Shut Down requests an orderly transition to the Disabled state, and might involve removing power, to completely erase any existing state. The Disabled state requests an immediate disabling of the element, such that it will not execute or accept any commands or processing requests. 

    

    This property is set as the result of a method invocation (such as Start or StopService on CIM_Service), or can be overridden and defined as WRITEable in a subclass. The method approach is considered superior to a WRITEable property, because it allows an explicit invocation of the operation and the return of a result code. 

    

    If knowledge of the last RequestedState is not supported for the EnabledLogicalElement, the property shall be NULL or have the value 12 "Not Applicable".

    
    ============ ===============
    ValueMap     Values         
    ============ ===============
    0            Unknown        
    2            Enabled        
    3            Disabled       
    4            Shut Down      
    5            No Change      
    6            Offline        
    7            Test           
    8            Deferred       
    9            Quiesce        
    10           Reboot         
    11           Reset          
    12           Not Applicable 
    ..           DMTF Reserved  
    32768..65535 Vendor Reserved
    ============ ===============
    
.. _LMI-SoftwareIdentityResource-HealthState:

``uint16`` **HealthState**

    Indicates the current health of the element. This attribute expresses the health of this element but not necessarily that of its subcomponents. The possible values are 0 to 30, where 5 means the element is entirely healthy and 30 means the element is completely non-functional. The following continuum is defined: 

    "Non-recoverable Error" (30) - The element has completely failed, and recovery is not possible. All functionality provided by this element has been lost. 

    "Critical Failure" (25) - The element is non-functional and recovery might not be possible. 

    "Major Failure" (20) - The element is failing. It is possible that some or all of the functionality of this component is degraded or not working. 

    "Minor Failure" (15) - All functionality is available but some might be degraded. 

    "Degraded/Warning" (10) - The element is in working order and all functionality is provided. However, the element is not working to the best of its abilities. For example, the element might not be operating at optimal performance or it might be reporting recoverable errors. 

    "OK" (5) - The element is fully functional and is operating within normal operational parameters and without error. 

    "Unknown" (0) - The implementation cannot report on HealthState at this time. 

    DMTF has reserved the unused portion of the continuum for additional HealthStates in the future.

    
    ============ =====================
    ValueMap     Values               
    ============ =====================
    0            Unknown              
    5            OK                   
    10           Degraded/Warning     
    15           Minor failure        
    20           Major failure        
    25           Critical failure     
    30           Non-recoverable error
    ..           DMTF Reserved        
    32768..65535 Vendor Specific      
    ============ =====================
    
.. _LMI-SoftwareIdentityResource-AccessInfo:

``string`` **AccessInfo**

    Access or addressing information or a combination of this information for a remote connection. This information can be a host name, network address, or similar information.

    
.. _LMI-SoftwareIdentityResource-StatusDescriptions:

``string[]`` **StatusDescriptions**

    Strings describing the various OperationalStatus array values. For example, if "Stopping" is the value assigned to OperationalStatus, then this property may contain an explanation as to why an object is being stopped. Note that entries in this array are correlated with those at the same array index in OperationalStatus.

    
.. _LMI-SoftwareIdentityResource-ExtendedResourceType:

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
    
.. _LMI-SoftwareIdentityResource-InstanceID:

``string`` **InstanceID**

    InstanceID is an optional property that may be used to opaquely and uniquely identify an instance of this class within the scope of the instantiating Namespace. Various subclasses of this class may override this property to make it required, or a key. Such subclasses may also modify the preferred algorithms for ensuring uniqueness that are defined below.

    To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon (:), and where <OrgID> must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness, <OrgID> must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If not null and the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance. 

    If not set to null for DMTF-defined instances, the "preferred" algorithm must be used with the <OrgID> set to CIM.

    
.. _LMI-SoftwareIdentityResource-SystemName:

``string`` **SystemName**

    The Name of the scoping System.

    
.. _LMI-SoftwareIdentityResource-MirrorList:

``string`` **MirrorList**

    URL to a file containing list of base URLS to mirrors of this repository. http://, ftp:// and file:// schemas are supported. This can contain special variables prefixed with $, which are substituted for system values. These include $releasever - defaults to the version of "redhat-release" package, $arch - architecture of system, $basearch - base architecture of system ($arch == "i686", then $basearch == "i386", $uuid - unique but persisent uuid for this machine.

    
.. _LMI-SoftwareIdentityResource-AccessContext:

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
    
.. _LMI-SoftwareIdentityResource-Description:

``string`` **Description**

    The Description property provides a textual description of the object.

    
.. _LMI-SoftwareIdentityResource-TransitioningToState:

``uint16`` **TransitioningToState**

    TransitioningToState indicates the target state to which the instance is transitioning. 

    A value of 5 "No Change" shall indicate that no transition is in progress.A value of 12 "Not Applicable" shall indicate the implementation does not support representing ongoing transitions. 

    A value other than 5 or 12 shall identify the state to which the element is in the process of transitioning.

    
    ======== ==============
    ValueMap Values        
    ======== ==============
    0        Unknown       
    2        Enabled       
    3        Disabled      
    4        Shut Down     
    5        No Change     
    6        Offline       
    7        Test          
    8        Defer         
    9        Quiesce       
    10       Reboot        
    11       Reset         
    12       Not Applicable
    ..       DMTF Reserved 
    ======== ==============
    
.. _LMI-SoftwareIdentityResource-TimeOfLastStateChange:

``datetime`` **TimeOfLastStateChange**

    The date or time when the EnabledState of the element last changed. If the state of the element has not changed and this property is populated, then it must be set to a 0 interval value. If a state change was requested, but rejected or not yet processed, the property must not be updated.

    
.. _LMI-SoftwareIdentityResource-AvailableRequestedStates:

``uint16[]`` **AvailableRequestedStates**

    AvailableRequestedStates indicates the possible values for the RequestedState parameter of the method RequestStateChange, used to initiate a state change. The values listed shall be a subset of the values contained in the RequestedStatesSupported property of the associated instance of CIM_EnabledLogicalElementCapabilities where the values selected are a function of the current state of the CIM_EnabledLogicalElement. This property may be non-null if an implementation is able to advertise the set of possible values as a function of the current state. This property shall be null if an implementation is unable to determine the set of possible values as a function of the current state.

    
    ======== =============
    ValueMap Values       
    ======== =============
    2        Enabled      
    3        Disabled     
    4        Shut Down    
    6        Offline      
    7        Test         
    8        Defer        
    9        Quiesce      
    10       Reboot       
    11       Reset        
    ..       DMTF Reserved
    ======== =============
    
.. _LMI-SoftwareIdentityResource-RepoGPGCheck:

``boolean`` **RepoGPGCheck**

    Whether or not a GPG signature check should be performed on the repodata from this repository.

    
.. _LMI-SoftwareIdentityResource-ResourceType:

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
    
.. _LMI-SoftwareIdentityResource-OperationalStatus:

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
    
.. _LMI-SoftwareIdentityResource-GPGCheck:

``boolean`` **GPGCheck**

    Whether or not a GPG signature check should be performed on the packages gotten from this repository.

    
.. _LMI-SoftwareIdentityResource-Name:

``string`` **Name**

    Repository id. A unique name representing repository of system.

    
.. _LMI-SoftwareIdentityResource-EnabledDefault:

``uint16`` **EnabledDefault**

    An enumerated value indicating an administrator's default or startup configuration for the Enabled State of an element. By default, the element is "Enabled" (value=2).

    
    ============ ===================
    ValueMap     Values             
    ============ ===================
    2            Enabled            
    3            Disabled           
    5            Not Applicable     
    6            Enabled but Offline
    7            No Default         
    9            Quiesce            
    ..           DMTF Reserved      
    32768..65535 Vendor Reserved    
    ============ ===================
    
.. _LMI-SoftwareIdentityResource-EnabledState:

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
    
.. _LMI-SoftwareIdentityResource-ElementName:

``string`` **ElementName**

    A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. 

    Note that the Name property of ManagedSystemElement is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. Note that if there is an associated instance of CIM_EnabledLogicalElementCapabilities, restrictions on this properties may exist as defined in ElementNameMask and MaxElementNameLen properties defined in that class.

    
.. _LMI-SoftwareIdentityResource-Caption:

``string`` **Caption**

    A human readable string describing the repository.

    
.. _LMI-SoftwareIdentityResource-PrimaryStatus:

``uint16`` **PrimaryStatus**

    PrimaryStatus provides a high level status value, intended to align with Red-Yellow-Green type representation of status. It should be used in conjunction with DetailedStatus to provide high level and detailed health status of the ManagedElement and its subcomponents. 

    PrimaryStatus consists of one of the following values: Unknown, OK, Degraded or Error. "Unknown" indicates the implementation is in general capable of returning this property, but is unable to do so at this time. 

    "OK" indicates the ManagedElement is functioning normally. 

    "Degraded" indicates the ManagedElement is functioning below normal. 

    "Error" indicates the ManagedElement is in an Error condition.

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    0        Unknown        
    1        OK             
    2        Degraded       
    3        Error          
    ..       DMTF Reserved  
    0x8000.. Vendor Reserved
    ======== ===============
    
.. _LMI-SoftwareIdentityResource-InfoFormat:

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
    
.. _LMI-SoftwareIdentityResource-Generation:

``uint64`` **Generation**

    Generation is an optional, monotonically increasing property that may be used to identify a particular generation of the resource represented by this class.

    If Generation is supported by the implementation, its value shall not be null. 

    Except as otherwise specified, a value (including null) of Generation specified at creation time shall be replaced by null if Generation is not supported by the implementation or shall be a, (possibly different), non-null value if the implementation does support Generation.

    After creation and if supported, Generation shall be updated, at least once per access, whenever the represented resource is modified, regardless of the source of the modification.

    Note: the Generation value only needs to be updated once between references, even if the resource is updated many times. The key point is to assure that it will be different if there have been updates, not to count each update.

    Note: unless otherwise specified, the value of Generation within one instance is not required to be coordinated with the value of Generation in any other instance.

    Note:the semantics of the instance, (as defined by its creation class), define the underlying resource. That underlying resource may be a collection or aggregation of resources. And, in that case, the semantics of the instance further define when updates to constituent resources also require updates to the Generation of the collective resource. Default behavior of composite aggregations should be to update the Generation of the composite whenever the Generation of a component is updated.

    Subclasses may define additional requirements for updates on some or all of related instances.

    For a particular instance, the value of Generation may wrap through zero, but the elapsed time between wraps shall be greater than 10's of years.

    This class does not require Generation to be unique across instances of other classes nor across instances of the same class that have different keys. Generation shall be different across power cycles, resets, or reboots if any of those actions results in an update. Generation may be different across power cycles, resets, or reboots if those actions do not result in an update. If the Generation property of an instance is non-null, and if any attempt to update the instance includes the Generation property, then if it doesn't match the current value, the update shall fail.

    The usage of this property is intended to be further specified by applicable management profiles. 

    Typically, a client will read the value of this property and then supply that value as input to an operation that modifies the instance in some means. This may be via an explicit parameter in an extrinsic method or via an embedded value in an extrinsic method or intrinsic operation.

    For example: a profile may require that an intrinsic instance modification supply the Generation property and that it must match for the modification to succeed.

    
.. _LMI-SoftwareIdentityResource-OtherAccessContext:

``string`` **OtherAccessContext**

    When the AccessContext property contains a value of 1, "Other" then this is a free form string providing more information about the role of RemoteServiceAccessPoint in the hosting system.

    
.. _LMI-SoftwareIdentityResource-Cost:

``sint32`` **Cost**

    Relative cost of accessing this repository. Useful for weighing one repo's packages as greater/less than any other.

    
.. _LMI-SoftwareIdentityResource-CreationClassName:

``string`` **CreationClassName**

    CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

    
.. _LMI-SoftwareIdentityResource-SystemCreationClassName:

``string`` **SystemCreationClassName**

    The CreationClassName of the scoping System.

    
.. _LMI-SoftwareIdentityResource-TimeOfLastUpdate:

``datetime`` **TimeOfLastUpdate**

    Time of the repository's last update on server.

    

Local methods
^^^^^^^^^^^^^

    .. _LMI-SoftwareIdentityResource-RequestStateChange:

``uint32`` **RequestStateChange** (``uint16`` RequestedState, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, ``datetime`` TimeoutPeriod)

    Requests that the state of the element be changed to the value specified in the RequestedState parameter. When the requested state change takes place, the EnabledState and RequestedState of the element will be the same. Invoking the RequestStateChange method multiple times could result in earlier requests being overwritten or lost. 

    A return code of 0 shall indicate the state change was successfully initiated. 

    A return code of 3 shall indicate that the state transition cannot complete within the interval specified by the TimeoutPeriod parameter. 

    A return code of 4096 (0x1000) shall indicate the state change was successfully initiated, a ConcreteJob has been created, and its reference returned in the output parameter Job. Any other return code indicates an error condition.

    
    ============ =======================================
    ValueMap     Values                                 
    ============ =======================================
    0            Completed with No Error                
    1            Not Supported                          
    2            Unknown or Unspecified Error           
    3            Cannot complete within Timeout Period  
    4            Failed                                 
    5            Invalid Parameter                      
    6            In Use                                 
    ..           DMTF Reserved                          
    4096         Method Parameters Checked - Job Started
    4097         Invalid State Transition               
    4098         Use of Timeout Parameter Not Supported 
    4099         Busy                                   
    4100..32767  Method Reserved                        
    32768..65535 Vendor Specific                        
    ============ =======================================
    
    **Parameters**
    
        *IN* ``uint16`` **RequestedState**
            The state requested for the element. This information will be placed into the RequestedState property of the instance if the return code of the RequestStateChange method is 0 ('Completed with No Error'), or 4096 (0x1000) ('Job Started'). Refer to the description of the EnabledState and RequestedState properties for the detailed explanations of the RequestedState values.

            
            ============ ===============
            ValueMap     Values         
            ============ ===============
            2            Enabled        
            3            Disabled       
            4            Shut Down      
            6            Offline        
            7            Test           
            8            Defer          
            9            Quiesce        
            10           Reboot         
            11           Reset          
            ..           DMTF Reserved  
            32768..65535 Vendor Reserved
            ============ ===============
            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            May contain a reference to the ConcreteJob created to track the state transition initiated by the method invocation.

            
        
        *IN* ``datetime`` **TimeoutPeriod**
            A timeout period that specifies the maximum amount of time that the client expects the transition to the new state to take. The interval format must be used to specify the TimeoutPeriod. A value of 0 or a null parameter indicates that the client has no time requirements for the transition. 

            If this property does not contain 0 or null and the implementation does not support this parameter, a return code of 'Use Of Timeout Parameter Not Supported' shall be returned.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string`` :ref:`OtherResourceType <CIM-SoftwareIdentityResource-OtherResourceType>`
| ``string`` :ref:`OtherInfoFormatDescription <CIM-RemoteServiceAccessPoint-OtherInfoFormatDescription>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

