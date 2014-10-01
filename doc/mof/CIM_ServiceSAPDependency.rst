.. _CIM-ServiceSAPDependency:

CIM_ServiceSAPDependency
------------------------

Class reference
===============
Subclass of :ref:`CIM_Dependency <CIM-Dependency>`

CIM_ServiceSAPDependency is an association between a Service and a ServiceAccessPoint that indicates that the referenced SAP is utilized by the Service to provide its functionality. For example, Boot Services can invoke BIOS Disk Services (interrupts) in order to function.


Key properties
^^^^^^^^^^^^^^

| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-ServiceSAPDependency-Dependent:

:ref:`CIM_Service <CIM-Service>` **Dependent**

    The Service that is dependent on an underlying SAP.

    
.. _CIM-ServiceSAPDependency-Antecedent:

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

