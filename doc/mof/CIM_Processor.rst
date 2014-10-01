.. _CIM-Processor:

CIM_Processor
-------------

Class reference
===============
Subclass of :ref:`CIM_LogicalDevice <CIM-LogicalDevice>`

Capabilities and management of the Processor LogicalDevice.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-Processor-LoadPercentage:

``uint16`` **LoadPercentage**

    Loading of this Processor, averaged over the last minute, in Percent.

    
.. _CIM-Processor-ExternalBusClockSpeed:

``uint32`` **ExternalBusClockSpeed**

    The speed (in MHz) of the external bus interface (also known as the front side bus).

    
.. _CIM-Processor-MaxClockSpeed:

``uint32`` **MaxClockSpeed**

    The maximum speed (in MHz) of this Processor.

    
.. _CIM-Processor-UniqueID:

``string`` **UniqueID**

    A globally unique identifier for the Processor. This identifier can be unique only within a Processor Family.

    
.. _CIM-Processor-AddressWidth:

``uint16`` **AddressWidth**

    Processor address width in bits.

    
.. _CIM-Processor-CurrentClockSpeed:

``uint32`` **CurrentClockSpeed**

    The current speed (in MHz) of this Processor.

    
.. _CIM-Processor-Stepping:

``string`` **Stepping**

    Stepping is a free-form string that indicates the revision level of the Processor within the Processor.Family.

    
.. _CIM-Processor-DataWidth:

``uint16`` **DataWidth**

    Processor data width in bits.

    
.. _CIM-Processor-NumberOfEnabledCores:

``uint16`` **NumberOfEnabledCores**

    Number of processor cores enabled for processor.

    
.. _CIM-Processor-OtherFamilyDescription:

``string`` **OtherFamilyDescription**

    A string that describes the Processor Family type. It is used when the Family property is set to 1 ("Other"). This string should be set to NULL when the Family property is any value other than 1.

    
.. _CIM-Processor-Family:

