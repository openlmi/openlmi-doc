.. _CIM-FileIdentity:

CIM_FileIdentity
----------------

Class reference
===============
Subclass of :ref:`CIM_LogicalIdentity <CIM-LogicalIdentity>`

CIM_FileIdentity indicates that a UnixFile describes Unix- specific aspects of the various subclasses of LogicalFile. The association exists since it forces UnixFile to be weak to (scoped by) the LogicalFile. This is not true in the association's superclass, LogicalIdentity.


Key properties
^^^^^^^^^^^^^^

| :ref:`SameElement <CIM-LogicalIdentity-SameElement>`
| :ref:`SystemElement <CIM-LogicalIdentity-SystemElement>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-FileIdentity-SameElement:

:ref:`CIM_UnixFile <CIM-UnixFile>` **SameElement**

    SameElement represents the additional aspects of the Unix/Linux Logical file.

    
.. _CIM-FileIdentity-SystemElement:

:ref:`CIM_LogicalFile <CIM-LogicalFile>` **SystemElement**

    The Logical File.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

