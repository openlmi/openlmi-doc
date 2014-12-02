.. _LMI-PCIPortGroup:

LMI_PCIPortGroup
----------------

Class reference
===============
Subclass of :ref:`CIM_PCIPortGroup <CIM-PCIPortGroup>`

A collection of one or more PCI device ports.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-SystemSpecificCollection-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-PCIPortGroup-BusNumber:

``uint8`` **BusNumber**

    The bus number shared by the PCI device ports.

    
.. _LMI-PCIPortGroup-ElementName:

``string`` **ElementName**

    A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. 

    Note that the Name property of ManagedSystemElement is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. Note that if there is an associated instance of CIM_EnabledLogicalElementCapabilities, restrictions on this properties may exist as defined in ElementNameMask and MaxElementNameLen properties defined in that class.

    
.. _LMI-PCIPortGroup-Name:

``string`` **Name**

    The Name property defines the identity by which the LogicalPortGroup is known.

    
.. _LMI-PCIPortGroup-InstanceID:

``string`` **InstanceID**

    Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. To ensure uniqueness within the NameSpace, the value of InstanceID should be constructed using the following 'preferred' algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon ':', and where <OrgID> must include a unique name. It can be a copyrighted, trademarked, or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID. Or, it could be a registered ID that is assigned to the business entity by a recognized global authority.(This requirement is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness <OrgID> must not contain a colon (':'). When using this algorithm, the first colon to appear in InstanceID must appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and should not be re-used to identify different underlying (real-world) elements. If the above 'preferred' algorithm is not used, the defining entity must ensure that the resulting InstanceID is not re-used as any of InstanceIDs produced by this or other providers for the NameSpace of this instance. 

    For DMTF-defined instances, the 'preferred' algorithm must be used with the <OrgID> set to 'CIM'.

    
.. _LMI-PCIPortGroup-Caption:

``string`` **Caption**

    The Caption property is a short textual description (one- line string) of the object.

    
.. _LMI-PCIPortGroup-Description:

``string`` **Description**

    The Description property provides a textual description of the object.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`OtherNameFormat <CIM-LogicalPortGroup-OtherNameFormat>`
| ``string`` :ref:`NameFormat <CIM-LogicalPortGroup-NameFormat>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