``uint16`` **Family**

    The Processor family type. For example, values include "Pentium(R) processor with MMX(TM) technology" (value=14) and "68040" (value=96).

    
    ======== ===============================================================
    ValueMap Values                                                         
    ======== ===============================================================
    1        Other                                                          
    2        Unknown                                                        
    3        8086                                                           
    4        80286                                                          
    5        80386                                                          
    6        80486                                                          
    7        8087                                                           
    8        80287                                                          
    9        80387                                                          
    10       80487                                                          
    11       Pentium(R) brand                                               
    12       Pentium(R) Pro                                                 
    13       Pentium(R) II                                                  
    14       Pentium(R) processor with MMX(TM) technology                   
    15       Celeron(TM)                                                    
    16       Pentium(R) II Xeon(TM)                                         
    17       Pentium(R) III                                                 
    18       M1 Family                                                      
    19       M2 Family                                                      
    20       Intel(R) Celeron(R) M processor                                
    21       Intel(R) Pentium(R) 4 HT processor                             
    24       K5 Family                                                      
    25       K6 Family                                                      
    26       K6-2                                                           
    27       K6-3                                                           
    28       AMD Athlon(TM) Processor Family                                
    29       AMD(R) Duron(TM) Processor                                     
    30       AMD29000 Family                                                
    31       K6-2+                                                          
    32       Power PC Family                                                
    33       Power PC 601                                                   
    34       Power PC 603                                                   
    35       Power PC 603+                                                  
    36       Power PC 604                                                   
    37       Power PC 620                                                   
    38       Power PC X704                                                  
    39       Power PC 750                                                   
    40       Intel(R) Core(TM) Duo processor                                
    41       Intel(R) Core(TM) Duo mobile processor                         
    42       Intel(R) Core(TM) Solo mobile processor                        
    43       Intel(R) Atom(TM) processor                                    
    48       Alpha Family                                                   
    49       Alpha 21064                                                    
    50       Alpha 21066                                                    
    51       Alpha 21164                                                    
    52       Alpha 21164PC                                                  
    53       Alpha 21164a                                                   
    54       Alpha 21264                                                    
    55       Alpha 21364                                                    
    56       AMD Turion(TM) II Ultra Dual-Core Mobile M Processor Family    
    57       AMD Turion(TM) II Dual-Core Mobile M Processor Family          
    58       AMD Athlon(TM) II Dual-Core Mobile M Processor Family          
    59       AMD Opteron(TM) 6100 Series Processor                          
    60       AMD Opteron(TM) 4100 Series Processor                          
    61       AMD Opteron(TM) 6200 Series Processor                          
    62       AMD Opteron(TM) 4200 Series Processor                          
    63       AMD FX(TM) Series Processor                                    
    64       MIPS Family                                                    
    65       MIPS R4000                                                     
    66       MIPS R4200                                                     
    67       MIPS R4400                                                     
    68       MIPS R4600                                                     
    69       MIPS R10000                                                    
    70       AMD C-Series Processor                                         
    71       AMD E-Series Processor                                         
    72       AMD A-Series Processor                                         
    73       AMD G-Series Processor                                         
    74       AMD Z-Series Processor                                         
    75       AMD R-Series Processor                                         
    76       AMD Opteron(TM) 4300 Series Processor                          
    77       AMD Opteron(TM) 6300 Series Processor                          
    78       AMD Opteron(TM) 3300 Series Processor                          
    79       AMD FirePro(TM) Series Processor                               
    80       SPARC Family                                                   
    81       SuperSPARC                                                     
    82       microSPARC II                                                  
    83       microSPARC IIep                                                
    84       UltraSPARC                                                     
    85       UltraSPARC II                                                  
    86       UltraSPARC IIi                                                 
    87       UltraSPARC III                                                 
    88       UltraSPARC IIIi                                                
    96       68040                                                          
    97       68xxx Family                                                   
    98       68000                                                          
    99       68010                                                          
    100      68020                                                          
    101      68030                                                          
    102      AMD Athlon(TM) X4 Quad-Core Processor Family                   
    103      AMD Opteron(TM) X1000 Series Processor                         
    104      AMD Opteron(TM) X2000 Series APU                               
    112      Hobbit Family                                                  
    120      Crusoe(TM) TM5000 Family                                       
    121      Crusoe(TM) TM3000 Family                                       
    122      Efficeon(TM) TM8000 Family                                     
    128      Weitek                                                         
    130      Itanium(TM) Processor                                          
    131      AMD Athlon(TM) 64 Processor Family                             
    132      AMD Opteron(TM) Processor Family                               
    133      AMD Sempron(TM) Processor Family                               
    134      AMD Turion(TM) 64 Mobile Technology                            
    135      Dual-Core AMD Opteron(TM) Processor Family                     
    136      AMD Athlon(TM) 64 X2 Dual-Core Processor Family                
    137      AMD Turion(TM) 64 X2 Mobile Technology                         
    138      Quad-Core AMD Opteron(TM) Processor Family                     
    139      Third-Generation AMD Opteron(TM) Processor Family              
    140      AMD Phenom(TM) FX Quad-Core Processor Family                   
    141      AMD Phenom(TM) X4 Quad-Core Processor Family                   
    142      AMD Phenom(TM) X2 Dual-Core Processor Family                   
    143      AMD Athlon(TM) X2 Dual-Core Processor Family                   
    144      PA-RISC Family                                                 
    145      PA-RISC 8500                                                   
    146      PA-RISC 8000                                                   
    147      PA-RISC 7300LC                                                 
    148      PA-RISC 7200                                                   
    149      PA-RISC 7100LC                                                 
    150      PA-RISC 7100                                                   
    160      V30 Family                                                     
    161      Quad-Core Intel(R) Xeon(R) processor 3200 Series               
    162      Dual-Core Intel(R) Xeon(R) processor 3000 Series               
    163      Quad-Core Intel(R) Xeon(R) processor 5300 Series               
    164      Dual-Core Intel(R) Xeon(R) processor 5100 Series               
    165      Dual-Core Intel(R) Xeon(R) processor 5000 Series               
    166      Dual-Core Intel(R) Xeon(R) processor LV                        
    167      Dual-Core Intel(R) Xeon(R) processor ULV                       
    168      Dual-Core Intel(R) Xeon(R) processor 7100 Series               
    169      Quad-Core Intel(R) Xeon(R) processor 5400 Series               
    170      Quad-Core Intel(R) Xeon(R) processor                           
    171      Dual-Core Intel(R) Xeon(R) processor 5200 Series               
    172      Dual-Core Intel(R) Xeon(R) processor 7200 Series               
    173      Quad-Core Intel(R) Xeon(R) processor 7300 Series               
    174      Quad-Core Intel(R) Xeon(R) processor 7400 Series               
    175      Multi-Core Intel(R) Xeon(R) processor 7400 Series              
    176      Pentium(R) III Xeon(TM)                                        
    177      Pentium(R) III Processor with Intel(R) SpeedStep(TM) Technology
    178      Pentium(R) 4                                                   
    179      Intel(R) Xeon(TM)                                              
    180      AS400 Family                                                   
    181      Intel(R) Xeon(TM) processor MP                                 
    182      AMD Athlon(TM) XP Family                                       
    183      AMD Athlon(TM) MP Family                                       
    184      Intel(R) Itanium(R) 2                                          
    185      Intel(R) Pentium(R) M processor                                
    186      Intel(R) Celeron(R) D processor                                
    187      Intel(R) Pentium(R) D processor                                
    188      Intel(R) Pentium(R) Processor Extreme Edition                  
    189      Intel(R) Core(TM) Solo Processor                               
    190      K7                                                             
    191      Intel(R) Core(TM)2 Duo Processor                               
    192      Intel(R) Core(TM)2 Solo processor                              
    193      Intel(R) Core(TM)2 Extreme processor                           
    194      Intel(R) Core(TM)2 Quad processor                              
    195      Intel(R) Core(TM)2 Extreme mobile processor                    
    196      Intel(R) Core(TM)2 Duo mobile processor                        
    197      Intel(R) Core(TM)2 Solo mobile processor                       
    198      Intel(R) Core(TM) i7 processor                                 
    199      Dual-Core Intel(R) Celeron(R) Processor                        
    200      S/390 and zSeries Family                                       
    201      ESA/390 G4                                                     
    202      ESA/390 G5                                                     
    203      ESA/390 G6                                                     
    204      z/Architectur base                                             
    205      Intel(R) Core(TM) i5 processor                                 
    206      Intel(R) Core(TM) i3 processor                                 
    210      VIA C7(TM)-M Processor Family                                  
    211      VIA C7(TM)-D Processor Family                                  
    212      VIA C7(TM) Processor Family                                    
    213      VIA Eden(TM) Processor Family                                  
    214      Multi-Core Intel(R) Xeon(R) processor                          
    215      Dual-Core Intel(R) Xeon(R) processor 3xxx Series               
    216      Quad-Core Intel(R) Xeon(R) processor 3xxx Series               
    217      VIA Nano(TM) Processor Family                                  
    218      Dual-Core Intel(R) Xeon(R) processor 5xxx Series               
    219      Quad-Core Intel(R) Xeon(R) processor 5xxx Series               
    221      Dual-Core Intel(R) Xeon(R) processor 7xxx Series               
    222      Quad-Core Intel(R) Xeon(R) processor 7xxx Series               
    223      Multi-Core Intel(R) Xeon(R) processor 7xxx Series              
    224      Multi-Core Intel(R) Xeon(R) processor 3400 Series              
    228      AMD Opteron(TM) 3000 Series Processor                          
    229      AMD Sempron(TM) II Processor Family                            
    230      Embedded AMD Opteron(TM) Quad-Core Processor Family            
    231      AMD Phenom(TM) Triple-Core Processor Family                    
    232      AMD Turion(TM) Ultra Dual-Core Mobile Processor Family         
    233      AMD Turion(TM) Dual-Core Mobile Processor Family               
    234      AMD Athlon(TM) Dual-Core Processor Family                      
    235      AMD Sempron(TM) SI Processor Family                            
    236      AMD Phenom(TM) II Processor Family                             
    237      AMD Athlon(TM) II Processor Family                             
    238      Six-Core AMD Opteron(TM) Processor Family                      
    239      AMD Sempron(TM) M Processor Family                             
    250      i860                                                           
    251      i960                                                           
    254      Reserved (SMBIOS Extension)                                    
    255      Reserved (Un-initialized Flash Content - Lo)                   
    260      SH-3                                                           
    261      SH-4                                                           
    280      ARM                                                            
    281      StrongARM                                                      
    300      6x86                                                           
    301      MediaGX                                                        
    302      MII                                                            
    320      WinChip                                                        
    350      DSP                                                            
    500      Video Processor                                                
    65534    Reserved (For Future Special Purpose Assignment)               
    65535    Reserved (Un-initialized Flash Content - Hi)                   
    ======== ===============================================================
    
