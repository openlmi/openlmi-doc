.. _CIM-SoftwareIdentity:

CIM_SoftwareIdentity
--------------------

Class reference
===============
Subclass of :ref:`CIM_LogicalElement <CIM-LogicalElement>`

SoftwareIdentity provides descriptive information about a software component for asset tracking and/or installation dependency management. When the IsEntity property has the value TRUE, the instance of SoftwareIdentity represents an individually identifiable entity similar to Physical Element. SoftwareIdentity does NOT indicate whether the software is installed, executing, etc. This extra information may be provided through specialized associations to Software Identity. For instance, both InstalledSoftwareIdentity and ElementSoftwareIdentity may be used to indicate that the software identified by this class is installed. SoftwareIdentity is used when managing the software components of a ManagedElement that is the management focus. Since software may be acquired, SoftwareIdentity can be associated with a Product using the ProductSoftwareComponent relationship. The Application Model manages the deployment and installation of software via the classes, SoftwareFeatures and SoftwareElements. SoftwareFeature and SoftwareElement are used when the software component is the management focus. The deployment/installation concepts are related to the asset/identity one. In fact, a SoftwareIdentity may correspond to a Product, or to one or more SoftwareFeatures or SoftwareElements - depending on the granularity of these classes and the deployment model. The correspondence of Software Identity to Product, SoftwareFeature or SoftwareElement is indicated using the ConcreteIdentity association. Note that there may not be sufficient detail or instrumentation to instantiate ConcreteIdentity. And, if the association is instantiated, some duplication of information may result. For example, the Vendor described in the instances of Product and SoftwareIdentity MAY be the same. However, this is not necessarily true, and it is why vendor and similar information are duplicated in this class. 

Note that ConcreteIdentity can also be used to describe the relationship of the software to any LogicalFiles that result from installing it. As above, there may not be sufficient detail or instrumentation to instantiate this association.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-SoftwareIdentity-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-SoftwareIdentity-TargetOSTypes:

``uint16[]`` **TargetOSTypes**

    The TargetOSTypes property specifies the target operating systems supported by the software. When the target operating system of the software is not listed in the enumeration values, TargetOperatingSystems[] property should be used to specify the target operating system.

    
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
    
.. _CIM-SoftwareIdentity-ExtendedResourceType:

``uint16`` **ExtendedResourceType**

    The binary format type of the installation package of the software. This property can be used to locate a SoftwareInstallationService capable of installing this software.

    
    ======== ==================================
    ValueMap Values                            
    ======== ==================================
    0        Unknown                           
    1        Other                             
    2        Not Applicable                    
    3        Linux RPM                         
    4        HP-UX Depot                       
    5        Windows MSI                       
    6        Solaris Package                   
    7        Macintosh Disk Image              
    8        Debian linux Package              
    9        VMware vSphere Installation Bundle
    10       VMware Software Bulletin          
    11       HP Smart Component                
    ..       DMTF Reserved                     
    0x8000.. Vendor Reserved                   
    ======== ==================================
    
.. _CIM-SoftwareIdentity-InstanceID:

