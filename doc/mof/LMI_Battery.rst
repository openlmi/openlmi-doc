.. _LMI-Battery:

LMI_Battery
-----------

Class reference
===============
Subclass of :ref:`CIM_Battery <CIM-Battery>`

Capabilities and management of the Battery. This class applies to both batteries in Laptop Systems and other internal or external batteries, such as an uninterruptible power supply (UPS).


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-Battery-BatteryStatus:

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
    
.. _LMI-Battery-Capacity:

``uint8`` **Capacity**

    Percentage of the current battery capacity.

    
.. _LMI-Battery-InstanceID:

``string`` **InstanceID**

    InstanceID is an optional property that may be used to opaquely and uniquely identify an instance of this class within the scope of the instantiating Namespace. Various subclasses of this class may override this property to make it required, or a key. Such subclasses may also modify the preferred algorithms for ensuring uniqueness that are defined below.

    To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon (:), and where <OrgID> must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness, <OrgID> must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If not null and the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance. 

    If not set to null for DMTF-defined instances, the "preferred" algorithm must be used with the <OrgID> set to CIM.

    
.. _LMI-Battery-DesignCapacity:

``uint32`` **DesignCapacity**

    The design capacity of the battery in mWatt-hours. If this property is not supported, enter 0.

    
.. _LMI-Battery-SystemName:

``string`` **SystemName**

    The System Name of the scoping system.

    
.. _LMI-Battery-ElementName:

``string`` **ElementName**

    A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. 

    Note that the Name property of ManagedSystemElement is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. Note that if there is an associated instance of CIM_EnabledLogicalElementCapabilities, restrictions on this properties may exist as defined in ElementNameMask and MaxElementNameLen properties defined in that class.

    
.. _LMI-Battery-TimeToFullCharge:

``uint32`` **TimeToFullCharge**

    The remaining time in minutes to charge the battery fully at the current charging rate and usage.

    
.. _LMI-Battery-Description:

``string`` **Description**

    The Description property provides a textual description of the object.

    
.. _LMI-Battery-RemainingCapacity:

``uint32`` **RemainingCapacity**

    The Battery's remaining charge capacity in mWatt-hours.

    
.. _LMI-Battery-ChargingStatus:

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
    
.. _LMI-Battery-Name:

``string`` **Name**

    The Name property defines the label by which the object is known. When subclassed, the Name property can be overridden to be a Key property.

    
.. _LMI-Battery-DesignVoltage:

``uint64`` **DesignVoltage**

    The design voltage of the battery in mVolts. If this attribute is not supported, enter 0.

    
.. _LMI-Battery-EstimatedChargeRemaining:

``uint16`` **EstimatedChargeRemaining**

    An estimate of the percentage of full charge remaining.

    
.. _LMI-Battery-Caption:

``string`` **Caption**

    The Caption property is a short textual description (one- line string) of the object.

    
.. _LMI-Battery-DeviceID:

``string`` **DeviceID**

    An address or other identifying information used to uniquely name the LogicalDevice.

    
.. _LMI-Battery-HealthPercent:

``uint8`` **HealthPercent**

    An estimate of the percentage of the overall battery health. It indicates how much the battery has deteriorated over time. It can take values 0 to 100; 255 if it is unknown.

    
.. _LMI-Battery-Chemistry:

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
    
.. _LMI-Battery-CreationClassName:

``string`` **CreationClassName**

    CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

    
.. _LMI-Battery-EstimatedRunTime:

``uint32`` **EstimatedRunTime**

    EstimatedRunTime is an estimate in minutes of the time that battery charge depletion will occur under the present load conditions if the utility power is off, or is lost and remains off, or a Laptop is disconnected from a power source.

    
.. _LMI-Battery-FullChargeCapacity:

``uint32`` **FullChargeCapacity**

    The full charge capacity of the battery in mWatt-hours. Comparison of this value to the Battery DesignCapacity determines when the Battery requires replacement. The end of life of a Battery is typically when the FullCharge Capacity falls below 80% of the DesignCapacity. If this property is not supported, enter 0.

    
.. _LMI-Battery-SystemCreationClassName:

``string`` **SystemCreationClassName**

    The CreationClassName of the scoping system.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``string`` :ref:`OutputPowerUnits <CIM-PowerSource-OutputPowerUnits>`
| ``string`` :ref:`OtherChemistryDescription <CIM-Battery-OtherChemistryDescription>`
| ``uint32`` :ref:`MaxRechargeTime <CIM-Battery-MaxRechargeTime>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint8`` :ref:`RemainingCapacityMaxError <CIM-Battery-RemainingCapacityMaxError>`
| ``uint16`` :ref:`PermanentErrorInfo <CIM-Battery-PermanentErrorInfo>`
| ``uint16`` :ref:`Availability <CIM-LogicalDevice-Availability>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``string[]`` :ref:`IdentifyingDescriptions <CIM-LogicalDevice-IdentifyingDescriptions>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``boolean`` :ref:`ErrorCleared <CIM-LogicalDevice-ErrorCleared>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``uint16`` :ref:`LocationIndicator <CIM-LogicalDevice-LocationIndicator>`
| ``uint32`` :ref:`MaxRechargeCount <CIM-Battery-MaxRechargeCount>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string[]`` :ref:`OtherIdentifyingInfo <CIM-LogicalDevice-OtherIdentifyingInfo>`
| ``uint32`` :ref:`TimeOnBattery <CIM-Battery-TimeOnBattery>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16[]`` :ref:`AdditionalAvailability <CIM-LogicalDevice-AdditionalAvailability>`
| ``uint32`` :ref:`RatedMaxOutputPower <CIM-PowerSource-RatedMaxOutputPower>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``uint16`` :ref:`StatusInfo <CIM-LogicalDevice-StatusInfo>`
| ``uint16[]`` :ref:`PowerManagementCapabilities <CIM-LogicalDevice-PowerManagementCapabilities>`
| ``uint64`` :ref:`PowerOnHours <CIM-LogicalDevice-PowerOnHours>`
| ``uint32`` :ref:`ExpectedLife <CIM-Battery-ExpectedLife>`
| ``uint32`` :ref:`RechargeCount <CIM-Battery-RechargeCount>`
| ``uint64`` :ref:`MaxQuiesceTime <CIM-LogicalDevice-MaxQuiesceTime>`
| ``uint64`` :ref:`TotalPowerOnHours <CIM-LogicalDevice-TotalPowerOnHours>`
| ``string`` :ref:`SmartBatteryVersion <CIM-Battery-SmartBatteryVersion>`
| ``string`` :ref:`ErrorDescription <CIM-LogicalDevice-ErrorDescription>`
| ``boolean`` :ref:`IsACOutput <CIM-PowerSource-IsACOutput>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint32`` :ref:`LastErrorCode <CIM-LogicalDevice-LastErrorCode>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`

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

