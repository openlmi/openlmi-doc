.. _LMI-AccountManagementServiceSettingData:

LMI_AccountManagementServiceSettingData
---------------------------------------

Class reference
===============
Subclass of :ref:`CIM_ElementSettingData <CIM-ElementSettingData>`

ElementSettingData represents the association between ManagedElements and applicable setting data. This association also describes whether this is a default or current setting. Each non-null, non-key property of the associated SettingData instance defines a setting value for the associated ManagedElement. The properties, IsDefault, IsCurrent, IsNext, IsMinimum, IsMaximum, and IsPending further qualify those setting values. 

Note: the referenced SettingData instance does not reflect the current desired state of the referenced ManagedElement unless IsCurrent = "Is Current". 

When IsMinimum and/or IsMaximum properties have the value "Is Minimum" or "Is Maximum" respectively, the referenced SettingData instance reflects desired minimum or maximum values respectively. When IsMinimum and IsMaximum have any other value, the referenced SettingData reflects actual desired values.


Key properties
^^^^^^^^^^^^^^

| :ref:`SettingData <CIM-ElementSettingData-SettingData>`
| :ref:`ManagedElement <CIM-ElementSettingData-ManagedElement>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-AccountManagementServiceSettingData-SettingData:

:ref:`LMI_AccountSettingData <LMI-AccountSettingData>` **SettingData**

    The default enforced setting for new Accounts

    
.. _LMI-AccountManagementServiceSettingData-ManagedElement:

:ref:`LMI_AccountManagementService <LMI-AccountManagementService>` **ManagedElement**

    The Central Instance of Account management

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`IsMinimum <CIM-ElementSettingData-IsMinimum>`
| ``uint16`` :ref:`IsPending <CIM-ElementSettingData-IsPending>`
| ``uint16`` :ref:`IsNext <CIM-ElementSettingData-IsNext>`
| ``uint16`` :ref:`IsCurrent <CIM-ElementSettingData-IsCurrent>`
| ``uint16`` :ref:`IsMaximum <CIM-ElementSettingData-IsMaximum>`
| ``uint16`` :ref:`IsDefault <CIM-ElementSettingData-IsDefault>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

