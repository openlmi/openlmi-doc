.. _LMI-SoftwareInstallationService:

LMI_SoftwareInstallationService
-------------------------------

Class reference
===============
Subclass of :ref:`CIM_SoftwareInstallationService <CIM-SoftwareInstallationService>`

A subclass of service which provides methods to install (or update) Software Identities in ManagedElements.


Key properties
^^^^^^^^^^^^^^

| :ref:`Name <CIM-Service-Name>`
| :ref:`SystemName <CIM-Service-SystemName>`
| :ref:`SystemCreationClassName <CIM-Service-SystemCreationClassName>`
| :ref:`CreationClassName <CIM-Service-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-SoftwareInstallationService-RequestedState:

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
    
.. _LMI-SoftwareInstallationService-HealthState:

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
    
.. _LMI-SoftwareInstallationService-InstanceID:

``string`` **InstanceID**

    InstanceID is an optional property that may be used to opaquely and uniquely identify an instance of this class within the scope of the instantiating Namespace. Various subclasses of this class may override this property to make it required, or a key. Such subclasses may also modify the preferred algorithms for ensuring uniqueness that are defined below.

    To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon (:), and where <OrgID> must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness, <OrgID> must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If not null and the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance. 

    If not set to null for DMTF-defined instances, the "preferred" algorithm must be used with the <OrgID> set to CIM.

    
.. _LMI-SoftwareInstallationService-CommunicationStatus:

``uint16`` **CommunicationStatus**

    CommunicationStatus indicates the ability of the instrumentation to communicate with the underlying ManagedElement. CommunicationStatus consists of one of the following values: Unknown, None, Communication OK, Lost Communication, or No Contact. 

    A Null return indicates the implementation (provider) does not implement this property. 

    "Unknown" indicates the implementation is in general capable of returning this property, but is unable to do so at this time. 

    "Not Available" indicates that the implementation (provider) is capable of returning a value for this property, but not ever for this particular piece of hardware/software or the property is intentionally not used because it adds no meaningful information (as in the case of a property that is intended to add additional info to another property). 

    "Communication OK " indicates communication is established with the element, but does not convey any quality of service. 

    "No Contact" indicates that the monitoring system has knowledge of this element, but has never been able to establish communications with it. 

    "Lost Communication" indicates that the Managed Element is known to exist and has been contacted successfully in the past, but is currently unreachable.

    
    ======== ==================
    ValueMap Values            
    ======== ==================
    0        Unknown           
    1        Not Available     
    2        Communication OK  
    3        Lost Communication
    4        No Contact        
    ..       DMTF Reserved     
    0x8000.. Vendor Reserved   
    ======== ==================
    
.. _LMI-SoftwareInstallationService-SystemName:

``string`` **SystemName**

    The Name of the scoping System.

    
.. _LMI-SoftwareInstallationService-DetailedStatus:

``uint16`` **DetailedStatus**

    DetailedStatus compliments PrimaryStatus with additional status detail. It consists of one of the following values: Not Available, No Additional Information, Stressed, Predictive Failure, Error, Non-Recoverable Error, SupportingEntityInError. Detailed status is used to expand upon the PrimaryStatus of the element. 

    A Null return indicates the implementation (provider) does not implement this property. 

    "Not Available" indicates that the implementation (provider) is capable of returning a value for this property, but not ever for this particular piece of hardware/software or the property is intentionally not used because it adds no meaningful information (as in the case of a property that is intended to add additional info to another property). 

    "No Additional Information" indicates that the element is functioning normally as indicated by PrimaryStatus = "OK". 

    "Stressed" indicates that the element is functioning, but needs attention. Examples of "Stressed" states are overload, overheated, and so on. 

    "Predictive Failure" indicates that an element is functioning normally but a failure is predicted in the near future. 

    "Non-Recoverable Error " indicates that this element is in an error condition that requires human intervention. 

    "Supporting Entity in Error" indicates that this element might be "OK" but that another element, on which it is dependent, is in error. An example is a network service or endpoint that cannot function due to lower-layer networking problems.

    
    ======== ==========================
    ValueMap Values                    
    ======== ==========================
    0        Not Available             
    1        No Additional Information 
    2        Stressed                  
    3        Predictive Failure        
    4        Non-Recoverable Error     
    5        Supporting Entity in Error
    ..       DMTF Reserved             
    0x8000.. Vendor Reserved           
    ======== ==========================
    
.. _LMI-SoftwareInstallationService-Description:

``string`` **Description**

    The Description property provides a textual description of the object.

    
.. _LMI-SoftwareInstallationService-TransitioningToState:

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
    
.. _LMI-SoftwareInstallationService-Started:

``boolean`` **Started**

    Started is a Boolean that indicates whether the Service has been started (TRUE), or stopped (FALSE).

    
.. _LMI-SoftwareInstallationService-Name:

``string`` **Name**

    The Name property uniquely identifies the Service and provides an indication of the functionality that is managed. This functionality is described in more detail in the Description property of the object.

    
.. _LMI-SoftwareInstallationService-EnabledDefault:

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
    
.. _LMI-SoftwareInstallationService-EnabledState:

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
    
.. _LMI-SoftwareInstallationService-Caption:

``string`` **Caption**

    The Caption property is a short textual description (one- line string) of the object.

    
.. _LMI-SoftwareInstallationService-PrimaryStatus:

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
    
.. _LMI-SoftwareInstallationService-OperationalStatus:

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
    
.. _LMI-SoftwareInstallationService-OperatingStatus:

``uint16`` **OperatingStatus**

    OperatingStatus provides a current status value for the operational condition of the element and can be used for providing more detail with respect to the value of EnabledState. It can also provide the transitional states when an element is transitioning from one state to another, such as when an element is transitioning between EnabledState and RequestedState, as well as other transitional conditions.

    OperatingStatus consists of one of the following values: Unknown, Not Available, In Service, Starting, Stopping, Stopped, Aborted, Dormant, Completed, Migrating, Emmigrating, Immigrating, Snapshotting. Shutting Down, In Test 

    A Null return indicates the implementation (provider) does not implement this property. 

    "Unknown" indicates the implementation is in general capable of returning this property, but is unable to do so at this time. 

    "None" indicates that the implementation (provider) is capable of returning a value for this property, but not ever for this particular piece of hardware/software or the property is intentionally not used because it adds no meaningful information (as in the case of a property that is intended to add additional info to another property). 

    "Servicing" describes an element being configured, maintained, cleaned, or otherwise administered. 

    "Starting" describes an element being initialized. 

    "Stopping" describes an element being brought to an orderly stop. 

    "Stopped" and "Aborted" are similar, although the former implies a clean and orderly stop, while the latter implies an abrupt stop where the state and configuration of the element might need to be updated. 

    "Dormant" indicates that the element is inactive or quiesced. 

    "Completed" indicates that the element has completed its operation. This value should be combined with either OK, Error, or Degraded in the PrimaryStatus so that a client can tell if the complete operation Completed with OK (passed), Completed with Error (failed), or Completed with Degraded (the operation finished, but it did not complete OK or did not report an error). 

    "Migrating" element is being moved between host elements. 

    "Immigrating" element is being moved to new host element. 

    "Emigrating" element is being moved away from host element. 

    "Shutting Down" describes an element being brought to an abrupt stop. 

    "In Test" element is performing test functions. 

    "Transitioning" describes an element that is between states, that is, it is not fully available in either its previous state or its next state. This value should be used if other values indicating a transition to a specific state are not applicable.

    "In Service" describes an element that is in service and operational.

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    0        Unknown        
    1        Not Available  
    2        Servicing      
    3        Starting       
    4        Stopping       
    5        Stopped        
    6        Aborted        
    7        Dormant        
    8        Completed      
    9        Migrating      
    10       Emigrating     
    11       Immigrating    
    12       Snapshotting   
    13       Shutting Down  
    14       In Test        
    15       Transitioning  
    16       In Service     
    ..       DMTF Reserved  
    0x8000.. Vendor Reserved
    ======== ===============
    
.. _LMI-SoftwareInstallationService-SystemCreationClassName:

``string`` **SystemCreationClassName**

    The CreationClassName of the scoping System.

    
.. _LMI-SoftwareInstallationService-CreationClassName:

``string`` **CreationClassName**

    CreationClassName indicates the name of the class or the subclass that is used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

    

Local methods
^^^^^^^^^^^^^

    .. _LMI-SoftwareInstallationService-InstallFromURI:

``uint32`` **InstallFromURI** (:ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, ``string`` URI, :ref:`CIM_ManagedElement <CIM-ManagedElement>` Target, ``uint16[]`` InstallOptions, ``string[]`` InstallOptionsValues)

    Start a job to install software from a specific URI in a ManagedElement. 

    Note that this method is provided to support existing, alternative download mechanisms (such as used for firmware download). The 'normal' mechanism will be to use the InstallFromSoftwareIdentity method.

    If 0 is returned, the function completed successfully and no ConcreteJob instance was required. If 4096/0x1000 is returned, a ConcreteJob will be started to to perform the install. The Job's reference will be returned in the output parameter Job.

    
    ============ =============================================
    ValueMap     Values                                       
    ============ =============================================
    0            Job Completed with No Error                  
    1            Not Supported                                
    2            Unspecified Error                            
    3            Timeout                                      
    4            Failed                                       
    5            Invalid Parameter                            
    6            Target In Use                                
    ..           DMTF Reserved                                
    4096         Method Parameters Checked - Job Started      
    4097         Unsupported TargetType                       
    4098         Unattended/silent installation not supported 
    4099         Downgrade/reinstall not supported            
    4100         Not enough memory                            
    4101         Not enough swap-space                        
    4102         Unsupported version transition               
    4103         Not enough disk space                        
    4104         Software and target operating system mismatch
    4105         Missing dependencies                         
    4106         Not applicable to target                     
    4107         URI not accessible                           
    4108..32767  Method Reserved                              
    32768..65535 Vendor Specific                              
    ============ =============================================
    
    **Parameters**
    
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *IN* ``string`` **URI**
            A URI for the software based on RFC 2079.

            
        
        *IN* :ref:`CIM_ManagedElement <CIM-ManagedElement>` **Target**
            The installation target.

            
        
        *IN* ``uint16[]`` **InstallOptions**
            Options to control the install process. 

            See the InstallOptions parameter of the SoftwareInstallationService.InstallFromSoftwareIdentity method for the description of these values.

            
            ============ =========================
            ValueMap     Values                   
            ============ =========================
            2            Defer target/system reset
            3            Force installation       
            4            Install                  
            5            Update                   
            6            Repair                   
            7            Reboot                   
            8            Password                 
            9            Uninstall                
            10           Log                      
            11           SilentMode               
            12           AdministrativeMode       
            13           ScheduleInstallAt        
            ..           DMTF Reserved            
            32768..65535 Vendor Specific          
            ============ =========================
            
        
        *IN* ``string[]`` **InstallOptionsValues**
            InstallOptionsValues is an array of strings providing additionalinformation to InstallOptions for the method to install the software. Each entry of this array is related to the entry in InstallOptions that is located at the same index providing additional information for InstallOptions. 

            For further information on the use of InstallOptionsValues parameter, see the description of the InstallOptionsValues parameter of the SoftwareInstallationService.InstallFromSoftwareIdentity method.

            
        
    
    .. _LMI-SoftwareInstallationService-CheckSoftwareIdentity:

``uint32`` **CheckSoftwareIdentity** (:ref:`CIM_SoftwareIdentity <CIM-SoftwareIdentity>` Source, :ref:`CIM_ManagedElement <CIM-ManagedElement>` Target, :ref:`CIM_Collection <CIM-Collection>` Collection, ``uint16[]`` InstallCharacteristics)

    This method allows a client application to determine whether a specific SoftwareIdentity can be installed (or updated) on a ManagedElement. It also allows other characteristics to be determined such as whether install will require a reboot. In addition a client can check whether the SoftwareIdentity can be added simulataneously to a specified SofwareIndentityCollection. A client MAY specify either or both of the Collection and Target parameters. The Collection parameter is only supported if SoftwareInstallationServiceCapabilities.CanAddToCollection is TRUE.

    
    ============ =============================================
    ValueMap     Values                                       
    ============ =============================================
    0            Job Completed with No Error                  
    1            Not Supported                                
    2            Unspecified Error                            
    3            Timeout                                      
    4            Failed                                       
    5            Invalid Parameter                            
    6            Target In Use                                
    ..           DMTF Reserved                                
    4096         Method Reserved                              
    4097         Unsupported TargetType                       
    4098         Unattended/silent installation not supported 
    4099         Downgrade/reinstall not supported            
    4100         Not enough memory                            
    4101         Not enough swap-space                        
    4102         Unsupported version transition               
    4103         Not enough disk space                        
    4104         Software and target operating system mismatch
    4105         Missing dependencies                         
    4106         Not applicable to target                     
    4107         No supported path to image                   
    4108         Cannot add to Collection                     
    4109         Asynchronous Job already in progress         
    4110..32767  Method Reserved                              
    32768..65535 Vendor Specific                              
    ============ =============================================
    
    **Parameters**
    
        *IN* :ref:`CIM_SoftwareIdentity <CIM-SoftwareIdentity>` **Source**
            Reference to the SoftwareIdentity to be checked.

            
        
        *IN* :ref:`CIM_ManagedElement <CIM-ManagedElement>` **Target**
            Reference to the ManagedElement that the Software Identity is going to be installed in (or updated).

            
        
        *IN* :ref:`CIM_Collection <CIM-Collection>` **Collection**
            Reference to the Collection to which the Software Identity will be added.

            
        
        *OUT* ``uint16[]`` **InstallCharacteristics**
            The parameter describes the characteristics of the installation/update that will take place if the Source Software Identity is installed: 

            Target automatic reset: The target element will automatically reset once the installation is complete. 

            System automatic reset: The containing system of the target ManagedElement (normally a logical device or the system itself) will automatically reset/reboot once the installation is complete. 

            Separate target reset required: EnabledLogicalElement.RequestStateChange MUST be used to reset the target element after the SoftwareIdentity is installed. 

            Separate system reset required: EnabledLogicalElement.RequestStateChange MUST be used to reset/reboot the containing system of the target ManagedElement after the SoftwareIdentity is installed. 

            Manual Reboot Required: The system MUST be manually rebooted by the user. 

            No reboot required : No reboot is required after installation. 

            User Intervention Recomended : It is recommended that a user confirm installation of this SoftwareIdentity. Inappropriate application MAY have serious consequences. 

            MAY be added to specified collection : The SoftwareIndentity MAY be added to specified Collection.

            
            ============== ====================================
            ValueMap       Values                              
            ============== ====================================
            2              Target automatic reset              
            3              System automatic reset              
            4              Separate target reset Required      
            5              Separate system reset Required      
            6              Manual Reboot Required              
            7              No Reboot Required                  
            8              User Intervention recommended       
            9              MAY be added to specified Collection
            ..             DMTF Reserved                       
            0x7FFF..0xFFFF Vendor Specific                     
            ============== ====================================
            
        
    
    .. _LMI-SoftwareInstallationService-FindIdentity:

``uint32`` **FindIdentity** (``string`` Name, ``uint32`` Epoch, ``string`` Version, ``string`` Release, ``string`` Architecture, :ref:`LMI_SoftwareIdentityResource <LMI-SoftwareIdentityResource>` Repository, ``boolean`` AllowDuplicates, ``boolean`` ExactMatch, ``boolean`` Installed, :ref:`LMI_SoftwareIdentity[] <LMI-SoftwareIdentity>` Matches)

    Search for installed or available software identity matching specified properties. In case "Repository" is given, only available packages of this repository will be browsed. "AllowDuplicates" causes, that packages of the name <name>.<arch> will be listed multiple times if more versions are available. Other input parameters with non-NULL values are compared to corresponding properties of LMI_SoftwareIdentity instances. 0 is returned if any matching package is found, 1 otherwise.

    
    **Parameters**
    
        *IN* ``string`` **Name**
            
        
        *IN* ``uint32`` **Epoch**
            
        
        *IN* ``string`` **Version**
            
        
        *IN* ``string`` **Release**
            
        
        *IN* ``string`` **Architecture**
            
        
        *IN* :ref:`LMI_SoftwareIdentityResource <LMI-SoftwareIdentityResource>` **Repository**
            Allows to specify particular software repository, where the search shall take place. If given, only available packages will be browsed.

            Using this parameter in conjunction with "Installed" parameter makes perfect sense. Just those packages available in given repository and installed at the same time will be queried in case of "Installed=True". And just those available and not installed at the same time will be queried in case of "Installed=False".

            
        
        *IN* ``boolean`` **AllowDuplicates**
            Whether the different versions of the same package shall be included in result. This defaults to "False".

            
        
        *IN* ``boolean`` **ExactMatch**
            Whether to compare "Name" for exact match. If "False", package name and its summary string ("Caption") will be searched for occurences of "Name" parameter's value. Defaults to "False".

            
        
        *IN* ``boolean`` **Installed**
            Limit the query just to installed packages by setting this paramater to True. Or make it search just not installed ones by setting it to False. All packages will be queried by default.

            
        
        *OUT* :ref:`LMI_SoftwareIdentity[] <LMI-SoftwareIdentity>` **Matches**
            All matching packages found shall be available in this parameter.

            
        
    
    .. _LMI-SoftwareInstallationService-InstallFromSoftwareIdentity:

``uint32`` **InstallFromSoftwareIdentity** (:ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, ``uint16[]`` InstallOptions, ``string[]`` InstallOptionsValues, :ref:`CIM_SoftwareIdentity <CIM-SoftwareIdentity>` Source, :ref:`CIM_ManagedElement <CIM-ManagedElement>` Target, :ref:`CIM_Collection <CIM-Collection>` Collection)

    Start a job to install or update a SoftwareIdentity (Source) on a ManagedElement (Target). 

    In addition the method can be used to add the SoftwareIdentity simulataneously to a specified SofwareIndentityCollection. A client MAY specify either or both of the Collection and Target parameters. The Collection parameter is only supported if SoftwareInstallationService.CanAddToCollection is TRUE. 

    If 0 is returned, the function completed successfully and no ConcreteJob instance was required. If 4096/0x1000 is returned, a ConcreteJob will be started to perform the install. The Job's reference will be returned in the output parameter Job.

    
    ============ =============================================
    ValueMap     Values                                       
    ============ =============================================
    0            Job Completed with No Error                  
    1            Not Supported                                
    2            Unspecified Error                            
    3            Timeout                                      
    4            Failed                                       
    5            Invalid Parameter                            
    6            Target In Use                                
    ..           DMTF Reserved                                
    4096         Method Parameters Checked - Job Started      
    4097         Unsupported TargetType                       
    4098         Unattended/silent installation not supported 
    4099         Downgrade/reinstall not supported            
    4100         Not enough memory                            
    4101         Not enough swap-space                        
    4102         Unsupported version transition               
    4103         Not enough disk space                        
    4104         Software and target operating system mismatch
    4105         Missing dependencies                         
    4106         Not applicable to target                     
    4107         No supported path to image                   
    4108         Cannot add to Collection                     
    4109..32767  Method Reserved                              
    32768..65535 Vendor Specific                              
    ============ =============================================
    
    **Parameters**
    
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *IN* ``uint16[]`` **InstallOptions**
            Options to control the install process.

            Defer target/system reset : do not automatically reset the target/system.

            Force installation : Force the installation of the same or an older SoftwareIdentity. Install: Perform an installation of this software on the managed element.

            Update: Perform an update of this software on the managed element.

            Repair: Perform a repair of the installation of this software on the managed element by forcing all the files required for installing the software to be reinstalled.

            Reboot: Reboot or reset the system immediately after the install or update of this software, if the install or the update requires a reboot or reset.

            Password: Password will be specified as clear text without any encryption for performing the install or update.

            Uninstall: Uninstall the software on the managed element.

            Log: Create a log for the install or update of the software.

            SilentMode: Perform the install or update without displaying any user interface.

            AdministrativeMode: Perform the install or update of the software in the administrative mode. ScheduleInstallAt: Indicates the time at which theinstall or update of the software will occur.

            
            ============ =========================
            ValueMap     Values                   
            ============ =========================
            2            Defer target/system reset
            3            Force installation       
            4            Install                  
            5            Update                   
            6            Repair                   
            7            Reboot                   
            8            Password                 
            9            Uninstall                
            10           Log                      
            11           SilentMode               
            12           AdministrativeMode       
            13           ScheduleInstallAt        
            ..           DMTF Reserved            
            32768..65535 Vendor Specific          
            ============ =========================
            
        
        *IN* ``string[]`` **InstallOptionsValues**
            InstallOptionsValues is an array of strings providing additional information to InstallOptions for the method to install the software. Each entry of this array is related to the entry in InstallOptions that is located at the same index providing additional information for InstallOptions. 

            If the index in InstallOptions has the value "Password " then a value at the corresponding index of InstallOptionValues shall not be NULL. 

            If the index in InstallOptions has the value "ScheduleInstallAt" then the value at the corresponding index of InstallOptionValues shall not be NULL and shall be in the datetime type format. 

            If the index in InstallOptions has the value "Log " then a value at the corresponding index of InstallOptionValues may be NULL. 

            If the index in InstallOptions has the value "Defer target/system reset", "Force installation","Install", "Update", "Repair" or "Reboot" then a value at the corresponding index of InstallOptionValues shall be NULL.

            
        
        *IN* :ref:`CIM_SoftwareIdentity <CIM-SoftwareIdentity>` **Source**
            Reference to the source of the install.

            
        
        *IN* :ref:`CIM_ManagedElement <CIM-ManagedElement>` **Target**
            The installation target. If NULL then the SOftwareIdentity will be added to Collection only. The underlying implementation is expected to be able to obtain any necessary metadata from the Software Identity.

            
        
        *IN* :ref:`CIM_Collection <CIM-Collection>` **Collection**
            Reference to the Collection to which the Software Identity SHALL be added. If NULL then the Software Identity will not be added to a Collection.

            
        
    
    .. _LMI-SoftwareInstallationService-VerifyInstalledIdentity:

``uint32`` **VerifyInstalledIdentity** (:ref:`CIM_SoftwareIdentity <CIM-SoftwareIdentity>` Source, :ref:`CIM_ManagedElement <CIM-ManagedElement>` Target, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`LMI_SoftwareIdentityFileCheck[] <LMI-SoftwareIdentityFileCheck>` Failed)

    Start a job to verify installed package represented by SoftwareIdentity (Source) on a ManagedElement (Target).

    If 0 is returned, the function completed successfully and no ConcreteJob instance was required. If 4096/0x1000 is returned, a ConcreteJob will be started to perform the verification. The Job's reference will be returned in the output parameter Job.

    In former case, the Failed parameterwill contain all associated file checks, that did not pass. In the latter case this property will be NULL.

    
    ============ =======================================
    ValueMap     Values                                 
    ============ =======================================
    0            Job Completed with No Error            
    1            Not Supported                          
    2            Unspecified Error                      
    3            Timeout                                
    4            Failed                                 
    5            Invalid Parameter                      
    6            Target In Use                          
    ..           DMTF Reserved                          
    4096         Method Parameters Checked - Job Started
    4097         Unsupported TargetType                 
    4098..32767  Method Reserved                        
    32768        Software Identity Not Installed        
    32769..65535 Vendor Specific                        
    ============ =======================================
    
    **Parameters**
    
        *IN* :ref:`CIM_SoftwareIdentity <CIM-SoftwareIdentity>` **Source**
            Reference to the installed SoftwareIdentity to be verified.

            
        
        *IN* :ref:`CIM_ManagedElement <CIM-ManagedElement>` **Target**
            Reference to the ManagedElement that the Software Identity is installed on.

            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *OUT* :ref:`LMI_SoftwareIdentityFileCheck[] <LMI-SoftwareIdentityFileCheck>` **Failed**
            Array of file checks that did not pass verification. This is NULL in case that asynchronous job has been started.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`LoSID <CIM-Service-LoSID>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string`` :ref:`LoSOrgID <CIM-Service-LoSOrgID>`
| ``string`` :ref:`StartMode <CIM-Service-StartMode>`
| ``string`` :ref:`PrimaryOwnerName <CIM-Service-PrimaryOwnerName>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``string`` :ref:`PrimaryOwnerContact <CIM-Service-PrimaryOwnerContact>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`
| :ref:`StopService <CIM-Service-StopService>`
| :ref:`ChangeAffectedElementsAssignedSequence <CIM-Service-ChangeAffectedElementsAssignedSequence>`
| :ref:`StartService <CIM-Service-StartService>`
| :ref:`InstallFromByteStream <CIM-SoftwareInstallationService-InstallFromByteStream>`

