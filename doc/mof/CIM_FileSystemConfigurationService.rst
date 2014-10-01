.. _CIM-FileSystemConfigurationService:

CIM_FileSystemConfigurationService
----------------------------------

Class reference
===============
Subclass of :ref:`CIM_Service <CIM-Service>`

This service allows the active management of a NAS Head or other FileSystem Server. It allows jobs to be started for the creation, modification, and deletion of FileSystems (that derive from CIM_LocalFileSystem).


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

    .. _CIM-FileSystemConfigurationService-ModifyFileSystem:

``uint32`` **ModifyFileSystem** (``string`` ElementName, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, ``string`` Goal, :ref:`CIM_FileSystem <CIM-FileSystem>` TheElement, ``uint16`` InUseOptions, ``uint32`` WaitTime)

    Start a job to modify a previously created FileSystem. If the operation completes successfully and did not require a long-running ConcreteJob, it will return 0. If 4096/0x1000 is returned, a ConcreteJob will be started to modify the element. A Reference to the ConcreteJob will be returned in the output parameter Job. If any other value is returned, either the job will not be started, or if started, no action will be taken. 

    This method MUST return a CIM_Error representing that a single named property of a setting (or other) parameter (either reference or embedded object) has an invalid value or that an invalid combination of named properties of a setting (or other) parameter (either reference or embedded object) has been requested. 

    The parameter TheElement specifies the FileSystem to be modified. This element MUST be associated via ElementSettingData with a FileSystemSetting which is in turn associated via SettingGeneratedByCapabilities to a FileSystemCapabilities supported by this FileSystemConfigurationService. 

    The desired settings for the FileSystem are specified by the Goal parameter. Goal is an element of class CIM_FileSystemSetting, or a derived class, encoded as a string-valued embedded instance parameter; this allows the client to specify the properties desired for the file system. The Goal parameter includes information that can be used by the vendor to compute the required size of the FileSystem. If the operation would result in a change in the size of the file system, the StorageExtent identified by the ResidesOnExtent association will be used to determine how to implement the change. If the StorageExtent cannot be expanded to support the goal size, an appropriate error value will be returned, and no action will be taken. If the operation succeeds, the ResidesOnExtent association might reference a different StorageExtent.

    
    ============ =======================================
    ValueMap     Values                                 
    ============ =======================================
    0            Job Completed with No Error            
    1            Not Supported                          
    2            Unknown                                
    3            Timeout                                
    4            Failed                                 
    5            Invalid Parameter                      
    6            FileSystem In Use, cannot Modify       
    7            Cannot satisfy new Goal.               
    ..           DMTF Reserved                          
    4096         Method Parameters Checked - Job Started
    4098..32767  Method Reserved                        
    32768..65535 Vendor Specific                        
    ============ =======================================
    
    **Parameters**
    
        *IN* ``string`` **ElementName**
            A end user relevant name for the FileSystem being modified. If NULL, then the name will not be changed. If not NULL, this parameter will supply a new name for the FileSystem element.

            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *IN* ``string`` **Goal**
            The requirements for the FileSystem element to maintain. This is an element of class CIM_FileSystemSetting, or a derived class, encoded as a string-valued embedded instance parameter; this allows the client to specify the properties desired for the file system. If NULL or the empty string, the FileSystem service attributes will not be changed. If not NULL, this parameter will supply new settings that replace or are merged with the current settings of the FileSystem element.

            
        
        *IN* :ref:`CIM_FileSystem <CIM-FileSystem>` **TheElement**
            The FileSystem element to modify.

            
        
        *IN* ``uint16`` **InUseOptions**
            An enumerated integer that specifies the action to take if the FileSystem is still in use when this request is made. This option is only relevant if the FileSystem must be made unavailable while the request is being executed.

            
            ============== ===================================================================
            ValueMap       Values                                                             
            ============== ===================================================================
            2              Do Not Execute Request                                             
            3              Wait for specified time, then Execute Request Immediately          
            4              Try to Quiesce for specified time, then Execute Request Immediately
            ..             DMTF Reserved                                                      
            0x1000..0xFFFF Vendor Defined                                                     
            ============== ===================================================================
            
        
        *IN* ``uint32`` **WaitTime**
            An integer that indicates the time (in seconds) that the provider must wait before performing the request on this FileSystem. If WaitTime is not zero, the method will create a job, if supported by the provider, and return immediately. If the provider does not support asynchronous jobs, there is a possibility that the client could time-out before the job is completed. 

            The combination of InUseOptions = '4' and WaitTime ='0' (the default) is interpreted as 'Wait (forever) until Quiescence, then Execute Request' and will be performed asynchronously if possible.

            
        
    
    .. _CIM-FileSystemConfigurationService-DeleteFileSystem:

