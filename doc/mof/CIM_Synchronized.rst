.. _CIM-Synchronized:

CIM_Synchronized
----------------

Class reference
===============
Indicates that two ManagedElements were aligned or made to be equivalent at the specified point in time. If the Boolean property SyncMaintained is true, then synchronization of the Elements is preserved. Both like and unlike objects can be synchronized. For example, two WatchDog timers can be aligned, or the contents of a LogicalFile can be synchronized with the contents of a StorageExtent.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemElement <CIM-Synchronized-SystemElement>`
| :ref:`SyncedElement <CIM-Synchronized-SyncedElement>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-Synchronized-WhenActivated:

``datetime`` **WhenActivated**

    Specifies when point-in-time was taken or when the replication association is activated, reactivated, resumed or restablished. Must be set to NULL if implementation is not capable of providing this information. A value of 0 indicates the information is not known.

    
.. _CIM-Synchronized-FailedCopyStopsHostIO:

``boolean`` **FailedCopyStopsHostIO**

    If true, the storage array tells host to stop sending data to source element if copying to a remote element fails.

    
.. _CIM-Synchronized-CopyState:

``uint16`` **CopyState**

    CopyState describes the state of the association with respect to Replication activity. Values are: 

    Initialized: The link to enable replication is established and source/replica elements are associated, but the data flow has not started. 

    Unsynchronized: Not all the source element data has been copied to the target element. 

    Synchronized: For the Mirror, Snapshot, or Clone replication, the target represents a copy of the source. 

    Broken: The relationship is non-functional due to errors in the source, the target, the path between the two or space constraints. 

    Fractured: Target is split from the source. 

    Split: The target element was gracefully (or systematically) split from its source element -- consistency is guaranteed. 

    Inactive: Data flow has stopped, writes to source element will not be sent to target element. 

    Suspended: Data flow between the source and target elements has stopped. Writes to source element are held until the association is Resumed. 

    Failedover: Reads and writes to/from the target element. Source element is not reachable. 

    Prepared: Initialization is completed, the data flow has started, however, the data flow has not started. 

    Aborted: The copy operation is aborted with the Abort operation. Use the Resync Replica operation to restart the copy operation. 

    Skewed: The target has been modified and is no longer synchronized with the source element or the point-in-time view. 

    Mixed: Applies to the CopyState of GroupSynchronized. It indicates the StorageSynchronized associations of the elements in the groups have different CopyState values.

    Partitioned: State of replication relationship can not be determined, for example, due to a connection problem.

    Invalid: The array is unable to determine the state of the replication relationship, for example, after the connection is restored; however, either source or target elements have an unknown status. 

    Restored: It indicates the source element was restored from the target element.

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    2        Initialized    
    3        Unsynchronized 
    4        Synchronized   
    5        Broken         
    6        Fractured      
    7        Split          
    8        Inactive       
    9        Suspended      
    10       Failedover     
    11       Prepared       
    12       Aborted        
    13       Skewed         
    14       Mixed          
    15       Not Applicable 
    16       Partitioned    
    17       Invalid        
    18       Restored       
    ..       DMTF Reserved  
    0x8000.. Vendor Specific
    ======== ===============
    
.. _CIM-Synchronized-WhenDeactivated:

``datetime`` **WhenDeactivated**

    Specifies when the association was deactivated. A deactivated association is reactivated.Must be set to NULL if implementation is not capable of providing this information. A value of 0 indicates the information is not known.

    
.. _CIM-Synchronized-CopyRecoveryMode:

``uint16`` **CopyRecoveryMode**

    Describes whether the copy operation continues after a broken link is restored.

    Automatic: copy operation resumes automatically.

    Manual: CopyState is set to Suspended after the link is restored. It is required to issue the Resume operation to continue.

    
    ============ ===============
    ValueMap     Values         
    ============ ===============
    0            Unknown        
    2            Automatic      
    3            Manual         
    ..           DMTF Reserved  
    32768..65535 Vendor Specific
    ============ ===============
    
.. _CIM-Synchronized-SyncType:

``uint16`` **SyncType**

    SyncType describes the intended outcome of the replication.Values are: 

    Mirror: create and maintain a copy of the source. 

    Snapshot: create a PIT, virtual copy of the source. 

    Clone: create a PIT, full copy the source.

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    ..       DMTF Reserved  
    6        Mirror         
    7        Snapshot       
    8        Clone          
    ..       DMTF Reserved  
    0x8000.. Vendor Specific
    ======== ===============
    
.. _CIM-Synchronized-WhenSuspended:

