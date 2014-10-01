.. _LMI-NetworkInstModification:

LMI_NetworkInstModification
---------------------------

Class reference
===============
Subclass of :ref:`CIM_InstModification <CIM-InstModification>`

LMI_NetworkInstModification notifies when an instance of one of the following classes is modified: LMI_IPAssignmentSettingData and LMI_IPNetworkConnection.

LMI_NetworkInstModification with LMI_IPNetworkConnection as a ``SourceInstance`` is also used to notify that Setting has been applied to IPNetworkConnection.


Key properties
^^^^^^^^^^^^^^


Local properties
^^^^^^^^^^^^^^^^

*None*

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string[]`` :ref:`ChangedPropertyNames <CIM-InstModification-ChangedPropertyNames>`
| ``string`` :ref:`OtherSeverity <CIM-Indication-OtherSeverity>`
| ``string`` :ref:`PreviousInstance <CIM-InstModification-PreviousInstance>`
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

