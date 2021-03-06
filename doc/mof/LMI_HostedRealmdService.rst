.. _LMI-HostedRealmdService:

LMI_HostedRealmdService
-----------------------

Class reference
===============
Subclass of :ref:`CIM_HostedService <CIM-HostedService>`

CIM_HostedService is an association between a Service and the System on which the functionality is located. The cardinality of this association is one-to-many. A System can host many Services. Services are weak with respect to their hosting System. Heuristic: A Service is hosted on the System where the LogicalDevices or SoftwareFeatures that implement the Service are located. The model does not represent Services hosted across multiple systems. The model is as an ApplicationSystem that acts as an aggregation point for Services that are each located on a single host.


Key properties
^^^^^^^^^^^^^^

| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-HostedRealmdService-Dependent:

:ref:`LMI_RealmdService <LMI-RealmdService>` **Dependent**

    The Central Instance of realm management

    
.. _LMI-HostedRealmdService-Antecedent:

:ref:`CIM_ComputerSystem <CIM-ComputerSystem>` **Antecedent**

    The hosting System

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

