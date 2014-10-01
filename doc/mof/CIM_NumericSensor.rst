.. _CIM-NumericSensor:

CIM_NumericSensor
-----------------

Class reference
===============
Subclass of :ref:`CIM_Sensor <CIM-Sensor>`

A Numeric Sensor is capable of returning numeric readings and optionally supports thresholds settings.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-NumericSensor-SupportedThresholds:

``uint16[]`` **SupportedThresholds**

    An array representing the thresholds supported by this Sensor.

    
    ======== =========================
    ValueMap Values                   
    ======== =========================
    0        LowerThresholdNonCritical
    1        UpperThresholdNonCritical
    2        LowerThresholdCritical   
    3        UpperThresholdCritical   
    4        LowerThresholdFatal      
    5        UpperThresholdFatal      
    ======== =========================
    
.. _CIM-NumericSensor-LowerThresholdCritical:

``sint32`` **LowerThresholdCritical**

    The Sensor's threshold values specify the ranges (min and max values) for determining whether the Sensor is operating under Normal, NonCritical, Critical or Fatal conditions. If the CurrentReading is between LowerThresholdCritical and Lower ThresholdFatal, then the CurrentState is Critical.

    
.. _CIM-NumericSensor-EnabledThresholds:

``uint16[]`` **EnabledThresholds**

    An array representing the thresholds that are currently enabled for this Sensor.

    
    ======== =========================
    ValueMap Values                   
    ======== =========================
    0        LowerThresholdNonCritical
    1        UpperThresholdNonCritical
    2        LowerThresholdCritical   
    3        UpperThresholdCritical   
    4        LowerThresholdFatal      
    5        UpperThresholdFatal      
    ======== =========================
    
.. _CIM-NumericSensor-ValueFormulation:

``uint16`` **ValueFormulation**

    Indicates the method used by the sensor to produce its reading. 2 "Measured" shall indicate the value is measured directly by the sensor.

    3 "Derived" shall indicate the value is derived from other measured values that are not reported discretely by this sensor.

    
    ============ ===============
    ValueMap     Values         
    ============ ===============
    0            Unknown        
    2            Measured       
    3            Derived        
    ..           DMTF Reserved  
    32768..65535 Vendor Reserved
    ============ ===============
    
.. _CIM-NumericSensor-UnitModifier:

``sint32`` **UnitModifier**

    The unit multiplier for the values returned by this Sensor. All the values returned by this Sensor are represented in the units obtained by (BaseUnits * 10 raised to the power of the UnitModifier). For example, if BaseUnits is Volts and the Unit Modifier is -6, then the units of the values returned are MicroVolts. However, if the RateUnits property is set to a value other than "None", then the units are further qualified as rate units. In the above example, if RateUnits is set to "Per Second", then the values returned by the Sensor are in MicroVolts/Second. The units apply to all numeric properties of the Sensor, unless explicitly overridden by the Units qualifier.

    
.. _CIM-NumericSensor-MinReadable:

``sint32`` **MinReadable**

    MinReadable indicates the smallest value of the measured property that can be read by the NumericSensor.

    
.. _CIM-NumericSensor-LowerThresholdNonCritical:

``sint32`` **LowerThresholdNonCritical**

    The Sensor's threshold values specify the ranges (min and max values) for determining whether the Sensor is operating under Normal, NonCritical, Critical or Fatal conditions. If Current Reading is between LowerThresholdNonCritical and Upper ThresholdNonCritical, then the Sensor is reporting a normal value. If CurrentReading is between LowerThresholdNonCritical and LowerThresholdCritical, then the CurrentState is NonCritical.

    
.. _CIM-NumericSensor-Tolerance:

``sint32`` **Tolerance**

    **Deprecated!** 
    This property is being deprecated in lieu of using the Resolution and Accuracy properties. 

    Indicates the tolerance of the Sensor for the measured property. Tolerance, along with Resolution and Accuracy, is used to calculate the actual value of the measured physical property. Tolerance may vary depending on whether the Device is linear over its dynamic range.

    
.. _CIM-NumericSensor-BaseUnits:

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
    
.. _CIM-NumericSensor-Accuracy:

``sint32`` **Accuracy**

    **Deprecated!** 
    Indicates the accuracy of the Sensor for the measured property. Its value is recorded as plus/minus hundredths of a percent. Accuracy, along with Resolution, is used to calculate the actual value of the measured physical property. Accuracy may vary depending on whether the Device is linear over its dynamic range.

    
