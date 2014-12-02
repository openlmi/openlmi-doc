.. _CIM-LogicalDevice:

CIM_LogicalDevice
-----------------

Class reference
===============
Subclass of :ref:`CIM_EnabledLogicalElement <CIM-EnabledLogicalElement>`

An abstraction or emulation of a hardware entity, that might or might not be Realized in physical hardware. Any characteristics of a LogicalDevice that are used to manage its operation or configuration are contained in, or associated with, the LogicalDevice object. Examples of the operational properties of a Printer would be paper sizes supported or detected errors. Examples of the configuration properties of a Sensor Device would be threshold settings. Various configurations could exist for a LogicalDevice. These configurations could be contained in Setting objects and associated with the LogicalDevice.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-LogicalDevice-PowerManagementSupported:

``boolean`` **PowerManagementSupported**

    **Deprecated!** 
    Note: The use of this property has been deprecated. Instead, the existence of an associated PowerManagementCapabilities class (associated using the ElementCapabilities relationship) indicates that power management is supported. Deprecated description: Boolean that indicates that the Device can use power management.

    
.. _CIM-LogicalDevice-SystemName:

``string`` **SystemName**

    The System Name of the scoping system.

    
.. _CIM-LogicalDevice-IdentifyingDescriptions:

``string[]`` **IdentifyingDescriptions**

    An array of free-form strings providing explanations and details behind the entries in the OtherIdentifyingInfo array. Note that each entry of this array is related to the entry in OtherIdentifyingInfo that is located at the same index.

    
.. _CIM-LogicalDevice-ErrorCleared:

``boolean`` **ErrorCleared**

    **Deprecated!** 
    Note: The use of this method is deprecated. 

    Deprecated description: ErrorCleared is a Boolean property that indicates that the error reported in LastErrorCode is now cleared.

    
.. _CIM-LogicalDevice-LocationIndicator:

``uint16`` **LocationIndicator**

    An integer that reflects the state of an indicator (e.g., LED) that is part of a device. Reading the value gives the current state. Writing the value with 'On'/'Off' turns the indicator on/off, other values may not be written.

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Unknown      
    2        On           
    3        Off          
    4        Not Supported
    ======== =============
    
.. _CIM-LogicalDevice-OtherIdentifyingInfo:

``string[]`` **OtherIdentifyingInfo**

    OtherIdentifyingInfo captures data, in addition to DeviceID information, that could be used to identify a LogicalDevice. For example, you could use this property to hold the operating system's user-friendly name for the Device.

    
.. _CIM-LogicalDevice-PowerOnHours:

``uint64`` **PowerOnHours**

    Note: The use of this method is deprecated. 

    Deprecated description: The number of consecutive hours that this Device has been powered on since its last power cycle.

    
.. _CIM-LogicalDevice-AdditionalAvailability:

``uint16[]`` **AdditionalAvailability**

    Additional availability and status of the Device in addition to that specified in the Availability property. The Availability property denotes the primary status and availability of the Device. In some cases, this property will not be sufficient to denote the complete status of the Device. In those cases, the AdditionalAvailability property can be used to provide further information. For example, the primary Availability of a device might be "Off line" (value=8) or in a low-power state (AdditionalAvailability value=14), or the Device could be running Diagnostics (AdditionalAvailability value=5, "In Test").

    
    ======== ===========================
    ValueMap Values                     
    ======== ===========================
    1        Other                      
    2        Unknown                    
    3        Running/Full Power         
    4        Warning                    
    5        In Test                    
    6        Not Applicable             
    7        Power Off                  
    8        Off Line                   
    9        Off Duty                   
    10       Degraded                   
    11       Not Installed              
    12       Install Error              
    13       Power Save - Unknown       
    14       Power Save - Low Power Mode
    15       Power Save - Standby       
    16       Power Cycle                
    17       Power Save - Warning       
    18       Paused                     
    19       Not Ready                  
    20       Not Configured             
    21       Quiesced                   
    ======== ===========================
    
.. _CIM-LogicalDevice-StatusInfo:

