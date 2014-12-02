Provider Registration
=====================

Each CMPI provider needs to be registered within the Object Manager (CIMOM) so
the CIMOM can expose the classes implemented by the provider and delegate the
client requested operations properly. This process is not covered by the DMTF
standards and is being implemented by each CIMOM in a different proprietary
way.

The OpenLMI project offers a special ``openlmi-mof-register`` script that
enables the provider registration in a CIMOM-agnostic way and tries to overcome
some of the other difficulties of the process. The script was designed for
troubleshooting purposes and for distribution packagers. It is not meant to be
used directly for the provider (de)registration under normal circumstances.

.. note::

    System administrators normaly do not need to use ``openlmi-mof-register``
    tool when using OpenLMI providers installed from Linux distribution
    packages, such as Fedora RPM. The packaging system should already register
    the providers automatically (using ``openlmi-mof-register`` internally).

    ``openlmi-mof-register`` is still avalaible there to either manually diagnose
    and fix problems in provider registration and for package maintainers to
    register/unregister providers on package installation/removal.

Using the registration script
-----------------------------
The script provides a usage help when run with the ``--help`` option.

Basic operations
^^^^^^^^^^^^^^^^

Every provider is accompanied with one or more MOF files and optionally a
REG file. The registration process is slightly different for each case.

Registration with the REG file requires also manual specification of the
provider version:

.. code-block:: bash

    openlmi-mof-register register -v 1.0.0  MyMofFile1.mof MyMofFile2.mof MyRegFile.reg

In the case there is no REG file:

.. code-block:: bash

    openlmi-mof-register register --just-mofs  MyMofFile1.mof MyMofFile2.mof

These commands register the provider implemented classes in the ``root/cimv2``
namespace by default. The namespace can be overriden using the ``-n`` option if
needed. It is possible to force registration for only one particular CIMOM using
the ``-c`` option. So, for example to register a provider only in the Pegasus'
``/root/interop`` namespace:

.. code-block:: bash

    openlmi-mof-register register -n "root/interop" -c pegasus --just-mofs  MyMofFile1.mof MyMofFile2.mof

To unregister the provider, run:

.. code-block:: bash

    openlmi-mof-register unregister MyMofFile.mof MyMofFile2.mof MyRegFile.reg

Again, to unregister just from one CIMOM, use the ``-c`` option.

To view the known registrations:

.. code-block:: bash

    openlmi-mof-register list

Re-registration
^^^^^^^^^^^^^^^

The script stores the registration data in a  special database in
``/var/lib/openlmi-registration/redb.sqlite`` and backs up the provided
MOF and REG files. The purpose of this arrangement is to allow installation of
the providers independent of the CIMOM installation. The script should be able
to detect presence of SFCB and/or OpenPegasus CIMOM and re-do the registrations
simply by running:

.. code-block:: bash

    openlmi-mof-register re-register
