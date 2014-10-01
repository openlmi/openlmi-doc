.. _CIM-ServiceAvailableToElement:

CIM_ServiceAvailableToElement
-----------------------------

Class reference
===============
CIM_ServiceAvailableToElement conveys the semantics of a Service that is available for the use of a ManagedElement. An example of an available Service is that a Processor and an enclosure (a PhysicalElement) can use AlertOnLAN Services to signal an incomplete or erroneous boot. In reality, AlertOnLAN is simply a HostedService on a computer system that is generally available for use and is not a dependency of the processor or enclosure. To describe that the use of this service might be restricted or have limited availability or applicability, the CIM_ServiceAvailableToElement association would be instantiated between the Service and specific CIM_Processors and CIM_Chassis.


Key properties
^^^^^^^^^^^^^^

| :ref:`UserOfService <CIM-ServiceAvailableToElement-UserOfService>`
| :ref:`ServiceProvided <CIM-ServiceAvailableToElement-ServiceProvided>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-ServiceAvailableToElement-UserOfService:

:ref:`CIM_ManagedElement <CIM-ManagedElement>` **UserOfService**

    The ManagedElement that can use the Service.

    
.. _CIM-ServiceAvailableToElement-ServiceProvided:

:ref:`CIM_Service <CIM-Service>` **ServiceProvided**

    The Service that is available.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

