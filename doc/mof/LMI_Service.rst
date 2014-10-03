.. _LMI-Service:

LMI_Service
-----------

Class reference
===============
Subclass of :ref:`CIM_Service <CIM-Service>`

Class representing Linux Service


Key properties
^^^^^^^^^^^^^^

| :ref:`Name <CIM-Service-Name>`
| :ref:`SystemName <CIM-Service-SystemName>`
| :ref:`SystemCreationClassName <CIM-Service-SystemCreationClassName>`
| :ref:`CreationClassName <CIM-Service-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

*None*

Local methods
^^^^^^^^^^^^^

    .. _LMI-Service-ReloadOrRestartService:

``uint32`` **ReloadOrRestartService** ()

    Reload the service if it supports it. If not, restart the service instead. If the service is not running yet, it will be started.

    
    **Parameters**
    
*None*
    .. _LMI-Service-ReloadService:

``uint32`` **ReloadService** ()

    Reload configuration of the service.

    
    **Parameters**
    
*None*
    .. _LMI-Service-StopService:

``uint32`` **StopService** ()

    Stop (deactivate) the service.

    
    **Parameters**
    
*None*
    .. _LMI-Service-TurnServiceOn:

``uint32`` **TurnServiceOn** ()

    Enable the service persistently. The service will start on the next boot of the system. Note that this method does not have the effect of also starting the service being enabled. If this is desired, a separate StartService method call must be invoked for the service.

    
    **Parameters**
    
*None*
    .. _LMI-Service-TurnServiceOff:

``uint32`` **TurnServiceOff** ()

    Disable the service. The service will not start on the next boot of the system. Note that this method does not implicitly stop the service that is being disabled. If this is desired, an additional StopService method call command should be executed afterwards.

    
    **Parameters**
    
*None*
    .. _LMI-Service-TryRestartService:

``uint32`` **TryRestartService** ()

    Restart the service if the service is running. This does nothing if the service is not running.

    
    **Parameters**
    
*None*
    .. _LMI-Service-ReloadOrTryRestartService:

``uint32`` **ReloadOrTryRestartService** ()

    Reload the service if it supports it. If not, restart the service instead. This does nothing if the service is not running.

    
    **Parameters**
    
*None*
    .. _LMI-Service-StartService:

``uint32`` **StartService** ()

    Start (activate) the service.

    
    **Parameters**
    
*None*
    .. _LMI-Service-CondRestartService:

``uint32`` **CondRestartService** ()

    Equivalent to the TryRestartService() method.

    
    **Parameters**
    
*None*
    .. _LMI-Service-RestartService:

``uint32`` **RestartService** ()

    Restart the service. If the service is not running yet, it will be started.

    
    **Parameters**
    
*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`SystemName <CIM-Service-SystemName>`
| ``string`` :ref:`LoSID <CIM-Service-LoSID>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``boolean`` :ref:`Started <CIM-Service-Started>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`Name <CIM-Service-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``string`` :ref:`LoSOrgID <CIM-Service-LoSOrgID>`
| ``string`` :ref:`PrimaryOwnerContact <CIM-Service-PrimaryOwnerContact>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`StartMode <CIM-Service-StartMode>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`SystemCreationClassName <CIM-Service-SystemCreationClassName>`
| ``string`` :ref:`CreationClassName <CIM-Service-CreationClassName>`
| ``string`` :ref:`PrimaryOwnerName <CIM-Service-PrimaryOwnerName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`ChangeAffectedElementsAssignedSequence <CIM-Service-ChangeAffectedElementsAssignedSequence>`
| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`

