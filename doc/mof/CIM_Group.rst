.. _CIM-Group:

CIM_Group
---------

Class reference
===============
Subclass of :ref:`CIM_Collection <CIM-Collection>`

The Group class is used to collect ManagedElements that are intended to be conformant with an LDAP GroupOfNames, as defined by IETF RFC 2256. For other purposes, ConcreteCollection, or other subclasses of Collection, may be more appropriate. 

This class is defined so as to incorporate commonly-used LDAP attributes to permit implementations to easily derive this information from LDAP-accessible directories. This class's properties are a subset of a related class, OtherGroupInformation, which defines all the group properties and in array form for directory compatibility.


Key properties
^^^^^^^^^^^^^^

| :ref:`CreationClassName <CIM-Group-CreationClassName>`
| :ref:`Name <CIM-Group-Name>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-Group-Name:

``string`` **Name**

    The Name property defines the label by which the object is known. In the case of an LDAP-derived instance, the Name property value may be set to the distinguished name of the LDAP-accessed object instance.

    
.. _CIM-Group-BusinessCategory:

``string`` **BusinessCategory**

    The BusinessCategory property may be used to describe the kind of business activity performed by the members of the group.

    
.. _CIM-Group-CommonName:

``string`` **CommonName**

    A Common Name is a (possibly ambiguous) name by which the group is commonly known in some limited scope (such as an organization) and conforms to the naming conventions of the country or culture with which it is associated.

    
.. _CIM-Group-CreationClassName:

``string`` **CreationClassName**

    CreationClassName indicates the name of the class or the subclass used in the creation of an instance. When used with the other key properties of this class, this property allows all instances of this class and its subclasses to be uniquely identified.

    

Local methods
^^^^^^^^^^^^^

*None*

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

