.. _CIM-AssociatedCacheMemory:

CIM_AssociatedCacheMemory
-------------------------

Class reference
===============
Subclass of :ref:`CIM_AssociatedMemory <CIM-AssociatedMemory>`

Indicates that the Memory provides Cache to the Dependent Logical Element.


Key properties
^^^^^^^^^^^^^^

| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-AssociatedCacheMemory-WritePolicy:

``uint16`` **WritePolicy**

    Defines whether this is write-back (value=2) or write-through (value=3) Cache, or whether this information "Varies with Address" (4) or is defined individually for each I/O (5). Also, "Other" (1) and "Unknown" (0) can be specified.

    
    ======== =====================
    ValueMap Values               
    ======== =====================
    0        Unknown              
    1        Other                
    2        Write Back           
    3        Write Through        
    4        Varies with Address  
    5        Determination Per I/O
    ======== =====================
    
.. _CIM-AssociatedCacheMemory-FlushTimer:

``uint32`` **FlushTimer**

    Maximum amount of time, in seconds, dirty lines or buckets may remain in the Cache before they are flushed. A value of zero indicated that a cache flush is not controlled by a flushing timer.

    
.. _CIM-AssociatedCacheMemory-CacheType:

``uint16`` **CacheType**

    Defines whether this is for instruction caching (value=2), data caching (value=3) or both (value=4, "Unified"). Also, "Other" (1) and "Unknown" (0) can be defined.

    
    ======== ===========
    ValueMap Values     
    ======== ===========
    0        Unknown    
    1        Other      
    2        Instruction
    3        Data       
    4        Unified    
    ======== ===========
    
.. _CIM-AssociatedCacheMemory-LineSize:

``uint32`` **LineSize**

    Size, in bytes, of a single cache bucket or line.

    
.. _CIM-AssociatedCacheMemory-OtherLevelDescription:

``string`` **OtherLevelDescription**

    A string describing the cache level when the Level value is 1, "Other".

    
.. _CIM-AssociatedCacheMemory-OtherReplacementPolicyDescription:

``string`` **OtherReplacementPolicyDescription**

    A string describing the Cache replacement policy when the ReplacementPolicy value is 1, "Other".

    
.. _CIM-AssociatedCacheMemory-ReadPolicy:

``uint16`` **ReadPolicy**

    Policy that shall be employed by the Cache for handling read requests. For example, "Read", "Read-Ahead" or both can be specified using the values, 2, 3 or 4, respectively. If the read policy is determined individually (ie, for each request), then the value 5 ("Determination per I/O") should be specified. "Other" (1) and "Unknown" (0) are also valid values.

    
    ======== =====================
    ValueMap Values               
    ======== =====================
    0        Unknown              
    1        Other                
    2        Read                 
    3        Read-Ahead           
    4        Read and Read-Ahead  
    5        Determination Per I/O
    ======== =====================
    
.. _CIM-AssociatedCacheMemory-OtherWritePolicyDescription:

``string`` **OtherWritePolicyDescription**

    A string describing the Write Policy when the WritePolicy value is 1, "Other".

    
.. _CIM-AssociatedCacheMemory-ReplacementPolicy:

``uint16`` **ReplacementPolicy**

    An integer enumeration describing the algorithm to determine which cache lines or buckets should be re-used.

    
    ======== ==================================
    ValueMap Values                            
    ======== ==================================
    0        Unknown                           
    1        Other                             
    2        Unknown                           
    3        Least Recently Used (LRU)         
    4        First In First Out (FIFO)         
    5        Last In First Out (LIFO)          
    6        Least Frequently Used (LFU)       
    7        Most Frequently Used (MFU)        
    8        Data Dependent Multiple Algorithms
    ======== ==================================
    
.. _CIM-AssociatedCacheMemory-Associativity:

``uint16`` **Associativity**

    An integer enumeration defining the system cache associativity. For example, 5 indicates a fully associative cache.

    
    ======== ======================
    ValueMap Values                
    ======== ======================
    0        Unknown               
    1        Other                 
    2        Direct Mapped         
    3        2-way Set-Associative 
    4        4-way Set-Associative 
    5        Fully Associative     
    6        8-way Set-Associative 
    7        16-way Set-Associative
    8        12-way Set Associative
    9        24-way Set Associative
    10       32-way Set Associative
    11       48-way Set Associative
    12       64-way Set Associative
    13       20-way Set Associative
    ======== ======================
    
.. _CIM-AssociatedCacheMemory-OtherReadPolicyDescription:

``string`` **OtherReadPolicyDescription**

    A string describing the read policy when the ReadPolicy value is 1, "Other".

    
.. _CIM-AssociatedCacheMemory-Level:

``uint16`` **Level**

    Defines whether this is the Primary (value=3), Secondary (value=4) or Tertiary (value=5) Cache. Also, "Other" (1), "Unknown" (0) and "Not Applicable" (2) can be defined.

    
    ======== ==============
    ValueMap Values        
    ======== ==============
    0        Unknown       
    1        Other         
    2        Not Applicable
    3        Primary       
    4        Secondary     
    5        Tertiary      
    ======== ==============
    
.. _CIM-AssociatedCacheMemory-OtherAssociativityDescription:

``string`` **OtherAssociativityDescription**

    A string describing the cache associativity when the Associativity value is 1, "Other".

    
.. _CIM-AssociatedCacheMemory-OtherCacheTypeDescription:

``string`` **OtherCacheTypeDescription**

    A string describing the Cache Type when the CacheType value is 1, "Other".

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| :ref:`CIM_Memory <CIM-Memory>` :ref:`Antecedent <CIM-AssociatedMemory-Antecedent>`
| :ref:`CIM_LogicalElement <CIM-LogicalElement>` :ref:`Dependent <CIM-AssociatedMemory-Dependent>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

