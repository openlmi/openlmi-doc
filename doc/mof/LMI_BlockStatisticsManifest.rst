.. _LMI-BlockStatisticsManifest:

LMI_BlockStatisticsManifest
---------------------------

Class reference
===============
Subclass of :ref:`CIM_BlockStatisticsManifest <CIM-BlockStatisticsManifest>`

Instances of this class define a list of supported or desired properties of BlockStatisticalData instances. In the case where a BlockStatisticsManifest instance is a member of a BlockStatisticsManifestCollection used in a BlockStatisticsService.GetStatisticsCollection request, for each of the boolean "include" properties set to true in that BlockStatisticsManifest, the corresponding BlockStatisticalData property will be included, if available, in the statistics returned for BlockStatisticalData instances whose ElementType matches the ElementType of the BlockStatisticsManifest.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-BlockStatisticsManifest-IncludeIOTimeCounter:

``boolean`` **IncludeIOTimeCounter**

    Whether to include in a filter for a metered element the cumulative elapsed I/O time (number of Clock Tick Intervals) for all I/Os for that element as defined in 'Total I/Os'.

    
.. _LMI-BlockStatisticsManifest-IncludeIdleTimeCounter:

``boolean`` **IncludeIdleTimeCounter**

    Whether to include in a filter for a metered element the cumulative elapsed idle time for that element.

    
.. _LMI-BlockStatisticsManifest-IncludeReadIOTimeCounter:

``boolean`` **IncludeReadIOTimeCounter**

    Whether to include in a filter for a metered element the cumulative elapsed time for all cumulative Read I/Os for that element.

    
.. _LMI-BlockStatisticsManifest-IncludeKBytesWritten:

``boolean`` **IncludeKBytesWritten**

    Whether to include in a filter for a metered element the cumulative count of data written in Kbytes for that element.

    
.. _LMI-BlockStatisticsManifest-IncludeReadIOs:

``boolean`` **IncludeReadIOs**

    Whether to include in a filter for a metered element the cumulative count of all reads for that element.

    
.. _LMI-BlockStatisticsManifest-IncludeMaintTimeCounter:

``boolean`` **IncludeMaintTimeCounter**

    Whether to include in a filter for a metered element the cumulative elapsed maintenance time for that element.

    
.. _LMI-BlockStatisticsManifest-IncludeStartStatisticTime:

``boolean`` **IncludeStartStatisticTime**

    Indicates whether or not the Statistics property of StatisticsService.GetStatisticsCollection method will include the time at time when statistics for this BlockStatisticsManifest were first captured.

    
.. _LMI-BlockStatisticsManifest-IncludeWriteHitIOs:

``boolean`` **IncludeWriteHitIOs**

    Whether to include in a filter for a metered element the cumulative count of Write Cache Hits (Writes that went directly to Cache) for that element.

    
.. _LMI-BlockStatisticsManifest-IncludeTotalIOs:

``boolean`` **IncludeTotalIOs**

    Whether to include in a filter for a metered element the cumulative count of I/Os for that element.

    
.. _LMI-BlockStatisticsManifest-IncludeMaintOp:

``boolean`` **IncludeMaintOp**

    Whether to include in a filter for a metered element the cumulative count of all maintenance operations for that element.

    
.. _LMI-BlockStatisticsManifest-IncludeWriteIOTimeCounter:

``boolean`` **IncludeWriteIOTimeCounter**

    Whether to include in a filter for a metered element the cumulative elapsed time for all Write I/Os for that element.

    
.. _LMI-BlockStatisticsManifest-IncludeStatisticTime:

``boolean`` **IncludeStatisticTime**

    Indicates whether or not the Statistics property of StatisticsService.GetStatisticsCollection method will include the time when statistics for this BlockStatisticsManifest were last captured.

    
.. _LMI-BlockStatisticsManifest-IncludeKBytesTransferred:

``boolean`` **IncludeKBytesTransferred**

    Whether to include in a filter for a metered element the cumulative count of data transferred in Kbytes for that element.

    
.. _LMI-BlockStatisticsManifest-ElementType:

``uint16`` **ElementType**

    Determines the type of elements that this BlockStatisticsManifest can be applied to (e.g. during a GetStatisticsCollection request). This is used when the same set of statistical metrics is calculated for several types of devices. In this way, a single BlockStatisticsManifest instance can be used to filter all the StatsiticalData instances that contain metrics for the same type of element in a StatisticsCollection. If used, a subclass should override this property to specify the element types supported by that class, preferably through ValueMap and Values qualifiers to allow clients to programmatically retrieve those supported types.

    
    ======== =========================
    ValueMap Values                   
    ======== =========================
    2        Computer System          
    3        Front-end Computer System
    4        Peer Computer System     
    5        Back-end Computer System 
    6        Front-end Port           
    7        Back-end Port            
    8        Volume                   
    9        Extent                   
    10       Disk Drive               
    11       Arbitrary LUs            
    12       Remote Replica Group     
    ..       DMTF Reserved            
    0x8000.. Vendor Specific          
    ======== =========================
    
.. _LMI-BlockStatisticsManifest-IncludeWriteIOs:

``boolean`` **IncludeWriteIOs**

    Whether to include in a filter for a metered element the cumulative count of all writes for tat element.

    
.. _LMI-BlockStatisticsManifest-IncludeReadHitIOTimeCounter:

``boolean`` **IncludeReadHitIOTimeCounter**

    Whether to include in a filter for a metered element the cumulative elapsed time for all Read I/Os read from cache for that element.

    
.. _LMI-BlockStatisticsManifest-IncludeWriteHitIOTimeCounter:

``boolean`` **IncludeWriteHitIOTimeCounter**

    Whether to include in a filter for a metered element the cumulative elapsed time for all Write I/Os written to cache for that element.

    
.. _LMI-BlockStatisticsManifest-IncludeKBytesRead:

``boolean`` **IncludeKBytesRead**

    Whether to include in a filter for a metered element the cumulative count of data read in Kbytes for that element.

    
.. _LMI-BlockStatisticsManifest-IncludeReadHitIOs:

``boolean`` **IncludeReadHitIOs**

    Whether to include in a filter for a metered element the cumulative count of all read cache hits (Reads from Cache) for that element.

    
.. _LMI-BlockStatisticsManifest-CSVSequence:

``string[]`` **CSVSequence**

    The sequence of BlockStorageStatisticalData property names for properties that will be returned are encoded in the CSVSequence array. Properties that are not included will not be returned with GetStatisticsCollection. Properties that are included in CSVSequence will be returned in the order they appear in CSVSequence.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`InstanceID <CIM-BlockStatisticsManifest-InstanceID>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

