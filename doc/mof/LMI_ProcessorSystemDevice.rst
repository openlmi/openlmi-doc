.. _LMI-ProcessorSystemDevice:

LMI_ProcessorSystemDevice
-------------------------

Class reference
===============
Subclass of :ref:`CIM_SystemDevice <CIM-SystemDevice>`

LogicalDevices can be aggregated by a System. This relationship is made explicit by the SystemDevice association.


Key properties
^^^^^^^^^^^^^^

| :ref:`GroupComponent <CIM-AbstractComponent-GroupComponent>`
| :ref:`PartComponent <CIM-AbstractComponent-PartComponent>`
| :ref:`GroupComponent <CIM-AbstractComponent-GroupComponent>`
| :ref:`PartComponent <CIM-AbstractComponent-PartComponent>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-ProcessorSystemDevice-GroupComponent:

:ref:`CIM_ComputerSystem <CIM-ComputerSystem>` **GroupComponent**

    The parent system in the Association.

    
.. _LMI-ProcessorSystemDevice-PartComponent:

:ref:`LMI_Processor <LMI-Processor>` **PartComponent**

    The LogicalDevice that is a component of a System.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

