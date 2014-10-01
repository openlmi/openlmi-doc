Usage
=====

Some common use cases are described in the following parts.

List services
-------------
List all services available on managed machine, print whether the service has been
started (TRUE), or stopped (FALSE) and print status string of the service::

    for service in c.root.cimv2.LMI_Service.instances():
        print "%s:\t%s" % (service.Name, service.Status)

List only enabled by default services (automatically started on boot). Note that value
of EnabledDefault property is '2' for enabled services (and it's '3' for disabled services)::

    service_cls = c.root.cimv2.LMI_Service
    for service in service_cls.instances():
        if service.EnabledDefault == service_cls.EnabledDefaultValues.Enabled:
            print service.Name

See available information about the 'cups' service::

    cups = c.root.cimv2.LMI_Service.first_instance({"Name" : "cups.service"})
    cups.doc()


Start/stop service
------------------
Start and stop 'cups' service, see status::

    cups = c.root.cimv2.LMI_Service.first_instance({"Name" : "cups.service"})
    cups.StartService()
    print cups.Status
    cups.StopService()
    print cups.Status

Enable/disable service
----------------------
Disable and enable 'cups' service, print EnabledDefault property::

    cups = c.root.cimv2.LMI_Service.first_instance({"Name" : "cups.service"})
    cups.TurnServiceOff()
    print cups.EnabledDefault
    cups.TurnServiceOn()
    print cups.EnabledDefault

Indications
-----------
OpenLMI Service provider is able (using indication manager and polling) to emit indication
event upon service (i. e. :ref:`LMI_Service <LMI-Service>` instance) property modification
(:ref:`LMI_ServiceInstanceModificationIndication <LMI-ServiceInstanceModificationIndication>`).

This is useful mainly for being notified when a service has changed state (has been started,
or stopped).

In order to receive indications, create instances of CIM_IndicationFilter (which indications
should be delivered), CIM_IndicationHandler (what to do with those indications) and
CIM_IndicationSubscription (links filter and handler together).

The following example in LMIShell does it all in one step::

    c.subscribe_indication(
        Name="service_modification",
        QueryLanguage="DMTF:CQL",
        Query="SELECT * FROM LMI_ServiceInstanceModificationIndication WHERE SOURCEINSTANCE ISA LMI_Service",
        CreationNamespace="root/interop",
        SubscriptionCreationClassName="CIM_IndicationSubscription",
        FilterCreationClassName="CIM_IndicationFilter",
        FilterSystemCreationClassName="CIM_ComputerSystem",
        FilterSourceNamespace="root/cimv2",
        HandlerCreationClassName="CIM_IndicationHandlerCIMXML",
        HandlerSystemCreationClassName="CIM_ComputerSystem",
        Destination="http://localhost:12121"
    )

Indications are sent to the location specified in 'Destination' argument.
