.. _CIM-NetworkPipe:

CIM_NetworkPipe
---------------

Class reference
===============
Subclass of :ref:`CIM_EnabledLogicalElement <CIM-EnabledLogicalElement>`

NetworkPipe is a subclass of EnabledLogicalElement, representing the state and management of a connection or trail between endpoints. This object is different than the association between the endpoints (CIM_ActiveConnection) since the emphasis is NOT on the endpoints but on the management of the pipe itself - its state, configuration, etc. NetworkPipes are defined in the context of a CIM_Network and represent the 'transfer of information . . . between . . . endpoints'. These concepts are aligned with the definition of the Pipe object in ITU's M.3100 specification.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-NetworkPipe-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-NetworkPipe-RequestedState:

``uint16`` **RequestedState**

    RequestedState is an integer enumeration that indicates the last requested or desired state for the element, irrespective of the mechanism through which it was requested. The actual state of the element is represented by EnabledState. This property is provided to compare the last requested and current enabled or disabled states. Note that when EnabledState is set to 5 ("Not Applicable"), then this property has no meaning. Refer to the EnabledState property description for explanations of the values in the RequestedState enumeration. 

    "Unknown" (0) indicates the last requested state for the element is unknown.

    Note that the value "No Change" (5) has been deprecated in lieu of indicating the last requested state is "Unknown" (0). If the last requested or desired state is unknown, RequestedState should have the value "Unknown" (0), but may have the value "No Change" (5).Offline (6) indicates that the element has been requested to transition to the Enabled but Offline EnabledState. 

    It should be noted that there are two new values in RequestedState that build on the statuses of EnabledState. These are "Reboot" (10) and "Reset" (11). Reboot refers to doing a "Shut Down" and then moving to an "Enabled" state. Reset indicates that the element is first "Disabled" and then "Enabled". The distinction between requesting "Shut Down" and "Disabled" should also be noted. Shut Down requests an orderly transition to the Disabled state, and might involve removing power, to completely erase any existing state. The Disabled state requests an immediate disabling of the element, such that it will not execute or accept any commands or processing requests. 

    

    This property is set as the result of a method invocation (such as Start or StopService on CIM_Service), or can be overridden and defined as WRITEable in a subclass. The method approach is considered superior to a WRITEable property, because it allows an explicit invocation of the operation and the return of a result code. 

    

    If knowledge of the last RequestedState is not supported for the EnabledLogicalElement, the property shall be NULL or have the value 12 "Not Applicable".

    
    ============ ===============
    ValueMap     Values         
    ============ ===============
    0            Unknown        
    2            Enabled        
    3            Disabled       
    4            Shut Down      
    5            No Change      
    6            Offline        
    7            Test           
    8            Deferred       
    9            Quiesce        
    10           Reboot         
    11           Reset          
    12           Not Applicable 
    ..           DMTF Reserved  
    32768..65535 Vendor Reserved
    ============ ===============
    
.. _CIM-NetworkPipe-InstanceID:

``string`` **InstanceID**

    Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. In order to ensure uniqueness within the NameSpace, the value of InstanceID SHOULD be constructed using the following 'preferred' algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon ':', and where <OrgID> MUST include a copyrighted, trademarked or otherwise unique name that is owned by the business entity creating/defining the InstanceID, or is a registered ID that is assigned to the business entity by a recognized global authority. (This is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness <OrgID> MUST NOT contain a colon (':'). When using this algorithm, the first colon to appear in InstanceID MUST appear between <OrgID> and <LocalID>. (For DMTF defined instances, the 'preferred' algorithm MUST be used with the <OrgID> set to 'CIM'.) 

    <LocalID> MUST include either a vendor specified unique identifier, or if mapping from an ITU M.3100 environment, the trailID, connectionID or subNetworkConnectionID of the instances of PipeR2.

    
.. _CIM-NetworkPipe-AggregationBehavior:

``uint16`` **AggregationBehavior**

    Indicates whether the pipe is composed of lower-level pipes, and if so, how these lower-level pipes are aggregated (in parallel or in sequence). The specific instances of NetworkPipe that are combined are described using the NetworkPipeComposition association. 

    

    In the context of M.3100, the ability to be composed of lower-level pipes is modeled as a Trail. A Trail is made up of one or more Connections. (Note that both Trails and Connections are subclasses of Pipe). Because of the flexibility of the NetworkPipeComposition association, there is no need to subclass NetworkPipe, as was done in M.3100, but merely to instantiate the NetworkPipeComposition association to describe the bundling of the lower-level pipes (i.e., the connections), or the sequencing of them.

    
    ======== ==========================
    ValueMap Values                    
    ======== ==========================
    0        Unknown                   
    2        No Lower-Level Composition
    3        Combined In Parallel      
    4        Combined In Sequence      
    ======== ==========================
    
.. _CIM-NetworkPipe-EnabledState:

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
    
.. _CIM-NetworkPipe-Directionality:

``uint16`` **Directionality**

    Indicates whether the pipe is bi-directional (value = 2), unidirectional (value = 3), or this information is not known (value = 0). For unidirectional pipes, the source and sink are indicated by a property (SourceOrSink) of the association, EndpointOfNetworkPipe.

    
    ======== ==============
    ValueMap Values        
    ======== ==============
    0        Unknown       
    2        Bi-Directional
    3        Unidirectional
    ======== ==============
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`

