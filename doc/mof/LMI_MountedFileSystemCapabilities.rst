.. _LMI-MountedFileSystemCapabilities:

LMI_MountedFileSystemCapabilities
---------------------------------

Class reference
===============
Subclass of :ref:`CIM_Capabilities <CIM-Capabilities>`

This class describes capabilities of associated LMI_MountConfigurationService. It can also be used to create new LMI_MountedFileSystemSetting.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-MountedFileSystemCapabilities-SupportedAsynchronousMethods:

``uint16[]`` **SupportedAsynchronousMethods**

    
    ======== ===========
    ValueMap Values     
    ======== ===========
    0        CreateMount
    1        ModifyMount
    2        DeleteMount
    ======== ===========
    

Local methods
^^^^^^^^^^^^^

    .. _LMI-MountedFileSystemCapabilities-CreateSetting:

``uint32`` **CreateSetting** (:ref:`LMI_MountedFileSystemSetting <LMI-MountedFileSystemSetting>` MountSetting)

    Method to create and populate an LMI_MountedFileSystemSetting instance. This removes the need to populate default settings and other settings in the context of each LMI_MountedFileSystemCapabilities (which could be numerous).

    
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
    
        *OUT* :ref:`LMI_MountedFileSystemSetting <LMI-MountedFileSystemSetting>` **MountSetting**
            Reference to the created setting instance.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`ElementName <CIM-Capabilities-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`InstanceID <CIM-Capabilities-InstanceID>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`CreateGoalSettings <CIM-Capabilities-CreateGoalSettings>`

