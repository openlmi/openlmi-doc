.. _LMI-IPElementSettingData:

LMI_IPElementSettingData
------------------------

Class reference
===============
Subclass of :ref:`CIM_ElementSettingData <CIM-ElementSettingData>`

IPElementSettingData represents the association between ManagedElement (IPNetworkConnection or LinkAggregator8023ad) and applicable setting data. This association also describes whether this is a default or current setting. Each non-null, non-key property of the associated SettingData instance defines a setting value for the associated ManagedElement. The properties, IsDefault, IsCurrent and IsNext, further qualify those setting values.

.. note::    The referenced SettingData instance does not reflect the     current desired state of the referenced ManagedElement unless     ``IsCurrent`` has value ``1 (Is Current)``. 




Key properties
^^^^^^^^^^^^^^

| :ref:`SettingData <CIM-ElementSettingData-SettingData>`
| :ref:`ManagedElement <CIM-ElementSettingData-ManagedElement>`
| :ref:`SettingData <CIM-ElementSettingData-SettingData>`
| :ref:`ManagedElement <CIM-ElementSettingData-ManagedElement>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-IPElementSettingData-SettingData:

:ref:`CIM_IPAssignmentSettingData <CIM-IPAssignmentSettingData>` **SettingData**

    The SettingData object associated with the element.

    
.. _LMI-IPElementSettingData-IsNext:

``uint16`` **IsNext**

    An enumerated integer indicating whether or not the referenced setting is the next setting to be applied. For example, the application could take place on a re-initialization, reset, reconfiguration request.

    
    ======== ===========
    ValueMap Values     
    ======== ===========
    1        Is Next    
    2        Is Not Next
    ======== ===========
    
.. _LMI-IPElementSettingData-IsCurrent:

``uint16`` **IsCurrent**

    An enumerated integer that indicates that the referenced SettingData represents currently active configuration.

    

    
    ======== ==============
    ValueMap Values        
    ======== ==============
    1        Is Current    
    2        Is Not Current
    ======== ==============
    
.. _LMI-IPElementSettingData-ManagedElement:

:ref:`CIM_ManagedElement <CIM-ManagedElement>` **ManagedElement**

    The managed element.

    
.. _LMI-IPElementSettingData-IsDefault:

``uint16`` **IsDefault**

    An enumerated integer that indicates that the referenced setting is a default setting for the element.

    
    ======== ==============
    ValueMap Values        
    ======== ==============
    1        Is Default    
    2        Is Not Default
    ======== ==============
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`IsMinimum <CIM-ElementSettingData-IsMinimum>`
| ``uint16`` :ref:`IsPending <CIM-ElementSettingData-IsPending>`
| ``uint16`` :ref:`IsMaximum <CIM-ElementSettingData-IsMaximum>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

