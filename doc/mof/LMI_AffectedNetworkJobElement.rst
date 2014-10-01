.. _LMI-AffectedNetworkJobElement:

LMI_AffectedNetworkJobElement
-----------------------------

Class reference
===============
Subclass of :ref:`LMI_AffectedJobElement <LMI-AffectedJobElement>`

AffectedJobElement represents an association between a Job and the ManagedElement(s) that may be affected by its execution. It may not be feasible for the Job to describe all of the affected elements. The main purpose of this association is to provide information when a Job requires exclusive use of the 'affected' ManagedElment(s) or when describing that side effects may result.


Key properties
^^^^^^^^^^^^^^

| :ref:`AffectedElement <LMI-AffectedNetworkJobElement-AffectedElement>`
| :ref:`AffectingElement <LMI-AffectedNetworkJobElement-AffectingElement>`
| :ref:`AffectedElement <CIM-AffectedJobElement-AffectedElement>`
| :ref:`AffectingElement <CIM-AffectedJobElement-AffectingElement>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-AffectedNetworkJobElement-AffectedElement:

:ref:`CIM_ManagedElement <CIM-ManagedElement>` **AffectedElement**

    The ManagedElement affected by the execution of the Job.

    
.. _LMI-AffectedNetworkJobElement-AffectingElement:

:ref:`LMI_NetworkJob <LMI-NetworkJob>` **AffectingElement**

    The Job that is affecting the ManagedElement.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string[]`` :ref:`OtherElementEffectsDescriptions <CIM-AffectedJobElement-OtherElementEffectsDescriptions>`
| ``uint16[]`` :ref:`ElementEffects <CIM-AffectedJobElement-ElementEffects>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

