.. _CIM-IPVersionSettingData:

CIM_IPVersionSettingData
------------------------

Class reference
===============
Subclass of :ref:`CIM_SettingData <CIM-SettingData>`

This SettingData instance represents an IP version. This instance can be associated to one or more CIM_ManagedElements (Eg. CIM_ComputerSystem or CIM_IPNetworkConnection) to respresent the IP version. The properties of the CIM_ElementSettingData can be used show the IPVersions that are configured as default, current or Next boot.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-IPVersionSettingData-ProtocolIFType:

``uint16`` **ProtocolIFType**

    An enumeration that describes the IP version.

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    0        Unknown        
    ..       DMTF Reserved  
    4096     IPv4           
    4097     IPv6           
    32768..  Vendor Reserved
    ======== ===============
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`SoOrgID <CIM-SettingData-SoOrgID>`
| ``string`` :ref:`SoID <CIM-SettingData-SoID>`
| ``string`` :ref:`ElementName <CIM-SettingData-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`ChangeableType <CIM-SettingData-ChangeableType>`
| ``string[]`` :ref:`ComponentSetting <CIM-SettingData-ComponentSetting>`
| ``string`` :ref:`InstanceID <CIM-SettingData-InstanceID>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`ConfigurationName <CIM-SettingData-ConfigurationName>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

