.. _CIM-UnixDeviceFile:

CIM_UnixDeviceFile
------------------

Class reference
===============
Subclass of :ref:`CIM_DeviceFile <CIM-DeviceFile>`

DeviceFile is a special type of LogicalFile that represents a Device. This class is a specialization of DeviceFile for a Unix environment.


Key properties
^^^^^^^^^^^^^^

| :ref:`FSCreationClassName <CIM-LogicalFile-FSCreationClassName>`
| :ref:`Name <CIM-LogicalFile-Name>`
| :ref:`CSName <CIM-LogicalFile-CSName>`
| :ref:`CSCreationClassName <CIM-LogicalFile-CSCreationClassName>`
| :ref:`CreationClassName <CIM-LogicalFile-CreationClassName>`
| :ref:`FSName <CIM-LogicalFile-FSName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-UnixDeviceFile-DeviceFileType:

``uint16`` **DeviceFileType**

    The type of device file.

    
    ======== =========
    ValueMap Values   
    ======== =========
    0        Unknown  
    1        Other    
    2        Block    
    3        Character
    ======== =========
    
.. _CIM-UnixDeviceFile-OtherTypeDescription:

``string`` **OtherTypeDescription**

    Additional information when the DeviceFileType property is set to "Other".

    
.. _CIM-UnixDeviceFile-DeviceDescription:

``string`` **DeviceDescription**

    Additional information provided by the driver. This property may be null if no information is available, or a general description of the device when available, e.g. "Non-rewind tape streamer".

    
.. _CIM-UnixDeviceFile-DeviceMinor:

``string`` **DeviceMinor**

    The Device's Minor Id.

    
.. _CIM-UnixDeviceFile-DeviceMajor:

``string`` **DeviceMajor**

    The Device's Major Id.

    
.. _CIM-UnixDeviceFile-DeviceId:

``string`` **DeviceId**

    The device Identifier: this is the st_rdev field in the stat structure.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``boolean`` :ref:`Executable <CIM-LogicalFile-Executable>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``string`` :ref:`CSName <CIM-LogicalFile-CSName>`
| ``boolean`` :ref:`Readable <CIM-LogicalFile-Readable>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`EncryptionMethod <CIM-LogicalFile-EncryptionMethod>`
| ``datetime`` :ref:`LastAccessed <CIM-LogicalFile-LastAccessed>`
| ``string`` :ref:`FSCreationClassName <CIM-LogicalFile-FSCreationClassName>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint64`` :ref:`InUseCount <CIM-LogicalFile-InUseCount>`
| ``datetime`` :ref:`LastModified <CIM-LogicalFile-LastModified>`
| ``string`` :ref:`CompressionMethod <CIM-LogicalFile-CompressionMethod>`
| ``uint64`` :ref:`FileSize <CIM-LogicalFile-FileSize>`
| ``boolean`` :ref:`Writeable <CIM-LogicalFile-Writeable>`
| ``string`` :ref:`Name <CIM-LogicalFile-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``string`` :ref:`FSName <CIM-LogicalFile-FSName>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`CSCreationClassName <CIM-LogicalFile-CSCreationClassName>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`CreationClassName <CIM-LogicalFile-CreationClassName>`
| ``datetime`` :ref:`CreationDate <CIM-LogicalFile-CreationDate>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

