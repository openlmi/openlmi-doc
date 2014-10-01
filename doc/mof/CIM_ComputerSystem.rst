.. _CIM-ComputerSystem:

CIM_ComputerSystem
------------------

Class reference
===============
Subclass of :ref:`CIM_System <CIM-System>`

A class derived from System that is a special collection of ManagedSystemElements. This collection is related to the providing of compute capabilities and MAY serve as an aggregation point to associate one or more of the following elements: FileSystem, OperatingSystem, Processor and Memory (Volatile and/or NonVolatile Storage).


Key properties
^^^^^^^^^^^^^^

| :ref:`Name <CIM-System-Name>`
| :ref:`CreationClassName <CIM-System-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-ComputerSystem-NameFormat:

``string`` **NameFormat**

    The ComputerSystem object and its derivatives are Top Level Objects of CIM. They provide the scope for numerous components. Having unique System keys is required. The NameFormat property identifies how the ComputerSystem Name is generated. The NameFormat ValueMap qualifier defines the various mechanisms for assigning the name. Note that another name can be assigned and used for the ComputerSystem that better suit a business, using the inherited ElementName property.

    If the NameFormat is set to "UUID", then the Name property shall be a UUID in its canonical form consisting of 32 hexadecimal digits in 5 groups separated by hyphens, in the form 8-4-4-4-12 for a total of 36 characters (32 digits and 4 hyphens). For the first three fields, the most significant digit is on the left. The last two fields are treated as eight separate bytes, each having their most significant digit on the left, and they follow each other from left to right.

    
.. _CIM-ComputerSystem-OtherDedicatedDescriptions:

``string[]`` **OtherDedicatedDescriptions**

    A string describing how or why the system is dedicated when the Dedicated array includes the value 2, "Other".

    
.. _CIM-ComputerSystem-ResetCapability:

``uint16`` **ResetCapability**

    If enabled (value = 4), the ComputerSystem can be reset via hardware (e.g. the power and reset buttons). If disabled (value = 3), hardware reset is not allowed. In addition to Enabled and Disabled, other Values for the property are also defined - "Not Implemented" (5), "Other" (1) and "Unknown" (2).

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    1        Other          
    2        Unknown        
    3        Disabled       
    4        Enabled        
    5        Not Implemented
    ======== ===============
    
.. _CIM-ComputerSystem-PowerManagementCapabilities:

``uint16[]`` **PowerManagementCapabilities**

    **Deprecated!** 
    An enumerated array describing the power management capabilities of the ComputerSystem. The use of this property has been deprecated. Instead, the Power Capabilites property in an associated PowerManagement Capabilities class should be used.

    
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
    
.. _CIM-ComputerSystem-Dedicated:

``uint16[]`` **Dedicated**

    Enumeration indicating the purpose(s) to which the ComputerSystem is dedicated, if any, and what functionality is provided. For example, one could specify that the System is dedicated to "Print" (value=11) or acts as a "Hub" (value=8). 

    Also, one could indicate that this is a general purpose system by indicating 'Not Dedicated' (value=0) but that it also hosts 'Print' (value=11) or mobile phone 'Mobile User Device' (value=17) services. 

    A clarification is needed with respect to the value 17 ("Mobile User Device"). An example of a dedicated user device is a mobile phone or a barcode scanner in a store that communicates via radio frequency. These systems are quite limited in functionality and programmability, and are not considered 'general purpose' computing platforms. Alternately, an example of a mobile system that is 'general purpose' (i.e., is NOT dedicated) is a hand-held computer. Although limited in its programmability, new software can be downloaded and its functionality expanded by the user. 

    A value of "Management" indicates this instance is dedicated to hosting system management software.

    A value of "Management Controller" indicates this instance represents specialized hardware dedicated to systems management (i.e., a Baseboard Management Controller (BMC) or service processor).

    The management scope of a "Management Controller" is typically a single managed system in which it is contained.

    A value of "Chassis Manager" indicates this instance represents a system dedicated to management of a blade chassis and its contained devices. This value would be used to represent a Shelf Controller. A "Chassis Manager" is an aggregation point for management and may rely on subordinate management controllers for the management of constituent parts. A value of "Host-based RAID Controller" indicates this instance represents a RAID storage controller contained within a host computer. A value of "Storage Device Enclosure" indicates this instance represents an enclosure that contains storage devices. A "Virtual Tape Library" is the emulation of a tape library by a Virtual Library System. A "Virtual Library System" uses disk storage to emulate tape libraries.A "FC Switch" indicates this instance is dedicated to switching layer 2 fibre channel frames. An "Ethernet Switch" indicates this instance is dedicated to switching layer 2 ethernet frames.

    "Server" indicates that the system is an independent computer system whose primary purpose is to host services for other systems and devices to access; typically as in a stand-alone floor or rack-mounted system.

    "Blade" indicates this instance is a computer system that fits into another chassis and depends on it for services, such as power, cooling, etc.

    
    ============ ==========================
    ValueMap     Values                    
    ============ ==========================
    0            Not Dedicated             
    1            Unknown                   
    2            Other                     
    3            Storage                   
    4            Router                    
    5            Switch                    
    6            Layer 3 Switch            
    7            Central Office Switch     
    8            Hub                       
    9            Access Server             
    10           Firewall                  
    11           Print                     
    12           I/O                       
    13           Web Caching               
    14           Management                
    15           Block Server              
    16           File Server               
    17           Mobile User Device        
    18           Repeater                  
    19           Bridge/Extender           
    20           Gateway                   
    21           Storage Virtualizer       
    22           Media Library             
    23           ExtenderNode              
    24           NAS Head                  
    25           Self-contained NAS        
    26           UPS                       
    27           IP Phone                  
    28           Management Controller     
    29           Chassis Manager           
    30           Host-based RAID controller
    31           Storage Device Enclosure  
    32           Desktop                   
    33           Laptop                    
    34           Virtual Tape Library      
    35           Virtual Library System    
    36           Network PC/Thin Client    
    37           FC Switch                 
    38           Ethernet Switch           
    39           Server                    
    40           Blade                     
    ..           DMTF Reserved             
    32568..65535 Vendor Reserved           
    ============ ==========================
    

Local methods
^^^^^^^^^^^^^

    .. _CIM-ComputerSystem-SetPowerState:

``uint32`` **SetPowerState** (``uint32`` PowerState, ``datetime`` Time)

    Sets the power state of the computer. The use of this method has been deprecated. Instead, use the SetPowerState method in the associated PowerManagementService class.

    
    **Parameters**
    
        *IN* ``uint32`` **PowerState**
            The Desired state for the COmputerSystem.

            
            ======== ===========================
            ValueMap Values                     
            ======== ===========================
            1        Full Power                 
            2        Power Save - Low Power Mode
            3        Power Save - Standby       
            4        Power Save - Other         
            5        Power Cycle                
            6        Power Off                  
            7        Hibernate                  
            8        Soft Off                   
            ======== ===========================
            
        
        *IN* ``datetime`` **Time**
            Time indicates when the power state should be set, either as a regular date-time value or as an interval value (where the interval begins when the method invocation is received.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``string[]`` :ref:`IdentifyingDescriptions <CIM-System-IdentifyingDescriptions>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string[]`` :ref:`OtherIdentifyingInfo <CIM-System-OtherIdentifyingInfo>`
| ``string`` :ref:`Name <CIM-System-Name>`
| ``string[]`` :ref:`Roles <CIM-System-Roles>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`PrimaryOwnerContact <CIM-System-PrimaryOwnerContact>`
| ``string`` :ref:`CreationClassName <CIM-System-CreationClassName>`
| ``string`` :ref:`PrimaryOwnerName <CIM-System-PrimaryOwnerName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`

