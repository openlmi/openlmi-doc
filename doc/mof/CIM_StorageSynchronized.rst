.. _CIM-StorageSynchronized:

CIM_StorageSynchronized
-----------------------

Class reference
===============
Subclass of :ref:`CIM_Synchronized <CIM-Synchronized>`

Indicates that two Storage objects were replicated at the specified point in time. If the CopyType property is set to 'Sync' (=3), then synchronization of the Storage objects is preserved.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemElement <CIM-Synchronized-SystemElement>`
| :ref:`SyncedElement <CIM-Synchronized-SyncedElement>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-StorageSynchronized-CopyPriority:

``uint16`` **CopyPriority**

    CopyPriority allows the priority of background copy engine I/O to be managed relative to host I/O operations during a sequential background copy operation. 

    Values are: Low: copy engine I/O lower priority than host I/O. Same: copy engine I/O has the same priority as host I/O. High: copy engine I/O has higher priority than host I/O. Urgent: copy operation to be performed as soon as possible, regardless of the host I/O requests.

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    0        Not Managed    
    1        Low            
    2        Same           
    3        High           
    4        Urgent         
    ..       DMTF Reserved  
    0x8000.. Vendor Specific
    ======== ===============
    
.. _CIM-StorageSynchronized-ReplicaType:

``uint16`` **ReplicaType**

    ReplicaType provides information on how the Replica is being maintained. Values are: 

    Full Copy: This indicates that a full copy of the source object is (or will be) generated . 

    Before Delta: This indicates that the source object will be maintained as a delta data from the replica. 

    After Delta: This indicates that the replica will be maintained as delta data from the source object. 

    Log: This indicates that the replica object is being maintained as a log of changes to the source. 

    Not Specified: The method of maintaining the copy is not specified.

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    0        Not Specified  
    2        Full Copy      
    3        Before Delta   
    4        After Delta    
    5        Log            
    ..       DMTF Reserved  
    0x8000.. Vendor Specific
    ======== ===============
    
.. _CIM-StorageSynchronized-SystemElement:

:ref:`CIM_ManagedElement <CIM-ManagedElement>` **SystemElement**

    SystemElement represents the Storage that is the source of the replication.

    
.. _CIM-StorageSynchronized-UndiscoveredElement:

``uint16`` **UndiscoveredElement**

    This property specifies whether the source, the target, or both elements involved in a copy operation are undiscovered. An element is considered undiscovered if its object model is not known to the service performing the copy operation. The values are: 

    SystemElement: The source element. 

    SyncedElement: The target element. 

    Both: Both the source and the target elements. If both the source and the target elements are discovered, the value of this property shall be NULL.

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    2        SystemElement  
    3        SyncedElement  
    4        Both           
    ..       DMTF Reserved  
    0x8000.. Vendor Specific
    ======== ===============
    
.. _CIM-StorageSynchronized-CopyType:

``uint16`` **CopyType**

    CopyType describes the Replication Policy. Values are: 

    Async: create and maintain an asynchronous copy of the source. 

    Sync: create and maintain a synchronized copy of the source. 

    UnSyncAssoc: create an unsynchronized copy and maintain an association to the source. 

    UnSyncUnAssoc: create an unsynchronized copy with a temporary association that is deleted upon completion of the copy operation.

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    2        Async          
    3        Sync           
    4        UnSyncAssoc    
    5        UnSyncUnAssoc  
    ..       DMTF Reserved  
    0x8000.. Vendor Specific
    ======== ===============
    
.. _CIM-StorageSynchronized-CopyMethodology:

``uint16`` **CopyMethodology**

    CopyMethodology specifies what copy methodology the service uses to create and/or maintain the target element. 

    Values are: 

    Not Specified: The method of maintaining the copy is not specified. 

    Full Copy: This indicates that a full copy of the source object is (or will be) generated . 

    Incremental-Copy: Only changed data from source element is copied to target element. 

    Differential-Copy: Only the new writes to source element are copied to the target element. 

    Copy-On-Write: Affected data is copied on the first write to the source or to the target elements. 

    Copy-On-Access: Affected data is copied on the first access to the source element. 

    Delta-Update: Difference based replication where after the initial copy, only updates to source are copied to target. 

    Snap-And-Clone: The service creates a snapshot of the source element first, then uses the the snapshot as the source of the copy operation to the target element.

    
    ======== ======================
    ValueMap Values                
    ======== ======================
    0        Not Specified         
    1        Other                 
    2        Implementation decides
    3        Full Copy             
    4        Incremental-Copy      
    5        Differential-Copy     
    6        Copy-On-Write         
    7        Copy-On-Access        
    8        Delta-Update          
    9        Snap-And-Clone        
    ..       DMTF Reserved         
    0x8000.. Vendor Specific       
    ======== ======================
    
