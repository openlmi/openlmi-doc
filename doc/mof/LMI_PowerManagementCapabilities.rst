.. _LMI-PowerManagementCapabilities:

LMI_PowerManagementCapabilities
-------------------------------

Class reference
===============
Subclass of :ref:`CIM_PowerManagementCapabilities <CIM-PowerManagementCapabilities>`

A class derived from Capabilities that describes the power management aspects of an element (typically a system or device). The element's power management capabilities are decoupled from a PowerManagementService, since a single service could apply to multiple elements, each with specific capabilities.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-PowerManagementCapabilities-PowerStatesSupported:

``uint16[]`` **PowerStatesSupported**

    An enumeration that indicates the power states supported by a managed element. Because this is an array, multiple values can be specified. The current values in the enumeration are: 

    4 = Sleep - Deep, corresponding to ACPI state G1, S3, or D2.

    5 = Power Cycle (Off - Soft), corresponding to ACPI state G2, S5, or D3, but where the managed element is set to return to power state "On". 

    7 = Hibernate (Off - Soft), corresponding to ACPI state S4, where the state of the managed element is preserved and will be recovered upon powering on. 

    8 = Off - Soft, corresponding to ACPI state G2, S5, or D3. 

    12 = Off - Soft  Graceful, equivalent to Off Soft but preceded by a request to the managed element to perform an orderly shutdown. 

    15 = Power Cycle (Off - Soft Graceful), equivalent to Power Cycle (Off - Soft) but preceded by a request to the managed element to perform an orderly shutdown.

    
    ======== =================================
    ValueMap Values                           
    ======== =================================
    4        Sleep - Deep                     
    5        Power Cycle (Off - Soft)         
    7        Hibernate (Off - Soft)           
    8        Off - Soft                       
    12       Off - Soft Graceful              
    15       Power Cycle (Off - Soft Graceful)
    ======== =================================
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`ElementName <CIM-Capabilities-ElementName>`
| ``string`` :ref:`OtherPowerChangeCapabilities <CIM-PowerManagementCapabilities-OtherPowerChangeCapabilities>`
| ``string[]`` :ref:`OtherPowerCapabilitiesDescriptions <CIM-PowerManagementCapabilities-OtherPowerCapabilitiesDescriptions>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16[]`` :ref:`RequestedPowerStatesSupported <CIM-PowerManagementCapabilities-RequestedPowerStatesSupported>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint16[]`` :ref:`PowerChangeCapabilities <CIM-PowerManagementCapabilities-PowerChangeCapabilities>`
| ``string`` :ref:`InstanceID <CIM-Capabilities-InstanceID>`
| ``uint16[]`` :ref:`PowerCapabilities <CIM-PowerManagementCapabilities-PowerCapabilities>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`CreateGoalSettings <CIM-Capabilities-CreateGoalSettings>`

