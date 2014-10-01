.. _CIM-BindsToLANEndpoint:

CIM_BindsToLANEndpoint
----------------------

Class reference
===============
Subclass of :ref:`CIM_BindsTo <CIM-BindsTo>`

This association makes explicit the dependency of a SAP or ProtocolEndpoint on an underlying LANEndpoint, on the same system.


Key properties
^^^^^^^^^^^^^^

| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-BindsToLANEndpoint-Dependent:

:ref:`CIM_ServiceAccessPoint <CIM-ServiceAccessPoint>` **Dependent**

    The AccessPoint or ProtocolEndpoint dependent on the LANEndpoint.

    
.. _CIM-BindsToLANEndpoint-Antecedent:

:ref:`CIM_LANEndpoint <CIM-LANEndpoint>` **Antecedent**

    The underlying LANEndpoint, which is depended upon.

    
.. _CIM-BindsToLANEndpoint-FrameType:

``uint16`` **FrameType**

    This describes the framing method for the upper layer SAP or Endpoint that is bound to the LANEndpoint. Note: "Raw802.3" is only known to be used with the IPX protocol.

    
    ======== ========
    ValueMap Values  
    ======== ========
    0        Unknown 
    1        Ethernet
    2        802.2   
    3        SNAP    
    4        Raw802.3
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

