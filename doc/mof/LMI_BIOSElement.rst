.. _LMI-BIOSElement:

LMI_BIOSElement
---------------

Class reference
===============
Subclass of :ref:`CIM_BIOSElement <CIM-BIOSElement>`

BIOSElement represents the low-level software that is loaded into non-volatile storage and used to bring up and configure a ComputerSystem.


Key properties
^^^^^^^^^^^^^^

| :ref:`TargetOperatingSystem <CIM-SoftwareElement-TargetOperatingSystem>`
| :ref:`Name <CIM-SoftwareElement-Name>`
| :ref:`SoftwareElementID <CIM-SoftwareElement-SoftwareElementID>`
| :ref:`Version <CIM-SoftwareElement-Version>`
| :ref:`SoftwareElementState <CIM-SoftwareElement-SoftwareElementState>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-BIOSElement-InstanceID:

``string`` **InstanceID**

    InstanceID is an optional property that may be used to opaquely and uniquely identify an instance of this class within the scope of the instantiating Namespace. Various subclasses of this class may override this property to make it required, or a key. Such subclasses may also modify the preferred algorithms for ensuring uniqueness that are defined below.

    To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon (:), and where <OrgID> must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness, <OrgID> must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If not null and the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance. 

    If not set to null for DMTF-defined instances, the "preferred" algorithm must be used with the <OrgID> set to CIM.

    
.. _LMI-BIOSElement-Version:

``string`` **Version**

    Software Version should be in the form <Major>.<Minor>.<Revision> or <Major>.<Minor><letter><revision>.

    
.. _LMI-BIOSElement-ElementName:

``string`` **ElementName**

    A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. 

    Note that the Name property of ManagedSystemElement is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. Note that if there is an associated instance of CIM_EnabledLogicalElementCapabilities, restrictions on this properties may exist as defined in ElementNameMask and MaxElementNameLen properties defined in that class.

    
.. _LMI-BIOSElement-Description:

``string`` **Description**

    The Description property provides a textual description of the object.

    
.. _LMI-BIOSElement-ReleaseDate:

``datetime`` **ReleaseDate**

    Date that this BIOS was released.

    
.. _LMI-BIOSElement-Manufacturer:

``string`` **Manufacturer**

    Manufacturer of this SoftwareElement.

    
.. _LMI-BIOSElement-TargetOperatingSystem:

``uint16`` **TargetOperatingSystem**

    The TargetOperatingSystem property specifies the element's operating system environment. The value of this property does not ensure that it is binary executable. Two other pieces of information are needed. First, the version of the OS needs to be specified using the class, CIM_OSVersion Check. The second piece of information is the architecture that the OS runs on. This information is verified using CIM_ArchitectureCheck. The combination of these constructs clearly identifies the level of OS required for a particular SoftwareElement.

    
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
    
.. _LMI-BIOSElement-ListOfLanguages:

``string[]`` **ListOfLanguages**

    A list of installable languages for the BIOS. This information can be obtained from SMBIOS, from the string list that follows the Type 13 structure. An ISO 639 Language Name should be used to specify the BIOS' installable languages. The ISO 3166 Territory Name and the encoding method may also be specified, following the Language Name.

    
.. _LMI-BIOSElement-Name:

``string`` **Name**

    The name used to identify this SoftwareElement.

    
.. _LMI-BIOSElement-LanguageEdition:

``string`` **LanguageEdition**

    The value of this property identifies the language edition of this SoftwareElement. The language codes defined in ISO 639 should be used. Where the element represents a multi-lingual or international version, the string "Multilingual" should be used.

    
.. _LMI-BIOSElement-LoadedStartingAddress:

``uint64`` **LoadedStartingAddress**

    The starting address of the memory which this BIOS occupies.

    
.. _LMI-BIOSElement-Caption:

``string`` **Caption**

    The Caption property is a short textual description (one- line string) of the object.

    
.. _LMI-BIOSElement-SystemBIOSMinorRelease:

``uint8`` **SystemBIOSMinorRelease**

    Indicates the minor release of the system BIOS, e.g. the value will be 16h for revision 10.22 and 01h for revision 2.1. The value 0xFF denotes the system does not support the use of this field.

    
.. _LMI-BIOSElement-SoftwareElementState:

``uint16`` **SoftwareElementState**

    The SoftwareElementState is defined in this model to identify various states of a SoftwareElement's life cycle. 

    - A SoftwareElement in the deployable state describes the details necessary to successfully distribute it and the details (Checks and Actions) required to move it to the installable state (i.e, the next state). 

    - A SoftwareElement in the installable state describes the details necessary to successfully install it and the details (Checks and Actions) required to create an element in the executable state (i.e., the next state). 

    - A SoftwareElement in the executable state describes the details necessary to successfully start it and the details (Checks and Actions) required to move it to the running state (i.e., the next state). 

    - A SoftwareElement in the running state describes the details necessary to manage the started element.

    
    ======== ===========
    ValueMap Values     
    ======== ===========
    0        Deployable 
    1        Installable
    2        Executable 
    3        Running    
    ======== ===========
    
.. _LMI-BIOSElement-EmbeddedControllerFirmwareMajorRelease:

``uint8`` **EmbeddedControllerFirmwareMajorRelease**

    Indicates the major release of the embedded controller firmware, e.g. the value will be 0Ah for revision 10.22 and 02h for revision 2.1. The value 0xFF denotes the embedded controller firmware is not field-upgradeable.

    
.. _LMI-BIOSElement-CurrentLanguage:

``string`` **CurrentLanguage**

    The currently selected language for the BIOS. This information can be obtained from SMBIOS, using the Current Language attribute of the Type 13 structure, to index into the string list following the structure. The property is formatted using the ISO 639 Language Name, and may be followed by the ISO 3166 Territory Name and the encoding method.

    
.. _LMI-BIOSElement-SystemBIOSMajorRelease:

``uint8`` **SystemBIOSMajorRelease**

    Indicates the major release of the system BIOS, e.g. the value will be 0Ah for revision 10.22 and 02h for revision 2.1. The value 0xFF denotes the system does not support the use of this field.

    
.. _LMI-BIOSElement-SoftwareElementID:

``string`` **SoftwareElementID**

    This is an identifier for the SoftwareElement and is designed to be used in conjunction with other keys to create a unique representation of the element.

    
.. _LMI-BIOSElement-PrimaryBIOS:

``boolean`` **PrimaryBIOS**

    If true, this is the primary BIOS of the ComputerSystem.

    
.. _LMI-BIOSElement-EmbeddedControllerFirmwareMinorRelease:

``uint8`` **EmbeddedControllerFirmwareMinorRelease**

    Indicates the minor release of the embedded controller firmware, e.g. the value will be 16h for revision 10.22 and 01h for revision 2.1. The value 0xFF denotes the embedded controller firmware is not field-upgradeable.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string`` :ref:`IdentificationCode <CIM-SoftwareElement-IdentificationCode>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`SerialNumber <CIM-SoftwareElement-SerialNumber>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`BuildNumber <CIM-SoftwareElement-BuildNumber>`
| ``string[]`` :ref:`RegistryURIs <CIM-BIOSElement-RegistryURIs>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string`` :ref:`OtherTargetOS <CIM-SoftwareElement-OtherTargetOS>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint64`` :ref:`LoadedEndingAddress <CIM-BIOSElement-LoadedEndingAddress>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`CodeSet <CIM-SoftwareElement-CodeSet>`
| ``string`` :ref:`LoadUtilityInformation <CIM-BIOSElement-LoadUtilityInformation>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

