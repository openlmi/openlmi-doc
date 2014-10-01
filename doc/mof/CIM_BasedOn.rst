.. _CIM-BasedOn:

CIM_BasedOn
-----------

Class reference
===============
Subclass of :ref:`CIM_AbstractBasedOn <CIM-AbstractBasedOn>`

BasedOn is an association describing how StorageExtents can be assembled from lower level Extents. For example, ProtectedSpaceExtents are parts of PhysicalExtents, while VolumeSets are assembled from one or more Physical or ProtectedSpaceExtents. As another example, CacheMemory can be defined independently and realized in a PhysicalElement or can be 'based on' Volatile or NonVolatileStorageExtents.


Key properties
^^^^^^^^^^^^^^

| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-BasedOn-Dependent:

:ref:`CIM_StorageExtent <CIM-StorageExtent>` **Dependent**

    The higher level StorageExtent.

    
.. _CIM-BasedOn-Antecedent:

:ref:`CIM_StorageExtent <CIM-StorageExtent>` **Antecedent**

    The lower level StorageExtent.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint64`` :ref:`StartingAddress <CIM-AbstractBasedOn-StartingAddress>`
| ``uint64`` :ref:`EndingAddress <CIM-AbstractBasedOn-EndingAddress>`
| ``uint16`` :ref:`OrderIndex <CIM-AbstractBasedOn-OrderIndex>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