.. _CIM-Processor-Characteristics:

``uint16[]`` **Characteristics**

    Array of enumerated values that describes the characteristics of the processor. The characteristics include certain features of the processor such as 64 bit support for data width of the processor. Note that if this property does not contain the value corresponding to a feature of the processor, than the feature either is not that some of the features of the processor may exist but may not be enabled. To find the the currently enabled features the processor, reffer to the EnabledProcessorCharacteristics property. Values specified in the enumeration may be obtained from SMBIOS v2.5 Type 4 offset 26h (Processor Characteristics Word). 32-bit Capable - describes whether the processor has the capability for 32 bits data width. 64-bit Capable - describes whether the processor has the capability for 64 bits data width. Enhanced Virtualization - describes whether the processor has the capability for executing enhanced virtualization instructions. Hardware Thread - indicates that the processor is capable of the hardware threading. NX-bit - describes whether the processor has capability to utilize non-execute bit and can differentiate the memory marked strictly for storage. Power/Performance Control - describes whether the processor has capability for load based power savings. Core Frequency Boosting - describes whether the processor has a capability for one processor core to increase its frequency whenever the other core has gone into an idle state.

    
    ============ =========================
    ValueMap     Values                   
    ============ =========================
    0            Unknown                  
    1            DMTF Reserved            
    2            64-bit Capable           
    3            32-bit Capable           
    4            Enhanced Virtualization  
    5            Hardware Thread          
    6            NX-bit                   
    7            Power/Performance Control
    8            Core Frequency Boosting  
    9..32567     DMTF Reserved            
    32568..65535 Vendor Reserved          
    ============ =========================
    
