.. _LMI-BridgingMasterSettingData:

LMI_BridgingMasterSettingData
-----------------------------

Class reference
===============
Subclass of :ref:`LMI_IPAssignmentSettingData <LMI-IPAssignmentSettingData>`

Master SettingData for bridging


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-BridgingMasterSettingData-InterfaceName:

``string`` **InterfaceName**

    The name of the virtual in-kernel bridging network interface

    
.. _LMI-BridgingMasterSettingData-Priority:

``uint32`` **Priority**

    Sets the Spanning Tree Protocol (STP) priority for this bridge. Lower values are 'better'; the lowest priority bridge will be elected the root bridge.

    
.. _LMI-BridgingMasterSettingData-MaxAge:

``uint32`` **MaxAge**

    The Spanning Tree Protocol (STP) maximum message age.

    
.. _LMI-BridgingMasterSettingData-AgeingTime:

``uint32`` **AgeingTime**

    The ethernet MAC address aging time.

    
.. _LMI-BridgingMasterSettingData-ForwardDelay:

``uint32`` **ForwardDelay**

    The Spanning Tree Protocol (STP) forwarding delay.

    
.. _LMI-BridgingMasterSettingData-STP:

``boolean`` **STP**

    Controls whether Spanning Tree Protocol (STP) is enabled for this bridge.

    
.. _LMI-BridgingMasterSettingData-HelloTime:

``uint32`` **HelloTime**

    The Spanning Tree Protocol (STP) hello time.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`InstanceID <CIM-SettingData-InstanceID>`
| ``string`` :ref:`ElementName <CIM-SettingData-ElementName>`
| ``string`` :ref:`OtherAddressPrefixOriginDescription <CIM-IPAssignmentSettingData-OtherAddressPrefixOriginDescription>`
| ``string`` :ref:`ConfigurationName <CIM-SettingData-ConfigurationName>`
| ``string`` :ref:`SoOrgID <CIM-SettingData-SoOrgID>`
| ``string`` :ref:`OtherAddressSuffixOriginDescription <CIM-IPAssignmentSettingData-OtherAddressSuffixOriginDescription>`
| ``uint16`` :ref:`ProtocolIFType <LMI-IPAssignmentSettingData-ProtocolIFType>`
| ``uint16`` :ref:`AddressPrefixOrigin <CIM-IPAssignmentSettingData-AddressPrefixOrigin>`
| ``uint16`` :ref:`IPv6Type <LMI-IPAssignmentSettingData-IPv6Type>`
| ``uint16`` :ref:`AddressSuffixOrigin <CIM-IPAssignmentSettingData-AddressSuffixOrigin>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`SoID <CIM-SettingData-SoID>`
| ``uint16`` :ref:`ChangeableType <CIM-SettingData-ChangeableType>`
| ``string`` :ref:`Caption <LMI-IPAssignmentSettingData-Caption>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string[]`` :ref:`ComponentSetting <CIM-SettingData-ComponentSetting>`
| ``uint16`` :ref:`IPv4Type <LMI-IPAssignmentSettingData-IPv4Type>`
| ``uint16`` :ref:`AddressOrigin <LMI-IPAssignmentSettingData-AddressOrigin>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`LMI_AddStaticIPRoute <LMI-IPAssignmentSettingData-LMI-AddStaticIPRoute>`

