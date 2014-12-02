.. _openlmi-logicalfile-provider:

LogicalFile Provider
====================

.. rubric:: Overview

OpenLMI-LogicalFile is a CIM provider which provides a way to read information
about files and directories. The provider also allows to traverse the file
hierarchy and to create and remove empty directories.

The provider implements a part of the
`CIM System schema <http://dmtf.org/standards/cim/schemas>`_ (sections "Local
File Systems" and "Unix System"). It exposes remotely accessible
object-oriented API using `WBEM <http://www.openlmi.org/node/1785>`_ set of
protocols and technologies.


.. rubric:: Clients

The API can be accessed by any WBEM-capable client. OpenLMI already provides:

* Python module :ref:`lmi.scripts.logicalfile <openlmi-scripts-logicalfile-python>`,
  part of :ref:`OpenLMI scripts <openlmi-scripts-python>`.

* Command line tool: :ref:`LMI metacommand <lmi_metacommand>`, with
  :ref:`'file' <openlmi-scripts-logicalfile-cmd>` subcommand.

.. rubric:: Features

* List files in a directory, incl. their SELinux contexts.
* Create a directory.
* Remove an empty directory.

.. note::

    Manipulation with files and directories is intentionally limited to
    creating and removing empty directories. This allows remote admins to
    to create a directory to mount a filesystem into it (using OpenLMI-Storage
    provider), while providing very little attack surface to potential
    attackers.

.. rubric:: Examples

Following :ref:`LMIShell <lmi_shell>` example prints content of the root
directory::

    c = connect("localhost", "pegasus", "mypassword")
    system = c.root.cimv2.PG_ComputerSystem.first_instance()
    root = system.first_associator(AssocClass="LMI_RootDirectory")

    # list all items in the root directory
    files = root.associators(AssocClass="LMI_DirectoryContainsFile", Role="GroupComponent")
    for file in files:
        print file.Name

More examples can be found in the :ref:`Usage <logicalfile-usage>` chapter.

.. rubric:: Table of Contents


.. toctree::
   :maxdepth: 2

   usage

   configuration
