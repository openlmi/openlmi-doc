.. _LMI-FileSystemCapabilities:

LMI_FileSystemCapabilities
--------------------------

Class reference
===============
Subclass of :ref:`CIM_FileSystemCapabilities <CIM-FileSystemCapabilities>`

FileSystemCapabilities specifies the combination of properties that a FileSystemService can support when creating or maintaining FileSystems. Each supported combination of properties is specified by a FileSystemSetting that is associated with the FileSystemCapabilities element via ElementSettingData.

A FileSystemCapabilities element specifies the properties supported when using it.

This class *does not* provide a CreateGoal method! Use CreateSetting instead, which works similarly to LMI_StorageCapabilities.CreateSetting.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-FileSystemCapabilities-SupportedProperties:

``uint16[]`` **SupportedProperties**

    An array of property names of the Setting that this Capabilities element supports. The Object-related parameters are not specified because they must always be supported even if not used.

    
    ======== =======================
    ValueMap Values                 
    ======== =======================
    2        DataExtentsSharing     
    3        CopyTarget             
    4        FilenameCaseAttributes 
    5        FilenameStreamFormats  
    6        FilenameFormats        
    7        LockingSemantics       
    8        AuthorizationProtocols 
    9        AuthenticationProtocols
    10       Persistence            
    ..       DMTF Reserved          
    0x8000.. Vendor Defined         
    ======== =======================
    
.. _LMI-FileSystemCapabilities-SupportedPersistenceTypes:

``uint16[]`` **SupportedPersistenceTypes**

    **Deprecated!** 
    An array of enumerated values representing the persistence capabilities of the FileSystem. A value of "Persistent" indicates that the FileSystem supports persistence, can be preserved through an orderly shutdown and could be protected. A value of "Temporary" indicates that the FileSystem supports non-persistence, may not be protected and may not survive a shutdown. A value of "External" indicates that the FileSystem could controlled outside of the operating environment and may need to be protected by specialized means. A value of "Other" is provided to allow for additional persistence types, to be described in the OtherPersistenceType attribute, and is expected to be rarely, if ever, used.

    
    ======== ==========
    ValueMap Values    
    ======== ==========
    1        Other     
    2        Persistent
    3        Temporary 
    4        External  
    ======== ==========
    
.. _LMI-FileSystemCapabilities-ActualFileSystemType:

``uint16`` **ActualFileSystemType**

    An enumerated value that indicates the file system implementation type supported by this Capabilities.

    
    ======== =============
    ValueMap Values       
    ======== =============
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
    32769    EXT4         
    32770    BTRFS        
    32771    JFS          
    32772    TMPFS        
    32773    VFAT         
    ======== =============
    

Local methods
^^^^^^^^^^^^^

    .. _LMI-FileSystemCapabilities-LMI-CreateSetting:

``uint16`` **LMI_CreateSetting** (:ref:`LMI_FileSystemSetting <LMI-FileSystemSetting>` Setting)

    Creates a supported FileSystemSetting. Caller can modify the setting via ModifyInstance intrinsic method.Unlike CIM standard CreateGoal, LMI_CreateSetting works with references to LMI_FileSystemSetting stored on the CIMOM, not with embedded instances and does not require iterating through several CreateGoal calls. The functionality is very similar to CIM_StorageCapabilities and CIM_StorageSetting.

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Success      
    1        Not Supported
    4        Failed       
    ======== =============
    
    **Parameters**
    
        *OUT* :ref:`LMI_FileSystemSetting <LMI-FileSystemSetting>` **Setting**
            Created setting.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string[]`` :ref:`SupportedOtherPersistenceTypes <CIM-FileSystemCapabilities-SupportedOtherPersistenceTypes>`
| ``string`` :ref:`InstanceID <CIM-Capabilities-InstanceID>`
| ``uint16[]`` :ref:`SupportedOperations <CIM-FileSystemCapabilities-SupportedOperations>`
| ``string`` :ref:`ElementName <CIM-Capabilities-ElementName>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`GetRequiredStorageSize <CIM-FileSystemCapabilities-GetRequiredStorageSize>`
| :ref:`CreateGoalSettings <CIM-Capabilities-CreateGoalSettings>`
| :ref:`CreateGoal <CIM-FileSystemCapabilities-CreateGoal>`

