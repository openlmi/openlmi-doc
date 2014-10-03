.. _LMI-FileSystemConfigurationService:

LMI_FileSystemConfigurationService
----------------------------------

Class reference
===============
Subclass of :ref:`CIM_FileSystemConfigurationService <CIM-FileSystemConfigurationService>`

This service allows the active management of a NAS Head or other FileSystem Server. It allows jobs to be started for the creation, modification, and deletion of FileSystems (that derive from CIM_LocalFileSystem).


Key properties
^^^^^^^^^^^^^^

| :ref:`Name <CIM-Service-Name>`
| :ref:`SystemName <CIM-Service-SystemName>`
| :ref:`SystemCreationClassName <CIM-Service-SystemCreationClassName>`
| :ref:`CreationClassName <CIM-Service-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-FileSystemConfigurationService-HealthState:

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
    
.. _LMI-FileSystemConfigurationService-Started:

``boolean`` **Started**

    Started is a Boolean that indicates whether the Service has been started (TRUE), or stopped (FALSE).

    
.. _LMI-FileSystemConfigurationService-PrimaryStatus:

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
    
.. _LMI-FileSystemConfigurationService-EnabledDefault:

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
    
.. _LMI-FileSystemConfigurationService-EnabledState:

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
    
.. _LMI-FileSystemConfigurationService-StartMode:

``string`` **StartMode**

    Note: The use of this element is deprecated in lieu of the EnabledDefault property that is inherited from EnabledLogicalElement. The EnabledLogicalElement addresses the same semantics. The change to a uint16 data type was discussed when CIM V2.0 was defined. However, existing V1.0 implementations used the string property. To remain compatible with those implementations, StartMode was grandfathered into the schema. Use of the deprecated qualifier allows the maintenance of the existing property but also permits an improved, clarified definition using EnabledDefault. 

    Deprecated description: StartMode is a string value that indicates whether the Service is automatically started by a System, an Operating System, and so on, or is started only upon request.

    
.. _LMI-FileSystemConfigurationService-OperationalStatus:

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

    .. _LMI-FileSystemConfigurationService-LMI-CreateFileSystem:

``uint32`` **LMI_CreateFileSystem** (``uint16`` FileSystemType, ``string`` ElementName, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`CIM_FileSystemSetting <CIM-FileSystemSetting>` Goal, :ref:`CIM_StorageExtent[] <CIM-StorageExtent>` InExtents, :ref:`CIM_FileSystem <CIM-FileSystem>` TheElement)

    Start a job to create a FileSystem on StorageExtents. If the operation completes successfully and did not require a long-running ConcreteJob, it will return 0. If 4096/0x1000 is returned, a ConcreteJob will be started to create the element. A Reference to the ConcreteJob will be returned in the output parameter Job. If any other value is returned, the job will not be started, and no action will be taken.

    The parameter TheElement will contain a Reference to the FileSystem if this operation completed successfully.

    The StorageExtents to use is specified by the InExtents parameter.

    The desired settings for the FileSystem are specified by the Goal parameter. Goal is an element of class CIM_FileSystemSetting, or a derived class. Unlike CIM standard CreateFileSystem, the parameter is reference to CIM_FileSystemSetting stored on the CIMOM.

    A ResidesOnExtent association is created between the created FileSystem and the StorageExtents used for it.

    
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
    
        *IN* ``uint16`` **FileSystemType**
            Type of file system to create. When NULL, file system type is retrieved from Goal parameter, which cannot be NULL.

            
            ======== =============
            ValueMap Values       
            ======== =============
            0        Unknown      
            2        UFS          
            3        HFS          
            4        FAT          
            5        FAT16        
            6        FAT32        
            7        NTFS4        
            8        NTFS5        
            9        XFS          
            10       AFS          
            11       EXT2         
            12       EXT3         
            13       REISERFS     
            ..       DMTF Reserved
            32769    EXT4         
            32770    BTRFS        
            32771    JFS          
            32772    TMPFS        
            32773    VFAT         
            ======== =============
            
        
        *IN* ``string`` **ElementName**
            Label of the filesystem being created. If NULL, a system-supplied default name can be used. The value will be stored in the 'ElementName' property for the created element.

            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *IN* :ref:`CIM_FileSystemSetting <CIM-FileSystemSetting>` **Goal**
            The requirements for the FileSystem element to maintain. This is an element of class CIM_FileSystemSetting, or a derived class. This allows the client to specify the properties desired for the file system. If NULL, the FileSystemConfigurationService will create default filesystem.

            
        
        *IN* :ref:`CIM_StorageExtent[] <CIM-StorageExtent>` **InExtents**
            The StorageExtents on which the created FileSystem will reside. At least one extent must be provided. If the filesystem being created supports more than one storage extent (e.g. btrfs), more extents can be provided. The filesystem will then reside on all of them.

            
        
        *OUT* :ref:`CIM_FileSystem <CIM-FileSystem>` **TheElement**
            The newly created FileSystem.

            
        
    
    .. _LMI-FileSystemConfigurationService-DeleteFileSystem:

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

            This option is not supported by OpenLMI.

            
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

            This option is not supported by OpenLMI.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`SystemName <CIM-Service-SystemName>`
| ``string`` :ref:`LoSID <CIM-Service-LoSID>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`Name <CIM-Service-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string`` :ref:`LoSOrgID <CIM-Service-LoSOrgID>`
| ``string`` :ref:`PrimaryOwnerContact <CIM-Service-PrimaryOwnerContact>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`SystemCreationClassName <CIM-Service-SystemCreationClassName>`
| ``string`` :ref:`CreationClassName <CIM-Service-CreationClassName>`
| ``string`` :ref:`PrimaryOwnerName <CIM-Service-PrimaryOwnerName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`
| :ref:`StopService <CIM-Service-StopService>`
| :ref:`ModifyFileSystem <CIM-FileSystemConfigurationService-ModifyFileSystem>`
| :ref:`ChangeAffectedElementsAssignedSequence <CIM-Service-ChangeAffectedElementsAssignedSequence>`
| :ref:`StartService <CIM-Service-StartService>`
| :ref:`CreateFileSystem <CIM-FileSystemConfigurationService-CreateFileSystem>`

