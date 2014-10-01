.. _CIM-PowerManagementCapabilities:

CIM_PowerManagementCapabilities
-------------------------------

Class reference
===============
Subclass of :ref:`CIM_Capabilities <CIM-Capabilities>`

A class derived from Capabilities that describes the power management aspects of an element (typically a system or device). The element's power management capabilities are decoupled from a PowerManagementService, since a single service could apply to multiple elements, each with specific capabilities.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-PowerManagementCapabilities-OtherPowerChangeCapabilities:

``string`` **OtherPowerChangeCapabilities**

    A string describing the additional power management capabilities of the element, used when the PowerChangeCapabilities is set to the value 1, "Other".

    
.. _CIM-PowerManagementCapabilities-OtherPowerCapabilitiesDescriptions:

``string[]`` **OtherPowerCapabilitiesDescriptions**

    An array of strings describing an element's additional power management capabilities, used when the PowerCapabilities array includes the value 1, "Other".

    
.. _CIM-PowerManagementCapabilities-RequestedPowerStatesSupported:

``uint16[]`` **RequestedPowerStatesSupported**

    An enumeration that indicates the requested power states supported by the power management service. Because this is an array, multiple values can be specified. The current values in the enumeration are: 

    2=On, corresponding to ACPI state G0 or S0 or D0. 

    3=Sleep - Light, corresponding to ACPI state G1, S1/S2, or D1. 

    4=Sleep - Deep, corresponding to ACPI state G1, S3, or D2.

    5=Power Cycle (Off - Soft), corresponding to ACPI state G2, S5, or D3, but where the managed element is set to return to power state "On" at a pre-determined time. 

    6=Off - Hard, corresponding to ACPI state G3, S5, or D3. 

    7=Hibernate (Off - Soft), corresponding to ACPI state S4, where the state of the managed element is preserved and will be recovered upon powering on. 

    8=Off - Soft, corresponding to ACPI state G2, S5, or D3. 9= Power Cycle (Off-Hard), corresponds to the managed element reaching the ACPI state G3 followed by ACPI state S0. 

    10=Master Bus Reset, corresponds to the system reaching ACPI state S5 followed by ACPI state S0. This is used to represent system master bus reset. 11=Diagnostic Interrupt (NMI), corresponding to the system reaching ACPI state S5 followed by ACPI state S0. This is used to represent system non-maskable interrupt. 12=Off - Soft Graceful, equivalent to Off Soft but preceded by a request to the managed element to perform an orderlyshutdown. 

    13=Off - Hard Graceful, equivalent to Off Hard but preceded by a request to the managed element to perform an orderly shutdown. 

    14=Master Bus Rest Graceful, equivalent to Master Bus Reset but preceded by a request to the managed element to perform an orderly shutdown. 

    15=Power Cycle (Off - Soft Graceful), equivalent to Power Cycle (Off - Soft) but preceded by a request to the managed element to perform an orderly shutdown. 

    16=Power Cycle (Off - Hard Graceful), equivalent to Power Cycle (Off - Hard) but preceded by a request to the managed element to perform an orderly shutdown. 

    17=Diagnostic Interrupt (INIT), equivalent to Diagnostic Interrupt (NMI) but performed by an INIT switch instead because the NMI signal is masked. 

    ..=DMTF Reserved. 

    0x7FFF..0xFFFF = Vendor Specific.

    
    ============== =================================
    ValueMap       Values                           
    ============== =================================
    1              Other                            
    2              On                               
    3              Sleep - Light                    
    4              Sleep -Deep                      
    5              Power Cycle (Off - Soft)         
    6              Off - Hard                       
    7              Hibernate (Off - Soft)           
    8              Off - Soft                       
    9              Power Cycle (Off-Hard)           
    10             Master Bus Reset                 
    11             Diagnostic Interrupt (NMI)       
    12             Off - Soft Graceful              
    13             Off - Hard Graceful              
    14             Master Bus Reset Graceful        
    15             Power Cycle (Off - Soft Graceful)
    16             Power Cycle (Off - Hard Graceful)
    17             Diagnostic Interrupt (INIT)      
    ..             DMTF Reserved                    
    0x7FFF..0xFFFF Vendor Specific                  
    ============== =================================
    
.. _CIM-PowerManagementCapabilities-PowerChangeCapabilities:

``uint16[]`` **PowerChangeCapabilities**

    An enumeration indicating the specific power-related capabilities of a managed element. Since this is an array, multiple values may be specified. The current values in the enumeration are: 

    0 = Unknown 

    1 = Other 

    2 = Power Saving Modes Entered Automatically, describing that a managed element can change its power state based on usage or other criteria 

    3 = Power State Settable, indicating that the RequestPowerStateChange method is supported 

    4 = Power Cycling Supported, indicating that the RequestPowerStateChange method can be invoked with the PowerState input variable set to 'Power Cycle (Off Soft)' 

    5 = Timed Power On Supported, indicating that the RequestPowerStateChange method can be invoked with the PowerState input variable set to 'Power On' and the Time parameter set to a specific date and time, or interval, for power-on.8 = Graceful Shutdown Supported, indicating that the managed element can be sent a hardware signal requesting an orderly shutdown prior to the requested power state change.

    
    ======== ========================================
    ValueMap Values                                  
    ======== ========================================
    0        Unknown                                 
    1        Other                                   
    2        Power Saving Modes Entered Automatically
    3        Power State Settable                    
    4        Power Cycling Supported                 
    5        Timed Power On Supported                
    6        Off Hard Power Cycling Supported        
    7        HW Reset Supported                      
    8        Graceful Shutdown Supported             
    ======== ========================================
    
