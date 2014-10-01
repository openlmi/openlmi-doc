.. _LMI-FanSensor:

LMI_FanSensor
-------------

Class reference
===============
Subclass of :ref:`CIM_NumericSensor <CIM-NumericSensor>`

A Numeric Sensor is capable of returning numeric readings and optionally supports thresholds settings.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-FanSensor-HealthState:

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
    
.. _LMI-FanSensor-StatusDescriptions:

``string[]`` **StatusDescriptions**

    Strings describing the various OperationalStatus array values. For example, if "Stopping" is the value assigned to OperationalStatus, then this property may contain an explanation as to why an object is being stopped. Note that entries in this array are correlated with those at the same array index in OperationalStatus.

    
.. _LMI-FanSensor-CurrentReading:

``sint32`` **CurrentReading**

    The current value indicated by the Sensor.

    
.. _LMI-FanSensor-UnitModifier:

``sint32`` **UnitModifier**

    The unit multiplier for the values returned by this Sensor. All the values returned by this Sensor are represented in the units obtained by (BaseUnits * 10 raised to the power of the UnitModifier). For example, if BaseUnits is Volts and the Unit Modifier is -6, then the units of the values returned are MicroVolts. However, if the RateUnits property is set to a value other than "None", then the units are further qualified as rate units. In the above example, if RateUnits is set to "Per Second", then the values returned by the Sensor are in MicroVolts/Second. The units apply to all numeric properties of the Sensor, unless explicitly overridden by the Units qualifier.

    
.. _LMI-FanSensor-MinReadable:

``sint32`` **MinReadable**

    MinReadable indicates the smallest value of the measured property that can be read by the NumericSensor.

    
.. _LMI-FanSensor-SystemName:

``string`` **SystemName**

    The System Name of the scoping system.

    
.. _LMI-FanSensor-BaseUnits:

``uint16`` **BaseUnits**

    The base unit of the values returned by this Sensor. All the values returned by this Sensor are represented in the units obtained by (BaseUnits * 10 raised to the power of the UnitModifier). For example, if BaseUnits is Volts and the UnitModifier is -6, then the units of the values returned are MicroVolts. However, if the RateUnits property is set to a value other than "None", then the units are further qualified as rate units. In the above example, if RateUnits is set to "Per Second", then the values returned by the Sensor are in MicroVolts/Second. The units apply to all numeric properties of the Sensor, unless explicitly overridden by the Units qualifier.

    
    ======== ===========================
    ValueMap Values                     
    ======== ===========================
    0        Unknown                    
    1        Other                      
    2        Degrees C                  
    3        Degrees F                  
    4        Degrees K                  
    5        Volts                      
    6        Amps                       
    7        Watts                      
    8        Joules                     
    9        Coulombs                   
    10       VA                         
    11       Nits                       
    12       Lumens                     
    13       Lux                        
    14       Candelas                   
    15       kPa                        
    16       PSI                        
    17       Newtons                    
    18       CFM                        
    19       RPM                        
    20       Hertz                      
    21       Seconds                    
    22       Minutes                    
    23       Hours                      
    24       Days                       
    25       Weeks                      
    26       Mils                       
    27       Inches                     
    28       Feet                       
    29       Cubic Inches               
    30       Cubic Feet                 
    31       Meters                     
    32       Cubic Centimeters          
    33       Cubic Meters               
    34       Liters                     
    35       Fluid Ounces               
    36       Radians                    
    37       Steradians                 
    38       Revolutions                
    39       Cycles                     
    40       Gravities                  
    41       Ounces                     
    42       Pounds                     
    43       Foot-Pounds                
    44       Ounce-Inches               
    45       Gauss                      
    46       Gilberts                   
    47       Henries                    
    48       Farads                     
    49       Ohms                       
    50       Siemens                    
    51       Moles                      
    52       Becquerels                 
    53       PPM (parts/million)        
    54       Decibels                   
    55       DbA                        
    56       DbC                        
    57       Grays                      
    58       Sieverts                   
    59       Color Temperature Degrees K
    60       Bits                       
    61       Bytes                      
    62       Words (data)               
    63       DoubleWords                
    64       QuadWords                  
    65       Percentage                 
    66       Pascals                    
    ======== ===========================
    
.. _LMI-FanSensor-ElementName:

``string`` **ElementName**

    A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. 

    Note that the Name property of ManagedSystemElement is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. Note that if there is an associated instance of CIM_EnabledLogicalElementCapabilities, restrictions on this properties may exist as defined in ElementNameMask and MaxElementNameLen properties defined in that class.

    
.. _LMI-FanSensor-Description:

``string`` **Description**

    The Description property provides a textual description of the object.

    
.. _LMI-FanSensor-IdentifyingDescriptions:

``string[]`` **IdentifyingDescriptions**

    An array of free-form strings providing explanations and details behind the entries in the OtherIdentifyingInfo array. Note that each entry of this array is related to the entry in OtherIdentifyingInfo that is located at the same index.

    
.. _LMI-FanSensor-PossibleStates:

``string[]`` **PossibleStates**

    PossibleStates enumerates the string outputs of the Sensor. For example, a "Switch" Sensor may output the states "On", or "Off". Another implementation of the Switch may output the states "Open", and "Close". Another example is a NumericSensor supporting thresholds. This Sensor can report the states like "Normal", "Upper Fatal", "Lower Non-Critical", etc. A NumericSensor that does not publish readings and thresholds, but stores this data internally, can still report its states.

    
.. _LMI-FanSensor-NormalMax:

``sint32`` **NormalMax**

    NormalMax provides guidance for the user as to the normal maximum range for the NumericSensor.

    
.. _LMI-FanSensor-OperationalStatus:

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
    
.. _LMI-FanSensor-RateUnits:

``uint16`` **RateUnits**

    Specifies if the units returned by this Sensor are rate units. All the values returned by this Sensor are represented in the units obtained by (BaseUnits * 10 raised to the power of the UnitModifier). This is true unless this property (RateUnits) has a value different than "None". For example, if BaseUnits is Volts and the UnitModifier is -6, then the units of the values returned are MicroVolts. But, if the RateUnits property is set to a value other than "None", then the units are further qualified as rate units. In the above example, if RateUnits is set to "Per Second", then the values returned by the Sensor are in MicroVolts/Second. The units apply to all numeric properties of the Sensor, unless explicitly overridden by the Units qualifier. Any implementation of CurrentReading should be qualified with either a Counter or a Gauge qualifier, depending on the characteristics of the sensor being modeled.

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    0        None           
    1        Per MicroSecond
    2        Per MilliSecond
    3        Per Second     
    4        Per Minute     
    5        Per Hour       
    6        Per Day        
    7        Per Week       
    8        Per Month      
    9        Per Year       
    ======== ===============
    
.. _LMI-FanSensor-OtherIdentifyingInfo:

``string[]`` **OtherIdentifyingInfo**

    OtherIdentifyingInfo captures data, in addition to DeviceID information, that could be used to identify a LogicalDevice. For example, you could use this property to hold the operating system's user-friendly name for the Device.

    
.. _LMI-FanSensor-Name:

``string`` **Name**

    Name of fan provided by system.

    
.. _LMI-FanSensor-NormalMin:

``sint32`` **NormalMin**

    NormalMin provides guidance for the user as to the normal minimum range for the NumericSensor.

    
.. _LMI-FanSensor-Caption:

``string`` **Caption**

    The Caption property is a short textual description (one- line string) of the object.

    
.. _LMI-FanSensor-DeviceID:

``string`` **DeviceID**

    Uniquely identifies fan. It is a composition of SysPath and Name glued with slash ('/').

    
.. _LMI-FanSensor-PrimaryStatus:

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
    
.. _LMI-FanSensor-IsLinear:

``boolean`` **IsLinear**

    Indicates that the Sensor is linear over its dynamic range.

    
.. _LMI-FanSensor-OperatingStatus:

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

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    0        Unknown        
    1        Not Available  
    2        Servicing      
    3        Starting       
    4        Stopping       
    5        Stopped        
    6        Aborted        
    7        Dormant        
    8        Completed      
    9        Migrating      
    10       Emigrating     
    11       Immigrating    
    12       Snapshotting   
    13       Shutting Down  
    14       In Test        
    15       Transitioning  
    16       In Service     
    ..       DMTF Reserved  
    0x8000.. Vendor Reserved
    ======== ===============
    
.. _LMI-FanSensor-CreationClassName:

``string`` **CreationClassName**

    CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

    
.. _LMI-FanSensor-SystemCreationClassName:

``string`` **SystemCreationClassName**

    The CreationClassName of the scoping system.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16[]`` :ref:`SupportedThresholds <CIM-NumericSensor-SupportedThresholds>`