.. _CIM-Processor-UpgradeMethod:

``uint16`` **UpgradeMethod**

    CPU socket information that includes data on how this Processor can be upgraded (if upgrades are supported). This property is an integer enumeration.

    
    ======== ======================
    ValueMap Values                
    ======== ======================
    1        Other                 
    2        Unknown               
    3        Daughter Board        
    4        ZIF Socket            
    5        Replacement/Piggy Back
    6        None                  
    7        LIF Socket            
    8        Slot 1                
    9        Slot 2                
    10       370 Pin Socket        
    11       Slot A                
    12       Slot M                
    13       Socket 423            
    14       Socket A (Socket 462) 
    15       Socket 478            
    16       Socket 754            
    17       Socket 940            
    18       Socket 939            
    19       Socket mPGA604        
    20       Socket LGA771         
    21       Socket LGA775         
    22       Socket S1             
    23       Socket AM2            
    24       Socket F (1207)       
    25       Socket LGA1366        
    26       Socket G34            
    27       Socket AM3            
    28       Socket C32            
    29       Socket LGA1156        
    30       Socket LGA1567        
    31       Socket PGA988A        
    32       Socket BGA1288        
    33       rPGA988B              
    34       BGA1023               
    35       BGA1224               
    36       LGA1155               
    37       LGA1356               
    38       LGA2011               
    39       Socket FS1            
    40       Socket FS2            
    41       Socket FM1            
    42       Socket FM2            
    43       Socket LGA2011-3      
    44       Socket LGA1356-3      
    45       Socket LGA1150        
    46       Socket BGA1168        
    ======== ======================
    
