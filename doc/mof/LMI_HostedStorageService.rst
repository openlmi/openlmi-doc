.. _LMI-HostedStorageService:

LMI_HostedStorageService
------------------------

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

*None*

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| :ref:`CIM_Service <CIM-Service>` :ref:`Dependent <CIM-HostedService-Dependent>`
| :ref:`CIM_System <CIM-System>` :ref:`Antecedent <CIM-HostedService-Antecedent>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

