.. _LMI-BlockStatisticsService:

LMI_BlockStatisticsService
--------------------------

Class reference
===============
Subclass of :ref:`CIM_BlockStatisticsService <CIM-BlockStatisticsService>`

A subclass of StatisticsService that provides services for filtering and retrieving statistics from a StatisticsManifestCollection that contains instances of BlockStatisticalData.


Key properties
^^^^^^^^^^^^^^

| :ref:`Name <CIM-Service-Name>`
| :ref:`SystemName <CIM-Service-SystemName>`
| :ref:`SystemCreationClassName <CIM-Service-SystemCreationClassName>`
| :ref:`CreationClassName <CIM-Service-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-BlockStatisticsService-HealthState:

``uint16`` **HealthState**

    Indicates the current health of the element. This attribute expresses the health of this element but not necessarily that of its subcomponents. The possible values are 0 to 30, where 5 means the element is entirely healthy and 30 means the element is completely non-functional. The following continuum is defined: 

    "Non-recoverable Error" (30) - The element has completely failed, and recovery is not possible. All functionality provided by this element has been lost. 

    "Critical Failure" (25) - The element is non-functional and recovery might not be possible. 

    "Major Failure" (20) - The element is failing. It is possible that some or all of the functionality of this component is degraded or not working. 

    "Minor Failure" (15) - All functionality is available but some might be degraded. 

    "Degraded/Warning" (10) - The element is in working order and all functionality is provided. However, the element is not working to the best of its abilities. For example, the element might not be operating at optimal performance or it might be reporting recoverable errors. 

    "OK" (5) - The element is fully functional and is operating within normal operational parameters and without error. 

    "Unknown" (0) - The implementation cannot report on HealthState at this time. 

    DMTF has reserved the unused portion of the continuum for additional HealthStates in the future.

    
    ============ =====================
    ValueMap     Values               
    ============ =====================
    0            Unknown              
    5            OK                   
    10           Degraded/Warning     
    15           Minor failure        
    20           Major failure        
    25           Critical failure     
    30           Non-recoverable error
    ..           DMTF Reserved        
    32768..65535 Vendor Specific      
    ============ =====================
    
.. _LMI-BlockStatisticsService-Started:

``boolean`` **Started**

    Started is a Boolean that indicates whether the Service has been started (TRUE), or stopped (FALSE).

    
.. _LMI-BlockStatisticsService-PrimaryStatus:

``uint16`` **PrimaryStatus**

    PrimaryStatus provides a high level status value, intended to align with Red-Yellow-Green type representation of status. It should be used in conjunction with DetailedStatus to provide high level and detailed health status of the ManagedElement and its subcomponents. 

    PrimaryStatus consists of one of the following values: Unknown, OK, Degraded or Error. "Unknown" indicates the implementation is in general capable of returning this property, but is unable to do so at this time. 

    "OK" indicates the ManagedElement is functioning normally. 

    "Degraded" indicates the ManagedElement is functioning below normal. 

    "Error" indicates the ManagedElement is in an Error condition.

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    0        Unknown        
    1        OK             
    2        Degraded       
    3        Error          
    ..       DMTF Reserved  
    0x8000.. Vendor Reserved
    ======== ===============
    
.. _LMI-BlockStatisticsService-EnabledDefault:

``uint16`` **EnabledDefault**

    An enumerated value indicating an administrator's default or startup configuration for the Enabled State of an element. By default, the element is "Enabled" (value=2).

    
    ============ ===================
    ValueMap     Values             
    ============ ===================
    2            Enabled            
    3            Disabled           
    5            Not Applicable     
    6            Enabled but Offline
    7            No Default         
    9            Quiesce            
    ..           DMTF Reserved      
    32768..65535 Vendor Reserved    
    ============ ===================
    
.. _LMI-BlockStatisticsService-EnabledState:

``uint16`` **EnabledState**

    EnabledState is an integer enumeration that indicates the enabled and disabled states of an element. It can also indicate the transitions between these requested states. For example, shutting down (value=4) and starting (value=10) are transient states between enabled and disabled. The following text briefly summarizes the various enabled and disabled states: 

    Enabled (2) indicates that the element is or could be executing commands, will process any queued commands, and queues new requests. 

    Disabled (3) indicates that the element will not execute commands and will drop any new requests. 

    Shutting Down (4) indicates that the element is in the process of going to a Disabled state. 

    Not Applicable (5) indicates the element does not support being enabled or disabled. 

    Enabled but Offline (6) indicates that the element might be completing commands, and will drop any new requests. 

    Test (7) indicates that the element is in a test state. 

    Deferred (8) indicates that the element might be completing commands, but will queue any new requests. 

    Quiesce (9) indicates that the element is enabled but in a restricted mode.

    Starting (10) indicates that the element is in the process of going to an Enabled state. New requests are queued.

    
    ============ ===================
    ValueMap     Values             
    ============ ===================
    0            Unknown            
    1            Other              
    2            Enabled            
    3            Disabled           
    4            Shutting Down      
    5            Not Applicable     
    6            Enabled but Offline
    7            In Test            
    8            Deferred           
    9            Quiesce            
    10           Starting           
    11..32767    DMTF Reserved      
    32768..65535 Vendor Reserved    
    ============ ===================
    
.. _LMI-BlockStatisticsService-StartMode:

``string`` **StartMode**

    **Deprecated!** 
    Note: The use of this element is deprecated in lieu of the EnabledDefault property that is inherited from EnabledLogicalElement. The EnabledLogicalElement addresses the same semantics. The change to a uint16 data type was discussed when CIM V2.0 was defined. However, existing V1.0 implementations used the string property. To remain compatible with those implementations, StartMode was grandfathered into the schema. Use of the deprecated qualifier allows the maintenance of the existing property but also permits an improved, clarified definition using EnabledDefault. 

    Deprecated description: StartMode is a string value that indicates whether the Service is automatically started by a System, an Operating System, and so on, or is started only upon request.

    
.. _LMI-BlockStatisticsService-OperationalStatus:

``uint16[]`` **OperationalStatus**

    Indicates the current statuses of the element. Various operational statuses are defined. Many of the enumeration's values are self-explanatory. However, a few are not and are described here in more detail. 

    "Stressed" indicates that the element is functioning, but needs attention. Examples of "Stressed" states are overload, overheated, and so on. 

    "Predictive Failure" indicates that an element is functioning nominally but predicting a failure in the near future. 

    "In Service" describes an element being configured, maintained, cleaned, or otherwise administered. 

    "No Contact" indicates that the monitoring system has knowledge of this element, but has never been able to establish communications with it. 

    "Lost Communication" indicates that the ManagedSystem Element is known to exist and has been contacted successfully in the past, but is currently unreachable. 

    "Stopped" and "Aborted" are similar, although the former implies a clean and orderly stop, while the latter implies an abrupt stop where the state and configuration of the element might need to be updated. 

    "Dormant" indicates that the element is inactive or quiesced. 

    "Supporting Entity in Error" indicates that this element might be "OK" but that another element, on which it is dependent, is in error. An example is a network service or endpoint that cannot function due to lower-layer networking problems. 

    "Completed" indicates that the element has completed its operation. This value should be combined with either OK, Error, or Degraded so that a client can tell if the complete operation Completed with OK (passed), Completed with Error (failed), or Completed with Degraded (the operation finished, but it did not complete OK or did not report an error). 

    "Power Mode" indicates that the element has additional power model information contained in the Associated PowerManagementService association. 

    "Relocating" indicates the element is being relocated.

    OperationalStatus replaces the Status property on ManagedSystemElement to provide a consistent approach to enumerations, to address implementation needs for an array property, and to provide a migration path from today's environment to the future. This change was not made earlier because it required the deprecated qualifier. Due to the widespread use of the existing Status property in management applications, it is strongly recommended that providers or instrumentation provide both the Status and OperationalStatus properties. Further, the first value of OperationalStatus should contain the primary status for the element. When instrumented, Status (because it is single-valued) should also provide the primary status of the element.

    
    ======== ==========================
    ValueMap Values                    
    ======== ==========================
    0        Unknown                   
    1        Other                     
    2        OK                        
    3        Degraded                  
    4        Stressed                  
    5        Predictive Failure        
    6        Error                     
    7        Non-Recoverable Error     
    8        Starting                  
    9        Stopping                  
    10       Stopped                   
    11       In Service                
    12       No Contact                
    13       Lost Communication        
    14       Aborted                   
    15       Dormant                   
    16       Supporting Entity in Error
    17       Completed                 
    18       Power Mode                
    19       Relocating                
    ..       DMTF Reserved             
    0x8000.. Vendor Reserved           
    ======== ==========================
    

Local methods
^^^^^^^^^^^^^

    .. _LMI-BlockStatisticsService-GetStatisticsCollection:

``uint32`` **GetStatisticsCollection** (:ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, ``uint16[]`` ElementTypes, :ref:`CIM_BlockStatisticsManifestCollection <CIM-BlockStatisticsManifestCollection>` ManifestCollection, ``uint16`` StatisticsFormat, ``string[]`` Statistics)

    Retrieves statistics in a well-defined bulk format. The collection of statistics returned is determined by the list of element types passed in to the method and the manifests for those types contained in the supplied BlockStatisticsManifestCollection. If both the Elements and BlockStatisticsManifestCollection parameters are supplied, then the types of elements returned is an intersection of the element types listed in the Elements parameter and the types for which BlockStatisticsManifest instances exist in the supplied BlockStatisticsManifestCollection. The statistics are returned through a well-defined array of strings, whose format is specified by the StatisticsFormat parameter, that can be parsed to retrieve the desired statistics as well as limited information about the elements that those metrics describe.

    
    ============ =======================================
    ValueMap     Values                                 
    ============ =======================================
    0            Job Completed with No Error            
    1            Not Supported                          
    2            Unknown                                
    3            Timeout                                
    4            Failed                                 
    5            Invalid Parameter                      
    ..           Method Reserved                        
    4096         Method Parameters Checked - Job Started
    4097         Element Not Supported                  
    4098         Statistics Format Not Supported        
    4099..32767  Method Reserved                        
    32768..65535 Vendor Specific                        
    ============ =======================================
    
    **Parameters**
    
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (may be null if job completed).

            
        
        *IN* ``uint16[]`` **ElementTypes**
            Element types for which statistics should be returned. If not supplied (i.e. parameter is null) this parameter is not considered when filtering the instances of StatisticalData that will populate the Statistics output parameter. If the array is not null, but is empty, then no statistics will be returned by this method. A client SHOULD NOT specify this parameter if it is not meaningful (i.e. the service only provides statistics for a single type of element).

            
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
            
        
        *IN* :ref:`CIM_BlockStatisticsManifestCollection <CIM-BlockStatisticsManifestCollection>` **ManifestCollection**
            The BlockStatisticsManifestCollection that contains the manifests that list the metrics to be returned for each element type. If not supplied (i.e. parameter is null), then all available statistics will be returned unfiltered. Only elements that match the element type properties (if meaningful) of the BlockStatisticsManifest instances contained within the BlockStatisticsManifestCollection will have data returned by this method. If the supplied BlockStatisticsManifestCollection does not contain any BlockStatisticsManifest instances, then no statistics will be returned by this method.

            
        
        *IN* ``uint16`` **StatisticsFormat**
            Specifies the format of the Statistics output parameter.

            - CSV = Comma Separated Values.

            
            ======== ===============
            ValueMap Values         
            ======== ===============
            0        Unknown        
            1        Other          
            2        CSV            
            ..       DMTF Reserved  
            0x8000.. Vendor Specific
            ======== ===============
            
        
        *OUT* ``string[]`` **Statistics**
            The statistics for all the elements as determined by the Elements, ManifestCollection parameters, and StatisticsFormat parameters.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`SystemName <CIM-Service-SystemName>`
| ``string`` :ref:`LoSID <CIM-Service-LoSID>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`Name <CIM-Service-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string`` :ref:`LoSOrgID <CIM-Service-LoSOrgID>`
| ``string`` :ref:`PrimaryOwnerContact <CIM-Service-PrimaryOwnerContact>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`SystemCreationClassName <CIM-Service-SystemCreationClassName>`
| ``string`` :ref:`CreationClassName <CIM-Service-CreationClassName>`
| ``string`` :ref:`PrimaryOwnerName <CIM-Service-PrimaryOwnerName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`
| :ref:`RemoveManifests <CIM-BlockStatisticsService-RemoveManifests>`
| :ref:`ChangeAffectedElementsAssignedSequence <CIM-Service-ChangeAffectedElementsAssignedSequence>`
| :ref:`AddOrModifyManifest <CIM-BlockStatisticsService-AddOrModifyManifest>`
| :ref:`StopService <CIM-Service-StopService>`
| :ref:`StartService <CIM-Service-StartService>`
| :ref:`CreateManifestCollection <CIM-BlockStatisticsService-CreateManifestCollection>`

