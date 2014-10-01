.. _CIM-InstModification:

CIM_InstModification
--------------------

Class reference
===============
Subclass of :ref:`CIM_InstIndication <CIM-InstIndication>`

CIM_InstModification notifies when an instance is modified.


Key properties
^^^^^^^^^^^^^^


Local properties
^^^^^^^^^^^^^^^^

.. _CIM-InstModification-ChangedPropertyNames:

``string[]`` **ChangedPropertyNames**

    This property lists the names of those properties of the object embedded in the SourceInstance whose change generated the indication.

    Each property name shall be included at most once.

    If the infrastructure cannot reliably determine which properties have changed, this property shall be NULL.

    Notes:

    \tKey properties do not change, so will not be listed.

    \tRead-only property values can change, so might be listed.

    \tBecause of the protocol dependent serialization EmbeddedObjects, properties that transition from or to NULL are not necessarily listed in the EmbeddedObject of the corresponding PreviousInstance or SourceInstance.

    
.. _CIM-InstModification-PreviousInstance:

``string`` **PreviousInstance**

    The property values of the object embedded in PreviousInstance shall reflect the consistent state of that object before the change that is reported in the indication.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`OtherSeverity <CIM-Indication-OtherSeverity>`
| ``string`` :ref:`SourceInstanceHost <CIM-InstIndication-SourceInstanceHost>`
| ``string`` :ref:`IndicationFilterName <CIM-Indication-IndicationFilterName>`
| ``datetime`` :ref:`IndicationTime <CIM-Indication-IndicationTime>`
| ``sint64`` :ref:`SequenceNumber <CIM-Indication-SequenceNumber>`
| ``string`` :ref:`SequenceContext <CIM-Indication-SequenceContext>`
| ``string`` :ref:`SourceInstance <CIM-InstIndication-SourceInstance>`
| ``string[]`` :ref:`CorrelatedIndications <CIM-Indication-CorrelatedIndications>`
| ``uint16`` :ref:`PerceivedSeverity <CIM-Indication-PerceivedSeverity>`
| ``string`` :ref:`IndicationIdentifier <CIM-Indication-IndicationIdentifier>`
| ``string`` :ref:`SourceInstanceModelPath <CIM-InstIndication-SourceInstanceModelPath>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

