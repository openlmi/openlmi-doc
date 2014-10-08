.. _CIM-PowerManagementService:

CIM_PowerManagementService
--------------------------

Class reference
===============
Subclass of :ref:`CIM_Service <CIM-Service>`

A class derived from Service that describes power management functionality, hosted on a System. Whether this service might be used to affect the power state of a particular element is defined by the CIM_ServiceAvailable ToElement association.


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

    .. _CIM-PowerManagementService-SetPowerState:

``uint32`` **SetPowerState** (``uint16`` PowerState, :ref:`CIM_ManagedElement <CIM-ManagedElement>` ManagedElement, ``datetime`` Time)

    The CIM_PowerManagementService.RequestPowerStateChange method should be used instead of SetPowerState method, which is deprecated. SetPowerState defines the desired power state of the managed element and when the element should be put into that state. The SetPowerState method has three input parameters, no output parameters, and a result. 

    - PowerState indicates the desired power state. 

    - ManagedElement indicates the element whose state is set. This element should be associated with the service using the ServiceAvailableToElement relationship. 

    - Time indicates when the power state should be set, either as a regular date-time value or as an interval value (where the interval begins when the method invocation is received). 

    Note that when the PowerState parameter is equal to 5, "Power Cycle (Off -Soft)", the Time parameter indicates when the managed element should be powered on again. Power-off is immediate. 

    SetPowerState should return 0 if successful, 1 if the specified State and Time request is not supported for the element, and some other value if any other error occurred. In a subclass, the set of possible return codes could be specified, using a ValueMap qualifier on the method. The strings to which the ValueMap contents are 'translated' can also be specified in the subclass as a Values array qualifier.

    
    **Parameters**
    
        *IN* ``uint16`` **PowerState**
            The power state for ManagedElement.

            
            ======== ========================
            ValueMap Values                  
            ======== ========================
            1        On                      
            2        Sleep - Light           
            3        Sleep -Deep             
            4        Vendor Specific         
            5        Power Cycle (Off - Soft)
            6        Off - Hard              
            7        Hibernate (Off - Soft)  
            8        Off - Soft              
            ======== ========================
            
        
        *IN* :ref:`CIM_ManagedElement <CIM-ManagedElement>` **ManagedElement**
            ManagedElement indicates the element whose state is set.

            
        
        *IN* ``datetime`` **Time**
            Time indicates when the power state should be set, either as a regular date-time value or as an interval value (where the interval begins when the method invocation is received.

            
        
    
    .. _CIM-PowerManagementService-RequestPowerStateChange:

``uint32`` **RequestPowerStateChange** (``uint16`` PowerState, :ref:`CIM_ManagedElement <CIM-ManagedElement>` ManagedElement, ``datetime`` Time, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job, ``datetime`` TimeoutPeriod)

    RequestPowerStateChange defines the desired power state of the managed element, and when the element should be put into that state. The RequestPowerStateChange method has five input parameters and a result code. 

    - PowerState indicates the desired power state. 

    - ManagedElement indicates the element whose state is set. This element SHOULD be associated to the service using the AssociatedPowerManagementService relationship. 

    - Time indicates when the power state should be set, either as a regular date-time value or as an interval value (where the interval begins when the method invocation is received). 

    - Job is a reference to the job if started. 

    - TimeOutPeriod indicates the maximum amount of time a client is expects the transition to take. 

    See CIM_PowerStateCapabilities for descriptions of PowerState parameter enumerations.

    
    ============ =======================================
    ValueMap     Values                                 
    ============ =======================================
    0            Completed with No Error                
    1            Not Supported                          
    2            Unknown or Unspecified Error           
    3            Cannot complete within Timeout Period  
    4            Failed                                 
    5            Invalid Parameter                      
    6            In Use                                 
    ..           DMTF Reserved                          
    4096         Method Parameters Checked - Job Started
    4097         Invalid State Transition               
    4098         Use of Timeout Parameter Not Supported 
    4099         Busy                                   
    4100..32767  Method Reserved                        
    32768..65535 Vendor Specific                        
    ============ =======================================
    
    **Parameters**
    
        *IN* ``uint16`` **PowerState**
            The power state for ManagedElement.

            
            ======== =================================
            ValueMap Values                           
            ======== =================================
            2        Power On                         
            3        Sleep - Light                    
            4        Sleep - Deep                     
            5        Power Cycle (Off Soft)           
            6        Power Off - Hard                 
            7        Hibernate                        
            8        Power Off - Soft                 
            9        Power Cycle (Off Hard)           
            10       Master Bus Reset                 
            11       Diagnostic Interrupt (NMI)       
            12       Power Off - Soft Graceful        
            13       Power Off - Hard Graceful        
            14       Master Bus Reset Graceful        
            15       Power Cycle (Off - Soft Graceful)
            16       Power Cycle (Off - Hard Graceful)
            ======== =================================
            
        
        *IN* :ref:`CIM_ManagedElement <CIM-ManagedElement>` **ManagedElement**
            ManagedElement indicates the element whose state is set.

            
        
        *IN* ``datetime`` **Time**
            Time indicates when the power state should be set, either as a regular date-time value or as an interval value (where the interval begins when the method invocation is received.

            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job (can be null if the task is completed).

            
        
        *IN* ``datetime`` **TimeoutPeriod**
            A timeout period that specifies the maximum amount of time that the client expects the transition to the new state to take. The interval format must be used to specify the TimeoutPeriod. A value of 0 or a null parameter indicates that the client has no time requirements for the transition. 

            If this property does not contain 0 or null and the implementation does not support this parameter, a return code of 'Use Of Timeout Parameter Not Supported' must be returned.

            
        
    

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
| :ref:`StopService <CIM-Service-StopService>`
| :ref:`ChangeAffectedElementsAssignedSequence <CIM-Service-ChangeAffectedElementsAssignedSequence>`
| :ref:`StartService <CIM-Service-StartService>`

