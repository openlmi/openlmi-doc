.. _LMI-StorageSetting:

LMI_StorageSetting
------------------

Class reference
===============
Subclass of :ref:`CIM_StorageSetting <CIM-StorageSetting>`

Abstract StorageSetting class. This class just defines persistence types of all LMI StorageSetting classes. All subclasses of LMI_StorageSetting can be persistently stored by modifying ChangeableType property.

Transient setting can be deleted during CIMOM restart or after configurable time.

In addition, all LMI_StorageSetting subclasses have Clone() method to easily create copy  the same setting.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-StorageSetting-DataRedundancyMin:

``uint16`` **DataRedundancyMin**

    DataRedundancyMin describes the minimum number of complete copies of data to be maintained. Examples would be RAID 5 where 1 copy is maintained and RAID 1 where 2 or more copies are maintained. Possible values are 1 to n. The desired redundancy is specified using DataRedundancyGoal, while the maximum is defined by DataRedundancyMax.

    
.. _LMI-StorageSetting-NoSinglePointOfFailure:

``boolean`` **NoSinglePointOfFailure**

    Indicates the desired value for No Single Point of Failure. Possible values are false = single point of failure, and true = no single point of failure.

    
.. _LMI-StorageSetting-ParityLayout:

``uint16`` **ParityLayout**

    ParityLayout specifies whether a parity-based storage organization is using rotated or non-rotated parity. When used in a goal setting instance, ParityLayout is the desired value. It MUST be set to NULL if the scoping StorageCapablities indicates that it is not supported in this context. If the property is supported, and is part of StorageSettingWithHints it MAY be set to NULL. If used it will constrain the effects of Hint selections. When used in a Setting instance associated to a Volume, this property indicates the specific value that the Volume was created with.

    
    ======== ==================
    ValueMap Values            
    ======== ==================
    1        Non-rotated Parity
    2        Rotated Parity    
    ======== ==================
    
.. _LMI-StorageSetting-PackageRedundancyMax:

``uint16`` **PackageRedundancyMax**

    PackageRedundancyMax describes the maximum number of redundant packages to be used. For example, in the storage domain, package redundancy describes how many disk spindles can fail without data loss including, at most, one spare. An example would be RAID5 with a spare disk which would have a PackageRedundancy of 2. Possible values are 0 to n. The desired redundancy is specified using PackageRedundancyGoal, while the minimum is defined by PackageRedundancyMin.

    
.. _LMI-StorageSetting-ExtentStripeLength:

``uint16`` **ExtentStripeLength**

    ExtentStripeLength describes the number of underlying StorageExtents across which data is striped in the common striping-based storage organizations. This is also known as the number of 'members' or 'columns'. When used in a goal setting instance, ExtentStripeLength is the optimal desired value. The bounds (max and min) for Stripe Length are defined using the properties ExtentStripeLengthMax and ExtentStripeLengthMin. ExtentStripeLength MUST be set to NULL if the scoping StorageCapablities indicates that it is not supported in this context. ExtentStripeLength can be used in conjunction with CreateOrModifyElementFromELements to explicitly configure storage. An example would be RAID 0+1 with mirroring two stripe sets, each set being three wide. In this case CreateOrModifyElementFromElements would be passed a goal setting with DataRedundancy = 2 and ExtentStripeLength = 3. The size of the InElements array would be 6 and would contain the StorageExtents to be used to construct the StorageElement as a RAID 0+1. ExtentStripeLengthMin and ExtentStripeLengthMax are meaningless and wouldbe set to NULL. If the property is supported, and is part of StorageSettingWithHints it MAY be set to NULL. If used it will constrain the effects of Hint selections. When used in a Setting instance associated to a Volume, this property indicates the specific value that the Volume was created with, and ExtentStripeLengthMin and ExtentStripeLengthMax will be set to the same specific value.

    
.. _LMI-StorageSetting-ExtentStripeLengthMin:

