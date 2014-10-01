.. _LMI-IPNetworkConnection:

LMI_IPNetworkConnection
-----------------------

Class reference
===============
Subclass of :ref:`CIM_IPNetworkConnection <CIM-IPNetworkConnection>`

LMI_IPNetworkConnection represents the IP network connection in the system, Eg. "Local Area Connection","eth0"


Key properties
^^^^^^^^^^^^^^

| :ref:`CreationClassName <CIM-ServiceAccessPoint-CreationClassName>`
| :ref:`SystemName <CIM-ServiceAccessPoint-SystemName>`
| :ref:`Name <CIM-ServiceAccessPoint-Name>`
| :ref:`SystemCreationClassName <CIM-ServiceAccessPoint-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-IPNetworkConnection-ElementName:

``string`` **ElementName**

    Human readable device name

    
.. _LMI-IPNetworkConnection-OperatingStatus:

``uint16`` **OperatingStatus**

    OperatingStatus provides a current status value for the operational condition of the element. It can also provide the transitional states when an element is transitioning from one state to another.

    OperatingStatus consists of one of the following values: Unknown, Not Available, Starting, Stopping, Stopped, Aborted, Dormant, In Service

    - ``Unknown`` indicates the implementation is in general capable of returning this property, but is unable to do so at this time.

    - ``Not Available`` indicates that the device is recognized, but not managed by implementation

    - ``Starting`` describes an element being initialized. 

    - ``Stopping`` describes an element being brought to an orderly stop.

    - ``Stopped`` describes an element can be activate, but is currently idle

    - ``Aborted`` indicates that the element is unable to complete requested action (usually activate the connection).

    - ``Dormant`` indicates that the element is not available to use. Reasons might include the wireless switched off, missing firmware, no ethernet carrier, missing supplicant or modem manager, etc.

    - ``In Service`` describes an element that is in service and operational.

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Unknown      
    1        Not Available
    3        Starting     
    4        Stopping     
    5        Stopped      
    6        Aborted      
    7        Dormant      
    16       In Service   
    ======== =============
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`SystemName <CIM-ServiceAccessPoint-SystemName>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`Name <CIM-ServiceAccessPoint-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`ID <CIM-IPNetworkConnection-ID>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``string`` :ref:`CreationClassName <CIM-ServiceAccessPoint-CreationClassName>`
| ``string`` :ref:`SystemCreationClassName <CIM-ServiceAccessPoint-SystemCreationClassName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`

