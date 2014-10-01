.. _LMI-AccountManagementService:

LMI_AccountManagementService
----------------------------

Class reference
===============
Subclass of :ref:`CIM_SecurityService <CIM-SecurityService>`

LMI_AccountManagementService creates, manages, and if necessary destroys Linux Accounts on behalf of other SecurityServices.


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

    .. _LMI-AccountManagementService-CreateAccount:

``uint32`` **CreateAccount** (:ref:`CIM_ComputerSystem <CIM-ComputerSystem>` System, ``string`` Name, ``string`` GECOS, ``string`` HomeDirectory, ``boolean`` DontCreateHome, ``string`` Shell, ``uint32`` UID, ``uint32`` GID, ``boolean`` SystemAccount, ``string`` Password, ``boolean`` DontCreateGroup, ``boolean`` PasswordIsPlain, :ref:`CIM_Account <CIM-Account>` Account, :ref:`CIM_Identity[] <CIM-Identity>` Identities)

    Create a new account on the system

    
    ======== ==============================================================
    ValueMap Values                                                        
    ======== ==============================================================
    0        Operation completed successfully                              
    1        Operation unsupported                                         
    2        Failed                                                        
    ..       DMTF Reserved                                                 
    4096     Unable to set password, user created                          
    4097     Unable to create home directory, user created and password set
    ======== ==============================================================
    
    **Parameters**
    
        *IN* :ref:`CIM_ComputerSystem <CIM-ComputerSystem>` **System**
            The scoping ComputerSystem in which to create the Account.

            
        
        *IN* ``string`` **Name**
            Desired user login name for the account to be created.

            
        
        *IN* ``string`` **GECOS**
            GECOS information for new user

            
        
        *IN* ``string`` **HomeDirectory**
            Set home directory for the user.

            
        
        *IN* ``boolean`` **DontCreateHome**
            Wheter to create home directory.

            
        
        *IN* ``string`` **Shell**
            Default shell for new user

            
        
        *IN* ``uint32`` **UID**
            Pick a specific user id for new user

            
        
        *IN* ``uint32`` **GID**
            Pick a specific group id for new user

            
        
        *IN* ``boolean`` **SystemAccount**
            True for creating system account

            
        
        *IN* ``string`` **Password**
            Password for a new user. By default has to be encrypted, but can be plaintext if PasswordIsPlain is set to true

            
        
        *IN* ``boolean`` **DontCreateGroup**
            Whether to create group

            
        
        *IN* ``boolean`` **PasswordIsPlain**
            If set to true, the Password is treated as plain text, otherwise has to be ecnrypted

            
        
        *OUT* :ref:`CIM_Account <CIM-Account>` **Account**
            Reference to the instance of CIM_Account created when the method returns a value of 0.

            
        
        *OUT* :ref:`CIM_Identity[] <CIM-Identity>` **Identities**
            Reference to the instances of CIM_Identity created when the method returns a value of 0. NULL if no such instances are created.

            
        
    
    .. _LMI-AccountManagementService-CreateGroup:

``uint32`` **CreateGroup** (:ref:`CIM_ComputerSystem <CIM-ComputerSystem>` System, ``string`` Name, ``uint32`` GID, ``boolean`` SystemAccount, :ref:`CIM_Group <CIM-Group>` Group, :ref:`CIM_Identity[] <CIM-Identity>` Identities)

    Create a new group on the system

    
    ======== ================================
    ValueMap Values                          
    ======== ================================
    0        Operation completed successfully
    1        Operation unsupported           
    2        Failed                          
    ..       DMTF Reserved                   
    ======== ================================
    
    **Parameters**
    
        *IN* :ref:`CIM_ComputerSystem <CIM-ComputerSystem>` **System**
            The scoping ComputerSystem in which to create the Account.

            
        
        *IN* ``string`` **Name**
            Desired group name for the account to be created.

            
        
        *IN* ``uint32`` **GID**
            Pick a specific group id for new user

            
        
        *IN* ``boolean`` **SystemAccount**
            True for creating system account

            
        
        *OUT* :ref:`CIM_Group <CIM-Group>` **Group**
            Reference to the instance of CIM_Group created when the method returns a value of 0.

            
        
        *OUT* :ref:`CIM_Identity[] <CIM-Identity>` **Identities**
            Reference to the instances of CIM_Identity created when the method returns a value of 0. NULL if no such instances are created.

            
        
    

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

