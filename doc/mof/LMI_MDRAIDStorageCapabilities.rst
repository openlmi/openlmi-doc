.. _LMI-MDRAIDStorageCapabilities:

LMI_MDRAIDStorageCapabilities
-----------------------------

Class reference
===============
Subclass of :ref:`CIM_StorageCapabilities <CIM-StorageCapabilities>`

This class represents capability of LMI_StorageConfigurationService to create MD RAID arrays. It describes, which properties and which values can be used in LMI_MDRAIDStorageSetting.

There are no additional properties for now.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-MDRAIDStorageCapabilities-PackageRedundancyMax:

``uint16`` **PackageRedundancyMax**

    PackageRedundancyMax describes the maximum number of redundant packages that can be used. For example, in the storage domain, package redundancy describes how many disk spindles can fail without data loss including, at most, one spare. An example would be RAID5 with a spare disk which would have a PackageRedundancy of 2. Possible values are 0 to n. The default redundancy is specified using PackageRedundancyDefault, while the maximum is defined by PackageRedundancyMax.

    
.. _LMI-MDRAIDStorageCapabilities-DataRedundancyMin:

``uint16`` **DataRedundancyMin**

    DataRedundancyMin describes the minimum number of complete copies of data that can be maintained. Examples would be RAID 5 where 1 copy is maintained and RAID 1 where 2 or more copies are maintained). Possible values are 1 to n. The default redundancy is specified using DataRedundancyDefault, while the maximum is defined by DataRedundancyMax.

    
.. _LMI-MDRAIDStorageCapabilities-NoSinglePointOfFailure:

``boolean`` **NoSinglePointOfFailure**

    Indicates whether or not the associated element supports no single point of failure. Values are: FALSE = does not support no single point of failure, and TRUE = supports no single point of failure.

    
.. _LMI-MDRAIDStorageCapabilities-PackageRedundancyDefault:

``uint16`` **PackageRedundancyDefault**

    PackageRedundancyDefault describes the default number of redundant packages that will be used. For example, in the storage domain, package redundancy describes how many disk spindles can fail without data loss including, at most, one spare. An example would be RAID5 with a spare disk which would have a PackageRedundancy of 2. Possible values are 0 to n. The bounds for redundancy are specified using the properties, PackageRedundancyMax and PackageRedundancyMin.

    
.. _LMI-MDRAIDStorageCapabilities-ElementName:

``string`` **ElementName**

    The user friendly name for this instance of Capabilities. In addition, the user friendly name can be used as a index property for a search of query. (Note: Name does not have to be unique within a namespace.)

    
.. _LMI-MDRAIDStorageCapabilities-DataRedundancyDefault:

``uint16`` **DataRedundancyDefault**

    DataRedundancyDefault describes the default number of complete copies of data that can be maintained. Examples would be RAID 5 where 1 copy is maintained and RAID 1 where 2 or more copies are maintained. Possible values are 1 to n. The bounds for the redundancy (max and min) are defined by DataRedundancyMax and DataRedundancyMin.

    
.. _LMI-MDRAIDStorageCapabilities-NoSinglePointOfFailureDefault:

``boolean`` **NoSinglePointOfFailureDefault**

    Indicates the default value for the NoSinglePointOfFailure property.

    
.. _LMI-MDRAIDStorageCapabilities-ExtentStripeLengthDefault:

``uint16`` **ExtentStripeLengthDefault**

    Extent Stripe Length describes the number of underlying StorageExtents across which data is striped in the common striping-based storage organizations. This is also known as the number of 'members' or 'columns'. 

    A NULL value for ExtentStripeLengthDefault indicates that the system does not support configuration of storage by specifying Stripe Length. 

    If Extent Stripe Length is supported, and this Capabilities instance is associated with a pool that was created with a range of QOS then ExtentStripeLengthDefault represents the default value. Other available values(such as min, max, and discrete values) can be determined by using the 'GetSupportedStripeLengths' and 'GetSupportedStripeLengthRange' methods. 

    If Extent Stripe Length is supported and the pool was created with a single specific QOS, representing a Raid group, set, or rank, then this property represents the current/fixed value for the pool, and Extent Stripe Length is not supported in subsequent creation of elements from this pool. Consequently, the 'GetSupportedStripeLength' methods cannot be used, and in a StorageSetting instance used as a goal when creating or modifying a child element of the pool, ExtentStripeLengthGoal, ExtentStripeLengthMin, and ExtentStripeLengthMax MUST be set to NULL.

    
.. _LMI-MDRAIDStorageCapabilities-DataRedundancyMax:

``uint16`` **DataRedundancyMax**

    DataRedundancyMax describes the maximum number of complete copies of data that can be maintained. Examples would be RAID 5 (where 1 copy is maintained) and RAID 1 (where 2 or more copies are maintained). Possible values are 1 to n. The default redundancy is specified using DataRedundancyDefault, while the minimum is defined by DataRedundancyMin.

    
