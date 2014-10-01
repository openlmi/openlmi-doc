.. _LMI-IPVersionElementSettingData:

LMI_IPVersionElementSettingData
-------------------------------

Class reference
===============
Subclass of :ref:`CIM_ElementSettingData <CIM-ElementSettingData>`

LMI_IPVersionElementSettingData is association between IPVersionSettingData and ComputerSystem or IPNetworkConnection.

Association with ComputerSystem means that the ComputerSystem supports given IP version. Association with IPNetworkConnection means that the IPNetworkConnection supports given IP version.


Key properties
^^^^^^^^^^^^^^

| :ref:`SettingData <CIM-ElementSettingData-SettingData>`
| :ref:`ManagedElement <CIM-ElementSettingData-ManagedElement>`
| :ref:`SettingData <CIM-ElementSettingData-SettingData>`
| :ref:`ManagedElement <CIM-ElementSettingData-ManagedElement>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-IPVersionElementSettingData-SettingData:

:ref:`CIM_IPVersionSettingData <CIM-IPVersionSettingData>` **SettingData**

    The SettingData object associated with the element.

    
.. _LMI-IPVersionElementSettingData-ManagedElement:

:ref:`CIM_ManagedElement <CIM-ManagedElement>` **ManagedElement**

    The managed element.

    

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

