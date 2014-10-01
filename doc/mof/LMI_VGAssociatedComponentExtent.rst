.. _LMI-VGAssociatedComponentExtent:

LMI_VGAssociatedComponentExtent
-------------------------------

Class reference
===============
Subclass of :ref:`CIM_AssociatedComponentExtent <CIM-AssociatedComponentExtent>`

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

*None*

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| :ref:`CIM_StoragePool <CIM-StoragePool>` :ref:`GroupComponent <CIM-AssociatedComponentExtent-GroupComponent>`
| :ref:`CIM_StorageExtent <CIM-StorageExtent>` :ref:`PartComponent <CIM-AssociatedComponentExtent-PartComponent>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

