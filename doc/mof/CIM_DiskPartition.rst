.. _CIM-DiskPartition:

CIM_DiskPartition
-----------------

Class reference
===============
Subclass of :ref:`CIM_GenericDiskPartition <CIM-GenericDiskPartition>`

A DiskPartition is a subclass of GenericDiskPartition for MBR (Master Boot Record) style partitions used in X86 platforms such as Windows and Linux.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-DiskPartition-PartitionSubtype:

``uint16`` **PartitionSubtype**

    The 'sub' type of a primary, extended, or logical Partition. The list of possible values corresponds to the decimal representation of the typical values in the Partition record.

    
    ======== ===========================================================
    ValueMap Values                                                     
    ======== ===========================================================
    0        Empty | Microsoft                                          
    1        DOS 12-bit FAT                                             
    2        XENIX root                                                 
    3        XENIX usr                                                  
    4        DOS 16-bit FAT                                             
    5        DOS Extended                                               
    6        DOS 16-bit FAT (> 32MB)                                    
    7        OS/2 HPFS | Win NTFS | QNX Ver 2 | Adv UNIX                
    8        AIX Boot | OS /2 | Dell (Array) | Commodore DOS            
    9        AIX Data, Coherent                                         
    10       OS/2 Boot Manager                                          
    11       32-bit FAT                                                 
    12       32-bit FAT                                                 
    14       Microsoft 16-bit FAT                                       
    15       Microsoft DOS Extended                                     
    16       OPUS | OS/2 2.0                                            
    17       OS/2 (MOSS) Inactive Type 1                                
    18       Compaq Diagnostics Partition | Microsoft                   
    20       OS/2 (MOSS) Inactive Type 4                                
    22       OS/2 (MOSS) Inactive Type 6                                
    23       OS/2 (MOSS) Inactive Type 7                                
    27       OS/2 (MOSS) Inactive Type B                                
    28       OS/2 (MOSS) Inactive Type C                                
    33       Microsoft                                                  
    35       Microsoft                                                  
    36       Microsoft                                                  
    38       Microsoft                                                  
    49       Microsoft                                                  
    51       Microsoft                                                  
    52       Microsoft                                                  
    53       OS/2 Logical Volume Manager                                
    54       Microsoft                                                  
    55       OS/2 JFS Log                                               
    60       PowerQuest                                                 
    64       VENIX 80286 | Series/1 Disk                                
    65       Personal RISC Boot                                         
    66       Veritas                                                    
    67       Veritas                                                    
    80       OnTrack Disk Manager Read Only DOS                         
    81       OnTrack Disk Manager Read/Write DOS                        
    82       CPM | Microport System V/386 | OnTrack Disk Mgr | Microsoft
    83       OnTrack Disk Manager                                       
    84       OnTrack Disk Manager Non-DOS                               
    85       Micro House EZ-Drive Non-DOS                               
    86       Golden Bow Vfeature | Microsoft                            
    97       Storage Dimensions SpeedStor | Microsoft                   
    99       UNIX - AT&T System V/386 | SCO UNIX                        
    100      Novell NetWare | Speedstore                                
    101      Novell NetWare                                             
    102      Novell NetWare                                             
    103      Novell                                                     
    104      Novell                                                     
    105      Novell                                                     
    113      Microsoft                                                  
    115      Microsoft                                                  
    116      Microsoft                                                  
    117      PC/IX IBM                                                  
    118      Microsoft                                                  
    119      QNX POSIX                                                  
    120      QNX POSIX (Secondary)                                      
    121      QNX POSIX (Secondary)                                      
    128      Minix (<=1.4a) | Linux | Microsoft                         
    129      Minix (>=1.4b) | Microsoft                                 
    130      Linux Swap | Prime                                         
    131      Linux Native | Apple                                       
    132      System Hibernation for APM                                 
    134      Microsoft                                                  
    135      HPFS FT mirror                                             
    147      Amoeba | Microsoft                                         
    148      Amoeba BBT | Microsoft                                     
    161      Microsoft                                                  
    163      Microsoft                                                  
    164      Microsoft                                                  
    165      BSD/386                                                    
    166      Microsoft                                                  
    177      Microsoft                                                  
    179      Microsoft                                                  
    180      Microsoft                                                  
    182      Microsoft                                                  
    183      BSDI fs | Microsoft                                        
    184      BSDI Swap | Microsoft                                      
    193      Microsoft                                                  
    196      Microsoft                                                  
    198      Microsoft                                                  
    199      Syrinx | HPFS FT Disabled Mirror                           
    216      CP/M 86                                                    
    219      Digital Research CPM-86 | Concurrent DOS | OUTRIGGER       
    225      SpeedStor 12-bit FAT Extended                              
    227      DOS Read-Only | Storage Dimensions                         
    228      SpeedStor 16-bit FAT Extended                              
    229      Microsoft                                                  
    230      Microsoft                                                  
    239      Intel                                                      
    240      OS/2 Raw Data                                              
    241      Storage Dimensions                                         
    242      DOS (Secondary)                                            
    243      Microsoft                                                  
    244      SpeedStor Large | Storage Dimensions                       
    246      Microsoft                                                  
    254      Lan Step | SpeedStor | IBM PS/2 IML                        
    255      Bad Block Tables                                           
    65535    Unknown                                                    
    ======== ===========================================================
    
