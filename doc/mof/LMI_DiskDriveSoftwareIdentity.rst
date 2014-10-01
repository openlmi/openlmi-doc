.. _LMI-DiskDriveSoftwareIdentity:

LMI_DiskDriveSoftwareIdentity
-----------------------------

Class reference
===============
Subclass of :ref:`CIM_SoftwareIdentity <CIM-SoftwareIdentity>`

SoftwareIdentity provides descriptive information about a software component for asset tracking and/or installation dependency management. When the IsEntity property has the value TRUE, the instance of SoftwareIdentity represents an individually identifiable entity similar to Physical Element. SoftwareIdentity does NOT indicate whether the software is installed, executing, etc. This extra information may be provided through specialized associations to Software Identity. For instance, both InstalledSoftwareIdentity and ElementSoftwareIdentity may be used to indicate that the software identified by this class is installed. SoftwareIdentity is used when managing the software components of a ManagedElement that is the management focus. Since software may be acquired, SoftwareIdentity can be associated with a Product using the ProductSoftwareComponent relationship. The Application Model manages the deployment and installation of software via the classes, SoftwareFeatures and SoftwareElements. SoftwareFeature and SoftwareElement are used when the software component is the management focus. The deployment/installation concepts are related to the asset/identity one. In fact, a SoftwareIdentity may correspond to a Product, or to one or more SoftwareFeatures or SoftwareElements - depending on the granularity of these classes and the deployment model. The correspondence of Software Identity to Product, SoftwareFeature or SoftwareElement is indicated using the ConcreteIdentity association. Note that there may not be sufficient detail or instrumentation to instantiate ConcreteIdentity. And, if the association is instantiated, some duplication of information may result. For example, the Vendor described in the instances of Product and SoftwareIdentity MAY be the same. However, this is not necessarily true, and it is why vendor and similar information are duplicated in this class. 

Note that ConcreteIdentity can also be used to describe the relationship of the software to any LogicalFiles that result from installing it. As above, there may not be sufficient detail or instrumentation to instantiate this association.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-SoftwareIdentity-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-DiskDriveSoftwareIdentity-InstanceID:

``string`` **InstanceID**

    Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. In order to ensure uniqueness within the NameSpace, the value of InstanceID SHOULD be constructed using the following 'preferred' algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon ':', and where <OrgID> MUST include a copyrighted, trademarked or otherwise unique name that is owned by the business entity creating/defining the InstanceID, or is a registered ID that is assigned to the business entity by a recognized global authority (This is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness <OrgID> MUST NOT contain a colon (':'). When using this algorithm, the first colon to appear in InstanceID MUST appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and SHOULD not be re-used to identify different underlying (real-world) elements. If the above 'preferred' algorithm is not used, the defining entity MUST assure that the resultant InstanceID is not re-used across any InstanceIDs produced by this or other providers for this instance's NameSpace. 

    For DMTF defined instances, the 'preferred' algorithm MUST be used with the <OrgID> set to 'CIM'.

    
.. _LMI-DiskDriveSoftwareIdentity-ElementName:

``string`` **ElementName**

    A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. 

    Note that the Name property of ManagedSystemElement is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. Note that if there is an associated instance of CIM_EnabledLogicalElementCapabilities, restrictions on this properties may exist as defined in ElementNameMask and MaxElementNameLen properties defined in that class.

    
.. _LMI-DiskDriveSoftwareIdentity-Description:

``string`` **Description**

    The Description property provides a textual description of the object.

    
.. _LMI-DiskDriveSoftwareIdentity-IsEntity:

``boolean`` **IsEntity**

    The IsEntity property is used to indicate whether the SoftwareIdentity corresponds to a discrete copy of the software component or is being used to convey descriptive and identifying information about software that is not present in the management domain.A value of TRUE shall indicate that the SoftwareIdentity instance corresponds to a discrete copy of the software component. A value of FALSE shall indicate that the SoftwareIdentity instance does not correspond to a discrete copy of the Software.

    
.. _LMI-DiskDriveSoftwareIdentity-IsLargeBuildNumber:

``boolean`` **IsLargeBuildNumber**

    The IsLargeBuildNumber property is used to indicate if the BuildNumber of LargeBuildNumber property contains the value of the software build. A value of TRUE shall indicate that the build number is represented by the LargeBuildNumber property. A value of FALSE shall indicate that the build number is represented by the BuildNumber property.

    
.. _LMI-DiskDriveSoftwareIdentity-Manufacturer:

``string`` **Manufacturer**

    Manufacturer of this software.

    
.. _LMI-DiskDriveSoftwareIdentity-Classifications:

``uint16[]`` **Classifications**

    An array of enumerated integers that classify this software. For example, the software MAY be instrumentation (value=5) or firmware and diagnostic software (10 and 7). The use of value 6, Firmware/BIOS, is being deprecated. Instead, either the value 10 (Firmware) and/or 11 (BIOS/FCode) SHOULD be used. The value 13, Software Bundle, identifies a software package consisting of multiple discrete software instances that can be installed individually or together.

    Each contained software instance is represented by an instance of SoftwareIdentity that is associated to this instance of SoftwareIdentityinstance via a Component association.

    
    ============== ======================
    ValueMap       Values                
    ============== ======================
    0              Unknown               
    1              Other                 
    2              Driver                
    3              Configuration Software
    4              Application Software  
    5              Instrumentation       
    6              Firmware/BIOS         
    7              Diagnostic Software   
    8              Operating System      
    9              Middleware            
    10             Firmware              
    11             BIOS/FCode            
    12             Support/Service Pack  
    13             Software Bundle       
    ..             DMTF Reserved         
    0x8000..0xFFFF Vendor Reserved       
    ============== ======================
    
.. _LMI-DiskDriveSoftwareIdentity-Name:

``string`` **Name**

    The Name property defines the label by which the object is known. When subclassed, the Name property can be overridden to be a Key property.

    
.. _LMI-DiskDriveSoftwareIdentity-Caption:

``string`` **Caption**

    The Caption property is a short textual description (one- line string) of the object.

    
.. _LMI-DiskDriveSoftwareIdentity-VersionString:

``string`` **VersionString**

    A string representing the complete software version information - for example, '12.1(3)T'. This string and the numeric major/minor/revision/build properties are complementary. Since vastly different representations and semantics exist for versions, it is not assumed that one representation is sufficient to permit a client to perform computations (i.e., the values are numeric) and a user to recognize the software's version (i.e., the values are understandable and readable). Hence, both numeric and string representations of version are provided.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``uint16[]`` :ref:`TargetOSTypes <CIM-SoftwareIdentity-TargetOSTypes>`
| ``uint16`` :ref:`ExtendedResourceType <CIM-SoftwareIdentity-ExtendedResourceType>`
| ``string`` :ref:`SerialNumber <CIM-SoftwareIdentity-SerialNumber>`
| ``string[]`` :ref:`Languages <CIM-SoftwareIdentity-Languages>`
| ``uint16`` :ref:`MinExtendedResourceTypeMajorVersion <CIM-SoftwareIdentity-MinExtendedResourceTypeMajorVersion>`
| ``string[]`` :ref:`TargetTypes <CIM-SoftwareIdentity-TargetTypes>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string[]`` :ref:`TargetOperatingSystems <CIM-SoftwareIdentity-TargetOperatingSystems>`
| ``uint64`` :ref:`LargeBuildNumber <CIM-SoftwareIdentity-LargeBuildNumber>`
| ``uint16`` :ref:`MinExtendedResourceTypeMinorVersion <CIM-SoftwareIdentity-MinExtendedResourceTypeMinorVersion>`
| ``datetime`` :ref:`ReleaseDate <CIM-SoftwareIdentity-ReleaseDate>`
| ``string[]`` :ref:`ClassificationDescriptions <CIM-SoftwareIdentity-ClassificationDescriptions>`
| ``string[]`` :ref:`IdentityInfoType <CIM-SoftwareIdentity-IdentityInfoType>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string[]`` :ref:`IdentityInfoValue <CIM-SoftwareIdentity-IdentityInfoValue>`
| ``string`` :ref:`OtherExtendedResourceTypeDescription <CIM-SoftwareIdentity-OtherExtendedResourceTypeDescription>`
| ``uint16`` :ref:`MinExtendedResourceTypeBuildNumber <CIM-SoftwareIdentity-MinExtendedResourceTypeBuildNumber>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`MinorVersion <CIM-SoftwareIdentity-MinorVersion>`
| ``uint16`` :ref:`MajorVersion <CIM-SoftwareIdentity-MajorVersion>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint16`` :ref:`MinExtendedResourceTypeRevisionNumber <CIM-SoftwareIdentity-MinExtendedResourceTypeRevisionNumber>`
| ``uint16`` :ref:`BuildNumber <CIM-SoftwareIdentity-BuildNumber>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16`` :ref:`RevisionNumber <CIM-SoftwareIdentity-RevisionNumber>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

