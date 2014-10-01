.. _CIM-AccountManagementCapabilities:

CIM_AccountManagementCapabilities
---------------------------------

Class reference
===============
Subclass of :ref:`CIM_EnabledLogicalElementCapabilities <CIM-EnabledLogicalElementCapabilities>`

AccountManagementCapabilities describes the capabilities supported for managing Accounts associated with an instance of AccountManagementService. AccountManagementCapabilities is associated with an instance of AccountManagementService through the ElementCapabilities association.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-AccountManagementCapabilities-SupportedUserPasswordEncodings:

``uint32[]`` **SupportedUserPasswordEncodings**

    This property enumerates encoding algorithms that a client may use to encode the UserPassword property when creating or modifying an instance of CIM_Account. See CIM_Account property UserPasswordEncoding for a description of each enum value.

    
    ================= ===============
    ValueMap          Values         
    ================= ===============
    2                 ascii          
    3                 kbd            
    4                 pin            
    5                 UTF-8          
    6                 UTF-16         
    7                 UTF-16LE       
    8                 UTF-16BE       
    9                 UCS-2          
    10                UCS-2LE        
    11                UCS-2BE        
    ..                DMTF Reserved  
    65536..4294967295 Vendor Reserved
    ================= ===============
    
.. _CIM-AccountManagementCapabilities-MaximumAccountsSupported:

``uint16`` **MaximumAccountsSupported**

    MaximumAccountsSupported shall indicate the maximum number of accounts that may be managed by the associated instance of CIM_AccountManagementService. Note that if multiple instances of CIM_AccountManagementService manage the accounts of a system, the total maximum number of accounts supported on the system is the sum of MaximumAccountsSupported for all of the instances of CIM_AccountManagementService. A value of zero shall indicate that the maximum number of accounts is unknown or that a maximum number of accounts is not enforced.

    
.. _CIM-AccountManagementCapabilities-OperationsSupported:

``uint16[]`` **OperationsSupported**

    OperationsSupported describes the type of operations that are supported for an Account associated with the AccountManagementService.

    "Create" indicates the AccountManagementService may be used to create new accounts.

    "Modify" indicates that the associated Accounts may be modified.

    "Delete" indicates that associated Accounts may be deleted.

    
    ============== ===========================
    ValueMap       Values                     
    ============== ===========================
    2              Create                     
    3              Modify                     
    4              Delete                     
    5              CreateUserContact          
    6              CreateUserContactByIdentity
    7              ModifyUserContact          
    8              DeleteUserContact          
    9              GetAccount                 
    10             GetUserContact             
    ..             DMTF Reserved              
    0x8000..0xFFFF Vendor Reserved            
    ============== ===========================
    
.. _CIM-AccountManagementCapabilities-SupportedUserPasswordEncryptionAlgorithms:

``uint16[]`` **SupportedUserPasswordEncryptionAlgorithms**

    This property enumerates encryption algorithms that a client may use to encrypt a value in the UserPassword property when creating or modifying an instance of CIM_Account. This capability is aimed at ensuring some measure of confidentiality when the password is transferred over an unencrypted transport protocol. An implementation may elect to accept only encrypted passwords, without regard to whether the transport protocol is encrypted. Similarly, a a client may elect to always provide encrypted passwords to implementations that accept either unencrypted or encrypted passwords, even if the underlying transport protocol is encrypted.

    See CIM_Account property UserPasswordEncryptionAlgorithm for a description of each enum value.

    
    ======== ===================
    ValueMap Values             
    ======== ===================
    0        None               
    1        Other              
    2        HTTP Digest MD5(A1)
    ..       DMTF Reserved      
    ======== ===================
    
.. _CIM-AccountManagementCapabilities-UserPasswordEncryptionSalt:

``string`` **UserPasswordEncryptionSalt**

    A value unique to the specific WBEM server that may be used in the selected UserPassword encryption algorithm to ensure a value that is unique among all WBEM servers even if a user uses the same password on multiple WBEM servers.

    
.. _CIM-AccountManagementCapabilities-OtherSupportedUserPasswordEncryptionAlgorithms:

``string[]`` **OtherSupportedUserPasswordEncryptionAlgorithms**

    Additional implementation-specific algorithms that a client may use to encrypt a value in the UserPassword property when creating or modifying an instance of CIM_Account. If this property is non-NULL, a client may select an algorithm in it by setting CIM_Account.UserPasswordEncryptionAlgorithm to 1 ("Other") and setting CIM_Account.OtherUserPasswordEncryptionAlgorithm to the value of the selected algorithm string.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`ElementName <CIM-Capabilities-ElementName>`
| ``uint16`` :ref:`MaxElementNameLen <CIM-EnabledLogicalElementCapabilities-MaxElementNameLen>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16[]`` :ref:`RequestedStatesSupported <CIM-EnabledLogicalElementCapabilities-RequestedStatesSupported>`
| ``string`` :ref:`ElementNameMask <CIM-EnabledLogicalElementCapabilities-ElementNameMask>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`InstanceID <CIM-Capabilities-InstanceID>`
| ``uint16[]`` :ref:`StateAwareness <CIM-EnabledLogicalElementCapabilities-StateAwareness>`
| ``boolean`` :ref:`ElementNameEditSupported <CIM-EnabledLogicalElementCapabilities-ElementNameEditSupported>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`CreateGoalSettings <CIM-Capabilities-CreateGoalSettings>`

