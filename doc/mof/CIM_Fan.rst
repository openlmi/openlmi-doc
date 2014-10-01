.. _CIM-Fan:

CIM_Fan
-------

Class reference
===============
Subclass of :ref:`CIM_CoolingDevice <CIM-CoolingDevice>`

Capabilities and management of a Fan CoolingDevice.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-Fan-VariableSpeed:

``boolean`` **VariableSpeed**

    Indication of whether the fan supports variable speeds.

    
.. _CIM-Fan-DesiredControlMode:

``uint16`` **DesiredControlMode**

    DesiredControlMode is an integer enumeration indicating the last requested or desired control mode for the fan. The actual control mode is represented by ControlMode. The property is provided to compare the last requested and the current control mode. Refer to the ControlMode property Description for explanations of the values in the DesiredControlMode enumeration.

    
    ============ ===============
    ValueMap     Values         
    ============ ===============
    0            Unknown        
    2            Automatic      
    3            Manual         
    4..32767     DMTF Reserved  
    32768..65535 Vendor Reserved
    ============ ===============
    
.. _CIM-Fan-ControlModesSupported:

``uint16[]`` **ControlModesSupported**

    ControlModesSupported indicates the supported control modes of the Fan: automatic or manual. In Automatic mode the Fan is controlled automatically in management function below the CIM. In Manual mode, the fan speed may be controlled by the CIM user by the SetSpeed method. Changing from Automatic to Manual, would not generally cause the speed to change. Changing from Manual to Automatic may cause the fan speed to change depending on the Thermal conditions of the system and the thermal management function.

    
    ============ ================
    ValueMap     Values          
    ============ ================
    0            Unknown         
    2            Automatic       
    3            Manual          
    4..32767     DMTF Reserved   
    32768..65535 Vendor Specified
    ============ ================
    
.. _CIM-Fan-DesiredSpeed:

``uint64`` **DesiredSpeed**

    DesiredSpeed is the currently requested fan speed, defined in revolutions per minute, when a variable speed fan is supported (VariableSpeed Boolean = TRUE). The current speed is determined using a sensor (CIM_Tachometer) that is associated with the Fan using the CIM_AssociatedSensor relationship.

    
.. _CIM-Fan-ControlMode:

``uint16`` **ControlMode**

    ControlMode indicates the mode in which management of the Fan is operating. When in Manual mode, the SetSpeed method can be used to control the fan speed.

    
    ============ ===============
    ValueMap     Values         
    ============ ===============
    0            Unknown        
    2            Automatic      
    3            Manual         
    4..32767     DMTF Reserved  
    32768..65535 Vendor Reserved
    ============ ===============
    

Local methods
^^^^^^^^^^^^^

    .. _CIM-Fan-SetSpeed:

``uint32`` **SetSpeed** (``uint64`` DesiredSpeed)

    Method that requests that the Fan speed be set to the value specified in the input parameter of the method. The return value should be: 

    0 if the request was successfully executed 

    1 if the request is not supported 

    2 if the request is not valid for the current mode 

    3 if the requested speed is not currently valid 

    Some other value if an error occurred. In a subclass, the set of possible return codes could be specified, using a ValueMap qualifier on the method. The strings to which the ValueMap contents are 'translated' can also be specified in the subclass as a Values array qualifier.

    
    ============ =====================================
    ValueMap     Values                               
    ============ =====================================
    0            Completed with No Errors             
    1            Not Supported                        
    2            Invalid ControlMode for Setting Speed
    3            Invalid Speed                        
    4..32767     DMTF Reserved                        
    32768..65535 Vendor Reserved                      
    ============ =====================================
    
    **Parameters**
    
        *IN* ``uint64`` **DesiredSpeed**
            The desired speed for the fan.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``string[]`` :ref:`IdentifyingDescriptions <CIM-LogicalDevice-IdentifyingDescriptions>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``boolean`` :ref:`ErrorCleared <CIM-LogicalDevice-ErrorCleared>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16`` :ref:`LocationIndicator <CIM-LogicalDevice-LocationIndicator>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string[]`` :ref:`OtherIdentifyingInfo <CIM-LogicalDevice-OtherIdentifyingInfo>`
| ``uint64`` :ref:`PowerOnHours <CIM-LogicalDevice-PowerOnHours>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``uint16[]`` :ref:`AdditionalAvailability <CIM-LogicalDevice-AdditionalAvailability>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16`` :ref:`StatusInfo <CIM-LogicalDevice-StatusInfo>`
| ``string`` :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| ``uint16[]`` :ref:`PowerManagementCapabilities <CIM-LogicalDevice-PowerManagementCapabilities>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`MaxQuiesceTime <CIM-LogicalDevice-MaxQuiesceTime>`
| ``uint64`` :ref:`TotalPowerOnHours <CIM-LogicalDevice-TotalPowerOnHours>`
| ``string`` :ref:`ErrorDescription <CIM-LogicalDevice-ErrorDescription>`
| ``uint16`` :ref:`Availability <CIM-LogicalDevice-Availability>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint32`` :ref:`LastErrorCode <CIM-LogicalDevice-LastErrorCode>`
| ``string`` :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`
| ``string`` :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| ``boolean`` :ref:`ActiveCooling <CIM-CoolingDevice-ActiveCooling>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`Reset <CIM-LogicalDevice-Reset>`
| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`
| :ref:`SetPowerState <CIM-LogicalDevice-SetPowerState>`
| :ref:`QuiesceDevice <CIM-LogicalDevice-QuiesceDevice>`
| :ref:`EnableDevice <CIM-LogicalDevice-EnableDevice>`
| :ref:`OnlineDevice <CIM-LogicalDevice-OnlineDevice>`
| :ref:`SaveProperties <CIM-LogicalDevice-SaveProperties>`
| :ref:`RestoreProperties <CIM-LogicalDevice-RestoreProperties>`

