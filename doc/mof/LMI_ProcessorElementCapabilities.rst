.. _LMI-ProcessorElementCapabilities:

LMI_ProcessorElementCapabilities
--------------------------------

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

.. _LMI-ProcessorElementCapabilities-Capabilities:

:ref:`LMI_ProcessorCapabilities <LMI-ProcessorCapabilities>` **Capabilities**

    The Capabilities object associated with the element.

    
.. _LMI-ProcessorElementCapabilities-ManagedElement:

:ref:`LMI_Processor <LMI-Processor>` **ManagedElement**

    The managed element.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16[]`` :ref:`Characteristics <CIM-ElementCapabilities-Characteristics>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