.. _CIM-PowerManagementCapabilities-PowerCapabilities:

``uint16[]`` **PowerCapabilities**

    An enumeration indicating the specific power-related capabilities of a managed element. Since this is an array, multiple values may be specified. The current values in the enumeration are: 

    0 = Unknown 

    1 = Other 

    2 = Power Saving Modes Entered Automatically, describing that a managed element can change its power state based on usage or other criteria 

    3 = Power State Settable, indicating that the SetPowerState method is supported 

    4 = Power Cycling Supported, indicating that the SetPowerState method can be invoked with the PowerState input variable set to 'Power Cycle' 

    5 = Timed Power On Supported, indicating that the SetPowerState method can be invoked with the PowerState input variable set to 'Power Cycle' and the Time parameter set to a specific date and time, or interval, for power-on.

    
    ======== ========================================
    ValueMap Values                                  
    ======== ========================================
    0        Unknown                                 
    1        Other                                   
    2        Power Saving Modes Entered Automatically
    3        Power State Settable                    
    4        Power Cycling Supported                 
    5        Timed Power On Supported                
    ======== ========================================
    
.. _CIM-PowerManagementCapabilities-PowerStatesSupported:

``uint16[]`` **PowerStatesSupported**

    An enumeration that indicates the power states supported by a managed element. Because this is an array, multiple values can be specified. The current values in the enumeration are: 

    2=On, corresponding to ACPI state G0 or S0 or D0. 

    3=Sleep - Light, corresponding to ACPI state G1, S1/S2, or D1. 

    4=Sleep - Deep, corresponding to ACPI state G1, S3, or D2.

    5=Power Cycle (Off - Soft), corresponding to ACPI state G2, S5, or D3, but where the managed element is set to return to power state "On" at a pre-determined time. 

    6=Off - Hard, corresponding to ACPI state G3, S5, or D3. 

    7=Hibernate (Off - Soft), corresponding to ACPI state S4, where the state of the managed element is preserved and will be recovered upon powering on. 

    8=Off - Soft, corresponding to ACPI state G2, S5, or D3. 9= Power Cycle (Off-Hard), corresponds to the managed element reaching the ACPI state G3 followed by ACPI state S0. 

    10=Master Bus Reset, corresponds to the system reaching ACPI state S5 followed by ACPI state S0. This is used to represent system master bus reset. 11=Diagnostic Interrupt (NMI), corresponding to the system reaching ACPI state S5 followed by ACPI state S0. This is used to represent system non-maskable interrupt. 12=Off - Soft Graceful, equivalent to Off Soft but preceded by a request to the managed element to perform an orderlyshutdown. 

    13=Off - Hard Graceful, equivalent to Off Hard but preceded by a request to the managed element to perform an orderly shutdown. 

    14=Master Bus Rest Graceful, equivalent to Master Bus Reset but preceded by a request to the managed element to perform an orderly shutdown. 

    15=Power Cycle (Off - Soft Graceful), equivalent to Power Cycle (Off - Soft) but preceded by a request to the managed element to perform an orderly shutdown. 

    16=Power Cycle (Off - Hard Graceful), equivalent to Power Cycle (Off - Hard) but preceded by a request to the managed element to perform an orderly shutdown. 

    ..=DMTF Reserved. 

    0x7FFF..0xFFFF = Vendor Specific.

    
    ============== =================================
    ValueMap       Values                           
    ============== =================================
    1              Other                            
    2              On                               
    3              Sleep - Light                    
    4              Sleep -Deep                      
    5              Power Cycle (Off - Soft)         
    6              Off - Hard                       
    7              Hibernate (Off - Soft)           
    8              Off - Soft                       
    9              Power Cycle (Off-Hard)           
    10             Master Bus Reset                 
    11             Diagnostic Interrupt (NMI)       
    12             Off - Soft Graceful              
    13             Off - Hard Graceful              
    14             Master Bus Reset Graceful        
    15             Power Cycle (Off - Soft Graceful)
    16             Power Cycle (Off - Hard Graceful)
    ..             DMTF Reserved                    
    0x7FFF..0xFFFF Vendor Specific                  
    ============== =================================
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`ElementName <CIM-Capabilities-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`InstanceID <CIM-Capabilities-InstanceID>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`CreateGoalSettings <CIM-Capabilities-CreateGoalSettings>`

