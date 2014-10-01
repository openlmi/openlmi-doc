.. _LMI-SoftwareIdentityFileCheck:

LMI_SoftwareIdentityFileCheck
-----------------------------

Class reference
===============
Subclass of :ref:`CIM_FileSpecification <CIM-FileSpecification>`

Identifies both a physical file installed from RPM package and its original source in package. It represents a set of checks made to a single installed file provided by RPM package.


Key properties
^^^^^^^^^^^^^^

| :ref:`CheckID <CIM-Check-CheckID>`
| :ref:`TargetOperatingSystem <CIM-Check-TargetOperatingSystem>`
| :ref:`Name <CIM-Check-Name>`
| :ref:`SoftwareElementID <CIM-Check-SoftwareElementID>`
| :ref:`Version <CIM-Check-Version>`
| :ref:`SoftwareElementState <CIM-Check-SoftwareElementState>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-SoftwareIdentityFileCheck-CheckMode:

``boolean`` **CheckMode**

    The CheckMode property is used to indicate whether the condition is expected to exist or not exist in the environment. When the value is True, the condition is expected to exist (e.g., a file is expected to be on a system), so the Invoke methods are expected to return True. When the value is False, the condition is not expected to exist (e.g., a file is not to be on a system), so the Invoke methods are expected to return False.

    
.. _LMI-SoftwareIdentityFileCheck-FileExists:

``boolean`` **FileExists**

    True, if file is present on file system.

    
.. _LMI-SoftwareIdentityFileCheck-UserID:

``uint32`` **UserID**

    User ID of installed file.

    
.. _LMI-SoftwareIdentityFileCheck-Version:

``string`` **Version**

    Version of RPM package in EVRA form. It stands for Epoch, Version, Revision and Architecture. It has a specific format: <epoch>-<version>-<release>.<architecture>.

    
.. _LMI-SoftwareIdentityFileCheck-FileSizeOriginal:

``uint64`` **FileSizeOriginal**

    File size in Bytes from RPM database.

    
.. _LMI-SoftwareIdentityFileCheck-FileName:

``string`` **FileName**

    File name of verified file without any directory prefix.

    
.. _LMI-SoftwareIdentityFileCheck-ChecksumType:

``uint16`` **ChecksumType**

    Number of hash algorithm according to RFC4880. This algorithm is used for making checksums of RPM files and packages. This algorithm is same for the whole RPM database.

    
    ======== ===========
    ValueMap Values     
    ======== ===========
    0        UNKNOWN    
    1        MD5        
    2        SHA-1      
    3        RIPE-MD/160
    8        SHA256     
    9        SHA384     
    10       SHA512     
    11       SHA224     
    ======== ===========
    
.. _LMI-SoftwareIdentityFileCheck-LastModificationTime:

``uint64`` **LastModificationTime**

    Time of last modification of installed file as number a of seconds since the Epoch, 1970-01-01 00:00:00 +0000 (UTC). NULL if file does not exist.

    
.. _LMI-SoftwareIdentityFileCheck-LinkTargetOriginal:

``string`` **LinkTargetOriginal**

    Target destination of symbolic link from RPM database as returned by readlink. If file is not a symbolic link, NULL is returned.

    
.. _LMI-SoftwareIdentityFileCheck-FileModeFlags:

``uint8[]`` **FileModeFlags**

    File mode of installed file as an array of permissions. Each value represents a bit position in file mode.

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Execute Other
    1        Write Other  
    2        Read Other   
    3        Execute Group
    4        Write Group  
    5        Read Group   
    6        Execute User 
    7        Write User   
    8        Read User    
    9        Sticky       
    10       SGID         
    11       SUID         
    ======== =============
    
.. _LMI-SoftwareIdentityFileCheck-FileModeFlagsOriginal:

``uint8[]`` **FileModeFlagsOriginal**

    File mode as an array of permissions of file from RPM database. Each value represents a bit position in file mode.

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Execute Other
    1        Write Other  
    2        Read Other   
    3        Execute Group
    4        Write Group  
    5        Read Group   
    6        Execute User 
    7        Write User   
    8        Read User    
    9        Sticky       
    10       SGID         
    11       SUID         
    ======== =============
    
.. _LMI-SoftwareIdentityFileCheck-FileModeOriginal:

``uint32`` **FileModeOriginal**

    File mode as a number given by RPM database.

    
.. _LMI-SoftwareIdentityFileCheck-FileMode:

``uint32`` **FileMode**

    File mode of installed file as a number. NULL if file does not exist.

    
.. _LMI-SoftwareIdentityFileCheck-GroupIDOriginal:

``uint32`` **GroupIDOriginal**

    Group ID of file from RPM database.

    
.. _LMI-SoftwareIdentityFileCheck-FileTypeOriginal:

``uint16`` **FileTypeOriginal**

    File type of file in RPM database.

    
    ======== ================
    ValueMap Values          
    ======== ================
    0        Unknown         
    1        File            
    2        Directory       
    3        Symlink         
    4        FIFO            
    5        Character Device
    6        Block Device    
    ======== ================
    
.. _LMI-SoftwareIdentityFileCheck-TargetOperatingSystem:

``uint16`` **TargetOperatingSystem**

    The Target Operating System of the SoftwareElement being checked.

    
    ======== =====================================
    ValueMap Values                               
    ======== =====================================
    0        Unknown                              
    1        Other                                
    2        MACOS                                
    3        ATTUNIX                              
    4        DGUX                                 
    5        DECNT                                
    6        Tru64 UNIX                           
    7        OpenVMS                              
    8        HPUX                                 
    9        AIX                                  
    10       MVS                                  
    11       OS400                                
    12       OS/2                                 
    13       JavaVM                               
    14       MSDOS                                
    15       WIN3x                                
    16       WIN95                                
    17       WIN98                                
    18       WINNT                                
    19       WINCE                                
    20       NCR3000                              
    21       NetWare                              
    22       OSF                                  
    23       DC/OS                                
    24       Reliant UNIX                         
    25       SCO UnixWare                         
    26       SCO OpenServer                       
    27       Sequent                              
    28       IRIX                                 
    29       Solaris                              
    30       SunOS                                
    31       U6000                                
    32       ASERIES                              
    33       HP NonStop OS                        
    34       HP NonStop OSS                       
    35       BS2000                               
    36       LINUX                                
    37       Lynx                                 
    38       XENIX                                
    39       VM                                   
    40       Interactive UNIX                     
    41       BSDUNIX                              
    42       FreeBSD                              
    43       NetBSD                               
    44       GNU Hurd                             
    45       OS9                                  
    46       MACH Kernel                          
    47       Inferno                              
    48       QNX                                  
    49       EPOC                                 
    50       IxWorks                              
    51       VxWorks                              
    52       MiNT                                 
    53       BeOS                                 
    54       HP MPE                               
    55       NextStep                             
    56       PalmPilot                            
    57       Rhapsody                             
    58       Windows 2000                         
    59       Dedicated                            
    60       OS/390                               
    61       VSE                                  
    62       TPF                                  
    63       Windows (R) Me                       
    64       Caldera Open UNIX                    
    65       OpenBSD                              
    66       Not Applicable                       
    67       Windows XP                           
    68       z/OS                                 
    69       Microsoft Windows Server 2003        
    70       Microsoft Windows Server 2003 64-Bit 
    71       Windows XP 64-Bit                    
    72       Windows XP Embedded                  
    73       Windows Vista                        
    74       Windows Vista 64-Bit                 
    75       Windows Embedded for Point of Service
    76       Microsoft Windows Server 2008        
    77       Microsoft Windows Server 2008 64-Bit 
    78       FreeBSD 64-Bit                       
    79       RedHat Enterprise Linux              
    80       RedHat Enterprise Linux 64-Bit       
    81       Solaris 64-Bit                       
    82       SUSE                                 
    83       SUSE 64-Bit                          
    84       SLES                                 
    85       SLES 64-Bit                          
    86       Novell OES                           
    87       Novell Linux Desktop                 
    88       Sun Java Desktop System              
    89       Mandriva                             
    90       Mandriva 64-Bit                      
    91       TurboLinux                           
    92       TurboLinux 64-Bit                    
    93       Ubuntu                               
    94       Ubuntu 64-Bit                        
    95       Debian                               
    96       Debian 64-Bit                        
    97       Linux 2.4.x                          
    98       Linux 2.4.x 64-Bit                   
    99       Linux 2.6.x                          
    100      Linux 2.6.x 64-Bit                   
    101      Linux 64-Bit                         
    102      Other 64-Bit                         
    103      Microsoft Windows Server 2008 R2     
    104      VMware ESXi                          
    105      Microsoft Windows 7                  
    106      CentOS 32-bit                        
    107      CentOS 64-bit                        
    108      Oracle Linux 32-bit                  
    109      Oracle Linux 64-bit                  
    110      eComStation 32-bitx                  
    111      Microsoft Windows Server 2011        
    113      Microsoft Windows Server 2012        
    114      Microsoft Windows 8                  
    115      Microsoft Windows 8 64-bit           
    116      Microsoft Windows Server 2012 R2     
    ======== =====================================
    
.. _LMI-SoftwareIdentityFileCheck-Name:

``string`` **Name**

    Absolute path of file being checked.

    
.. _LMI-SoftwareIdentityFileCheck-UserIDOriginal:

``uint32`` **UserIDOriginal**

    User ID of file from RPM database.

    
.. _LMI-SoftwareIdentityFileCheck-FileType:

``uint16`` **FileType**

    File type of installed file. NULL if file does not exist.

    
    ======== ================
    ValueMap Values          
    ======== ================
    0        Unknown         
    1        File            
    2        Directory       
    3        Symlink         
    4        FIFO            
    5        Character Device
    6        Block Device    
    ======== ================
    
.. _LMI-SoftwareIdentityFileCheck-LastModificationTimeOriginal:

``uint64`` **LastModificationTimeOriginal**

    Time of last modification of file from RPM database as a number of secodns since the Epoch, 1970-01-01 00:00:00 +0000 (UTC).

    
.. _LMI-SoftwareIdentityFileCheck-FileChecksumOriginal:

``string`` **FileChecksumOriginal**

    Checksum of file from RPM database. Hash algorithm used can be obtained with ChecksumType property. It contains NULL for all file types but regular file.

    
.. _LMI-SoftwareIdentityFileCheck-LinkTarget:

``string`` **LinkTarget**

    Target destination of symbolic link as returned by readlink. If file is not a symbolic link or it's missing, NULL is returned.

    
.. _LMI-SoftwareIdentityFileCheck-SoftwareElementState:

``uint16`` **SoftwareElementState**

    The SoftwareElementState of the SoftwareElement being checked.

    
    ======== ===========
    ValueMap Values     
    ======== ===========
    0        Deployable 
    1        Installable
    2        Executable 
    3        Running    
    ======== ===========
    
.. _LMI-SoftwareIdentityFileCheck-GroupID:

``uint32`` **GroupID**

    Group ID of installed file.

    
.. _LMI-SoftwareIdentityFileCheck-MD5Checksum:

``string`` **MD5Checksum**

    MD5 checksum of installed file. It's computed only for regular files.

    
.. _LMI-SoftwareIdentityFileCheck-FailedFlags:

``uint16[]`` **FailedFlags**

    Returns array of flags representing test that did not pass. Note that not all tests are run on every file. Tests are selected depending on file type stored in package database. If the file is missing, no other tests are run. Flag is present in the output array if the test has been run and file did not pass it. Values representing tests being run are: "Existence" - it applies to every file type; "FileSize" - applies only to regular files and symbolic links; "FileMode" - includes check for permissions and file type. Permissions are not checked for symbolic links. "Checksum" - applies only to regular files; "Device Number" -  tests major/minor device number; "LinkTarget" - tested only on symbolic links; "UserID" and "GroupID" - apply to every file type; "Last Modification Time" is tested only on regular files.

    
    ======== ======================
    ValueMap Values                
    ======== ======================
    0        Existence             
    1        FileSize              
    2        FileMode              
    3        Checksum              
    4        Device Number         
    5        LinkTarget            
    6        UserID                
    7        GroupID               
    8        Last Modification Time
    ======== ======================
    
.. _LMI-SoftwareIdentityFileCheck-CheckID:

``string`` **CheckID**

    This contains InstanceID of asynchronous job if this check is a result of job invocation. Otherwise "LMI:LMI_SoftwareIdentityFileCheck" will be present. In former case, the format of value will be: "LMI:LMI_SoftwareVerificationJob:<id>", where <id> is job's identification number in decimal format.

    
.. _LMI-SoftwareIdentityFileCheck-SoftwareElementID:

``string`` **SoftwareElementID**

    This is an identifier for the SoftwareElement being checked.

    
.. _LMI-SoftwareIdentityFileCheck-FileSize:

``uint64`` **FileSize**

    Size of installed file in Bytes. It's NULL if file does not exist or it's not a regular file or symbolic link.

    
.. _LMI-SoftwareIdentityFileCheck-FileChecksum:

``string`` **FileChecksum**

    Checksum of installed file. Hash algorithm used can be obtained with ChecksumType property. This property contains valid value only for regular files. NULL is present if check could not be done.

    

Local methods
^^^^^^^^^^^^^

    .. _LMI-SoftwareIdentityFileCheck-Invoke:

``uint32`` **Invoke** ()

    The Invoke method evaluates this Check. The details of the evaluation are described by the specific subclasses of CIM_Check. When the SoftwareElement being checked is already installed, the CIM_InstalledSoftwareElement association identifies the CIM_ComputerSystem in whose context the Invoke is executed. If this association is not in place, then the InvokeOnSystem method should be used - since it identifies the TargetSystem as an input parameter of the method. 

    The results of the Invoke method are based on the return value. A zero is returned if the condition is satisfied. A one is returned if the method is not supported. Any other value indicates the condition is not satisfied.

    
    **Parameters**
    
*None*
    .. _LMI-SoftwareIdentityFileCheck-InvokeOnSystem:

``uint32`` **InvokeOnSystem** (:ref:`CIM_ComputerSystem <CIM-ComputerSystem>` TargetSystem)

    The InvokeOnSystem method evaluates this Check. The details of the evaluation are described by the specific subclasses of CIM_Check. The method's TargetSystem input parameter specifies the ComputerSystem in whose context the method is invoked. 

    The results of the InvokeOnSystem method are based on the return value. A zero is returned if the condition is satisfied. A one is returned if the method is not supported. Any other value indicates the condition is not satisfied.

    
    **Parameters**
    
        *IN* :ref:`CIM_ComputerSystem <CIM-ComputerSystem>` **TargetSystem**
            Reference to ComputerSystem in whose context the method is to be invoked.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint32`` :ref:`CRC1 <CIM-FileSpecification-CRC1>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``datetime`` :ref:`CreateTimeStamp <CIM-FileSpecification-CreateTimeStamp>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint32`` :ref:`CheckSum <CIM-FileSpecification-CheckSum>`
| ``uint32`` :ref:`CRC2 <CIM-FileSpecification-CRC2>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

