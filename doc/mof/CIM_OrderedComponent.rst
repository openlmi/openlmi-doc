.. _CIM-OrderedComponent:

CIM_OrderedComponent
--------------------

Class reference
===============
Subclass of :ref:`CIM_Component <CIM-Component>`

CIM_OrderedComponent is a generic association used to establish 'part of' relationships between ManagedElements. It arranges the PartComponents in a specific assigned order. The semantics of the order depends on the context and use by the referencing classes. For example, if this association is used to arrange settings in a hierarchical order, then this specifies the sequence in which the settings are applied.


Key properties
^^^^^^^^^^^^^^

| :ref:`GroupComponent <CIM-AbstractComponent-GroupComponent>`
| :ref:`PartComponent <CIM-AbstractComponent-PartComponent>`
| :ref:`GroupComponent <CIM-AbstractComponent-GroupComponent>`
| :ref:`PartComponent <CIM-AbstractComponent-PartComponent>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-OrderedComponent-AssignedSequence:

``uint64`` **AssignedSequence**

    AssignedSequence is an unsigned integer 'n' that indicates the relative order of ManagedElement instances. When 'n' is a positive integer, it indicates a place in the sequence of members, with smaller integers indicating earlier positions in the sequence. The special value '0' indicates 'don't care'. If two or more members have the same non-zero sequence number, then the ordering between those members is irrelevant, but they must all be ordered at the appropriate place in the overall sequence. 

    

    A series of examples will make ordering of members clearer: 

    If all members have the same sequence number, 

    regardless of whether it is '0' or non-zero, any 

    order is acceptable. 

    o The values: 

    1:MEMBER A 

    2:MEMBER B 

    1:MEMBER C 

    3:MEMBER D 

    indicate two acceptable orders: A,C,B,D or C,A,B,D, 

    since A and C can be ordered in either sequence, but 

    only at the '1' position. 

    

    Note that the non-zero sequence numbers need not start with '1', and they need not be consecutive. All that matters is their relative magnitude.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| :ref:`CIM_ManagedElement <CIM-ManagedElement>` :ref:`GroupComponent <CIM-Component-GroupComponent>`
| :ref:`CIM_ManagedElement <CIM-ManagedElement>` :ref:`PartComponent <CIM-Component-PartComponent>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

