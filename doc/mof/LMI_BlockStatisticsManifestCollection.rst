.. _LMI-BlockStatisticsManifestCollection:

LMI_BlockStatisticsManifestCollection
-------------------------------------

Class reference
===============
Subclass of :ref:`CIM_BlockStatisticsManifestCollection <CIM-BlockStatisticsManifestCollection>`

The BlockStatisticsManifestCollection class aggregates, via MemberOfCollection, a set of BlockStatisticsManifests. This collection is associated via AssociatedBlockStatisticsManifestCollection to exactly one StatisticsCollection. The BlockStatisticsManifestCollection is used to filter the retrieval of statistics. For example, a BlockStatisticsManifestCollection is specified as part of the StatisticsService.GetStatisticsCollection method to filter the statistics returned by that method.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-SystemSpecificCollection-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-BlockStatisticsManifestCollection-ElementName:

``string`` **ElementName**

    A user-friendly name for the BlockStatisticsManifestCollection. It can be set through the ElementName parameter of the StatisticsService.CreateManifestCollection method.

    
.. _LMI-BlockStatisticsManifestCollection-IsDefault:

``boolean`` **IsDefault**

    Denotes whether or not this BlockStatisticsManifestCollection is a provider defined default BlockStatisticsManifestCollection.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`InstanceID <CIM-SystemSpecificCollection-InstanceID>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

