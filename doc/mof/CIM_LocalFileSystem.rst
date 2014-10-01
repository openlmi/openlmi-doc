.. _CIM-LocalFileSystem:

CIM_LocalFileSystem
-------------------

Class reference
===============
Subclass of :ref:`CIM_FileSystem <CIM-FileSystem>`

A class derived from FileSystem that represents the file store controlled by a ComputerSystem through local means (e.g., direct device driver access). In this case, the file store is managed directly by the ComputerSystem without the need for another computer to act as a file server. This definition does not breakdown in the case of a Clustered File System. In this scenario, the FileSystem is a LocalFileSystem, weak to the Cluster.


Key properties
^^^^^^^^^^^^^^

| :ref:`CSName <CIM-FileSystem-CSName>`
| :ref:`Name <CIM-FileSystem-Name>`
| :ref:`CSCreationClassName <CIM-FileSystem-CSCreationClassName>`
| :ref:`CreationClassName <CIM-FileSystem-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

*None*

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint32`` :ref:`MaxFileNameLength <CIM-FileSystem-MaxFileNameLength>`
| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``string`` :ref:`CSName <CIM-FileSystem-CSName>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``uint32`` :ref:`ClusterSize <CIM-FileSystem-ClusterSize>`
| ``string`` :ref:`EncryptionMethod <CIM-FileSystem-EncryptionMethod>`
| ``boolean`` :ref:`ReadOnly <CIM-FileSystem-ReadOnly>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint64`` :ref:`ResizeIncrement <CIM-FileSystem-ResizeIncrement>`
| ``boolean`` :ref:`CasePreserved <CIM-FileSystem-CasePreserved>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``boolean`` :ref:`CaseSensitive <CIM-FileSystem-CaseSensitive>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint64`` :ref:`FileSystemSize <CIM-FileSystem-FileSystemSize>`
| ``string`` :ref:`OtherPersistenceType <CIM-FileSystem-OtherPersistenceType>`
| ``string`` :ref:`CompressionMethod <CIM-FileSystem-CompressionMethod>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`Name <CIM-FileSystem-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint64`` :ref:`BlockSize <CIM-FileSystem-BlockSize>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``uint64`` :ref:`NumberOfFiles <CIM-FileSystem-NumberOfFiles>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`Root <CIM-FileSystem-Root>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint16`` :ref:`PersistenceType <CIM-FileSystem-PersistenceType>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`FileSystemType <CIM-FileSystem-FileSystemType>`
| ``string`` :ref:`CSCreationClassName <CIM-FileSystem-CSCreationClassName>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16`` :ref:`IsFixedSize <CIM-FileSystem-IsFixedSize>`
| ``uint64`` :ref:`AvailableSpace <CIM-FileSystem-AvailableSpace>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16[]`` :ref:`CodeSet <CIM-FileSystem-CodeSet>`
| ``string`` :ref:`CreationClassName <CIM-FileSystem-CreationClassName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`

