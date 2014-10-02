.. _openlmi-networking-provider:

Networking Provider
===================

OpenLMI-Networking is CIM provider which manages local network devices.

This provider is based on following `DMTF <http://dmtf.org>`_ standards:

* `DSP1116 - IP Configuration Profile <http://dmtf.org/sites/default/files/standards/documents/DSP1116_1.0.0.pdf>`_
* `DSP1035 - Host LAN Network Port Profile <http://dmtf.org/sites/default/files/standards/documents/DSP1035_1.0.2.pdf>`_

The knowledge of these standards is not necessary, but it can help a lot.

Application developers should first get familliar with :ref:`Networking API concepts <network-concepts>`
and then look at :ref:`usage of OpenLMI-Networking <network-usage>`.

Content:

.. toctree::
   :maxdepth: 2

   concepts
   usage

.. ifconfig:: includeClasses

   OpenLMI Networking CIM classes:

   .. toctree::
      :maxdepth: 1

      mof/tree
      mof/index
