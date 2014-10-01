.. _network-usage:

Usage
=====

All example scripts are for ``lmishell``. See it's documentation_ on OpenLMI_
page.

.. _documentation: https://fedorahosted.org/openlmi/wiki/shell
.. _OpenLMI: https://fedorahosted.org/openlmi/

We also assume that ``lmishell`` is connected to the CIMOM and the
connection is stored in ``connection`` variable and variable ``ns`` points to
cimv2 namespace::

    connection = connect("server", "username", "password")
    ns = connection.root.cimv2

Enumeration of network devices
------------------------------

Obtaining a list of network devices can be done by executing following
commands in ``lmishell``::

    for device in ns.LMI_IPNetworkConnection.instances():
        print device.ElementName


Get parameters of network devices
---------------------------------

Obtaining parameters of network device might be a little bit tricky.
DMTF standards split network device to three classes and one might need
to traverse between them through associations, see
:ref:`Networking API concepts <network-hardware>`.

Following example prints name, its status, MAC address, link technology and
maximal speed for each device.

MAC address is not in the :ref:`LMI_IPNetworkConnection<LMI-IPNetworkConnection>`
class and must be accessed through
:ref:`LMI_EndpointForIPNetworkConnection<LMI-EndpointForIPNetworkConnection>`
association to :ref:`LMI_LANEndpoint<LMI-LANEndpoint>` class,
same for MaxSpeed and LinkTechnology, those are in
:ref:`CIM_NetworkPort<CIM-NetworkPort>` subclasses, associated through
:ref:`LMI_NetworkDeviceSAPImplementation<LMI-NetworkDeviceSAPImplementation>`
class::

    for device in ns.LMI_IPNetworkConnection.instances():
        # print device name
        print device.ElementName,
        # print operating status
        print ns.LMI_IPNetworkConnection.OperatingStatusValues.value_name(device.OperatingStatus),

        # MAC address in not part of LMI_IPNetworkConnection but LMI_LANEndpoint class,
        # which is associated through LMI_EndpointForIPNetworkConnection
        lanendpoint = device.first_associator(AssocClass="LMI_EndpointForIPNetworkConnection")

        # print MAC address
        print lanendpoint.MACAddress,

        # LinkTechnology is part of CIM_NetworkPort subclasses, we need to traverse
        # through LMI_NetworkDeviceSAPImplementation association
        networkport = lanendpoint.first_associator(AssocClass="LMI_NetworkDeviceSAPImplementation")

        # print link technology
        print ns.CIM_NetworkPort.LinkTechnologyValues.value_name(networkport.LinkTechnology),

        # network speed might not be defined
        if networkport.MaxSpeed:
            # Convert bps to Mbps
            print "%dMbps" % (networkport.MaxSpeed // (1024*1024)),
        else:
            print "unknown",
        print


Get current IP configuration
----------------------------

Current IP addresses are in the
:ref:`LMI_IPProtocolEndpoint<LMI-IPProtocolEndpoint>` class associated
to given :ref:`LMI_IPNetworkConnection<LMI-IPNetworkConnection>`::

    device = ns.LMI_IPNetworkConnection.first_instance({'ElementName': 'eth0'})
    for endpoint in device.associators(AssocClass="LMI_NetworkSAPSAPDependency", ResultClass="LMI_IPProtocolEndpoint"):
        if endpoint.ProtocolIFType == ns.LMI_IPProtocolEndpoint.ProtocolIFTypeValues.IPv4:
            print "IPv4: %s/%s" % (endpoint.IPv4Address, endpoint.SubnetMask)
        elif endpoint.ProtocolIFType == ns.LMI_IPProtocolEndpoint.ProtocolIFTypeValues.IPv6:
            print "IPv6: %s/%d" % (endpoint.IPv6Address, endpoint.IPv6SubnetPrefixLength)

Default gateway is represented by instance of
:ref:`LMI_NetworkRemoteServiceAccessPoint<LMI-NetworkRemoteServiceAccessPoint>`
with ``AccessContext`` equal to ``DefaultGateway``::

    for rsap in device.associators(AssocClass="LMI_NetworkRemoteAccessAvailableToElement", ResultClass="LMI_NetworkRemoteServiceAccessPoint"):
        if rsap.AccessContext == ns.LMI_NetworkRemoteServiceAccessPoint.AccessContextValues.DefaultGateway:
            print "Default Gateway: %s" % rsap.AccessInfo


For the list of DNS servers we need to traverse the object model a little bit.
First get :ref:`LMI_IPProtocolEndpoint<LMI-IPProtocolEndpoint>` instances
associated with given :ref:`LMI_IPNetworkConnection<LMI-IPNetworkConnection>`
via :ref:`LMI_NetworkSAPSAPDependency<LMI-NetworkSAPSAPDependency>`.
Then use the same association to get instances of
:ref:`LMI_DNSProtocolEndpoint<LMI-DNSProtocolEndpoint>`.
Finally instances of
:ref:`LMI_NetworkRemoteServiceAccessPoint<LMI-NetworkRemoteServiceAccessPoint>`
with ``AccessContext`` equal to ``DNS Server`` associated through
:ref:`LMI_NetworkRemoteAccessAvailableToElement<LMI-NetworkRemoteAccessAvailableToElement>`
have the DNS server address in the ``AccessInfo`` property.

Note that there might be more possible path to get to the
RemoteServiceAccessPath and you might get duplicated entries. The ``set`` is
used here to deduplicate the list of DNS servers::

    dnsservers = set()
    for ipendpoint in device.associators(AssocClass="LMI_NetworkSAPSAPDependency", ResultClass="LMI_IPProtocolEndpoint"):
        for dnsedpoint in ipendpoint.associators(AssocClass="LMI_NetworkSAPSAPDependency", ResultClass="LMI_DNSProtocolEndpoint"):
            for rsap in dnsedpoint.associators(AssocClass="LMI_NetworkRemoteAccessAvailableToElement", ResultClass="LMI_NetworkRemoteServiceAccessPoint"):
                if rsap.AccessContext == ns.LMI_NetworkRemoteServiceAccessPoint.AccessContextValues.DNSServer:
                    dnsservers.add(rsap.AccessInfo)
    print "DNS:", ", ".join(dnsservers)


Bring up / take down a network device
-------------------------------------

.. note::
    Changing the state of a network device is not recommended! Just disconnect
    the active setting.

Use method :ref:`RequestStateChange<LMI-LANEndpoint-RequestStateChange>` of the
:ref:`LMI_LANEndpoint<LMI-LANEndpoint>` object. ``RequestedState`` parameter
can be either ``Enabled`` or ``Disabled``::

    lanendpoint = ns.LMI_LANEndpoint.first_instance({ "ElementName": "eth0" })
    lanendpoint.RequestStateChange(RequestedState=ns.LMI_LANEndpoint.RequestedStateValues.Enabled)


Enumerate available settings
----------------------------

One setting is a set of configuration options that are applicable to a network
interface. This setting is represented by a
:ref:`LMI_IPAssignmentSettingData<LMI-IPAssignmentSettingData>` instances that
have ``AddressOrigin`` equal to ``Cumulative Configuration``::

    for settingdata in ns.LMI_IPAssignmentSettingData.instances():
        if settingdata.AddressOrigin == ns.LMI_IPAssignmentSettingData.AddressOriginValues.cumulativeconfiguration:
            print "Setting: %s" % settingdata.Caption

Obtaining setting details
-------------------------

Setting configuration is spread between the instances of
:ref:`LMI_IPAssignmentSettingData<LMI-IPAssignmentSettingData>` subclasses
associated with the "master" setting::

    settingdata = ns.LMI_IPAssignmentSettingData.first_instance({ "Caption": "eth0" })
    for setting in settingdata.associators(AssocClass="LMI_OrderedIPAssignmentComponent"):
        if setting.classname == "LMI_DHCPSettingData":
            if setting.ProtocolIFType == ns.LMI_IPAssignmentSettingData.ProtocolIFTypeValues.IPv4:
                print "IPv4 DHCP"
            else:
                print "IPv6 DHCPv6"
        elif setting.classname == "LMI_ExtendedStaticIPAssignmentSettingData":
            for i in range(len(setting["IPAddresses"])):
                if setting["ProtocolIFType"] == ns.LMI_IPAssignmentSettingData.ProtocolIFTypeValues.IPv4:
                    print "Static IPv4 address: %s/%s, Gateway %s" % (
                            setting["IPAddresses"][i],
                            setting["SubnetMasks"][i],
                            setting["GatewayAddresses"][i])
                else:
                    print "Static IPv6 address: %s/%d, Gateway %s" % (
                            setting["IPAddresses"][i],
                            setting["IPv6SubnetPrefixLengths"][i],
                            setting["GatewayAddresses"][i])
        elif (setting.classname == "LMI_IPAssignmentSettingData" and
            setting["AddressOrigin"] == ns.LMI_IPAssignmentSettingData.AddressOriginValues.Stateless):
                print "IPv6 Stateless"

Create new setting
------------------

New setting is created by calling
:ref:`LMI_CreateIPSetting<LMI-IPNetworkConnectionCapabilities-LMI-CreateIPSetting>`
method on the instance of
:ref:`LMI_IPNetworkConnectionCapabilities<LMI-IPNetworkConnectionCapabilities>`,
which is associated with :ref:`LMI_IPNetworkConnection<LMI-IPNetworkConnection>`
through
:ref:`LMI_IPNetworkConnectionElementCapabilities<LMI-IPNetworkConnectionElementCapabilities>`.
It also has the ``ElementName`` property same as is the name of the network
interface.

Created setting can be modified by using ``ModifyInstance`` intrinsic method
(``push()`` in the lmishell).

Let's say we want to create a new setting with static IPv4 and stateless IPv6
configuration for given network interface::

    capability = ns.LMI_IPNetworkConnectionCapabilities.first_instance({ 'ElementName': 'eth0' })
    result = capability.LMI_CreateIPSetting(Caption='eth0 Static',
            IPv4Type=capability.LMI_CreateIPSetting.IPv4TypeValues.Static,
            IPv6Type=capability.LMI_CreateIPSetting.IPv6TypeValues.Stateless)
    setting = result.rparams["SettingData"].to_instance()
    for settingData in setting.associators(AssocClass="LMI_OrderedIPAssignmentComponent"):
        if setting.ProtocolIFType == ns.LMI_IPAssignmentSettingData.ProtocolIFTypeValues.IPv4:
            # Set static IPv4 address
            settingData.IPAddresses = ["192.168.1.100"]
            settingData.SubnetMasks = ["255.255.0.0"]
            settingData.GatewayAddresses = ["192.168.1.1"]
            settingData.push()


Set DNS servers for given setting
---------------------------------

DNS server for given setting is stored in the
:ref:`DNSServerAddresses<LMI-DNSSettingData-DNSServerAddresses>` property
of class :ref:`LMI_DNSSettingData<LMI-DNSSettingData>`.

Following code adds IPv4 DNS server to the existing setting::

    setting = ns.LMI_IPAssignmentSettingData.first_instance({ "Caption": "eth0 Static" })
    for settingData in setting.associators(AssocClass="LMI_OrderedIPAssignmentComponent"):
        if (settingData.classname == "LMI_DNSSettingData" and
                settingData.ProtocolIFType == ns.LMI_IPAssignmentSettingData.ProtocolIFTypeValues.IPv4):
            settingData.DNSServerAddresses.append("192.168.1.1")
            settingData.push()

Manage static routes for given setting
--------------------------------------

Static route can be added by calling
:ref:`LMI_AddStaticIPRoute<LMI-IPAssignmentSettingData-LMI-AddStaticIPRoute>`
method on the instance of the
:ref:`LMI_IPAssignmentSettingData<LMI-IPAssignmentSettingData>` class::

    setting = ns.LMI_IPAssignmentSettingData.first_instance({ "Caption": "eth0 Static" })
    result = setting.LMI_AddStaticIPRoute(
            AddressType=setting.LMI_AddStaticIPRouteValues.IPv4,
            DestinationAddress="192.168.2.1",
            DestinationMask="255.255.255.0")
    route = result.rparams["Route"]

Additional parameters can be set by modifying the instance of
:ref:`LMI_IPRouteSettingData<LMI-IPRouteSettingData>`. The route can be deleted
by using ``DeleteInstance`` intrinsic method (``delete()`` in lmishell).

Delete setting
--------------

For setting deletion just call DeleteInstance intrinsic method (``delete()``
in the lmishell) to the instance of
:ref:`LMI_IPAssignmentSettingData<LMI-IPAssignmentSettingData>`::

    setting = ns.LMI_IPAssignmentSettingData.first_instance({ 'Caption': 'eth0 Static' })
    setting.delete()

Apply setting
-------------

The setting can by applied to the network interface by calling
:ref:`ApplySettingToIPNetworkConnection<LMI-IPConfigurationService-ApplySettingToIPNetworkConnection>`
of the :ref:`LMI_IPConfigurationService<LMI-IPConfigurationService>` class.

This method is asynchronous and returns a job, but lmishell can call it
synchronously::

    setting = ns.LMI_IPAssignmentSettingData.first_instance({ "Caption": "eth0 Static" })
    port = ns.LMI_IPNetworkConnection.first_instance({ 'ElementName': 'ens8' })
    service = ns.LMI_IPConfigurationService.first_instance()
    service.SyncApplySettingToIPNetworkConnection(SettingData=setting, IPNetworkConnection=port, Mode=32768)

``Mode`` parameter affects how is the setting applied. Most commonly used
values are:

* Mode 1 -- apply the setting now and make it auto-activated
* Mode 2 -- just make it auto-activated, don't apply now
* Mode 4 -- disconnect and disable auto-activation
* Mode 5 -- don't change the setting state, only disable auto-activation
* Mode 32768 -- apply the setting
* Mode 32769 -- disconnect


Bridging and bonding
--------------------

.. warning::
    Bridge, bond and vlan support needs to be explicitly enabled when using
    0.8 version of NetworkManager as a backend (for example on RHEL-6). Add following
    line to the /etc/sysconfig/network file and restart NetworkManager

    NM_BOND_BRIDGE_VLAN_ENABLED=yes


Setting up
^^^^^^^^^^

Use following code to create and activate bond with eth0 and eth1 interfaces::

    # Get the interfaces
    interface1 = ns.LMI_IPNetworkConnection.first_instance({ 'ElementName': 'eth0' })
    interface2 = ns.LMI_IPNetworkConnection.first_instance({ 'ElementName': 'eth1' })

    # Get the capabilities
    capability1 = interface1.first_associator(AssocClass="LMI_IPNetworkConnectionElementCapabilities",
            ResultClass="LMI_IPNetworkConnectionCapabilities")
    capability2 = interface2.first_associator(AssocClass="LMI_IPNetworkConnectionElementCapabilities",
            ResultClass="LMI_IPNetworkConnectionCapabilities")
    # Use one of the capabilities to create the bond
    result = capability1.LMI_CreateIPSetting(Caption='Bond',
            Type=capability1.LMI_CreateIPSetting.TypeValues.Bonding,
            IPv4Type=capability1.LMI_CreateIPSetting.IPv4TypeValues.DHCP)
    setting = result.rparams["SettingData"].to_instance()
    # Get first slave setting
    slave1setting = setting.first_associator_name(ResultClass="LMI_BondingSlaveSettingData",
                AssocClass="LMI_OrderedIPAssignmentComponent")
    # Enslave the second interface using the second capability
    result = capability2.LMI_CreateSlaveSetting(MasterSettingData=setting)
    # Get second slave setting
    slave2setting = result.rparams["SettingData"]
    service = ns.LMI_IPConfigurationService.first_instance()
    # Activate the bond
    service.SyncApplySettingToIPNetworkConnection(
            SettingData=slave1setting,
            IPNetworkConnection=interface1,
            Mode=32768)
    service.SyncApplySettingToIPNetworkConnection(
            SettingData=slave2setting,
            IPNetworkConnection=interface2,
            Mode=32768)

Displaying current state
^^^^^^^^^^^^^^^^^^^^^^^^

Following code displays existing bonds and bonded interfaces::

    for linkaggregation in ns.LMI_LinkAggregator8023ad.instances():
        print "Bond: %s" % linkaggregation.Name
        for lagport in linkaggregation.associators(AssocClass="LMI_LinkAggregationBindsTo",
                ResultClass="LMI_LAGPort8023ad"):
            print "Bonded interface: %s" % lagport.Name

Following code displays existing bridges and bridged interfaces::

    for switchservice in ns.LMI_SwitchService.instances():
        print "Bridge: %s" % switchservice.Name
        for switchport in switchservice.associators(AssocClass="LMI_SwitchesAmong",
                ResultClass="LMI_SwitchPort"):
            print "Bridged interface: %s" % switchport.Name

.. todo::
    Document notifications about changes in network devices and settings
    (created, modified, deleted)
