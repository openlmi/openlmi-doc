.. _CIM-SoftwareInstallationService:

CIM_SoftwareInstallationService
-------------------------------

Class reference
===============
Subclass of :ref:`CIM_Service <CIM-Service>`

A subclass of service which provides methods to install (or update) Software Identities in ManagedElements.


Key properties
^^^^^^^^^^^^^^

| :ref:`Name <CIM-Service-Name>`
| :ref:`SystemName <CIM-Service-SystemName>`
| :ref:`SystemCreationClassName <CIM-Service-SystemCreationClassName>`
| :ref:`CreationClassName <CIM-Service-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

*None*

Local methods
^^^^^^^^^^^^^

    .. _CIM-SoftwareInstallationService-InstallFromURI:

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

            
        
    
    .. _CIM-SoftwareInstallationService-CheckSoftwareIdentity:

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
            
        
    
    .. _CIM-SoftwareInstallationService-InstallFromSoftwareIdentity:

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
            Reference to the Collection to which the Software Identity SHALL be added. If NULL then the SOftware Identity will not be added to a Collection.

            
        
    
    .. _CIM-SoftwareInstallationService-InstallFromByteStream:

``uint32`` **InstallFromByteStream** (:ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, ``uint8[]`` Image, :ref:`CIM_ManagedElement <CIM-ManagedElement>` Target, ``uint16[]`` InstallOptions, ``string[]`` InstallOptionsValues)

    Start a job to download a series of bytes containing a software image to a ManagedElement. 

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
    4107         No supported path to image                   
    4108..32767  Method Reserved                              
    32768..65535 Vendor Specific                              
    ============ =============================================
    
    **Parameters**
    
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *IN* ``uint8[]`` **Image**
            A array of bytes containing the install image.

            
        
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
            InstallOptionsValues is an array of strings providing additional information to InstallOptions for the method to install the software. Each entry of this array is related to the entry in InstallOptions that is located at the same index providing additional information for InstallOptions. 

            

            For further information on the use of InstallOptionsValues parameter, see the description of the InstallOptionsValues parameter of the SoftwareInstallationService.InstallFromSoftwareIdentity method.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`SystemName <CIM-Service-SystemName>`
| ``string`` :ref:`LoSID <CIM-Service-LoSID>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``boolean`` :ref:`Started <CIM-Service-Started>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`Name <CIM-Service-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``string`` :ref:`LoSOrgID <CIM-Service-LoSOrgID>`
| ``string`` :ref:`PrimaryOwnerContact <CIM-Service-PrimaryOwnerContact>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`StartMode <CIM-Service-StartMode>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`SystemCreationClassName <CIM-Service-SystemCreationClassName>`
| ``string`` :ref:`CreationClassName <CIM-Service-CreationClassName>`
| ``string`` :ref:`PrimaryOwnerName <CIM-Service-PrimaryOwnerName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`
| :ref:`StopService <CIM-Service-StopService>`
| :ref:`ChangeAffectedElementsAssignedSequence <CIM-Service-ChangeAffectedElementsAssignedSequence>`
| :ref:`StartService <CIM-Service-StartService>`

