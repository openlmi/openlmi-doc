.. _CIM-StorageCapabilities:

CIM_StorageCapabilities
-----------------------

Class reference
===============
Subclass of :ref:`CIM_Capabilities <CIM-Capabilities>`

A subclass of Capabilities that defines the Capabilities of a StorageService or StoragePool. For example, an instance of StorageCapabilities could be associated with either a StorageConfigurationService or StoragePool by using ElementCapabilities.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-StorageCapabilities-SupportedDataOrganizations:

``uint16[]`` **SupportedDataOrganizations**

    Types of volume data organizations supported.

    
    ======== ==============
    ValueMap Values        
    ======== ==============
    0        Other         
    1        Unknown       
    2        Fixed Block   
    3        Variable Block
    4        Count Key Data
    ======== ==============
    
.. _CIM-StorageCapabilities-AvailableRPM:

``uint32[]`` **AvailableRPM**

    The rotational speed of disk media which are be available. Values are in revolutions per minute. SSD devices shall report 0.

    
.. _CIM-StorageCapabilities-PackageRedundancyMax:

``uint16`` **PackageRedundancyMax**

    PackageRedundancyMax describes the maximum number of redundant packages that can be used. For example, in the storage domain, package redundancy describes how many disk spindles can fail without data loss including, at most, one spare. An example would be RAID5 with a spare disk which would have a PackageRedundancy of 2. Possible values are 0 to n. The default redundancy is specified using PackageRedundancyDefault, while the maximum is defined by PackageRedundancyMax.

    
.. _CIM-StorageCapabilities-DataRedundancyMin:

``uint16`` **DataRedundancyMin**

    DataRedundancyMin describes the minimum number of complete copies of data that can be maintained. Examples would be RAID 5 where 1 copy is maintained and RAID 1 where 2 or more copies are maintained). Possible values are 1 to n. The default redundancy is specified using DataRedundancyDefault, while the maximum is defined by DataRedundancyMax.

    
.. _CIM-StorageCapabilities-Encryption:

``uint16`` **Encryption**

    This property reflects support of the encryption feature implemented by some disk drives.

    
    ======== =============
    ValueMap Values       
    ======== =============
    0        Unknown      
    1        Not Supported
    2        Supported    
    ======== =============
    
.. _CIM-StorageCapabilities-NoSinglePointOfFailure:

``boolean`` **NoSinglePointOfFailure**

    Indicates whether or not the associated element supports no single point of failure. Values are: FALSE = does not support no single point of failure, and TRUE = supports no single point of failure.

    
.. _CIM-StorageCapabilities-PackageRedundancyDefault:

``uint16`` **PackageRedundancyDefault**

    PackageRedundancyDefault describes the default number of redundant packages that will be used. For example, in the storage domain, package redundancy describes how many disk spindles can fail without data loss including, at most, one spare. An example would be RAID5 with a spare disk which would have a PackageRedundancy of 2. Possible values are 0 to n. The bounds for redundancy are specified using the properties, PackageRedundancyMax and PackageRedundancyMin.

    
.. _CIM-StorageCapabilities-ElementType:

``uint16`` **ElementType**

    Enumeration indicating the type of element to which this StorageCapabilities applies.

    
    ======== ===========================
    ValueMap Values                     
    ======== ===========================
    0        Unknown                    
    1        Reserved                   
    2        Any Type                   
    3        StorageVolume              
    4        StorageExtent              
    5        StoragePool                
    6        StorageConfigurationService
    7        LogicalDisk                
    8        StorageTier                
    ======== ===========================
    
.. _CIM-StorageCapabilities-AvailableDiskType:

``uint16[]`` **AvailableDiskType**

    Enumeration indicating the type of DiskDrives which may be available.

    
    ======== =================
    ValueMap Values           
    ======== =================
    0        Unknown          
    1        Other            
    2        Hard Disk Drive  
    3        Solid State Drive
    4        Hybrid           
    ======== =================
    
.. _CIM-StorageCapabilities-DataRedundancyDefault:

``uint16`` **DataRedundancyDefault**

    DataRedundancyDefault describes the default number of complete copies of data that can be maintained. Examples would be RAID 5 where 1 copy is maintained and RAID 1 where 2 or more copies are maintained. Possible values are 1 to n. The bounds for the redundancy (max and min) are defined by DataRedundancyMax and DataRedundancyMin.

    
.. _CIM-StorageCapabilities-AvailableInterconnectSpeed:

``uint64[]`` **AvailableInterconnectSpeed**

    The speed of disk interfaces which are be available. Values are in bits/second.

    
.. _CIM-StorageCapabilities-NoSinglePointOfFailureDefault:

``boolean`` **NoSinglePointOfFailureDefault**

    Indicates the default value for the NoSinglePointOfFailure property.

    
