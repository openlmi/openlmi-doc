.. _CIM-RemoteAccessAvailableToElement:

CIM_RemoteAccessAvailableToElement
----------------------------------

Class reference
===============
Subclass of :ref:`CIM_Dependency <CIM-Dependency>`

Describes an element's knowledge regarding accessing other (i.e., remote) Servers and Systems.


Key properties
^^^^^^^^^^^^^^

| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-RemoteAccessAvailableToElement-Dependent:

:ref:`CIM_EnabledLogicalElement <CIM-EnabledLogicalElement>` **Dependent**

    The EnabledLogicalElement which has knowledge of the remote server or system.

    
.. _CIM-RemoteAccessAvailableToElement-Antecedent:

:ref:`CIM_RemoteServiceAccessPoint <CIM-RemoteServiceAccessPoint>` **Antecedent**

    The remote server or system.

    
.. _CIM-RemoteAccessAvailableToElement-OrderOfAccess:

``uint16`` **OrderOfAccess**

    When an element is accessing remote services and systems, it MAY be necessary to order those accesses. This property defines that ordering - where lower numbers indicate a higher priority for access. A value of 0 (default) indicates that ordering does not apply. If multiple RemoteAccessPoint instances have the same value for OrderOfAccess, then these AccessPoints MAY be used in any sequence defined by the implementation.

    
.. _CIM-RemoteAccessAvailableToElement-IsDefault:

``boolean`` **IsDefault**

    Indicates that this access information is defined as a default configuration for the system.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

