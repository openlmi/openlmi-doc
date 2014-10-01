.. _PCP-MetricValue:

PCP_MetricValue
---------------

Class reference
===============
Subclass of :ref:`CIM_StatisticalData <CIM-StatisticalData>`

CIM_StatisticalData is a root class for any arbitrary collection of statistical data and/or metrics applicable to one or more ManagedElements. These statistics MUST represent the most recent observations and MUST NOT be provided if irrelevant or stale. Note that this class uses a simplified naming/identity algorithm as compared to CIM_StatisticalInformation.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _PCP-MetricValue-InstanceName:

``string`` **InstanceName**

    PMAPI indom instance name

    
.. _PCP-MetricValue-InstanceNumber:

``uint32`` **InstanceNumber**

    PMAPI indom instance number

    
.. _PCP-MetricValue-Units:

``string`` **Units**

    The metric units, as returned by pmUnitsStr(3)

    
.. _PCP-MetricValue-PMID:

``uint32`` **PMID**

    PCP metric PMID

    
.. _PCP-MetricValue-Type:

``string`` **Type**

    The metric type, as returned by pmTypeStr(3)

    
.. _PCP-MetricValue-ValueString:

``string`` **ValueString**

    The metric value, as rendered into string form by pmAtomStr() or pmPrintValue(3)

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`ElementName <CIM-StatisticalData-ElementName>`
| ``datetime`` :ref:`StatisticTime <CIM-StatisticalData-StatisticTime>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``datetime`` :ref:`StartStatisticTime <CIM-StatisticalData-StartStatisticTime>`
| ``string`` :ref:`InstanceID <CIM-StatisticalData-InstanceID>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``datetime`` :ref:`SampleInterval <CIM-StatisticalData-SampleInterval>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`ResetSelectedStats <CIM-StatisticalData-ResetSelectedStats>`

