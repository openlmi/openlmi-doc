.. _CIM-LogicalFile:

CIM_LogicalFile
---------------

Class reference
===============
Subclass of :ref:`CIM_LogicalElement <CIM-LogicalElement>`

A LogicalFile is a named collection of data or executable code, or represents a LogicalDevice or Directory. It is located within the context of a FileSystem, on a Storage Extent.


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

.. _CIM-LogicalFile-Executable:

``boolean`` **Executable**

    Indicates the file is executable.

    
.. _CIM-LogicalFile-CSName:

``string`` **CSName**

    The scoping ComputerSystem's Name.

    
.. _CIM-LogicalFile-Readable:

``boolean`` **Readable**

    Boolean indicating that the File can be read.

    
.. _CIM-LogicalFile-EncryptionMethod:

``string`` **EncryptionMethod**

    A free form string indicating the algorithm or tool used to encrypt the LogicalFile. If it is not possible or not desired to describe the encryption scheme (perhaps for security reasons), recommend using the following words: "Unknown" to represent that it is not known whether the LogicalFile is encrypted or not, "Encrypted" to represent that the File is encrypted but either its encryption scheme is not known or not disclosed, and "Not Encrypted" to represent that the LogicalFile is not encrypted.

    
.. _CIM-LogicalFile-LastAccessed:

``datetime`` **LastAccessed**

    Time that the File was last accessed.

    
.. _CIM-LogicalFile-FSCreationClassName:

``string`` **FSCreationClassName**

    The scoping FileSystem's CreationClassName.

    
.. _CIM-LogicalFile-InUseCount:

``uint64`` **InUseCount**

    Integer indicating the number of 'file opens' that are currently active against the File.

    
.. _CIM-LogicalFile-LastModified:

``datetime`` **LastModified**

    Time that the File was last modified.

    
.. _CIM-LogicalFile-CompressionMethod:

``string`` **CompressionMethod**

    A free form string indicating the algorithm or tool used to compress the LogicalFile. If it is not possible or not desired to describe the compression scheme (perhaps because it is not known), recommend using the following words: "Unknown" to represent that it is not known whether the LogicalFile is compressed or not, "Compressed" to represent that the File is compressed but either its compression scheme is not known or not disclosed, and "Not Compressed" to represent that the LogicalFile is not compressed.

    
.. _CIM-LogicalFile-Writeable:

``boolean`` **Writeable**

    Boolean indicating that the File can be written.

    
.. _CIM-LogicalFile-Name:

``string`` **Name**

    The inherited Name serves as part of the key of a LogicalFile instance within a FileSystem. A unique identifier (such as a full path name) is required as a Name value. Since Files are weak to their FileSystem (and not to a Directory which would provide a more granular naming algorithm), care must be taken to make LogicalFile's Name unique for a given Creation ClassName and FileSystem. A full path name is one way to do this.

    
.. _CIM-LogicalFile-FSName:

``string`` **FSName**

    The scoping FileSystem's Name.

    
.. _CIM-LogicalFile-CSCreationClassName:

``string`` **CSCreationClassName**

    The scoping ComputerSystem's CreationClassName.

    
.. _CIM-LogicalFile-FileSize:

``uint64`` **FileSize**

    Size of the File in bytes.

    
.. _CIM-LogicalFile-CreationClassName:

``string`` **CreationClassName**

    CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

    
.. _CIM-LogicalFile-CreationDate:

``datetime`` **CreationDate**

    File's creation date.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