.. _CIM-StorageCapabilities-SupportedCompressionRates:

``uint16[]`` **SupportedCompressionRates**

    The SupportedCompressionRates identifies the compression rates that are supported by the implementation, including "None". If "None" is specified, then no other rate may be identified.

    
    ============ ======================
    ValueMap     Values                
    ============ ======================
    1            None                  
    2            High                  
    3            Medium                
    4            Low                   
    5            DMTF Reserved         
    ..           Implementation Decides
    32768..65535 Vendor Specific       
    ============ ======================
    
.. _CIM-StorageCapabilities-ParityLayoutDefault:

``uint16`` **ParityLayoutDefault**

    ParityLayout specifies whether a parity-based storage organization is using rotated or non-rotated parity. If this capabilities instance is associated with a pool that was created with a range of QOS then ParityLayoutDefault represents the default value. Other available values can be determined by using the 'GetSupportedParityLayouts' method. If the pool was created with a single specific QOS, representing a Raid group, set, or rank, then this property represents the current/fixed value for the pool, and ParityLayout is not supported in subsequent creation of elements from this pool. Consequently, the 'GetSupportedParityLayouts' method cannot be used, and the ParityLayoutGoal property in StorageSetting instances used in child element operations on this pool MUST be set to NULL. A NULL value for ParityLayoutDefault indicates that the system does not support configuration of storage by specifying ParityLayout.

    
    ======== ==================
    ValueMap Values            
    ======== ==================
    2        Non-Rotated Parity
    3        Rotated Parity    
    ======== ==================
    
.. _CIM-StorageCapabilities-DeltaReservationMin:

``uint16`` **DeltaReservationMin**

    DeltaReservationMin is a number between 1 (1%) and a 100 (100%) that specifies the minimum amount of space that should be reserved in a replica for caching changes. For a complete copy this would be 100%, but it can be lower in some implementations. This parameter sets the lower limit, while DeltaReservationMax sets the upper limit.

    
.. _CIM-StorageCapabilities-DeltaReservationDefault:

``uint16`` **DeltaReservationDefault**

    Delta reservation is a number between 1 (1%) and a 100 (100%) that specifies how much space should be reserved by default in a replica for caching changes. For a complete copy this would be 100%, but it can be lower in some implementations. This parameter sets the default value, while DeletaReservationMax and DeltReservationMin set the upper and lower bounds.

    
.. _CIM-StorageCapabilities-DeltaReservationMax:

``uint16`` **DeltaReservationMax**

    DeltaReservatioMax is a number between 1 (1%) and a 100 (100%) that specifies the maximum amount of space reserved in a replica for caching changes. For a complete copy this would be 100%, but it can be lower in some implementations. This parameter sets the upper limit, while DeltaReservationMin sets the lower limit.

    
.. _CIM-StorageCapabilities-AvailableInterconnectType:

``uint16[]`` **AvailableInterconnectType**

    Enumeration indicating the type of disk interfaces which may be available.

    
    ======== ========
    ValueMap Values  
    ======== ========
    0        Unknown 
    1        other   
    2        SAS     
    3        SATA    
    4        SAS/SATA
    5        FC      
    6        SOP     
    ======== ========
    
.. _CIM-StorageCapabilities-ExtentStripeLengthDefault:

``uint16`` **ExtentStripeLengthDefault**

    Extent Stripe Length describes the number of underlying StorageExtents across which data is striped in the common striping-based storage organizations. This is also known as the number of 'members' or 'columns'. 

    A NULL value for ExtentStripeLengthDefault indicates that the system does not support configuration of storage by specifying Stripe Length. 

    If Extent Stripe Length is supported, and this Capabilities instance is associated with a pool that was created with a range of QOS then ExtentStripeLengthDefault represents the default value. Other available values(such as min, max, and discrete values) can be determined by using the 'GetSupportedStripeLengths' and 'GetSupportedStripeLengthRange' methods. 

    If Extent Stripe Length is supported and the pool was created with a single specific QOS, representing a Raid group, set, or rank, then this property represents the current/fixed value for the pool, and Extent Stripe Length is not supported in subsequent creation of elements from this pool. Consequently, the 'GetSupportedStripeLength' methods cannot be used, and in a StorageSetting instance used as a goal when creating or modifying a child element of the pool, ExtentStripeLengthGoal, ExtentStripeLengthMin, and ExtentStripeLengthMax MUST be set to NULL.

    
.. _CIM-StorageCapabilities-AvailableFormFactorType:

``uint16[]`` **AvailableFormFactorType**

    Enumeration indicating the types of disk form factors which may be available.

    
    ======== ============
    ValueMap Values      
    ======== ============
    0        Unknown     
    1        Other       
    2        Not Reported
    3        5.25 inch   
    4        3.5 inch    
    5        2.5 inch    
    6        1.8 inch    
    ======== ============
    
