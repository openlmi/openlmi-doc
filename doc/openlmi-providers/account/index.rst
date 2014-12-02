.. _openlmi-account-provider:

Account Provider
================

.. rubric:: Overview

OpenLMI-Account is CIM provider which manages POSIX accounts.
It exposes remotely accessible object-oriented API using
`WBEM <http://www.openlmi.org/node/1785>`_ set of protocols and technologies.
The provider implements DMTF identity profile, for more details read
:ref:`DMTF profile <account-dmtf-profile>`.

The provider manages only users and groups listed in ``/etc/passwd`` and
``/etc/groups`` files. It uses
`libuser <https://fedorahosted.org/libuser/>`_ library to access these files.

.. rubric:: Clients

The API can be accessed by any WBEM-capable client. OpenLMI already provides:

* Python module :ref:`lmi.scripts.account <openlmi-scripts-account-python>`,
  part of :ref:`OpenLMI scripts <openlmi-scripts-python>`.

* Command line tool: :ref:`LMI metacommand <lmi_metacommand>`, with
  :ref:`'user' and 'group' <openlmi-scripts-account-cmd>` subcommands.

.. rubric:: Features

* Create, modify or remove user and/or group.
* List users in a group and modify group membership.
* Event based monitoring of users and groups (emit indication event when an
  user or group is created or removed).

.. rubric:: Examples

For examples how to use OpenLMI-Account provider remotely
from :ref:`LMIShell <lmi_shell>`, see the :ref:`usage <account-usage>`.

.. rubric:: Table of Contents

.. toctree::
   :maxdepth: 2

   dmtf-profile
   usage
