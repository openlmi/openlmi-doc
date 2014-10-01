.. _CIM-NextHopIPRoute:

CIM_NextHopIPRoute
------------------

Class reference
===============
Subclass of :ref:`CIM_NextHopRoute <CIM-NextHopRoute>`

NextHopIPRoute specifies routing in an IP network.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-NextHopIPRoute-OtherDerivation:

``string`` **OtherDerivation**

    A string describing how the route was derived when the RouteDerivation property is 1 ("Other").

    
.. _CIM-NextHopIPRoute-RouteDerivation:

``uint16`` **RouteDerivation**

    An enumerated integer indicating how the route was derived. This is useful for display and query purposes.

    
    ======== ============
    ValueMap Values      
    ======== ============
    0        Unknown     
    1        Other       
    2        Connected   
    3        User-Defined
    4        IGRP        
    5        EIGRP       
    6        RIP         
    7        Hello       
    8        EGP         
    9        BGP         
    10       ISIS        
    11       OSPF        
    ======== ============
    
.. _CIM-NextHopIPRoute-DestinationMask:

``string`` **DestinationMask**

    The mask for the Ipv4 destination address.

    
.. _CIM-NextHopIPRoute-AddressType:

``uint16`` **AddressType**

    An enumeration that describes the format of the address properties.

    
    ======== =======
    ValueMap Values 
    ======== =======
    0        Unknown
    1        IPv4   
    2        IPv6   
    ======== =======
    
.. _CIM-NextHopIPRoute-PrefixLength:

``uint8`` **PrefixLength**

    The prefix length for the IPv6 destination address.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`InstanceID <CIM-NextHopRoute-InstanceID>`
| ``boolean`` :ref:`IsStatic <CIM-NextHopRoute-IsStatic>`
| ``string`` :ref:`DestinationAddress <CIM-NextHopRoute-DestinationAddress>`
| ``uint16`` :ref:`AdminDistance <CIM-NextHopRoute-AdminDistance>`
| ``uint16`` :ref:`RouteMetric <CIM-NextHopRoute-RouteMetric>`
| ``uint16`` :ref:`TypeOfRoute <CIM-NextHopRoute-TypeOfRoute>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

