.. _openlmi-networking-provider:

Networking Provider
===================

.. rubric:: Overview

OpenLMI-Networking is CIM provider which manages local network devices.
It exposes remotely accessible object-oriented API using
`WBEM <http://www.openlmi.org/node/1785>`_ set of protocols and technologies.

.. rubric:: Clients

The API can be accessed by any WBEM-capable client. OpenLMI already provides:

* Python module :ref:`lmi.scripts.networking <openlmi-scripts-networking-python>`,
  part of
  :ref:`OpenLMI scripts <openlmi-scripts-python>`.

* Command line tool: :ref:`LMI metacommand <lmi_metacommand>`, with
  :ref:`'networking' <openlmi-scripts-networking-cmd>` subcommand.

.. rubric:: Features

* Enumerate all network devices
* Display current network IP configuration
* Manage available settings
* Settings activation/deactivation
* Support for bridging and bonding

The provider is based on concept of ``settings`` -- a network profile that
can be applied to the network device(s).

.. rubric:: Examples

For examples how to use OpenLMI-Networking provider remotely
from :ref:`LMIShell <lmi_shell>`_,
see :ref:`usage of OpenLMI-Networking <network-usage>`.

.. rubric:: Documentation

This provider is based on following `DMTF <http://dmtf.org>`_ standards:

* `DSP1116 - IP Configuration Profile <http://dmtf.org/sites/default/files/standards/documents/DSP1116_1.0.0.pdf>`_
* `DSP1035 - Host LAN Network Port Profile <http://dmtf.org/sites/default/files/standards/documents/DSP1035_1.0.2.pdf>`_

The knowledge of these standards is not necessary, but it can help a lot.

Application developers and/or sysadmins should skip the DMTF standards
and start at :ref:`Networking API concepts <network-concepts>`.

.. rubric:: Table of contents

.. toctree::
   :maxdepth: 2

   concepts
   usage

.. ifconfig:: includeClasses

   OpenLMI Networking CIM classes:

   .. toctree::
      :maxdepth: 2

      classes
