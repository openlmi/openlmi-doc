.. _LMI-PhysicalMemoryContainer:

LMI_PhysicalMemoryContainer
---------------------------

Class reference
===============
Subclass of :ref:`CIM_Container <CIM-Container>`

The Container association represents the relationship between a contained and a containing PhysicalElement. A containing object must be a PhysicalPackage.


Key properties
^^^^^^^^^^^^^^

| :ref:`GroupComponent <CIM-AbstractComponent-GroupComponent>`
| :ref:`PartComponent <CIM-AbstractComponent-PartComponent>`
| :ref:`GroupComponent <CIM-AbstractComponent-GroupComponent>`
| :ref:`PartComponent <CIM-AbstractComponent-PartComponent>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-PhysicalMemoryContainer-GroupComponent:

:ref:`LMI_MemoryPhysicalPackage <LMI-MemoryPhysicalPackage>` **GroupComponent**

    The PhysicalPackage that contains other PhysicalElements, including other Packages.

    
.. _LMI-PhysicalMemoryContainer-PartComponent:

:ref:`LMI_PhysicalMemory <LMI-PhysicalMemory>` **PartComponent**

    The PhysicalElement which is contained in the Package.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`LocationWithinContainer <CIM-Container-LocationWithinContainer>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

