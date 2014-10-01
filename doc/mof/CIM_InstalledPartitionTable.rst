.. _CIM-InstalledPartitionTable:

CIM_InstalledPartitionTable
---------------------------

Class reference
===============
Subclass of :ref:`CIM_Dependency <CIM-Dependency>`

This association describes the attributes of a partition table installed in an extent. The attributes are in the capabilities class.


Key properties
^^^^^^^^^^^^^^

| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-InstalledPartitionTable-Dependent:

:ref:`CIM_StorageExtent <CIM-StorageExtent>` **Dependent**

    The extent 'hosting' the partitions 

    .

    
.. _CIM-InstalledPartitionTable-Antecedent:

:ref:`CIM_DiskPartitionConfigurationCapabilities <CIM-DiskPartitionConfigurationCapabilities>` **Antecedent**

    The DiskPartitionConfigurationCapabilities describing the capabilities of partitions based on this extent.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

