SMI-S File Storage Profile
==========================

This profile is fully implemented. See the next chapter for its usage and
mapping to ``LMI_`` classes.

SMI-S Filesystem Profile
========================

OpenLMI-Storage implements the Filesystem Profile with these adjustments:

* Local Access is not implemented, we use LMI_MountService to mount local
  filesystems:

  * SMI-S expects that one filesystem can be mounted only once using Local
    Access, which is not true on Linux, we might mount one filesystem multiple
    times.

  * Mounting a filesystem is totally different operation to
    creating/modifying of a filesystem, these two functions should be
    separated. Therefore we introduce LMI_MountService to mount various
    filesystems.

* Directory Services are not implemented.


Implementation
--------------

All mandatory classes and methods are implemented.

Classes
^^^^^^^

Implemented SMI-S classes:

* :ref:`LMI_FileSystemSetting <LMI-FileSystemSetting>`

* :ref:`LMI_FileSystemElementSettingData <LMI-FileSystemElementSettingData>`

* :ref:`LMI_HostedFileSystem <LMI-HostedFileSystem>`

* :ref:`LMI_LocalFileSystem <LMI-LocalFileSystem>`

.. Following line produces "WARNING: undefined label: lmi-logicalfile" in storage
   docs, but the links is useful in overall documentation.

* :ref:`CIM_LogicalFile <CIM-LogicalFile>` using separate
  :ref:`LogicalFile provider <logicalfile-index>`
  from OpenLMI-Providers package.

Not implemented classes:

* ```CIM_FileStorage``

* ``SNIA_LocalAccessAvailable``

* ``SNIA_LocalFileSystem``

* ``SNIA_LocallyAccessibleFileSystemSetting``

* and all related references.

Methods
^^^^^^^

There are no methods in this profile.

.. warning::

   Mandatory indications are not implemented.

   Blivet does not provide such functionality and it would be very
   CPU-intensive to periodically scan for modified filesystems.


SMI-S Filesystem Manipulation Profile
=====================================

OpenLMI-Storage implements the Filesystem Profile with these adjustments:

* Local Access is not implemented, we use LMI_MountService to mount local
  filesystems:

  * SMI-S expects that one filesystem can be mounted only once using Local
    Access, which is not true on Linux, we might mount one filesystem multiple
    times.

  * Mounting a filesystem is totally different operation to
    creating/modifying of a filesystem, these two functions should be separated.

* Directory Services are not implemented.


Implementation
--------------

SNIA-specific classes and methods (with ``SNIA_`` prefix) are not implemented to
avoid any copyright problems - SNIA MOF files have a license which does not
allow us to implement it in open source project.

We implement our ``LMI_`` counterparts, inspired by CIM_StorageService and
CIM_StorageSetting. The major difference to ``CIM_`` and
``SNIA_FileSystemConfigurationService`` is that all methods accepts a Setting
argument as reference and not as embedded instance to match the rest of the
methods (mainly in Block Services profile).

Classes
^^^^^^^

Implemented SMI-S classes:

* :ref:`LMI_FileSystemConfigurationElementCapabilities <LMI-FileSystemConfigurationElementCapabilities>`

* :ref:`LMI_FileSystemElementSettingData <LMI-FileSystemElementSettingData>`

* :ref:`LMI_HostedFileSystem <LMI-HostedFileSystem>`

* :ref:`LMI_HostedStorageService <LMI-HostedStorageService>`

* :ref:`LMI_FileSystemCapabilities <LMI-FileSystemCapabilities>`

  * not derived from ``SNIA_FileSystemCapabilities``!

* :ref:`LMI_FileSystemConfigurationCapabilities <LMI-FileSystemConfigurationCapabilities>`

  * not derived from ``SNIA_FileSystemConfigurationCapabilities``!

* :ref:`LMI_FileSystemConfigurationService <LMI-FileSystemConfigurationService>`

  * not derived from ``SNIA_FileSystemConfigurationService``!

* :ref:`LMI_FileSystemSetting <LMI-FileSystemSetting>`

  * not derived from ``SNIA_FileSystemSetting``!

* :ref:`LMI_LocalFileSystem <LMI-LocalFileSystem>`

  * not derived from ``SNIA_LocalFileSystem``!

Not implemented classes:

* ``SNIA_FileSystemCapabilities``

* ``SNIA_FileSystemConfigurationCapabilities``

* ``SNIA_FileSystemConfigurationService``

* ``SNIA_FileSystemSetting``

* ``SNIA_LocalFileSystem``

* ``SNIA_LocalAccessAvailable``

* ``SNIA_LocallyAccessibleFileSystemCapabilities``

* ``SNIA_LocallyAccessibleFileSystemSetting``

* and all related references.

Methods
^^^^^^^

Implemented:

* :ref:`LMI_CreateSetting <LMI-FileSystemCapabilities-LMI-CreateSetting>`

* :ref:`LMI-CreateFileSystem <LMI-FileSystemConfigurationService-LMI-CreateFileSystem>`

  * Similar to plain CIM ``CreateFileSystem``, with these modifications:

    * ``Goal`` parameters is passed as reference and not as embedded
      instance, i.e. all :ref:`LMI_FileSystemSetting <LMI-FileSystemSetting>`
      instances reside on server and are created using
      :ref:`LMI_CreateSetting <LMI-FileSystemCapabilities-LMI-CreateSetting>`

    * Multiple extents can be passed in ``InExtents`` parameter. The
      method then creates one filesystem on multiple devices. Currently only
      btrfs supports this behavior, other filesystems can be created only on
      one device.

* :ref:`DeleteFileSystem <LMI-FileSystemConfigurationService-DeleteFileSystem>`

Not implemented:

* ``CreateGoalSettings``

* ``GetRequiredStorageSize``

* ``SNIA_CreateFileSystem``

* ``SNIA_ModifyFileSystem``

* :ref:`CreateFileSystem <CIM-FileSystemConfigurationService-CreateFileSystem>`

* :ref:`ModifyFileSystem <CIM-FileSystemConfigurationService-ModifyFileSystem>`

.. warning::

   Mandatory indications are not implemented.
   
   Blivet does not provide such functionality and it would be very CPU-intensive
   to periodically scan for modified filesystems.
