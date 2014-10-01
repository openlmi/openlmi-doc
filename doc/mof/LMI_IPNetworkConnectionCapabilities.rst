.. _LMI-IPNetworkConnectionCapabilities:

LMI_IPNetworkConnectionCapabilities
-----------------------------------

Class reference
===============
Subclass of :ref:`CIM_EnabledLogicalElementCapabilities <CIM-EnabledLogicalElementCapabilities>`

EnabledLogicalElementCapabilities describes the capabilities supported for changing the state of the assciated EnabledLogicalElement.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-IPNetworkConnectionCapabilities-ElementName:

``string`` **ElementName**

    Human readable device name

    
.. _LMI-IPNetworkConnectionCapabilities-ElementNameEditSupported:

``boolean`` **ElementNameEditSupported**

    Boolean indicating whether the ElementName can be modified.

    

Local methods
^^^^^^^^^^^^^

    .. _LMI-IPNetworkConnectionCapabilities-LMI-CreateIPSetting:

``uint16`` **LMI_CreateIPSetting** (``string`` Caption, ``uint16`` Type, ``uint16`` IPv4Type, ``uint16`` IPv6Type, :ref:`CIM_IPAssignmentSettingData <CIM-IPAssignmentSettingData>` SettingData)

    Creates a LMI_IPAssignmentSettingData instance or instance of its subclasses.

    Caller can modify the setting via ModifyInstance instrinsic method. Created IPAssignmentSettingData will be associated with instance of LMI_IPNetworkConnection that this instance is associated with.

    When both IPv4Type and IPv6Type is not ``0 - Disabled``, LMI_IPAssignmentSettingData instance with ``AddressOrigin = 11 (cumulative configuration)`` will be created and both LMI_IPAssignmentSettingData subclasses will be associated to it.

    For types ``4 - Bonding`` and ``5 - Bridging`` the associated IPNetworkConnection will be enslaved by created SettingData(meaning that LMI_CreateSlaveSetting will be automatically called).

    
    ======== =========================
    ValueMap Values                   
    ======== =========================
    0        No Error                 
    1        Unknown Error            
    2        Timeout                  
    3        Wrong Parameter          
    4        Memory Allocation Failure
    5        Backend Error            
    6        Not Implemented          
    ======== =========================
    
    **Parameters**
    
        *IN* ``string`` **Caption**
            Name of the configuration

            
        
        *IN* ``uint16`` **Type**
            Base type of the settings. Use this option to specify the type of setting. Currently supported are:

            - ``Ethernet`` - create ethernet connection. This is default value.- ``Bonding`` - create master connection for bonding- ``Bridging`` - create master connection for bridging

            
            ======== ========
            ValueMap Values  
            ======== ========
            1        Ethernet
            4        Bonding 
            5        Bridging
            ======== ========
            
        
        *IN* ``uint16`` **IPv4Type**
            Type of the setting for IPv4, default is ``0 - Disabled``.

            
            ======== ========
            ValueMap Values  
            ======== ========
            0        Disabled
            3        Static  
            4        DHCP    
            ======== ========
            
        
        *IN* ``uint16`` **IPv6Type**
            Type of the setting for IPv6, default is ``0 - Disabled``.

            
            ======== =========
            ValueMap Values   
            ======== =========
            0        Disabled 
            3        Static   
            7        DHCPv6   
            9        Stateless
            ======== =========
            
        
        *OUT* :ref:`CIM_IPAssignmentSettingData <CIM-IPAssignmentSettingData>` **SettingData**
            Created setting data

            
        
    
    .. _LMI-IPNetworkConnectionCapabilities-LMI-CreateSlaveSetting:

``uint16`` **LMI_CreateSlaveSetting** (:ref:`CIM_IPAssignmentSettingData <CIM-IPAssignmentSettingData>` MasterSettingData, :ref:`CIM_IPAssignmentSettingData <CIM-IPAssignmentSettingData>` SettingData)

    Add associated IPNetworkConnection to the given MasterSettingData. The MasterSettingData must have type ``4 - Bonding`` or ``5 - Bridging``.

    
    **Parameters**
    
        *IN* :ref:`CIM_IPAssignmentSettingData <CIM-IPAssignmentSettingData>` **MasterSettingData**
            SettingData to add IPNetworkConnection to.

            
        
        *OUT* :ref:`CIM_IPAssignmentSettingData <CIM-IPAssignmentSettingData>` **SettingData**
            Created setting data

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`MaxElementNameLen <CIM-EnabledLogicalElementCapabilities-MaxElementNameLen>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16[]`` :ref:`RequestedStatesSupported <CIM-EnabledLogicalElementCapabilities-RequestedStatesSupported>`
| ``string`` :ref:`ElementNameMask <CIM-EnabledLogicalElementCapabilities-ElementNameMask>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`InstanceID <CIM-Capabilities-InstanceID>`
| ``uint16[]`` :ref:`StateAwareness <CIM-EnabledLogicalElementCapabilities-StateAwareness>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`CreateGoalSettings <CIM-Capabilities-CreateGoalSettings>`

