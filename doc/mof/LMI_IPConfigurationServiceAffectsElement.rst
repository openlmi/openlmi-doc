.. _LMI-IPConfigurationServiceAffectsElement:

LMI_IPConfigurationServiceAffectsElement
----------------------------------------

Class reference
===============
Subclass of :ref:`CIM_ServiceAffectsElement <CIM-ServiceAffectsElement>`

IPConfigurationServiceAffectsElement represents an association between IPConfigurationService and the ManagedElements that might be affected by its execution.


Key properties
^^^^^^^^^^^^^^

| :ref:`AffectedElement <CIM-ServiceAffectsElement-AffectedElement>`
| :ref:`AffectingElement <CIM-ServiceAffectsElement-AffectingElement>`
| :ref:`AffectedElement <CIM-ServiceAffectsElement-AffectedElement>`
| :ref:`AffectingElement <CIM-ServiceAffectsElement-AffectingElement>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-IPConfigurationServiceAffectsElement-AffectedElement:

:ref:`CIM_ManagedElement <CIM-ManagedElement>` **AffectedElement**

    The Managed Element that is affected by the Service.

    
.. _LMI-IPConfigurationServiceAffectsElement-AffectingElement:

:ref:`LMI_IPConfigurationService <LMI-IPConfigurationService>` **AffectingElement**

    The Service that is affecting the ManagedElement.

    

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

