.. _CIM-InstIndication:

CIM_InstIndication
------------------

Class reference
===============
Subclass of :ref:`CIM_Indication <CIM-Indication>`

CIM_InstIndication is an abstract superclass describing changes to instances. Subclasses represent specific types of change notifications, such as instance creation, deletion and modification.


Key properties
^^^^^^^^^^^^^^


Local properties
^^^^^^^^^^^^^^^^

.. _CIM-InstIndication-SourceInstanceHost:

``string`` **SourceInstanceHost**

    The host name or IP address of the SourceInstance.

    
.. _CIM-InstIndication-SourceInstance:

``string`` **SourceInstance**

    A copy of the instance that changed to generate the Indication. SourceInstance contains the current values of the properties selected by the Indication Filter's Query. In the case of CIM_InstDeletion, the property values are copied before the instance is deleted.

    
.. _CIM-InstIndication-SourceInstanceModelPath:

``string`` **SourceInstanceModelPath**

    The Model Path of the SourceInstance. The following format MUST be used to encode the Model Path: 

    <NamespacePath>:<ClassName>.<Prop1>="<Value1>", 

    <Prop2>="<Value2>", ...

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`IndicationFilterName <CIM-Indication-IndicationFilterName>`
| ``string`` :ref:`OtherSeverity <CIM-Indication-OtherSeverity>`
| ``sint64`` :ref:`SequenceNumber <CIM-Indication-SequenceNumber>`
| ``datetime`` :ref:`IndicationTime <CIM-Indication-IndicationTime>`
| ``string`` :ref:`IndicationIdentifier <CIM-Indication-IndicationIdentifier>`
| ``string`` :ref:`SequenceContext <CIM-Indication-SequenceContext>`
| ``string[]`` :ref:`CorrelatedIndications <CIM-Indication-CorrelatedIndications>`
| ``uint16`` :ref:`PerceivedSeverity <CIM-Indication-PerceivedSeverity>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