.. _CIM-StorageCapabilities-DataRedundancyMax:

``uint16`` **DataRedundancyMax**

    DataRedundancyMax describes the maximum number of complete copies of data that can be maintained. Examples would be RAID 5 (where 1 copy is maintained) and RAID 1 (where 2 or more copies are maintained). Possible values are 1 to n. The default redundancy is specified using DataRedundancyDefault, while the minimum is defined by DataRedundancyMin.

    
.. _CIM-StorageCapabilities-PackageRedundancyMin:

``uint16`` **PackageRedundancyMin**

    PackageRedundancyMin describes the minimum number of redundant packages that can be used. For example, in the storage domain, package redundancy describes how many disk spindles can fail without data loss including, at most, one spare. An example would be RAID5 with a spare disk which would have a PackageRedundancy of 2. Possible values are 0 to n. The default redundancy is specified using PackageRedundancyDefault, while the minimum is defined by PackageRedundancyMin.

    
.. _CIM-StorageCapabilities-UserDataStripeDepthDefault:

``uint64`` **UserDataStripeDepthDefault**

    User Data Stripe Depth describes the number of bytes forming a strip in common striping-based storage organizations. The strip is defined as the size of the portion of a stripe that lies on one extent. Thus, ExtentStripeLength * UserDataStripeDepth will yield the size of one stripe of user data. A NULL value for UserDataStripeDepthDefault indicates that the system does not support configuration of storage by specifying Stripe Depth. 

    If User Data Stripe Depth is supported, and this Capabilities instance is associated with a pool that was created with a range of QOS then UserDataStripeDepthDefault represents the default value. Other available values(such as min, max, and discrete values) can be determined by using the 'GetSupportedStripeDepths' and 'GetSupportedStripeDepthRange' methods. 

    If User Data Stripe Depth is supported and the pool was created with a single specific QOS, representing a Raid group, set, or rank, then this property represents the current/fixed value for the pool, and User Data Stripe Depth is not supported in subsequent creation of elements from this pool. Consequently, the 'GetSupportedStripeDepth' methods cannot be used, and in a StorageSetting instance used as a goal when creating or modifying a child element of the pool, UserDataStripeDepthGoal, UserDataStripeDepthMin, and UserDataStripeDepthMax MUST be set to NULL.

    

Local methods
^^^^^^^^^^^^^

    .. _CIM-StorageCapabilities-GetSupportedStripeLengths:

``uint32`` **GetSupportedStripeLengths** (``uint16[]`` StripeLengths)

    For systems that support discrete ExtentStripeLengths for volume or pool creation, this method can be used to retrieve a list of supported values. Note that different implementations may support either the GetSupportedStripeLengths or the GetSupportedStripeLengthRange method. Also note that the advertised sizes may change after the call due to requests from other clients. If the system only supports a range of sizes, then the return value will be set to 3.

    
    ======== =========================================
    ValueMap Values                                   
    ======== =========================================
    0        Method completed OK                      
    1        Method not supported                     
    2        Choices not available for this Capability
    3        Use GetSupportedStripeLengthRange instead
    ======== =========================================
    
    **Parameters**
    
        *OUT* ``uint16[]`` **StripeLengths**
            List of supported ExtentStripeLengths for a Volume/Pool creation or modification.

            
        
    
    .. _CIM-StorageCapabilities-GetSupportedParityLayouts:

``uint32`` **GetSupportedParityLayouts** (``uint16[]`` ParityLayout)

    For systems that support Parity-based storage organizations for volume or pool creation, this method can be used to the supported parity layouts.

    
    ======== =========================================
    ValueMap Values                                   
    ======== =========================================
    0        Method completed OK                      
    1        Method not supported                     
    2        Choice not aavailable for this capability
    ======== =========================================
    
    **Parameters**
    
        *OUT* ``uint16[]`` **ParityLayout**
            List of supported Parity for a Volume/Pool creation or modification.

            
            ======== ==================
            ValueMap Values            
            ======== ==================
            2        Non-Rotated Parity
            3        Rotated Parity    
            ======== ==================
            
        
    
    .. _CIM-StorageCapabilities-GetSupportedStripeDepthRange:

