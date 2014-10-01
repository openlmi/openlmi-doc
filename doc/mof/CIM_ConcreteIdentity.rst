.. _CIM-ConcreteIdentity:

CIM_ConcreteIdentity
--------------------

Class reference
===============
Subclass of :ref:`CIM_LogicalIdentity <CIM-LogicalIdentity>`

CIM_ConcreteIdentity associates two elements that represent different aspects of the same underlying entity. It is defined as a concrete subclass of the abstract CIM_LogicalIdentity class, to be used in place of many specific subclasses of LogicalIdentity that add no semantics, that is, subclasses that do not clarify the type of identity, update cardinalities, or add or remove qualifiers. Note that when you define additional semantics for LogicalIdentity, this class should not be subclassed. Specific semantics continue to be defined as subclasses of the abstract CIM_LogicalIdentity. ConcreteIdentity is limited in its use as a concrete form of a general identity relationship. 



It was deemed more prudent to create this concrete subclass than to change LogicalIdentity from an abstract to a concrete class. LogicalIdentity already had multiple abstract subclasses in the CIM Schema, and wider industry usage and impact could not be anticipated.


Key properties
^^^^^^^^^^^^^^

| :ref:`SameElement <CIM-LogicalIdentity-SameElement>`
| :ref:`SystemElement <CIM-LogicalIdentity-SystemElement>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-ConcreteIdentity-SameElement:

:ref:`CIM_ManagedElement <CIM-ManagedElement>` **SameElement**

    Another aspect of the ManagedElement.

    
.. _CIM-ConcreteIdentity-SystemElement:

:ref:`CIM_ManagedElement <CIM-ManagedElement>` **SystemElement**

    One aspect of the ManagedElement. The use of 'System' in the name does not limit the scope of the association. This name is an artifact of the original definition of the association.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

