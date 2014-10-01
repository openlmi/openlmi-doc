.. _LMI-AccountManagementServiceCapabilities:

LMI_AccountManagementServiceCapabilities
----------------------------------------

Class reference
===============
Subclass of :ref:`CIM_ElementCapabilities <CIM-ElementCapabilities>`

ElementCapabilities represents the association between ManagedElements and their Capabilities. Note that the cardinality of the ManagedElement reference is Min(1). This cardinality mandates the instantiation of the ElementCapabilities association for the referenced instance of Capabilities. ElementCapabilities describes the existence requirements and context for the referenced instance of ManagedElement. Specifically, the ManagedElement MUST exist and provides the context for the Capabilities.


Key properties
^^^^^^^^^^^^^^

| :ref:`Capabilities <CIM-ElementCapabilities-Capabilities>`
| :ref:`ManagedElement <CIM-ElementCapabilities-ManagedElement>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-AccountManagementServiceCapabilities-Capabilities:

:ref:`LMI_AccountManagementCapabilities <LMI-AccountManagementCapabilities>` **Capabilities**

    The supported Capabilities for managing Linux Accounts

    
.. _LMI-AccountManagementServiceCapabilities-ManagedElement:

:ref:`LMI_AccountManagementService <LMI-AccountManagementService>` **ManagedElement**

    The Central Instance of Account Management

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16[]`` :ref:`Characteristics <CIM-ElementCapabilities-Characteristics>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

