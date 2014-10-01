.. _LMI-NetworkRemoteServiceAccessPoint:

LMI_NetworkRemoteServiceAccessPoint
-----------------------------------

Class reference
===============
Subclass of :ref:`CIM_RemoteServiceAccessPoint <CIM-RemoteServiceAccessPoint>`

RemoteServiceAccessPoint describes access or addressing information or a combination of this information for a remote connection that is known to a local network element. This information is scoped or contained by the local network element, because this is the context in which the connection is remote. 

The relevance of the remote access point and information on its use are described by subclassing RemoteServiceAccessPoint or by associating to it.


Key properties
^^^^^^^^^^^^^^

| :ref:`CreationClassName <CIM-ServiceAccessPoint-CreationClassName>`
| :ref:`SystemName <CIM-ServiceAccessPoint-SystemName>`
| :ref:`Name <CIM-ServiceAccessPoint-Name>`
| :ref:`SystemCreationClassName <CIM-ServiceAccessPoint-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-NetworkRemoteServiceAccessPoint-AccessInfo:

``string`` **AccessInfo**

    Access or addressing information or a combination of this information for a remote connection. This information can be a host name, network address, or similar information.

    
.. _LMI-NetworkRemoteServiceAccessPoint-AccessContext:

``uint16`` **AccessContext**

    The AccessContext property identifies the role this RemoteServiceAccessPoint is playing in the hosting system.

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    2        Default Gateway
    3        DNS Server     
    ======== ===============
    
.. _LMI-NetworkRemoteServiceAccessPoint-InfoFormat:

``uint16`` **InfoFormat**

    An enumerated integer that describes the format and interpretation of the AccessInfo property.

    
    ======== ============
    ValueMap Values      
    ======== ============
    3        IPv4 Address
    4        IPv6 Address
    ======== ============
    

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
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`OtherInfoFormatDescription <CIM-RemoteServiceAccessPoint-OtherInfoFormatDescription>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`OtherAccessContext <CIM-RemoteServiceAccessPoint-OtherAccessContext>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`CreationClassName <CIM-ServiceAccessPoint-CreationClassName>`
| ``string`` :ref:`SystemCreationClassName <CIM-ServiceAccessPoint-SystemCreationClassName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`

