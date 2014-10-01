.. _CIM-StatisticsCapabilities:

CIM_StatisticsCapabilities
--------------------------

Class reference
===============
Subclass of :ref:`CIM_Capabilities <CIM-Capabilities>`

An instance of this class defines the specific support for the metered elements and methods for retrieving that statistical data from a StatisticsService.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-StatisticsCapabilities-SynchronousMethodsSupported:

``uint16[]`` **SynchronousMethodsSupported**

    The synchronous mechanisms supported for retrieving statistics and defining and modifying filters for statistics retrieval.

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    ..       DMTF Reserved  
    0x8000.. Vendor Specific
    ======== ===============
    
.. _CIM-StatisticsCapabilities-ElementTypesSupported:

``uint16[]`` **ElementTypesSupported**

    The list of element types for which statistical data is available. This property may not be meaningful if the StatisticsService these capabilities describe does not support StatisticalData instances for different types of elements.

    
.. _CIM-StatisticsCapabilities-AsynchronousMethodsSupported:

``uint16[]`` **AsynchronousMethodsSupported**

    The asychronous mechanisms supported for retrieving statistics.

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    ..       DMTF Reserved  
    0x8000.. Vendor Specific
    ======== ===============
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`ElementName <CIM-Capabilities-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`InstanceID <CIM-Capabilities-InstanceID>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`CreateGoalSettings <CIM-Capabilities-CreateGoalSettings>`