.. _CIM-StorageSynchronized-SyncState:

``uint16`` **SyncState**

    SyncState describes the state of the association with respect to Replication activity. Values are: 

    Initialized: The link to enable replication is established. 

    and source/replica elements are associated, but the Copy engine has not started. 

    PrepareInProgress: Preparation for Replication is in progress and the Copy engine has started. 

    Prepared: All necessary preparation has completed. 

    ResyncInProgress: Synchronization or Resynchronization is in progress. 

    This may be the initial 'copy' or subsequent changes being copied. 

    Synchronized: An Async or Sync replication is currently synchronized. When this value is set, SyncMaintained will be true. 

    FractureInProgress: An operation to fracture an Async or Sync replication is in progress. 

    Fractured: An Async or Sync replication is fractured. 

    QuiesceInProgress: A quiesce operation is in progress. 

    Quiesced: The replication has been quiesced and is ready for a change. 

    RestoreInProgress: An operation is in progress to copy the Synced object to the System object. 

    Idle: The 'normal' state for an UnSyncAssoc replica. 

    Frozen: All blocks copied from source to an UnSyncAssoc replica and the copy engine is stopped. 

    CopyInProgress: A deferred background copy operation is in progress to copy the source to the replica target for an UnSyncAssoc association. 

    Broken: The relationship is non-functional due to errors in the source, the target, the path between the two or space constraints.

    
    ======== ====================
    ValueMap Values              
    ======== ====================
    0        Unknown             
    2        Initialized         
    3        PrepareInProgress   
    4        Prepared            
    5        ResyncInProgress    
    6        Synchronized        
    7        Fracture In Progress
    8        QuiesceInProgress   
    9        Quiesced            
    10       Restore In Progresss
    11       Idle                
    12       Broken              
    13       Fractured           
    14       Frozen              
    15       Copy In Progress    
    ..       DMTF Reserved       
    0x8000.. Vendor Specific     
    ======== ====================
    
.. _CIM-StorageSynchronized-ReadOnly:

``uint16`` **ReadOnly**

    This property specifies whether the source, the target, or both elements are "read only" to the host.SystemElement: The source element. 

    SyncedElement: The target element. 

    Both: Both the source and the target elements.are read only to the host.

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    2        SystemElement  
    3        SyncedElement  
    4        Both           
    ..       DMTF Reserved  
    0x8000.. Vendor Specific
    ======== ===============
    
.. _CIM-StorageSynchronized-SyncedElement:

:ref:`CIM_ManagedElement <CIM-ManagedElement>` **SyncedElement**

    SyncedElement represents the Storage that is the target of the replication.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``datetime`` :ref:`WhenActivated <CIM-Synchronized-WhenActivated>`
| ``uint16`` :ref:`CopyState <CIM-Synchronized-CopyState>`
| ``datetime`` :ref:`WhenSynchronized <CIM-Synchronized-WhenSynchronized>`
| ``uint16`` :ref:`SyncType <CIM-Synchronized-SyncType>`
| ``datetime`` :ref:`WhenSuspended <CIM-Synchronized-WhenSuspended>`
| ``datetime`` :ref:`WhenEstablished <CIM-Synchronized-WhenEstablished>`
| ``boolean`` :ref:`FailedCopyStopsHostIO <CIM-Synchronized-FailedCopyStopsHostIO>`
| ``uint16`` :ref:`RequestedCopyState <CIM-Synchronized-RequestedCopyState>`
| ``uint16`` :ref:`Mode <CIM-Synchronized-Mode>`
| ``uint16`` :ref:`PercentSynced <CIM-Synchronized-PercentSynced>`
| ``datetime`` :ref:`WhenDeactivated <CIM-Synchronized-WhenDeactivated>`
| ``uint16`` :ref:`CopyRecoveryMode <CIM-Synchronized-CopyRecoveryMode>`
| ``uint16`` :ref:`ProgressStatus <CIM-Synchronized-ProgressStatus>`
| ``datetime`` :ref:`WhenSynced <CIM-Synchronized-WhenSynced>`
| ``boolean`` :ref:`SyncMaintained <CIM-Synchronized-SyncMaintained>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

