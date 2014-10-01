.. _LMI-BaseboardContainer:

LMI_BaseboardContainer
----------------------

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

.. _LMI-BaseboardContainer-GroupComponent:

:ref:`LMI_Chassis <LMI-Chassis>` **GroupComponent**

    The PhysicalPackage that contains other PhysicalElements, including other Packages.

    
.. _LMI-BaseboardContainer-PartComponent:

:ref:`LMI_Baseboard <LMI-Baseboard>` **PartComponent**

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

