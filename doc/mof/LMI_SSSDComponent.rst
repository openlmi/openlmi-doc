.. _LMI-SSSDComponent:

LMI_SSSDComponent
-----------------

Class reference
===============
Subclass of :ref:`CIM_ManagedElement <CIM-ManagedElement>`

Base class for SSSD's components.


Key properties
^^^^^^^^^^^^^^

| :ref:`Name <LMI-SSSDComponent-Name>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-SSSDComponent-Name:

``string`` **Name**

    Name of the SSSD component.

    
.. _LMI-SSSDComponent-IsEnabled:

``boolean`` **IsEnabled**

    True if this process is enabled at SSSD startup and false otherwise.

    
.. _LMI-SSSDComponent-DebugLevel:

``uint16`` **DebugLevel**

    Debug level used within this component.

    
.. _LMI-SSSDComponent-Type:

``uint16`` **Type**

    Type of the SSSD component.

    
    ======== =========
    ValueMap Values   
    ======== =========
    0        Monitor  
    1        Responder
    2        Backend  
    ======== =========
    

Local methods
^^^^^^^^^^^^^

    .. _LMI-SSSDComponent-SetDebugLevelPermanently:

``uint32`` **SetDebugLevelPermanently** (``uint16`` debug_level)

    Permanently change debug level of this component.

    
    ======== =======================
    ValueMap Values                 
    ======== =======================
    0        Success                
    1        Failed                 
    2        Operation not supported
    3        I/O error              
    ======== =======================
    
    **Parameters**
    
        *IN* ``uint16`` **debug_level**
            
        
    
    .. _LMI-SSSDComponent-Enable:

``uint32`` **Enable** ()

    Enable this component. SSSD has to be restarted in order this change to take any effect.

    
    ======== =======================
    ValueMap Values                 
    ======== =======================
    0        Success                
    1        Failed                 
    2        Operation not supported
    3        I/O error              
    ======== =======================
    
    **Parameters**
    
*None*
    .. _LMI-SSSDComponent-Disable:

``uint32`` **Disable** ()

    Disable this component. SSSD has to be restarted in order this change to take any effect.

    
    ======== =======================
    ValueMap Values                 
    ======== =======================
    0        Success                
    1        Failed                 
    2        Operation not supported
    3        I/O error              
    ======== =======================
    
    **Parameters**
    
*None*
    .. _LMI-SSSDComponent-SetDebugLevelTemporarily:

``uint32`` **SetDebugLevelTemporarily** (``uint16`` debug_level)

    Change debug level of this component but switch it back to the original value when SSSD is restarted.

    
    ======== =======================
    ValueMap Values                 
    ======== =======================
    0        Success                
    1        Failed                 
    2        Operation not supported
    3        I/O error              
    ======== =======================
    
    **Parameters**
    
        *IN* ``uint16`` **debug_level**
            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

