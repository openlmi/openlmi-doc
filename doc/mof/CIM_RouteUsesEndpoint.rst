.. _CIM-RouteUsesEndpoint:

CIM_RouteUsesEndpoint
---------------------

Class reference
===============
Subclass of :ref:`CIM_Dependency <CIM-Dependency>`

RouteUsesEndpoint depicts the relationship between a next hop route and the local Endpoint that is used to transmit the traffic to the 'next hop'.


Key properties
^^^^^^^^^^^^^^

| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-RouteUsesEndpoint-Dependent:

:ref:`CIM_NextHopRoute <CIM-NextHopRoute>` **Dependent**

    The route using the endpoint.

    
.. _CIM-RouteUsesEndpoint-Antecedent:

:ref:`CIM_ProtocolEndpoint <CIM-ProtocolEndpoint>` **Antecedent**

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

