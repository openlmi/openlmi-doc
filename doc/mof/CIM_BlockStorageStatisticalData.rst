.. _CIM-BlockStorageStatisticalData:

CIM_BlockStorageStatisticalData
-------------------------------

Class reference
===============
Subclass of :ref:`CIM_StatisticalData <CIM-StatisticalData>`

A subclass of StatisticalData which identifies individual statistics for an element of a block storage system. This class defines the metrics that MAY be kept for managed elements of the system.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-BlockStorageStatisticalData-WriteHitIOTimeCounter:

``uint64`` **WriteHitIOTimeCounter**

    The cumulative elapsed time using ClockTickInterval units for all Write I/Os written to cache for all cumulative Write I/Os.

    
.. _CIM-BlockStorageStatisticalData-ReadHitIOTimeCounter:

``uint64`` **ReadHitIOTimeCounter**

    The cumulative elapsed time for all Read I/Os read from cache for all cumulative Read I/Os.

    
.. _CIM-BlockStorageStatisticalData-MaintTimeCounter:

``uint64`` **MaintTimeCounter**

    The cumulative elapsed disk mainenance time. Maintainance response time is added to this counter at the completion of each measured maintenance operation using ClockTickInterval units.

    
.. _CIM-BlockStorageStatisticalData-IdleTimeCounter:

``uint64`` **IdleTimeCounter**

    The cumulative elapsed idle time using ClockTickInterval units (Cumulative Number of Time Units for all idle time in the array).

    
.. _CIM-BlockStorageStatisticalData-KBytesRead:

``uint64`` **KBytesRead**

    The cumulative count of data read in Kbytes (1024bytes = 1KByte).

    
.. _CIM-BlockStorageStatisticalData-ReadHitIOs:

``uint64`` **ReadHitIOs**

    The cumulative count of all read cache hits (Reads from Cache).

    
.. _CIM-BlockStorageStatisticalData-TotalIOs:

``uint64`` **TotalIOs**

    The cumulative count of I/Os for the object.

    
.. _CIM-BlockStorageStatisticalData-KBytesTransferred:

``uint64`` **KBytesTransferred**

    The cumulative count of data transferred in Kbytes (1024bytes = 1KByte).

    
.. _CIM-BlockStorageStatisticalData-WriteIOTimeCounter:

``uint64`` **WriteIOTimeCounter**

    The cumulative elapsed time for all Write I/Os for all cumulative Writes.

    
.. _CIM-BlockStorageStatisticalData-ReadIOs:

``uint64`` **ReadIOs**

    The cumulative count of all reads.

    
.. _CIM-BlockStorageStatisticalData-ElementType:

``uint16`` **ElementType**

    Defines the role that the element played for which this statistics record was collected. If the metered element is a system or a component of a system associated to a RegisteredProfile, then that profile may provide a more specialized definition and additional usage information for this property. 

    Generally, the ElementTypes defined here have the following meaning in the context of this class: 2, "Computer System": Cumulative statistics for the storage system. In the case of a complex system with multiple component Computer Systems, these are the statistics for the top-level aggregate Computer System. 3, "Front-end Computer System": Statistics for a component computer system that communicate with systems that initiate IO requests. 4, "Peer Computer System": Statistics for a component computer system that communicates with peer storage systems e.g. to provide remote mirroring of a volume. 5, "Back-end Computer System": Statistics for a component computer system that communicates with back-end storage. 6, "Front-end Port": Statistics for a port that communicates with systems that initiate IO requests. 7, "Back-end Port": Statistics for a port that initiates IO requests to storage devices. 8, "Volume": Statistics for an exposable storage extent, such as a StorageVolume or LogicalDisk. 9, "Extent": Statistics for an intermediate storage extent, i.e. an extent that is neither a volume or a disk. 10, "Disk Drive: Statistics for a StorageExtent that is associated to a DiskDrive through the MediaPresent association. 11, "Arbitrary LUs": Statistics that derive from access to Logical Units that are NOT StorageVolumes (e.g., controller commands). 12, "Remote Replica Group": Statistics for control IOs between an array and a remote mirror across a Network. Note that statistics for the actual movement of data to the remote mirror are attributed to the targeted StorageVolume (or LogicalDisk). Note that a particular element could be associated to multiple BlockStorageStatisticalData instances if it had multiple roles. For example, a storage array could contain redundant component computer systems that communicate both with hosts on the front end and disks on the back end. Such a device could have one BlockStorageStatisticalData instance where ElementType=3 and another instance where ElementType=5.

    
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
    
.. _CIM-BlockStorageStatisticalData-KBytesWritten:

``uint64`` **KBytesWritten**

    The cumulative count of data written in Kbytes (1024bytes = 1KByte).

    
.. _CIM-BlockStorageStatisticalData-ReadIOTimeCounter:

``uint64`` **ReadIOTimeCounter**

    The cumulative elapsed time for all Read I/Os for all cumulative Read I/Os.

    
.. _CIM-BlockStorageStatisticalData-IOTimeCounter:

``uint64`` **IOTimeCounter**

    The cumulative elapsed I/O time (number of Clock Tick Intervals) for all I/Os as defined in 'Total I/Os'. I/O response time is added to this counter at the completion of each measured I/O using ClockTickInterval units. This value can be divided by number of IOs to obtain an average response time.

    
.. _CIM-BlockStorageStatisticalData-MaintOp:

``uint64`` **MaintOp**

    The cumulative count of all disk maintenance operations (SCSI commands such as: Verify, skip-mask, XOR read, XOR write-read, etc).This is needed to understand the load on the disks that may interfere with normal read and write operations.

    
.. _CIM-BlockStorageStatisticalData-WriteHitIOs:

``uint64`` **WriteHitIOs**

    The cumulative count of Write Cache Hits (Writes that went directly to Cache).

    
.. _CIM-BlockStorageStatisticalData-WriteIOs:

``uint64`` **WriteIOs**

    The cumulative count of all writes.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``datetime`` :ref:`StartStatisticTime <CIM-StatisticalData-StartStatisticTime>`
| ``string`` :ref:`InstanceID <CIM-StatisticalData-InstanceID>`
| ``string`` :ref:`ElementName <CIM-StatisticalData-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``datetime`` :ref:`StatisticTime <CIM-StatisticalData-StatisticTime>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``datetime`` :ref:`SampleInterval <CIM-StatisticalData-SampleInterval>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`ResetSelectedStats <CIM-StatisticalData-ResetSelectedStats>`

