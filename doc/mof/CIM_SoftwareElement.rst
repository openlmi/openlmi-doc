.. _CIM-SoftwareElement:

CIM_SoftwareElement
-------------------

Class reference
===============
Subclass of :ref:`CIM_LogicalElement <CIM-LogicalElement>`

The CIM_SoftwareElement class is used to decompose a CIM_SoftwareFeature object into a set of individually manageable or deployable parts, for a particular platform. A SoftwareElement's platform is uniquely identified by its underlying hardware architecture and operating system (for example Sun Solaris on Sun Sparc or Windows NT on Intel platforms). As such, to understand the details of how the functionality of a particular SoftwareFeature is provided on a particular platform, the CIM_SoftwareElement objects referenced by CIM_SoftwareFeatureSoftwareElements associations are organized in disjoint sets based on the TargetOperatingSystem property. A CIM_SoftwareElement object captures the management details of a part or component in one of four states characterized by the SoftwareElementState property.


Key properties
^^^^^^^^^^^^^^

| :ref:`TargetOperatingSystem <CIM-SoftwareElement-TargetOperatingSystem>`
| :ref:`Name <CIM-SoftwareElement-Name>`
| :ref:`SoftwareElementID <CIM-SoftwareElement-SoftwareElementID>`
| :ref:`Version <CIM-SoftwareElement-Version>`
| :ref:`SoftwareElementState <CIM-SoftwareElement-SoftwareElementState>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-SoftwareElement-IdentificationCode:

``string`` **IdentificationCode**

    The manufacturer's identifier for this SoftwareElement. Often this will be a stock keeping unit (SKU) or a part number.

    
.. _CIM-SoftwareElement-SerialNumber:

``string`` **SerialNumber**

    The assigned serial number of this SoftwareElement.

    
.. _CIM-SoftwareElement-Version:

``string`` **Version**

    Software Version should be in the form <Major>.<Minor>.<Revision> or <Major>.<Minor><letter><revision>.

    
.. _CIM-SoftwareElement-Manufacturer:

``string`` **Manufacturer**

    Manufacturer of this SoftwareElement.

    
.. _CIM-SoftwareElement-TargetOperatingSystem:

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
    
.. _CIM-SoftwareElement-Name:

``string`` **Name**

    The name used to identify this SoftwareElement.

    
.. _CIM-SoftwareElement-LanguageEdition:

``string`` **LanguageEdition**

    The value of this property identifies the language edition of this SoftwareElement. The language codes defined in ISO 639 should be used. Where the element represents a multi-lingual or international version, the string "Multilingual" should be used.

    
.. _CIM-SoftwareElement-OtherTargetOS:

``string`` **OtherTargetOS**

    The OtherTargetOS property records the manufacturer and operating system type for a SoftwareElement when the TargetOperatingSystem property has a value of 1 ("Other"). For all other values of TargetOperatingSystem, the OtherTargetOS property is NULL.

    
.. _CIM-SoftwareElement-SoftwareElementState:

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
    
.. _CIM-SoftwareElement-SoftwareElementID:

``string`` **SoftwareElementID**

    This is an identifier for the SoftwareElement and is designed to be used in conjunction with other keys to create a unique representation of the element.

    
.. _CIM-SoftwareElement-BuildNumber:

``string`` **BuildNumber**

    The internal identifier for this compilation of SoftwareElement.

    
.. _CIM-SoftwareElement-CodeSet:

``string`` **CodeSet**

    The code set used by this SoftwareElement. It defines the bit patterns that a system uses to identify characters. ISO defines various code sets such as UTF-8 and ISO8859-1.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

