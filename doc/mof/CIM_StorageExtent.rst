.. _CIM-StorageExtent:

CIM_StorageExtent
-----------------

Class reference
===============
Subclass of :ref:`CIM_LogicalDevice <CIM-LogicalDevice>`

StorageExtent describes the capabilities and management of the various media that exist to store data and allow data retrieval. This superclass could be used to represent the various components of RAID (Hardware or Software) or as a raw logical extent on top of physical media.


Key properties
^^^^^^^^^^^^^^

| :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-StorageExtent-DeltaReservation:

``uint8`` **DeltaReservation**

    Current value for Delta reservation. This is a percentage that specifies the amount of space that should be reserved in a replica for caching changes.

    
.. _CIM-StorageExtent-IsBasedOnUnderlyingRedundancy:

``boolean`` **IsBasedOnUnderlyingRedundancy**

    True indicates that the underlying StorageExtent(s) participate in a StorageRedundancyGroup.

    
.. _CIM-StorageExtent-ClientSettableUsage:

``uint16[]`` **ClientSettableUsage**

    Indicates which values from the "Usage" valuemap can be manipulated by a client using the method "StorageConfigurationService.RequestUsageChange".

    
.. _CIM-StorageExtent-IsCompressed:

``boolean`` **IsCompressed**

    The IsCompressed property indicates whether or not the data in the storage extent is compressed. When set to "true" the data is compressed. When set to "false" the data is not compressed.

    
.. _CIM-StorageExtent-DataOrganization:

``uint16`` **DataOrganization**

    Type of data organization used.

    
    ======== ==============
    ValueMap Values        
    ======== ==============
    0        Other         
    1        Unknown       
    2        Fixed Block   
    3        Variable Block
    4        Count Key Data
    ======== ==============
    
.. _CIM-StorageExtent-Access:

``uint16`` **Access**

    Access describes whether the media is readable (value=1), writeable (value=2), or both (value=3). "Unknown" (0) and "Write Once" (4) can also be defined.

    
    ======== ====================
    ValueMap Values              
    ======== ====================
    0        Unknown             
    1        Readable            
    2        Writeable           
    3        Read/Write Supported
    4        Write Once          
    ======== ====================
    
.. _CIM-StorageExtent-Primordial:

``boolean`` **Primordial**

    If true, "Primordial" indicates that the containing System does not have the ability to create or delete this operational element. This is important because StorageExtents are assembled into higher-level abstractions using the BasedOn association. Although the higher-level abstractions can be created and deleted, the most basic, (i.e. primordial), hardware-based storage entities cannot. They are physically realized as part of the System, or are actually managed by some other System and imported as if they were physically realized. In other words, a Primordial StorageExtent exists in, but is not created by its System and conversely a non-Primordial StorageExtent is created in the context of its System. For StorageVolumes, this property will generally be false. One use of this property is to enable algorithms that aggregate StorageExtent.ConsumableSpace across all, StorageExtents but that also want to distinquish the space that underlies Primordial StoragePools. Since implementations are not required to surface all Component StorageExtents of a StoragePool, this information is not accessible in any other way.

    
.. _CIM-StorageExtent-NoSinglePointOfFailure:

``boolean`` **NoSinglePointOfFailure**

    Indicates whether or not there exists no single point of failure.

    
.. _CIM-StorageExtent-Usage:

``uint16`` **Usage**

    Indicates the intended usage or any restrictions that may have been imposed on the usage of this component. For example, an element may be reserved for use by the block server. In that case the Usage of the element is marked as "Reserved for the ComputerSystem". In the case of "Other", see OtherUsageDescription for more information. In the value map, the "Element Component" indicates a StorageVolume or LogicalDisk that is only available as an EmbeddedInstance. The storage that it represents may also be represented as another StorageExent that is a component of another LogicalElement. 

    "Reserved to be Unrestricted Pool Contributor": Indicates the element is currently available and it is intended to be used as an Unrestricted Pool Contributor. Once such element is in use, the elements Usage value will change to "In use as Unrestricted Pool Contributor". 

    Use the method GetElementsBasedOnUsage to locate such volumes or logical disks.

    
    ============ ==================================================
    ValueMap     Values                                            
    ============ ==================================================
    1            Other                                             
    2            Unrestricted                                      
    3            Reserved for ComputerSystem (the block server)    
    4            Reserved by Replication Services                  
    5            Reserved by Migration Services                    
    6            Local Replica Source                              
    7            Remote Replica Source                             
    8            Local Replica Target                              
    9            Remote Replica Target                             
    10           Local Replica Source or Target                    
    11           Remote Replica Source or Target                   
    12           Delta Replica Target                              
    13           Element Component                                 
    14           Reserved to be Unrestricted Pool Contributor      
    15           Composite Volume Member                           
    16           Composite LogicalDisk Member                      
    17           Reserved for Sparing                              
    18           In use as Unrestricted Pool Contributor           
    19           Reserved to be Delta Replica Pool Contributor     
    20           Reserved to be Local Replication Pool Contributor 
    21           Reserved to be Remote Replication Pool Contributor
    22           In use as Delta Replica Pool Contributor          
    23           In use as Local Replication Pool Contributor      
    24           In use as Remote Replication Pool Contributor     
    ..           DMTF Reserved                                     
    32768..65535 Vendor Reserved                                   
    ============ ==================================================
    