``uint32`` **DeleteFileSystem** (:ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`CIM_ManagedElement <CIM-ManagedElement>` TheFileSystem, ``uint16`` InUseOptions, ``uint32`` WaitTime)

    Start a job to delete a FileSystem. If the FileSystem cannot be deleted, no action will be taken, and the Return Value will be 4097/0x1001. If the method completed successfully and did not require a long-running ConcreteJob, it will return 0. If 4096/0x1000 is returned, a ConcreteJob will be started to delete the FileSystem. A Reference to the ConcreteJob will be returned in the output parameter Job.

    
    ============== =======================================
    ValueMap       Values                                 
    ============== =======================================
    0              Job Completed with No Error            
    1              Not Supported                          
    2              Unknown                                
    3              Timeout                                
    4              Failed, Unspecified Reasons            
    5              Invalid Parameter                      
    6              FileSystem in use, Failed              
    ..             DMTF Reserved                          
    0x1000         Method Parameters Checked - Job Started
    0x1001..0x7FFF Method Reserved                        
    0x8000..       Vendor Specific                        
    ============== =======================================
    
    **Parameters**
    
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *IN* :ref:`CIM_ManagedElement <CIM-ManagedElement>` **TheFileSystem**
            An element or association that uniquely identifies the FileSystem to be deleted.

            
        
        *IN* ``uint16`` **InUseOptions**
            An enumerated integer that specifies the action to take if the FileSystem is still in use when this request is made.

            
            ============== ==============================================================
            ValueMap       Values                                                        
            ============== ==============================================================
            2              Do Not Delete                                                 
            3              Wait for specified time, then Delete Immediately              
            4              Attempt Quiescence for specified time, then Delete Immediately
            ..             DMTF Reserved                                                 
            0x1000..0xFFFF Vendor Defined                                                
            ============== ==============================================================
            
        
        *IN* ``uint32`` **WaitTime**
            An integer that indicates the time (in seconds) that the provider must wait before deleting this FileSystem. If WaitTime is not zero, the method will create a job, if supported by the provider, and return immediately. If the provider does not support asynchronous jobs, there is a possibility that the client could time-out before the job is completed. 

            The combination of InUseOptions = '4' and WaitTime ='0' (the default) is interpreted as 'Wait (forever) until Quiescence, then Delete Filesystem' and will be performed asynchronously if possible.

            
        
    
    .. _CIM-FileSystemConfigurationService-CreateFileSystem:

``uint32`` **CreateFileSystem** (``string`` ElementName, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, ``string`` Goal, :ref:`CIM_StorageExtent <CIM-StorageExtent>` InExtent, :ref:`CIM_FileSystem <CIM-FileSystem>` TheElement)

    Start a job to create a FileSystem on a StorageExtent. If the operation completes successfully and did not require a long-running ConcreteJob, it will return 0. If 4096/0x1000 is returned, a ConcreteJob will be started to create the element. A Reference to the ConcreteJob will be returned in the output parameter Job. If any other value is returned, the job will not be started, and no action will be taken. 

    This method MUST return a CIM_Error representing that a single named property of a setting (or other) parameter (either reference or embedded object) has an invalid value or that an invalid combination of named properties of a setting (or other) parameter (either reference or embedded object) has been requested. 

    The parameter TheElement will contain a Reference to the FileSystem if this operation completed successfully. 

    The StorageExtent to use is specified by the InExtent parameter. If this is NULL, a default StorageExtent will be created in a vendor-specific way and used. One way to create the default StorageExtent is to use one of the canned settings supported by the StorageConfigurationService hosted by the host hosting the FileSystemConfigurationService. 

    The desired settings for the FileSystem are specified by the Goal parameter. Goal is an element of class CIM_FileSystemSetting, or a derived class, encoded as a string-valued embedded object parameter; this allows the client to specify the properties desired for the file system. The Goal parameter includes information that can be used by the vendor to compute the size of the FileSystem. If the StorageExtent specified here cannot support the goal size, an appropriate error value will be returned, and no action will be taken. 

    A ResidesOnExtent association is created between the created FileSystem and the StorageExtent used for it.

    
    ============ =======================================================
    ValueMap     Values                                                 
    ============ =======================================================
    0            Job Completed with No Error                            
    1            Not Supported                                          
    2            Unknown                                                
    3            Timeout                                                
    4            Failed                                                 
    5            Invalid Parameter                                      
    6            StorageExtent is not big enough to satisfy the request.
    7            StorageExtent specified by default cannot be created.  
    ..           DMTF Reserved                                          
    4096         Method Parameters Checked - Job Started                
    4098..32767  Method Reserved                                        
    32768..65535 Vendor Specific                                        
    ============ =======================================================
    
    **Parameters**
    
        *IN* ``string`` **ElementName**
            A end user relevant name for the FileSystem being created. If NULL, a system-supplied default name can be used. The value will be stored in the 'ElementName' property for the created element.

            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *IN* ``string`` **Goal**
            The requirements for the FileSystem element to maintain. This is an element of class CIM_FileSystemSetting, or a derived class, encoded as a string-valued embedded instance parameter; this allows the client to specify the properties desired for the file system. If NULL or the empty string, the FileSystemConfigurationService will use a vendor-specific default Goal obtained by using the FileSystemCapabilities element specified by the DefaultElementCapabilities association to obtain a default FileSystemSetting element.

            
        
        *IN* :ref:`CIM_StorageExtent <CIM-StorageExtent>` **InExtent**
            The StorageExtent on which the created FileSystem will reside. If this is NULL, a default StorageExtent will be created in a vendor-specific way and used. One way to create the default StorageExtent is to use one of the default settings supported by the StorageConfigurationService on the same hosting ComputerSystem as the FileSystemConfigurationService.

            
        
        *IN*, *OUT* :ref:`CIM_FileSystem <CIM-FileSystem>` **TheElement**
            The newly created FileSystem.

            
        
    

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

