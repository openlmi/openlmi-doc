.. _LMI-DiskPartitionConfigurationSetting:

LMI_DiskPartitionConfigurationSetting
-------------------------------------

Class reference
===============
Subclass of :ref:`CIM_SettingData <CIM-SettingData>`

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

.. _LMI-DiskPartitionConfigurationSetting-Bootable:

``boolean`` **Bootable**

    Bootable flag of the partition. It should be enabled if you want to boot off the partition.  The semantics vary between partition tables. For MS-DOS (MBR) partition table, only one partition can be bootable. If you are installing LILO on a partition that partition must be bootable.  For PC98 partition table, all ext2 partitions must be bootable (this is enforced by this API).

    
.. _LMI-DiskPartitionConfigurationSetting-Hidden:

``boolean`` **Hidden**

    Flag can be enabled to hide partitions from Microsoft operating systems.

    
.. _LMI-DiskPartitionConfigurationSetting-PartitionType:

``uint16`` **PartitionType**

    Partition type of the partition which is going to be created/modified. It should be used only for MS-DOS (MBR/EMBR) partition tables.

    
    ======== ========
    ValueMap Values  
    ======== ========
    0        Unknown 
    1        Primary 
    2        Extended
    3        Logical 
    ======== ========
    

Local methods
^^^^^^^^^^^^^

    .. _LMI-DiskPartitionConfigurationSetting-CloneSetting:

``uint32`` **CloneSetting** (:ref:`CIM_StorageSetting <CIM-StorageSetting>` Clone)

    Create a copy of this instance. The resulting instance will have the same class and the same properties as the original instance except ChangeableType, which will be set to "Changeable - Transient" in the clone, and InstanceID.

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Success      
    1        Not Supported
    4        Failed       
    ======== =============
    
    **Parameters**
    
        *OUT* :ref:`CIM_StorageSetting <CIM-StorageSetting>` **Clone**
            Created copy.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`SoOrgID <CIM-SettingData-SoOrgID>`
| ``string`` :ref:`SoID <CIM-SettingData-SoID>`
| ``string`` :ref:`ElementName <CIM-SettingData-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`ChangeableType <CIM-SettingData-ChangeableType>`
| ``string[]`` :ref:`ComponentSetting <CIM-SettingData-ComponentSetting>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`InstanceID <CIM-SettingData-InstanceID>`
| ``string`` :ref:`ConfigurationName <CIM-SettingData-ConfigurationName>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

