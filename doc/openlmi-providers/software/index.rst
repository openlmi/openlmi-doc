.. _openlmi-software-provider:

Software Provider
=================

.. rubric:: Overview

OpenLMI-Software is a CIM provider managing software packages on a Linux machine.
It exposes remotely accessible object-oriented API using
`WBEM <http://www.openlmi.org/node/1785>`_ set of protocols and technologies.

.. rubric:: Clients

The API can be accessed by any WBEM-capable client. OpenLMI already provides:

* Python module :ref:`lmi.scripts.software <openlmi-scripts-software-python>`,
  part of
  :ref:`OpenLMI scripts <openlmi-scripts-python>`.

* Command line tool: :ref:`LMI metacommand <lmi_metacommand>`, with
  :ref:`'software' <openlmi-scripts-software-cmd>` subcommand.

.. rubric:: Features

* Enumerate installed and available packages.
* Enumerate package repositories.
* Package lookup.
* Package installation.
* Package removal.
* Package update.
* Package verification [*].
* Enable and disable repository.

Currently, above can be performed on single packages only. Dependencies are
resolved and installed when needed. However, whole system update is out of
scope of this provider as of now.

.. [*] Available only for `RPM`_ packages.

.. rubric:: Implementations

Currently there are two implementations. The first is a stable one written in
python and requiring `YUM`_, therefore it can manage just `RPM`_ packages.
Second one is written in C and uses `PackageKit`_ as a backend. It is unstable
though.

.. rubric:: Examples

There are several examples how to use OpenLMI-Software provider remotely from
:ref:`LMIShell <lmi_shell>`:

* :ref:`List installed packages <example-list-installed-packages>`.
* :ref:`List available packages <example-list-available-packages>`.
* :ref:`List package repositories <example-list-repositories>`.
* :ref:`Find packages <example-search-package>`.
* :ref:`Install a package <example-install-package>`.
* :ref:`Remove a package <example-remove-package>`.
* :ref:`Update a package <example-update-package>`.
* :ref:`Verify a package <example-verify-package>`.
* :ref:`Enable and disable repositories <example-change-repo-state>`.

Table of contents:

.. toctree::
    :maxdepth: 2

    dmtf
    concept
    configuration
    usage

.. _yum: https://fedoraproject.org/wiki/Yum
.. _RPM: http://www.rpm.org/
.. _PackageKit: http://www.freedesktop.org/software/PackageKit/

