.. _LMI-SoftwareIdentityChecks:

LMI_SoftwareIdentityChecks
--------------------------

Class reference
===============
This association ties a SoftwareIdentity to a specific Check to validate its state. Each file installed by corresponding RPM package to local file system yields one instance of this class.


Key properties
^^^^^^^^^^^^^^

| :ref:`Check <LMI-SoftwareIdentityChecks-Check>`
| :ref:`Element <LMI-SoftwareIdentityChecks-Element>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-SoftwareIdentityChecks-Check:

:ref:`LMI_SoftwareIdentityFileCheck <LMI-SoftwareIdentityFileCheck>` **Check**

    The Check for the file.

    
.. _LMI-SoftwareIdentityChecks-Element:

:ref:`LMI_SoftwareIdentity <LMI-SoftwareIdentity>` **Element**

    The SoftwareIdentity being checked.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

