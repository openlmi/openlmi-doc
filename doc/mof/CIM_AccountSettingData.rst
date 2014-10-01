.. _CIM-AccountSettingData:

CIM_AccountSettingData
----------------------

Class reference
===============
Subclass of :ref:`CIM_SettingData <CIM-SettingData>`

CIM_AccountSettingData provides the ability to manage the desired configuration for an instance of CIM_Account. When associated with an instance of CIM_AccountManagementService, this class may be used to constrain the properties of instances of CIM_Accountcreated using the service. When associated with an instance of CIM_Account, this class may be used to manage the configuration of the CIM_Acount instance.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-AccountSettingData-MaximumPasswordExpiration:

``datetime`` **MaximumPasswordExpiration**

    MaximumPasswordExpiration indicates the maximum password age enforced for the Account. The value shall be expressed in interval format or shall be NULL. A value of NULL shall indicate that the password aging is not enforced.

    
.. _CIM-AccountSettingData-MaximumSuccessiveLoginFailures:

``uint16`` **MaximumSuccessiveLoginFailures**

    MaximumSuccessiveLoginFailures indicates the number of successive failed login attempts that shall result in the Account being disabled. A value of zero shall indicate that the Account will not be disabled due to successive failed login attempts.

    
.. _CIM-AccountSettingData-ComplexPasswordRulesEnforced:

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
    
.. _CIM-AccountSettingData-InactivityTimeout:

``datetime`` **InactivityTimeout**

    InactivityTimeout specifies the interval after which if an account has been inactive, it shall be Disabled. The value shall be expressed in interval format or shall be NULL. A value of NULL shall indicate that the Account will not be disabled due to inactivity.

    
.. _CIM-AccountSettingData-PasswordHistoryDepth:

``uint16`` **PasswordHistoryDepth**

    PasswordHistoryDepth indicates the number of previous passwords that shall be maintained for the Account. The Account shall preclude the selection of a password if it occurs in the password history. A value of zero shall indicate that a password history is not maintained.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`SoOrgID <CIM-SettingData-SoOrgID>`
| ``string`` :ref:`SoID <CIM-SettingData-SoID>`
| ``string`` :ref:`ElementName <CIM-SettingData-ElementName>`
| ``string`` :ref:`ConfigurationName <CIM-SettingData-ConfigurationName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`ChangeableType <CIM-SettingData-ChangeableType>`
| ``string`` :ref:`InstanceID <CIM-SettingData-InstanceID>`
| ``string[]`` :ref:`ComponentSetting <CIM-SettingData-ComponentSetting>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

