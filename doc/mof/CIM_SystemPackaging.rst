.. _CIM-SystemPackaging:

CIM_SystemPackaging
-------------------

Class reference
===============
Subclass of :ref:`CIM_Dependency <CIM-Dependency>`

Similar to the way that LogicalDevices are 'Realized' by PhysicalElements, Systems can be associated with specific packaging or PhysicalElements. This association explicitly defines the relationship between a System and its packaging.


Key properties
^^^^^^^^^^^^^^

| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-SystemPackaging-Dependent:

:ref:`CIM_System <CIM-System>` **Dependent**

    The System whose packaging is described.

    
.. _CIM-SystemPackaging-Antecedent:

:ref:`CIM_PhysicalElement <CIM-PhysicalElement>` **Antecedent**

    The PhysicalElements that provide the packaging of a System.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

