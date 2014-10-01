.. _CIM-InstMethodCall:

CIM_InstMethodCall
------------------

Class reference
===============
Subclass of :ref:`CIM_InstIndication <CIM-InstIndication>`

CIM_InstMethodCall notifies when an instance's method is invoked.


Key properties
^^^^^^^^^^^^^^


Local properties
^^^^^^^^^^^^^^^^

.. _CIM-InstMethodCall-MethodName:

``string`` **MethodName**

    The name of the method invoked.

    
.. _CIM-InstMethodCall-ReturnValueType:

``uint16`` **ReturnValueType**

    The type of the method return value.

    
    ======== =============
    ValueMap Values       
    ======== =============
    2        boolean      
    3        string       
    4        char16       
    5        uint8        
    6        sint8        
    7        uint16       
    8        sint16       
    9        uint32       
    10       sint32       
    11       uint64       
    12       sint64       
    13       datetime     
    14       real32       
    15       real64       
    16       reference    
    ..       DMTF Reserved
    ======== =============
    
.. _CIM-InstMethodCall-MethodParameters:

``string`` **MethodParameters**

    The input and output parameters of the method (depending on the PreCall property), represented as an embedded instance with a class name of "__MethodParameters".

    That embedded instance contains properties representing the parameters of the method invocation. Each parameter is mapped to a corresponding property of the same name and type. REF-typed parameters are represented as Reference-qualified properties of type string whose value is the instance path in WBEM URI format.

    If PreCall is TRUE, the embedded instance contains only properties corresponding to the input parameters of the method, and their values are the parameter values before the method call.

    If PreCall is FALSE, the embedded instance contains only properties corresponding to the output parameters of the method, and their values are the parameter values after the method call.

    
.. _CIM-InstMethodCall-ReturnValue:

``string`` **ReturnValue**

    The return value of the method (depending on the PreCall property). If PreCall is True, this property is NULL describing that there is no method return value (since the method has not yet executed).

    If PreCall is False, ReturnValue contains a string representation of the method's return value. REF-typed method return values shall be represented as an instance path in WBEM URI format

    
.. _CIM-InstMethodCall-Error:

``instance[]`` **Error**

    Error's data is dependent on the PreCall property. When PreCall is TRUE, this property is NULL describing that there is no method Error instances (since the method has not yet executed). When PreCall is FALSE, Error contains an array of zero or more entries containing CIM_ERROR instances represented as an array of Embedded Instances.

    
.. _CIM-InstMethodCall-PreCall:

``boolean`` **PreCall**

    Boolean indicating whether the Indication is sent before the method begins executing (TRUE) or when the method completes (FALSE). When TRUE, the inherited property SourceInstance contains the value of the instance (the properties defined by the Filter's Query clause), before execution of the method. When PreCall is FALSE, SourceInstance embeds the instance as it appears after the completion of the method.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`IndicationFilterName <CIM-Indication-IndicationFilterName>`
| ``string`` :ref:`OtherSeverity <CIM-Indication-OtherSeverity>`
| ``sint64`` :ref:`SequenceNumber <CIM-Indication-SequenceNumber>`
| ``string`` :ref:`SourceInstanceHost <CIM-InstIndication-SourceInstanceHost>`
| ``datetime`` :ref:`IndicationTime <CIM-Indication-IndicationTime>`
| ``string`` :ref:`SourceInstance <CIM-InstIndication-SourceInstance>`
| ``string`` :ref:`SequenceContext <CIM-Indication-SequenceContext>`
| ``string[]`` :ref:`CorrelatedIndications <CIM-Indication-CorrelatedIndications>`
| ``uint16`` :ref:`PerceivedSeverity <CIM-Indication-PerceivedSeverity>`
| ``string`` :ref:`IndicationIdentifier <CIM-Indication-IndicationIdentifier>`
| ``string`` :ref:`SourceInstanceModelPath <CIM-InstIndication-SourceInstanceModelPath>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

