.. _CIM-SystemDevice:

CIM_SystemDevice
----------------

Class reference
===============
Subclass of :ref:`CIM_SystemComponent <CIM-SystemComponent>`

LogicalDevices can be aggregated by a System. This relationship is made explicit by the SystemDevice association.


Key properties
^^^^^^^^^^^^^^

| :ref:`GroupComponent <CIM-AbstractComponent-GroupComponent>`
| :ref:`PartComponent <CIM-AbstractComponent-PartComponent>`
| :ref:`GroupComponent <CIM-AbstractComponent-GroupComponent>`
| :ref:`PartComponent <CIM-AbstractComponent-PartComponent>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-SystemDevice-GroupComponent:

:ref:`CIM_System <CIM-System>` **GroupComponent**

    The parent system in the Association.

    
.. _CIM-SystemDevice-PartComponent:

:ref:`CIM_LogicalDevice <CIM-LogicalDevice>` **PartComponent**

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

