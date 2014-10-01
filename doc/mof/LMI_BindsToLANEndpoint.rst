.. _LMI-BindsToLANEndpoint:

LMI_BindsToLANEndpoint
----------------------

Class reference
===============
Subclass of :ref:`CIM_BindsToLANEndpoint <CIM-BindsToLANEndpoint>`

This association makes explicit the dependency of a SAP or ProtocolEndpoint on an underlying LANEndpoint, on the same system.


Key properties
^^^^^^^^^^^^^^

| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-BindsToLANEndpoint-Dependent:

:ref:`CIM_ServiceAccessPoint <CIM-ServiceAccessPoint>` **Dependent**

    The AccessPoint or ProtocolEndpoint dependent on the LANEndpoint.

    
.. _LMI-BindsToLANEndpoint-Antecedent:

:ref:`CIM_LANEndpoint <CIM-LANEndpoint>` **Antecedent**

    The underlying LANEndpoint, which is depended upon.

    
.. _LMI-BindsToLANEndpoint-FrameType:

``uint16`` **FrameType**

    This describes the framing method for the upper layer SAP or Endpoint that is bound to the LANEndpoint.

    
    ======== ========
    ValueMap Values  
    ======== ========
    1        Ethernet
    ======== ========
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

