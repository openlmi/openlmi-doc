.. _LMI-AffectedSoftwareJobElement:

LMI_AffectedSoftwareJobElement
------------------------------

Class reference
===============
Subclass of :ref:`LMI_AffectedJobElement <LMI-AffectedJobElement>`

AffectedJobElement represents an association between a Job and the ManagedElement(s) that may be affected by its execution. It may not be feasible for the Job to describe all of the affected elements. The main purpose of this association is to provide information when a Job requires exclusive use of the 'affected' ManagedElment(s) or when describing that side effects may result.


Key properties
^^^^^^^^^^^^^^

| :ref:`AffectedElement <CIM-AffectedJobElement-AffectedElement>`
| :ref:`AffectingElement <CIM-AffectedJobElement-AffectingElement>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-AffectedSoftwareJobElement-OtherElementEffectsDescriptions:

``string[]`` **OtherElementEffectsDescriptions**

    Provides details for the 'effect' at the corresponding array position in ElementEffects. This information is required whenever ElementEffects contains the value 1 ("Other").

    
.. _LMI-AffectedSoftwareJobElement-ElementEffects:

``uint16[]`` **ElementEffects**

    An enumeration describing the 'effect' on the ManagedElement. This array corresponds to the OtherElementEffectsDescriptions array, where the latter provides details related to the high-level 'effects' enumerated by this property. Additional detail is required if the ElementEffects array contains the value 1, "Other".

    
    ======== ==================
    ValueMap Values            
    ======== ==================
    0        Unknown           
    1        Other             
    2        Exclusive Use     
    3        Performance Impact
    4        Element Integrity 
    5        Create            
    ======== ==================
    
.. _LMI-AffectedSoftwareJobElement-AffectingElement:

:ref:`LMI_SoftwareJob <LMI-SoftwareJob>` **AffectingElement**

    The Job that is affecting the ManagedElement.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| :ref:`CIM_ManagedElement <CIM-ManagedElement>` :ref:`AffectedElement <CIM-AffectedJobElement-AffectedElement>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

