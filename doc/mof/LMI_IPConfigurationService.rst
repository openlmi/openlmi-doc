.. _LMI-IPConfigurationService:

LMI_IPConfigurationService
--------------------------

Class reference
===============
Subclass of :ref:`CIM_IPConfigurationService <CIM-IPConfigurationService>`

CIM_IPConfigurationService provides management of the IP configuration associated with a LANEndpoint or IPProtocolEndpoint or IPNetworkConnection or the global IP configuration for the ComputerSystem.


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

    .. _LMI-IPConfigurationService-ApplySettingToLANEndpoint:

``uint32`` **ApplySettingToLANEndpoint** (:ref:`CIM_IPAssignmentSettingData <CIM-IPAssignmentSettingData>` Configuration, :ref:`CIM_LANEndpoint <CIM-LANEndpoint>` Endpoint, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job)

    Apply the configuration represented by the IPAssignmentSettingData to the specified LANEndpoint. This will result in the value of the IsCurrent property of the CIM_ElementSettingData which associates the specified CIM_IPAssignmentSettingData and specified CIM_LANEndpoint have a value of "true". The IsCurrent property of any other instances of CIM_ElementSettingData which reference the specified CIM_LANEndpoint and an instance of CIM_IPAssignmentSettingData will have a value of "false". Each instance of CIM_StaticIPAssignmentSettingData which is aggregated into the target CIM_IPAssignmentSettingData instance will result in the creation of an instance of CIM_IPProtocolEndpoint associated with the target CIM_LANEndpoint instance via an instance of the CIM_BindsTo association. The created CIM_IPProtocolEndpoint instance will have the values specified in the CIM_StaticIPAssignmentSettingData instance.

    
    ======== =======================================
    ValueMap Values                                 
    ======== =======================================
    0        Completed with No Error                
    1        Not Supported                          
    2        Unknown/Unspecified Error              
    3        Failed                                 
    4        Invalid Parameter                      
    5        Busy                                   
    4096     Method Parameters Checked - Job Started
    ======== =======================================
    
    **Parameters**
    
        *IN* :ref:`CIM_IPAssignmentSettingData <CIM-IPAssignmentSettingData>` **Configuration**
            The IPAssignmentSettingData to apply.

            
        
        *IN* :ref:`CIM_LANEndpoint <CIM-LANEndpoint>` **Endpoint**
            The LANEndpoint to which the configuration will be applied.

            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job spawned if the operation continues after the method returns. (may be null if task completed).

            
        
    
    .. _LMI-IPConfigurationService-ApplySettingToIPNetworkConnection:

``uint32`` **ApplySettingToIPNetworkConnection** (:ref:`CIM_IPAssignmentSettingData <CIM-IPAssignmentSettingData>` SettingData, :ref:`CIM_IPVersionSettingData <CIM-IPVersionSettingData>` IPVersionSettingData, :ref:`CIM_IPNetworkConnection <CIM-IPNetworkConnection>` IPNetworkConnection, ``uint16`` Mode, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job)

    Apply the IP setting respresented by the LMI_IPAssignmentSettingData to the specified IPNetworkConnection. The settings may take effect or disable immediately or may be set to take effect or disable in the next boot, depending on system, IPNetworkConnection, Setting and the value specified for Mode. This will reflect in the IsCurrent & IsNext property of instances of LMI_IPElementSettingData associating the SettingData with the IPNetworkConnection. For cases, enabling one setting can result in automatic disabling of another setting, it will be refelected in the properties of ElementSettingData associating those settings to the IPNetworkConnection. Refer the description for the Mode parameter for more details.

    
    ======== =======================================
    ValueMap Values                                 
    ======== =======================================
    0        Completed with No Error                
    1        Not Supported                          
    2        Unknown/Unspecified Error              
    3        Failed                                 
    4        Invalid Parameter                      
    5        Busy                                   
    4096     Method Parameters Checked - Job Started
    ======== =======================================
    
    **Parameters**
    
        *IN* :ref:`CIM_IPAssignmentSettingData <CIM-IPAssignmentSettingData>` **SettingData**
            The IPAssignmentSettingData to apply.

            
        
        *IN* :ref:`CIM_IPVersionSettingData <CIM-IPVersionSettingData>` **IPVersionSettingData**
            This value is always ignored, present only for API compatibility.

            
        
        *IN* :ref:`CIM_IPNetworkConnection <CIM-IPNetworkConnection>` **IPNetworkConnection**
            The IPNetworkConnection to which the configuration will be applied

            
        
        *IN* ``uint16`` **Mode**
            The mode in which the configuration need to be applied to the IPNetworkConnection.

            - ``Mode 0`` - implies use ``Mode 1`` if allowed, else ``Mode 2``.

            - ``Mode 1`` - Results in ``IsNext = 1 (Is Next)``, ``IsCurrent = 1 (Is Current)`` for the CIM_ElementSettingData associating the setting with IPNetworkConnection.

            - ``Mode 2`` - Results in ``IsNext = 1 (Is Next)`` for the CIM_ElementSettingData associating the setting with IPNetworkConnection. The value of ``IsCurrent`` will not be affected.

            - ``Mode 3`` - implies use ``Mode 4`` if allowed, else ``Mode 5``.

            - ``Mode 4`` - Results in ``IsNext = 2 (Is Not Next)``, ``IsCurrent = 2 (Is Not Current)`` for the CIM_ElementSettingData associating the setting with IPNetworkConnection.

            - ``Mode 5`` - Results in ``IsNext = 2 (Is Not Next)`` for the CIM_ElementSettingData associating the setting with IPNetworkConnection. The value of ``IsCurrent`` will not be affected.

            - ``Mode 6`` - Results in ``IsNext = 3 (Is Next For Single Use)`` for the CIM_ElementSettingData associating the setting with IPNetworkConnection. The value of IsCurrent will not be affected. To change the ``IsNext = 3 (Is Next For Single Use)`` for a Setting, invoke the method with any of the other values for the mode.- ``Mode 32768`` - Results in ``IsCurrent = 1 (Is Current)`` for the CIM_ElementSettingData associating the setting with IPNetworkConnection. The value of ``IsNext`` will not be affected.

            - ``Mode 32769`` - Results in ``IsCurrent = 2 (Is Not Current)`` for the CIM_ElementSettingData associating the setting with IPNetworkConnection. The value of ``IsNext`` will not be affected.

            

            
            ======== ==========
            ValueMap Values    
            ======== ==========
            0        Mode 0    
            1        Mode 1    
            2        Mode 2    
            3        Mode 3    
            4        Mode 4    
            5        Mode 5    
            6        Mode 6    
            32768    Mode 32768
            32769    Mode 32769
            ======== ==========
            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job spawned if the operation continues after the method returns. (may be null if task completed).

            
        
    
    .. _LMI-IPConfigurationService-ApplySettingToIPProtocolEndpoint:

``uint32`` **ApplySettingToIPProtocolEndpoint** (:ref:`CIM_IPAssignmentSettingData <CIM-IPAssignmentSettingData>` Configuration, :ref:`CIM_IPProtocolEndpoint <CIM-IPProtocolEndpoint>` Endpoint, :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` Job)

    Apply the configuration represented by the CIM_IPAssignmentSettingData to the specified IPProtocolEndpoint. This will result in the value of the IsCurrent property of the CIM_ElementSettingData which associates the specified CIM_IPAssignmentSettingData and specified CIM_IPProtocolEndpoint having a value of "true". The IsCurrent property of any other instances of CIM_ElementSettingData which reference the specified CIM_IPProtocolEndpoint and an instance of CIM_IPAssignmentSettingData will have a value of "false". Each instance of CIM_IPAssignmentSettingData which is aggregated into the target CIM_IPAssignmentSettingData instance will be applied to the CIM_ProtocolEndpoint to which it is associated via an instance of CIM_ElementSettingData where the CIM_ProtocolEndpoint is associated with the target CIM_IPProtocolEndpoint via an instance of CIM_EndpointIdentity.

    
    ======== =======================================
    ValueMap Values                                 
    ======== =======================================
    0        Completed with No Error                
    1        Not Supported                          
    2        Unknown/Unspecified Error              
    3        Failed                                 
    4        Invalid Parameter                      
    5        Busy                                   
    4096     Method Parameters Checked - Job Started
    ======== =======================================
    
    **Parameters**
    
        *IN* :ref:`CIM_IPAssignmentSettingData <CIM-IPAssignmentSettingData>` **Configuration**
            The IPAssignmentSettingData to apply.

            
        
        *IN* :ref:`CIM_IPProtocolEndpoint <CIM-IPProtocolEndpoint>` **Endpoint**
            The IPProtocolEndpoint to which the configuration will be applied.

            
        
        *OUT* :ref:`CIM_ConcreteJob <CIM-ConcreteJob>` **Job**
            Reference to the job spawned if the operation continues after the method returns. This parameter MUST NOT be null if a value of 4096 is returned. This parameter MUST be null if any other value is returned by the method.

            
        
    

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
| :ref:`ApplySettingToComputerSystem <CIM-IPConfigurationService-ApplySettingToComputerSystem>`
| :ref:`AddStaticIPv4Interface <CIM-IPConfigurationService-AddStaticIPv4Interface>`
| :ref:`ChangeAffectedElementsAssignedSequence <CIM-Service-ChangeAffectedElementsAssignedSequence>`
| :ref:`StartService <CIM-Service-StartService>`