.. _CIM-DiskPartition-NameFormat:

``uint16`` **NameFormat**

    DiskPartition names MUST use OS Device Name format. In cases where the partition names can not be used by applications programmatically (for example, open()) the NameFormat SHOULD be 'Other'.

    
    ======== ==============
    ValueMap Values        
    ======== ==============
    1        Other         
    12       OS Device Name
    ======== ==============
    
.. _CIM-DiskPartition-PrimaryPartition:

``boolean`` **PrimaryPartition**

    Boolean indicating that the DiskPartition is labelled as the primary partition for a ComputerSystem.

    
.. _CIM-DiskPartition-PartitionType:

``uint16`` **PartitionType**

    The type of Partition.

    
    ======== ========
    ValueMap Values  
    ======== ========
    0        Unknown 
    1        Primary 
    2        Extended
    3        Logical 
    ======== ========
    
.. _CIM-DiskPartition-NameNamespace:

``uint16`` **NameNamespace**

    DiskPartition names MUST use OS Device Namespace.

    
    ======== ===================
    ValueMap Values             
    ======== ===================
    1        Other              
    8        OS Device Namespace
    ======== ===================
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint8`` :ref:`DeltaReservation <CIM-StorageExtent-DeltaReservation>`
| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint64`` :ref:`BlockSize <CIM-StorageExtent-BlockSize>`
| ``boolean`` :ref:`Allocatable <CIM-MediaPartition-Allocatable>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``uint16[]`` :ref:`ClientSettableUsage <CIM-StorageExtent-ClientSettableUsage>`
| ``string[]`` :ref:`ExtentDiscriminator <CIM-StorageExtent-ExtentDiscriminator>`
| ``string[]`` :ref:`OtherIdentifyingInfo <CIM-LogicalDevice-OtherIdentifyingInfo>`
| ``uint16`` :ref:`DataOrganization <CIM-StorageExtent-DataOrganization>`
| ``uint16`` :ref:`Access <CIM-StorageExtent-Access>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``boolean`` :ref:`Primordial <CIM-StorageExtent-Primordial>`
| ``string`` :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| ``uint16`` :ref:`CompressionRate <CIM-StorageExtent-CompressionRate>`
| ``boolean`` :ref:`NoSinglePointOfFailure <CIM-StorageExtent-NoSinglePointOfFailure>`
| ``uint16`` :ref:`Usage <CIM-StorageExtent-Usage>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``string`` :ref:`SignatureAlgorithm <CIM-MediaPartition-SignatureAlgorithm>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string`` :ref:`OtherNameNamespace <CIM-StorageExtent-OtherNameNamespace>`
| ``uint64`` :ref:`ExtentInterleaveDepth <CIM-StorageExtent-ExtentInterleaveDepth>`
| ``string[]`` :ref:`IdentifyingDescriptions <CIM-LogicalDevice-IdentifyingDescriptions>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``string`` :ref:`OtherNameFormat <CIM-StorageExtent-OtherNameFormat>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``boolean`` :ref:`ErrorCleared <CIM-LogicalDevice-ErrorCleared>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``string`` :ref:`Purpose <CIM-StorageExtent-Purpose>`
| ``uint64`` :ref:`ExtentStripeLength <CIM-StorageExtent-ExtentStripeLength>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``boolean`` :ref:`IsBasedOnUnderlyingRedundancy <CIM-StorageExtent-IsBasedOnUnderlyingRedundancy>`
| ``uint16`` :ref:`LocationIndicator <CIM-LogicalDevice-LocationIndicator>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``boolean`` :ref:`Extendable <CIM-MediaPartition-Extendable>`
| ``boolean`` :ref:`IsCompressed <CIM-StorageExtent-IsCompressed>`
| ``string`` :ref:`Name <CIM-StorageExtent-Name>`
| ``uint16[]`` :ref:`PowerManagementCapabilities <CIM-LogicalDevice-PowerManagementCapabilities>`
| ``boolean`` :ref:`Bootable <CIM-MediaPartition-Bootable>`
| ``uint16`` :ref:`CompressionState <CIM-StorageExtent-CompressionState>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``boolean`` :ref:`SequentialAccess <CIM-StorageExtent-SequentialAccess>`
| ``uint16[]`` :ref:`AdditionalAvailability <CIM-LogicalDevice-AdditionalAvailability>`
| ``string`` :ref:`OtherUsageDescription <CIM-StorageExtent-OtherUsageDescription>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``boolean`` :ref:`IsComposite <CIM-StorageExtent-IsComposite>`
| ``uint16`` :ref:`StatusInfo <CIM-LogicalDevice-StatusInfo>`
| ``string`` :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| ``string`` :ref:`Signature <CIM-MediaPartition-Signature>`
| ``uint16`` :ref:`PackageRedundancy <CIM-StorageExtent-PackageRedundancy>`
| ``uint64`` :ref:`PowerOnHours <CIM-LogicalDevice-PowerOnHours>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint16`` :ref:`DataRedundancy <CIM-StorageExtent-DataRedundancy>`
| ``uint64`` :ref:`NumberOfBlocks <CIM-StorageExtent-NumberOfBlocks>`
| ``uint64`` :ref:`MaxQuiesceTime <CIM-LogicalDevice-MaxQuiesceTime>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint64`` :ref:`TotalPowerOnHours <CIM-LogicalDevice-TotalPowerOnHours>`
| ``string`` :ref:`ErrorDescription <CIM-LogicalDevice-ErrorDescription>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``boolean`` :ref:`IsConcatenated <CIM-StorageExtent-IsConcatenated>`
| ``uint32`` :ref:`LastErrorCode <CIM-LogicalDevice-LastErrorCode>`
| ``string`` :ref:`ErrorMethodology <CIM-StorageExtent-ErrorMethodology>`
| ``string`` :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| ``uint16[]`` :ref:`ExtentStatus <CIM-StorageExtent-ExtentStatus>`
| ``string`` :ref:`SignatureState <CIM-MediaPartition-SignatureState>`
| ``uint16`` :ref:`Availability <CIM-LogicalDevice-Availability>`
| ``string`` :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`
| ``uint64`` :ref:`ConsumableBlocks <CIM-StorageExtent-ConsumableBlocks>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`Reset <CIM-LogicalDevice-Reset>`
| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`
| :ref:`SetPowerState <CIM-LogicalDevice-SetPowerState>`
| :ref:`QuiesceDevice <CIM-LogicalDevice-QuiesceDevice>`
| :ref:`EnableDevice <CIM-LogicalDevice-EnableDevice>`
| :ref:`OnlineDevice <CIM-LogicalDevice-OnlineDevice>`
| :ref:`SaveProperties <CIM-LogicalDevice-SaveProperties>`
| :ref:`RestoreProperties <CIM-LogicalDevice-RestoreProperties>`

