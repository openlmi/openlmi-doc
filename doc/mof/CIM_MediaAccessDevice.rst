.. _CIM-MediaAccessDevice:

CIM_MediaAccessDevice
---------------------

Class reference
===============
Subclass of :ref:`CIM_LogicalDevice <CIM-LogicalDevice>`

A MediaAccessDevice represents the ability to access one or more media and use this media to store and retrieve data.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-MediaAccessDevice-MediaIsLocked:

``boolean`` **MediaIsLocked**

    True indicates that the media is locked in the Device and can not be ejected. For non-removeable Devices, this value should be true.

    
.. _CIM-MediaAccessDevice-MaxAccessTime:

``uint64`` **MaxAccessTime**

    Time in milliseconds to move from the first location on the Media to the location that is furthest with respect to time. For a DiskDrive, this represents full seek + full rotational delay. For TapeDrives, this represents a search from the beginning of the tape to the most physically distant point. (The end of a tape may be at its most physically distant point, but this is not necessarily true.)

    
.. _CIM-MediaAccessDevice-UnitsDescription:

``string`` **UnitsDescription**

    Defines 'Units' relative to its use in the property, MaxUnitsBeforeCleaning. This describes the criteria used to determine when the MediaAccessDevice should be cleaned.

    
.. _CIM-MediaAccessDevice-TimeOfLastMount:

``datetime`` **TimeOfLastMount**

    For a MediaAccessDevice that supports removable Media, the most recent date and time that Media was mounted on the Device. For Devices accessing nonremovable Media, such as hard disks, this property has no meaning and is not applicable.

    
.. _CIM-MediaAccessDevice-Capabilities:

``uint16[]`` **Capabilities**

    Capabilities of the MediaAccessDevice. For example, the Device may support "Random Access", removeable media and "Automatic Cleaning". In this case, the values 3, 7 and 9 would be written to the array. 

    Several of the enumerated values require some explanation: 1) Value 11, Supports Dual Sided Media, distinguishes a Device that can access both sides of dual sided Media, from a Device that reads only a single side and requires the Media to be flipped; and, 2) Value 12, Predismount Eject Not Required, indicates that Media does not have to be explicitly ejected from the Device before being accessed by a PickerElement.

    
    ======== ==============================
    ValueMap Values                        
    ======== ==============================
    0        Unknown                       
    1        Other                         
    2        Sequential Access             
    3        Random Access                 
    4        Supports Writing              
    5        Encryption                    
    6        Compression                   
    7        Supports Removeable Media     
    8        Manual Cleaning               
    9        Automatic Cleaning            
    10       SMART Notification            
    11       Supports Dual Sided Media     
    12       Predismount Eject Not Required
    ======== ==============================
    
.. _CIM-MediaAccessDevice-UnloadTime:

``uint64`` **UnloadTime**

    Time in milliseconds from being able to read or write a Media to its 'unload'. For example, for DiskDrives, this is the interval between a disk spinning at nominal speeds and a disk not spinning. For TapeDrives, this is the time for a Media to go from its BOT to being fully ejected and accessible to a PickerElement or human operator.

    
.. _CIM-MediaAccessDevice-TotalMountTime:

``uint64`` **TotalMountTime**

    For a MediaAccessDevice that supports removable Media, the total time (in seconds) that Media have been mounted for data transfer or to clean the Device. For Devices accessing nonremovable Media, such as hard disks, this property is not applicable and should be set to 0.

    
.. _CIM-MediaAccessDevice-UncompressedDataRate:

``uint32`` **UncompressedDataRate**

    The sustained data transfer rate in KB/sec that the Device can read from and write to a Media. This is a sustained, raw data rate. Maximum rates or rates assuming compression should not be reported in this property.

    
.. _CIM-MediaAccessDevice-LastCleaned:

``datetime`` **LastCleaned**

    The date and time on which the Device was last cleaned.

    
.. _CIM-MediaAccessDevice-CompressionMethod:

``string`` **CompressionMethod**

    A free form string indicating the algorithm or tool used by the device to support compression. If it is not possible or not desired to describe the compression scheme (perhaps because it is not known), recommend using the following words: "Unknown" to represent that it is not known whether the device supports compression capabilities or not, "Compressed" to represent that the device supports compression capabilities but either its compression scheme is not known or not disclosed, and "Not Compressed" to represent that the devices does not support compression capabilities.

    
.. _CIM-MediaAccessDevice-UnitsUsed:

``uint64`` **UnitsUsed**

    An unsigned integer indicating the currently used 'units' of the AccessDevice, helpful to describe when the Device may require cleaning. The property, UnitsDescription, defines how 'units' should be interpreted.

    
.. _CIM-MediaAccessDevice-NumberOfMediaSupported:

``uint32`` **NumberOfMediaSupported**

    When the MediaAccessDevice supports multiple individual Media, this property defines the maximum number which can be supported or inserted.

    
.. _CIM-MediaAccessDevice-DefaultBlockSize:

``uint64`` **DefaultBlockSize**

    Default block size, in bytes, for this Device.

    
.. _CIM-MediaAccessDevice-CapabilityDescriptions:

``string[]`` **CapabilityDescriptions**

    An array of free-form strings providing more detailed explanations for any of the AccessDevice features indicated in the Capabilities array. Note, each entry of this array is related to the entry in the Capabilities array that is located at the same index.

    
