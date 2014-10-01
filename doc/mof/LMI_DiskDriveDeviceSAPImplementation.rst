.. _LMI-DiskDriveDeviceSAPImplementation:

LMI_DiskDriveDeviceSAPImplementation
------------------------------------

Class reference
===============
Subclass of :ref:`CIM_DeviceSAPImplementation <CIM-DeviceSAPImplementation>`

An association between a ServiceAccessPoint (SAP) and how it is implemented. The cardinality of this association is many-to-many. A SAP can be provided by more than one LogicalDevice, operating in conjunction. And, any Device can provide more than one ServiceAccessPoint. When many LogicalDevices are associated with a single SAP, it is assumed that these elements operate in conjunction to provide the AccessPoint. If different implementations of a SAP exist, each of these implementations would result in individual instantiations of the ServiceAccessPoint object. These individual instantiations would then have associations to the unique implementations.


Key properties
^^^^^^^^^^^^^^

| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-DiskDriveDeviceSAPImplementation-Dependent:

:ref:`LMI_DiskDriveATAProtocolEndpoint <LMI-DiskDriveATAProtocolEndpoint>` **Dependent**

    The ServiceAccessPoint implemented using the LogicalDevice.

    
.. _LMI-DiskDriveDeviceSAPImplementation-Antecedent:

:ref:`LMI_DiskDriveATAPort <LMI-DiskDriveATAPort>` **Antecedent**

    The LogicalDevice.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

