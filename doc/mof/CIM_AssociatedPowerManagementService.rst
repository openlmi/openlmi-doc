.. _CIM-AssociatedPowerManagementService:

CIM_AssociatedPowerManagementService
------------------------------------

Class reference
===============
Subclass of :ref:`CIM_ServiceAvailableToElement <CIM-ServiceAvailableToElement>`

The association between a Managed System Element and its power management service.


Key properties
^^^^^^^^^^^^^^

| :ref:`UserOfService <CIM-ServiceAvailableToElement-UserOfService>`
| :ref:`ServiceProvided <CIM-ServiceAvailableToElement-ServiceProvided>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-AssociatedPowerManagementService-TransitioningToPowerState:

``uint16`` **TransitioningToPowerState**

    TransitioningToPowerState indicates the target power state to which the system is transitioning. 

    A value of 19 "No Change" shall indicate that no transition is in progress. A value of 18 "Not Applicable" shall indicate the implementation does not support representing ongoing transitions. 

    A value other than 18 or 19 shall identify the power state to which the element is in the process of transitioning.

    
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
    18             Not Applicable                   
    19             No Change                        
    ..             DMTF Reserved                    
    0x7FFF..0xFFFF Vendor Specific                  
    ============== =================================
    
.. _CIM-AssociatedPowerManagementService-PowerState:

``uint16`` **PowerState**

    The current power state of the associated Managed System Element.

    
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
    
.. _CIM-AssociatedPowerManagementService-AvailableRequestedPowerStates:

``uint16[]`` **AvailableRequestedPowerStates**

    AvailableRequestedPowerStates indicates the possible values for the PowerState parameter of the method RequestPowerStateChange, used to initiate a power state change.The values listed shall be a subset of the values contained in the RequestedPowerStatesSupported property of the CIM_PowerManagementCapabilities where the values selected are a function of the current power state of the system. This property shall be non-null if an implementation supports the advertisement of the set of possible values as a function of the current state. This property shall be null if an implementation does not support the advertisement of the set of possible values as a function of the current state. 

    The current values in the enumeration are: 

    2=On, corresponding to ACPI state G0 or S0 or D0. 

    3=Sleep - Light, corresponding to ACPI state G1, S1/S2, or D1. 

    4=Sleep - Deep, corresponding to ACPI state G1, S3, or D2.

    5=Power Cycle (Off - Soft), corresponding to ACPI state G2, S5, or D3, but where the managed element is set to return to power state "On" at a pre-determined time. 

    6=Off - Hard, corresponding to ACPI state G3, S5, or D3. 

    7=Hibernate (Off - Soft), corresponding to ACPI state S4, where the state of the managed element is preserved and will be recovered upon powering on. 

    8=Off - Soft, corresponding to ACPI state G2, S5, or D3. 9= Power Cycle (Off-Hard), corresponds to the managed element reaching the ACPI state G3 followed by ACPI state S0. 

    10=Master Bus Reset, corresponds to the system reaching ACPI state S5 followed by ACPI state S0. This is used to represent system master bus reset. 11=Diagnostic Interrupt (NMI), corresponding to the system reaching ACPI state S5 followed by ACPI state S0. This is used to represent system non-maskable interrupt. 12=Off - Soft Graceful, equivalent to Off Soft but preceded by a request to the managed element to perform an orderly shutdown. 

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
    
.. _CIM-AssociatedPowerManagementService-PowerOnTime:

``datetime`` **PowerOnTime**

    The time when the element will be powered on again, used when the RequestedPowerState has the value 2, "On", 5, "Power Cycle (Off - Soft)" or 6, "Power Cycle (Off - Hard)".

    
.. _CIM-AssociatedPowerManagementService-OtherPowerState:

``string`` **OtherPowerState**

    A string describing the additional power management state of the element, used when the PowerState is set to the value 1, "Other".

    
.. _CIM-AssociatedPowerManagementService-RequestedPowerState:

``uint16`` **RequestedPowerState**

    The desired or the last requested power state of the associated Managed System Element, irrespective of the mechanism through which the request was made. If the requested power state is unknown, then the property shall have the value of 0 ("Unknown"). If the property has no meaning or is not supported, then the property shall have value 12("Not Applicable").

    
    ============== =================================
    ValueMap       Values                           
    ============== =================================
    0              Unknown                          
    1              Other                            
    2              On                               
    3              Sleep - Light                    
    4              Sleep -_Deep                     
    5              Power Cycle (Off - Soft)         
    6              Off - Hard                       
    7              Hibernate (Off - Soft)           
    8              Off - Soft                       
    9              Power Cycle (Off-Hard)           
    10             Master Bus Reset                 
    11             Diagnostic Interrupt (NMI)       
    12             Not Applicable                   
    13             Off - Soft Graceful              
    14             Off - Hard Graceful              
    15             Master Bus Reset Graceful        
    16             Power Cycle (Off - Soft Graceful)
    17             Power Cycle (Off - Hard Graceful)
    18             Diagnostic Interrupt (INIT)      
    ..             DMTF Reserved                    
    0x7FFF..0xFFFF Vendor Specific                  
    ============== =================================
    
.. _CIM-AssociatedPowerManagementService-OtherRequestedPowerState:

``string`` **OtherRequestedPowerState**

    A string describing the additional power management state of the element, used when the RequestedPowerState is set to the value 1, "Other".

    
.. _CIM-AssociatedPowerManagementService-ServiceProvided:

:ref:`CIM_PowerManagementService <CIM-PowerManagementService>` **ServiceProvided**

    The Service that is available.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| :ref:`CIM_ManagedElement <CIM-ManagedElement>` :ref:`UserOfService <CIM-ServiceAvailableToElement-UserOfService>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

