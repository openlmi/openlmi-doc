.. _CIM-MediaPresent:

CIM_MediaPresent
----------------

Class reference
===============
Subclass of :ref:`CIM_Dependency <CIM-Dependency>`

Where a StorageExtent must be accessed through a MediaAccess Device, this relationship is described by the MediaPresent association.


Key properties
^^^^^^^^^^^^^^

| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-MediaPresent-Dependent:

:ref:`CIM_StorageExtent <CIM-StorageExtent>` **Dependent**

    The StorageExtent accessed using the MediaAccessDevice.

    
.. _CIM-MediaPresent-Antecedent:

:ref:`CIM_MediaAccessDevice <CIM-MediaAccessDevice>` **Antecedent**

    The MediaAccessDevice.

    
.. _CIM-MediaPresent-FixedMedia:

``boolean`` **FixedMedia**

    Boolean indicating that the accessed StorageExtent is fixed in the MediaAccessDevice and can not be ejected.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

