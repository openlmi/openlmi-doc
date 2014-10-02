Configuration
=============

Configuration is stored in ``/etc/openlmi/storage/storage.conf``.

In addition to :ref:`common configuration options <common-configuration>`,
this provider can be configured to allow or deny various filesystem operations.
Default configuration::

  [Log]
  # Toggles logging of detailed debug messages in Blivet.
  DebugBlivet=False

  [Storage]
  # Path to temporary directory. The provider (usually running as root) need
  # read/write access there. When SELinux or other security enhancement
  # mechanism is used, **only** the provider should have read/write access
  # to this directory.
  Tempdir=/tmp

Options and their values are self-explanatory.


Persistent setting
------------------

OpenLMI-Storage stores persistent data in ``/var/lib/openlmi-storage/``.
Typically, various :ref:`CIM_SettingData <CIM-SettingData>` instances with
:ref:`ChangeableType <CIM-SettingData-ChangeableType>`
``Changeable - Persistent`` are stored here.
