.. _CIM-Capabilities:

CIM_Capabilities
----------------

Class reference
===============
Subclass of :ref:`CIM_ManagedElement <CIM-ManagedElement>`

Capabilities is an abstract class whose subclasses describe abilities and/or potential for use. For example, one may describe the maximum number of VLANs that can be supported on a system using a subclass of Capabilities. Capabilities are tied to the elements which they describe using the ElementCapabilities association. Note that the cardinality of the ManagedElement reference is Min(1). This cardinality mandates the instantiation of the ElementCapabilities association for the referenced instance of Capabilities. ElementCapabilities describes the existence requirements for the referenced instance of ManagedElement. Specifically, the ManagedElement MUST exist and provide the context for the Capabilities. Note that Capabilities do not indicate what IS configured or operational, but what CAN or CANNOT exist, be defined or be used. Note that it is possible to describe both supported and excluded abilities and functions (both capabilities and limitations) using this class.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-Capabilities-InstanceID:

``string`` **InstanceID**

    Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. In order to ensure uniqueness within the NameSpace, the value of InstanceID SHOULD be constructed using the following 'preferred' algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon ':', and where <OrgID> MUST include a copyrighted, trademarked or otherwise unique name that is owned by the business entity creating/defining the InstanceID, or is a registered ID that is assigned to the business entity by a recognized global authority (This is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness <OrgID> MUST NOT contain a colon (':'). When using this algorithm, the first colon to appear in InstanceID MUST appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and SHOULD not be re-used to identify different underlying (real-world) elements. If the above 'preferred' algorithm is not used, the defining entity MUST assure that the resultant InstanceID is not re-used across any InstanceIDs produced by this or other providers for this instance's NameSpace. 

    For DMTF defined instances, the 'preferred' algorithm MUST be used with the <OrgID> set to 'CIM'.

    
.. _CIM-Capabilities-ElementName:

``string`` **ElementName**

    The user friendly name for this instance of Capabilities. In addition, the user friendly name can be used as a index property for a search of query. (Note: Name does not have to be unique within a namespace.)

    

Local methods
^^^^^^^^^^^^^

    .. _CIM-Capabilities-CreateGoalSettings:

``uint16`` **CreateGoalSettings** (``string[]`` TemplateGoalSettings, ``string[]`` SupportedGoalSettings)

    Method to create a set of supported SettingData elements, from two sets of SettingData elements, provided by the caller. 

    CreateGoal should be used when the SettingData instances that represents the goal will not persist beyond the execution of the client and where those instances are not intended to be shared with other, non-cooperating clients. 

    Both TemplateGoalSettings and SupportedGoalSettings are represented as strings containing EmbeddedInstances of a CIM_SettingData subclass. These embedded instances do not exist in the infrastructure supporting this method but are maintained by the caller/client. 

    This method should return CIM_Error(s) representing that a single named property of a setting (or other) parameter (either reference or embedded object) has an invalid value or that an invalid combination of named properties of a setting (or other) parameter (either reference or embedded object) has been requested. 

    If the input TemplateGoalSettings is NULL or the empty string, this method returns a default SettingData element that is supported by this Capabilities element. 

    If the TemplateGoalSettings specifies values that cannot be supported, this method shall return an appropriate CIM_Error and should return a best match for a SupportedGoalSettings. 

    The client proposes a goal using the TemplateGoalSettings parameter and gets back Success if the TemplateGoalSettings is exactly supportable. It gets back "Alternative Proposed" if the output SupportedGoalSettings represents a supported alternative. This alternative should be a best match, as defined by the implementation. 

    If the implementation is conformant to a RegisteredProfile, then that profile may specify the algorithms used to determine best match. A client may compare the returned value of each property against the requested value to determine if it is left unchanged, degraded or upgraded. 

    

    Otherwise, if the TemplateGoalSettings is not applicable an "Invalid Parameter" error is returned. 

    

    When a mutually acceptable SupportedGoalSettings has been achieved, the client may use the contained SettingData instances as input to methods for creating a new object ormodifying an existing object. Also the embedded SettingData instances returned in the SupportedGoalSettings may be instantiated via CreateInstance, either by a client or as a side-effect of the execution of an extrinsic method for which the returned SupportedGoalSettings is passed as an embedded instance.

    
    ============ ====================
    ValueMap     Values              
    ============ ====================
    0            Success             
    1            Not Supported       
    2            Unknown             
    3            Timeout             
    4            Failed              
    5            Invalid Parameter   
    6            Alternative Proposed
    ..           DMTF Reserved       
    32768..65535 Vendor Specific     
    ============ ====================
    
    **Parameters**
    
        *IN* ``string[]`` **TemplateGoalSettings**
            If provided, TemplateGoalSettings are elements of class CIM_SettingData, or a derived class, that is used as the template to be matched. . 

            At most, one instance of each SettingData subclass may be supplied. 

            All SettingData instances provided by this property are interpreted as a set, relative to this Capabilities instance. 

            SettingData instances that are not relevant to this instance are ignored. 

            If not provided, it shall be set to NULL. In that case, a SettingData instance representing the default settings of the associated ManagedElement is used.

            
        
        *IN*, *OUT* ``string[]`` **SupportedGoalSettings**
            SupportedGoalSettings are elements of class CIM_SettingData, or a derived class. 

            At most, one instance of each SettingData subclass may be supplied. 

            All SettingData instances provided by this property are interpreted as a set, relative to this Capabilities instance. 

            

            To enable a client to provide additional information towards achieving the TemplateGoalSettings, an input set of SettingData instances may be provided. If not provided, this property shall be set to NULL on input.. Note that when provided, what property values are changed, and how, is implementation dependent and may be the subject of other standards. 

            If provided, the input SettingData instances must be ones that the implementation is able to support relative to the ManagedElement associated via ElementCapabilities. Typically, the input SettingData instances are created by a previous instantiation of CreateGoalSettings. 

            If the input SupportedGoalSettings is not supported by the implementation, then an "Invalid Parameter" (5) error is returned by this call. In this case, a corresponding CIM_ERROR should also be returned. 

            On output, this property is used to return the best supported match to the TemplateGoalSettings. 

            If the output SupportedGoalSettings matches the input SupportedGoalSettings, then the implementation is unable to improve further towards meeting the TemplateGoalSettings.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

