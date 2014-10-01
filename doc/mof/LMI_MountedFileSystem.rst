.. _LMI-MountedFileSystem:

LMI_MountedFileSystem
---------------------

Class reference
===============
Subclass of :ref:`CIM_ManagedElement <CIM-ManagedElement>`

Class for representing mounted filesystems. Can be thought of as either an entry in /etc/mtab, or in /etc/fstab, according to its associated LMI_MountedFileSystemSetting.


Key properties
^^^^^^^^^^^^^^

| :ref:`MountPointPath <LMI-MountedFileSystem-MountPointPath>`
| :ref:`FileSystemSpec <LMI-MountedFileSystem-FileSystemSpec>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-MountedFileSystem-MountPointPath:

``string`` **MountPointPath**

    Path to a directory where the device is mounted.

    
.. _LMI-MountedFileSystem-FileSystemType:

``string`` **FileSystemType**

    Filesystem type.

    
.. _LMI-MountedFileSystem-FileSystemSpec:

``string`` **FileSystemSpec**

    Filesystem specification. Corresponds to the device field in /etc/fstab.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

