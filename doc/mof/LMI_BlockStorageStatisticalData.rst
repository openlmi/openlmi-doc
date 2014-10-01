.. _LMI-BlockStorageStatisticalData:

LMI_BlockStorageStatisticalData
-------------------------------

Class reference
===============
Subclass of :ref:`CIM_BlockStorageStatisticalData <CIM-BlockStorageStatisticalData>`

A subclass of StatisticalData which identifies individual statistics for an element of a block storage system. This class defines the metrics that MAY be kept for managed elements of the system.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-BlockStorageStatisticalData-StartStatisticTime:

``datetime`` **StartStatisticTime**

    The time, relative to managed element where the statistic was collected, when the first measurement was taken. If the statistic is reset, the StartStatisticTime is the time when the reset was performed.

    
.. _LMI-BlockStorageStatisticalData-IdleTimeCounter:

``uint64`` **IdleTimeCounter**

    The cumulative elapsed idle time using ClockTickInterval units (Cumulative Number of Time Units for all idle time in the array).

    
.. _LMI-BlockStorageStatisticalData-KBytesRead:

``uint64`` **KBytesRead**

    The cumulative count of data read in Kbytes (1024bytes = 1KByte).

    
.. _LMI-BlockStorageStatisticalData-ElementName:

``string`` **ElementName**

    The user friendly name for this instance of StatisticalData. In addition, the user friendly name can be used as a index property for a search of query. (Note: Name does not have to be unique within a namespace.)

    
.. _LMI-BlockStorageStatisticalData-TotalIOs:

``uint64`` **TotalIOs**

    The cumulative count of I/Os for the object.

    
.. _LMI-BlockStorageStatisticalData-KBytesTransferred:

``uint64`` **KBytesTransferred**

    The cumulative count of data transferred in Kbytes (1024bytes = 1KByte).

    
.. _LMI-BlockStorageStatisticalData-ReadIOs:

``uint64`` **ReadIOs**

    The cumulative count of all reads.

    
.. _LMI-BlockStorageStatisticalData-StatisticTime:

``datetime`` **StatisticTime**

    The time the most recent measurement was taken, relative to the managed element where the statistic was collected.

    
.. _LMI-BlockStorageStatisticalData-ElementType:

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
    
.. _LMI-BlockStorageStatisticalData-KBytesWritten:

``uint64`` **KBytesWritten**

    The cumulative count of data written in Kbytes (1024bytes = 1KByte).

    
.. _LMI-BlockStorageStatisticalData-IOTimeCounter:

``uint64`` **IOTimeCounter**

    The cumulative elapsed I/O time (number of Clock Tick Intervals) for all I/Os as defined in 'Total I/Os'. I/O response time is added to this counter at the completion of each measured I/O using ClockTickInterval units. This value can be divided by number of IOs to obtain an average response time.

    
.. _LMI-BlockStorageStatisticalData-SampleInterval:

``datetime`` **SampleInterval**

    Some statistics are sampled at consistent time intervals. This property provides the sample interval so that client applications can determine the minimum time that new statistics should be pulled. If the statistics are not sampled at consistent time intervals, this property must be set to a zero time interval.

    
.. _LMI-BlockStorageStatisticalData-WriteIOs:

``uint64`` **WriteIOs**

    The cumulative count of all writes.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`InstanceID <CIM-StatisticalData-InstanceID>`
| ``uint64`` :ref:`WriteHitIOTimeCounter <CIM-BlockStorageStatisticalData-WriteHitIOTimeCounter>`
| ``uint64`` :ref:`ReadHitIOTimeCounter <CIM-BlockStorageStatisticalData-ReadHitIOTimeCounter>`
| ``uint64`` :ref:`ReadIOTimeCounter <CIM-BlockStorageStatisticalData-ReadIOTimeCounter>`
| ``uint64`` :ref:`MaintTimeCounter <CIM-BlockStorageStatisticalData-MaintTimeCounter>`
| ``uint64`` :ref:`ReadHitIOs <CIM-BlockStorageStatisticalData-ReadHitIOs>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint64`` :ref:`WriteIOTimeCounter <CIM-BlockStorageStatisticalData-WriteIOTimeCounter>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint64`` :ref:`MaintOp <CIM-BlockStorageStatisticalData-MaintOp>`
| ``uint64`` :ref:`WriteHitIOs <CIM-BlockStorageStatisticalData-WriteHitIOs>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`ResetSelectedStats <CIM-StatisticalData-ResetSelectedStats>`

