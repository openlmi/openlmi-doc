.. _LMI-SoftwareInstallationServiceAffectsElement:

LMI_SoftwareInstallationServiceAffectsElement
---------------------------------------------

Class reference
===============
Subclass of :ref:`CIM_ServiceAffectsElement <CIM-ServiceAffectsElement>`

ServiceAffectsElement represents an association between a Service and the ManagedElements that might be affected by its execution. Instantiating this association indicates that running the service may change, manage, provide functionality for,or pose some burden on the ManagedElement. This burden might affect performance, throughput, availability, and so on.


Key properties
^^^^^^^^^^^^^^

| :ref:`AffectedElement <CIM-ServiceAffectsElement-AffectedElement>`
| :ref:`AffectingElement <CIM-ServiceAffectsElement-AffectingElement>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-SoftwareInstallationServiceAffectsElement-OtherElementEffectsDescriptions:

``string[]`` **OtherElementEffectsDescriptions**

    Provides details for the effect at the corresponding array position in ElementEffects. This information is required if ElementEffects contains the value 1 (Other).

    
.. _LMI-SoftwareInstallationServiceAffectsElement-ElementEffects:

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
    
.. _LMI-SoftwareInstallationServiceAffectsElement-AffectingElement:

:ref:`LMI_SoftwareInstallationService <LMI-SoftwareInstallationService>` **AffectingElement**

    The Service that is affecting the ManagedElement.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| :ref:`CIM_ManagedElement <CIM-ManagedElement>` :ref:`AffectedElement <CIM-ServiceAffectsElement-AffectedElement>`
| ``uint16`` :ref:`AssignedSequence <CIM-ServiceAffectsElement-AssignedSequence>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

