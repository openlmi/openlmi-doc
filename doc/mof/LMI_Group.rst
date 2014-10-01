.. _LMI-Group:

LMI_Group
---------

Class reference
===============
Subclass of :ref:`CIM_Group <CIM-Group>`

The Group class is used to collect ManagedElements that are intended to be conformant with an LDAP GroupOfNames, as defined by IETF RFC 2256. For other purposes, ConcreteCollection, or other subclasses of Collection, may be more appropriate. 

This class is defined so as to incorporate commonly-used LDAP attributes to permit implementations to easily derive this information from LDAP-accessible directories. This class's properties are a subset of a related class, OtherGroupInformation, which defines all the group properties and in array form for directory compatibility.


Key properties
^^^^^^^^^^^^^^

| :ref:`CreationClassName <CIM-Group-CreationClassName>`
| :ref:`Name <CIM-Group-Name>`

Local properties
^^^^^^^^^^^^^^^^

*None*

Local methods
^^^^^^^^^^^^^

    .. _LMI-Group-DeleteGroup:

``uint32`` **DeleteGroup** ()

    Delete the group. The group is not deleted if it is a primary group of a user.

    
    ======== ================================
    ValueMap Values                          
    ======== ================================
    0        Operation completed successfully
    1        Failed                          
    ..       DMTF Reserved                   
    4096     Non existing group              
    4097     Group is primary group of a user
    ======== ================================
    
    **Parameters**
    
*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Name <CIM-Group-Name>`
| ``string`` :ref:`BusinessCategory <CIM-Group-BusinessCategory>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``string`` :ref:`CommonName <CIM-Group-CommonName>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`CreationClassName <CIM-Group-CreationClassName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