.. _CIM-NumericSensor-SettableThresholds:

``uint16[]`` **SettableThresholds**

    An array representing the writable thresholds supported by Sensor.

    
    ======== =========================
    ValueMap Values                   
    ======== =========================
    0        LowerThresholdNonCritical
    1        UpperThresholdNonCritical
    2        LowerThresholdCritical   
    3        UpperThresholdCritical   
    4        LowerThresholdFatal      
    5        UpperThresholdFatal      
    ======== =========================
    
.. _CIM-NumericSensor-CurrentReading:

``sint32`` **CurrentReading**

    The current value indicated by the Sensor.

    
.. _CIM-NumericSensor-Hysteresis:

``uint32`` **Hysteresis**

    Indicates the margin built around the thresholds. This margin prevents unnecessary state changes when the Sensor reading may fluctuate very close to its thresholds. This could be due to the Sensor's tolerance/accuracy/resolution or due to environmental factors. Once a threshold is crossed, the state of the Sensor should change. However, the state should not fluctuate between the old and new states unless the Sensor's change in the reading exceeds the hysteresis value. The units for this measurement are determined by BaseUnit*UnitModifier/RateUnit.

    
.. _CIM-NumericSensor-NormalMax:

``sint32`` **NormalMax**

    NormalMax provides guidance for the user as to the normal maximum range for the NumericSensor.

    
.. _CIM-NumericSensor-LowerThresholdFatal:

``sint32`` **LowerThresholdFatal**

    The Sensor's threshold values specify the ranges (min and max values) for determining whether the Sensor is operating under Normal, NonCritical, Critical or Fatal conditions. If the CurrentReading is below LowerThresholdFatal, then the Current State is Fatal.

    
.. _CIM-NumericSensor-AccuracyUnits:

``string`` **AccuracyUnits**

    Identifies the specific units in which the accuracy is expressed. The value of this property shall be a legal value of the Programmatic Units qualifier as defined in Appendix C.1 of DSP0004 V2.4 or later where the base unit is "percent".

    
.. _CIM-NumericSensor-RateUnits:

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
    
.. _CIM-NumericSensor-NormalMin:

``sint32`` **NormalMin**

    NormalMin provides guidance for the user as to the normal minimum range for the NumericSensor.

    
.. _CIM-NumericSensor-UpperThresholdNonCritical:

``sint32`` **UpperThresholdNonCritical**

    The Sensor's threshold values specify the ranges (min and max values) for determining whether the Sensor is operating under Normal, NonCritical, Critical or Fatal conditions. If the CurrentReading is between LowerThresholdNonCritical and UpperThresholdNonCritical, then the Sensor is reporting a normal value. If the CurrentReading is between UpperThreshold NonCritical and UpperThresholdCritical, then the CurrentState is NonCritical.

    
.. _CIM-NumericSensor-UpperThresholdFatal:

``sint32`` **UpperThresholdFatal**

    The Sensor's threshold values specify the ranges (min and max values) for determining whether the Sensor is operating under Normal, NonCritical, Critical or Fatal conditions. If the CurrentReading is above UpperThresholdFatal, then the Current State is Fatal.

    
.. _CIM-NumericSensor-Resolution:

``uint32`` **Resolution**

    Resolution indicates the ability of the Sensor to resolve differences in the measured property. The units for this measurement are determined by BaseUnit*UnitModifier/RateUnit.

    
.. _CIM-NumericSensor-IsLinear:

``boolean`` **IsLinear**

    Indicates that the Sensor is linear over its dynamic range.

    
.. _CIM-NumericSensor-MaxReadable:

``sint32`` **MaxReadable**

    MaxReadable indicates the largest value of the measured property that can be read by the NumericSensor.

    
.. _CIM-NumericSensor-NominalReading:

``sint32`` **NominalReading**

    NominalReading indicates the 'normal' or expected value for the NumericSensor.

    
.. _CIM-NumericSensor-ProgrammaticAccuracy:

``uint32`` **ProgrammaticAccuracy**

    Indicates the accuracy of the Sensor for the measured property. The accuracy is expressed as the value of theProgrammaticAccuracy property in the units specified by the by the AccuracyUnits property. ProgrammaticAccuracy, along with Resolution, is used to calculate the actual value of the measured physical property. ProgrammaticAccuracy may vary depending on whether the Device is linear over its dynamic range.

    
