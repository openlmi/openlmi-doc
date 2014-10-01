.. _LMI-AssociatedPowerManagementService:

LMI_AssociatedPowerManagementService
------------------------------------

Class reference
===============
Subclass of :ref:`CIM_AssociatedPowerManagementService <CIM-AssociatedPowerManagementService>`

The association between a Managed System Element and its power management service.


Key properties
^^^^^^^^^^^^^^

| :ref:`UserOfService <CIM-ServiceAvailableToElement-UserOfService>`
| :ref:`ServiceProvided <CIM-ServiceAvailableToElement-ServiceProvided>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-AssociatedPowerManagementService-UserOfService:

:ref:`CIM_ComputerSystem <CIM-ComputerSystem>` **UserOfService**

    The ManagedElement that can use the Service.

    
.. _LMI-AssociatedPowerManagementService-ServiceProvided:

:ref:`LMI_PowerManagementService <LMI-PowerManagementService>` **ServiceProvided**

    The Service that is available.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`TransitioningToPowerState <CIM-AssociatedPowerManagementService-TransitioningToPowerState>`
| ``uint16`` :ref:`PowerState <CIM-AssociatedPowerManagementService-PowerState>`
| ``uint16[]`` :ref:`AvailableRequestedPowerStates <CIM-AssociatedPowerManagementService-AvailableRequestedPowerStates>`
| ``datetime`` :ref:`PowerOnTime <CIM-AssociatedPowerManagementService-PowerOnTime>`
| ``string`` :ref:`OtherPowerState <CIM-AssociatedPowerManagementService-OtherPowerState>`
| ``uint16`` :ref:`RequestedPowerState <CIM-AssociatedPowerManagementService-RequestedPowerState>`
| ``string`` :ref:`OtherRequestedPowerState <CIM-AssociatedPowerManagementService-OtherRequestedPowerState>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