``uint16`` **ExtentStripeLengthMin**

    ExtentStripeLength describes the number of underlying StorageExtents across which data is striped in the common striping-based storage organizations. This is also known as the number of 'members' or 'columns'. When used in a goal setting instance, ExtentStripeLengthMin is the minimum acceptable value. The desired Stripe Length is specified using ExtentStripeLength, while the maximum is defined by ExtentStripeLengthMax. ExtentStripeLengthMin MUST be set to NULL if the scoping StorageCapablities indicates that it is not supported in this context. If the property is supported, and is part of StorageSettingWithHints it MAY be set to NULL. If used it will constrain the effects of Hint selections. When used in a Setting instance associated to a Volume, this property is set to the specific value of ExtentStripeLength.

    
.. _LMI-StorageSetting-DataRedundancyGoal:

``uint16`` **DataRedundancyGoal**

    DataRedundancyGoal describes the desired number of complete copies of data to be maintained. Examples would be RAID 5 where 1 copy is maintained and RAID 1 where 2 or more copies are maintained. Possible values are 1 to n. The bounds (max and min) for redundancy are defined using the properties, DataRedundancyMax and DataRedundancyMin.

    
.. _LMI-StorageSetting-ChangeableType:

``uint16`` **ChangeableType**

    Enumeration indicating the type of setting. "Fixed - Not Changeable" settings are primordial. These setting are defined at the implementor of the class. "Changeable - Transient" is the type of setting produced by the "CreateSetting" method. A client can subsequently request that the implementation persist the generated and potentially modified setting indefinately. Only a "Changeable - Transient" setting SHALL be converted to a "Changeable = Persistent" setting; the setting SHALL NOT be changed back.

    
    ======== =======================
    ValueMap Values                 
    ======== =======================
    0        Fixed - Not Changeable 
    1        Changeable - Transient 
    2        Changeable - Persistent
    ======== =======================
    
.. _LMI-StorageSetting-ExtentStripeLengthMax:

``uint16`` **ExtentStripeLengthMax**

    ExtentStripeLength describes the number of underlying StorageExtents across which data is striped in the common striping-based storage organizations. This is also known as the number of 'members' or 'columns'. When used in a goal setting instance, ExtentStripeLengthMax is the maximum acceptable value. The desired Stripe Length is specified using ExtentStripeLength, while the minimum is defined by ExtentStripeLengthMin. ExtentStripeLengthMax MUST be set to NULL if the scoping StorageCapablities indicates that it is not supported in this context. If the property is supported, and is part of StorageSettingWithHints it MAY be set to NULL. If used it will constrain the effects of Hint selections. When used in a Setting instance associated to a Volume, this property is set to the specific value of ExtentStripeLength.

    
.. _LMI-StorageSetting-PackageRedundancyGoal:

``uint16`` **PackageRedundancyGoal**

    PackageRedundancyGoal describes the desired number of redundant packages to be used. For example, in the storage domain, package redundancy describes how many disk spindles can fail without data loss including, at most, one spare. An example would be RAID5 with a spare disk which would have a PackageRedundancy of 2. Possible values are 0 to n. The bounds (max and min) for redundancy are defined using the properties, PackageRedundancyMax and PackageRedundancyMin.

    
.. _LMI-StorageSetting-DataRedundancyMax:

``uint16`` **DataRedundancyMax**

    DataRedundancyMax describes the maximum number of complete copies of data to be maintained. Examples would be RAID 5 where 1 copy is maintained and RAID 1 where 2 or more copies are maintained. Possible values are 1 to n. The desired redundancy is specified using DataRedundancyGoal, while the minimum is defined by DataRedundancyMin.

    
.. _LMI-StorageSetting-PackageRedundancyMin:

``uint16`` **PackageRedundancyMin**

    PackageRedundancyMin describes the minimum number of redundant packages to be used. For example, in the storage domain, package redundancy describes how many disk spindles can fail without data loss including, at most, one spare. An example would be RAID5 with a spare disk which would have a PackageRedundancy of 2. Possible values are 0 to n. The desired redundancy is specified using PackageRedundancyGoal, while the maximum is defined by PackageRedundancyMax.

    

Local methods
^^^^^^^^^^^^^

    .. _LMI-StorageSetting-CloneSetting:

