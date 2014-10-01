.. _LMI-MountedFileSystemSetting:

LMI_MountedFileSystemSetting
----------------------------

Class reference
===============
Subclass of :ref:`CIM_SettingData <CIM-SettingData>`

Class for representing mount options. Basic boolean properties represent filesystem independent mount options (as listed in mount(8)).


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-MountedFileSystemSetting-InterpretDevices:

``boolean`` **InterpretDevices**

    Interpret character or block special devices on the filesystem.Corresponds to 'dev' mount option.

    
.. _LMI-MountedFileSystemSetting-Silent:

``boolean`` **Silent**

    Turn on the silent flag. Corresponds to 'silent' mount option.

    
.. _LMI-MountedFileSystemSetting-UpdateAccessTimes:

``boolean`` **UpdateAccessTimes**

    Update inode access times on this filesystem. Corresponds to 'atime' mount option.

    
.. _LMI-MountedFileSystemSetting-AllowSUID:

``boolean`` **AllowSUID**

    Allow set-user-identifier or set-group-identifier bits to take effect. Corresponds to 'suid' mount option.

    
.. _LMI-MountedFileSystemSetting-UpdateFullAccessTimes:

``boolean`` **UpdateFullAccessTimes**

    Allows to explicitly requesting full atime updates. This makes it possible for kernel to defaults to relatime or noatime but still allow userspace to override it. Corresponds to 'strictatime' mount option.

    
.. _LMI-MountedFileSystemSetting-AllowExecution:

``boolean`` **AllowExecution**

    Permit execution of binaries. Corresponds to 'exec' mount option.

    
.. _LMI-MountedFileSystemSetting-Auto:

``boolean`` **Auto**

    Mount automatically at boot-up. Corresponds to 'auto' mount option. This option is only relevant in /etc/fstab.

    
.. _LMI-MountedFileSystemSetting-AllowUserMount:

``boolean`` **AllowUserMount**

    Allow an ordinary user to mount the filesystem. Corresponds to 'user' mount option. This option is only relevant in /etc/fstab.

    
.. _LMI-MountedFileSystemSetting-UpdateDirectoryAccessTimes:

``boolean`` **UpdateDirectoryAccessTimes**

    Update directory inode access times on this filesystem. This is the default. Corresponds to 'diratime' mount option.

    
.. _LMI-MountedFileSystemSetting-OtherOptions:

``string[]`` **OtherOptions**

    Other mount options that can be filesystem specific. This property is also used to specify options with values (e.g. uid=0 or gid=100). OtherOptions are appended (in the same order as they appear in the array) to the basic options.

    
.. _LMI-MountedFileSystemSetting-UpdateRelativeAccessTimes:

``boolean`` **UpdateRelativeAccessTimes**

    Update inode access times relative to modify or change time. Access time is only updated if the previous access time was earlier than the current modify or change time. Corresponds to 'relatime' mount option.

    
.. _LMI-MountedFileSystemSetting-AllowWrite:

``boolean`` **AllowWrite**

    Mount the filesystem read-write. If false, mount read-only.Corresponds to 'rw' mount option.

    
.. _LMI-MountedFileSystemSetting-FileSystemCheckOrder:

``uint16`` **FileSystemCheckOrder**

    Used by the fsck(8) program to determine the order in which filesystem checks are done at reboot time. The root filesystem should be specified with a 1, other filesystems with a 2. Filesystems within a drive are checked sequentially, but filesystems on different drives are checked in parallel. This option is only relevant in /etc/fstab.

    
.. _LMI-MountedFileSystemSetting-AllowMandatoryLock:

``boolean`` **AllowMandatoryLock**

    Allow mandatory locks on this filesystem. See fcntl(2). Corresponds to 'mand' mount option.

    
.. _LMI-MountedFileSystemSetting-Dump:

``boolean`` **Dump**

    This field is used for these filesystems by the dump(8) command to determine which filesystems need to be dumped. If the field is not present, a value of zero is returned and dump will assume that the filesystem does not need to be dumped. This option is only relevant in /etc/fstab.

    
.. _LMI-MountedFileSystemSetting-SynchronousDirectoryUpdates:

``boolean`` **SynchronousDirectoryUpdates**

    All directory updates within the filesystem should be done synchronously. This affects the following system calls: creat, link, unlink, symlink, mkdir, rmdir, mknod and rename. Corresponds to 'dirsync' mount option.

    
.. _LMI-MountedFileSystemSetting-SynchronousIO:

``boolean`` **SynchronousIO**

    All I/O to the filesystem should be done synchronously. In case of media with limited number of write cycles (e.g. some flash drives), this option may cause life-cycle shortening. Corresponds to 'sync' mount option.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`InstanceID <CIM-SettingData-InstanceID>`
| ``string`` :ref:`ElementName <CIM-SettingData-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`ConfigurationName <CIM-SettingData-ConfigurationName>`
| ``string`` :ref:`SoOrgID <CIM-SettingData-SoOrgID>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`SoID <CIM-SettingData-SoID>`
| ``uint16`` :ref:`ChangeableType <CIM-SettingData-ChangeableType>`
| ``string[]`` :ref:`ComponentSetting <CIM-SettingData-ComponentSetting>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

