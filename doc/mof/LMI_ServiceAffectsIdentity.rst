.. _LMI-ServiceAffectsIdentity:

LMI_ServiceAffectsIdentity
--------------------------

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

.. _LMI-ServiceAffectsIdentity-AffectedElement:

:ref:`LMI_Identity <LMI-Identity>` **AffectedElement**

    The managed Identity

    
.. _LMI-ServiceAffectsIdentity-AffectingElement:

:ref:`LMI_AccountManagementService <LMI-AccountManagementService>` **AffectingElement**

    The Central Instance of Account management

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string[]`` :ref:`OtherElementEffectsDescriptions <CIM-ServiceAffectsElement-OtherElementEffectsDescriptions>`
| ``uint16[]`` :ref:`ElementEffects <CIM-ServiceAffectsElement-ElementEffects>`
| ``uint16`` :ref:`AssignedSequence <CIM-ServiceAffectsElement-AssignedSequence>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

