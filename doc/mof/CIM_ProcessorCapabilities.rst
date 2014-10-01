.. _CIM-ProcessorCapabilities:

CIM_ProcessorCapabilities
-------------------------

Class reference
===============
Subclass of :ref:`CIM_EnabledLogicalElementCapabilities <CIM-EnabledLogicalElementCapabilities>`

ProcessorCapabilities inherits the capabilities of EnabledLogicalElementCapabilities and adds properties describing processor core and hardware thread support.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-ProcessorCapabilities-NumberOfProcessorCores:

``uint16`` **NumberOfProcessorCores**

    Number of processor cores available for processor. This number would not include cores disabled by hardware and may be obtained from SMBIOS 2.5 Type 4 offset 23h.

    
.. _CIM-ProcessorCapabilities-NumberOfHardwareThreads:

``uint16`` **NumberOfHardwareThreads**

    Number of hardware threads available for the processor. May be obtained from SMBIOS v2.5 4 offset 25h.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`ElementName <CIM-Capabilities-ElementName>`
| ``uint16`` :ref:`MaxElementNameLen <CIM-EnabledLogicalElementCapabilities-MaxElementNameLen>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16[]`` :ref:`RequestedStatesSupported <CIM-EnabledLogicalElementCapabilities-RequestedStatesSupported>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`InstanceID <CIM-Capabilities-InstanceID>`
| ``uint16[]`` :ref:`StateAwareness <CIM-EnabledLogicalElementCapabilities-StateAwareness>`
| ``boolean`` :ref:`ElementNameEditSupported <CIM-EnabledLogicalElementCapabilities-ElementNameEditSupported>`
| ``string`` :ref:`ElementNameMask <CIM-EnabledLogicalElementCapabilities-ElementNameMask>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`CreateGoalSettings <CIM-Capabilities-CreateGoalSettings>`

