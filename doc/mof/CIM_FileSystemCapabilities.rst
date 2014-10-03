.. _CIM-FileSystemCapabilities:

CIM_FileSystemCapabilities
--------------------------

Class reference
===============
Subclass of :ref:`CIM_Capabilities <CIM-Capabilities>`

FileSystemCapabilities specifies the combination of properties that a FileSystemService can support when creating or maintaining FileSystems. Each supported combination of properties is specified by a FileSystemSetting that is associated with the FileSystemCapabilities element via ElementSettingData. 

A FileSystemCapabilities element specifies the properties supported when using it. 

This class provides a CreateGoal method that can be used to create a FileSystemSetting element that can be used as a goal for creating or modifying a filesystem. This class also supports persistence and recoverability of a FileSystem and its contained elements as defined in CIM 2.8 for the use of DatabaseStorageArea.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-FileSystemCapabilities-SupportedProperties:

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
    
.. _CIM-FileSystemCapabilities-SupportedOtherPersistenceTypes:

``string[]`` **SupportedOtherPersistenceTypes**

    **Deprecated!** 
    An array of strings describing the persistence capabilities where the corresponding entry in SupportedPersistenceTypes has a value of "Other". This value is ignored in all other cases.

    
.. _CIM-FileSystemCapabilities-SupportedPersistenceTypes:

``uint16[]`` **SupportedPersistenceTypes**

    An array of enumerated values representing the persistence capabilities of the FileSystem. A value of "Persistent" indicates that the FileSystem supports persistence, can be preserved through an orderly shutdown and could be protected. A value of "Temporary" indicates that the FileSystem supports non-persistence, may not be protected and may not survive a shutdown. A value of "External" indicates that the FileSystem could controlled outside of the operating environment and may need to be protected by specialized means. A value of "Other" is provided to allow for additional persistence types, to be described in the OtherPersistenceType attribute, and is expected to be rarely, if ever, used.

    
    ======== ==========
    ValueMap Values    
    ======== ==========
    1        Other     
    2        Persistent
    3        Temporary 
    4        External  
    ======== ==========
    
.. _CIM-FileSystemCapabilities-SupportedOperations:

``uint16[]`` **SupportedOperations**

    An array of enumerated values representing the operations to files and directories on the file system. Set of supported operations depends on the file system type. The operation information is used as the action type in the access control management.

    
    ======== ================
    ValueMap Values          
    ======== ================
    1        Read            
    2        Write           
    3        Execute         
    4        Create          
    5        Rename          
    6        Delete          
    7        Change Attribute
    ..       DMTF Reserved   
    0x8000.. Vendor Reserved 
    ======== ================
    
.. _CIM-FileSystemCapabilities-ActualFileSystemType:

``uint16`` **ActualFileSystemType**

    An enumerated value that indicates the file system implementation type supported by this Capabilities.

    
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
    

Local methods
^^^^^^^^^^^^^

    .. _CIM-FileSystemCapabilities-GetRequiredStorageSize:

``uint64`` **GetRequiredStorageSize** (``string`` FileSystemGoal, ``string`` ExtentSetting, ``uint64`` ExpectedSize, ``uint64`` MinimumSizeAcceptable, ``uint64`` MaximumSizeUsable)

    This method returns the "expected" size of StorageExtent that would support a file system specified by the input FileSystemGoal parameter assuming that the other settings for the StorageExtent are specified by the ExtentSetting parameter. 

    If the input FileSystemGoal or the ExtentSetting are NULL, this method returns a value computed by using the default FileSystemSetting or some vendor-specific canned StorageSetting. 

    A value of 0 is returned if this method is not able to determine a reasonable size or does not restrict sizes based on setting information.

    
    **Parameters**
    
        *IN* ``string`` **FileSystemGoal**
            FileSystemGoal is an element of class CIM_FileSystemSetting, or a derived class, encoded as a string-valued embedded object parameter, that is used to specify the settings for the FileSystem to be created.

            
        
        *IN* ``string`` **ExtentSetting**
            ExtentSetting is an element of class CIM_StorageSetting, or a derived class, encoded as a string-valued embedded object parameter, that is used to specify the settings of the StorageExtent to be used for this FileSystem.

            
        
        *OUT* ``uint64`` **ExpectedSize**
            A number that indicates the size of the storage extent that this FileSystem is expected to need. A value of 0 indicates that there is no expected size.

            
        
        *OUT* ``uint64`` **MinimumSizeAcceptable**
            A number that indicates the size of the smallest storage extent that would support the specified FileSystem. A value of 0 indicates that there is no minimum size.

            
        
        *OUT* ``uint64`` **MaximumSizeUsable**
            A number that indicates the size of the largest storage extent that would be usable for the specified FileSystem. A value of 0 indicates that there is no maximum size.

            
        
    
    .. _CIM-FileSystemCapabilities-CreateGoal:

``uint16`` **CreateGoal** (:ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, ``string`` TemplateGoal, ``string`` SupportedGoal)

    Start a job to create a supported FileSystemSetting from a FileSystemSetting provided by the caller. If the operation completes successfully and did not require a long-running ConcreteJob, it will return 0. If 4096/0x1000 is returned, a ConcreteJob will be started to create the element. A Reference to the ConcreteJob will be returned in the output parameter Job. 

    This method MAY return a CIM_Error representing that a single named property of a setting (or other) parameter (either reference or embedded object) has an invalid value or that an invalid combination of named properties of a setting (or other) parameter (either reference or embedded object) has been requested. 

    If the input TemplateGoal is NULL or the empty string, this method returns a default FileSystemSetting that is supported by this FileSystemCapabilities. 

    The output is returned as the SupportedGoal parameter. Both TemplateGoal and SupportedGoal are embedded objects and do not exist in the provider but are maintained by the client. 

    If the TemplateGoal specifies values that cannot be supported this method MUST return an appropriate error and should return a best match for a SupportedGoal.

    
    ============ =======================================================
    ValueMap     Values                                                 
    ============ =======================================================
    0            Job Completed with No Error                            
    1            Not Supported                                          
    2            Unknown                                                
    3            Timeout                                                
    4            Failed                                                 
    5            Invalid Parameter                                      
    6            TemplateGoal is not well-formed                        
    7            TemplateGoal cannot be satisfied exactly               
    8            StorageSetting cannot be used with ActualFileSystemType
    9            StorageSetting cannot be used with CopyTarget          
    10           StorageSetting cannot be used with ObjectType          
    ..           DMTF Reserved                                          
    4097         Method Parameters Checked - Job Started                
    4098..32767  Method Reserved                                        
    32768..65535 Vendor Specific                                        
    ============ =======================================================
    
    **Parameters**
    
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *IN* ``string`` **TemplateGoal**
            TemplateGoal is an element of class CIM_FileSystemSetting, or a derived class, encoded as a string-valued embedded object parameter, that is used as the template to be matched .

            
        
        *OUT* ``string`` **SupportedGoal**
            SupportedGoal is an element of class CIM_FileSystemSetting, or a derived class, encoded as a string-valued embedded object parameter, that is used to return the best supported match to the TemplateGoal.

            
        
    

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

