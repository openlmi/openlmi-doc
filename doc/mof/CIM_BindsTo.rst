.. _CIM-BindsTo:

CIM_BindsTo
-----------

Class reference
===============
Subclass of :ref:`CIM_SAPSAPDependency <CIM-SAPSAPDependency>`

This association establishes a ServiceAccessPoint as a requestor of protocol services from a ProtocolEndpoint. Typically, this association runs between SAPs and endpoints on a single system. Because a ProtocolEndpoint is a kind of ServiceAccessPoint, this binding can be used to establish a layering of two protocols, with the upper layer represented by the Dependent and the lower layer represented by the Antecedent.


Key properties
^^^^^^^^^^^^^^

| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-BindsTo-Dependent:

:ref:`CIM_ServiceAccessPoint <CIM-ServiceAccessPoint>` **Dependent**

    The AccessPoint or ProtocolEndpoint that is dependent on the lower-level endpoint.

    
.. _CIM-BindsTo-Antecedent:

:ref:`CIM_ProtocolEndpoint <CIM-ProtocolEndpoint>` **Antecedent**

    The lower-level endpoint that is accessed by the SAP.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

