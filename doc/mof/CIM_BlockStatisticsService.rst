.. _CIM-BlockStatisticsService:

CIM_BlockStatisticsService
--------------------------

Class reference
===============
Subclass of :ref:`CIM_StatisticsService <CIM-StatisticsService>`

A subclass of StatisticsService that provides services for filtering and retrieving statistics from a StatisticsManifestCollection that contains instances of BlockStatisticalData.


Key properties
^^^^^^^^^^^^^^

| :ref:`Name <CIM-Service-Name>`
| :ref:`SystemName <CIM-Service-SystemName>`
| :ref:`SystemCreationClassName <CIM-Service-SystemCreationClassName>`
| :ref:`CreationClassName <CIM-Service-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

*None*

Local methods
^^^^^^^^^^^^^

    .. _CIM-BlockStatisticsService-RemoveManifests:

``uint32`` **RemoveManifests** (:ref:`CIM_BlockStatisticsManifestCollection <CIM-BlockStatisticsManifestCollection>` ManifestCollection, :ref:`CIM_BlockStatisticsManifest[] <CIM-BlockStatisticsManifest>` Manifests)

    Extrinsic method that removes manifests from a BlockStatisticsManifestCollection.

    
    ============ ==================
    ValueMap     Values            
    ============ ==================
    0            Success           
    1            Not Supported     
    2            Unknown           
    3            Timeout           
    4            Failed            
    5            Invalid Parameter 
    ..           Method Reserved   
    4096         Manifest not found
    4097..32767  Method Reserved   
    32768..65535 Vendor Specific   
    ============ ==================
    
    **Parameters**
    
        *IN* :ref:`CIM_BlockStatisticsManifestCollection <CIM-BlockStatisticsManifestCollection>` **ManifestCollection**
            BlockStatisticsManifestCollection from which the BlockStatisticsManifests will be removed.

            
        
        *IN* :ref:`CIM_BlockStatisticsManifest[] <CIM-BlockStatisticsManifest>` **Manifests**
            List of BlockStatisticsManifests to be removed from the BlockStatisticsManifestCollection.

            
        
    
    .. _CIM-BlockStatisticsService-GetStatisticsCollection:

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

            
        
    
    .. _CIM-BlockStatisticsService-AddOrModifyManifest:

``uint32`` **AddOrModifyManifest** (:ref:`CIM_BlockStatisticsManifestCollection <CIM-BlockStatisticsManifestCollection>` ManifestCollection, ``uint16`` ElementType, ``string`` ElementName, ``string[]`` StatisticsList, :ref:`CIM_BlockStatisticsManifest <CIM-BlockStatisticsManifest>` Manifest)

    Method that creates or modifies a BlockStatisticsManifest for this statistics service. A client supplies a BlockStatisticsManifestCollection in which the new BlockStatisticsManifest will be placed or an existing BlockStatisticsManifest will be modified, the element type of the statistics that the BlockStatisticsManifest will filter, and a list of metrics, which serves as a filter for statistical data of that element type.

    
    ============ =============================
    ValueMap     Values                       
    ============ =============================
    0            Success                      
    1            Not Supported                
    2            Unknown                      
    3            Timeout                      
    4            Failed                       
    5            Invalid Parameter            
    ..           Method Reserved              
    4096         Element Not Supported        
    4097         Metric not supported         
    4098         ElementType Parameter Missing
    4099..32767  Method Reserved              
    32768..65535 Vendor Specific              
    ============ =============================
    
    **Parameters**
    
        *IN* :ref:`CIM_BlockStatisticsManifestCollection <CIM-BlockStatisticsManifestCollection>` **ManifestCollection**
            BlockStatisticsManifestCollection that the BlockStatisticsManifest is or should be a member of.

            
        
        *IN* ``uint16`` **ElementType**
            The type of elements whose statistics the BlockStatisticsManifest will filter.

            
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
            
        
        *IN* ``string`` **ElementName**
            A client-defined string that identifies the BlockStatisticsManifest created or modified by this method.

            
        
        *IN* ``string[]`` **StatisticsList**
            The metrics that will be included by the filter. The metrics supplied here are the properties of CIM_StatisticalData or one of its subclasses that will remain after the BlockStatisticsManifest filter is applied.

            
        
        *OUT* :ref:`CIM_BlockStatisticsManifest <CIM-BlockStatisticsManifest>` **Manifest**
            The BlockStatisticsManifest that is created or modified on successful execution of the method.

            
        
    
    .. _CIM-BlockStatisticsService-CreateManifestCollection:

``uint32`` **CreateManifestCollection** (:ref:`CIM_StatisticsCollection <CIM-StatisticsCollection>` Statistics, ``string`` ElementName, :ref:`CIM_BlockStatisticsManifestCollection <CIM-BlockStatisticsManifestCollection>` ManifestCollection)

    Creates a new BlockStatisticsManifestCollection instance, whose members can serve as a filter for metrics retrieved through the GetStatisticsCollection method.

    
    ============ =================
    ValueMap     Values           
    ============ =================
    0            Ok               
    1            Not Supported    
    2            Unknown          
    3            Timeout          
    4            Failed           
    5            Invalid Parameter
    6..32767     Method Reserved  
    32768..65535 Vendor Specific  
    ============ =================
    
    **Parameters**
    
        *IN* :ref:`CIM_StatisticsCollection <CIM-StatisticsCollection>` **Statistics**
            The collection of statistics that will be filtered using the new BlockStatisticsManifestCollection.

            
        
        *IN* ``string`` **ElementName**
            Client-defined name for the new BlockStatisticsManifestCollection.

            
        
        *OUT* :ref:`CIM_BlockStatisticsManifestCollection <CIM-BlockStatisticsManifestCollection>` **ManifestCollection**
            Reference to the new BlockStatisticsManifestCollection.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`SystemName <CIM-Service-SystemName>`
| ``string`` :ref:`LoSID <CIM-Service-LoSID>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``boolean`` :ref:`Started <CIM-Service-Started>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`Name <CIM-Service-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``string`` :ref:`LoSOrgID <CIM-Service-LoSOrgID>`
| ``string`` :ref:`PrimaryOwnerContact <CIM-Service-PrimaryOwnerContact>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`StartMode <CIM-Service-StartMode>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`SystemCreationClassName <CIM-Service-SystemCreationClassName>`
| ``string`` :ref:`CreationClassName <CIM-Service-CreationClassName>`
| ``string`` :ref:`PrimaryOwnerName <CIM-Service-PrimaryOwnerName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`
| :ref:`ChangeAffectedElementsAssignedSequence <CIM-Service-ChangeAffectedElementsAssignedSequence>`
| :ref:`StopService <CIM-Service-StopService>`
| :ref:`StartService <CIM-Service-StartService>`

