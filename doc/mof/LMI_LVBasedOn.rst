.. _LMI-LVBasedOn:

LMI_LVBasedOn
-------------

Class reference
===============
Subclass of :ref:`CIM_BasedOn <CIM-BasedOn>`

BasedOn is an association describing how StorageExtents can be assembled from lower level Extents. For example, ProtectedSpaceExtents are parts of PhysicalExtents, while VolumeSets are assembled from one or more Physical or ProtectedSpaceExtents. As another example, CacheMemory can be defined independently and realized in a PhysicalElement or can be 'based on' Volatile or NonVolatileStorageExtents.


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

| :ref:`CIM_StorageExtent <CIM-StorageExtent>` :ref:`Dependent <CIM-BasedOn-Dependent>`
| :ref:`CIM_StorageExtent <CIM-StorageExtent>` :ref:`Antecedent <CIM-BasedOn-Antecedent>`
| ``uint64`` :ref:`StartingAddress <CIM-AbstractBasedOn-StartingAddress>`
| ``uint64`` :ref:`EndingAddress <CIM-AbstractBasedOn-EndingAddress>`
| ``uint16`` :ref:`OrderIndex <CIM-AbstractBasedOn-OrderIndex>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

