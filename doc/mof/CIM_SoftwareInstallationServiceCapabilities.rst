.. _CIM-SoftwareInstallationServiceCapabilities:

CIM_SoftwareInstallationServiceCapabilities
-------------------------------------------

Class reference
===============
Subclass of :ref:`CIM_Capabilities <CIM-Capabilities>`

A subclass of capabilities that defines the capabilities of a SoftwareInstallationService. A single instance of SoftwareInstallationServiceCapabilities is associated with a SoftwareInstallationService using ElementCapabilities.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-SoftwareInstallationServiceCapabilities-SupportedExtendedResourceTypes:

``uint16[]`` **SupportedExtendedResourceTypes**

    An array containing a list of the binary format types that this service 'knows' how to install. The Values for this property are the subset of CIM_SoftwareIdentityResource.ExtendedResourceTypes that apply to the 'Installer and Payload', 'Installer' and ' Installability Checker' ResourceTypes. For example, an a Windows system, this property may be set to '4' indicating 'Windows MSI'. This property should be set to '2' (Not Applicable) if this service is not OS specific.

    
    ======== ==================================
    ValueMap Values                            
    ======== ==================================
    0        Unknown                           
    1        Other                             
    2        Not Applicable                    
    3        Linux RPM                         
    4        HP-UX Depot                       
    5        Windows MSI                       
    6        Solaris Package                   
    7        Macintosh Disk Image              
    8        Debian linux Package              
    9        VMware vSphere Installation Bundle
    10       VMware Software Bulletin          
    11       HP Smart Component                
    ..       DMTF Reserved                     
    0x8000.. Vendor Reserved                   
    ======== ==================================
    
.. _CIM-SoftwareInstallationServiceCapabilities-SupportedTargetTypes:

``string[]`` **SupportedTargetTypes**

    An array containing a list of SoftwareIdentity.TargetType properties that this service 'knows' how to install. TargetType is an application specific string which is invariant across version or name changes of the SoftwareIdentity and so can be used by a client to select Software Identities compatible with this service. 

    If the service is generic (for example an OS installer), this array will be empty.

    
.. _CIM-SoftwareInstallationServiceCapabilities-SupportedExtendedResourceTypesBuildNumbers:

``uint16[]`` **SupportedExtendedResourceTypesBuildNumbers**

    This property represents the build number component of the installer version supported by the SoftwareInstallationService.The installer format is represented by the element at the same index in the SupportedExtendedResourceTypes array.

    
.. _CIM-SoftwareInstallationServiceCapabilities-CanAddToCollection:

``boolean`` **CanAddToCollection**

    This property indicates whether SoftwareInstallationService.InstallFromSoftwareIdentity supports adding a SoftwareIdentity to a Collection.

    
.. _CIM-SoftwareInstallationServiceCapabilities-SupportedURISchemes:

``uint16[]`` **SupportedURISchemes**

    This property lists the URI schemes supported by the SoftwareInstallationService.

    
    ============== ===============
    ValueMap       Values         
    ============== ===============
    2              data           
    3              file           
    4              ftp            
    5              http           
    6              https          
    7              nfs            
    8              tftp           
    ..             DMTF Reserved  
    0x8000..0xFFFF Vendor Specific
    ============== ===============
    
.. _CIM-SoftwareInstallationServiceCapabilities-SupportedInstallOptions:

``uint16[]`` **SupportedInstallOptions**

    An enumeration indicating the specific install related optionssupported by this service. Since this is an array, multiple values may be specified. See the InstallOptions parameter of theSoftwareInstallationService.InstallFromSoftwareIdentity method for the description of these values.

    
    ============ =========================
    ValueMap     Values                   
    ============ =========================
    2            Defer target/system reset
    3            Force installation       
    4            Install                  
    5            Update                   
    6            Repair                   
    7            Reboot                   
    8            Password                 
    9            Uninstall                
    10           Log                      
    11           SilentMode               
    12           AdministrativeMode       
    13           ScheduleInstallAt        
    ..           DMTF Reserved            
    32768..65535 Vendor Specific          
    ============ =========================
    
.. _CIM-SoftwareInstallationServiceCapabilities-SupportedExtendedResourceTypesMajorVersions:

``uint16[]`` **SupportedExtendedResourceTypesMajorVersions**

    This property represents the major number component of the installer version supported by the SoftwareInstallationService.The installer format is represented by the element at the same index in the SupportedExtendedResourceTypes array.

    
.. _CIM-SoftwareInstallationServiceCapabilities-SupportedSynchronousActions:

``uint16[]`` **SupportedSynchronousActions**

    Enumeration indicating what operations will be executed without the creation of a job. If an operation is included in both this and SupportedAsynchronousActions then the underlying instrumentation is indicating that it may or may not create a job.

    
    ======== ==============================
    ValueMap Values                        
    ======== ==============================
    2        None supported                
    3        Install From Software Identity
    4        Install from ByteStream       
    5        Install from URI              
    ======== ==============================
    
.. _CIM-SoftwareInstallationServiceCapabilities-SupportedAsynchronousActions:

``uint16[]`` **SupportedAsynchronousActions**

    Enumeration indicating what operations will be executed as asynchronous jobs. If an operation is included in both this and SupportedSynchronousActions then the underlying implementation is indicating that it may or may not create a job. If a Job is created, then the methods in SoftwareInstallationService return a reference to that Job as the Job parameter.

    
    ======== ==============================
    ValueMap Values                        
    ======== ==============================
    2        None supported                
    3        Install From Software Identity
    4        Install from ByteStream       
    5        Install from URI              
    ======== ==============================
    
.. _CIM-SoftwareInstallationServiceCapabilities-OtherSupportedExtendedResourceTypeDescriptions:

``string[]`` **OtherSupportedExtendedResourceTypeDescriptions**

    A string describing the binary format types that this service 'knows' how to install when the corresponding SupportedExtendedResourceTypes array includes the value 1 (Other).

    
.. _CIM-SoftwareInstallationServiceCapabilities-SupportedExtendedResourceTypesRevisionNumbers:

``uint16[]`` **SupportedExtendedResourceTypesRevisionNumbers**

    This property represents the revision number component of the installer version supported by the SoftwareInstallationService.The installer format is represented by the element at the same index in the SupportedExtendedResourceTypes array.

    
.. _CIM-SoftwareInstallationServiceCapabilities-SupportedExtendedResourceTypesMinorVersions:

``uint16[]`` **SupportedExtendedResourceTypesMinorVersions**

    This property represents the minor number component of the installer version supported by the SoftwareInstallationService.The installer format is represented by the element at the same index in the SupportedExtendedResourceTypes array.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`ElementName <CIM-Capabilities-ElementName>`
| ``string`` :ref:`InstanceID <CIM-Capabilities-InstanceID>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`CreateGoalSettings <CIM-Capabilities-CreateGoalSettings>`

