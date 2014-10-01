.. _LMI-Processor:

LMI_Processor
-------------

Class reference
===============
Subclass of :ref:`CIM_Processor <CIM-Processor>`

Capabilities and management of the Processor LogicalDevice.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-Processor-InstanceID:

``string`` **InstanceID**

    InstanceID is an optional property that may be used to opaquely and uniquely identify an instance of this class within the scope of the instantiating Namespace. Various subclasses of this class may override this property to make it required, or a key. Such subclasses may also modify the preferred algorithms for ensuring uniqueness that are defined below.

    To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon (:), and where <OrgID> must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness, <OrgID> must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If not null and the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance. 

    If not set to null for DMTF-defined instances, the "preferred" algorithm must be used with the <OrgID> set to CIM.

    
.. _LMI-Processor-SystemName:

``string`` **SystemName**

    The System Name of the scoping system.

    
.. _LMI-Processor-ExternalBusClockSpeed:

``uint32`` **ExternalBusClockSpeed**

    The speed (in MHz) of the external bus interface (also known as the front side bus).

    
.. _LMI-Processor-Architecture:

``string`` **Architecture**

    System architecture.

    
.. _LMI-Processor-Role:

``string`` **Role**

    A free-form string that describes the role of the Processor, for example, "Central Processor" or "Math Processor".

    
.. _LMI-Processor-Name:

``string`` **Name**

    The Name property defines the label by which the object is known. When subclassed, the Name property can be overridden to be a Key property.

    
.. _LMI-Processor-ElementName:

``string`` **ElementName**

    A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. 

    Note that the Name property of ManagedSystemElement is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. Note that if there is an associated instance of CIM_EnabledLogicalElementCapabilities, restrictions on this properties may exist as defined in ElementNameMask and MaxElementNameLen properties defined in that class.

    
.. _LMI-Processor-Description:

``string`` **Description**

    The Description property provides a textual description of the object.

    
.. _LMI-Processor-AddressWidth:

``uint16`` **AddressWidth**

    Processor address width in bits.

    
.. _LMI-Processor-EnabledProcessorCharacteristics:

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
    
.. _LMI-Processor-CurrentClockSpeed:

``uint32`` **CurrentClockSpeed**

    The current speed (in MHz) of this Processor.

    
.. _LMI-Processor-MaxClockSpeed:

``uint32`` **MaxClockSpeed**

    The maximum speed (in MHz) of this Processor.

    
.. _LMI-Processor-UniqueID:

``string`` **UniqueID**

    A globally unique identifier for the Processor. This identifier can be unique only within a Processor Family.

    
.. _LMI-Processor-EnabledState:

``uint16`` **EnabledState**

    EnabledState is an integer enumeration that indicates the enabled and disabled states of an element. It can also indicate the transitions between these requested states. For example, shutting down (value=4) and starting (value=10) are transient states between enabled and disabled. The following text briefly summarizes the various enabled and disabled states: 

    Enabled (2) indicates that the element is or could be executing commands, will process any queued commands, and queues new requests. 

    Disabled (3) indicates that the element will not execute commands and will drop any new requests. 

    Shutting Down (4) indicates that the element is in the process of going to a Disabled state. 

    Not Applicable (5) indicates the element does not support being enabled or disabled. 

    Enabled but Offline (6) indicates that the element might be completing commands, and will drop any new requests. 

    Test (7) indicates that the element is in a test state. 

    Deferred (8) indicates that the element might be completing commands, but will queue any new requests. 

    Quiesce (9) indicates that the element is enabled but in a restricted mode.

    Starting (10) indicates that the element is in the process of going to an Enabled state. New requests are queued.

    
    ============ ===================
    ValueMap     Values             
    ============ ===================
    0            Unknown            
    1            Other              
    2            Enabled            
    3            Disabled           
    4            Shutting Down      
    5            Not Applicable     
    6            Enabled but Offline
    7            In Test            
    8            Deferred           
    9            Quiesce            
    10           Starting           
    11..32767    DMTF Reserved      
    32768..65535 Vendor Reserved    
    ============ ===================
    
.. _LMI-Processor-Caption:

``string`` **Caption**

    The Caption property is a short textual description (one- line string) of the object.

    
.. _LMI-Processor-Flags:

