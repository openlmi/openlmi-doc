.. _LMI-NextHopIPRoute:

LMI_NextHopIPRoute
------------------

Class reference
===============
Subclass of :ref:`CIM_NextHopIPRoute <CIM-NextHopIPRoute>`

NextHopIPRoute specifies routing in an IP network.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-NextHopIPRoute-DestinationAddress:

``string`` **DestinationAddress**

    The address which serves as the destination to be reached.

    
.. _LMI-NextHopIPRoute-AddressType:

``uint16`` **AddressType**

    An enumeration that describes the format of the address properties.

    
    ======== =======
    ValueMap Values 
    ======== =======
    0        Unknown
    1        IPv4   
    2        IPv6   
    ======== =======
    
.. _LMI-NextHopIPRoute-DestinationMask:

``string`` **DestinationMask**

    The mask for the IPv4 destination address.

    
.. _LMI-NextHopIPRoute-RouteMetric:

``uint16`` **RouteMetric**

    RouteMetric provides a numeric indication as to the preference of this route, compared to other routes that reach the same destination.

    
.. _LMI-NextHopIPRoute-NextHop:

``string`` **NextHop**

    Address of the next-hop router

    
.. _LMI-NextHopIPRoute-PrefixLength:

``uint8`` **PrefixLength**

    The prefix length for the IPv6 destination address.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``boolean`` :ref:`IsStatic <CIM-NextHopRoute-IsStatic>`
| ``string`` :ref:`OtherDerivation <CIM-NextHopIPRoute-OtherDerivation>`
| ``uint16`` :ref:`AdminDistance <CIM-NextHopRoute-AdminDistance>`
| ``string`` :ref:`InstanceID <CIM-NextHopRoute-InstanceID>`
| ``uint16`` :ref:`RouteDerivation <CIM-NextHopIPRoute-RouteDerivation>`
| ``uint16`` :ref:`TypeOfRoute <CIM-NextHopRoute-TypeOfRoute>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

