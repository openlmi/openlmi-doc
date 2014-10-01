.. _CIM-Check:

CIM_Check
---------

Class reference
===============
Subclass of :ref:`CIM_ManagedElement <CIM-ManagedElement>`

A CIM_Check is a condition or characteristic that is expected to be true in an environment defined or scoped by an instance of a CIM_ComputerSystem. The Checks associated with a particular SoftwareElement are organized into one of two groups using the Phase property of the CIM_SoftwareElementChecks association. Conditions that are expected to be true when a SoftwareElement is in a particular state and environment are known as 'in-state' conditions. Conditions that need to be satisfied in order to transition the SoftwareElement to its next state are known as 'next-state' conditions. 

A CIM_ComputerSystem object represents the environment in which CIM_SoftwareElements are already deployed/installed or into which the elements will be deployed/installed. For the case in which an element is already installed, the CIM_InstalledSoftwareElement association identifies the CIM_ComputerSystem object that represents the "environment". When a SoftwareElement is being deployed for installation on a ComputerSystem, that system is the target of the Check and is identified using the TargetSystem reference of the InvokeOnSystem method.


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

.. _CIM-Check-CheckID:

``string`` **CheckID**

    An identifier used in conjunction with other keys to uniquely identify the Check.

    
.. _CIM-Check-CheckMode:

``boolean`` **CheckMode**

    The CheckMode property is used to indicate whether the condition is expected to exist or not exist in the environment. When the value is True, the condition is expected to exist (e.g., a file is expected to be on a system), so the Invoke methods are expected to return True. When the value is False, the condition is not expected to exist (e.g., a file is not to be on a system), so the Invoke methods are expected to return False.

    
.. _CIM-Check-TargetOperatingSystem:

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
    
.. _CIM-Check-Name:

``string`` **Name**

    The name used to identify the SoftwareElement that is being checked.

    
.. _CIM-Check-SoftwareElementID:

``string`` **SoftwareElementID**

    This is an identifier for the SoftwareElement being checked.

    
.. _CIM-Check-Version:

``string`` **Version**

    The version of the SoftwareElement being checked.

    
.. _CIM-Check-SoftwareElementState:

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
    

Local methods
^^^^^^^^^^^^^

    .. _CIM-Check-Invoke:

``uint32`` **Invoke** ()

    The Invoke method evaluates this Check. The details of the evaluation are described by the specific subclasses of CIM_Check. When the SoftwareElement being checked is already installed, the CIM_InstalledSoftwareElement association identifies the CIM_ComputerSystem in whose context the Invoke is executed. If this association is not in place, then the InvokeOnSystem method should be used - since it identifies the TargetSystem as an input parameter of the method. 

    The results of the Invoke method are based on the return value. A zero is returned if the condition is satisfied. A one is returned if the method is not supported. Any other value indicates the condition is not satisfied.

    
    **Parameters**
    
*None*
    .. _CIM-Check-InvokeOnSystem:

``uint32`` **InvokeOnSystem** (:ref:`CIM_ComputerSystem <CIM-ComputerSystem>` TargetSystem)

    The InvokeOnSystem method evaluates this Check. The details of the evaluation are described by the specific subclasses of CIM_Check. The method's TargetSystem input parameter specifies the ComputerSystem in whose context the method is invoked. 

    The results of the InvokeOnSystem method are based on the return value. A zero is returned if the condition is satisfied. A one is returned if the method is not supported. Any other value indicates the condition is not satisfied.

    
    **Parameters**
    
        *IN* :ref:`CIM_ComputerSystem <CIM-ComputerSystem>` **TargetSystem**
            Reference to ComputerSystem in whose context the method is to be invoked.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