``uint16[]`` **Flags**

    Flags supported by Processor. (Available only for x86 architecture.)

    
    ======== ==================
    ValueMap Values            
    ======== ==================
    0        fpu               
    1        vme               
    2        de                
    3        pse               
    4        tsc               
    5        msr               
    6        pae               
    7        mce               
    8        cx8               
    9        apic              
    11       sep               
    12       mtrr              
    13       pge               
    14       mca               
    15       cmov              
    16       pat               
    17       pse36             
    18       pn                
    19       clflush           
    21       dts               
    22       acpi              
    23       mmx               
    24       fxsr              
    25       sse               
    26       sse2              
    27       ss                
    28       ht                
    29       tm                
    30       ia64              
    31       pbe               
    43       syscall           
    51       mp                
    52       nx                
    54       mmxext            
    57       fxsr_opt          
    58       pdpe1gb           
    59       rdtscp            
    61       lm                
    62       3dnowext          
    63       3dnow             
    64       recovery          
    65       longrun           
    67       lrti              
    96       cxmmx             
    97       k6_mtrr           
    98       cyrix_arr         
    99       centaur_mcr       
    100      k8                
    101      k7                
    102      p3                
    103      p4                
    104      constant_tsc      
    105      up                
    106      fxsave_leak       
    107      arch_perfmon      
    108      pebs              
    109      bts               
    110      syscall32         
    111      sysenter32        
    112      rep_good          
    113      mfence_rdtsc      
    114      lfence_rdtsc      
    115      11ap              
    116      nopl              
    118      xtopology         
    119      tsc_reliable      
    120      nonstop_tsc       
    121      clflush_monitor   
    122      extd_apicid       
    123      amd_dcm           
    124      aperfmperf        
    125      eagerfpu          
    128      pni               
    129      pclmulqdq         
    130      dtes64            
    131      monitor           
    132      ds_cpl            
    133      vmx               
    134      smx               
    135      est               
    136      tm2               
    137      ssse3             
    138      cid               
    140      fma               
    141      cx16              
    142      xtpr              
    143      pdcm              
    145      pcid              
    146      dca               
    147      sse4_1            
    148      sse4_2            
    149      x2apic            
    150      movbe             
    151      popcnt            
    152      tsc_deadline_timer
    153      aes               
    154      xsave             
    155      osxsave           
    156      avx               
    157      f16c              
    158      rdrand            
    159      hypervisor        
    162      rng               
    163      rng_en            
    166      ace               
    167      ace_en            
    168      ace2              
    169      ace2_en           
    170      phe               
    171      phe_en            
    172      pmm               
    173      pmm_en            
    192      lahf_lm           
    193      cmp_legacy        
    194      svm               
    195      extapic           
    196      cr8_legacy        
    197      abm               
    198      sse4a             
    199      misalignsse       
    200      3dnowprefetch     
    201      osvw              
    202      ibs               
    203      xop               
    204      skinit            
    205      wdt               
    207      lwp               
    208      fma4              
    209      tce               
    211      nodeid_msr        
    213      tbm               
    214      topoext           
    215      perfctr_core      
    224      ida               
    225      arat              
    226      cpb               
    227      epb               
    228      xsaveopt          
    229      pln               
    230      pts               
    231      dtherm            
    232      hw_pstate         
    256      tpr_shadow        
    257      vnmi              
    258      flexpriority      
    259      ept               
    260      vpid              
    261      npt               
    262      lbrv              
    263      svm_lock          
    264      nrip_save         
    265      tsc_scale         
    266      vmcb_clean        
    267      flushbyasid       
    268      decodeassists     
    269      pausefilter       
    270      pfthreshold       
    288      fsgsbase          
    289      tsc_adjust        
    291      bmi1              
    292      hle               
    293      avx2              
    295      smep              
    296      bmi2              
    297      erms              
    298      invpcid           
    299      rtm               
    306      rdseed            
    307      adx               
    308      smap              
    ======== ==================
    
.. _LMI-Processor-CPUStatus:

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
    
.. _LMI-Processor-NumberOfEnabledCores:

``uint16`` **NumberOfEnabledCores**

    Number of processor cores enabled for processor.

    
.. _LMI-Processor-OtherFamilyDescription:

``string`` **OtherFamilyDescription**

    A string that describes the Processor Family type. It is used when the Family property is set to 1 ("Other"). This string should be set to NULL when the Family property is any value other than 1.

    
.. _LMI-Processor-Family:

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
    
.. _LMI-Processor-Characteristics:

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
    32568        Multi-Core               
    32569..65535 Vendor Reserved          
    ============ =========================
    
.. _LMI-Processor-UpgradeMethod:

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
    
.. _LMI-Processor-Stepping:

``string`` **Stepping**

    Stepping is a free-form string that indicates the revision level of the Processor within the Processor.Family.

    
.. _LMI-Processor-CreationClassName:

``string`` **CreationClassName**

    CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

    
.. _LMI-Processor-DataWidth:

``uint16`` **DataWidth**

    Processor data width in bits.

    
.. _LMI-Processor-SystemCreationClassName:

``string`` **SystemCreationClassName**

    The CreationClassName of the scoping system.

    
.. _LMI-Processor-DeviceID:

``string`` **DeviceID**

    An address or other identifying information used to uniquely name the LogicalDevice.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``string[]`` :ref:`IdentifyingDescriptions <CIM-LogicalDevice-IdentifyingDescriptions>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``boolean`` :ref:`ErrorCleared <CIM-LogicalDevice-ErrorCleared>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``uint16`` :ref:`LoadPercentage <CIM-Processor-LoadPercentage>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string[]`` :ref:`OtherIdentifyingInfo <CIM-LogicalDevice-OtherIdentifyingInfo>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16[]`` :ref:`AdditionalAvailability <CIM-LogicalDevice-AdditionalAvailability>`
| ``uint16[]`` :ref:`PowerManagementCapabilities <CIM-LogicalDevice-PowerManagementCapabilities>`
| ``uint64`` :ref:`PowerOnHours <CIM-LogicalDevice-PowerOnHours>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`MaxQuiesceTime <CIM-LogicalDevice-MaxQuiesceTime>`
| ``uint64`` :ref:`TotalPowerOnHours <CIM-LogicalDevice-TotalPowerOnHours>`
| ``string`` :ref:`ErrorDescription <CIM-LogicalDevice-ErrorDescription>`
| ``uint16`` :ref:`StatusInfo <CIM-LogicalDevice-StatusInfo>`
| ``uint16`` :ref:`LocationIndicator <CIM-LogicalDevice-LocationIndicator>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint32`` :ref:`LastErrorCode <CIM-LogicalDevice-LastErrorCode>`
| ``uint16`` :ref:`Availability <CIM-LogicalDevice-Availability>`

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