``datetime`` **WhenSuspended**

    Specifies when the association was suspended. A suspended association is resumed.Must be set to NULL if implementation is not capable of providing this information. A value of 0 indicates the information is not known.

    
.. _CIM-Synchronized-SystemElement:

:ref:`CIM_ManagedElement <CIM-ManagedElement>` **SystemElement**

    SystemElement represents one ManagedElement that is synchronized with the entity referenced as SyncedElement.

    
.. _CIM-Synchronized-WhenSynced:

``datetime`` **WhenSynced**

    The point in time that the Elements were synchronized.

    
.. _CIM-Synchronized-SyncMaintained:

``boolean`` **SyncMaintained**

    Boolean indicating whether synchronization is maintained.

    
.. _CIM-Synchronized-RequestedCopyState:

``uint16`` **RequestedCopyState**

    RequestedCopyState is an integer enumeration that indicates the last requested or desired state for the association. The actual state of the association is represented by CopyState. Note that when CopyState reaches the requested state, this property will be set to 'Not Applicable.

    
.. _CIM-Synchronized-WhenSynchronized:

``datetime`` **WhenSynchronized**

    Specifies when the CopyState has a value of Synchronized. Must be set to NULL if implementation is not capable of providing this information. A value of 0 indicates the information is not known.

    
.. _CIM-Synchronized-Mode:

``uint16`` **Mode**

    Mode describes whether the target elements will be updated synchronously or asynchronously. If NULL, implementaton decides the mode.

    
    ============ ===============
    ValueMap     Values         
    ============ ===============
    0            Unknown        
    2            Synchronous    
    3            Asynchronous   
    ..           DMTF Reserved  
    32768..65535 Vendor Specific
    ============ ===============
    
.. _CIM-Synchronized-ProgressStatus:

``uint16`` **ProgressStatus**

    ProgressStatus describes the status of the association with respect to Replication activity. Values are: Completed: The request is completed. Data flow is idle. 

    Dormant: Indicates that the data flow is inactive suspended or quiesced. 

    Initializing: In the process of establishing source/replica association and the data flow has not started. 

    Preparing: preparation-in-progress. 

    Synchronizing: sync-in-progress. 

    Resyncing: resync-in-progess. 

    Restoring: restore-in-progress. 

    Fracturing: fracture-in-progress. 

    Splitting: split-in-progress. 

    Failing over: in the process of switching source and target. 

    Failing back: Undoing the result of failover. 

    Detaching: detach-in-progress. 

    Aborting: abort-in-progress. 

    Mixed: Applies to groups with element pairs with different statuses. Generally, the individual statuses need to be examined.Suspending: The copy operation is in the process of being suspended. 

    Requires fracture: The requested operation has completed, however, the synchronization relationship needs to be fractured before further copy operations can be issued. 

    Requires resync: The requested operation has completed, however, the synchronization relationship needs to be resynced before further copy operations can be issued. 

    Requires activate: The requested operation has completed, however, the synchronization relationship needs to be activated before further copy operations can be issued. 

    Pending: The flow of data has stopped momentarily due to limited bandwidth or busy system. 

    Requires detach: The requested operation has completed, however, the synchronization relationship needs to be detached before further copy operations can be issued.

    
    ======== =================
    ValueMap Values           
    ======== =================
    0        Unknown          
    2        Completed        
    3        Dormant          
    4        Initializing     
    5        Preparing        
    6        Synchronizing    
    7        Resyncing        
    8        Restoring        
    9        Fracturing       
    10       Splitting        
    11       Failing over     
    12       Failing back     
    13       Aborting         
    14       Mixed            
    15       Not Applicable   
    16       Suspending       
    17       Requires fracture
    18       Requires resync  
    19       Requires activate
    20       Pending          
    21       Detaching        
    22       Requires detach  
    ..       DMTF Reserved    
    0x8000.. Vendor Specific  
    ======== =================
    
.. _CIM-Synchronized-PercentSynced:

``uint16`` **PercentSynced**

    Specifies the percent of the work completed to reach synchronization. Must be set to NULL if implementation is not capable of providing this information.

    
.. _CIM-Synchronized-SyncedElement:

:ref:`CIM_ManagedElement <CIM-ManagedElement>` **SyncedElement**

    SyncedElement represents another ManagedElement that is synchronized with the entity referenced as SystemElement.

    
.. _CIM-Synchronized-WhenEstablished:

``datetime`` **WhenEstablished**

    Specifies when the association was established. Must be set to NULL if implementation is not capable of providing this information. A value of 0 indicates the information is not known.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

