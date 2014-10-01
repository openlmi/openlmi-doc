.. _LMI-LANEndpoint:

LMI_LANEndpoint
---------------

Class reference
===============
Subclass of :ref:`CIM_LANEndpoint <CIM-LANEndpoint>`

A communication endpoint which, when its associated interface device is connected to a LAN, may send and receive data frames. LANEndpoints include Ethernet, Token Ring and FDDI interfaces.


Key properties
^^^^^^^^^^^^^^

| :ref:`CreationClassName <CIM-ServiceAccessPoint-CreationClassName>`
| :ref:`SystemName <CIM-ServiceAccessPoint-SystemName>`
| :ref:`Name <CIM-ServiceAccessPoint-Name>`
| :ref:`SystemCreationClassName <CIM-ServiceAccessPoint-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-LANEndpoint-RequestedState:

``uint16`` **RequestedState**

    RequestedState is an integer enumeration that indicates the last requested or desired state for the element, irrespective of the mechanism through which it was requested. The actual state of the element is represented by EnabledState. This property is provided to compare the last requested and current enabled or disabled states. Note that when EnabledState is set to 5 ("Not Applicable"), then this property has no meaning. Refer to the EnabledState property description for explanations of the values in the RequestedState enumeration. 

    "Unknown" (0) indicates the last requested state for the element is unknown.

    Note that the value "No Change" (5) has been deprecated in lieu of indicating the last requested state is "Unknown" (0). If the last requested or desired state is unknown, RequestedState should have the value "Unknown" (0), but may have the value "No Change" (5).Offline (6) indicates that the element has been requested to transition to the Enabled but Offline EnabledState. 

    It should be noted that there are two new values in RequestedState that build on the statuses of EnabledState. These are "Reboot" (10) and "Reset" (11). Reboot refers to doing a "Shut Down" and then moving to an "Enabled" state. Reset indicates that the element is first "Disabled" and then "Enabled". The distinction between requesting "Shut Down" and "Disabled" should also be noted. Shut Down requests an orderly transition to the Disabled state, and might involve removing power, to completely erase any existing state. The Disabled state requests an immediate disabling of the element, such that it will not execute or accept any commands or processing requests. 

    

    This property is set as the result of a method invocation (such as Start or StopService on CIM_Service), or can be overridden and defined as WRITEable in a subclass. The method approach is considered superior to a WRITEable property, because it allows an explicit invocation of the operation and the return of a result code. 

    

    If knowledge of the last RequestedState is not supported for the EnabledLogicalElement, the property shall be NULL or have the value 12 "Not Applicable".

    
    ======== =========
    ValueMap Values   
    ======== =========
    0        Unknown  
    2        Enabled  
    3        Disabled 
    5        No Change
    ======== =========
    
.. _LMI-LANEndpoint-ElementName:

``string`` **ElementName**

    The name of the device's control (and often data) interface. 

    
.. _LMI-LANEndpoint-ProtocolIFType:

``uint16`` **ProtocolIFType**

    ProtocolIFType's enumeration is limited to Layer 2-related and reserved values for this subclass of ProtocolEndpoint.

    
    ======== ================
    ValueMap Values          
    ======== ================
    6        Ethernet CSMA/CD
    ======== ================
    
.. _LMI-LANEndpoint-EnabledState:

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

    
    ======== ===================
    ValueMap Values             
    ======== ===================
    0        Unknown            
    2        Enabled            
    3        Disabled           
    6        Enabled but Offline
    ======== ===================
    
.. _LMI-LANEndpoint-AvailableRequestedStates:

``uint16[]`` **AvailableRequestedStates**

    AvailableRequestedStates indicates the possible values for the RequestedState parameter of the method RequestStateChange, used to initiate a state change. The values listed shall be a subset of the values contained in the RequestedStatesSupported property of the associated instance of CIM_EnabledLogicalElementCapabilities where the values selected are a function of the current state of the CIM_EnabledLogicalElement. This property may be non-null if an implementation is able to advertise the set of possible values as a function of the current state. This property shall be null if an implementation is unable to determine the set of possible values as a function of the current state.

    
    ======== ========
    ValueMap Values  
    ======== ========
    2        Enabled 
    3        Disabled
    ======== ========
    
.. _LMI-LANEndpoint-MACAddress:

``string`` **MACAddress**

    The principal unicast address used in communication with the LANEndpoint. The MAC address is formatted as twelve hexadecimal digits (e.g., "010203040506"), with each pair representing one of the six octets of the MAC address in "canonical" bit order according to RFC 2469.

    
.. _LMI-LANEndpoint-OperatingStatus:

``uint16`` **OperatingStatus**

    OperatingStatus provides a current status value for the operational condition of the element and can be used for providing more detail with respect to the value of EnabledState. It can also provide the transitional states when an element is transitioning from one state to another, such as when an element is transitioning between EnabledState and RequestedState, as well as other transitional conditions.

    OperatingStatus consists of one of the following values: Unknown, Not Available, In Service, Starting, Stopping, Stopped, Aborted, Dormant, Completed, Migrating, Emmigrating, Immigrating, Snapshotting. Shutting Down, In Test 

    A Null return indicates the implementation (provider) does not implement this property. 

    "Unknown" indicates the implementation is in general capable of returning this property, but is unable to do so at this time. 

    "None" indicates that the implementation (provider) is capable of returning a value for this property, but not ever for this particular piece of hardware/software or the property is intentionally not used because it adds no meaningful information (as in the case of a property that is intended to add additional info to another property). 

    "Servicing" describes an element being configured, maintained, cleaned, or otherwise administered. 

    "Starting" describes an element being initialized. 

    "Stopping" describes an element being brought to an orderly stop. 

    "Stopped" and "Aborted" are similar, although the former implies a clean and orderly stop, while the latter implies an abrupt stop where the state and configuration of the element might need to be updated. 

    "Dormant" indicates that the element is inactive or quiesced. 

    "Completed" indicates that the element has completed its operation. This value should be combined with either OK, Error, or Degraded in the PrimaryStatus so that a client can tell if the complete operation Completed with OK (passed), Completed with Error (failed), or Completed with Degraded (the operation finished, but it did not complete OK or did not report an error). 

    "Migrating" element is being moved between host elements. 

    "Immigrating" element is being moved to new host element. 

    "Emigrating" element is being moved away from host element. 

    "Shutting Down" describes an element being brought to an abrupt stop. 

    "In Test" element is performing test functions. 

    "Transitioning" describes an element that is between states, that is, it is not fully available in either its previous state or its next state. This value should be used if other values indicating a transition to a specific state are not applicable.

    "In Service" describes an element that is in service and operational.

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Unknown      
    1        Not Available
    3        Starting     
    4        Stopping     
    5        Stopped      
    6        Aborted      
    7        Dormant      
    16       In Service   
    ======== =============
    

Local methods
^^^^^^^^^^^^^

    .. _LMI-LANEndpoint-RequestStateChange:

``uint32`` **RequestStateChange** (``uint16`` RequestedState, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, ``datetime`` TimeoutPeriod)

    Requests that the state of the element be changed to the value specified in the RequestedState parameter. When the requested state change takes place, the EnabledState and RequestedState of the element will be the same. Invoking the RequestStateChange method multiple times could result in earlier requests being overwritten or lost. 

    TimeoutPeriod argument is not supported yet and should be NULL. 

    A return code of 0 shall indicate the state change was successfully initiated. 

    Any other return code indicates an error condition.

    
    ======== =======================================
    ValueMap Values                                 
    ======== =======================================
    0        Completed with No Error                
    1        Not Supported                          
    2        Unknown or Unspecified Error           
    3        Cannot complete within Timeout Period  
    4        Failed                                 
    5        Invalid Parameter                      
    6        In Use                                 
    4096     Method Parameters Checked - Job Started
    4097     Invalid State Transition               
    4098     Use of Timeout Parameter Not Supported 
    4099     Busy                                   
    ======== =======================================
    
    **Parameters**
    
        *IN* ``uint16`` **RequestedState**
            The state requested for the element. This information will be placed into the RequestedState property of the instance if the return code of the RequestStateChange method is 0 ('Completed with No Error'). Refer to the description of the EnabledState and RequestedState properties for the detailed explanations of the RequestedState values.

            
            ======== ========
            ValueMap Values  
            ======== ========
            2        Enabled 
            3        Disabled
            ======== ========
            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Creating jobs for changing Endpoint state is not supported. This parameter will always be NULL.

            
        
        *IN* ``datetime`` **TimeoutPeriod**
            Using TimeoutPeriod is not supported.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string[]`` :ref:`GroupAddresses <CIM-LANEndpoint-GroupAddresses>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`LANType <CIM-LANEndpoint-LANType>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`SystemName <CIM-ServiceAccessPoint-SystemName>`
| ``string`` :ref:`NameFormat <CIM-ProtocolEndpoint-NameFormat>`
| ``string[]`` :ref:`AliasAddresses <CIM-LANEndpoint-AliasAddresses>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`Description <CIM-ProtocolEndpoint-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-ProtocolEndpoint-TimeOfLastStateChange>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint32`` :ref:`MaxDataSize <CIM-LANEndpoint-MaxDataSize>`
| ``string`` :ref:`LANID <CIM-LANEndpoint-LANID>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`Name <CIM-ProtocolEndpoint-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`OtherTypeDescription <CIM-ProtocolEndpoint-OtherTypeDescription>`
| ``boolean`` :ref:`BroadcastResetSupported <CIM-ProtocolEndpoint-BroadcastResetSupported>`
| ``uint16`` :ref:`ProtocolType <CIM-ProtocolEndpoint-ProtocolType>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ProtocolEndpoint-OperationalStatus>`
| ``string`` :ref:`CreationClassName <CIM-ServiceAccessPoint-CreationClassName>`
| ``string`` :ref:`OtherLANType <CIM-LANEndpoint-OtherLANType>`
| ``string`` :ref:`SystemCreationClassName <CIM-ServiceAccessPoint-SystemCreationClassName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`BroadcastReset <CIM-ProtocolEndpoint-BroadcastReset>`

