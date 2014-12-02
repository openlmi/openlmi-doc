.. _openlmi-selinux-provider:

SELinux Provider
================

.. rubric:: Overview

OpenLMI-SELinux is CIM provider which provides a way to read and set SELinux
values, such as booleans, ports, or file labels.
It exposes remotely accessible object-oriented API using
`WBEM <http://www.openlmi.org/node/1785>`_ set of protocols and technologies.

The provider does not implement any DMTF standard profile.

.. rubric:: Clients

The API can be accessed by any WBEM-capable client. OpenLMI does not provide
any specialized client yet.

.. rubric:: Features

* Query information about current SELinux policy (version, type, port labels ...)
* Read and modify overall SELinux state (Enforcing/Permissive).
* Check and modify file contexts.

.. rubric:: Examples

There is number of examples in the :ref:`Usage <selinux-usage>` chapter.

.. rubric:: Table of Contents

Contents:

.. toctree::
   :maxdepth: 2

   introduction
   usage
