.. _CIM-UnixFile:

CIM_UnixFile
------------

Class reference
===============
Subclass of :ref:`CIM_LogicalElement <CIM-LogicalElement>`

The UnixFile class holds properties that are valid for various subclasses of LogicalFile, in a Unix environment. This is defined as a separate and unique class since it is applicable to Unix files, directories, etc. It is associated via a FileIdentity relationship to these subclasses of LogicalFile. Unless this approach of creating and associating a separate class is used, it is necessary to subclass each of the inheritance hierarchies under LogicalFile, duplicating the properties in this class. The referenced _PC* and _POSIX* constants are defined in unistd.h. Some properties indicate whether the UNIX implementation support a feature such as asynchronous I/O or priority I/O. If supported, sysconf returns the value as defined in the appropriate header file such as unistd.h. If a feature is not supported, then pathconf returns a -1. In this case, the corresponding property should be returned without any value.


Key properties
^^^^^^^^^^^^^^

| :ref:`CSName <CIM-UnixFile-CSName>`
| :ref:`FSCreationClassName <CIM-UnixFile-FSCreationClassName>`
| :ref:`LFCreationClassName <CIM-UnixFile-LFCreationClassName>`
| :ref:`FSName <CIM-UnixFile-FSName>`
| :ref:`LFName <CIM-UnixFile-LFName>`
| :ref:`CSCreationClassName <CIM-UnixFile-CSCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-UnixFile-SetUid:

``boolean`` **SetUid**

    Indicates whether the associated file has setuid permissions.

    
.. _CIM-UnixFile-CSName:

``string`` **CSName**

    The scoping ComputerSystem's Name.

    
.. _CIM-UnixFile-UserID:

``string`` **UserID**

    An Identifer that uniquely describes the owner of this file.

    
.. _CIM-UnixFile-PosixAsyncIo:

``uint64`` **PosixAsyncIo**

    Indicates whether asynchronous input or output operations may be performed for the associated file.

    
.. _CIM-UnixFile-NameMax:

``uint64`` **NameMax**

    Maximum number of bytes in a filename, not including terminating null.

    
.. _CIM-UnixFile-FSCreationClassName:

``string`` **FSCreationClassName**

    The scoping FileSystem's CreationClassName.

    
.. _CIM-UnixFile-PosixSyncIo:

``uint64`` **PosixSyncIo**

    Indicates whether synchronised input or output operations may be performed for the associated file.

    
.. _CIM-UnixFile-LFCreationClassName:

``string`` **LFCreationClassName**

    The scoping LogicalFile's CreationClassName.

    
.. _CIM-UnixFile-GroupID:

``string`` **GroupID**

    An identifier that describes the group that owns this file.

    
.. _CIM-UnixFile-PosixPrioIo:

``uint64`` **PosixPrioIo**

    Indicates whether prioritized input or output operations may be performed for the associated file.

    
.. _CIM-UnixFile-FSName:

``string`` **FSName**

    The scoping FileSystem's Name.

    
.. _CIM-UnixFile-SetGid:

``boolean`` **SetGid**

    Indicates whether the associated file has setgid permissions.

    
.. _CIM-UnixFile-LFName:

``string`` **LFName**

    The scoping LogicalFile's Name.

    
.. _CIM-UnixFile-PathMax:

``uint64`` **PathMax**

    Maximum number of bytes in a pathname, including the terminating null character.

    
.. _CIM-UnixFile-LinkCount:

``uint64`` **LinkCount**

    Count of the number of names for this file.

    
.. _CIM-UnixFile-LinkMax:

``uint64`` **LinkMax**

    Maximum number of links to a single file.

    
.. _CIM-UnixFile-PosixNoTrunc:

``uint64`` **PosixNoTrunc**

    Indicates whether pathname components longer than NameMax generate an error.

    
.. _CIM-UnixFile-FileInodeNumber:

``string`` **FileInodeNumber**

    File Inode number, as printed by "ls -i".

    
.. _CIM-UnixFile-LastModifiedInode:

``datetime`` **LastModifiedInode**

    The time that the Inode was last modified. This includes the Inode creation time, state modification, and etc.

    
.. _CIM-UnixFile-CSCreationClassName:

``string`` **CSCreationClassName**

    The scoping ComputerSystem's CreationClassName.

    
.. _CIM-UnixFile-PosixChownRestricted:

``uint64`` **PosixChownRestricted**

    The use of chown() is restricted to a process with appropriate privileges. chown() is used to change the group ID of a file. The group ID can be changed to the effective group ID or one of its supplementary group IDs.

    
.. _CIM-UnixFile-SaveText:

``boolean`` **SaveText**

    Indicates restricted deletion for directories, or possible implementation defined properties for executable files. For directories this is known as the sticky bit.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

