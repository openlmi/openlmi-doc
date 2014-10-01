.. _CIM-DiskDrive:

CIM_DiskDrive
-------------

Class reference
===============
Subclass of :ref:`CIM_MediaAccessDevice <CIM-MediaAccessDevice>`

Capabilities and managment of a DiskDrive, a subtype of MediaAccessDevice.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-DiskDrive-InterconnectSpeed:

``uint64`` **InterconnectSpeed**

    This property identifies the port speed in bit/second. If the speed is unknown the property should be set to 0.

    
.. _CIM-DiskDrive-InterconnectType:

``uint16`` **InterconnectType**

    This property identifies the drive interface type. 

    ATA: Advanced Technology Attachment 

    SATA: Serial ATA 

    SAS: Serial Attached SCSI 

    FC: Fibre Channel 

    SOP: SCSI Over PCIe -- Peripheral Component Interconnect express.

    
    ======== ==============
    ValueMap Values        
    ======== ==============
    0        Unknown       
    1        Other         
    2        Not Applicable
    3        ATA           
    4        SATA          
    5        SAS           
    6        FC            
    7        SOP           
    ======== ==============
    
.. _CIM-DiskDrive-Encryption:

``uint16`` **Encryption**

    This property reflects the state of the encryption feature implemented by some disk drives as defined by SCSI. The Unlocked state means the drive is capable of encryption but it is disabled. The Locked state means the drive is currently encrypted

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Unknown      
    1        Not Supported
    2        Unlocked     
    3        Locked       
    ======== =============
    
.. _CIM-DiskDrive-DiskType:

``uint16`` **DiskType**

    The technology used to store data. the hybrid uses a combination of HDD and SSD in the same drive.

    
    ======== =================
    ValueMap Values           
    ======== =================
    0        Unknown          
    1        Other            
    2        Hard Disk Drive  
    3        Solid State Drive
    4        Hybrid           
    ======== =================
    
.. _CIM-DiskDrive-OtherInterconnectType:

``string`` **OtherInterconnectType**

    This property identifies other interconnect types.

    
.. _CIM-DiskDrive-FormFactor:

``uint16`` **FormFactor**

    The Physical size of the disk drive.

    
    ======== ============
    ValueMap Values      
    ======== ============
    0        Unknown     
    1        Other       
    2        Not Reported
    3        5.25 inch   
    4        3.5 inch    
    5        2.5 inch    
    6        1.8 inch    
    ======== ============
    
.. _CIM-DiskDrive-RPM:

``uint32`` **RPM**

    This property identifies how fast the drive media spins in Rotations Per Minute. Solid State drives should set this property to 0. If the RPM is unknown the property should be set to 0xFFFFFFFF

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``boolean`` :ref:`MediaIsLocked <CIM-MediaAccessDevice-MediaIsLocked>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``uint64`` :ref:`MaxAccessTime <CIM-MediaAccessDevice-MaxAccessTime>`
| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``string`` :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| ``uint16[]`` :ref:`PowerManagementCapabilities <CIM-LogicalDevice-PowerManagementCapabilities>`
| ``datetime`` :ref:`TimeOfLastMount <CIM-MediaAccessDevice-TimeOfLastMount>`
| ``uint16[]`` :ref:`Capabilities <CIM-MediaAccessDevice-Capabilities>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| ``uint64`` :ref:`UnloadTime <CIM-MediaAccessDevice-UnloadTime>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint64`` :ref:`TotalMountTime <CIM-MediaAccessDevice-TotalMountTime>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``string[]`` :ref:`IdentifyingDescriptions <CIM-LogicalDevice-IdentifyingDescriptions>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``boolean`` :ref:`ErrorCleared <CIM-LogicalDevice-ErrorCleared>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``string`` :ref:`UnitsDescription <CIM-MediaAccessDevice-UnitsDescription>`
| ``uint32`` :ref:`UncompressedDataRate <CIM-MediaAccessDevice-UncompressedDataRate>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``datetime`` :ref:`LastCleaned <CIM-MediaAccessDevice-LastCleaned>`
| ``string`` :ref:`CompressionMethod <CIM-MediaAccessDevice-CompressionMethod>`
| ``uint16`` :ref:`LocationIndicator <CIM-LogicalDevice-LocationIndicator>`
| ``string[]`` :ref:`OtherIdentifyingInfo <CIM-LogicalDevice-OtherIdentifyingInfo>`
| ``uint64`` :ref:`UnitsUsed <CIM-MediaAccessDevice-UnitsUsed>`
| ``uint64`` :ref:`PowerOnHours <CIM-LogicalDevice-PowerOnHours>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint32`` :ref:`NumberOfMediaSupported <CIM-MediaAccessDevice-NumberOfMediaSupported>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``uint16[]`` :ref:`AdditionalAvailability <CIM-LogicalDevice-AdditionalAvailability>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``uint64`` :ref:`DefaultBlockSize <CIM-MediaAccessDevice-DefaultBlockSize>`
| ``uint16`` :ref:`StatusInfo <CIM-LogicalDevice-StatusInfo>`
| ``string[]`` :ref:`CapabilityDescriptions <CIM-MediaAccessDevice-CapabilityDescriptions>`
| ``string`` :ref:`ErrorMethodology <CIM-MediaAccessDevice-ErrorMethodology>`
| ``uint64`` :ref:`MinBlockSize <CIM-MediaAccessDevice-MinBlockSize>`
| ``uint16`` :ref:`Security <CIM-MediaAccessDevice-Security>`
| ``uint64`` :ref:`MaxUnitsBeforeCleaning <CIM-MediaAccessDevice-MaxUnitsBeforeCleaning>`
| ``uint64`` :ref:`MountCount <CIM-MediaAccessDevice-MountCount>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint64`` :ref:`MaxQuiesceTime <CIM-LogicalDevice-MaxQuiesceTime>`
| ``uint64`` :ref:`TotalPowerOnHours <CIM-LogicalDevice-TotalPowerOnHours>`
| ``uint64`` :ref:`LoadTime <CIM-MediaAccessDevice-LoadTime>`
| ``string`` :ref:`ErrorDescription <CIM-LogicalDevice-ErrorDescription>`
| ``boolean`` :ref:`NeedsCleaning <CIM-MediaAccessDevice-NeedsCleaning>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint64`` :ref:`MaxBlockSize <CIM-MediaAccessDevice-MaxBlockSize>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint32`` :ref:`LastErrorCode <CIM-LogicalDevice-LastErrorCode>`
| ``uint64`` :ref:`MaxMediaSize <CIM-MediaAccessDevice-MaxMediaSize>`
| ``uint16`` :ref:`Availability <CIM-LogicalDevice-Availability>`
| ``string`` :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`
| ``string`` :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`Reset <CIM-LogicalDevice-Reset>`
| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`
| :ref:`SetPowerState <CIM-LogicalDevice-SetPowerState>`
| :ref:`QuiesceDevice <CIM-LogicalDevice-QuiesceDevice>`
| :ref:`LockMedia <CIM-MediaAccessDevice-LockMedia>`
| :ref:`EnableDevice <CIM-LogicalDevice-EnableDevice>`
| :ref:`OnlineDevice <CIM-LogicalDevice-OnlineDevice>`
| :ref:`SaveProperties <CIM-LogicalDevice-SaveProperties>`
| :ref:`RestoreProperties <CIM-LogicalDevice-RestoreProperties>`