.. _CIM-StorageExtent-OtherNameNamespace:

``string`` **OtherNameNamespace**

    A string describing the namespace of the Name property when NameNamespace includes the value 1, "Other".

    
.. _CIM-StorageExtent-ExtentInterleaveDepth:

``uint64`` **ExtentInterleaveDepth**

    If not null, then IsComposite shall be true. Number of StorageExtents to stripe as a collective set. In SCSI SCC, this value is defined as the number of stripes to count before continuing to map into the next contiguous set of Extents, beyond the current stripe.

    
.. _CIM-StorageExtent-OtherNameFormat:

``string`` **OtherNameFormat**

    A string describing the format of the Name property when NameFormat includes the value 1, "Other".

    
.. _CIM-StorageExtent-NameFormat:

``uint16`` **NameFormat**

    The list here applies to all StorageExtent subclasses. Please look at the Description in each subclass for guidelines on the approriate values for that subclass. Note that any of these formats could apply to a CompositeExtent. 

    

    Note - this property originally touched on two concepts that are now separated into this property and NameNamespace. Values 2,3,4,5,6, and 8 are retained for backwards compatibility but are deprecated in lieu of the corresponding values in CIM_StorageExtent.NameNamespace. 

    

    For example, the preferred source for SCSI virtual (RAID) disk names is from Inquiry VPD page 83 response, type 3 identifiers. These will have NameFormat set to 'NAA' and NameNamespace to 'VPD83Type3'. 

    

    Format of the Name property. Values for extents representing SCSI volumes are (per SCSI SPC-3): 

    2 = VPD Page 83, NAA IEEE Registered Extended (VPD83NAA6) 

    (DEPRECATED) 

    3 = VPD Page 83, NAA IEEE Registered (VPD83NAA5) 

    (DEPRECATED) 

    4 = VPD Page 83, (VPD83Type2) (DEPRECATED) 

    5 = VPD Page 83, 

    T10 Vendor Identification (VPD83Type1) (DEPRECATED) 

    6 = VPD Page 83, Vendor Specific (VPD83Type0) (DEPRECATED) 

    7 = Serial Number/Vendor/Model (SNVM) SNVM is 3 strings representing the vendor name, product name within the vendor namespace, and the serial number within the model namespace. Strings are delimited with a '+'. Spaces may be included and are significant. The serial number is the text representation of the serial number in hexadecimal upper case. This represents the vendor and model ID from SCSI Inquiry data; the vendor field MUST be 8 characters wide and the product field MUST be 16 characters wide. For example, 

    'ACME____+SUPER DISK______+124437458' (_ is a space character) 

    8 = Node WWN (for single LUN/controller) (NodeWWN) 

    (DEPRECATED) 

    9 = NAA as a generic format. See 

    http://standards.ieee.org/regauth/oui/tutorials/fibrecomp_id.html. Formatted as 16 or 32 unseparated uppercase hex characters (2 per binary byte). For example '21000020372D3C73' 

    10 = EUI as a generic format (EUI64) See 

    http://standards.ieee.org/regauth/oui/tutorials/EUI64.html. 

    Formatted as 16 unseparated uppercase hex characters (2 per binary byte) 

    11 = T10 vendor identifier format as returned by SCSI Inquiry VPD page 83, identifier type 1. See T10 SPC-3 specification. This is the 8-byte ASCII vendor ID from the T10 registry followed by a vendor specific ASCII identifier; spaces are permitted. For non SCSI volumes, 'SNVM' may be the most appropriate choice. 12 = OS Device Name (for LogicalDisks). See LogicalDisk Name description for details.

    
    ======== ==============
    ValueMap Values        
    ======== ==============
    0        Unknown       
    1        Other         
    2        VPD83NAA6     
    3        VPD83NAA5     
    4        VPD83Type2    
    5        VPD83Type1    
    6        VPD83Type0    
    7        SNVM          
    8        NodeWWN       
    9        NAA           
    10       EUI64         
    11       T10VID        
    12       OS Device Name
    ======== ==============
    
