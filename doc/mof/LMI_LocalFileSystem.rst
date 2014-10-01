.. _LMI-LocalFileSystem:

LMI_LocalFileSystem
-------------------

Class reference
===============
Subclass of :ref:`CIM_LocalFileSystem <CIM-LocalFileSystem>`

Base class for filesystems on StorageExtents of this system.


Key properties
^^^^^^^^^^^^^^

| :ref:`CSName <CIM-FileSystem-CSName>`
| :ref:`Name <CIM-FileSystem-Name>`
| :ref:`CSCreationClassName <CIM-FileSystem-CSCreationClassName>`
| :ref:`CreationClassName <CIM-FileSystem-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-LocalFileSystem-MaxFileNameLength:

``uint32`` **MaxFileNameLength**

    Integer indicating the maximum length of a file name within the FileSystem. 0 indicates that there is no limit on file name length.

    
.. _LMI-LocalFileSystem-CasePreserved:

``boolean`` **CasePreserved**

    Indicates that the case of file names are preserved.

    
.. _LMI-LocalFileSystem-CaseSensitive:

``boolean`` **CaseSensitive**

    Indicates that case sensitive file names are supported.

    
.. _LMI-LocalFileSystem-OperationalStatus:

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
    
.. _LMI-LocalFileSystem-FileSystemSize:

``uint64`` **FileSystemSize**

    The FileSystemSize property stores the total size of the File System in bytes. If unknown, enter 0.

    
.. _LMI-LocalFileSystem-IsFixedSize:

``uint16`` **IsFixedSize**

    Indicates whether the File size is fixed at creation time (value = 1) - the file size is fixed, (value = 2) - the file is not a fixed size. The default (value = 0) indicates that this information is not specified. If the File size is not fixed, the ResizeIncrement property should specify the growth increment, in bytes.

    
    ======== ==============
    ValueMap Values        
    ======== ==============
    0        Not Specified 
    1        Fixed Size    
    2        Not Fixed Size
    ======== ==============
    
.. _LMI-LocalFileSystem-Name:

``string`` **Name**

    Unique identifier of the filesystem on computer system. Usually UUID.

    
.. _LMI-LocalFileSystem-BlockSize:

``uint64`` **BlockSize**

    FileSystems can read/write data in blocks which are defined independently of the underlying StorageExtents. This property captures the FileSystem's block size for data storage and retrieval.

    
.. _LMI-LocalFileSystem-Root:

``string`` **Root**

    Path name or other information defining the root of the FileSystem.

    
.. _LMI-LocalFileSystem-PersistenceType:

``uint16`` **PersistenceType**

    An enumerated value representing the FileSystem's perception of its own persistence characteristics. This property would typically be set at the time the FileSystem is instantiated and would not be changed by external actions. A value of "Persistent" indicates that the FileSystem is persistent, will be preserved through an orderly shutdown and should be protected. A value of "Temporary" indicates that the FileSystem is non-persistent, should not be protected and may not survive a shutdown. A value of "External" indicates that the FileSystem is controlled outside of the scope of the operating environment and may need to be protected by specialized means. A value of "Other" is provided to allow for additional persistence types, to be described in the OtherPersistenceType attribute, and is expected to be rarely, if ever, used. A value of "Unknown" indicates that the persistence of the FileSystem can not be determined.

    
    ======== ==========
    ValueMap Values    
    ======== ==========
    0        Unknown   
    1        Other     
    2        Persistent
    3        Temporary 
    4        External  
    ======== ==========
    
.. _LMI-LocalFileSystem-UUID:

``string`` **UUID**

    UUID of the filesystem.

    
.. _LMI-LocalFileSystem-FileSystemType:

``string`` **FileSystemType**

    String describing the type of FileSystem and therefore, its conventions. For example, "NTFS" or "S5" may be listed as well as any additional information on the FileSystem's implementation. Since various flavors of FileSystems (like S5) exist, this property is defined as a string.

    
.. _LMI-LocalFileSystem-ReadOnly:

``boolean`` **ReadOnly**

    Indicates that the FileSystem is designated as read only.

    
.. _LMI-LocalFileSystem-AvailableSpace:

``uint64`` **AvailableSpace**

    AvailableSpace indicates the total amount of free space for the FileSystem, in bytes. If unknown, enter 0.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``string`` :ref:`CSName <CIM-FileSystem-CSName>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``uint32`` :ref:`ClusterSize <CIM-FileSystem-ClusterSize>`
| ``string`` :ref:`EncryptionMethod <CIM-FileSystem-EncryptionMethod>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint64`` :ref:`ResizeIncrement <CIM-FileSystem-ResizeIncrement>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``string`` :ref:`OtherPersistenceType <CIM-FileSystem-OtherPersistenceType>`
| ``string`` :ref:`CompressionMethod <CIM-FileSystem-CompressionMethod>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``uint64`` :ref:`NumberOfFiles <CIM-FileSystem-NumberOfFiles>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`CSCreationClassName <CIM-FileSystem-CSCreationClassName>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16[]`` :ref:`CodeSet <CIM-FileSystem-CodeSet>`
| ``string`` :ref:`CreationClassName <CIM-FileSystem-CreationClassName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`

