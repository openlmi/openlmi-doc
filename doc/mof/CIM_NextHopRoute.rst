.. _CIM-NextHopRoute:

CIM_NextHopRoute
----------------

Class reference
===============
Subclass of :ref:`CIM_ManagedElement <CIM-ManagedElement>`

NextHopRoute represents one of a series of 'hops' to reach a network destination. A route is administratively defined, or calculated/learned by a particular routing process. A ConcreteDependency associaton may be instantiated between a route and its routing service to indicate this. (In this scenario, the route is dependent on the service.)


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-NextHopRoute-DestinationAddress:

``string`` **DestinationAddress**

    The address which serves as the destination to be reached.

    
.. _CIM-NextHopRoute-InstanceID:

``string`` **InstanceID**

    Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. In order to ensure uniqueness within the NameSpace, the value of InstanceID SHOULD be constructed using the following 'preferred' algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon ':', and where <OrgID> MUST include a copyrighted, trademarked or otherwise unique name that is owned by the business entity creating/defining the InstanceID, or is a registered ID that is assigned to the business entity by a recognized global authority. (This is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness <OrgID> MUST NOT contain a colon (':'). When using this algorithm, the first colon to appear in InstanceID MUST appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and SHOULD not be re-used to identify different underlying (real-world) elements. If the above 'preferred' algorithm is not used, the defining entity MUST assure that the resultant InstanceID is not re-used across any InstanceIDs produced by this or other providers for this instance's NameSpace. 

    For DMTF defined instances, the 'preferred' algorithm MUST be used with the <OrgID> set to 'CIM'.

    
.. _CIM-NextHopRoute-IsStatic:

``boolean`` **IsStatic**

    TRUE indicates that this is a static route, and FALSE indicates a dynamically-learned route.

    
.. _CIM-NextHopRoute-AdminDistance:

``uint16`` **AdminDistance**

    The specific administrative distance of this route, overriding any default distances specified by the system or routing service.

    
.. _CIM-NextHopRoute-RouteMetric:

``uint16`` **RouteMetric**

    RouteMetric provides a numeric indication as to the preference of this route, compared to other routes that reach the same destination.

    
.. _CIM-NextHopRoute-TypeOfRoute:

``uint16`` **TypeOfRoute**

    An enumerated integer indicating whether the route is administrator-defined (value=2), computed (via a routing protocol/algorithm, value=3) or the actual route implemented in the network (value=4). The default is a computed route.

    
    ======== ===========================
    ValueMap Values                     
    ======== ===========================
    2        Administrator Defined Route
    3        Computed Route             
    4        Actual Route               
    ======== ===========================
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