``uint16`` **StatusInfo**

    Note: The use of this method is deprecated in lieu of a more clearly named property (EnabledState) that is inherited from ManagedSystemElement and that has additional enumerated values. 

    Deprecated description: The StatusInfo property indicates whether the Logical Device is in an enabled state (value=3), disabled state (value=4), some other state (value=1), or an unknown state (value=2). If this property does not apply to the LogicalDevice, the value 5 ("Not Applicable") should be used. If a Device is ("Enabled")(value=3), it has been powered up and is configured and operational. The Device might or might not be functionally active, depending on whether its Availability (or AdditionalAvailability) indicates that it is ("Running/Full Power")(value=3) or ("Off line") (value=8). In an enabled but offline mode, a Device might be performing out-of-band requests, such as running Diagnostics. If StatusInfo is ("Disabled") (value=4), a Device can only be "enabled" or powered off. In a personal computer environment, ("Disabled") means that the driver of the device is not available in the stack. In other environments, a Device can be disabled by removing its configuration file. A disabled device is physically present in a System and consuming resources, but it cannot be communicated with until a driver is loaded, a configuration file is loaded, or some other "enabling" activity has occurred.

    
    ======== ==============
    ValueMap Values        
    ======== ==============
    1        Other         
    2        Unknown       
    3        Enabled       
    4        Disabled      
    5        Not Applicable
    ======== ==============
    
.. _CIM-LogicalDevice-DeviceID:

``string`` **DeviceID**

    An address or other identifying information used to uniquely name the LogicalDevice.

    
.. _CIM-LogicalDevice-PowerManagementCapabilities:

``uint16[]`` **PowerManagementCapabilities**

    **Deprecated!** 
    Note: The use of this property has been deprecated. Instead, use the PowerCapabilites property in an associated PowerManagementCapabilities class. Deprecated description: An enumerated array describing the power management capabilities of the Device.

    
    ======== ========================================
    ValueMap Values                                  
    ======== ========================================
    0        Unknown                                 
    1        Not Supported                           
    2        Disabled                                
    3        Enabled                                 
    4        Power Saving Modes Entered Automatically
    5        Power State Settable                    
    6        Power Cycling Supported                 
    7        Timed Power On Supported                
    ======== ========================================
    
.. _CIM-LogicalDevice-MaxQuiesceTime:

``uint64`` **MaxQuiesceTime**

    **Deprecated!** 
    Note: The use of this property has been deprecated. When evaluating the use of Quiesce, it was determined that this single property is not adequate for describing when a device will automatically exit a quiescent state. In fact, the most likely scenario for a device to exit a quiescent state was determined to be based on the number of outstanding requests queued rather than on a maximum time. This decision will be re-evaluated and repositioned later. 

    Deprecated description: Maximum time, in milliseconds, that a Device can run in a "Quiesced" state. The state is defined in its Availability and AdditionalAvailability properties, where "Quiesced" is conveyed by the value 21. What occurs at the end of the time limit is device-specific. The Device can unquiesce, can be offline, or can take other actions. A value of 0 indicates that a Device can remain quiesced indefinitely.

    
.. _CIM-LogicalDevice-TotalPowerOnHours:

``uint64`` **TotalPowerOnHours**

    **Deprecated!** 
    Note: The use of this method is deprecated. 

    Deprecated description: The total number of hours that this Device has been powered on.

    
.. _CIM-LogicalDevice-ErrorDescription:

``string`` **ErrorDescription**

    **Deprecated!** 
    Note: The use of this method is deprecated. 

    Deprecated description: ErrorDescription is a free-form string that supplies more information about the error recorded in LastErrorCode and information on any corrective actions that can be taken.

    
.. _CIM-LogicalDevice-LastErrorCode:

``uint32`` **LastErrorCode**

    **Deprecated!** 
    Note: The use of this method is deprecated. 

    Deprecated description: LastErrorCode captures the last error code reported by the LogicalDevice.

    
.. _CIM-LogicalDevice-CreationClassName:

``string`` **CreationClassName**

    CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

    
.. _CIM-LogicalDevice-Availability:

``uint16`` **Availability**

    Note: The use of this property has been deprecated. 

    Deprecated description: The primary availability and status of the Device. (Additional status information can be specified using the Additional Availability array property.) For example, the Availability property indicates that the Device is running and has full power (value=3), or is in a warning (4), test (5), degraded (10) or power save state (values 13-15 and 17). The Power Save states are defined as follows: Value 13 ("Power Save - Unknown") indicates that the Device is known to be in a power save mode, but its exact status in this mode is unknown; value 14 ("Power Save - Low Power Mode") indicates that the Device is in a power save state but still functioning, and might exhibit degraded performance; value 15 ("Power Save - Standby") indicates that the Device is not functioning but could be brought to full power 'quickly'; and value 17 ("Power Save - Warning") indicates that the Device is in a warning state, but is also in a power save mode.

    
    ======== ===========================
    ValueMap Values                     
    ======== ===========================
    1        Other                      
    2        Unknown                    
    3        Running/Full Power         
    4        Warning                    
    5        In Test                    
    6        Not Applicable             
    7        Power Off                  
    8        Off Line                   
    9        Off Duty                   
    10       Degraded                   
    11       Not Installed              
    12       Install Error              
    13       Power Save - Unknown       
    14       Power Save - Low Power Mode
    15       Power Save - Standby       
    16       Power Cycle                
    17       Power Save - Warning       
    18       Paused                     
    19       Not Ready                  
    20       Not Configured             
    21       Quiesced                   
    ======== ===========================
    
.. _CIM-LogicalDevice-SystemCreationClassName:

``string`` **SystemCreationClassName**

    The CreationClassName of the scoping system.

    

Local methods
^^^^^^^^^^^^^

    .. _CIM-LogicalDevice-Reset:

``uint32`` **Reset** ()

    Requests a reset of the LogicalDevice. The return value should be 0 if the request was successfully executed, 1 if the request is not supported, and some other value if an error occurred. In a subclass, the set of possible return codes could be specified, using a ValueMap qualifier on the method. The strings to which the ValueMap contents are 'translated' can also be specified in the subclass as a Values array qualifier.

    
    **Parameters**
    
*None*
    .. _CIM-LogicalDevice-SetPowerState:

``uint32`` **SetPowerState** (``uint16`` PowerState, ``datetime`` Time)

    **Deprecated!** 
    Note: The use of this method has been deprecated. Instead, use the SetPowerState method in the associated PowerManagementService class. Deprecated description: Sets the power state of the Device.

    
    **Parameters**
    
        *IN* ``uint16`` **PowerState**
            The power state to set.

            
            ======== ===========================
            ValueMap Values                     
            ======== ===========================
            1        Full Power                 
            2        Power Save - Low Power Mode
            3        Power Save - Standby       
            4        Power Save - Other         
            5        Power Cycle                
            6        Power Off                  
            ======== ===========================
            
        
        *IN* ``datetime`` **Time**
            Time indicates when the power state should be set, either as a regular date-time value or as an interval value (where the interval begins when the method invocation is received).

            
        
    
    .. _CIM-LogicalDevice-QuiesceDevice:

``uint32`` **QuiesceDevice** (``boolean`` Quiesce)

    Note: The use of this method has been deprecated in lieu of the more general RequestStateChange method that directly overlaps with the functionality provided by this method. 

    Deprecated description: Requests that the LogicalDevice cleanly cease all activity ("Quiesce" input parameter=TRUE) or resume activity (=FALSE). For this method to quiesce a Device, that Device should have an Availability (or Additional Availability) of "Running/Full Power" (value=3) and an EnabledStatus/StatusInfo of "Enabled". For example, if quiesced, a Device can then be taken offline for diagnostics, or disabled for power off and hot swap. For the method to "unquiesce" a Device, that Device should have an Availability (or AdditionalAvailability) of "Quiesced" (value=21) and an EnabledStatus or StatusInfo of "Enabled". In this case, the Device would be returned to an "Enabled" and "Running/Full Power" status. 

    The return code of the method should indicate the success or failure of the quiesce. It should return 0 if successful, 1 if the request is not supported at all, 2 if the request is not supported due to the current state of the Device, and some other value if any other error occurred. In a subclass, the set of possible return codes could be specified, using a ValueMap qualifier on the method. The strings to which the ValueMap contents are 'translated' can also be specified in the subclass as a Values array qualifier.

    
    **Parameters**
    
        *IN* ``boolean`` **Quiesce**
            If set to TRUE, then cleanly cease all activity. If FALSE, resume activity.

            
        
    
    .. _CIM-LogicalDevice-EnableDevice:

