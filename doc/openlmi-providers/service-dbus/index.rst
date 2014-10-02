.. _openlmi-software-provider:

Service Provider
================

OpenLMI Service is CIM provider for managing Linux system services (using
the systemd D-Bus interface).

It allows to enumerate system services and get their status, start/stop/restart/...
a service and enable/disable a service.

The provider is also able to do event based monitoring of service status
(emit indication event upon service property change).

Contents:

.. toctree::
   :maxdepth: 2

   usage

.. ifconfig:: includeClasses

    CIM Classes:

    .. toctree::
       :maxdepth: 1

       mof/tree
       mof/index
