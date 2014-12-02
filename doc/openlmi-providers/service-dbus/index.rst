.. _openlmi-service-provider:

Service Provider
================

.. rubric:: Overview

OpenLMI-Service is CIM provider for managing Linux system services (using the
`systemd D-Bus interface <http://www.freedesktop.org/wiki/Software/systemd/dbus/>`_).

.. rubric:: Clients

The API can be accessed by any WBEM-capable client. OpenLMI already provides:

* Python module :ref:`lmi.scripts.service <openlmi-scripts-service-python>`,
  part of
  :ref:`OpenLMI scripts <openlmi-scripts-python>`.

* Command line tool: :ref:`LMI metacommand <lmi_metacommand>`, with
  :ref:`'service' <openlmi-scripts-service-cmd>` subcommand.

.. rubric:: Features

* Enumerate system services and get their status.
* Start/stop/restart/... a service and enable/disable a service.
* Event based monitoring of service status (emit indication event upon service property change).

.. rubric:: Examples

For examples how to use OpenLMI-Service provider remotely
from :ref:`LMIShell <lmi_shell>`, see the :ref:`usage <service-usage>`.

.. rubric:: Table of Contents

.. toctree::
   :maxdepth: 2

   usage
