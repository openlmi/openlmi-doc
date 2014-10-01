.. _LMI-SettingsDefineManagementCapabilities:

LMI_SettingsDefineManagementCapabilities
----------------------------------------

Class reference
===============
Subclass of :ref:`CIM_SettingsDefineCapabilities <CIM-SettingsDefineCapabilities>`

This association indicates that the non-null, non-key set of properties of the component SettingData instance specifies some capabilities of the associated Capabilities instance. The interpretation of the set of properties in the associated SettingData is governed by the properties: PropertyPolicy and ValueRole.

For a particular Capabilities instance, the complete set of Component SettingData instances, together with properties of the Capabilities instance itself, defines the overall range of supported capabilities.

PropertyPolicy determines whether the properties of the set are interpreted independently or as a whole (i.e. correlated.)

ValueRole further qualifies the members of the set.

This association eliminates the need to define and maintain corresponding property definitions and values in both a Capabilities subclass and a SettingData subclass.

Typically these setting instances will be published along with the associated Capabilities instance and will not be modifiable by the client.


Key properties
^^^^^^^^^^^^^^

| :ref:`GroupComponent <CIM-AbstractComponent-GroupComponent>`
| :ref:`PartComponent <CIM-AbstractComponent-PartComponent>`
| :ref:`GroupComponent <CIM-AbstractComponent-GroupComponent>`
| :ref:`PartComponent <CIM-AbstractComponent-PartComponent>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-SettingsDefineManagementCapabilities-GroupComponent:

:ref:`LMI_AccountManagementCapabilities <LMI-AccountManagementCapabilities>` **GroupComponent**

    The Account Management Capabilities

    
.. _LMI-SettingsDefineManagementCapabilities-PartComponent:

:ref:`LMI_AccountSettingData <LMI-AccountSettingData>` **PartComponent**

    The default enforced setting for new Accounts

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`ValueRange <CIM-SettingsDefineCapabilities-ValueRange>`
| ``uint16`` :ref:`ValueRole <CIM-SettingsDefineCapabilities-ValueRole>`
| ``uint16`` :ref:`PropertyPolicy <CIM-SettingsDefineCapabilities-PropertyPolicy>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

