Overwrite policy
================

Before OpenLMI-Storage overwrites or deletes a device, it first checks if the
device is **unused**.

**Unused device**:

* Is not mounted.

* Is not part of running device, e.g. MD RAID, Volume Group or LUKS.

If a device is used, any operation which would overwrite or delete it returns
``CIM_Error`` with error message "Device XYZ is mounted" or "Device XYZ is used
by ABC". It is up to the application to first unmount the device, close the
LUKS/dm-crypt device, stop the RAID or  remove it from running Volume Group etc.
