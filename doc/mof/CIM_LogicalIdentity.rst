.. _CIM-LogicalIdentity:

CIM_LogicalIdentity
-------------------

Class reference
===============
CIM_LogicalIdentity is an abstract and generic association, indicating that two ManagedElements represent different aspects of the same underlying entity. This relationship conveys what could be defined with multiple inheritance. In most scenarios, the Identity relationship is determined by the equivalence of Keys or some other identifying properties of the related Elements. 



This relationship is reasonable in several scenarios. For example, it could be used to represent that a LogicalDevice is both a 'bus' entity and a 'functional' entity. A Device could be both a USB (bus) and a Keyboard (functional) entity.


Key properties
^^^^^^^^^^^^^^

| :ref:`SameElement <CIM-LogicalIdentity-SameElement>`
| :ref:`SystemElement <CIM-LogicalIdentity-SystemElement>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-LogicalIdentity-SameElement:

:ref:`CIM_ManagedElement <CIM-ManagedElement>` **SameElement**

    SameElement represents an alternate aspect of the ManagedElement.

    
.. _CIM-LogicalIdentity-SystemElement:

:ref:`CIM_ManagedElement <CIM-ManagedElement>` **SystemElement**

    SystemElement represents one aspect of the Managed Element. The use of 'System' in the role name does not limit the scope of the association. The role name was defined in the original association, where the referenced elements were limited to LogicalElements. Since that time, it has been found valuable to instantiate these types of relationships for ManagedElements, such as Collections. So, the referenced elements of the association were redefined to be ManagedElements. Unfortunately, the role name could not be changed without deprecating the entire association. This was not deemed necessary just to correct the role name.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

