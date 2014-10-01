.. _CIM-AllocatedFromStoragePool:

CIM_AllocatedFromStoragePool
----------------------------

Class reference
===============
Subclass of :ref:`CIM_ElementAllocatedFromPool <CIM-ElementAllocatedFromPool>`

AllocatedFromStoragePool is an association describing how LogicalElements are allocated from underlying StoragePools. These elements typically would be subclasses of StorageExtents or StoragePools.


Key properties
^^^^^^^^^^^^^^

| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`
| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-AllocatedFromStoragePool-Dependent:

:ref:`CIM_LogicalElement <CIM-LogicalElement>` **Dependent**

    The subsidiary element.

    
.. _CIM-AllocatedFromStoragePool-Antecedent:

:ref:`CIM_StoragePool <CIM-StoragePool>` **Antecedent**

    The StoragePool.

    
.. _CIM-AllocatedFromStoragePool-SpaceLimitWarningThreshold:

``uint16`` **SpaceLimitWarningThreshold**

    If the associated storage element may dynamically consume an increasing amount of space and a space limit is enforced on the element, then a non-zero warning threshold percentage indicates when a warning indication should be generated based on SpaceConsumed >= (SpaceLimit*SpaceLimitWarningThreshold)/100.

    
.. _CIM-AllocatedFromStoragePool-SpaceLimit:

``uint64`` **SpaceLimit**

    SpaceLimit is the consumption limit for the allocated storage element from the associated StoragePool. If SpaceLimt is greater than zero, the assumption is that the storage element can grow, (for instance an element representing the storage for a delta replica) 

    If SpaceLimit is greater than zero, SpaceConsumed shall not exceed the value of SpaceLimit. 

    If SpaceLimit = 0 (the default) then no limits are asserted on SpaceConsumed.

    
.. _CIM-AllocatedFromStoragePool-SpaceConsumed:

``uint64`` **SpaceConsumed**

    Space consumed from this Pool, in bytes. This value MUST be maintained so that, relative to the Antecedent StoragePool, it is possible to compute TotalManagedSpace as StoragePool.RemainingManagedSpace plus the sum of SpaceConsumed from all of the AllocatedFromStoragePool references from the antecedent StoragePool.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