.. _LMI-MDRAIDStorageCapabilities-PackageRedundancyMin:

``uint16`` **PackageRedundancyMin**

    PackageRedundancyMin describes the minimum number of redundant packages that can be used. For example, in the storage domain, package redundancy describes how many disk spindles can fail without data loss including, at most, one spare. An example would be RAID5 with a spare disk which would have a PackageRedundancy of 2. Possible values are 0 to n. The default redundancy is specified using PackageRedundancyDefault, while the minimum is defined by PackageRedundancyMin.

    

Local methods
^^^^^^^^^^^^^

    .. _LMI-MDRAIDStorageCapabilities-CreateMDRAIDStorageSetting:

``uint32`` **CreateMDRAIDStorageSetting** (``uint16`` Level, :ref:`CIM_StorageExtent[] <CIM-StorageExtent>` InExtents, :ref:`LMI_StorageSetting <LMI-StorageSetting>` Setting)

    This method creates new instance of LMI_MDRAIDStorageSetting, which will represent given RAID level. Applications then do not need to calculate DataRedundancy, PackageRedundancy and ExtentStripeLength.

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Success      
    1        Not Supported
    4        Failed       
    ======== =============
    
    **Parameters**
    
        *IN* ``uint16`` **Level**
            Requested level.

            
            ======== ======
            ValueMap Values
            ======== ======
            0        RAID0 
            1        RAID1 
            4        RAID4 
            5        RAID5 
            6        RAID6 
            10       RAID10
            ======== ======
            
        
        *IN* :ref:`CIM_StorageExtent[] <CIM-StorageExtent>` **InExtents**
            List of devices, from which the new device will be created. The created LMI_MDRAIDStorageSetting will take redundancy and striping of these devices into account. 

            For example, if the application wants to create RAID0 on top of two RAID1 devices, it passes InExtents = (FirstRAID1Extent, SecondRAID1Extent) and Level=0. Resulting LMI_MDRAIDStorageSetting will have DataRedundancy and PackageRedundancy as the minimum of the first and the second RAID1 extents and ExtentStripeLength will be 2 to indicate RAID0 with two devices.

            
        
        *OUT* :ref:`LMI_StorageSetting <LMI-StorageSetting>` **Setting**
            Created LMI_StorageSetting.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16[]`` :ref:`SupportedDataOrganizations <CIM-StorageCapabilities-SupportedDataOrganizations>`
| ``uint32[]`` :ref:`AvailableRPM <CIM-StorageCapabilities-AvailableRPM>`
| ``string`` :ref:`InstanceID <CIM-Capabilities-InstanceID>`
| ``uint16`` :ref:`Encryption <CIM-StorageCapabilities-Encryption>`
| ``uint16`` :ref:`ParityLayoutDefault <CIM-StorageCapabilities-ParityLayoutDefault>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16[]`` :ref:`AvailableDiskType <CIM-StorageCapabilities-AvailableDiskType>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint64[]`` :ref:`AvailableInterconnectSpeed <CIM-StorageCapabilities-AvailableInterconnectSpeed>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16[]`` :ref:`SupportedCompressionRates <CIM-StorageCapabilities-SupportedCompressionRates>`
| ``uint16`` :ref:`ElementType <CIM-StorageCapabilities-ElementType>`
| ``uint16`` :ref:`DeltaReservationMin <CIM-StorageCapabilities-DeltaReservationMin>`
| ``uint16`` :ref:`DeltaReservationDefault <CIM-StorageCapabilities-DeltaReservationDefault>`
| ``uint16`` :ref:`DeltaReservationMax <CIM-StorageCapabilities-DeltaReservationMax>`
| ``uint16[]`` :ref:`AvailableInterconnectType <CIM-StorageCapabilities-AvailableInterconnectType>`
| ``uint16[]`` :ref:`AvailableFormFactorType <CIM-StorageCapabilities-AvailableFormFactorType>`
| ``uint64`` :ref:`UserDataStripeDepthDefault <CIM-StorageCapabilities-UserDataStripeDepthDefault>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`GetSupportedStripeLengths <CIM-StorageCapabilities-GetSupportedStripeLengths>`
| :ref:`GetSupportedParityLayouts <CIM-StorageCapabilities-GetSupportedParityLayouts>`
| :ref:`GetSupportedStripeDepthRange <CIM-StorageCapabilities-GetSupportedStripeDepthRange>`
| :ref:`CreateGoalSettings <CIM-Capabilities-CreateGoalSettings>`
| :ref:`GetSupportedStripeLengthRange <CIM-StorageCapabilities-GetSupportedStripeLengthRange>`
| :ref:`GetSupportedStripeDepths <CIM-StorageCapabilities-GetSupportedStripeDepths>`
| :ref:`CreateSetting <CIM-StorageCapabilities-CreateSetting>`

