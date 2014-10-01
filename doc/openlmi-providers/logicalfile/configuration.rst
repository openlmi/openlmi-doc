Configuration
=============

Configuration is stored in ``/etc/openlmi/logicalfile/logicalfile.conf``.

In addition to :ref:`common configuration options <common-configuration>`,
this provider can be configured to allow or deny various filesystem operations.
Default configuration::

  [LMI_UnixDirectory]
  # Allow user to create directories. (default = True)
  AllowMkdir=True

  # Allow user to remove empty directories. (default = True)
  AllowRmdir=True

  [LMI_SymbolicLink]
  # Allow user to create symbolic links. (default = False)
  AllowSymlink=False

Options and their values are self-explanatory.
