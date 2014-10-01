.. _CIM-SymbolicLink:

CIM_SymbolicLink
----------------

Class reference
===============
Subclass of :ref:`CIM_LogicalFile <CIM-LogicalFile>`

This class is a special type of LogicalFile that represents a Symbolic Link. This convention is useful for some operating systems that want to represent a single file in multiple places or a single file that is represented via multiple names.


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

.. _CIM-SymbolicLink-TargetFile:

``string`` **TargetFile**

    The target file of the symbolic link.

    

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
| ``uint64`` :ref:`FileSize <CIM-LogicalFile-FileSize>`
| ``string`` :ref:`CreationClassName <CIM-LogicalFile-CreationClassName>`
| ``datetime`` :ref:`CreationDate <CIM-LogicalFile-CreationDate>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

