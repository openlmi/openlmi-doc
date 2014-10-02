OpenLMI
=======

**OpenLMI  = Open Linux Management Infrastructure.**

OpenLMI is open-source project aiming to improve management of Linux systems
using WBEM standards. We reuse many already available open-source WBEM
components, adding the missing ones and integrating them into one system
management solution.

In short, WBEM can be described as a *remote API for system management*.
See `WBEM overview <http://www.openlmi.org/node/1785>`_ for details.


Client components
-----------------

There are many already existing tools and libraries to manage WBEM-enabled
hosts. see `WBEM overview <http://www.openlmi.org/node/1785>`_ for details.

OpenLMI project adds LMI metacommand and LMIShell.

LMI metacommand
^^^^^^^^^^^^^^^
A command line utility to perform discovery and operations on remote managed
systems. For example, it can start a printing service on remote system:

::

    /usr/bin/lmi -h my.server.org service start cups

LMI metacommand users do not need to know anything about WBEM, all the complexity
is hidden inside. See :ref:`LMI metacommand documentation <lmi_metacommand>` for
details.

LMIShell
^^^^^^^^

A high-level python-based WBEM client, that can be used for scripting or as an
interactive shell to manage remote systems. For example, one can write a script
to start a service:

::

    c = connect("my.server.org", "root", "opensesame")
    cups = c.root.cimv2.LMI_Service.first_instance({"Name" : "cups.service"})
    cups.StartService()

LMIShell users do not need to know anything about WBEM transport protocols,
however some knowledge about the aforementioned remote API becomes necessary.
In the example above, the script author must know that system services are
exposed as instances of :ref:`LMI_Service<LMI-Service>` class with property
Name (the service name) and method StartService() that starts the service.

See :ref:`LMIShell <lmi_shell>` documentation for details.

Server components
-----------------

OpenLMI focuses on implementation of missing providers for networking, storage,
system services, packages and so on.
See :ref:`full list <lmi_server_components>` for details.

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2

   openlmi-tools/index
   server
