.. _LMI-Account:

LMI_Account
-----------

Class reference
===============
Subclass of :ref:`CIM_Account <CIM-Account>`

Class representing Linux Account


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-Account-SystemName>`
| :ref:`Name <CIM-Account-Name>`
| :ref:`CreationClassName <CIM-Account-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-Account-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-Account-HomeDirectory:

``string`` **HomeDirectory**

    User's home directory

    
.. _LMI-Account-AccountExpiration:

``datetime`` **AccountExpiration**

    The date of expiration of the account.

    
.. _LMI-Account-PasswordLastChange:

``datetime`` **PasswordLastChange**

    The date when was password last changed

    
.. _LMI-Account-UserPassword:

``string[]`` **UserPassword**

    In the case of an LDAP-derived instance, the UserPassword property may contain an encrypted password used to access the person's resources in a directory.

    

    When an instance of CIM_Account is retrieved and the underlying account has a valid password, the value of the CIM_Account.UserPassword property shall be an array of length zero to indicate that the account has a password configured.

    

    When the underlying account does not have a valid password, the CIM_Account.UserPassword property shall be NULL.

    
.. _LMI-Account-LoginShell:

``string`` **LoginShell**

    User's login shell

    
.. _LMI-Account-PasswordPossibleChange:

``datetime`` **PasswordPossibleChange**

    Minimum number of days between password change

    
.. _LMI-Account-PasswordExpirationWarning:

``datetime`` **PasswordExpirationWarning**

    Number of days of warning before password expires

    
.. _LMI-Account-PasswordInactivation:

``datetime`` **PasswordInactivation**

    Maximum number of days between password change

    

Local methods
^^^^^^^^^^^^^

    .. _LMI-Account-DeleteUser:

``uint32`` **DeleteUser** (``boolean`` DontDeleteHomeDirectory, ``boolean`` DontDeleteGroup, ``boolean`` Force)

    Delete the user. Along with the user, the home directory and user's primary group are deleted. If the user is not owner of the home directory it is not deleted. However this directory can be deleted if force parameter is set to True. If the home directory couldn't be deleted, no error is returned to be able to remove the user even when its home directory is inaccessible (e.g. unreachable NFS mount).

    
    ======== =======================================================
    ValueMap Values                                                 
    ======== =======================================================
    0        Operation completed successfully                       
    1        Failed                                                 
    ..       DMTF Reserved                                          
    4096     Non existing user                                      
    4097     Unable to delete Home Direcotry (currently unused)     
    4098     Unable to remove user, home directory removed          
    4099     Unable to remove group, user and home directory removed
    ======== =======================================================
    
    **Parameters**
    
        *IN* ``boolean`` **DontDeleteHomeDirectory**
            By default the user's home directory is deleted. Set to true to not delete the home directory.

            
        
        *IN* ``boolean`` **DontDeleteGroup**
            By default the user's private group, if the user has one, is deleted. Set to true to not delete the group.

            
        
        *IN* ``boolean`` **Force**
            Force the deletion of user's home directory, even if the user is not an owner.

            
        
    
    .. _LMI-Account-ChangePassword:

``uint32`` **ChangePassword** (``string`` Password)

    Change the user's password.

    
    ======== ================================
    ValueMap Values                          
    ======== ================================
    0        Operation completed successfully
    1        Failed                          
    ======== ================================
    
    **Parameters**
    
        *IN* ``string`` **Password**
            Plaintext string to which set the password; provider will encrypt the string using the default crypto algorithm

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`OrganizationName <CIM-Account-OrganizationName>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``string`` :ref:`UserID <CIM-Account-UserID>`
| ``uint16`` :ref:`MaximumSuccessiveLoginFailures <CIM-Account-MaximumSuccessiveLoginFailures>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``datetime`` :ref:`InactivityTimeout <CIM-Account-InactivityTimeout>`
| ``string`` :ref:`SystemName <CIM-Account-SystemName>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``datetime`` :ref:`LastLogin <CIM-Account-LastLogin>`
| ``uint16`` :ref:`UserPasswordEncryptionAlgorithm <CIM-Account-UserPasswordEncryptionAlgorithm>`
| ``string[]`` :ref:`SeeAlso <CIM-Account-SeeAlso>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``string[]`` :ref:`ObjectClass <CIM-Account-ObjectClass>`
| ``uint16[]`` :ref:`ComplexPasswordRulesEnforced <CIM-Account-ComplexPasswordRulesEnforced>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``string[]`` :ref:`Host <CIM-Account-Host>`
| ``string[]`` :ref:`LocalityName <CIM-Account-LocalityName>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`Name <CIM-Account-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``string[]`` :ref:`UserCertificate <CIM-Account-UserCertificate>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint32`` :ref:`UserPasswordEncoding <CIM-Account-UserPasswordEncoding>`
| ``string`` :ref:`OtherUserPasswordEncryptionAlgorithm <CIM-Account-OtherUserPasswordEncryptionAlgorithm>`
| ``string`` :ref:`CreationClassName <CIM-Account-CreationClassName>`
| ``string[]`` :ref:`OU <CIM-Account-OU>`
| ``datetime`` :ref:`PasswordExpiration <CIM-Account-PasswordExpiration>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string[]`` :ref:`Descriptions <CIM-Account-Descriptions>`
| ``uint16`` :ref:`PasswordHistoryDepth <CIM-Account-PasswordHistoryDepth>`
| ``string`` :ref:`SystemCreationClassName <CIM-Account-SystemCreationClassName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`