``string`` **InstanceID**

    Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. In order to ensure uniqueness within the NameSpace, the value of InstanceID SHOULD be constructed using the following 'preferred' algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon ':', and where <OrgID> MUST include a copyrighted, trademarked or otherwise unique name that is owned by the business entity creating/defining the InstanceID, or is a registered ID that is assigned to the business entity by a recognized global authority (This is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness <OrgID> MUST NOT contain a colon (':'). When using this algorithm, the first colon to appear in InstanceID MUST appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and SHOULD not be re-used to identify different underlying (real-world) elements. If the above 'preferred' algorithm is not used, the defining entity MUST assure that the resultant InstanceID is not re-used across any InstanceIDs produced by this or other providers for this instance's NameSpace. 

    For DMTF defined instances, the 'preferred' algorithm MUST be used with the <OrgID> set to 'CIM'.

    
.. _CIM-SoftwareIdentity-SerialNumber:

``string`` **SerialNumber**

    A manufacturer-allocated number used to identify the software.

    
.. _CIM-SoftwareIdentity-Languages:

``string[]`` **Languages**

    The language editions supported by the software. The language codes defined in ISO 639 should be used.

    
.. _CIM-SoftwareIdentity-MinExtendedResourceTypeMajorVersion:

``uint16`` **MinExtendedResourceTypeMajorVersion**

    This property represents the major number component of the minimum version of the installer, represented by the ExtendedResourceType property, that is required to install this software.

    
.. _CIM-SoftwareIdentity-TargetTypes:

``string[]`` **TargetTypes**

    An array of strings that describes the compatible installer(s). The purpose of the array elements is to establish compatibility between a SoftwareIdentity and a SoftwareInstallationService that can install the SoftwareIdentity by comparing the values of the array elements of this property to the values of SoftwareInstallationServiceCapabilities.SupportedTargetTypes[] property's array elements.

    
.. _CIM-SoftwareIdentity-TargetOperatingSystems:

``string[]`` **TargetOperatingSystems**

    Specifies the target operating systems of the software. This property should be used when a target operating system is not listed in the TargetOSTypes array values.

    
.. _CIM-SoftwareIdentity-LargeBuildNumber:

``uint64`` **LargeBuildNumber**

    The build number of the software if IsLargeBuildNumber is TRUE. TheLargeBuildNumber property should be used for all future implementations.

    
.. _CIM-SoftwareIdentity-MinorVersion:

``uint16`` **MinorVersion**

    The minor number component of the software's version information - for example, '1' from version 12.1(3)T. This property is defined as a numeric value to allow the determination of 'newer' vs. 'older' releases. A 'newer' minor release is indicated by a larger numeric value.

    
.. _CIM-SoftwareIdentity-IsEntity:

``boolean`` **IsEntity**

    The IsEntity property is used to indicate whether the SoftwareIdentity corresponds to a discrete copy of the software component or is being used to convey descriptive and identifying information about software that is not present in the management domain.A value of TRUE shall indicate that the SoftwareIdentity instance corresponds to a discrete copy of the software component. A value of FALSE shall indicate that the SoftwareIdentity instance does not correspond to a discrete copy of the Software.

    
.. _CIM-SoftwareIdentity-IsLargeBuildNumber:

``boolean`` **IsLargeBuildNumber**

    The IsLargeBuildNumber property is used to indicate if the BuildNumber of LargeBuildNumber property contains the value of the software build. A value of TRUE shall indicate that the build number is represented by the LargeBuildNumber property. A value of FALSE shall indicate that the build number is represented by the BuildNumber property.

    
.. _CIM-SoftwareIdentity-MinExtendedResourceTypeMinorVersion:

``uint16`` **MinExtendedResourceTypeMinorVersion**

    This property represents the minor number component of the minimum version of the installer, represented by theExtendedResourceType property, that is required to install this software.

    
.. _CIM-SoftwareIdentity-ReleaseDate:

``datetime`` **ReleaseDate**

    The date the software was released.

    
.. _CIM-SoftwareIdentity-ClassificationDescriptions:

``string[]`` **ClassificationDescriptions**

    An array of free-form strings providing more detailed explanations for any of the entries in the Classifications array. Note that each entry is related to one in the Classifications array located at the same index.

    
.. _CIM-SoftwareIdentity-IdentityInfoType:

``string[]`` **IdentityInfoType**

    An indexed array of fixed-form strings that provide the description of the type of information that is stored in the corresponding component of the IdentityInfoValue array. The elements of this property array describe the type of the value in the corresponding elements of the IndetityInfoValue array. When the IdentityInfoValue property is implemented, the IdentityInfoType property MUST be implemented. To insure uniqueness the IdentityInfoType property SHOULD be formatted using the following algorithm: < OrgID > : < LocalID > Where < OrgID > and < LocalID > are separated by a colon (:), and where < OrgID > MUST include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the IdentityInfoType or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the < Schema Name > _ < Class Name > structure of Schema class names.) In addition, to ensure uniqueness, < OrgID > MUST NOT contain a colon (:). When using this algorithm, the first colon to appear in IdentityInfoType MUST appear between < OrgID > and < LocalID > . < LocalID > is chosen by the business entity and SHOULD NOT be reused to identify different underlying software elements.

    
