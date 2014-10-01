.. _LMI-DiskDrive:

LMI_DiskDrive
-------------

Class reference
===============
Subclass of :ref:`CIM_DiskDrive <CIM-DiskDrive>`

Capabilities and managment of a DiskDrive, a subtype of MediaAccessDevice.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-DiskDrive-InterconnectSpeed:

``uint64`` **InterconnectSpeed**

    This property identifies the port speed in bit/second. If the speed is unknown the property should be set to 0.

    
.. _LMI-DiskDrive-InterconnectType:

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
    
.. _LMI-DiskDrive-Capacity:

``uint64`` **Capacity**

    Capacity of disk drive, in bytes.

    
.. _LMI-DiskDrive-Temperature:

``sint16`` **Temperature**

    Current temperature of disk drive, in degrees Celsius

    
.. _LMI-DiskDrive-InstanceID:

``string`` **InstanceID**

    InstanceID is an optional property that may be used to opaquely and uniquely identify an instance of this class within the scope of the instantiating Namespace. Various subclasses of this class may override this property to make it required, or a key. Such subclasses may also modify the preferred algorithms for ensuring uniqueness that are defined below.

    To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon (:), and where <OrgID> must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness, <OrgID> must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If not null and the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance. 

    If not set to null for DMTF-defined instances, the "preferred" algorithm must be used with the <OrgID> set to CIM.

    
.. _LMI-DiskDrive-DiskType:

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
    
.. _LMI-DiskDrive-SystemName:

``string`` **SystemName**

    The System Name of the scoping system.

    
.. _LMI-DiskDrive-ElementName:

``string`` **ElementName**

    A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. 

    Note that the Name property of ManagedSystemElement is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. Note that if there is an associated instance of CIM_EnabledLogicalElementCapabilities, restrictions on this properties may exist as defined in ElementNameMask and MaxElementNameLen properties defined in that class.

    
.. _LMI-DiskDrive-Description:

``string`` **Description**

    The Description property provides a textual description of the object.

    
.. _LMI-DiskDrive-RPM:

``uint32`` **RPM**

    This property identifies how fast the drive media spins in Rotations Per Minute. Solid State drives should set this property to 0. If the RPM is unknown the property should be set to 0xFFFFFFFF

    
.. _LMI-DiskDrive-FormFactor:

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
    
.. _LMI-DiskDrive-Name:

``string`` **Name**

    The Name property defines the label by which the object is known. When subclassed, the Name property can be overridden to be a Key property.

    
.. _LMI-DiskDrive-EnabledState:

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
    
.. _LMI-DiskDrive-Caption:

``string`` **Caption**

    The Caption property is a short textual description (one- line string) of the object.

    
.. _LMI-DiskDrive-DeviceID:

``string`` **DeviceID**

    An address or other identifying information used to uniquely name the LogicalDevice.

    
.. _LMI-DiskDrive-OperationalStatus:

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
    
.. _LMI-DiskDrive-CreationClassName:

``string`` **CreationClassName**

    CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

    
.. _LMI-DiskDrive-SystemCreationClassName:

``string`` **SystemCreationClassName**

    The CreationClassName of the scoping system.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``boolean`` :ref:`MediaIsLocked <CIM-MediaAccessDevice-MediaIsLocked>`
| ``uint64`` :ref:`MaxAccessTime <CIM-MediaAccessDevice-MaxAccessTime>`
| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`Encryption <CIM-DiskDrive-Encryption>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint64`` :ref:`MaxMediaSize <CIM-MediaAccessDevice-MaxMediaSize>`
| ``datetime`` :ref:`TimeOfLastMount <CIM-MediaAccessDevice-TimeOfLastMount>`
| ``uint16[]`` :ref:`Capabilities <CIM-MediaAccessDevice-Capabilities>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint64`` :ref:`TotalMountTime <CIM-MediaAccessDevice-TotalMountTime>`
| ``uint64`` :ref:`PowerOnHours <CIM-LogicalDevice-PowerOnHours>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``string[]`` :ref:`IdentifyingDescriptions <CIM-LogicalDevice-IdentifyingDescriptions>`
| ``uint64`` :ref:`LoadTime <CIM-MediaAccessDevice-LoadTime>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``boolean`` :ref:`ErrorCleared <CIM-LogicalDevice-ErrorCleared>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``string`` :ref:`UnitsDescription <CIM-MediaAccessDevice-UnitsDescription>`
| ``uint32`` :ref:`UncompressedDataRate <CIM-MediaAccessDevice-UncompressedDataRate>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``datetime`` :ref:`LastCleaned <CIM-MediaAccessDevice-LastCleaned>`
| ``uint16`` :ref:`LocationIndicator <CIM-LogicalDevice-LocationIndicator>`
| ``string`` :ref:`OtherInterconnectType <CIM-DiskDrive-OtherInterconnectType>`
| ``string[]`` :ref:`OtherIdentifyingInfo <CIM-LogicalDevice-OtherIdentifyingInfo>`
| ``uint64`` :ref:`UnitsUsed <CIM-MediaAccessDevice-UnitsUsed>`
| ``uint16[]`` :ref:`PowerManagementCapabilities <CIM-LogicalDevice-PowerManagementCapabilities>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint32`` :ref:`NumberOfMediaSupported <CIM-MediaAccessDevice-NumberOfMediaSupported>`
| ``uint16[]`` :ref:`AdditionalAvailability <CIM-LogicalDevice-AdditionalAvailability>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``uint16`` :ref:`StatusInfo <CIM-LogicalDevice-StatusInfo>`
| ``uint64`` :ref:`UnloadTime <CIM-MediaAccessDevice-UnloadTime>`
| ``string`` :ref:`ErrorMethodology <CIM-MediaAccessDevice-ErrorMethodology>`
| ``uint64`` :ref:`MinBlockSize <CIM-MediaAccessDevice-MinBlockSize>`
| ``uint16`` :ref:`Security <CIM-MediaAccessDevice-Security>`
| ``uint64`` :ref:`MaxUnitsBeforeCleaning <CIM-MediaAccessDevice-MaxUnitsBeforeCleaning>`
| ``uint64`` :ref:`MountCount <CIM-MediaAccessDevice-MountCount>`
| ``uint64`` :ref:`MaxQuiesceTime <CIM-LogicalDevice-MaxQuiesceTime>`
| ``uint64`` :ref:`TotalPowerOnHours <CIM-LogicalDevice-TotalPowerOnHours>`
| ``uint64`` :ref:`DefaultBlockSize <CIM-MediaAccessDevice-DefaultBlockSize>`
| ``string`` :ref:`ErrorDescription <CIM-LogicalDevice-ErrorDescription>`
| ``string`` :ref:`CompressionMethod <CIM-MediaAccessDevice-CompressionMethod>`
| ``boolean`` :ref:`NeedsCleaning <CIM-MediaAccessDevice-NeedsCleaning>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint64`` :ref:`MaxBlockSize <CIM-MediaAccessDevice-MaxBlockSize>`
| ``uint32`` :ref:`LastErrorCode <CIM-LogicalDevice-LastErrorCode>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`Availability <CIM-LogicalDevice-Availability>`
| ``string[]`` :ref:`CapabilityDescriptions <CIM-MediaAccessDevice-CapabilityDescriptions>`

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

