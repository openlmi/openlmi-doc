.. _CIM-Battery:

CIM_Battery
-----------

Class reference
===============
Subclass of :ref:`CIM_PowerSource <CIM-PowerSource>`

Capabilities and management of the Battery. This class applies to both batteries in Laptop Systems and other internal or external batteries, such as an uninterruptible power supply (UPS).


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-Battery-BatteryStatus:

``uint16`` **BatteryStatus**

    Description of the charge status of the Battery. Values such as "Fully Charged" (value=3) or "Partially Charged" (value=11) can be specified. The value, 10, is not valid in the CIM Schema because in DMI it represents that no battery is installed. In this case, this object should not be instantiated. The valuemaps: 6(Charging), 7(Charging and High), 8(Charging and Low), and 9(Charing and Critical) has been deprecated in lieu of the ChargingStatus property. 10(Undefined) has been deprecated in lieu of 2(Unknown).

    
    ============ =====================
    ValueMap     Values               
    ============ =====================
    1            Other                
    2            Unknown              
    3            Fully Charged        
    4            Low                  
    5            Critical             
    6            Charging             
    7            Charging and High    
    8            Charging and Low     
    9            Charging and Critical
    10           Undefined            
    11           Partially Charged    
    12           Learning             
    13           Overcharged          
    ..           DMTF Reserved        
    32768..65535 Vendor Specific      
    ============ =====================
    
.. _CIM-Battery-OtherChemistryDescription:

``string`` **OtherChemistryDescription**

    The description of the battery chemistry when the Chemistry property has value 1 (Other). The property shall be implemented if the Chemistry property has value 1(Other).

    
.. _CIM-Battery-DesignCapacity:

``uint32`` **DesignCapacity**

    The design capacity of the battery in mWatt-hours. If this property is not supported, enter 0.

    
.. _CIM-Battery-MaxRechargeTime:

``uint32`` **MaxRechargeTime**

    MaxRechargeTime indicates the maximum time, in minutes, to fully charge the Battery. This property represents the time to recharge a fully depleted Battery, not the current remaining charging time, which is indicated in the TimeToFullCharge property.

    
.. _CIM-Battery-RemainingCapacityMaxError:

``uint8`` **RemainingCapacityMaxError**

    The maximum error (as a percentage) in the mWatt-hour data reported by RemainingCapacity property.

    
.. _CIM-Battery-PermanentErrorInfo:

``uint16`` **PermanentErrorInfo**

    An enumeration that describes the error information in the event of permanent failure of the battery. This code will enable system administrators to troubleshoot the reason behind failed batteries. Unknown value means a permanent error has occured but the error type is unknown.

    
    ============ =========================
    ValueMap     Values                   
    ============ =========================
    0            Unknown                  
    2            No Failure               
    3            Fuse Blown               
    4            Cell imbalance           
    5            Over voltage             
    6            FET inoperative          
    7            Communication error      
    8            Incompatible battery type
    ..           DMTF Reserved            
    32768..65535 Vendor Reserved          
    ============ =========================
    
.. _CIM-Battery-TimeToFullCharge:

``uint32`` **TimeToFullCharge**

    The remaining time in minutes to charge the battery fully at the current charging rate and usage.

    
.. _CIM-Battery-MaxRechargeCount:

``uint32`` **MaxRechargeCount**

    The maximum number of times the Battery can be recharged.

    
.. _CIM-Battery-RemainingCapacity:

``uint32`` **RemainingCapacity**

    The Battery's remaining charge capacity in mWatt-hours.

    
.. _CIM-Battery-ChargingStatus:

``uint16`` **ChargingStatus**

    ChargingStatus indicates whether the battery is charging. Charging - the battery is charging. Discharging - the battery is discharging. Idle - the batter is neither charging nor discharging.

    
    ============ ================
    ValueMap     Values          
    ============ ================
    0            Unknown         
    2            Charging        
    3            Discharging     
    4            Idle            
    ..           DMTF Reserved   
    32768..65535 Vendor Specified
    ============ ================
    
.. _CIM-Battery-TimeOnBattery:

``uint32`` **TimeOnBattery**

    TimeOnBattery indicates the elapsed time in seconds since the ComputerSystem, UPS, or so on, last switched to battery power, or the time since the System or UPS was last restarted, whichever is less. Zero is returned if the Battery is 'on line'.

    
