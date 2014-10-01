.. _CIM-ResidesOnExtent:

CIM_ResidesOnExtent
-------------------

Class reference
===============
Subclass of :ref:`CIM_Dependency <CIM-Dependency>`

An association between a LogicalElement and the StorageExtent where it is located. Typically, a FileSystem ResidesOn a LogicalDisk. However, it is possible for a logical file or other internal data store to reside directly on a StorageExtent or appropriate subclass.


Key properties
^^^^^^^^^^^^^^

| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-ResidesOnExtent-Dependent:

:ref:`CIM_LogicalElement <CIM-LogicalElement>` **Dependent**

    The LogicalElement that is located on the StorageExtent.

    
.. _CIM-ResidesOnExtent-Antecedent:

:ref:`CIM_StorageExtent <CIM-StorageExtent>` **Antecedent**

    The StorageExtent.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

