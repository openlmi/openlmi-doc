.. _openlmi-fan-provider:

Fan Provider
============

.. rubric:: Overview

OpenLMI-Fan is CIM provider for managing hardware fans. It does so by using
`lm_sensors <http://www.lm-sensors.org/>`_ library.
It exposes remotely accessible object-oriented API using
`WBEM <http://www.openlmi.org/node/1785>`_ set of protocols and technologies.
The provider implements DMTF fan profile, for more details read
:ref:`DMTF profile <fan-dmtf-profile>`.

The provider does not expose much functionality and as such can serve as a
short example how to implement a CIM provider.

.. rubric:: Clients

The API can be accessed by any WBEM-capable client. OpenLMI does not provide
any specialized client, the best is to use :ref:`LMIShell <lmi_shell>`.

.. rubric:: Features

* Enumerate system fans and query their speed.

.. rubric:: Table of Contents

.. toctree::
    :maxdepth: 2

    dmtf
    usage
