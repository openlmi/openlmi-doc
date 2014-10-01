.. _LMI-RouteUsesEndpoint:

LMI_RouteUsesEndpoint
---------------------

Class reference
===============
Subclass of :ref:`CIM_RouteUsesEndpoint <CIM-RouteUsesEndpoint>`

RouteUsesEndpoint depicts the relationship between a next hop route and the local Endpoint that is used to transmit the traffic to the 'next hop'.


Key properties
^^^^^^^^^^^^^^

| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-RouteUsesEndpoint-Dependent:

:ref:`LMI_NextHopIPRoute <LMI-NextHopIPRoute>` **Dependent**

    The route using the endpoint.

    
.. _LMI-RouteUsesEndpoint-Antecedent:

:ref:`LMI_IPProtocolEndpoint <LMI-IPProtocolEndpoint>` **Antecedent**

    The endpoint used to reach the route's destination.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

