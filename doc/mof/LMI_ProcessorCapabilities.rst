.. _LMI-ProcessorCapabilities:

LMI_ProcessorCapabilities
-------------------------

Class reference
===============
Subclass of :ref:`CIM_ProcessorCapabilities <CIM-ProcessorCapabilities>`

ProcessorCapabilities inherits the capabilities of EnabledLogicalElementCapabilities and adds properties describing processor core and hardware thread support.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-ProcessorCapabilities-ElementName:

``string`` **ElementName**

    The user friendly name for this instance of Capabilities. In addition, the user friendly name can be used as a index property for a search of query. (Note: Name does not have to be unique within a namespace.)

    
.. _LMI-ProcessorCapabilities-Description:

``string`` **Description**

    The Description property provides a textual description of the object.

    
.. _LMI-ProcessorCapabilities-InstanceID:

``string`` **InstanceID**

    Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. In order to ensure uniqueness within the NameSpace, the value of InstanceID SHOULD be constructed using the following 'preferred' algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon ':', and where <OrgID> MUST include a copyrighted, trademarked or otherwise unique name that is owned by the business entity creating/defining the InstanceID, or is a registered ID that is assigned to the business entity by a recognized global authority (This is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness <OrgID> MUST NOT contain a colon (':'). When using this algorithm, the first colon to appear in InstanceID MUST appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and SHOULD not be re-used to identify different underlying (real-world) elements. If the above 'preferred' algorithm is not used, the defining entity MUST assure that the resultant InstanceID is not re-used across any InstanceIDs produced by this or other providers for this instance's NameSpace. 

    For DMTF defined instances, the 'preferred' algorithm MUST be used with the <OrgID> set to 'CIM'.

    
.. _LMI-ProcessorCapabilities-NumberOfProcessorCores:

``uint16`` **NumberOfProcessorCores**

    Number of processor cores available for processor. This number would not include cores disabled by hardware and may be obtained from SMBIOS 2.5 Type 4 offset 23h.

    
.. _LMI-ProcessorCapabilities-Caption:

``string`` **Caption**

    The Caption property is a short textual description (one- line string) of the object.

    
.. _LMI-ProcessorCapabilities-NumberOfHardwareThreads:

``uint16`` **NumberOfHardwareThreads**

    Number of hardware threads available for the processor. May be obtained from SMBIOS v2.5 4 offset 25h.

    
.. _LMI-ProcessorCapabilities-ElementNameEditSupported:

``boolean`` **ElementNameEditSupported**

    Boolean indicating whether the ElementName can be modified.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16[]`` :ref:`RequestedStatesSupported <CIM-EnabledLogicalElementCapabilities-RequestedStatesSupported>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint16[]`` :ref:`StateAwareness <CIM-EnabledLogicalElementCapabilities-StateAwareness>`
| ``string`` :ref:`ElementNameMask <CIM-EnabledLogicalElementCapabilities-ElementNameMask>`
| ``uint16`` :ref:`MaxElementNameLen <CIM-EnabledLogicalElementCapabilities-MaxElementNameLen>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`CreateGoalSettings <CIM-Capabilities-CreateGoalSettings>`

