.. _CIM-BlockStatisticsManifest:

CIM_BlockStatisticsManifest
---------------------------

Class reference
===============
Subclass of :ref:`CIM_ManagedElement <CIM-ManagedElement>`

Instances of this class define a list of supported or desired properties of BlockStatisticalData instances. In the case where a BlockStatisticsManifest instance is a member of a BlockStatisticsManifestCollection used in a BlockStatisticsService.GetStatisticsCollection request, for each of the boolean "include" properties set to true in that BlockStatisticsManifest, the corresponding BlockStatisticalData property will be included, if available, in the statistics returned for BlockStatisticalData instances whose ElementType matches the ElementType of the BlockStatisticsManifest.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-BlockStatisticsManifest-IncludeIOTimeCounter:

``boolean`` **IncludeIOTimeCounter**

    Whether to include in a filter for a metered element the cumulative elapsed I/O time (number of Clock Tick Intervals) for all I/Os for that element as defined in 'Total I/Os'.

    
.. _CIM-BlockStatisticsManifest-IncludeIdleTimeCounter:

``boolean`` **IncludeIdleTimeCounter**

    Whether to include in a filter for a metered element the cumulative elapsed idle time for that element.

    
.. _CIM-BlockStatisticsManifest-InstanceID:

``string`` **InstanceID**

    Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon (:), and where <OrgID> must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness, <OrgID> must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance. 

    For DMTF-defined instances, the "preferred" algorithm must be used with the <OrgID> set to CIM.

    
.. _CIM-BlockStatisticsManifest-IncludeReadIOTimeCounter:

``boolean`` **IncludeReadIOTimeCounter**

    Whether to include in a filter for a metered element the cumulative elapsed time for all cumulative Read I/Os for that element.

    
.. _CIM-BlockStatisticsManifest-IncludeKBytesWritten:

``boolean`` **IncludeKBytesWritten**

    Whether to include in a filter for a metered element the cumulative count of data written in Kbytes for that element.

    
.. _CIM-BlockStatisticsManifest-IncludeReadIOs:

``boolean`` **IncludeReadIOs**

    Whether to include in a filter for a metered element the cumulative count of all reads for that element.

    
.. _CIM-BlockStatisticsManifest-IncludeMaintTimeCounter:

``boolean`` **IncludeMaintTimeCounter**

    Whether to include in a filter for a metered element the cumulative elapsed maintenance time for that element.

    
.. _CIM-BlockStatisticsManifest-IncludeStartStatisticTime:

``boolean`` **IncludeStartStatisticTime**

    Indicates whether or not the Statistics property of StatisticsService.GetStatisticsCollection method will include the time at time when statistics for this BlockStatisticsManifest were first captured.

    
.. _CIM-BlockStatisticsManifest-IncludeWriteHitIOs:

``boolean`` **IncludeWriteHitIOs**

    Whether to include in a filter for a metered element the cumulative count of Write Cache Hits (Writes that went directly to Cache) for that element.

    
.. _CIM-BlockStatisticsManifest-IncludeTotalIOs:

``boolean`` **IncludeTotalIOs**

    Whether to include in a filter for a metered element the cumulative count of I/Os for that element.

    
.. _CIM-BlockStatisticsManifest-IncludeMaintOp:

``boolean`` **IncludeMaintOp**

    Whether to include in a filter for a metered element the cumulative count of all maintenance operations for that element.

    
.. _CIM-BlockStatisticsManifest-IncludeWriteIOTimeCounter:

``boolean`` **IncludeWriteIOTimeCounter**

    Whether to include in a filter for a metered element the cumulative elapsed time for all Write I/Os for that element.

    
.. _CIM-BlockStatisticsManifest-IncludeStatisticTime:

``boolean`` **IncludeStatisticTime**

    Indicates whether or not the Statistics property of StatisticsService.GetStatisticsCollection method will include the time when statistics for this BlockStatisticsManifest were last captured.

    
.. _CIM-BlockStatisticsManifest-IncludeKBytesTransferred:

``boolean`` **IncludeKBytesTransferred**

    Whether to include in a filter for a metered element the cumulative count of data transferred in Kbytes for that element.

    
.. _CIM-BlockStatisticsManifest-ElementType:

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
    
.. _CIM-BlockStatisticsManifest-IncludeWriteIOs:

``boolean`` **IncludeWriteIOs**

    Whether to include in a filter for a metered element the cumulative count of all writes for tat element.

    
.. _CIM-BlockStatisticsManifest-IncludeReadHitIOTimeCounter:

``boolean`` **IncludeReadHitIOTimeCounter**

    Whether to include in a filter for a metered element the cumulative elapsed time for all Read I/Os read from cache for that element.

    
.. _CIM-BlockStatisticsManifest-IncludeWriteHitIOTimeCounter:

``boolean`` **IncludeWriteHitIOTimeCounter**

    Whether to include in a filter for a metered element the cumulative elapsed time for all Write I/Os written to cache for that element.

    
.. _CIM-BlockStatisticsManifest-IncludeKBytesRead:

``boolean`` **IncludeKBytesRead**

    Whether to include in a filter for a metered element the cumulative count of data read in Kbytes for that element.

    
.. _CIM-BlockStatisticsManifest-IncludeReadHitIOs:

``boolean`` **IncludeReadHitIOs**

    Whether to include in a filter for a metered element the cumulative count of all read cache hits (Reads from Cache) for that element.

    
.. _CIM-BlockStatisticsManifest-CSVSequence:

``string[]`` **CSVSequence**

    The sequence of BlockStorageStatisticalData property names for properties that will be returned are encoded in the CSVSequence array. Properties that are not included will not be returned with GetStatisticsCollection. Properties that are included in CSVSequence will be returned in the order they appear in CSVSequence.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

