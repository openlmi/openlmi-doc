.. _openlmi-power-provider:

Power Management
================

.. rubric:: Overview

OpenLMI-PowerManagement is CIM provider that allows to manage power states of
the managed system. It exposes remotely accessible object-oriented API using
`WBEM <http://www.openlmi.org/node/1785>`_ set of protocols and technologies.

.. rubric:: Clients

The API can be accessed by any WBEM-capable client. OpenLMI already provides:

* Python module :ref:`lmi.scripts.powermanagement <openlmi-scripts-powermanagement-python>`,
  part of
  :ref:`OpenLMI scripts <openlmi-scripts-python>`.

* Command line tool: :ref:`LMI metacommand <lmi_metacommand>`, with
  :ref:`'power' <openlmi-scripts-powermanagement-cmd>` subcommand.

.. rubric:: Features

* Soft and hard reboot of the system
* Soft and hard power off the system
* Suspend
* Hibernation

.. rubric:: Examples

For examples how to use OpenLMI-PowerManagement provider remotely
from :ref:`LMIShell <lmi_shell>`, see the :ref:`usage <power-usage>`.

.. rubric:: Documentation

This provider is based on following `DMTF <http://dmtf.org>`_ standard:

* `DSP1027 - Power State Management Profile <http://dmtf.org/sites/default/files/standards/documents/DSP1027_2.0.0.pdf>`_

The knowledge of this standard is not necessary, but it can help a lot.

.. rubric:: Table of Contents

.. toctree::
    :maxdepth: 2

    usage