| ``uint16`` :ref:`ValueFormulation <CIM-NumericSensor-ValueFormulation>`
| ``uint16[]`` :ref:`EnabledThresholds <CIM-NumericSensor-EnabledThresholds>`
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``uint16[]`` :ref:`PowerManagementCapabilities <CIM-LogicalDevice-PowerManagementCapabilities>`
| ``uint16`` :ref:`SensorType <CIM-Sensor-SensorType>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16[]`` :ref:`SettableThresholds <CIM-NumericSensor-SettableThresholds>`
| ``sint32`` :ref:`LowerThresholdNonCritical <CIM-NumericSensor-LowerThresholdNonCritical>`
| ``uint32`` :ref:`Hysteresis <CIM-NumericSensor-Hysteresis>`
| ``sint32`` :ref:`Tolerance <CIM-NumericSensor-Tolerance>`
| ``string`` :ref:`CurrentState <CIM-Sensor-CurrentState>`
| ``sint32`` :ref:`LowerThresholdCritical <CIM-NumericSensor-LowerThresholdCritical>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``boolean`` :ref:`ErrorCleared <CIM-LogicalDevice-ErrorCleared>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint32`` :ref:`LastErrorCode <CIM-LogicalDevice-LastErrorCode>`
| ``sint32`` :ref:`LowerThresholdFatal <CIM-NumericSensor-LowerThresholdFatal>`
| ``string`` :ref:`OtherSensorTypeDescription <CIM-Sensor-OtherSensorTypeDescription>`
| ``string`` :ref:`AccuracyUnits <CIM-NumericSensor-AccuracyUnits>`
| ``sint32`` :ref:`Accuracy <CIM-NumericSensor-Accuracy>`
| ``uint16`` :ref:`LocationIndicator <CIM-LogicalDevice-LocationIndicator>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``uint16[]`` :ref:`AdditionalAvailability <CIM-LogicalDevice-AdditionalAvailability>`
| ``sint32`` :ref:`UpperThresholdNonCritical <CIM-NumericSensor-UpperThresholdNonCritical>`
| ``sint32`` :ref:`UpperThresholdFatal <CIM-NumericSensor-UpperThresholdFatal>`
| ``uint16`` :ref:`StatusInfo <CIM-LogicalDevice-StatusInfo>`
| ``uint32`` :ref:`ProgrammaticAccuracy <CIM-NumericSensor-ProgrammaticAccuracy>`
| ``uint64`` :ref:`PowerOnHours <CIM-LogicalDevice-PowerOnHours>`
| ``uint32`` :ref:`Resolution <CIM-NumericSensor-Resolution>`
| ``string`` :ref:`SensorContext <CIM-Sensor-SensorContext>`
| ``uint64`` :ref:`PollingInterval <CIM-Sensor-PollingInterval>`
| ``uint64`` :ref:`MaxQuiesceTime <CIM-LogicalDevice-MaxQuiesceTime>`
| ``uint64`` :ref:`TotalPowerOnHours <CIM-LogicalDevice-TotalPowerOnHours>`
| ``string`` :ref:`ErrorDescription <CIM-LogicalDevice-ErrorDescription>`
| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``sint32`` :ref:`MaxReadable <CIM-NumericSensor-MaxReadable>`
| ``sint32`` :ref:`NominalReading <CIM-NumericSensor-NominalReading>`
| ``sint32`` :ref:`UpperThresholdCritical <CIM-NumericSensor-UpperThresholdCritical>`
| ``uint16`` :ref:`Availability <CIM-LogicalDevice-Availability>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`Reset <CIM-LogicalDevice-Reset>`
| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`
| :ref:`SetPowerState <CIM-LogicalDevice-SetPowerState>`
| :ref:`QuiesceDevice <CIM-LogicalDevice-QuiesceDevice>`
| :ref:`GetNonLinearFactors <CIM-NumericSensor-GetNonLinearFactors>`
| :ref:`EnableDevice <CIM-LogicalDevice-EnableDevice>`
| :ref:`OnlineDevice <CIM-LogicalDevice-OnlineDevice>`
| :ref:`RestoreDefaultThresholds <CIM-NumericSensor-RestoreDefaultThresholds>`
| :ref:`SaveProperties <CIM-LogicalDevice-SaveProperties>`
| :ref:`RestoreProperties <CIM-LogicalDevice-RestoreProperties>`