``uint32`` **EnableDevice** (``boolean`` Enabled)

    **Deprecated!** 
    Note: The use of this method has been deprecated in lieu of the more general RequestStateChange method that directly overlaps with the functionality provided by this method. 

    Deprecated description: Requests that the LogicalDevice be enabled ("Enabled" input parameter=TRUE) or disabled (=FALSE). If successful, the StatusInfo or EnabledState properties of the Device should reflect the desired state (enabled or disabled). Note that this function overlaps with the RequestedState property. RequestedState was added to the model to maintain a record (for example, a persisted value) of the last state request. Invoking the EnableDevice method should set the RequestedState property appropriately. 

    The return code should be 0 if the request was successfully executed, 1 if the request is not supported, and some other value if an error occurred. In a subclass, the set of possible return codes could be specified by using a ValueMap qualifier on the method. The strings to which the ValueMap contents are 'translated' can also be specified in the subclass as a Values array qualifier.

    
    **Parameters**
    
        *IN* ``boolean`` **Enabled**
            If TRUE, enable the device. If FALSE, disable the device.

            
        
    
    .. _CIM-LogicalDevice-OnlineDevice:

``uint32`` **OnlineDevice** (``boolean`` Online)

    Note: The use of this method has been deprecated in lieu of the more general RequestStateChange method that directly overlaps with the functionality provided by this method. 

    Deprecated description: Requests that the LogicalDevice be brought online ("Online" input parameter=TRUE) or taken offline (=FALSE). "Online" indicates that the Device is ready to accept requests, and is operational and fully functioning. In this case, the Availability property of the Device would be set to a value of 3 ("Running/Full Power"). "Offline" indicates that a Device is powered on and operational, but is not processing functional requests. In an offline state, a Device might be capable of running diagnostics or generating operational alerts. For example, when the "Offline" button is pushed on a Printer, the Device is no longer available to process print jobs, but it could be available for diagnostics or maintenance. 

    If this method is successful, the Availability and AdditionalAvailability properties of the Device should reflect the updated status. If a failure occurs when you try to bring the Device online or offline, it should remain in its current state. The request, if unsuccessful, should not leave the Device in an indeterminate state. When bringing a Device back "Online" from an "Offline" mode, the Device should be restored to its last "Online" state, if at all possible. Only a Device that has an EnabledState or StatusInfo of "Enabled" and has been configured can be brought online or taken offline. 

    OnlineDevice should return 0 if successful, 1 if the request is not supported at all, 2 if the request is not supported due to the current state of the Device, and some other value if any other error occurred. In a subclass, the set of possible return codes could be specified, using a ValueMap qualifier on the method. The strings to which the ValueMap contents are 'translated' can also be specified in the subclass as a Values array qualifier. 

    Note that the function of this method overlaps with the RequestedState property. RequestedState was added to the model to maintain a record (for example, a persisted value) of the last state request. Invoking the OnlineDevice method should set the RequestedState property appropriately.

    
    **Parameters**
    
        *IN* ``boolean`` **Online**
            If TRUE, take the device online. If FALSE, take the device offline.

            
        
    
    .. _CIM-LogicalDevice-SaveProperties:

``uint32`` **SaveProperties** ()

    **Deprecated!** 
    Note: The use of this method is deprecated. Its function is handled more generally by the ConfigurationData subclass of SettingData. 

    Deprecated description: Requests that the Device capture its current configuration, setup or state information, or both in a backing store. 

    The information returned by this method could be used at a later time (using the RestoreProperties method) to return a Device to its present "condition". This method might not be supported by all Devices. The method should return 0 if successful, 1 if the request is not supported, and some other value if any other error occurred. In a subclass, the set of possible return codes could be specified, using a ValueMap qualifier on the method. The strings to which the ValueMap contents are 'translated' can also be specified in the subclass as a Values array qualifier.

    
    **Parameters**
    
*None*
    .. _CIM-LogicalDevice-RestoreProperties:

``uint32`` **RestoreProperties** ()

    Note: The use of this method is deprecated. Its function is handled more generally by the ConfigurationData subclass of SettingData. 

    Requests that the Device re-establish its configuration, setup or state information, or both from a backing store. The information would have been captured at an earlier time (using the SaveProperties method). This method might not be supported by all Devices. The method should return 0 if successful, 1 if the request is not supported, and some other value if any other error occurred. In a subclass, the set of possible return codes could be specified using a ValueMap qualifier on the method. The strings to which the ValueMap contents are 'translated' can also be specified in the subclass as a Values array qualifier.

    
    **Parameters**
    
*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`

