.. _openlmi-sssd-provider:

SSSD Provider
=============

.. rubric:: Overview

OpenLMI SSSD is a CIM provider for managing the `System Security Services
Daemon <https://fedorahosted.org/sssd/>`_.
It exposes remotely accessible object-oriented API using
`WBEM <http://www.openlmi.org/node/1785>`_ set of protocols and technologies.

.. rubric:: Clients

The API can be accessed by any WBEM-capable client. OpenLMI already provides:

* Python module :ref:`lmi.scripts.sssd <openlmi-scripts-sssd-python>`,
  part of :ref:`OpenLMI scripts <openlmi-scripts-python>`.

* Command line tool: :ref:`LMI metacommand <lmi_metacommand>`, with
  :ref:`'sssd' <openlmi-scripts-sssd-cmd>` subcommand.

.. rubric:: Features

* Query for current SSSD configuration.
* Enable and disable individual SSSD domains and services.
* Configure log levels of various SSSD components.

.. rubric:: Table of Contents

.. toctree::
   :maxdepth: 2

   introduction
   usage

