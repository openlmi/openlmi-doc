.. _CIM-AccountOnSystem:

CIM_AccountOnSystem
-------------------

Class reference
===============
Subclass of :ref:`CIM_SystemComponent <CIM-SystemComponent>`

A system (e.g., ApplicationSystem, ComputerSystem, AdminDomain) aggregates Accounts and scopes the uniqueness of the Account names (i.e., userids).


Key properties
^^^^^^^^^^^^^^

| :ref:`GroupComponent <CIM-AbstractComponent-GroupComponent>`
| :ref:`PartComponent <CIM-AbstractComponent-PartComponent>`
| :ref:`GroupComponent <CIM-AbstractComponent-GroupComponent>`
| :ref:`PartComponent <CIM-AbstractComponent-PartComponent>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-AccountOnSystem-GroupComponent:

:ref:`CIM_System <CIM-System>` **GroupComponent**

    The aggregating system also provides name scoping for the Account.

    
.. _CIM-AccountOnSystem-PartComponent:

:ref:`CIM_Account <CIM-Account>` **PartComponent**

    The subordinate Account.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

