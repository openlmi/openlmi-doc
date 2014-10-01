.. _CIM-Account:

CIM_Account
-----------

Class reference
===============
Subclass of :ref:`CIM_EnabledLogicalElement <CIM-EnabledLogicalElement>`

CIM_Account is the information held by a SecurityService to track identity and privileges managed by that service. Common examples of an Account are the entries in a UNIX /etc/passwd file. Several kinds of security services use various information from those entries - the /bin/login program uses the account name ('root') and hashed password to authenticate users, and the file service, for instance, uses the UserID field ('0') and GroupID field ('0') to record ownership and determine access control privileges on files in the file system. This class is defined so as to incorporate commonly-used LDAP attributes to permit implementations to easily derive this information from LDAP-accessible directories. 



The semantics of Account overlap with that of the class, CIM_Identity. However, aspects of Account - such as its specific tie to a System - are valuable and have been widely implemented. For this reason, the Account and Identity classes are associated using a subclass of LogicalIdentity (AccountIdentity), instead of deprecating the Account class in the CIM Schema. When an Account has been authenticated, the corresponding Identity's TrustEstablished Boolean would be set to TRUE. Then, the Identity class can be used as defined for authorization purposes.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-Account-SystemName>`
| :ref:`Name <CIM-Account-Name>`
| :ref:`CreationClassName <CIM-Account-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-Account-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-Account-OrganizationName:

``string[]`` **OrganizationName**

    The name of the organization related to the account.

    
.. _CIM-Account-UserID:

``string`` **UserID**

    UserID is the value used by the SecurityService to represent identity. For an authentication service, the UserID may be the name of the user, or for an authorization service the value which serves as a handle to a mapping of the identity.

    
.. _CIM-Account-MaximumSuccessiveLoginFailures:

``uint16`` **MaximumSuccessiveLoginFailures**

    MaximumSuccessiveLoginFailures indicates the number of successive failed login attempts that shall result in the Account being disabled. A value of zero shall indicate that the Account will not be disabled due to successive failed login attempts.

    
.. _CIM-Account-InactivityTimeout:

``datetime`` **InactivityTimeout**

    InactivityTimeout specifies the interval after which if an account has been inactive, it shall be Disabled. The value may be expressed in interval format, as an absolute date-time, or be NULL.

    An absolute date-time shall indicate when the password will be disabled due to inactivity.

    An interval value shall indicate the time remaining before the password is disabled due to inactivity.

    A value of NULL shall indicate that the Account will not be disabled due to inactivity.

    
.. _CIM-Account-SystemName:

``string`` **SystemName**

    The scoping System's Name.

    
.. _CIM-Account-LastLogin:

``datetime`` **LastLogin**

    LastLogin shall be an absolute date-time that specifies the last successful authentication that occurred for this Account.A value of 99990101000000.000000+000 shall indicate the Account has never been used. A value of NULL shall indicate the last successful login is unknown.

    
.. _CIM-Account-UserPasswordEncryptionAlgorithm:

``uint16`` **UserPasswordEncryptionAlgorithm**

    The encryption algorithm (if any) used by the client to produce the value in the UserPassword property when creating or modifying an instance of CIM_Account. The original password is encrypted using the algorithm specified in this property, and UserPassword contains the resulting encrypted value. In response to an operation request that would return the value of the UserPassword property to a client, an implementation shall instead return an array of length zero.

    The value of UserPasswordEncryptionAlgorithm in an instance of CIM_Account shall be 0 ("None") unless the SupportedUserPasswordEncryptionAlgorithms[] property in the CIM_AccountManagementCapabilities instance associated with the CIM_AccountManagementService instance associated with the CIM_Account instance contains a non-null entry other than 0 ("None").

    This property does not prevent the use of encryption at the transport, network, or data-link layer to protect communications between a management client and the server, nor is it meant to encourage communications without such encryption.

    The supported values for this property are:

    - 0 ("None"): Indicates that the contents of UserPassword are not encrypted.

    - 1 ("Other"): Indicates that the contents of UserPassword are encrypted using an algorithm not specifically identified in the value map for this property, and that this algorithm is described in OtherUserPasswordEncryptionAlgorithm.

    - 2 ("HTTP Digest MD5(A1)"): The MD5 hash algorithm, applied to the string A1 defined in RFC2617 as the concatenation username-value ":" realm-value ":" passwd, where username-value is provided by the client as the value of the UserID property. passwd is the underlying user password. realm-value is the HTTP digest realm value, and is provided by the server. The semantics of the HTTP digest realm are specified in RFC 2617. The server may surface the realm-value in the UserPasswordEncryptionSalt property of CIM_AccountManagementCapabilities.

    
    ======== ===================
    ValueMap Values             
    ======== ===================
    0        None               
    1        Other              
    2        HTTP Digest MD5(A1)
    ..       DMTF Reserved      
    ======== ===================
    
.. _CIM-Account-Name:

``string`` **Name**

    The Name property defines the label by which the object is known. The value of this property may be set to be the same as that of the UserID property or, in the case of an LDAP-derived instance, the Name property value may be set to the distinguishedName of the LDAP-accessed object instance.

    
.. _CIM-Account-ObjectClass:

``string[]`` **ObjectClass**

    In the case of an LDAP-derived instance, the ObjectClass property value(s) may be set to the objectClass attribute values.

    
.. _CIM-Account-ComplexPasswordRulesEnforced:

``uint16[]`` **ComplexPasswordRulesEnforced**

    ComplexPasswordRulesEnforced indicates the rules for constructing a complex password enforced by the Account.

    Minimum Length a minimum length is enforced for passwords for the account.

    Preclude User ID inclusion precluding the password from including the user ID is supported. 

    Maximum Repeating Characters a limit will be enforced on the number of times a character can occur consecutively. 

    Lower Case Alpha at least one lower case alpha character is required. 

    Upper Case Alpha at least one upper case alpha character is required. 

    Numeric Character at least one numeric character is required. 

    Special Character at least one special character is required.

    
    ============== ============================
    ValueMap       Values                      
    ============== ============================
    2              Minimum Length              
    3              Preclude User ID Inclusion  
    4              Maximum Repeating Characters
    5              Lower Case Alpha            
    6              Upper Case Alpha            
    7              Numeric Character           
    8              Special Character           
    ..             DMTF Reserved               
    0x8000..0xFFFF Vendor Reserved             
    ============== ============================
    
.. _CIM-Account-Host:

``string[]`` **Host**

    Based on RFC1274, the host name of the system(s) for which the account applies. The host name may be a fully-qualified DNS name or it may be an unqualified host name.

    
.. _CIM-Account-LocalityName:

``string[]`` **LocalityName**

    This property contains the name of a locality, such as a city, county or other geographic region.

    
.. _CIM-Account-SeeAlso:

``string[]`` **SeeAlso**

    In the case of an LDAP-derived instance, the SeeAlso property specifies distinguished name of other Directory objects which may be other aspects (in some sense) of the same real world object.

    
.. _CIM-Account-UserPasswordEncoding:

``uint32`` **UserPasswordEncoding**

    UserPasswordEncoding specifies encoding used for the UserPassword property.

    "kbd" denotes a string in hexadecimal format containing keyboard scan code input. An example of a UserPassword structured in this format would be "321539191E1F1F11181320", which is the representation of "my password" in US English keyboard scan codes.

    "ascii" denotes clear text that complies with the ASCII character set. An example would be "my password".

    "pin" denotes that only numeric input in ASCII text is allowed for the UserPassword. An example would be "1234".

    "UTF-8" denotes that the UserPassword is a Unicode string that is encoded using UTF-8 character set.

    "UTF-16" denotes that the UserPassword is a Unicode string that is encoded using UTF-16 character set. The byte order mark (BOM) shall be the first character of the string.

    "UTF-16LE" denotes that the UserPassword is a Unicode string that is encoded using UTF-16 character set in little-endian byte order.

    "UTF-16BE" denotes that the UserPassword is a Unicode string that is encoded using UTF-16 character set in big-endian byte order.

    "UCS-2" denotes that the UserPassword is a Unicode string that is encoded using UCS-2 character set.

    "UCS-2LE" denotes that the UserPassword is a Unicode string that is encoded using UCS-2 character set in little endian byte order.

    "UCS-2BE" denotes that the UserPassword is a Unicode string that is encoded using UCS-2 character set in big endian byte order.

    
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
    10                USC-2LE        
    11                UCS-2BE        
    ..                DMTF Reserved  
    65536..4294967295 Vendor Reserved
    ================= ===============
    
.. _CIM-Account-UserCertificate:

``string[]`` **UserCertificate**

    Based on inetOrgPerson and for directory compatibility, the UserCertificate property may be used to specify a public key certificate for the person.

    
.. _CIM-Account-UserPassword:

``string[]`` **UserPassword**

    In the case of an LDAP-derived instance, the UserPassword property may contain an encrypted password used to access the person's resources in a directory.

    
.. _CIM-Account-OtherUserPasswordEncryptionAlgorithm:

``string`` **OtherUserPasswordEncryptionAlgorithm**

    If the UserPasswordEncryptionAlgorithm property is set to 1 ("Other") this property contains a free form string that provides more information about the encryption algorithm. If UserPasswordEncryptionAlgorithm is not set to 1 ("Other") this property has no meaning.

    
.. _CIM-Account-PasswordExpiration:

``datetime`` **PasswordExpiration**

    PasswordExpiration indicates the maximum password age enforced for the Account. The value may be expressed as an absolute date-time as an interval, or may be NULL.

    An absolute date-time shall indicate the date and time when the password will expire.

    An interval value shall indicate the time remaining until the password expires.

    A value of NULL shall indicate the password never expires.

    
.. _CIM-Account-Descriptions:

``string[]`` **Descriptions**

    The Descriptions property values may contain human-readable descriptions of the object. In the case of an LDAP-derived instance, the description attribute may have multiple values that, therefore, cannot be placed in the inherited Description property.

    
.. _CIM-Account-PasswordHistoryDepth:

``uint16`` **PasswordHistoryDepth**

    PasswordHistoryDepth indicates the number of previous passwords that shall be maintained for the Account. The Account shall preclude the selection of a password if it occurs in the password history. A value of zero shall indicate that a password history is not maintained.

    
.. _CIM-Account-CreationClassName:

``string`` **CreationClassName**

    CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

    
.. _CIM-Account-OU:

``string[]`` **OU**

    The name of an organizational unit related to the account.

    
.. _CIM-Account-SystemCreationClassName:

``string`` **SystemCreationClassName**

    The scoping System's CCN.

    

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
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`

