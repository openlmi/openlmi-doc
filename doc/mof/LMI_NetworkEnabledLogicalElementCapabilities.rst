.. _LMI-NetworkEnabledLogicalElementCapabilities:

LMI_NetworkEnabledLogicalElementCapabilities
--------------------------------------------

Class reference
===============
Subclass of :ref:`CIM_EnabledLogicalElementCapabilities <CIM-EnabledLogicalElementCapabilities>`

EnabledLogicalElementCapabilities describes the capabilities supported for changing the state of the assciated EnabledLogicalElement.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-NetworkEnabledLogicalElementCapabilities-RequestedStatesSupported:

``uint16[]`` **RequestedStatesSupported**

    RequestedStatesSupported indicates the possible states that can be requested when using the method RequestStateChange on the EnabledLogicalElement.

    
    ======== ========
    ValueMap Values  
    ======== ========
    2        Enabled 
    3        Disabled
    ======== ========
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`ElementName <CIM-Capabilities-ElementName>`
| ``uint16`` :ref:`MaxElementNameLen <CIM-EnabledLogicalElementCapabilities-MaxElementNameLen>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`ElementNameMask <CIM-EnabledLogicalElementCapabilities-ElementNameMask>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`InstanceID <CIM-Capabilities-InstanceID>`
| ``uint16[]`` :ref:`StateAwareness <CIM-EnabledLogicalElementCapabilities-StateAwareness>`
| ``boolean`` :ref:`ElementNameEditSupported <CIM-EnabledLogicalElementCapabilities-ElementNameEditSupported>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`CreateGoalSettings <CIM-Capabilities-CreateGoalSettings>`