.. _CIM-MediaAccessDevice-ErrorMethodology:

``string`` **ErrorMethodology**

    ErrorMethodology is a free-form string describing the type(s) of error detection and correction supported by this Device.

    
.. _CIM-MediaAccessDevice-MinBlockSize:

``uint64`` **MinBlockSize**

    Minimum block size, in bytes, for media accessed by this Device.

    
.. _CIM-MediaAccessDevice-Security:

``uint16`` **Security**

    An enumeration indicating the operational security defined for the MediaAccessDevice. For example, information that the Device is "Read Only" (value=4) or "Boot Bypass" (value=6) can be described using this property.

    
    ======== =========================
    ValueMap Values                   
    ======== =========================
    1        Other                    
    2        Unknown                  
    3        None                     
    4        Read Only                
    5        Locked Out               
    6        Boot Bypass              
    7        Boot Bypass and Read Only
    ======== =========================
    
.. _CIM-MediaAccessDevice-MaxUnitsBeforeCleaning:

``uint64`` **MaxUnitsBeforeCleaning**

    An unsigned integer indicating the maximum 'units' that can be used, with respect to the AccessDevice, before the Device should be cleaned. The property, UnitsDescription, defines how 'units' should be interpreted.

    
.. _CIM-MediaAccessDevice-MountCount:

``uint64`` **MountCount**

    For a MediaAccessDevice that supports removable Media, the number of times that Media have been mounted for data transfer or to clean the Device. For Devices accessing nonremovable Media, such as hard disks, this property is not applicable and should be set to 0.

    
.. _CIM-MediaAccessDevice-LoadTime:

``uint64`` **LoadTime**

    Time in milliseconds from 'load' to being able to read or write a Media. For example, for DiskDrives, this is the interval between a disk not spinning to the disk reporting that it is ready for read/write (ie, the disk spinning at nominal speeds). For TapeDrives, this is the time from a Media being injected to reporting that it is ready for an application. This is usually at the tape's BOT area.

    
.. _CIM-MediaAccessDevice-NeedsCleaning:

``boolean`` **NeedsCleaning**

    Boolean indicating that the MediaAccessDevice needs cleaning. Whether manual or automatic cleaning is possible is indicated in the Capabilities array property.

    
.. _CIM-MediaAccessDevice-MaxBlockSize:

``uint64`` **MaxBlockSize**

    Maximum block size, in bytes, for media accessed by this Device.

    
.. _CIM-MediaAccessDevice-MaxMediaSize:

``uint64`` **MaxMediaSize**

    Maximum size, in KBytes, of media supported by this Device. KBytes is interpreted as the number of bytes multiplied by 1000 (NOT the number of bytes multiplied by 1024).

    

Local methods
^^^^^^^^^^^^^

    .. _CIM-MediaAccessDevice-LockMedia:

``uint32`` **LockMedia** (``boolean`` Lock)

    Method to lock and unlock the media in a removeable Access Device. The method takes one parameter as input - a boolean indicating whether to lock or unlock. TRUE indicates that the media should be locked in the Device, FALSE indicates that the media should be unlocked. The method returns 0 if successful, 1 if not supported, and any other value if an error occurred. The set of possible return codes should be specified in a ValueMap qualifier on the method. The strings to which the ValueMap contents are 'translated' should be specified as a Values array qualifier on the method.

    
    **Parameters**
    
        *IN* ``boolean`` **Lock**
            If TRUE, lock the media. If FALSE release the media.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``string`` :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| ``uint16[]`` :ref:`PowerManagementCapabilities <CIM-LogicalDevice-PowerManagementCapabilities>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
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
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16`` :ref:`LocationIndicator <CIM-LogicalDevice-LocationIndicator>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string[]`` :ref:`OtherIdentifyingInfo <CIM-LogicalDevice-OtherIdentifyingInfo>`
| ``uint64`` :ref:`PowerOnHours <CIM-LogicalDevice-PowerOnHours>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``uint16[]`` :ref:`AdditionalAvailability <CIM-LogicalDevice-AdditionalAvailability>`
| ``uint16`` :ref:`StatusInfo <CIM-LogicalDevice-StatusInfo>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint64`` :ref:`MaxQuiesceTime <CIM-LogicalDevice-MaxQuiesceTime>`
| ``uint64`` :ref:`TotalPowerOnHours <CIM-LogicalDevice-TotalPowerOnHours>`
| ``string`` :ref:`ErrorDescription <CIM-LogicalDevice-ErrorDescription>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint32`` :ref:`LastErrorCode <CIM-LogicalDevice-LastErrorCode>`
| ``uint16`` :ref:`Availability <CIM-LogicalDevice-Availability>`
| ``string`` :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`
| ``string`` :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`Reset <CIM-LogicalDevice-Reset>`
| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`
| :ref:`SetPowerState <CIM-LogicalDevice-SetPowerState>`
| :ref:`QuiesceDevice <CIM-LogicalDevice-QuiesceDevice>`
| :ref:`EnableDevice <CIM-LogicalDevice-EnableDevice>`
| :ref:`OnlineDevice <CIM-LogicalDevice-OnlineDevice>`
| :ref:`SaveProperties <CIM-LogicalDevice-SaveProperties>`
| :ref:`RestoreProperties <CIM-LogicalDevice-RestoreProperties>`

