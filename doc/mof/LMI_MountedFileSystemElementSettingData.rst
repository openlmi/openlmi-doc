.. _LMI-MountedFileSystemElementSettingData:

LMI_MountedFileSystemElementSettingData
---------------------------------------

Class reference
===============
Subclass of :ref:`CIM_ElementSettingData <CIM-ElementSettingData>`

This association connects mounted file system (representing a mount) with options of the mount.

If IsNext property of this association is 1 ('Is Next'), the associated setting represents options of persistent mount stored in /etc/fstab. This setting will be applied on next machine reboot.

If IsCurrent property of this association is 1 ('Is Current'), the associated setting represents currently active options of the mounted filesystem.




Key properties
^^^^^^^^^^^^^^

| :ref:`SettingData <CIM-ElementSettingData-SettingData>`
| :ref:`ManagedElement <CIM-ElementSettingData-ManagedElement>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-MountedFileSystemElementSettingData-SettingData:

:ref:`LMI_MountedFileSystemSetting <LMI-MountedFileSystemSetting>` **SettingData**

    A setting attached to the mounted filesystem. Each filesystem can have two setting instances attached, one for currently mounted filesystem and one for a persistent setting (typically an fstab entry).

    
.. _LMI-MountedFileSystemElementSettingData-ManagedElement:

:ref:`LMI_MountedFileSystem <LMI-MountedFileSystem>` **ManagedElement**

    A mounted filesystem.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`IsMinimum <CIM-ElementSettingData-IsMinimum>`
| ``uint16`` :ref:`IsPending <CIM-ElementSettingData-IsPending>`
| ``uint16`` :ref:`IsNext <CIM-ElementSettingData-IsNext>`
| ``uint16`` :ref:`IsCurrent <CIM-ElementSettingData-IsCurrent>`
| ``uint16`` :ref:`IsMaximum <CIM-ElementSettingData-IsMaximum>`
| ``uint16`` :ref:`IsDefault <CIM-ElementSettingData-IsDefault>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

