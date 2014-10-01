.. _LMI-RealmdService:

LMI_RealmdService
-----------------

Class reference
===============
Subclass of :ref:`CIM_Service <CIM-Service>`

Access to the Realmd Service. Realmd is used to discover realms available for joining as well as providing a mechanism for joining and leaving a realm.


Key properties
^^^^^^^^^^^^^^

| :ref:`Name <CIM-Service-Name>`
| :ref:`SystemName <CIM-Service-SystemName>`
| :ref:`SystemCreationClassName <CIM-Service-SystemCreationClassName>`
| :ref:`CreationClassName <CIM-Service-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-RealmdService-Domain:

``string`` **Domain**

    The name of the domain that this computer is a member of or NULL if not a member of any domain.

    

Local methods
^^^^^^^^^^^^^

    .. _LMI-RealmdService-LeaveDomain:

``uint32`` **LeaveDomain** (``string`` Domain, ``string`` User, ``string`` Password, ``string[]`` OptionNames, ``string[]`` OptionValues)

    Make the computer leave its joined domain.

    
    **Parameters**
    
        *IN* ``string`` **Domain**
            The name of the domain to join.

            
        
        *IN* ``string`` **User**
            The administrative user who is authorizing joining the domain. Or NULL for a one time password based join.

            
        
        *IN* ``string`` **Password**
            Either NULL for an automatic join, a one time password, or the password for the administrative user in the User parameter.

            
        
        *IN* ``string[]`` **OptionNames**
            This array is correlated with the OptionValues array. Each entry is related to the entries in the other array located at the same index. In this way a (name,value) tuple can be constructed.

            
        
        *IN* ``string[]`` **OptionValues**
            This array is correlated with the OptionNames array. Each entry is related to the entries in the other array located at the same index. In this way a (name,value) tuple can be constructed.

            
        
    
    .. _LMI-RealmdService-JoinDomain:

``uint32`` **JoinDomain** (``string`` Domain, ``string`` User, ``string`` Password, ``string[]`` OptionNames, ``string[]`` OptionValues)

    Join the computer to a domain.

    
    **Parameters**
    
        *IN* ``string`` **Domain**
            The name of the domain to join.

            
        
        *IN* ``string`` **User**
            The administrative user who is authorizing joining the domain. Or NULL for a one time password based join.

            
        
        *IN* ``string`` **Password**
            Either NULL for an automatic join, a one time password, or the password for the administrative user in the User parameter.

            
        
        *IN* ``string[]`` **OptionNames**
            This array is correlated with the OptionValues array. Each entry is related to the entries in the other array located at the same index. In this way a (name,value) tuple can be constructed.

            
        
        *IN* ``string[]`` **OptionValues**
            This array is correlated with the OptionNames array. Each entry is related to the entries in the other array located at the same index. In this way a (name,value) tuple can be constructed.

            
        
    

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

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`
| :ref:`StopService <CIM-Service-StopService>`
| :ref:`ChangeAffectedElementsAssignedSequence <CIM-Service-ChangeAffectedElementsAssignedSequence>`
| :ref:`StartService <CIM-Service-StartService>`

