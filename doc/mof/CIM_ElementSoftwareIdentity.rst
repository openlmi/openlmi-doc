.. _CIM-ElementSoftwareIdentity:

CIM_ElementSoftwareIdentity
---------------------------

Class reference
===============
Subclass of :ref:`CIM_Dependency <CIM-Dependency>`

ElementSoftwareIdentity allows a Managed Element to report its software related asset information (firmware, drivers, configuration software, and etc.)


Key properties
^^^^^^^^^^^^^^

| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-ElementSoftwareIdentity-Dependent:

:ref:`CIM_ManagedElement <CIM-ManagedElement>` **Dependent**

    The ManagedElement that requires or uses the software.

    
.. _CIM-ElementSoftwareIdentity-Antecedent:

:ref:`CIM_SoftwareIdentity <CIM-SoftwareIdentity>` **Antecedent**

    A LogicalElement's Software Asset.

    
.. _CIM-ElementSoftwareIdentity-UpgradeCondition:

``uint16`` **UpgradeCondition**

    Indicates the element's ability to upgrade this software asset.

    'Resides off element'(2), indicates the persistence of the software is outside of the element. Typically for a element this software is part of the OperatingSystem is typically upgradeable.

    'Owner Upgradeable' (3), indicates the persistence of the software is on the element and is upgradeable by the owner.

    'FactoryUpgradeable' (4),indicates the persistence of the software is on the element and is upgradeable by the manufacturer.

    'Not Upgradeable' (5), indicates the presistence of the software is on the element and is not upgradeable. (i.e. burned into a non replaceable ROM chip.

    
    ============== ===================
    ValueMap       Values             
    ============== ===================
    0              Unknown            
    1              Other              
    2              Resides off device 
    3              Owner Upgradeable  
    4              Factory Upgradeable
    5              Not Upgradeable    
    ..             DMTF Reserved      
    0x8000..0xFFFF Vendor Reserved    
    ============== ===================
    
.. _CIM-ElementSoftwareIdentity-ElementSoftwareStatus:

``uint16[]`` **ElementSoftwareStatus**

    A collection of properties describing the status of the software on the managed element. Multiple properties could be set at the same time. For example a ElementSoftwareStatus could have "Installed", "Default", "Current" and "FallBack" set at the same time. 

    "Current" indicates that the software is currently running on or for the Managed Element. 

    "Next" indicates that the software will run after the next reset or reboot unless superseded by a software with a status of "SingleUse". 

    "FallBack" indicates that the software will be run if the software which has a status of "Next" or "SingleUse" fails to run. 

    "Default" indicates the default version of the software that was originally shipped by the manufacturer. 

    "Installed" indicates that the software is persistently located and is available for use on the Managed Element. 

    "SingleUse" indicates that the software will run only after the next reset or reboot but will not run after the subsequent reset or reboot. 

    "Available" indicates that the software is available for installation on the Managed Element. 

    "Supports"indicates that the software will work with or operate the Managed Element but is or will be installed on a different Managed Element.

    
    ============ ===============
    ValueMap     Values         
    ============ ===============
    0            Unknown        
    2            Current        
    3            Next           
    4            FallBack       
    5            Default        
    6            Installed      
    7            Single Use     
    8            Available      
    9            Supports       
    ..           DMTF Reserved  
    32768..65535 Vendor Reserved
    ============ ===============
    
.. _CIM-ElementSoftwareIdentity-OtherUpgradeCondition:

``string`` **OtherUpgradeCondition**

    Describes the upgrade condition, when UpgradeCondition is set to 1 ("Other").

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

