.. _LMI-DiskDriveElementSoftwareIdentity:

LMI_DiskDriveElementSoftwareIdentity
------------------------------------

Class reference
===============
Subclass of :ref:`CIM_ElementSoftwareIdentity <CIM-ElementSoftwareIdentity>`

ElementSoftwareIdentity allows a Managed Element to report its software related asset information (firmware, drivers, configuration software, and etc.)


Key properties
^^^^^^^^^^^^^^

| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-DiskDriveElementSoftwareIdentity-Dependent:

:ref:`LMI_DiskDrive <LMI-DiskDrive>` **Dependent**

    The ManagedElement that requires or uses the software.

    
.. _LMI-DiskDriveElementSoftwareIdentity-Antecedent:

:ref:`LMI_DiskDriveSoftwareIdentity <LMI-DiskDriveSoftwareIdentity>` **Antecedent**

    A LogicalElement's Software Asset.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`UpgradeCondition <CIM-ElementSoftwareIdentity-UpgradeCondition>`
| ``uint16[]`` :ref:`ElementSoftwareStatus <CIM-ElementSoftwareIdentity-ElementSoftwareStatus>`
| ``string`` :ref:`OtherUpgradeCondition <CIM-ElementSoftwareIdentity-OtherUpgradeCondition>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

