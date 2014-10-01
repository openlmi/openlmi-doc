.. _LMI-SELinuxService:

LMI_SELinuxService
------------------

Class reference
===============
Subclass of :ref:`CIM_Service <CIM-Service>`

SELinux on the managed system.

SELinux can be in the following states:

   Enforcing - SELinux security policy is enforced.

   Permissive - SELinux prints warnings instead of enforcing.

   Disabled - No SELinux policy is loaded.




Key properties
^^^^^^^^^^^^^^

| :ref:`Name <CIM-Service-Name>`
| :ref:`SystemName <CIM-Service-SystemName>`
| :ref:`SystemCreationClassName <CIM-Service-SystemCreationClassName>`
| :ref:`CreationClassName <CIM-Service-CreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-SELinuxService-SELinuxState:

``uint16`` **SELinuxState**

    Current system-wide state of SELinux.

    
    ======== ==========
    ValueMap Values    
    ======== ==========
    0        Disabled  
    1        Permissive
    2        Enforcing 
    ======== ==========
    
.. _LMI-SELinuxService-SELinuxDefaultState:

``uint16`` **SELinuxDefaultState**

    SELinux system-wide state on next system boot.

    
    ======== ==========
    ValueMap Values    
    ======== ==========
    0        Disabled  
    1        Permissive
    2        Enforcing 
    ======== ==========
    
.. _LMI-SELinuxService-PolicyVersion:

``uint32`` **PolicyVersion**

    Current version of the SELinux system policy.

    
.. _LMI-SELinuxService-PolicyType:

``string`` **PolicyType**

    SELinux policy type.

    

Local methods
^^^^^^^^^^^^^

    .. _LMI-SELinuxService-SetSELinuxState:

``uint32`` **SetSELinuxState** (``uint16`` NewState, ``boolean`` MakeDefault, :ref:`LMI_SELinuxJob <LMI-SELinuxJob>` Job)

    Set SELinux state.

    
    ======== =======================================
    ValueMap Values                                 
    ======== =======================================
    0        Job Completed with No Error            
    1        Not Supported                          
    2        Unknown                                
    3        Timeout                                
    4        Failed                                 
    5        Invalid Parameter                      
    6        In Use                                 
    4096     Method Parameters Checked - Job Started
    ======== =======================================
    
    **Parameters**
    
        *IN* ``uint16`` **NewState**
            New state value.

            
            ======== ==========
            ValueMap Values    
            ======== ==========
            0        Disabled  
            1        Permissive
            2        Enforcing 
            ======== ==========
            
        
        *IN* ``boolean`` **MakeDefault**
            If set to True, makes the new state persistent.

            
        
        *OUT* :ref:`LMI_SELinuxJob <LMI-SELinuxJob>` **Job**
            
        
    
    .. _LMI-SELinuxService-RestoreLabels:

``uint32`` **RestoreLabels** (:ref:`LMI_UnixFile <LMI-UnixFile>` Target, ``uint16`` Action, ``boolean`` Recursively, :ref:`LMI_SELinuxJob <LMI-SELinuxJob>` Job)

    Restore default SELinux security contexts on files.

    There are two actions that can be taken on the specified files:

     Report: List files whose SELinux label is different than the one specified by the policy.

     Restore: Restore SELinux label on files to the respective values specified by the policy.

    

    
    ======== =======================================
    ValueMap Values                                 
    ======== =======================================
    0        Job Completed with No Error            
    1        Not Supported                          
    2        Unknown                                
    3        Timeout                                
    4        Failed                                 
    5        Invalid Parameter                      
    6        In Use                                 
    4096     Method Parameters Checked - Job Started
    ======== =======================================
    
    **Parameters**
    
        *IN*, *OUT* :ref:`LMI_UnixFile <LMI-UnixFile>` **Target**
            SELinux file to change. If it's not a directory, the Recursively parameter has no effect.

            
        
        *IN* ``uint16`` **Action**
            Action to take on mislabeled files.

            
            ======== ================
            ValueMap Values          
            ======== ================
            0        Report          
            1        Restore         
            ..       OpenLMI Reserved
            ======== ================
            
        
        *IN* ``boolean`` **Recursively**
            If True, restore labels recursively in case Target is a directory. If Target is not a directory, this value is ignored.

            
        
        *OUT* :ref:`LMI_SELinuxJob <LMI-SELinuxJob>` **Job**
            
        
    
    .. _LMI-SELinuxService-SetFileLabel:

``uint32`` **SetFileLabel** (:ref:`LMI_UnixFile <LMI-UnixFile>` Target, ``string`` Label, :ref:`LMI_SELinuxJob <LMI-SELinuxJob>` Job)

    Set label on an SELinux file.

    
    ======== =======================================
    ValueMap Values                                 
    ======== =======================================
    0        Job Completed with No Error            
    1        Not Supported                          
    2        Unknown                                
    3        Timeout                                
    4        Failed                                 
    5        Invalid Parameter                      
    6        In Use                                 
    4096     Method Parameters Checked - Job Started
    ======== =======================================
    
    **Parameters**
    
        *IN* :ref:`LMI_UnixFile <LMI-UnixFile>` **Target**
            An SELinux file to change.

            
        
        *IN* ``string`` **Label**
            New label.

            
        
        *OUT* :ref:`LMI_SELinuxJob <LMI-SELinuxJob>` **Job**
            
        
    
    .. _LMI-SELinuxService-SetPortLabel:

``uint32`` **SetPortLabel** (:ref:`LMI_SELinuxPort <LMI-SELinuxPort>` Target, ``string`` PortRange, :ref:`LMI_SELinuxJob <LMI-SELinuxJob>` Job)

    Set label on an SELinux port.

    
    ======== =======================================
    ValueMap Values                                 
    ======== =======================================
    0        Job Completed with No Error            
    1        Not Supported                          
    2        Unknown                                
    3        Timeout                                
    4        Failed                                 
    5        Invalid Parameter                      
    6        In Use                                 
    4096     Method Parameters Checked - Job Started
    ======== =======================================
    
    **Parameters**
    
        *IN* :ref:`LMI_SELinuxPort <LMI-SELinuxPort>` **Target**
            An SELinux port to change.

            
        
        *IN* ``string`` **PortRange**
            Network ports to change. Can be specified as a single port or as range, for example 1024-2048'.

            
        
        *OUT* :ref:`LMI_SELinuxJob <LMI-SELinuxJob>` **Job**
            
        
    
    .. _LMI-SELinuxService-SetBoolean:

``uint32`` **SetBoolean** (:ref:`LMI_SELinuxBoolean <LMI-SELinuxBoolean>` Target, ``boolean`` Value, ``boolean`` MakeDefault, :ref:`LMI_SELinuxJob <LMI-SELinuxJob>` Job)

    Set a new value of an SELinux boolean.

    
    ======== =======================================
    ValueMap Values                                 
    ======== =======================================
    0        Job Completed with No Error            
    1        Not Supported                          
    2        Unknown                                
    3        Timeout                                
    4        Failed                                 
    5        Invalid Parameter                      
    6        In Use                                 
    4096     Method Parameters Checked - Job Started
    ======== =======================================
    
    **Parameters**
    
        *IN* :ref:`LMI_SELinuxBoolean <LMI-SELinuxBoolean>` **Target**
            An SELinux boolean to change.

            
        
        *IN* ``boolean`` **Value**
            New value.

            
        
        *IN* ``boolean`` **MakeDefault**
            If True, makes the new state persistent.

            
        
        *OUT* :ref:`LMI_SELinuxJob <LMI-SELinuxJob>` **Job**
            
        
    

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
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
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
| ``string`` :ref:`SystemCreationClassName <CIM-Service-SystemCreationClassName>`
| ``string`` :ref:`CreationClassName <CIM-Service-CreationClassName>`
| ``string`` :ref:`PrimaryOwnerName <CIM-Service-PrimaryOwnerName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`
| :ref:`StopService <CIM-Service-StopService>`
| :ref:`ChangeAffectedElementsAssignedSequence <CIM-Service-ChangeAffectedElementsAssignedSequence>`
| :ref:`StartService <CIM-Service-StartService>`

