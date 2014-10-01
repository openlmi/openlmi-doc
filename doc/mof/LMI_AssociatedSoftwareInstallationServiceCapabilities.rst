.. _LMI-AssociatedSoftwareInstallationServiceCapabilities:

LMI_AssociatedSoftwareInstallationServiceCapabilities
-----------------------------------------------------

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

.. _LMI-AssociatedSoftwareInstallationServiceCapabilities-Characteristics:

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
    
.. _LMI-AssociatedSoftwareInstallationServiceCapabilities-Capabilities:

:ref:`LMI_SoftwareInstallationServiceCapabilities <LMI-SoftwareInstallationServiceCapabilities>` **Capabilities**

    The Capabilities object associated with the element.

    
.. _LMI-AssociatedSoftwareInstallationServiceCapabilities-ManagedElement:

:ref:`LMI_SoftwareInstallationService <LMI-SoftwareInstallationService>` **ManagedElement**

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

