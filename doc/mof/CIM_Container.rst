.. _CIM-Container:

CIM_Container
-------------

Class reference
===============
Subclass of :ref:`CIM_Component <CIM-Component>`

The Container association represents the relationship between a contained and a containing PhysicalElement. A containing object must be a PhysicalPackage.


Key properties
^^^^^^^^^^^^^^

| :ref:`GroupComponent <CIM-AbstractComponent-GroupComponent>`
| :ref:`PartComponent <CIM-AbstractComponent-PartComponent>`
| :ref:`GroupComponent <CIM-AbstractComponent-GroupComponent>`
| :ref:`PartComponent <CIM-AbstractComponent-PartComponent>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-Container-GroupComponent:

:ref:`CIM_PhysicalPackage <CIM-PhysicalPackage>` **GroupComponent**

    The PhysicalPackage that contains other PhysicalElements, including other Packages.

    
.. _CIM-Container-PartComponent:

:ref:`CIM_PhysicalElement <CIM-PhysicalElement>` **PartComponent**

    The PhysicalElement which is contained in the Package.

    
.. _CIM-Container-LocationWithinContainer:

``string`` **LocationWithinContainer**

    A free-form string representing the positioning of the PhysicalElement within the PhysicalPackage. Information relative to stationary elements in the Container (for example, 'second drive bay from the top'), angles, altitudes and other data may be recorded in this property. This string could supplement or be used in place of instantiating the CIM_Location object.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

