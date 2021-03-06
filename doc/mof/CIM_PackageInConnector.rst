.. _CIM-PackageInConnector:

CIM_PackageInConnector
----------------------

Class reference
===============
Subclass of :ref:`CIM_ElementInConnector <CIM-ElementInConnector>`

Adapter cards and other 'packaging' are plugged into System Connectors for power and/or to transfer data. This relationship is defined by PackageInConnector. For example, it would be used to describe the insertion of a daughtercard onto another Card. Various subclasses of PackageInConnector are also defined. PackageInSlot and its subclass, CardInSlot, are two examples of subclasses.


Key properties
^^^^^^^^^^^^^^

| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-PackageInConnector-Dependent:

:ref:`CIM_PhysicalPackage <CIM-PhysicalPackage>` **Dependent**

    The Package in the Connector.

    
.. _CIM-PackageInConnector-Antecedent:

:ref:`CIM_PhysicalConnector <CIM-PhysicalConnector>` **Antecedent**

    The Connector into which the Package is inserted.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