``uint32`` **GetSupportedStripeDepthRange** (``uint64`` MinimumStripeDepth, ``uint64`` MaximumStripeDepth, ``uint64`` StripeDepthDivisor)

    For systems that support a range of UserDataStripeDepths for volume or pool creation, this method can be used to retrieve the supported range. Note that different implementations may support either the GetSupportedStripeDepths or the GetSupportedStripeDepthRange method. If the system only supports discrete values, then the return value will be set to 2.

    
    ======== ====================================
    ValueMap Values                              
    ======== ====================================
    0        Method completed OK                 
    1        Method not supported                
    2        Use GetSupportedStripeDepths instead
    ======== ====================================
    
    **Parameters**
    
        *OUT* ``uint64`` **MinimumStripeDepth**
            The minimum UserDataStripeDepth for a volume/pool in bytes.

            
        
        *OUT* ``uint64`` **MaximumStripeDepth**
            The maximum UserDataStripeDepth for a volume/pool in bytes.

            
        
        *OUT* ``uint64`` **StripeDepthDivisor**
            A volume/pool UserDataStripeDepth must be a multiple of this value which is specified in bytes.

            
        
    
    .. _CIM-StorageCapabilities-GetSupportedStripeLengthRange:

``uint32`` **GetSupportedStripeLengthRange** (``uint16`` MinimumStripeLength, ``uint16`` MaximumStripeLength, ``uint32`` StripeLengthDivisor)

    For systems that support a range of ExtentStripeLengths for volume or pool creation, this method can be used to retrieve the supported range. Note that different implementations may support either the GetSupportedExtentLengths or the GetSupportedExtentLengthRange method. Also note that the advertised sizes may change after the call due to requests from other clients. If the system only supports discrete values, then the return value will be set to 3.

    
    ======== =========================================
    ValueMap Values                                   
    ======== =========================================
    0        Method completed OK                      
    1        Method not supported                     
    2        Choices not available for this Capability
    3        Use GetSupportedStripeLengths instead    
    ======== =========================================
    
    **Parameters**
    
        *OUT* ``uint16`` **MinimumStripeLength**
            The minimum ExtentStripeDepth for a volume/pool in bytes.

            
        
        *OUT* ``uint16`` **MaximumStripeLength**
            The maximum ExtentStripeLength for a volume/pool in bytes.

            
        
        *OUT* ``uint32`` **StripeLengthDivisor**
            A volume/pool ExtentStripeLength must be a multiple of this value which is specified in bytes.

            
        
    
    .. _CIM-StorageCapabilities-GetSupportedStripeDepths:

``uint32`` **GetSupportedStripeDepths** (``uint64[]`` StripeDepths)

    For systems that support discrete UserDataStripeDepths for volume or pool creation, this method can be used to retrieve a list of supported values. Note that different implementations may support either the GetSupportedStripeDepths or the GetSupportedStripeDepthRange method. If the system only supports a range of sizes, then the return value will be set to 2.

    
    ======== ========================================
    ValueMap Values                                  
    ======== ========================================
    0        Method completed OK                     
    1        Method not supported                    
    2        Use GetSupportedStripeDepthRange instead
    ======== ========================================
    
    **Parameters**
    
        *OUT* ``uint64[]`` **StripeDepths**
            List of supported UserDataStripeDepths for a Volume/Pool creation or modification.

            
        
    
    .. _CIM-StorageCapabilities-CreateSetting:

``uint32`` **CreateSetting** (``uint16`` SettingType, :ref:`CIM_StorageSetting <CIM-StorageSetting>` NewSetting)

    Method to create and populate a StorageSetting instance from a StorageCapability instance. This removes the need to populate default settings and other settings in the context of each StorageCapabilities (which could be numerous). If the underlying instrumentation supports the StorageSettingWithHints subclass, then an instance of that class will be created instead.

    
    ============ =================
    ValueMap     Values           
    ============ =================
    0            Success          
    1            Not Supported    
    2            Unspecified Error
    3            Timeout          
    4            Failed           
    5            Invalid Parameter
    ..           DMTF Reserved    
    32768..65535 Vendor Specific  
    ============ =================
    
    **Parameters**
    
        *IN* ``uint16`` **SettingType**
            If 'Default' is passed for the CreateDefault parameter, the Max, Goal, and Min setting attributes are set to the Default values of the parent StorageCapabilities when the instance is created. 

            If set to 'Goal' the new StorageSetting attributes are set to the related attributes of the parent StorageCapabilities, e.g. Min to Min, Goal to Default, and Max to Max. 

            

            This method maybe deprecated in lieu of intrinsics once limitations in the CIM Operations are addressed.

            
            ======== =======
            ValueMap Values 
            ======== =======
            2        Default
            3        Goal   
            ======== =======
            
        
        *OUT* :ref:`CIM_StorageSetting <CIM-StorageSetting>` **NewSetting**
            Reference to the created StorageSetting instance.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`InstanceID <CIM-Capabilities-InstanceID>`
| ``string`` :ref:`ElementName <CIM-Capabilities-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`CreateGoalSettings <CIM-Capabilities-CreateGoalSettings>`

