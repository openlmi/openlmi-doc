.. _CIM-ComputerSystemPackage:

CIM_ComputerSystemPackage
-------------------------

Class reference
===============
Subclass of :ref:`CIM_SystemPackaging <CIM-SystemPackaging>`

Similar to the way that LogicalDevices are 'Realized' by PhysicalElements, ComputerSystem may be realized in one or more PhysicalPackages. The ComputerSystemPackage association explicitly defines this relationship.


Key properties
^^^^^^^^^^^^^^

| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-ComputerSystemPackage-Dependent:

:ref:`CIM_ComputerSystem <CIM-ComputerSystem>` **Dependent**

    The UnitaryComputerSystem.

    
.. _CIM-ComputerSystemPackage-Antecedent:

:ref:`CIM_PhysicalPackage <CIM-PhysicalPackage>` **Antecedent**

    The PhysicalPackage(s) that realize a Unitary ComputerSystem.

    
.. _CIM-ComputerSystemPackage-PlatformGUID:

``string`` **PlatformGUID**

    A Gloabally Unique Identifier for the System's Package.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

