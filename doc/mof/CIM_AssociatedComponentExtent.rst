.. _CIM-AssociatedComponentExtent:

CIM_AssociatedComponentExtent
-----------------------------

Class reference
===============
Subclass of :ref:`CIM_Component <CIM-Component>`

This association defines the capacity, expressed in StorageExtents, that together represents the entire capacity collected in a StoragePool. The capacity represented by StorageExtents may represent capacity that is allocated or unallocated. 

StorageExtents associated to a StoragePool using this association shall not be also be associated to that StoragePool using the CIM_AssociatedRemainingExtent association.


Key properties
^^^^^^^^^^^^^^

| :ref:`GroupComponent <CIM-AbstractComponent-GroupComponent>`
| :ref:`PartComponent <CIM-AbstractComponent-PartComponent>`
| :ref:`GroupComponent <CIM-AbstractComponent-GroupComponent>`
| :ref:`PartComponent <CIM-AbstractComponent-PartComponent>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-AssociatedComponentExtent-GroupComponent:

:ref:`CIM_StoragePool <CIM-StoragePool>` **GroupComponent**

    The parent StoragePool in the association.

    
.. _CIM-AssociatedComponentExtent-PartComponent:

:ref:`CIM_StorageExtent <CIM-StorageExtent>` **PartComponent**

    The component StorageExtent in the association.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

