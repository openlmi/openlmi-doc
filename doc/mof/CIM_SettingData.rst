.. _CIM-SettingData:

CIM_SettingData
---------------

Class reference
===============
Subclass of :ref:`CIM_ManagedElement <CIM-ManagedElement>`

CIM_SettingData is used to represent configuration and and operational parameters for CIM_ManagedElement instances. There are a number of different uses of CIM_SettingData supported in the model today. Additional uses may be defined in the future.

Instances of CIM_SettingData may represent Aspects of a CIM_ManagedElement instance. This is modeled using the CIM_SettingsDefineState association. CIM_SettingData may be used to define capabilities when associated to an instance of CIM_Capabilities through the CIM_SettingsDefineCapabilities association. 

Instances of CIM_SettingData may represent different types of configurations for a CIM_ManagedElement, including persistent configurations, in progress configuration changes, or requested configurations. The CIM_ElementSettingData association is used to model the relationship between a CIM_SettingData instance and the CIM_ManagedElement for which it is a configuration. 

When an instance of CIM_SettingData represents a configuration, the current operational values for the parameters of the element are reflected by properties in the Element itself or by properties in its associations. These properties do not have to be the same values that are present in the SettingData object. For example, a modem might have a SettingData baud rate of 56Kb/sec but be operating at 19.2Kb/sec. 

Note: The CIM_SettingData class is very similar to CIM_Setting, yet both classes are present in the model because many implementations have successfully used CIM_Setting. However, issues have arisen that could not be resolved without defining a new class. Therefore, until a new major release occurs, both classes will exist in the model. Refer to the Core White Paper for additional information. SettingData instances can be aggregated together into higher- level SettingData objects using ConcreteComponent associations.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-SettingData-SoOrgID:

``string`` **SoOrgID**

    If not Null, the CIM_SettingData instance is being used to represent an ITIL element: either a service option, a service level requirement, or a service level target. When not Null, the value of SoOrgID shall be a unique identifier for the organization that specifies the value of SoID.

    
.. _CIM-SettingData-SoID:

``string`` **SoID**

    If not Null, the CIM_SettingData instance is being used to represent an ITIL element: either a service option, a service level requirement, or a service level target. The value SoID must be unique in the context of an Organization unique identifier specified in SoOrgID.

    
.. _CIM-SettingData-ElementName:

``string`` **ElementName**

    The user-friendly name for this instance of SettingData. In addition, the user-friendly name can be used as an index property for a search or query. (Note: The name does not have to be unique within a namespace.)

    
.. _CIM-SettingData-ChangeableType:

``uint16`` **ChangeableType**

    Enumeration indicating the type of setting. 0 "Not Changeable - Persistent" indicates the instance of SettingData represents primordial settings and shall not be modifiable. 1 "Changeable - Transient" indicates the SettingData represents modifiable settings that are not persisted. Establishing persistent settings from transient settings may be supported. 2 "Changeable - Persistent" indicates the SettingData represents a persistent configuration that may be modified. 3 "Not Changeable - Transient" indicates the SettingData represents a snapshot of the settings of the associated ManagedElement and is not persistent.

    
    ======== ===========================
    ValueMap Values                     
    ======== ===========================
    0        Not Changeable - Persistent
    1        Changeable - Transient     
    2        Changeable - Persistent    
    3        Not Changeable - Transient 
    ======== ===========================
    
.. _CIM-SettingData-ComponentSetting:

``string[]`` **ComponentSetting**

    The value of each CIM_ComponentSetting instance includes a CIM_SettingData instance that specifies further values for this CIM_SettingData instance. The values are interpreted according to the values of the Policy, ValueRole, and ValueRange properties included in each CIM_ComponentSetting instance.

    

    Note: If SoID is not null, then the embedded ComponentSetting elements may be interpreted as ITIL Service Level Targets.

    Note: For CIM v3, the type of ComponentSetting will be CIM_ComponentSetting. This is not represented as an EmbeddedInstance in CIM v2 to avoid a circular dependency that CIM v2 compilers cannot handle.

    
.. _CIM-SettingData-InstanceID:

``string`` **InstanceID**

    Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following "preferred" algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon (:), and where <OrgID> must include a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID or that is a registered ID assigned to the business entity by a recognized global authority. (This requirement is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness, <OrgID> must not contain a colon (:). When using this algorithm, the first colon to appear in InstanceID must appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and should not be reused to identify different underlying (real-world) elements. If the above "preferred" algorithm is not used, the defining entity must assure that the resulting InstanceID is not reused across any InstanceIDs produced by this or other providers for the NameSpace of this instance. 

    For DMTF-defined instances, the "preferred" algorithm must be used with the <OrgID> set to CIM.

    
.. _CIM-SettingData-ConfigurationName:

``string`` **ConfigurationName**

    An instance of CIM_SettingData may correspond to a well-known configuration that exists for an associated CIM_ManagedElement. If the ConfigurationName property is non-NULL, the instance of CIM_SettingData shall correspond to a well-known configuration for a Managed Element, the value of the ConfigurationName property shall be the name of the configuration, and the ChangeableType property shall have the value 0 or 2. A value of NULL for the ConfigurationName property shall mean that the instance of CIM_SettingData does not correspond to a well-known configuration for a Managed Element or that this information is unknown.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

