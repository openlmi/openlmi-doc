.. _CIM-NetworkPortStatistics:

CIM_NetworkPortStatistics
-------------------------

Class reference
===============
Subclass of :ref:`CIM_StatisticalData <CIM-StatisticalData>`

The NetworkPortStatistics class describes the statistics for the NetworkPort.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-NetworkPortStatistics-BytesReceived:

``uint64`` **BytesReceived**

    The total number of bytes that are received, including framing characters.

    
.. _CIM-NetworkPortStatistics-PacketsReceived:

``uint64`` **PacketsReceived**

    The total number of packets that are received.

    
.. _CIM-NetworkPortStatistics-BytesTransmitted:

``uint64`` **BytesTransmitted**

    The total number of bytes that are transmitted, including framing characters.

    
.. _CIM-NetworkPortStatistics-PacketsTransmitted:

``uint64`` **PacketsTransmitted**

    The total number of packets that are transmitted.

    

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

