.. _LMI-NetworkSAPSAPDependency:

LMI_NetworkSAPSAPDependency
---------------------------

Class reference
===============
Subclass of :ref:`CIM_SAPSAPDependency <CIM-SAPSAPDependency>`

CIM_SAPSAPDependency is an association between one ServiceAccessPoint and another ServiceAccessPoint that indicates that the latter is required for the former to utilize or connect with its Service. For example, to print to a network printer, local Print Access Points must utilize underlying network-related SAPs, or ProtocolEndpoints, to send the print request.


Key properties
^^^^^^^^^^^^^^

| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-NetworkSAPSAPDependency-Dependent:

:ref:`CIM_ServiceAccessPoint <CIM-ServiceAccessPoint>` **Dependent**

    The ServiceAccessPoint that is dependent on an underlying SAP.

    
.. _LMI-NetworkSAPSAPDependency-Antecedent:

:ref:`CIM_ServiceAccessPoint <CIM-ServiceAccessPoint>` **Antecedent**

    The required ServiceAccessPoint.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

