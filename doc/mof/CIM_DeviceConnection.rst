.. _CIM-DeviceConnection:

CIM_DeviceConnection
--------------------

Class reference
===============
Subclass of :ref:`CIM_Dependency <CIM-Dependency>`

The DeviceConnection relationship indicates that two or more Devices are connected together.


Key properties
^^^^^^^^^^^^^^

| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-DeviceConnection-Dependent:

:ref:`CIM_LogicalDevice <CIM-LogicalDevice>` **Dependent**

    A second LogicalDevice that is connected to the Antecedent Device.

    
.. _CIM-DeviceConnection-Antecedent:

:ref:`CIM_LogicalDevice <CIM-LogicalDevice>` **Antecedent**

    A LogicalDevice.

    
.. _CIM-DeviceConnection-NegotiatedSpeed:

``uint64`` **NegotiatedSpeed**

    When several bus and connection speeds are possible, the NegotiatedSpeed property defines the one that is in use between the Devices. Speed is specified in bits per second. If connection or bus speeds are not negotiated, or if this information is not available or not important to Device management, the property should be set to 0.

    
.. _CIM-DeviceConnection-NegotiatedDataWidth:

``uint32`` **NegotiatedDataWidth**

    When several bus and connection data widths are possible, the NegotiatedDataWidth property defines the one that is in use between the Devices. Data width is specified in bits. If data width is not negotiated, or if this information is not available or not important to Device management, the property should be set to 0.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

