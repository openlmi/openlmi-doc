.. _LMI-AffectedStorageJobElement:

LMI_AffectedStorageJobElement
-----------------------------

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

*None*

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string[]`` :ref:`OtherElementEffectsDescriptions <CIM-AffectedJobElement-OtherElementEffectsDescriptions>`
| :ref:`CIM_ManagedElement <CIM-ManagedElement>` :ref:`AffectedElement <CIM-AffectedJobElement-AffectedElement>`
| ``uint16[]`` :ref:`ElementEffects <CIM-AffectedJobElement-ElementEffects>`
| :ref:`CIM_Job <CIM-Job>` :ref:`AffectingElement <CIM-AffectedJobElement-AffectingElement>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

