.. _LMI-InstalledSoftwareIdentity:

LMI_InstalledSoftwareIdentity
-----------------------------

Class reference
===============
Subclass of :ref:`CIM_InstalledSoftwareIdentity <CIM-InstalledSoftwareIdentity>`

The InstalledSoftwareIdentity association identifies the System on which a SoftwareIdentity is installed. This class is a corollary to InstalledSoftwareElement, but deals with the asset aspects of software (as indicated by SoftwareIdentity), versus the deployment aspects (as indicated by SoftwareElement).


Key properties
^^^^^^^^^^^^^^

| :ref:`InstalledSoftware <CIM-InstalledSoftwareIdentity-InstalledSoftware>`
| :ref:`System <CIM-InstalledSoftwareIdentity-System>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-InstalledSoftwareIdentity-InstalledSoftware:

:ref:`LMI_SoftwareIdentity <LMI-SoftwareIdentity>` **InstalledSoftware**

    The SoftwareIdentity that is installed.

    
.. _LMI-InstalledSoftwareIdentity-System:

:ref:`CIM_ComputerSystem <CIM-ComputerSystem>` **System**

    The system on which the software is installed.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

