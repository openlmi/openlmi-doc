.. _LMI-SystemSoftwareCollection:

LMI_SystemSoftwareCollection
----------------------------

Class reference
===============
Subclass of :ref:`CIM_SystemSpecificCollection <CIM-SystemSpecificCollection>`

SystemSpecificCollection represents the general concept of a collection that is scoped (or contained) by a System. It represents a Collection that has meaning only in the context of a System, a Collection whose elements are restricted by the definition of the System, or both of these types of Collections. This meaning is explicitly described by the (required) association, HostedCollection. 

An example of a SystemSpecificCollection is a Fibre Channel zone that collects network ports, port groupings, and aliases (as required by a customer) in the context of an AdminDomain. The Collection is not a part of the domain, but merely an arbitrary grouping of the devices and other Collections in the domain. In other words, the context of the Collection is restricted to the domain, and its members are also limited by the domain.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-SystemSpecificCollection-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-SystemSoftwareCollection-InstanceID:

``string`` **InstanceID**

    Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following 'preferred' algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon ':', and where <OrgID> must include a unique name. It can be a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID. Or, it could be a registered ID that is assigned to the business entity by a recognized global authority.(This requirement is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness <OrgID> must not contain a colon (':'). When using this algorithm, the first colon to appear in InstanceID must appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and should not be re-used to identify different underlying (real-world) elements. If the above 'preferred' algorithm is not used, the defining entity must ensure that the resulting InstanceID is not re-used as any of InstanceIDs produced by this or other providers for the NameSpace of this instance. 

    For DMTF-defined instances, the 'preferred' algorithm must be used with the <OrgID> set to 'CIM'.

    
.. _LMI-SystemSoftwareCollection-Caption:

``string`` **Caption**

    The Caption property is a short textual description (one- line string) of the object.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

