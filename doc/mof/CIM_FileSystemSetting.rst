.. _CIM-FileSystemSetting:

CIM_FileSystemSetting
---------------------

Class reference
===============
Subclass of :ref:`CIM_SettingData <CIM-SettingData>`

The FileSystemSetting describes the attribute values set when creating a FileSystem by a FileSystemConfigurationService. These settings can be associated via the ElementSettingData association with the created FileSystem. If the setting is associated via SettingAssociatedToCapabilities to a FileSystemCapabilities, it is one of the canned settings supported by this capabilities instance. A setting can also be an embedded instance parameter to a method (for instance, when used as a Goal parameter). 

A NULL value for a property in a canned setting indicates support for a vendor-specific default. A NULL value for a property when the setting is used as a Goal parameter to a method indicates that the client does not care what value that property will have on creation and will accept any vendor-supplied default. When used with a FileSystem, a NULL value for a property must be interpreted as "Unknown". The ActualFileSystemType property cannot have a default value in any context. If this Setting is associated with a FileSystemCapabilities element via SettingAssociatedToCapabilities, the value of ActualFileSystemType in the Setting and the Capabilities MUST match. 

This class also supports persistence and recoverability of a FileSystem and its contained elements as defined in CIM 2.8 for the use of DatabaseStorageArea.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-FileSystemSetting-FilenameLengthMax:

``uint16[]`` **FilenameLengthMax**

    An array of integers that specify the maximum number of characters in a filename corresponding to an entry in the FilenameFormats property. 

    An entry of '0xFFFF' (the largest 16-bit integer) is interpreted as an indefinite length.

    
.. _CIM-FileSystemSetting-FilenameStreamFormats:

``uint16[]`` **FilenameStreamFormats**

    An array of enumerated integers representing the filename stream formats that the file system can support for access. The interpretation of these stream formats can be specific to vendors, or provided by some standard. But even within those constraints, the interpretation could be locale-specific or version-specific. For instance, Bytestream is locale-specific and is interpreted as ASCII for NFS v2 and v3 but UTF-8 in NFS v4. This additional information will normally be provided in the setting for the protocol used to access an element of this file system.

    
    ======== =======================
    ValueMap Values                 
    ======== =======================
    1        ASCII                  
    2        WideChar               
    3        MBCS                   
    4        UTF-8                  
    5        UNICODE UCS-16         
    6        UNICODE UCS-32         
    7        CIFS Client-interpreted
    8        Bytestream             
    ..       DMTF Reserved          
    0x8000.. Vendor Defined         
    ======== =======================
    
.. _CIM-FileSystemSetting-ObjectSizeMax:

``uint64[]`` **ObjectSizeMax**

    An array of integers that specifies the maximum size of objects (corresponding to the entry in the ObjectTypes array) that this FileSystem will "normally" contain. A value of 0 implies that there is no specific maximum associated with this setting.

    
.. _CIM-FileSystemSetting-FilenameFormats:

``uint16[]`` **FilenameFormats**

    An array of enumerated values that specify the filename formats supported on this FileSystem for naming files. Some common formats are: 

    a) DOS 8.3 

    b) VMS 'name.extension;version' where the extension specifies a file type 

    c) Unix name (file type is not specified in the name) 

    d) Windows 'name{.ext}*' where any of the exts can specify a file type 

    For each entry in this array there is an associated maximum length for the name and an associated reserved set of characters. 

    The interpretation of the maximum length of the name as well as the FilenameReservedCharacterSet string is vendor-specific.

    
    ======== =================
    ValueMap Values           
    ======== =================
    1        DOS8.3           
    2        Unix             
    3        VMS              
    4        Windows LongNames
    ..       DMTF Reserved    
    0x8000.. Vendor Defined   
    ======== =================
    
.. _CIM-FileSystemSetting-DataExtentsSharing:

``uint16`` **DataExtentsSharing**

    An enumerated value that specifies if the FileSystem supports or enforces sharing of data extents between objects.

    
    ======== =========================
    ValueMap Values                   
    ======== =========================
    0        Unknown                  
    1        No Sharing               
    2        Sharing Possible/Optional
    3        Sharing Enforced         
    ..       DMTF Reserved            
    0x8000.. Vendor Defined           
    ======== =========================
    
.. _CIM-FileSystemSetting-ObjectTypes:

``uint16[]`` **ObjectTypes**

    An array of enumerated values that specifies the set of object types that this FileSystem supports. This array is associated with a number of correspondingly indexed properties that specify the size and number of such objects. 

    When used as a goal, the client needs to specify only the subset of objects that they wish to specify; when used in a Setting associated with the FileSystem, this should contain all the types that the provider knows about; when used in a Setting associated with a Capabilities, this may only contain the types that the client can modify.

    "inodes" indicates that the number of required inodes is specified."files" indicates that the number of required files is specified."directories" indicates that the number of required directories is specified."links" indicates that the number of required links is specified."devices" indicates that the number of required devices is specified."files/directories" indicates that the number of required files and directories is specified."blocks" indicates that the size of required storage in client-specific storage units is specified. This represents the desired size of available space in the filesystem, exclusive of space reserved for meta-data and for other system functions. If "blocks" is specified, the corresponding ObjectSize properties must all be the same and must specify the intended size of the blocks in bytes.

    
    ======== =================
    ValueMap Values           
    ======== =================
    2        inodes           
    3        files            
    4        directories      
    5        links            
    6        devices          
    7        files/directories
    8        Blocks           
    ..       DMTF Reserved    
    0x8000.. Vendor Defined   
    ======== =================
    
.. _CIM-FileSystemSetting-CopyTarget:

``uint16`` **CopyTarget**

    An enumerated value that specifies if this FileSystem can be a target for synchronization with or mirror of another FileSystem, or if it cannot be a target.

    
    ======== ===============================
    ValueMap Values                         
    ======== ===============================
    0        Unknown                        
    1        Can be a Primary only          
    2        Can be a Mirror only           
    3        Can be a Synchronization Target
    4        Can be a Backup Target         
    5        Write Once                     
    ..       DMTF Reserved                  
    0x8000.. Vendor Defined                 
    ======== ===============================
    
.. _CIM-FileSystemSetting-FilenameCaseAttributes:

``uint16`` **FilenameCaseAttributes**

    An enumerated value that specifies how this FileSystem supports the case of characters in the Filename. Note that the host and the service may support multiple conflicting features, but each FileSystem must be configured with only one of the supported features.

    
    ======== ==============================
    ValueMap Values                        
    ======== ==============================
    0        Unknown                       
    1        Case-sensitive                
    2        Case-forced to upper case     
    3        Case-forced to lower-case     
    4        Case-indifferent but lost     
    5        Case-indifferent but preserved
    ..       DMTF Reserved                 
    0x8000.. Vendor Defined                
    ======== ==============================
    
.. _CIM-FileSystemSetting-SupportedAuthorizationProtocols:

``uint16[]`` **SupportedAuthorizationProtocols**

    An array of enumerated values that represent the authorization protocols that the FileSystem will support for access to objects by users, groups, accounts, etc. A FileSystem can support more than one authorization protocol.

    
    ======== =================
    ValueMap Values           
    ======== =================
    1        Posix Permissions
    2        Posix ACLs       
    3        NFSv4 ACLs       
    4        NTFS4            
    5        NTFS5            
    ..       DMTF Reserved    
    0x8000.. Vendor Defined   
    ======== =================
    
.. _CIM-FileSystemSetting-ObjectSizeMin:

``uint64[]`` **ObjectSizeMin**

    An array of integers that specifies the minimum size of objects (corresponding to the entry in the ObjectTypes array) that this FileSystem will "normally" contain. A value of 0 implies that there is no specific minimum associated with this setting.

    
.. _CIM-FileSystemSetting-SupportedAuthenticationProtocols:

``uint16[]`` **SupportedAuthenticationProtocols**

    An array of enumerated values that represent the authentication protocols that the FileSystem will support for access to objects by users, groups, accounts, etc.. 

    An entry of '0' is not allowed. 

    A FileSystem can support more than one authentication protocol.

    
    ======== =============================
    ValueMap Values                       
    ======== =============================
    1        AUTH_NONE                    
    2        AUTH_SYS                     
    3        AUTH_DH                      
    4        AUTH_KRB4                    
    5        AUTH_KRB5                    
    6        RPCSEC_GSS LIPKEY            
    7        RPCSEC_GSS SPKM-3            
    8        RPCSEC_GSS Challenge-Response
    9        NTLM v1                      
    10       NTLM v2                      
    11       Plain Text                   
    ..       DMTF Reserved                
    0x8000.. Vendor Defined               
    ======== =============================
    
.. _CIM-FileSystemSetting-NumberOfObjects:

