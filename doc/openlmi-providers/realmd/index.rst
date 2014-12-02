.. _openlmi-realmd-provider:

Realmd Provider
===============

.. rubric:: Overview

OpenLMI-Relamd is CIM provider  for managing the systems Active Directory or
Kerberos realms membership through the Realmd system service.
It exposes remotely accessible object-oriented API using
`WBEM <http://www.openlmi.org/node/1785>`_ set of protocols and technologies.

.. rubric:: Clients

The API can be accessed by any WBEM-capable client. OpenLMI already provides:

* Python module :ref:`lmi.scripts.realmd <openlmi-scripts-realmd-python>`,
  part of :ref:`OpenLMI scripts <openlmi-scripts-python>`.

* Command line tool: :ref:`LMI metacommand <lmi_metacommand>`, with
  :ref:`'realmd' <openlmi-scripts-realmd-cmd>` subcommand.

.. rubric:: Features

* Query for a domain membership.
* Join / leave a domain.

.. rubric:: Examples

Following :ref:`LMIShell <lmi_shell>` code joins an Active Directory domain::

    c = connect("localhost", "pegasus", "test")
    realmsrv = c.root.cimv2.LMI_RealmdService.first_instance()
    realmsrv.JoinDomain(Password='ZisIzSECRET', User='admin', Domain='AD.EXAMPLE.COM')

More examples can be found in the :ref:`Usage <realmd-usage>` chapter.

.. rubric:: Table of Contents

Contents:

.. toctree::
   :maxdepth: 2

   usage
