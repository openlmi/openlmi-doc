.. _CIM-HostedAccessPoint:

CIM_HostedAccessPoint
---------------------

Class reference
===============
Subclass of :ref:`CIM_HostedDependency <CIM-HostedDependency>`

CIM_HostedAccessPoint is an association between a Service AccessPoint and the System on which it is provided. The cardinality of this association is one-to-many and is weak with respect to the System. Each System can host many ServiceAccessPoints. Heuristic: If the implementation of the ServiceAccessPoint is modeled, it must be implemented by a Device or SoftwareFeature that is part of the System that is hosting the ServiceAccessPoint.


Key properties
^^^^^^^^^^^^^^

| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-HostedAccessPoint-Dependent:

:ref:`CIM_ServiceAccessPoint <CIM-ServiceAccessPoint>` **Dependent**

    The SAPs that are hosted on this System.

    
.. _CIM-HostedAccessPoint-Antecedent:

:ref:`CIM_System <CIM-System>` **Antecedent**

    The hosting System.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

