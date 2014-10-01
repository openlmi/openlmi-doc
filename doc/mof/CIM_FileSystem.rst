.. _CIM-FileSystem:

CIM_FileSystem
--------------

Class reference
===============
Subclass of :ref:`CIM_EnabledLogicalElement <CIM-EnabledLogicalElement>`

A file or dataset store local to a System (such as a ComputerSystem or an ApplicationSystem) or remotely mounted from a file server.


Key properties
^^^^^^^^^^^^^^

| :ref:`CSName <CIM-FileSystem-CSName>`
| :ref:`Name <CIM-FileSystem-Name>`
| :ref:`CSCreationClassName <CIM-FileSystem-CSCreationClassName>`
| :ref:`CreationClassName <CIM-FileSystem-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-FileSystem-MaxFileNameLength:

``uint32`` **MaxFileNameLength**

    Integer indicating the maximum length of a file name within the FileSystem. 0 indicates that there is no limit on file name length.

    
.. _CIM-FileSystem-CSName:

``string`` **CSName**

    The scoping System's Name. Note that this class was originally defined in the scope of a ComputerSystem, and was later allowed to be scoped by any System (for example, a computer or application system). Unfortunately, the property name, CSName, could not be changed (for example, to SystemName) without deprecating the class. This change was not deemed critical to the semantics and therefore did not merit deprecation. So, the property name remains.

    
.. _CIM-FileSystem-ClusterSize:

``uint32`` **ClusterSize**

    The minimum file allocation size (an integral number of blocks), imposed by the FileSystem. (The size of a block is specified in the BlockSize property for the FileSystem.) Minimum allocation size is the smallest amount of storage allocated to a LogicalFile by the FileSystem. This is not a mandatory minimum allocation for all FileSystems. Under stress conditions, some FileSystems may allocate storage in amounts smaller than the ClusterSize.

    
.. _CIM-FileSystem-EncryptionMethod:

``string`` **EncryptionMethod**

    A free form string indicating the algorithm or tool used to encrypt the FileSystem. If it is not possible or not desired to describe the encryption scheme (perhaps for security reasons), recommend using the following words: "Unknown" to represent that it is not known whether the FileSystem is encrypted or not, "Encrypted" to represent that the File System is encrypted but either its encryption scheme is not known or not disclosed, and "Not Encrypted" to represent that the FileSystem is not encrypted.

    
.. _CIM-FileSystem-ReadOnly:

``boolean`` **ReadOnly**

    Indicates that the FileSystem is designated as read only.

    
.. _CIM-FileSystem-ResizeIncrement:

``uint64`` **ResizeIncrement**

    The increment size of a resizable File in bytes. If the File is a fixed size, or the resize increment is not specified, the value of this property must be 0.

    
.. _CIM-FileSystem-CasePreserved:

``boolean`` **CasePreserved**

    Indicates that the case of file names are preserved.

    
.. _CIM-FileSystem-CaseSensitive:

``boolean`` **CaseSensitive**

    Indicates that case sensitive file names are supported.

    
.. _CIM-FileSystem-FileSystemSize:

``uint64`` **FileSystemSize**

    The FileSystemSize property stores the total size of the File System in bytes. If unknown, enter 0.

    
.. _CIM-FileSystem-OtherPersistenceType:

``string`` **OtherPersistenceType**

    A string describing the persistence characteristics when PersistenceType is "Other".

    
.. _CIM-FileSystem-CompressionMethod:

``string`` **CompressionMethod**

    A free form string indicating the algorithm or tool used to compress the FileSystem. If it is not possible or not desired to describe the compression scheme (perhaps because it is not known), recommend using the following words: "Unknown" to represent that it is not known whether the FileSystem is compressed or not, "Compressed" to represent that the File System is compressed but either its compression scheme is not known or not disclosed, and "Not Compressed" to represent that the FileSystem is not compressed.

    
.. _CIM-FileSystem-Name:

``string`` **Name**

    The inherited Name serves as key of a FileSystem instance within a ComputerSystem.

    
.. _CIM-FileSystem-BlockSize:

``uint64`` **BlockSize**

    FileSystems can read/write data in blocks which are defined independently of the underlying StorageExtents. This property captures the FileSystem's block size for data storage and retrieval.

    
.. _CIM-FileSystem-NumberOfFiles:

``uint64`` **NumberOfFiles**

    The number of files contained in the FileSystem.

    
.. _CIM-FileSystem-Root:

``string`` **Root**

    Path name or other information defining the root of the FileSystem.

    
.. _CIM-FileSystem-PersistenceType:

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
    
.. _CIM-FileSystem-FileSystemType:

``string`` **FileSystemType**

    String describing the type of FileSystem and therefore, its conventions. For example, "NTFS" or "S5" may be listed as well as any additional information on the FileSystem's implementation. Since various flavors of FileSystems (like S5) exist, this property is defined as a string.

    
.. _CIM-FileSystem-CSCreationClassName:

``string`` **CSCreationClassName**

    The scoping System's CreationClassName. Note that this class was originally defined in the scope of a ComputerSystem, and was later allowed to be scoped by any System (for example, a computer or application system). Unfortunately, the property name, CSCreationClassName, could not be changed (for example, to SystemCreationClass Name) without deprecating the class. This change was not deemed critical to the semantics and therefore did not merit deprecation. So, the property name remains.

    
.. _CIM-FileSystem-IsFixedSize:

``uint16`` **IsFixedSize**

    Indicates whether the File size is fixed at creation time (value = 1) - the file size is fixed, (value = 2) - the file is not a fixed size. The default (value = 0) indicates that this information is not specified. If the File size is not fixed, the ResizeIncrement property should specify the growth increment, in bytes.

    
    ======== ==============
    ValueMap Values        
    ======== ==============
    0        Not Specified 
    1        Fixed Size    
    2        Not Fixed Size
    ======== ==============
    
.. _CIM-FileSystem-AvailableSpace:

``uint64`` **AvailableSpace**

    AvailableSpace indicates the total amount of free space for the FileSystem, in bytes. If unknown, enter 0.

    
.. _CIM-FileSystem-CodeSet:

``uint16[]`` **CodeSet**

    Array defining the character sets or encoding supported by the FileSystem. For example, the values, "ASCII" (2) or "ISO2022" (4), may be specified.

    
    ======== ==================
    ValueMap Values            
    ======== ==================
    0        Unknown           
    1        Other             
    2        ASCII             
    3        Unicode           
    4        ISO2022           
    5        ISO8859           
    6        Extended UNIX Code
    7        UTF-8             
    8        UCS-2             
    ======== ==================
    
.. _CIM-FileSystem-CreationClassName:

``string`` **CreationClassName**

    CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`