.. _CIM-SoftwareIdentity-Manufacturer:

``string`` **Manufacturer**

    Manufacturer of this software.

    
.. _CIM-SoftwareIdentity-Classifications:

``uint16[]`` **Classifications**

    An array of enumerated integers that classify this software. For example, the software MAY be instrumentation (value=5) or firmware and diagnostic software (10 and 7). The use of value 6, Firmware/BIOS, is being deprecated. Instead, either the value 10 (Firmware) and/or 11 (BIOS/FCode) SHOULD be used. The value 13, Software Bundle, identifies a software package consisting of multiple discrete software instances that can be installed individually or together.

    Each contained software instance is represented by an instance of SoftwareIdentity that is associated to this instance of SoftwareIdentityinstance via a Component association.

    
    ============== ======================
    ValueMap       Values                
    ============== ======================
    0              Unknown               
    1              Other                 
    2              Driver                
    3              Configuration Software
    4              Application Software  
    5              Instrumentation       
    6              Firmware/BIOS         
    7              Diagnostic Software   
    8              Operating System      
    9              Middleware            
    10             Firmware              
    11             BIOS/FCode            
    12             Support/Service Pack  
    13             Software Bundle       
    ..             DMTF Reserved         
    0x8000..0xFFFF Vendor Reserved       
    ============== ======================
    
.. _CIM-SoftwareIdentity-IdentityInfoValue:

``string[]`` **IdentityInfoValue**

    IdentityInfoValue captures additional information that MAY be used by an organization to describe or identify a software instance within the context of the organization. For example, large organizations may have several ways to address or identify a particular instance of software depending on where it is stored; a catalog, a web site, or for whom it is intended; development, customer service, etc. The indexed array property IdentityInfoValue contains 0 or more strings that contain a specific identity info string value. IdentityInfoValue is mapped and indexed to IdentityInfoType. When the IdentityInfoValue property is implemented, the IdentityInfoType property MUST be implemented and shall be formatted using the algorithm provided in the IdentityInfoType property Description.

    
.. _CIM-SoftwareIdentity-OtherExtendedResourceTypeDescription:

``string`` **OtherExtendedResourceTypeDescription**

    A string describing the binary format type of the installation package of the software when the ExtendedResourceType property has a value of 1 (Other).

    
.. _CIM-SoftwareIdentity-MinExtendedResourceTypeBuildNumber:

``uint16`` **MinExtendedResourceTypeBuildNumber**

    This property represents the Build number component of the minimum version of the installer, represented by theExtendedResourceType property, that is required to install this software.

    
.. _CIM-SoftwareIdentity-MajorVersion:

``uint16`` **MajorVersion**

    The major number component of the software's version information - for example, '12' from version 12.1(3)T. This property is defined as a numeric value to allow the determination of 'newer' vs. 'older' releases. A 'newer' major release is indicated by a larger numeric value.

    
.. _CIM-SoftwareIdentity-MinExtendedResourceTypeRevisionNumber:

``uint16`` **MinExtendedResourceTypeRevisionNumber**

    This property represents the Revision number component of the minimum version of the installer, represented by theExtendedResourceType property, that is required to install this software.

    
.. _CIM-SoftwareIdentity-BuildNumber:

``uint16`` **BuildNumber**

    The build number of the software.

    
.. _CIM-SoftwareIdentity-VersionString:

``string`` **VersionString**

    A string representing the complete software version information - for example, '12.1(3)T'. This string and the numeric major/minor/revision/build properties are complementary. Since vastly different representations and semantics exist for versions, it is not assumed that one representation is sufficient to permit a client to perform computations (i.e., the values are numeric) and a user to recognize the software's version (i.e., the values are understandable and readable). Hence, both numeric and string representations of version are provided.

    
.. _CIM-SoftwareIdentity-RevisionNumber:

``uint16`` **RevisionNumber**

    The revision or maintenance release component of the software's version information - for example, '3' from version 12.1(3)T. This property is defined as a numeric value to allow the determination of 'newer' vs. 'older' releases. A 'newer' revision is indicated by a larger numeric value.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

