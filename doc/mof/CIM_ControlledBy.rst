.. _CIM-ControlledBy:

CIM_ControlledBy
----------------

Class reference
===============
Subclass of :ref:`CIM_DeviceConnection <CIM-DeviceConnection>`

The ControlledBy relationship indicates which Devices are controlled by a CIM_Controller.


Key properties
^^^^^^^^^^^^^^

| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-ControlledBy-Antecedent:

:ref:`CIM_Controller <CIM-Controller>` **Antecedent**

    The Controller.

    
.. _CIM-ControlledBy-NumberOfSoftResets:

``uint32`` **NumberOfSoftResets**

    Number of soft resets issued by the Controller. A soft reset does not completely clear current Device state or data. Exact semantics are dependent on the Device and on the protocols and mechanisms used to communicate with the Device.

    
.. _CIM-ControlledBy-Dependent:

:ref:`CIM_LogicalDevice <CIM-LogicalDevice>` **Dependent**

    The controlled Device.

    
.. _CIM-ControlledBy-AccessMode:

``uint16`` **AccessMode**

    This property describes the accessibility of the device through the antecedent controller.

    
    ======== =========
    ValueMap Values   
    ======== =========
    2        ReadWrite
    3        ReadOnly 
    4        NoAccess 
    ======== =========
    
.. _CIM-ControlledBy-AccessPriority:

``uint16`` **AccessPriority**

    The property describes the priority given to accesses of the device through this controller. The highest priority path will have the lowest value for this parameter.

    
.. _CIM-ControlledBy-DeviceNumber:

``string`` **DeviceNumber**

    Address of associated Device in context of the antecedent Controller.

    
.. _CIM-ControlledBy-TimeOfDeviceReset:

``datetime`` **TimeOfDeviceReset**

    The time that the downstream Device was last reset by the Controller.

    
.. _CIM-ControlledBy-NumberOfHardResets:

``uint32`` **NumberOfHardResets**

    Number of hard resets issued by the Controller. A hard reset returns the Device to its initialization or boot-up state. All internal Device state information and data are lost.

    
.. _CIM-ControlledBy-AccessState:

``uint16`` **AccessState**

    The State property indicates whether the Controller is actively commanding or accessing the Device (value=1) or not (value=2). Also, the value, "Unknown" (0), can be defined. This information is necessary when a LogicalDevice can be commanded by, or accessed through, multiple Controllers.

    
    ======== ========
    ValueMap Values  
    ======== ========
    0        Unknown 
    1        Active  
    2        Inactive
    ======== ========
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint32`` :ref:`NegotiatedDataWidth <CIM-DeviceConnection-NegotiatedDataWidth>`
| ``uint64`` :ref:`NegotiatedSpeed <CIM-DeviceConnection-NegotiatedSpeed>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

