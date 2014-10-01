.. _LMI-MountConfigurationService:

LMI_MountConfigurationService
-----------------------------

Class reference
===============
Subclass of :ref:`CIM_Service <CIM-Service>`

This service has methods to create, delete and modify both persistent mounts (in /etc/fstab) and runtime mounts (mounted just now on running system).


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

    .. _LMI-MountConfigurationService-CreateMount:

``uint32`` **CreateMount** (:ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`LMI_MountedFileSystem <LMI-MountedFileSystem>` Mount, :ref:`CIM_FileSystem <CIM-FileSystem>` FileSystem, ``string`` MountPoint, ``string`` FileSystemSpec, ``string`` FileSystemType, :ref:`LMI_MountedFileSystemSetting <LMI-MountedFileSystemSetting>` Goal, ``uint16`` Mode)

    Mounts the specified filesystem to a mountpoint.

    
    ============ =======================================
    ValueMap     Values                                 
    ============ =======================================
    0            Job Completed with No Error            
    1            Not Supported                          
    2            Unknown                                
    3            Timeout                                
    4            Failed                                 
    5            Invalid Parameter                      
    6            In Use                                 
    ..           DMTF Reserved                          
    4096         Method Parameters Checked - Job Started
    4098..32767  Method Reserved                        
    32768..65535 Vendor Specific                        
    ============ =======================================
    
    **Parameters**
    
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the created job.

            
        
        *OUT* :ref:`LMI_MountedFileSystem <LMI-MountedFileSystem>` **Mount**
            Reference to the created LMI_MountedFileSystem instance.

            
        
        *IN* :ref:`CIM_FileSystem <CIM-FileSystem>` **FileSystem**
            Existing filesystem that should be mounted. If NULL, mount a remote filesystem, or mount a non-device filesystem (e.g. tmpfs). If not NULL, mount a local filesystem. When mounting a local filesystem, the FileSystemType parameter has to agree with the type of FileSystem.

            
        
        *IN* ``string`` **MountPoint**
            Directory where the mounted filesystem should be attached at.

            
        
        *IN* ``string`` **FileSystemSpec**
            Filesystem specification. Specifies the device that should be mounted. Remote filesystems can be specified in their usual form (e.g. 'hostname:/share' for NFS, or '//hostname/share' for CIFS). Non-device filesystems can also be specified (e.g. 'tmpfs' or 'sysfs'). When performing a bind mount, FileSystemSpec is the path to the source directory.

            
        
        *IN* ``string`` **FileSystemType**
            Filesystem type. If NULL, perform a binding mount. If mounting a local filesystem, this parameter has to be in agreement with the FileSystem.

            
        
        *IN* :ref:`LMI_MountedFileSystemSetting <LMI-MountedFileSystemSetting>` **Goal**
            Desired mount settings. If NULL, defaults will be used. Default mount options are 'rw, suid, dev, exec, auto, nouser, async'.

            
        
        *IN* ``uint16`` **Mode**
            The mode in which the configuration is to be applied to the MountedFileSystem.

            IsNext and IsCurrent are properties of LMI_MountedFileSystemElementSettingData, which will be created.

            Meaning of IsNext and IsCurrent is: 

            IsCurrent = 1: The filesystem will be mounted.

            IsNext = 1: A persistent entry will be created (in /etc/fstab). 

            Mode 1 - IsNext = 1, IsCurrent = 1.

            Mode 2 - IsNext = 1, IsCurrent not affected.

            Mode 32768 - IsNext not affected, IsCurrent = 1.

            
            ======== =============
            ValueMap Values       
            ======== =============
            0        Mode 0       
            1        Mode 1       
            2        Mode 2       
            3        Mode 3       
            4        Mode 4       
            5        Mode 5       
            6        Mode 6       
            ..       DMTF Reserved
            32768    Mode 32768   
            32769    Mode 32769   
            ======== =============
            
        
    
    .. _LMI-MountConfigurationService-DeleteMount:

