.. _CIM-FileSystemConfigurationCapabilities:

CIM_FileSystemConfigurationCapabilities
---------------------------------------

Class reference
===============
Subclass of :ref:`CIM_Capabilities <CIM-Capabilities>`

FileSystemConfigurationCapabilities specifies the capability of a FileSystemConfigurationService to support the specified methods.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-FileSystemConfigurationCapabilities-SupportedActualFileSystemTypes:

``uint16[]`` **SupportedActualFileSystemTypes**

    An array of enumerated values that indicates the set of actual file system implementation types that this FileSystemConfigurationService can support in its Capabilities. For each file system type listed here, there MUST be at least one FileSystemCapabilities element.

    
    ======== ==============
    ValueMap Values        
    ======== ==============
    0        Unknown       
    2        UFS           
    3        HFS           
    4        FAT           
    5        FAT16         
    6        FAT32         
    7        NTFS4         
    8        NTFS5         
    9        XFS           
    10       AFS           
    11       EXT2          
    12       EXT3          
    13       REISERFS      
    ..       DMTF Reserved 
    0x8000.. Vendor Defined
    ======== ==============
    
.. _CIM-FileSystemConfigurationCapabilities-SupportedAsynchronousMethods:

``uint16[]`` **SupportedAsynchronousMethods**

    An array of methods of this Service that are supported as asynchronous methods.

    
    ======== ======================
    ValueMap Values                
    ======== ======================
    2        CreateFileSystem      
    3        DeleteFileSystem      
    4        ModifyFileSystem      
    5        CreateGoal            
    6        GetRequiredStorageSize
    ..       DMTF Reserved         
    0x8000.. Vendor Defined        
    ======== ======================
    
.. _CIM-FileSystemConfigurationCapabilities-InitialAvailability:

``uint16`` **InitialAvailability**

    An enumerated value that indicates the state of availability in which the Service can create the file system. The choices include 'Mounted' and 'Unmounted'. If 'Mounted', the mount-point will be at a vendor-specific default LogicalFile, and a MountedElement association will be surfaced.

    
    ======== ==============
    ValueMap Values        
    ======== ==============
    0        Unknown       
    2        Mounted       
    3        Unmounted     
    ..       DMTF Reserved 
    0x8000.. Vendor Defined
    ======== ==============
    
.. _CIM-FileSystemConfigurationCapabilities-SupportedSynchronousMethods:

``uint16[]`` **SupportedSynchronousMethods**

    An array of methods of this Service that are supported as synchronous methods.

    
    ======== ======================
    ValueMap Values                
    ======== ======================
    2        CreateFileSystem      
    3        DeleteFileSystem      
    4        ModifyFileSystem      
    5        CreateGoal            
    6        GetRequiredStorageSize
    ..       DMTF Reserved         
    0x8000.. Vendor Defined        
    ======== ======================
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`InstanceID <CIM-Capabilities-InstanceID>`
| ``string`` :ref:`ElementName <CIM-Capabilities-ElementName>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`CreateGoalSettings <CIM-Capabilities-CreateGoalSettings>`