.. _CIM-StorageExtent-Purpose:

``string`` **Purpose**

    A free form string describing the media and/or its use.

    
.. _CIM-StorageExtent-ExtentStripeLength:

``uint64`` **ExtentStripeLength**

    If not null, then IsComposite shall be true. Number of contiguous underlying StorageExtents counted before looping back to the first underlying StorageExtent of the current stripe. It is the number of StorageExtents forming the user data stripe.

    
.. _CIM-StorageExtent-CompressionState:

``uint16`` **CompressionState**

    The CompressionState indicates whether the compression is pending, initializing, in progress or completed.

    
    ============ ===============
    ValueMap     Values         
    ============ ===============
    1            Not applicable 
    2            Initializing   
    3            InProgress     
    4            Pending        
    5            Completed      
    ..           DMTF Reserved  
    32768..65535 Vendor Specific
    ============ ===============
    
.. _CIM-StorageExtent-Name:

``string`` **Name**

    A unique identifier for the Extent.

    
.. _CIM-StorageExtent-BlockSize:

``uint64`` **BlockSize**

    Size in bytes of the blocks which form this StorageExtent. If variable block size, then the maximum block size in bytes should be specified. If the block size is unknown or if a block concept is not valid (for example, for AggregateExtents, Memory or LogicalDisks), enter a 1.

    
.. _CIM-StorageExtent-SequentialAccess:

``boolean`` **SequentialAccess**

    Boolean set to TRUE if the Storage is sequentially accessed by a MediaAccessDevice. A TapePartition is an example of a sequentially accessed StorageExtent. StorageVolumes, Disk Partitions and LogicalDisks represent randomly accessed Extents.

    
.. _CIM-StorageExtent-OtherUsageDescription:

``string`` **OtherUsageDescription**

    Populated when "Usage" has the value of "Other".

    
.. _CIM-StorageExtent-NameNamespace:

``uint16`` **NameNamespace**

    The preferred source SCSI for volume names is SCSI VPD Page 83 responses. Page 83 returns a list of identifiers for various device elements. The metadata for each identifier includes an Association field, identifiers with association of 0 apply to volumes. Page 83 supports several namespaces specified in the Type field in the identifier metadata. See SCSI SPC-3 specification. 

    2 = VPD Page 83, Type 3 NAA (NameFormat SHOULD be NAA) 

    3 = VPD Page 83, Type 2 EUI64 (NameFormat EUI) 

    4 = VPD Page 83, Type 1 T10 Vendor Identification 

    (NameFormat T10) 

    Less preferred volume namespaces from other interfaces: 

    5 = VPD page 80, Serial number (NameFormat SHOULD be Other) 

    6 = FC NodeWWN (NameFormat SHOULD be NAA or EUI) 

    7 = Serial Number/Vendor/Model (NameFormat SHOULD be SNVM) 

    The preferred namespace for LogigicalDisk names is platform specific device namespace; see LogigicalDIsk Description. 

    8 = OS Device Namespace.

    
    ======== ===================
    ValueMap Values             
    ======== ===================
    0        Unknown            
    1        Other              
    2        VPD83Type3         
    3        VPD83Type2         
    4        VPD83Type1         
    5        VPD80              
    6        NodeWWN            
    7        SNVM               
    8        OS Device Namespace
    ======== ===================
    
.. _CIM-StorageExtent-IsComposite:

``boolean`` **IsComposite**

    True indicates that the data is a composition of various StorageExtents that are associated to this StorageExtent via a CIM_BasedOn. Composition models the distribution of user data across one or more underlying StorageExtents, which may or not be protected by some redundancy mechanism. Composite extents represent a contiguous range of logical blocks. Composite extents may overlap, however, the underlying StorageExtents within the overlap shall not contain any check data. Distribution of check data may be specified using the CompositeExtentBasedOn association.

    
.. _CIM-StorageExtent-ExtentDiscriminator:

``string[]`` **ExtentDiscriminator**

    An array of strings used to discriminate the association context in which this StorageExtent is instantiated. Each element of the array should be prefixed by a well known organization name followed by a colon and followed by a string defined by that organization. For example, SNIA SMI-S compliant instances might contain one or more of the following values: 

    'SNIA:Pool Component' - A StorageExtent (or CompositeExtent) that represents storage of a StoragePool and has an AssociatedComponentExtent to its StoragePool, but is not a remaining extent. 

    'SNIA:Remaining' - A StorageExtent that has an AssociatedRemainingExtent to a StoragePool (representing free storage in the StoragePool). 

    'SNIA:Intermediate' - A StorageExtent (or CompositeExtent) that is neither a Pool Component nor a Remaining Extent (it does not represent storage in the pool, remaining or otherwise). 

    'SNIA:Composite' - A StorageExtent that is a CompositeExtent. 

    'SNIA:DiskDrive' - A StorageExtent that is the media on a Disk Drive. 

    'SNIA:Imported' - A StorageExtent that is imported from an external source. 

    'SNIA:Allocated' - A StorageExtent that is subclassed to StorageVolume or LogicalDisk, and has an AllocatedFromStoragePool association from a Concrete StoragePool. 

    'SNIA:Shadow' - A StorageExtent (or subclass) that represents a StorageExtent in another autonomous profile (e.g., the StorageVirtualizer has StorageVolumes (Shadow) that represent StorageVolumes exported by Arrays). 

    'SNIA:Spare' - A StorageExtent that acts as a spare for other StorageExtents (and has the IsSpare association). 

    'SNIA:Reserved' - A StorageExtent that is reserved for some system use within the autonomous profile (e.g., in NAS profiles, an Allocated LogicalDisk is reserved for holding Filesystems).

    
.. _CIM-StorageExtent-PackageRedundancy:

``uint16`` **PackageRedundancy**

    How many physical packages can currently fail without data loss. For example, in the storage domain, this might be disk spindles.

    
.. _CIM-StorageExtent-DataRedundancy:

``uint16`` **DataRedundancy**

    Number of complete copies of data currently maintained.

    
.. _CIM-StorageExtent-NumberOfBlocks:

``uint64`` **NumberOfBlocks**

    Total number of logically contiguous blocks, of size Block Size, which form this Extent. The total size of the Extent can be calculated by multiplying BlockSize by NumberOfBlocks. If the BlockSize is 1, this property is the total size of the Extent.

    
.. _CIM-StorageExtent-CompressionRate:

``uint16`` **CompressionRate**

    CompressionRate identifies whether or not compression is being applied to the volume and at what rate.

    
    ============ ===============
    ValueMap     Values         
    ============ ===============
    0            Unknown        
    1            None           
    2            High           
    3            Medium         
    4            Low            
    ..           DMTF Reserved  
    32768..65535 Vendor Specific
    ============ ===============
    
.. _CIM-StorageExtent-IsConcatenated:

``boolean`` **IsConcatenated**

    If not null, then IsComposite shall be true. True indicates that the data is concatenated across the various StorageExtents in the Group.

    
.. _CIM-StorageExtent-ErrorMethodology:

``string`` **ErrorMethodology**

    ErrorMethodology is a free-form string describing the type of error detection and correction supported by this StorageExtent.

    
.. _CIM-StorageExtent-ExtentStatus:

``uint16[]`` **ExtentStatus**

    StorageExtents have additional status information beyond that captured in the OperationalStatus and other properties, inherited from ManagedSystemElement. This additional information (for example, "Protection Disabled", value=9) is captured in the ExtentStatus property. 

    'In-Band Access Granted' says that access to data on an extent is granted to some consumer and is only valid when 'Exported' is also set. It is set as a side effect of PrivilegeManagementService.ChangeAccess or equivalent interfaces. 

    'Imported' indicates that the extent is used in the current system, but known to be managed by some other system. For example, a server imports volumes from a disk array. 

    'Exported' indicates the extent is meant to be used by some comsumer. A disk array's logical units are exported. 

    Intermediate composite extents may be neither imported nor exported.

    'Relocating' indicates the extent is being relocated.

    
    ============ ======================
    ValueMap     Values                
    ============ ======================
    0            Other                 
    1            Unknown               
    2            None/Not Applicable   
    3            Broken                
    4            Data Lost             
    5            Dynamic Reconfig      
    6            Exposed               
    7            Fractionally Exposed  
    8            Partially Exposed     
    9            Protection Disabled   
    10           Readying              
    11           Rebuild               
    12           Recalculate           
    13           Spare in Use          
    14           Verify In Progress    
    15           In-Band Access Granted
    16           Imported              
    17           Exported              
    18           Relocating            
    ..           DMTF Reserved         
    32768..65535 Vendor Reserved       
    ============ ======================
    