``uint32`` **DeleteMount** (:ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`LMI_MountedFileSystem <LMI-MountedFileSystem>` Mount, ``uint16`` Mode)

    Unmounts an existing mount.

    
    ============ =======================================
    ValueMap     Values                                 
    ============ =======================================
    0            Job Completed with No Error            
    1            Not Supported                          
    2            Unknown                                
    3            Timeout                                
    4            Failed                                 
    5            Invalid Parameter                      
    6            In Use                                 
    ..           DMTF Reserved                          
    4096         Method Parameters Checked - Job Started
    4098..32767  Method Reserved                        
    32768..65535 Vendor Specific                        
    ============ =======================================
    
    **Parameters**
    
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the created job.

            
        
        *IN* :ref:`LMI_MountedFileSystem <LMI-MountedFileSystem>` **Mount**
            An existing mount.

            
        
        *IN* ``uint16`` **Mode**
            The mode in which the configuration is to be applied to the MountedFileSystem.

            IsNext and IsCurrent are properties of LMI_MountedFileSystemElementSettingData, which will be created.

            Meaning of IsNext and IsCurrent is: 

            IsCurrent = 1: The filesystem will be mounted.

            IsCurrent = 2: The filesystem will be unmounted.

            IsNext = 1: A persistent entry will be created (in /etc/fstab). 

            IsNext = 2: The persistent entry will be removed. 

            Mode 4 - IsNext = 2, IsCurrent = 2.

            Mode 5 - IsNext = 2, IsCurrent not affected.

            Mode 32769 - IsNext not affected, IsCurrent = 2.

            
            ======== =============
            ValueMap Values       
            ======== =============
            0        Mode 0       
            1        Mode 1       
            2        Mode 2       
            3        Mode 3       
            4        Mode 4       
            5        Mode 5       
            6        Mode 6       
            ..       DMTF Reserved
            32768    Mode 32768   
            32769    Mode 32769   
            ======== =============
            
        
    
    .. _LMI-MountConfigurationService-ModifyMount:

``uint32`` **ModifyMount** (:ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`LMI_MountedFileSystem <LMI-MountedFileSystem>` Mount, :ref:`LMI_MountedFileSystemSetting <LMI-MountedFileSystemSetting>` Goal, ``uint16`` Mode)

    Modifies (remounts) an existing mount.

    
    ============ =======================================
    ValueMap     Values                                 
    ============ =======================================
    0            Job Completed with No Error            
    1            Not Supported                          
    2            Unknown                                
    3            Timeout                                
    4            Failed                                 
    5            Invalid Parameter                      
    6            In Use                                 
    ..           DMTF Reserved                          
    4096         Method Parameters Checked - Job Started
    4098..32767  Method Reserved                        
    32768..65535 Vendor Specific                        
    ============ =======================================
    
    **Parameters**
    
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the created job.

            
        
        *IN*, *OUT* :ref:`LMI_MountedFileSystem <LMI-MountedFileSystem>` **Mount**
            Reference to the LMI_Mount instance that is being modified. 

            
        
        *IN* :ref:`LMI_MountedFileSystemSetting <LMI-MountedFileSystemSetting>` **Goal**
            Desired mount settings. If NULL, the mount options are not changed. If mount (or an fstab entry) should be performed (created), the appropriate respective MountedFileSystemSetting will be created.

            
        
        *IN* ``uint16`` **Mode**
            The mode in which the configuration is to be applied to the MountedFileSystem.

            IsNext and IsCurrent are properties of LMI_MountedFileSystemElementSettingData, which will be created.

            Meaning of IsNext and IsCurrent is: 

            IsCurrent = 1: The filesystem will be mounted.

            IsCurrent = 2: The filesystem will be unmounted.

            IsNext = 1: A persistent entry will be created (in /etc/fstab). 

            IsNext = 2: The persistent entry will be removed. 

            Mode 1 - IsNext = 1, IsCurrent = 1.

            Mode 2 - IsNext = 1, IsCurrent not affected.

            Mode 4 - IsNext = 2, IsCurrent = 2.

            Mode 5 - IsNext = 2, IsCurrent not affected.

            Mode 32768 - IsNext not affected, IsCurrent = 1.

            Mode 32769 - IsNext not affected, IsCurrent = 2.

            
            ======== =============
            ValueMap Values       
            ======== =============
            0        Mode 0       
            1        Mode 1       
            2        Mode 2       
            3        Mode 3       
            4        Mode 4       
            5        Mode 5       
            6        Mode 6       
            ..       DMTF Reserved
            32768    Mode 32768   
            32769    Mode 32769   
            ======== =============
            
        
    

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

