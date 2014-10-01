.. _LMI-ExtentEncryptionConfigurationService:

LMI_ExtentEncryptionConfigurationService
----------------------------------------

Class reference
===============
Subclass of :ref:`CIM_Service <CIM-Service>`

Service which configures LUKS formats on block devices.


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

    .. _LMI-ExtentEncryptionConfigurationService-CloseEncryptionFormat:

``uint32`` **CloseEncryptionFormat** (:ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`LMI_EncryptionFormat <LMI-EncryptionFormat>` Format)

    Closes a LUKS device. Appropriate device mapper device with clear-text data is destroyed and appropriate LMI_LUKSStorageExtent is removed.

    
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

            
        
        *IN* :ref:`LMI_EncryptionFormat <LMI-EncryptionFormat>` **Format**
            LUKS format to close.

            
        
    
    .. _LMI-ExtentEncryptionConfigurationService-DeletePassphrase:

``uint32`` **DeletePassphrase** (:ref:`LMI_EncryptionFormat <LMI-EncryptionFormat>` Format, ``string`` Passphrase)

    Remove a passphrase from LUKS format.

    
    **Parameters**
    
        *IN* :ref:`LMI_EncryptionFormat <LMI-EncryptionFormat>` **Format**
            The format to remove the passphrase from.

            
        
        *IN* ``string`` **Passphrase**
            The passphrase to remove.

            
        
    
    .. _LMI-ExtentEncryptionConfigurationService-AddPassphrase:

``uint32`` **AddPassphrase** (:ref:`LMI_EncryptionFormat <LMI-EncryptionFormat>` Format, ``string`` Passphrase, ``string`` NewPassphrase)

    Add new passphrase to LUKS format. LUKS supports up to 8 independent passphrases, adding any additional one will result in error. Application cannot specify which key slot will be used by which passphrase.

    
    **Parameters**
    
        *IN* :ref:`LMI_EncryptionFormat <LMI-EncryptionFormat>` **Format**
            The format to add the passphrase to.

            
        
        *IN* ``string`` **Passphrase**
            Any of the existing passphrase to unlock the format.

            
        
        *IN* ``string`` **NewPassphrase**
            New passphrase to add.

            
        
    
    .. _LMI-ExtentEncryptionConfigurationService-CreateEncryptionFormat:

``uint32`` **CreateEncryptionFormat** (:ref:`CIM_StorageExtent <CIM-StorageExtent>` InExtent, :ref:`LMI_EncryptionFormatSetting <LMI-EncryptionFormatSetting>` Goal, ``string`` Passphrase, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`LMI_EncryptionFormat <LMI-EncryptionFormat>` Format)

    Formats a device to become a LUKS device. All previous data on the device is destroyed.

    
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
    
        *IN* :ref:`CIM_StorageExtent <CIM-StorageExtent>` **InExtent**
            The block device to format.

            
        
        *IN* :ref:`LMI_EncryptionFormatSetting <LMI-EncryptionFormatSetting>` **Goal**
            Parameteres of the LUKS format. This parameter is unused currently and must be NULL.

            
        
        *IN* ``string`` **Passphrase**
            Passphrase to use to encrypt the device. This is not the encryption key!

            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the created job.

            
        
        *OUT* :ref:`LMI_EncryptionFormat <LMI-EncryptionFormat>` **Format**
            Created format.

            
        
    
    .. _LMI-ExtentEncryptionConfigurationService-OpenEncryptionFormat:

``uint32`` **OpenEncryptionFormat** (:ref:`LMI_EncryptionFormat <LMI-EncryptionFormat>` Format, ``string`` ElementName, ``string`` Passphrase, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, :ref:`CIM_StorageExtent <CIM-StorageExtent>` Extent)

    Opens a LUKS device. This means new block device with clear-text data is created. This new device is represented by LMI_LUKSStorageDevice and is returned as 'Extent' output parameter.

    
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
    
        *IN* :ref:`LMI_EncryptionFormat <LMI-EncryptionFormat>` **Format**
            Format to open.

            
        
        *IN* ``string`` **ElementName**
            Desired ElementName of the newly created LMI_LUKSStorageDevice. This name is also used as device mapper name, i.e. device with path /dev/mapper/<ElementName> will be created.

            
        
        *IN* ``string`` **Passphrase**
            Passphrase to unencrypt the device.

            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the created job.

            
        
        *OUT* :ref:`CIM_StorageExtent <CIM-StorageExtent>` **Extent**
            Created CIM_StorageExtent which represents the clear-text block device.

            
        
    

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

