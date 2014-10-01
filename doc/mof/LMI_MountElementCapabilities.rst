.. _LMI-MountElementCapabilities:

LMI_MountElementCapabilities
----------------------------

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

.. _LMI-MountElementCapabilities-Capabilities:

:ref:`LMI_MountedFileSystemCapabilities <LMI-MountedFileSystemCapabilities>` **Capabilities**

    Supported capabilities for mounting support.

    
.. _LMI-MountElementCapabilities-ManagedElement:

:ref:`LMI_MountConfigurationService <LMI-MountConfigurationService>` **ManagedElement**

    The central instance of mounting management.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16[]`` :ref:`Characteristics <CIM-ElementCapabilities-Characteristics>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

