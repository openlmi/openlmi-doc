.. _LMI-PCIControlledBy:

LMI_PCIControlledBy
-------------------

Class reference
===============
Subclass of :ref:`CIM_ControlledBy <CIM-ControlledBy>`

The ControlledBy relationship indicates which Devices are controlled by a CIM_Controller.


Key properties
^^^^^^^^^^^^^^

| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-PCIControlledBy-Antecedent:

:ref:`CIM_PCIDevice <CIM-PCIDevice>` **Antecedent**

    The Controller.

    
.. _LMI-PCIControlledBy-Dependent:

:ref:`LMI_PCIPort <LMI-PCIPort>` **Dependent**

    The controlled Device.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint32`` :ref:`NumberOfSoftResets <CIM-ControlledBy-NumberOfSoftResets>`
| ``uint32`` :ref:`NegotiatedDataWidth <CIM-DeviceConnection-NegotiatedDataWidth>`
| ``uint16`` :ref:`AccessMode <CIM-ControlledBy-AccessMode>`
| ``uint16`` :ref:`AccessPriority <CIM-ControlledBy-AccessPriority>`
| ``string`` :ref:`DeviceNumber <CIM-ControlledBy-DeviceNumber>`
| ``datetime`` :ref:`TimeOfDeviceReset <CIM-ControlledBy-TimeOfDeviceReset>`
| ``uint32`` :ref:`NumberOfHardResets <CIM-ControlledBy-NumberOfHardResets>`
| ``uint16`` :ref:`AccessState <CIM-ControlledBy-AccessState>`
| ``uint64`` :ref:`NegotiatedSpeed <CIM-DeviceConnection-NegotiatedSpeed>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

