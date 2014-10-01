.. _CIM-ServiceAffectsElement:

CIM_ServiceAffectsElement
-------------------------

Class reference
===============
ServiceAffectsElement represents an association between a Service and the ManagedElements that might be affected by its execution. Instantiating this association indicates that running the service may change, manage, provide functionality for,or pose some burden on the ManagedElement. This burden might affect performance, throughput, availability, and so on.


Key properties
^^^^^^^^^^^^^^

| :ref:`AffectedElement <CIM-ServiceAffectsElement-AffectedElement>`
| :ref:`AffectingElement <CIM-ServiceAffectsElement-AffectingElement>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-ServiceAffectsElement-AffectingElement:

:ref:`CIM_Service <CIM-Service>` **AffectingElement**

    The Service that is affecting the ManagedElement.

    
.. _CIM-ServiceAffectsElement-OtherElementEffectsDescriptions:

``string[]`` **OtherElementEffectsDescriptions**

    Provides details for the effect at the corresponding array position in ElementEffects. This information is required if ElementEffects contains the value 1 (Other).

    
.. _CIM-ServiceAffectsElement-AffectedElement:

:ref:`CIM_ManagedElement <CIM-ManagedElement>` **AffectedElement**

    The Managed Element that is affected by the Service.

    
.. _CIM-ServiceAffectsElement-ElementEffects:

``uint16[]`` **ElementEffects**

    An enumeration that describes the effect on the ManagedElement. This array corresponds to the OtherElementEffectsDescriptions array, where the latter provides details that are related to the high-level effects enumerated by this property. Additional detail is required if the ElementEffects array contains the value 1 (Other). The values are defined as follows: 

    - Exclusive Use (2): No other Service may have this association to the element. 

    - Performance Impact (3): Deprecated in favor of "Consumes", "Enhances Performance", or "Degrades Performance". Execution of the Service may enhance or degrade the performance of the element. This may be as a side-effect of execution or as an intended consequence of methods provided by the Service. 

    - Element Integrity (4): Deprecated in favor of "Consumes", "Enhances Integrity", or "Degrades Integrity". Execution of the Service may enhance or degrade the integrity of the element. This may be as a side-effect of execution or as an intended consequence of methods provided by the Service. 

    - Manages (5): The Service manages the element. 

    - Consumes (6): Execution of the Service consumes some or all of the associated element as a consequence of running the Service. For example, the Service may consume CPU cycles, which may affect performance, or Storage which may affect both performance and integrity. (For instance, the lack of free storage can degrade integrity by reducing the ability to save state. ) "Consumes" may be used alone or in conjunction with other values, in particular, "Degrades Performance" and "Degrades Integrity". 

    "Manages" and not "Consumes" should be used to reflect allocation services that may be provided by a Service. 

    - Enhances Integrity (7): The Service may enhance integrity of the associated element. 

    - Degrades Integrity (8): The Service may degrade integrity of the associated element. 

    - Enhances Performance (9): The Service may enhance performance of the associated element. 

    - Degrades Performance (10): The Service may degrade performance of the associated element.

    
    ============== ====================
    ValueMap       Values              
    ============== ====================
    0              Unknown             
    1              Other               
    2              Exclusive Use       
    3              Performance Impact  
    4              Element Integrity   
    5              Manages             
    6              Consumes            
    7              Enhances Integrity  
    8              Degrades Integrity  
    9              Enhances Performance
    10             Degrades Performance
    ..             DMTF Reserved       
    0x8000..0xFFFF Vendor Reserved     
    ============== ====================
    
.. _CIM-ServiceAffectsElement-AssignedSequence:

``uint16`` **AssignedSequence**

    AssignedSequence is an unsigned integer 'n' that indicates the relative sequence in which order the ManagedElement instances are affected by the Service, which is associated to the ManagedElement instances through this class. The implementation of the Service shall use the relative sequence to order all the managed elements represented by ManagedElements associated through this class for servicing or prioritizing. 

    When 'n' is a positive integer, it indicates a place in the sequence of affected elements, with smaller integers indicating earlier positions in the sequence. NULL or the special value '0' indicates 'don't care'. If two or more affected elements have the same non-zero sequence number, then the ordering between those elements is irrelevant, but they must all be serviced in the appropriate order in the overall sequence. 

    A series of examples will make order of elements clearer: If all elements affected have the same sequence number, 

    regardless of whether it is '0' or non-zero, any 

    order is acceptable. 

    The values: 

    1:ELEMENT A 

    2:ELEMENT B 

    1:ELEMENT C 

    3:ELEMENT D 

    indicate two acceptable orders: A,C,B,D or C,A,B,D, 

    since A and C can be ordered in either sequence, but 

    only at the '1' position. 

    

    Note that the non-zero sequence numbers need not start with '1', and they need not be consecutive. All that matters is their relative magnitude.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

