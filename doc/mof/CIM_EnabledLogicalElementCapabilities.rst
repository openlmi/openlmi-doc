.. _CIM-EnabledLogicalElementCapabilities:

CIM_EnabledLogicalElementCapabilities
-------------------------------------

Class reference
===============
Subclass of :ref:`CIM_Capabilities <CIM-Capabilities>`

EnabledLogicalElementCapabilities describes the capabilities supported for changing the state of the assciated EnabledLogicalElement.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-EnabledLogicalElementCapabilities-MaxElementNameLen:

``uint16`` **MaxElementNameLen**

    Maximum supported ElementName length.

    
.. _CIM-EnabledLogicalElementCapabilities-RequestedStatesSupported:

``uint16[]`` **RequestedStatesSupported**

    RequestedStatesSupported indicates the possible states that can be requested when using the method RequestStateChange on the EnabledLogicalElement.

    
    ======== =========
    ValueMap Values   
    ======== =========
    2        Enabled  
    3        Disabled 
    4        Shut Down
    6        Offline  
    7        Test     
    8        Defer    
    9        Quiesce  
    10       Reboot   
    11       Reset    
    ======== =========
    
.. _CIM-EnabledLogicalElementCapabilities-ElementNameMask:

``string`` **ElementNameMask**

    This string expresses the restrictions on ElementName.The mask is expressed as a regular expression.See DMTF standard ABNF with the Management Profile Specification Usage Guide, appendix C for the regular expression syntax permitted. 

    Since the ElementNameMask can describe the maximum length of the ElementName,any length defined in the regexp is in addition to the restriction defined in MaxElementNameLen (causing the smaller value to be the maximum length)The ElementName value satisfies the restriction, if and only if it matches the regular expression

    
.. _CIM-EnabledLogicalElementCapabilities-StateAwareness:

``uint16[]`` **StateAwareness**

    StateAwareness indicates support for modeling the state of the associated instance of CIM_EnabledLogicalElement. 

    If StateAwareness contains the value 2 "Implicit", the RequestedState and TransitioningToState properties of the associated instance of CIM_EnabledLogicalElement shall provide information about state transitions that were initiated through a mechanism other than invocation of the RequestStateChange() method. 

    If StateAwareness contains the value 3 "RequestStateChange", the RequestedState and TransitioningToState properties of the associated instance of CIM_EnabledLogicalElement shall provide information about state transitions initiated by invocation of the RequestStateChange() method. 

    A value of NULL or an array that contains zero elements shall indicate the RequestedState and TransitioningToState properties will not reflect any transitions, irrespective of how they are initiated.

    
    ======== ==================
    ValueMap Values            
    ======== ==================
    2        Implicit          
    3        RequestStateChange
    ..       DMTF Reserved     
    ======== ==================
    
.. _CIM-EnabledLogicalElementCapabilities-ElementNameEditSupported:

``boolean`` **ElementNameEditSupported**

    Boolean indicating whether the ElementName can be modified.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`ElementName <CIM-Capabilities-ElementName>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`InstanceID <CIM-Capabilities-InstanceID>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`CreateGoalSettings <CIM-Capabilities-CreateGoalSettings>`

