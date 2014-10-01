.. _LMI-IPVersionSettingData:

LMI_IPVersionSettingData
------------------------

Class reference
===============
Subclass of :ref:`CIM_IPVersionSettingData <CIM-IPVersionSettingData>`

This SettingData instance represents an IP version. This instance can be associated to one or more CIM_ManagedElements (Eg. CIM_ComputerSystem or CIM_IPNetworkConnection) to respresent the IP version. The properties of the CIM_ElementSettingData can be used show the IPVersions that are configured as default, current or Next boot.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-IPVersionSettingData-ElementName:

``string`` **ElementName**

    The user-friendly name for this instance of SettingData. In addition, the user-friendly name can be used as an index property for a search or query. (Note: The name does not have to be unique within a namespace.)

    
.. _LMI-IPVersionSettingData-ChangeableType:

``uint16`` **ChangeableType**

    Enumeration indicating the type of setting. ``0 - Not Changeable - Persistent`` indicates the instance of SettingData represents primordial settings and shall not be modifiable. ``1 - Changeable - Transient`` indicates the SettingData represents modifiable settings that are not persisted. Establishing persistent settings from transient settings may be supported. ``2 - Changeable - Persistent`` indicates the SettingData represents a persistent configuration that may be modified. ``3 - Not Changeable - Transient`` indicates the SettingData represents a snapshot of the settings of the associated ManagedElement and is not persistent.

    
    ======== ===========================
    ValueMap Values                     
    ======== ===========================
    0        Not Changeable - Persistent
    1        Changeable - Transient     
    2        Changeable - Persistent    
    3        Not Changeable - Transient 
    ======== ===========================
    
.. _LMI-IPVersionSettingData-ProtocolIFType:

``uint16`` **ProtocolIFType**

    An enumeration that describes the IP version.

    
    ======== ======
    ValueMap Values
    ======== ======
    4096     IPv4  
    4097     IPv6  
    ======== ======
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`SoOrgID <CIM-SettingData-SoOrgID>`
| ``string`` :ref:`SoID <CIM-SettingData-SoID>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string[]`` :ref:`ComponentSetting <CIM-SettingData-ComponentSetting>`
| ``string`` :ref:`InstanceID <CIM-SettingData-InstanceID>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`ConfigurationName <CIM-SettingData-ConfigurationName>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