``uint64[]`` **NumberOfObjects**

    An array of integers that specifies the number of objects (corresponding to the entry in the ObjectTypes array) that this FileSystem will "normally" contain. A value of 0 implies that there is no specific number associated with this setting. When the Setting is associated with a FileSystemCapabilities element, this is the default; When the Setting is associated with a FileSystem element, this is the expected value; When the Setting is used as an embedded parameter to a method this is the goal.

    
.. _CIM-FileSystemSetting-FilenameReservedCharacterSet:

``string[]`` **FilenameReservedCharacterSet**

    An array of strings that specifies the characters that may not appear in the name of any file contained by this FileSystem corresponding to the entry in the FilenameFormats property. 

    Note: It is not clear exactly how this works with the FilenameStreamFormats property above, since the format implicitly specifies the set of allowed characters.

    
.. _CIM-FileSystemSetting-SupportedLockingSemantics:

``uint16[]`` **SupportedLockingSemantics**

    An array of enumerated values that represent the locking semantics that the FileSystem can support for controlled access. A file system can support more than one locking model. Just because a file system supports more than one model does not imply that it supports them simultaneously for an element.

    
    ======== ============================
    ValueMap Values                      
    ======== ============================
    1        NLM/NFSv3                   
    2        NFSv4 Share Reservations    
    3        NFSv4 Byte-range locking    
    4        NFSv4 Delegations           
    5        CIFS Sharing locks          
    6        CIFS Byte-range locks       
    7        CIFS Exclusive/Batch oplocks
    8        CIFS Level II oplocks       
    ..       DMTF Reserved               
    0x8000.. Vendor Defined              
    ======== ============================
    
.. _CIM-FileSystemSetting-NumberOfObjectsMin:

``uint64[]`` **NumberOfObjectsMin**

    An array of integers that specifies the minimum number of objects (corresponding to the entry in the ObjectTypes array) that this FileSystem MUST be able to contain. A value of 0 implies that there is no specific minimum associated with this setting.

    
.. _CIM-FileSystemSetting-NumberOfObjectsMax:

``uint64[]`` **NumberOfObjectsMax**

    An array of integers that specifies the maximum number of objects (corresponding to the entry in the ObjectTypes array) that this FileSystem MUST be able to contain. A value of 0 implies that there is no specific maximum associated with this setting.

    
.. _CIM-FileSystemSetting-OtherPersistenceTypes:

``string[]`` **OtherPersistenceTypes**

    An array of strings describing the persistence attributes where the corresponding entry in the PersistenceTypes property has a value of "Other". This value is ignored in all other cases.

    
.. _CIM-FileSystemSetting-ActualFileSystemType:

``uint16`` **ActualFileSystemType**

    An enumerated value that indicates the file system implementation type supported by this Setting. This property MUST exist and have a value.

    
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
    
.. _CIM-FileSystemSetting-ObjectSize:

``uint64[]`` **ObjectSize**

    An array of integers that specifies the size of objects (corresponding to the entry in the ObjectTypes array) that this FileSystem will "normally" contain. A value of 0 implies that there is no specific number associated with this setting. When the Setting is associated with a FileSystemCapabilities element, this is the default; When the Setting is associated with a FileSystem element, this is the expected value; When the Setting is used as an embedded parameter to a method this is the goal.

    
.. _CIM-FileSystemSetting-PersistenceTypes:

``uint16[]`` **PersistenceTypes**

    An array of enumerated values representing the persistence attributes of the FileSystem. A value of "Persistent" indicates that the FileSystem supports persistence, can be preserved through an orderly shutdown and could be protected. A value of "Temporary" indicates that the FileSystem supports non-persistence, may not be protected and may not survive a shutdown. A value of "External" indicates that the FileSystem could controlled outside of the operating environment and may need to be protected by specialized means. A value of "Other" is provided to allow for additional persistence types, to be described in the corresponding entry of the OtherPersistenceTypes property, and is expected to be rarely, if ever, used.

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Unknown      
    1        Other        
    2        Persistent   
    3        Temporary    
    4        External     
    5..      DMTF Reserved
    ======== =============
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`InstanceID <CIM-SettingData-InstanceID>`
| ``string`` :ref:`ElementName <CIM-SettingData-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`ConfigurationName <CIM-SettingData-ConfigurationName>`
| ``string`` :ref:`SoOrgID <CIM-SettingData-SoOrgID>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`SoID <CIM-SettingData-SoID>`
| ``uint16`` :ref:`ChangeableType <CIM-SettingData-ChangeableType>`
| ``string[]`` :ref:`ComponentSetting <CIM-SettingData-ComponentSetting>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