.. _CIM-NumericSensor-UpperThresholdCritical:

``sint32`` **UpperThresholdCritical**

    The Sensor's threshold values specify the ranges (min and max values) for determining whether the Sensor is operating under Normal, NonCritical, Critical or Fatal conditions. If the CurrentReading is between UpperThresholdCritical and Upper ThresholdFatal, then the CurrentState is Critical.

    

Local methods
^^^^^^^^^^^^^

    .. _CIM-NumericSensor-GetNonLinearFactors:

``uint32`` **GetNonLinearFactors** (``sint32`` SensorReading, ``sint32`` Accuracy, ``uint32`` Resolution, ``sint32`` Tolerance, ``uint32`` Hysteresis)

    **Deprecated!** 
    The use of this method is being deprecated, since Current senor reading can be retrieved through the GetInstance operation. 

    For a non-linear Sensor, the resolution, accuracy, tolerance and hysteresis vary as the current reading moves. This method can be used to get these factors for a given reading. It returns 0 if successful, 1 if unsupported, and any other value if an error occurred. In a subclass, the set of possible return codes could be specified, using a ValueMap qualifier on the method. The strings to which the ValueMap contents are 'translated' may also be specified in the subclass as a Values array qualifier.

    
    **Parameters**
    
        *IN* ``sint32`` **SensorReading**
            The sensor reading to get information for.

            
        
        *OUT* ``sint32`` **Accuracy**
            The accuracy of the reading.

            
        
        *OUT* ``uint32`` **Resolution**
            The resolution of the reading.

            
        
        *OUT* ``sint32`` **Tolerance**
            The tolerance of the reading.

            
        
        *OUT* ``uint32`` **Hysteresis**
            The Hysteresis of the reading.

            
        
    
    .. _CIM-NumericSensor-RestoreDefaultThresholds:

``uint32`` **RestoreDefaultThresholds** ()

    This method resets the values of the thresholds to hardware defaults. This method returns 0 if successful, 1 if unsupported and any other value if an error occurred. In a subclass, the set of possible return codes could be specified, using a ValueMap qualifier on the method. The strings to which the ValueMap contents are 'translated' may also be specified in the subclass as a Values array qualifier.

    
    **Parameters**
    
*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``string`` :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| ``uint16`` :ref:`SensorType <CIM-Sensor-SensorType>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``string`` :ref:`CurrentState <CIM-Sensor-CurrentState>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``string[]`` :ref:`IdentifyingDescriptions <CIM-LogicalDevice-IdentifyingDescriptions>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``boolean`` :ref:`ErrorCleared <CIM-LogicalDevice-ErrorCleared>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``string`` :ref:`OtherSensorTypeDescription <CIM-Sensor-OtherSensorTypeDescription>`
| ``uint16`` :ref:`LocationIndicator <CIM-LogicalDevice-LocationIndicator>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string[]`` :ref:`OtherIdentifyingInfo <CIM-LogicalDevice-OtherIdentifyingInfo>`
| ``uint64`` :ref:`PowerOnHours <CIM-LogicalDevice-PowerOnHours>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``uint16[]`` :ref:`AdditionalAvailability <CIM-LogicalDevice-AdditionalAvailability>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16`` :ref:`StatusInfo <CIM-LogicalDevice-StatusInfo>`
| ``string`` :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| ``uint16[]`` :ref:`PowerManagementCapabilities <CIM-LogicalDevice-PowerManagementCapabilities>`
| ``string[]`` :ref:`PossibleStates <CIM-Sensor-PossibleStates>`
| ``string`` :ref:`SensorContext <CIM-Sensor-SensorContext>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint64`` :ref:`PollingInterval <CIM-Sensor-PollingInterval>`
| ``uint64`` :ref:`MaxQuiesceTime <CIM-LogicalDevice-MaxQuiesceTime>`
| ``uint64`` :ref:`TotalPowerOnHours <CIM-LogicalDevice-TotalPowerOnHours>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`ErrorDescription <CIM-LogicalDevice-ErrorDescription>`
| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint32`` :ref:`LastErrorCode <CIM-LogicalDevice-LastErrorCode>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``uint16`` :ref:`Availability <CIM-LogicalDevice-Availability>`
| ``string`` :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

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