.. _CIM-Processor-EnabledProcessorCharacteristics:

``uint16[]`` **EnabledProcessorCharacteristics**

    This property indicates the enabled states of the corresponding processor characteristics. The property array is indexed with ProcessorCharacteristics property array of the associated CIM_ProcessorCapabilities instance through the CIM_ElementCapabilities association. Each of the values in the ProcessorCharacteristics array property shall have its enabled state indicated in the corresponding element of this property array. For example; if the ProcessorCharacteristics array has value - NX-bit - for the first element of the array, then the first element of this property will contain the value for the enabled state of the NX-bit feature of the processor: whether the processor currently differentiates the dedicated storage memory based on the non-execute bit. Unknown - the processor feature is in unknown state. Enabled - the processor feature is enabled and could be used. Disabled - the processor feature is disabled and cannot be used. Not Applicable - the processor feature does not have state context.

    
    ============ ===============
    ValueMap     Values         
    ============ ===============
    0            Unknown        
    2            Enabled        
    3            Disabled       
    4            Not Applicable 
    5..32767     DMTF Reserved  
    32768..65535 Vendor Reserved
    ============ ===============
    
.. _CIM-Processor-Role:

``string`` **Role**

    A free-form string that describes the role of the Processor, for example, "Central Processor" or "Math Processor".

    
.. _CIM-Processor-CPUStatus:

``uint16`` **CPUStatus**

    The CPUStatus property that indicates the current status of the Processor. For example, the Processor might be disabled by the user (value=2), or disabled due to a POST error (value=3). Information in this property can be obtained from SMBIOS, the Type 4 structure, and the Status attribute.

    
    ======== =================================
    ValueMap Values                           
    ======== =================================
    0        Unknown                          
    1        CPU Enabled                      
    2        CPU Disabled by User             
    3        CPU Disabled By BIOS (POST Error)
    4        CPU Is Idle                      
    7        Other                            
    ======== =================================
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| ``uint64`` :ref:`PowerOnHours <CIM-LogicalDevice-PowerOnHours>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``string[]`` :ref:`IdentifyingDescriptions <CIM-LogicalDevice-IdentifyingDescriptions>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``boolean`` :ref:`ErrorCleared <CIM-LogicalDevice-ErrorCleared>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``string`` :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| ``uint16`` :ref:`LocationIndicator <CIM-LogicalDevice-LocationIndicator>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string[]`` :ref:`OtherIdentifyingInfo <CIM-LogicalDevice-OtherIdentifyingInfo>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``uint16[]`` :ref:`AdditionalAvailability <CIM-LogicalDevice-AdditionalAvailability>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16`` :ref:`StatusInfo <CIM-LogicalDevice-StatusInfo>`
| ``uint16[]`` :ref:`PowerManagementCapabilities <CIM-LogicalDevice-PowerManagementCapabilities>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`MaxQuiesceTime <CIM-LogicalDevice-MaxQuiesceTime>`
| ``uint64`` :ref:`TotalPowerOnHours <CIM-LogicalDevice-TotalPowerOnHours>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`ErrorDescription <CIM-LogicalDevice-ErrorDescription>`
| ``string`` :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint32`` :ref:`LastErrorCode <CIM-LogicalDevice-LastErrorCode>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``uint16`` :ref:`Availability <CIM-LogicalDevice-Availability>`
| ``string`` :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

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

