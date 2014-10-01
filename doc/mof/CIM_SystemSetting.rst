.. _CIM-SystemSetting:

CIM_SystemSetting
-----------------

Class reference
===============
Subclass of :ref:`CIM_Setting <CIM-Setting>`

CIM_SystemSetting represents the general concept of a CIM_Setting that is scoped by a System.


Key properties
^^^^^^^^^^^^^^

| :ref:`CreationClassName <CIM-SystemSetting-CreationClassName>`
| :ref:`SettingID <CIM-Setting-SettingID>`
| :ref:`SystemName <CIM-SystemSetting-SystemName>`
| :ref:`SystemCreationClassName <CIM-SystemSetting-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-SystemSetting-SettingID:

``string`` **SettingID**

    The identifier by which the Setting object is known.

    
.. _CIM-SystemSetting-SystemName:

``string`` **SystemName**

    The Name of the scoping system.

    
.. _CIM-SystemSetting-CreationClassName:

``string`` **CreationClassName**

    CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

    
.. _CIM-SystemSetting-SystemCreationClassName:

``string`` **SystemCreationClassName**

    The CreationClassName of the scoping system.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`VerifyOKToApplyIncrementalChangeToCollection <CIM-Setting-VerifyOKToApplyIncrementalChangeToCollection>`
| :ref:`VerifyOKToApplyIncrementalChangeToMSE <CIM-Setting-VerifyOKToApplyIncrementalChangeToMSE>`
| :ref:`ApplyToCollection <CIM-Setting-ApplyToCollection>`
| :ref:`VerifyOKToApplyToCollection <CIM-Setting-VerifyOKToApplyToCollection>`
| :ref:`ApplyToMSE <CIM-Setting-ApplyToMSE>`
| :ref:`ApplyIncrementalChangeToCollection <CIM-Setting-ApplyIncrementalChangeToCollection>`
| :ref:`VerifyOKToApplyToMSE <CIM-Setting-VerifyOKToApplyToMSE>`
| :ref:`ApplyIncrementalChangeToMSE <CIM-Setting-ApplyIncrementalChangeToMSE>`

