.. _LMI-DiskPartitionElementSettingData:

LMI_DiskPartitionElementSettingData
-----------------------------------

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

.. _LMI-DiskPartitionElementSettingData-IsCurrent:

``uint16`` **IsCurrent**

    An enumerated integer that indicates that the referenced SettingData represents the last requested values for attributes of the Managed Element or that this information is unknown. 

    Attributes of the SettingData itself indicate whether it represents the last configuration applied to the ManagedElement or is a transient snapshot of the requested settings. Current operational characteristics of a ManagedElement should be represented with properties of the ManagedElement. element or that this information is unknown. 

    For a given ManagedElement and all instances of a SettingData subclass, there shall be at most one instance of ElementSettingData which references the ManagedElement and an instance of the SettingData sub-class where there is a specified non-null, non-key property of the SettingData sub-class, and the IsMaximum property on the referencing ElementSettingData instance has a value of "Is Maximum" or the IsMinimum property on the referencing ElementSettingData instance has a value of "Is Minimum" and the IsCurrent property on the referencing ElementSettingData instance has a value of "Is Current". There shall be at most one instance of ElementSettingData which references a ManagedElement and an instance of a SettingData sub-class where the IsCurrent property has a value of "Is Current" and the IsMinimum property does not have a value of "Is Minimum" and the IsMaximum property does not have a value of "Is Maximum".

    
    ======== ==============
    ValueMap Values        
    ======== ==============
    0        Unknown       
    1        Is Current    
    2        Is Not Current
    ======== ==============
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`IsMinimum <CIM-ElementSettingData-IsMinimum>`
| :ref:`CIM_SettingData <CIM-SettingData>` :ref:`SettingData <CIM-ElementSettingData-SettingData>`
| ``uint16`` :ref:`IsPending <CIM-ElementSettingData-IsPending>`
| ``uint16`` :ref:`IsNext <CIM-ElementSettingData-IsNext>`
| :ref:`CIM_ManagedElement <CIM-ManagedElement>` :ref:`ManagedElement <CIM-ElementSettingData-ManagedElement>`
| ``uint16`` :ref:`IsMaximum <CIM-ElementSettingData-IsMaximum>`
| ``uint16`` :ref:`IsDefault <CIM-ElementSettingData-IsDefault>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

