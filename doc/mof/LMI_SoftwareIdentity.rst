.. _LMI-SoftwareIdentity:

LMI_SoftwareIdentity
--------------------

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

.. _LMI-SoftwareIdentity-InstanceID:

``string`` **InstanceID**

    Unique identifier for installed or available package. It's composed of OrgID and LocalID separated by ':',  where <OrgID> is LMI and LocalID is PKG:<PKG_NEVRA>. <PKG_NEVRA> is a string representing rpm package. Letters in NEVRA stand for name, epoch, version, release and architecture.

    
.. _LMI-SoftwareIdentity-Epoch:

``uint32`` **Epoch**

    Package's epoch.

    
.. _LMI-SoftwareIdentity-Version:

``string`` **Version**

    Package's version.

    
.. _LMI-SoftwareIdentity-TargetTypes:

``string[]`` **TargetTypes**

    An array of strings that describes the compatible installer(s). The purpose of the array elements is to establish compatibility between a SoftwareIdentity and a SoftwareInstallationService that can install the SoftwareIdentity by comparing the values of the array elements of this property to the values of SoftwareInstallationServiceCapabilities.SupportedTargetTypes[] property's array elements.

    
.. _LMI-SoftwareIdentity-ElementName:

``string`` **ElementName**

    Package's NEVRA string. That is also part of InstanceID.

    
.. _LMI-SoftwareIdentity-Description:

``string`` **Description**

    Package's description.

    
.. _LMI-SoftwareIdentity-IsEntity:

``boolean`` **IsEntity**

    The IsEntity property is used to indicate whether the SoftwareIdentity corresponds to a discrete copy of the software component or is being used to convey descriptive and identifying information about software that is not present in the management domain.A value of TRUE shall indicate that the SoftwareIdentity instance corresponds to a discrete copy of the software component. A value of FALSE shall indicate that the SoftwareIdentity instance does not correspond to a discrete copy of the Software.

    
.. _LMI-SoftwareIdentity-Classifications:

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
    
.. _LMI-SoftwareIdentity-Name:

``string`` **Name**

    Name of package. This does not uniquely identify package installed on computer system.

    
.. _LMI-SoftwareIdentity-InstallDate:

``datetime`` **InstallDate**

    A datetime value that indicates when the object was installed. Lack of a value does not indicate that the object is not installed.

    
.. _LMI-SoftwareIdentity-Caption:

``string`` **Caption**

    Package's summary.

    
.. _LMI-SoftwareIdentity-Architecture:

``string`` **Architecture**

    Package's architecture.

    
.. _LMI-SoftwareIdentity-Release:

``string`` **Release**

    Package's release.

    
.. _LMI-SoftwareIdentity-VersionString:

``string`` **VersionString**

    Package's EVRA, in format: <epoch>:<version>-<release>.<architecture>

    

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
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string[]`` :ref:`TargetOperatingSystems <CIM-SoftwareIdentity-TargetOperatingSystems>`
| ``uint64`` :ref:`LargeBuildNumber <CIM-SoftwareIdentity-LargeBuildNumber>`
| ``boolean`` :ref:`IsLargeBuildNumber <CIM-SoftwareIdentity-IsLargeBuildNumber>`
| ``uint16`` :ref:`MinExtendedResourceTypeMinorVersion <CIM-SoftwareIdentity-MinExtendedResourceTypeMinorVersion>`
| ``datetime`` :ref:`ReleaseDate <CIM-SoftwareIdentity-ReleaseDate>`
| ``string[]`` :ref:`ClassificationDescriptions <CIM-SoftwareIdentity-ClassificationDescriptions>`
| ``string[]`` :ref:`IdentityInfoType <CIM-SoftwareIdentity-IdentityInfoType>`
| ``string`` :ref:`Manufacturer <CIM-SoftwareIdentity-Manufacturer>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`OtherExtendedResourceTypeDescription <CIM-SoftwareIdentity-OtherExtendedResourceTypeDescription>`
| ``uint16`` :ref:`MinExtendedResourceTypeBuildNumber <CIM-SoftwareIdentity-MinExtendedResourceTypeBuildNumber>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint16`` :ref:`MinorVersion <CIM-SoftwareIdentity-MinorVersion>`
| ``uint16`` :ref:`MajorVersion <CIM-SoftwareIdentity-MajorVersion>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint16`` :ref:`MinExtendedResourceTypeRevisionNumber <CIM-SoftwareIdentity-MinExtendedResourceTypeRevisionNumber>`
| ``string[]`` :ref:`IdentityInfoValue <CIM-SoftwareIdentity-IdentityInfoValue>`
| ``uint16`` :ref:`BuildNumber <CIM-SoftwareIdentity-BuildNumber>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint16`` :ref:`RevisionNumber <CIM-SoftwareIdentity-RevisionNumber>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

