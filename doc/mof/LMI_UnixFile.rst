.. _LMI-UnixFile:

LMI_UnixFile
------------

Class reference
===============
Subclass of :ref:`CIM_UnixFile <CIM-UnixFile>`

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

.. _LMI-UnixFile-SELinuxExpectedContext:

``string`` **SELinuxExpectedContext**

    Expected SELinux context.

    
.. _LMI-UnixFile-SELinuxCurrentContext:

``string`` **SELinuxCurrentContext**

    Current SELinux context.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``boolean`` :ref:`SetUid <CIM-UnixFile-SetUid>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``string`` :ref:`CSName <CIM-UnixFile-CSName>`
| ``string`` :ref:`UserID <CIM-UnixFile-UserID>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``uint64`` :ref:`PosixAsyncIo <CIM-UnixFile-PosixAsyncIo>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint64`` :ref:`NameMax <CIM-UnixFile-NameMax>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``string`` :ref:`FSCreationClassName <CIM-UnixFile-FSCreationClassName>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``uint64`` :ref:`PosixSyncIo <CIM-UnixFile-PosixSyncIo>`
| ``string`` :ref:`LFCreationClassName <CIM-UnixFile-LFCreationClassName>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``string`` :ref:`GroupID <CIM-UnixFile-GroupID>`
| ``uint64`` :ref:`PosixPrioIo <CIM-UnixFile-PosixPrioIo>`
| ``string`` :ref:`FSName <CIM-UnixFile-FSName>`
| ``boolean`` :ref:`SetGid <CIM-UnixFile-SetGid>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string`` :ref:`LFName <CIM-UnixFile-LFName>`
| ``uint64`` :ref:`PathMax <CIM-UnixFile-PathMax>`
| ``uint64`` :ref:`LinkCount <CIM-UnixFile-LinkCount>`
| ``uint64`` :ref:`LinkMax <CIM-UnixFile-LinkMax>`
| ``uint64`` :ref:`PosixNoTrunc <CIM-UnixFile-PosixNoTrunc>`
| ``string`` :ref:`FileInodeNumber <CIM-UnixFile-FileInodeNumber>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``datetime`` :ref:`LastModifiedInode <CIM-UnixFile-LastModifiedInode>`
| ``string`` :ref:`CSCreationClassName <CIM-UnixFile-CSCreationClassName>`
| ``uint64`` :ref:`PosixChownRestricted <CIM-UnixFile-PosixChownRestricted>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``boolean`` :ref:`SaveText <CIM-UnixFile-SaveText>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

