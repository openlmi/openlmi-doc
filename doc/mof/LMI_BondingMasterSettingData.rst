.. _LMI-BondingMasterSettingData:

LMI_BondingMasterSettingData
----------------------------

Class reference
===============
Subclass of :ref:`LMI_IPAssignmentSettingData <LMI-IPAssignmentSettingData>`

Master SettingData for bonding.

See https://www.kernel.org/doc/Documentation/networking/bonding.txt for detailed description of the configuration options.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-BondingMasterSettingData-MIIMon:

``uint64`` **MIIMon**

    Specifies the MII link monitoring frequency in milliseconds. This determines how often the link state of each slave is inspected for link failures. A value of zero disables MII link monitoring. The default value is 0.

    
.. _LMI-BondingMasterSettingData-InterfaceName:

``string`` **InterfaceName**

    The name of the virtual in-kernel bonding network interface

    
.. _LMI-BondingMasterSettingData-DownDelay:

``uint64`` **DownDelay**

    Specifies the time, in milliseconds, to wait before disabling a slave after a link failure has been detected.  This option is only valid for the miimon link monitor. The downdelay value should be a multiple of the miimon value; if not, it will be rounded down to the nearest multiple. The default value is 0.

    
.. _LMI-BondingMasterSettingData-UpDelay:

``uint64`` **UpDelay**

    Specifies the time, in milliseconds, to wait before enabling a slave after a link recovery has been detected. This option is only valid for the miimon link monitor. The updelay value should be a multiple of the miimon value; if not, it will be rounded down to the nearest multiple. The default value is 0.

    
.. _LMI-BondingMasterSettingData-Mode:

``uint16`` **Mode**

    Specifies one of the bonding policies.

    ``BalanceRR`` - Round-robin policy: Transmit packets in sequential order from the first available slave through the last.  This mode provides load balancing and fault tolerance. This is the default.

    ``ActiveBackup`` - Active-backup policy: Only one slave in the bond is active.  A different slave becomes active if, and only if, the active slave fails. The bond's MAC address is externally visible on only one port (network adapter) to avoid confusing the switch.This mode provides fault tolerance.

    ``BalanceXOR`` - XOR policy: Transmit based on the selected transmit hash policy.  This mode provides load balancing and fault tolerance.

    ``Broadcast`` - Broadcast policy: transmits everything on all slave interfaces.  This mode provides fault tolerance.

    ``802.3AD`` - IEEE 802.3ad Dynamic link aggregation.  Creates aggregation groups that share the same speed and duplex settings. Utilizes all slaves in the active aggregator according to the 802.3ad specification.

    ``BalanceTLB`` - Adaptive transmit load balancing: channel bonding that does not require any special switch support.  The outgoing traffic is distributed according to the current load (computed relative to the speed) on each slave.  Incoming traffic is received by the current slave.  If the receiving slave fails, another slave takes over the MAC address of the failed receiving slave.

    ``BalanceALB`` - Adaptive load balancing: includes BalanceTLB plus receive load balancing (rlb) for IPV4 traffic, and does not require any special switch support.

    
    ======== ============
    ValueMap Values      
    ======== ============
    0        BalanceRR   
    1        ActiveBackup
    2        BalanceXOR  
    3        Broadcast   
    4        802.3AD     
    5        BalanceTLB  
    6        BalanceALB  
    ======== ============
    
.. _LMI-BondingMasterSettingData-ARPIPTarget:

``string[]`` **ARPIPTarget**

    Specifies the IP addresses to use as ARP monitoring peers when arp_interval is > 0. The default value is no IP addresses.

    
.. _LMI-BondingMasterSettingData-ARPInterval:

``uint64`` **ARPInterval**

    Specifies the ARP link monitoring frequency in milliseconds. A value of 0 disables ARP monitoring. The default value is 0.

    

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
| ``string`` :ref:`Caption <LMI-IPAssignmentSettingData-Caption>`
| ``uint16`` :ref:`ChangeableType <CIM-SettingData-ChangeableType>`
| ``string[]`` :ref:`ComponentSetting <CIM-SettingData-ComponentSetting>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint16`` :ref:`IPv4Type <LMI-IPAssignmentSettingData-IPv4Type>`
| ``uint16`` :ref:`AddressOrigin <LMI-IPAssignmentSettingData-AddressOrigin>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`LMI_AddStaticIPRoute <LMI-IPAssignmentSettingData-LMI-AddStaticIPRoute>`

