.. _CIM-LogicalPortGroup:

CIM_LogicalPortGroup
--------------------

Class reference
===============
Subclass of :ref:`CIM_SystemSpecificCollection <CIM-SystemSpecificCollection>`

A collection of one or more ports that are logically grouped for administrative and discovery or topology purposes. LogicalPortGroups define port collections for access control, or for use in routing policy or other management tasks. For example, in Fibre Channel and Infiniband, a LogicalPortGroup represents the concept of a 'node'.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-SystemSpecificCollection-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-LogicalPortGroup-Name:

``string`` **Name**

    The Name property defines the identity by which the LogicalPortGroup is known.

    
.. _CIM-LogicalPortGroup-OtherNameFormat:

``string`` **OtherNameFormat**

    A string that describes how the LogicalPortGroup is identified when the NameFormat is "Other".

    
.. _CIM-LogicalPortGroup-NameFormat:

``string`` **NameFormat**

    The NameFormat property identifies how the Name of the LogicalPortGroup is generated.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`InstanceID <CIM-SystemSpecificCollection-InstanceID>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

