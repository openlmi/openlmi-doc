.. _CIM-ElementCapabilities:

CIM_ElementCapabilities
-----------------------

Class reference
===============
ElementCapabilities represents the association between ManagedElements and their Capabilities. Note that the cardinality of the ManagedElement reference is Min(1). This cardinality mandates the instantiation of the ElementCapabilities association for the referenced instance of Capabilities. ElementCapabilities describes the existence requirements and context for the referenced instance of ManagedElement. Specifically, the ManagedElement MUST exist and provides the context for the Capabilities.


Key properties
^^^^^^^^^^^^^^

| :ref:`Capabilities <CIM-ElementCapabilities-Capabilities>`
| :ref:`ManagedElement <CIM-ElementCapabilities-ManagedElement>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-ElementCapabilities-Characteristics:

``uint16[]`` **Characteristics**

    Characteristics provides descriptive information about the Capabilities. when the value 2 "Default" is specified, the associated Capabilities shall represent the default capabilities of the associated Managed Element 

    when the value 2 "Default" is not specified, the Capabilities instance may represent the default capabilities of the Managed Element

    When the value 3 "Current" is specified, the associated Capabilities shall represent the current capabilities of the associated Managed Element

    When the value 3 "Current" is not specified, the Capabilities instance may represent the current capabilities of the Managed Element.

    
    ============ ===============
    ValueMap     Values         
    ============ ===============
    2            Default        
    3            Current        
    ..           DMTF Reserved  
    32768..65535 Vendor Specific
    ============ ===============
    
.. _CIM-ElementCapabilities-Capabilities:

:ref:`CIM_Capabilities <CIM-Capabilities>` **Capabilities**

    The Capabilities object associated with the element.

    
.. _CIM-ElementCapabilities-ManagedElement:

:ref:`CIM_ManagedElement <CIM-ManagedElement>` **ManagedElement**

    The managed element.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

