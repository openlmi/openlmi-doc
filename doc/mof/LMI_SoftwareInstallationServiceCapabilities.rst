.. _LMI-SoftwareInstallationServiceCapabilities:

LMI_SoftwareInstallationServiceCapabilities
-------------------------------------------

Class reference
===============
Subclass of :ref:`CIM_SoftwareInstallationServiceCapabilities <CIM-SoftwareInstallationServiceCapabilities>`

A subclass of capabilities that defines the capabilities of a SoftwareInstallationService. A single instance of SoftwareInstallationServiceCapabilities is associated with a SoftwareInstallationService using ElementCapabilities.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-SoftwareInstallationServiceCapabilities-SupportedTargetTypes:

``string[]`` **SupportedTargetTypes**

    An array containing a list of SoftwareIdentity.TargetType properties that this service 'knows' how to install. TargetType is an application specific string which is invariant across version or name changes of the SoftwareIdentity and so can be used by a client to select Software Identities compatible with this service. 

    If the service is generic (for example an OS installer), this array will be empty.

    
.. _LMI-SoftwareInstallationServiceCapabilities-Description:

``string`` **Description**

    The Description property provides a textual description of the object.

    
.. _LMI-SoftwareInstallationServiceCapabilities-SupportedInstallOptions:

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
    
.. _LMI-SoftwareInstallationServiceCapabilities-CanAddToCollection:

``boolean`` **CanAddToCollection**

    This property indicates whether SoftwareInstallationService.InstallFromSoftwareIdentity supports adding a SoftwareIdentity to a Collection.

    
.. _LMI-SoftwareInstallationServiceCapabilities-SupportedURISchemes:

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
    
.. _LMI-SoftwareInstallationServiceCapabilities-InstanceID:

``string`` **InstanceID**

    Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. In order to ensure uniqueness within the NameSpace, the value of InstanceID SHOULD be constructed using the following 'preferred' algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon ':', and where <OrgID> MUST include a copyrighted, trademarked or otherwise unique name that is owned by the business entity creating/defining the InstanceID, or is a registered ID that is assigned to the business entity by a recognized global authority (This is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness <OrgID> MUST NOT contain a colon (':'). When using this algorithm, the first colon to appear in InstanceID MUST appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and SHOULD not be re-used to identify different underlying (real-world) elements. If the above 'preferred' algorithm is not used, the defining entity MUST assure that the resultant InstanceID is not re-used across any InstanceIDs produced by this or other providers for this instance's NameSpace. 

    For DMTF defined instances, the 'preferred' algorithm MUST be used with the <OrgID> set to 'CIM'.

    
.. _LMI-SoftwareInstallationServiceCapabilities-SupportedAsynchronousActions:

``uint16[]`` **SupportedAsynchronousActions**

    Enumeration indicating what operations will be executed as asynchronous jobs. If an operation is included in both this and SupportedSynchronousActions then the underlying implementation is indicating that it may or may not create a job. If a Job is created, then the methods in SoftwareInstallationService return a reference to that Job as the Job parameter.

    
    ======== ==============================
    ValueMap Values                        
    ======== ==============================
    2        None supported                
    3        Install From Software Identity
    4        Install from ByteStream       
    5        Install from URI              
    10000    Verify Software Identity      
    ======== ==============================
    
.. _LMI-SoftwareInstallationServiceCapabilities-SupportedSynchronousActions:

``uint16[]`` **SupportedSynchronousActions**

    Enumeration indicating what operations will be executed without the creation of a job. If an operation is included in both this and SupportedAsynchronousActions then the underlying instrumentation is indicating that it may or may not create a job.

    
    ======== ==============================
    ValueMap Values                        
    ======== ==============================
    2        None supported                
    3        Install From Software Identity
    4        Install from ByteStream       
    5        Install from URI              
    10000    Verify Software Identity      
    ======== ==============================
    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16[]`` :ref:`SupportedExtendedResourceTypes <CIM-SoftwareInstallationServiceCapabilities-SupportedExtendedResourceTypes>`
| ``uint16[]`` :ref:`SupportedExtendedResourceTypesMajorVersions <CIM-SoftwareInstallationServiceCapabilities-SupportedExtendedResourceTypesMajorVersions>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16[]`` :ref:`SupportedExtendedResourceTypesBuildNumbers <CIM-SoftwareInstallationServiceCapabilities-SupportedExtendedResourceTypesBuildNumbers>`
| ``string`` :ref:`ElementName <CIM-Capabilities-ElementName>`
| ``string[]`` :ref:`OtherSupportedExtendedResourceTypeDescriptions <CIM-SoftwareInstallationServiceCapabilities-OtherSupportedExtendedResourceTypeDescriptions>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint16[]`` :ref:`SupportedExtendedResourceTypesRevisionNumbers <CIM-SoftwareInstallationServiceCapabilities-SupportedExtendedResourceTypesRevisionNumbers>`
| ``uint16[]`` :ref:`SupportedExtendedResourceTypesMinorVersions <CIM-SoftwareInstallationServiceCapabilities-SupportedExtendedResourceTypesMinorVersions>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`CreateGoalSettings <CIM-Capabilities-CreateGoalSettings>`

