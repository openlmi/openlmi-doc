.. _LMI-EndpointIdentity:

LMI_EndpointIdentity
--------------------

Class reference
===============
Subclass of :ref:`CIM_EndpointIdentity <CIM-EndpointIdentity>`

CIM_EndpointIdentity indicates that two ProtocolEndpoints represent different aspects of the same underlying address or protocol-specific ID. This association refines the CIM_LogicalIdentity superclass by restricting it to the Endpoint level and defining its use in well understood scenarios. One of these scenarios is to represent that an Endpoint has both 'LAN' and protocol-specific aspects. For example, an Endpoint could be both a LANEndpoint as well as a DHCPEndpoint.


Key properties
^^^^^^^^^^^^^^

| :ref:`SameElement <CIM-LogicalIdentity-SameElement>`
| :ref:`SystemElement <CIM-LogicalIdentity-SystemElement>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-EndpointIdentity-SameElement:

:ref:`CIM_ProtocolEndpoint <CIM-ProtocolEndpoint>` **SameElement**

    SameElement represents an alternate aspect of the Endpoint.

    
.. _LMI-EndpointIdentity-SystemElement:

:ref:`CIM_ProtocolEndpoint <CIM-ProtocolEndpoint>` **SystemElement**

    SystemElement represents one aspect of the Endpoint.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