``uint32`` **CloneSetting** (:ref:`LMI_StorageSetting <LMI-StorageSetting>` Clone)

    Create a copy of this instance. The resulting instance will have the same class and the same properties as the original instance except ChangeableType, which will be set to "Changeable - Transient" in the clone, and InstanceID.

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Success      
    1        Not Supported
    4        Failed       
    ======== =============
    
    **Parameters**
    
        *OUT* :ref:`LMI_StorageSetting <LMI-StorageSetting>` **Clone**
            Created copy.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint64`` :ref:`InterconnectSpeed <CIM-StorageSetting-InterconnectSpeed>`
| ``uint16`` :ref:`InterconnectType <CIM-StorageSetting-InterconnectType>`
| ``uint8`` :ref:`DeltaReservationGoal <CIM-StorageSetting-DeltaReservationGoal>`
| ``uint16`` :ref:`UseReplicationBuffer <CIM-StorageSetting-UseReplicationBuffer>`
| ``string`` :ref:`InstanceID <CIM-SettingData-InstanceID>`
| ``uint16`` :ref:`LowSpaceWarningThreshold <CIM-StorageSetting-LowSpaceWarningThreshold>`
| ``uint16`` :ref:`DiskType <CIM-StorageSetting-DiskType>`
| ``string`` :ref:`SubsystemID <CIM-StorageSetting-SubsystemID>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`DataOrganization <CIM-StorageSetting-DataOrganization>`
| ``uint64`` :ref:`UserDataStripeDepthMin <CIM-StorageSetting-UserDataStripeDepthMin>`
| ``string`` :ref:`EmulatedDevice <CIM-StorageSetting-EmulatedDevice>`
| ``uint16`` :ref:`CompressionRate <CIM-StorageSetting-CompressionRate>`
| ``uint16`` :ref:`ThinProvisionedPoolType <CIM-StorageSetting-ThinProvisionedPoolType>`
| ``uint16`` :ref:`FormFactorType <CIM-StorageSetting-FormFactorType>`
| ``string`` :ref:`ConfigurationName <CIM-SettingData-ConfigurationName>`
| ``boolean`` :ref:`CompressedElement <CIM-StorageSetting-CompressedElement>`
| ``string`` :ref:`CUImage <CIM-StorageSetting-CUImage>`
| ``string`` :ref:`SoOrgID <CIM-SettingData-SoOrgID>`
| ``boolean`` :ref:`PersistentReplica <CIM-StorageSetting-PersistentReplica>`
| ``uint16`` :ref:`InitialSynchronization <CIM-StorageSetting-InitialSynchronization>`
| ``uint16`` :ref:`Encryption <CIM-StorageSetting-Encryption>`
| ``uint16`` :ref:`StorageExtentInitialUsage <CIM-StorageSetting-StorageExtentInitialUsage>`
| ``string`` :ref:`ElementName <CIM-SettingData-ElementName>`
| ``uint64`` :ref:`ThinProvisionedInitialReserve <CIM-StorageSetting-ThinProvisionedInitialReserve>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16`` :ref:`PortType <CIM-StorageSetting-PortType>`
| ``boolean`` :ref:`IncrementalDeltas <CIM-StorageSetting-IncrementalDeltas>`
| ``uint16`` :ref:`StoragePoolInitialUsage <CIM-StorageSetting-StoragePoolInitialUsage>`
| ``string`` :ref:`SoID <CIM-SettingData-SoID>`
| ``uint16`` :ref:`ReplicationPriority <CIM-StorageSetting-ReplicationPriority>`
| ``uint8`` :ref:`DeltaReservationMin <CIM-StorageSetting-DeltaReservationMin>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint32`` :ref:`RPM <CIM-StorageSetting-RPM>`
| ``uint64`` :ref:`UserDataStripeDepthMax <CIM-StorageSetting-UserDataStripeDepthMax>`
| ``uint64`` :ref:`SpaceLimit <CIM-StorageSetting-SpaceLimit>`
| ``uint16`` :ref:`SpaceLimitWarningThreshold <CIM-StorageSetting-SpaceLimitWarningThreshold>`
| ``string[]`` :ref:`ComponentSetting <CIM-SettingData-ComponentSetting>`
| ``uint8`` :ref:`DeltaReservationMax <CIM-StorageSetting-DeltaReservationMax>`
| ``uint64`` :ref:`UserDataStripeDepth <CIM-StorageSetting-UserDataStripeDepth>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

