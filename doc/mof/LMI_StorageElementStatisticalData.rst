.. _LMI-StorageElementStatisticalData:

LMI_StorageElementStatisticalData
---------------------------------

Class reference
===============
Subclass of :ref:`CIM_ElementStatisticalData <CIM-ElementStatisticalData>`

CIM_ElementStatisticalData is an association that relates a ManagedElement to its StatisticalData. Note that the cardinality of the ManagedElement reference is Min(1), Max(1). This cardinality mandates the instantiation of the ElementStatisticalData association for the referenced instance of CIM_StatisticalData. ElementStatisticalData describes the existence requirements and context for the CIM_StatisticalData, relative to a specific ManagedElement.


Key properties
^^^^^^^^^^^^^^

| :ref:`Stats <CIM-AbstractElementStatisticalData-Stats>`
| :ref:`ManagedElement <CIM-AbstractElementStatisticalData-ManagedElement>`
| :ref:`Stats <CIM-AbstractElementStatisticalData-Stats>`
| :ref:`ManagedElement <CIM-AbstractElementStatisticalData-ManagedElement>`
| :ref:`Stats <CIM-AbstractElementStatisticalData-Stats>`
| :ref:`ManagedElement <CIM-AbstractElementStatisticalData-ManagedElement>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-StorageElementStatisticalData-Stats:

:ref:`LMI_BlockStorageStatisticalData <LMI-BlockStorageStatisticalData>` **Stats**

    The statistic information/object.

    
.. _LMI-StorageElementStatisticalData-ManagedElement:

:ref:`CIM_StorageExtent <CIM-StorageExtent>` **ManagedElement**

    The ManagedElement for which statistical or metric data is defined.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