.. _CIM-StorageExtent-ConsumableBlocks:

``uint64`` **ConsumableBlocks**

    The maximum number of blocks, of size BlockSize, which are available for consumption when layering StorageExtents using the BasedOn association. This property only has meaning when this StorageExtent is an Antecedent reference in a BasedOn relationship. For example, a StorageExtent could be composed of 120 blocks. However, the Extent itself may use 20 blocks for redundancy data. If another StorageExtent is BasedOn this Extent, only 100 blocks would be available to it. This information ('100 blocks is available for consumption') is indicated in the ConsumableBlocks property.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`RequestedState <CIM-EnabledLogicalElement-RequestedState>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``boolean`` :ref:`PowerManagementSupported <CIM-LogicalDevice-PowerManagementSupported>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`SystemName <CIM-LogicalDevice-SystemName>`
| ``boolean`` :ref:`ErrorCleared <CIM-LogicalDevice-ErrorCleared>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``datetime`` :ref:`TimeOfLastStateChange <CIM-EnabledLogicalElement-TimeOfLastStateChange>`
| ``uint64`` :ref:`PowerOnHours <CIM-LogicalDevice-PowerOnHours>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string[]`` :ref:`IdentifyingDescriptions <CIM-LogicalDevice-IdentifyingDescriptions>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16`` :ref:`LocationIndicator <CIM-LogicalDevice-LocationIndicator>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string[]`` :ref:`OtherIdentifyingInfo <CIM-LogicalDevice-OtherIdentifyingInfo>`
| ``uint16[]`` :ref:`PowerManagementCapabilities <CIM-LogicalDevice-PowerManagementCapabilities>`
| ``uint16`` :ref:`EnabledDefault <CIM-EnabledLogicalElement-EnabledDefault>`
| ``uint16`` :ref:`EnabledState <CIM-EnabledLogicalElement-EnabledState>`
| ``uint16[]`` :ref:`AdditionalAvailability <CIM-LogicalDevice-AdditionalAvailability>`
| ``uint16`` :ref:`StatusInfo <CIM-LogicalDevice-StatusInfo>`
| ``string`` :ref:`DeviceID <CIM-LogicalDevice-DeviceID>`
| ``uint16[]`` :ref:`AvailableRequestedStates <CIM-EnabledLogicalElement-AvailableRequestedStates>`
| ``uint64`` :ref:`MaxQuiesceTime <CIM-LogicalDevice-MaxQuiesceTime>`
| ``uint16`` :ref:`TransitioningToState <CIM-EnabledLogicalElement-TransitioningToState>`
| ``uint64`` :ref:`TotalPowerOnHours <CIM-LogicalDevice-TotalPowerOnHours>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`ErrorDescription <CIM-LogicalDevice-ErrorDescription>`
| ``string`` :ref:`OtherEnabledState <CIM-EnabledLogicalElement-OtherEnabledState>`
| ``uint32`` :ref:`LastErrorCode <CIM-LogicalDevice-LastErrorCode>`
| ``string`` :ref:`CreationClassName <CIM-LogicalDevice-CreationClassName>`
| ``uint16`` :ref:`Availability <CIM-LogicalDevice-Availability>`
| ``string`` :ref:`SystemCreationClassName <CIM-LogicalDevice-SystemCreationClassName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`Reset <CIM-LogicalDevice-Reset>`
| :ref:`RequestStateChange <CIM-EnabledLogicalElement-RequestStateChange>`
| :ref:`SetPowerState <CIM-LogicalDevice-SetPowerState>`
| :ref:`QuiesceDevice <CIM-LogicalDevice-QuiesceDevice>`
| :ref:`EnableDevice <CIM-LogicalDevice-EnableDevice>`
| :ref:`OnlineDevice <CIM-LogicalDevice-OnlineDevice>`
| :ref:`SaveProperties <CIM-LogicalDevice-SaveProperties>`
| :ref:`RestoreProperties <CIM-LogicalDevice-RestoreProperties>`

