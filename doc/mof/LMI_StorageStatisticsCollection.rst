.. _LMI-StorageStatisticsCollection:

LMI_StorageStatisticsCollection
-------------------------------

Class reference
===============
Subclass of :ref:`CIM_StatisticsCollection <CIM-StatisticsCollection>`

A subclass of SystemSpecificCollection which collects together statistics for a system. This class forms an 'anchor point' from which all the statistics kept for the system can be found (via the MemberOfCollection associations).


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-SystemSpecificCollection-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-StorageStatisticsCollection-SampleInterval:

``datetime`` **SampleInterval**

    This property provides the minimum sampling interval for the associated statistics so that client applications can determine the minimum interval that the StatisticsCollection should be sampled. If the statistics are sampled at different cycles, this property MUST be set to a zero time interval.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``datetime`` :ref:`TimeLastSampled <CIM-StatisticsCollection-TimeLastSampled>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`InstanceID <CIM-SystemSpecificCollection-InstanceID>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