.. _CIM-Battery-DesignVoltage:

``uint64`` **DesignVoltage**

    The design voltage of the battery in mVolts. If this attribute is not supported, enter 0.

    
.. _CIM-Battery-EstimatedChargeRemaining:

``uint16`` **EstimatedChargeRemaining**

    An estimate of the percentage of full charge remaining.

    
.. _CIM-Battery-SmartBatteryVersion:

``string`` **SmartBatteryVersion**

    The Smart Battery Data Specification version number that is supported by this Battery. If the Battery does not support this function, the value should be left blank.

    
.. _CIM-Battery-HealthPercent:

``uint8`` **HealthPercent**

    An estimate of the percentage of the overall battery health. It indicates how much the battery has deteriorated over time. It can take values 0 to 100; 255 if it is unknown.

    
.. _CIM-Battery-Chemistry:

``uint16`` **Chemistry**

    An enumeration that describes the chemistry of the Battery.

    
    ============ ====================
    ValueMap     Values              
    ============ ====================
    1            Other               
    2            Unknown             
    3            Lead Acid           
    4            Nickel Cadmium      
    5            Nickel Metal Hydride
    6            Lithium-ion         
    7            Zinc air            
    8            Lithium Polymer     
    ..           DMTF Reserved       
    32768..65535 Vendor Specified    
    ============ ====================
    
.. _CIM-Battery-ExpectedLife:

``uint32`` **ExpectedLife**

    Indicates the expected lifetime of the Battery in minutes, assuming that the Battery is fully charged. This property represents the total expected life of the Battery, not its current remaining life, which is indicated by the EstimatedRunTime property.

    
.. _CIM-Battery-RechargeCount:

``uint32`` **RechargeCount**

    The number of times the Battery has been recharged.

    
.. _CIM-Battery-EstimatedRunTime:

``uint32`` **EstimatedRunTime**

    EstimatedRunTime is an estimate in minutes of the time that battery charge depletion will occur under the present load conditions if the utility power is off, or is lost and remains off, or a Laptop is disconnected from a power source.

    
.. _CIM-Battery-FullChargeCapacity:

``uint32`` **FullChargeCapacity**

    The full charge capacity of the battery in mWatt-hours. Comparison of this value to the Battery DesignCapacity determines when the Battery requires replacement. The end of life of a Battery is typically when the FullCharge Capacity falls below 80% of the DesignCapacity. If this property is not supported, enter 0.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``string`` :ref:`OutputPowerUnits <CIM-PowerSource-OutputPowerUnits>`
| ``string`` :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16`` :ref:`Availability <CIM-LogicalDevice-Availability>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``string[]`` :ref:`IdentifyingDescriptions <CIM-LogicalDevice-IdentifyingDescriptions>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``boolean`` :ref:`ErrorCleared <CIM-LogicalDevice-ErrorCleared>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`LocationIndicator <CIM-LogicalDevice-LocationIndicator>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string[]`` :ref:`OtherIdentifyingInfo <CIM-LogicalDevice-OtherIdentifyingInfo>`
| ``uint64`` :ref:`PowerOnHours <CIM-LogicalDevice-PowerOnHours>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16[]`` :ref:`AdditionalAvailability <CIM-LogicalDevice-AdditionalAvailability>`
| ``uint32`` :ref:`RatedMaxOutputPower <CIM-PowerSource-RatedMaxOutputPower>`
| ``uint16`` :ref:`StatusInfo <CIM-LogicalDevice-StatusInfo>`
| ``string`` :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| ``uint16[]`` :ref:`PowerManagementCapabilities <CIM-LogicalDevice-PowerManagementCapabilities>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint64`` :ref:`MaxQuiesceTime <CIM-LogicalDevice-MaxQuiesceTime>`
| ``uint64`` :ref:`TotalPowerOnHours <CIM-LogicalDevice-TotalPowerOnHours>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`ErrorDescription <CIM-LogicalDevice-ErrorDescription>`
| ``boolean`` :ref:`IsACOutput <CIM-PowerSource-IsACOutput>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint32`` :ref:`LastErrorCode <CIM-LogicalDevice-LastErrorCode>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``string`` :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
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

