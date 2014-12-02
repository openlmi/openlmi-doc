.. _CIM-SoftwareFeature:

CIM_SoftwareFeature
-------------------

Class reference
===============
Subclass of :ref:`CIM_LogicalElement <CIM-LogicalElement>`

The CIM_SoftwareFeature class defines a particular function or capability of a product or application system. This class captures a level of granularity describing a unit of installation, rather than the units that reflect how the product is built or packaged. The latter detail is captured using a CIM_SoftwareElement class. When a SoftwareFeature can exist on multiple platforms or operating systems (for example, a client component of a three tiered client/server application that runs on Solaris, Windows NT, and Windows 95), the Feature is a collection of all the SoftwareElements for these different platforms. In this case, the users of the model must be aware of this situation since typically they will be interested in a sub-collection of the SoftwareElements required for a particular platform. 

SoftwareFeatures are always defined in the context of a CIM_Product, using the CIM_ProductSoftwareFeature association. Features are delivered through Products. Optionally, SoftwareFeatures from one or more Products can be organized into ApplicationSystems using the CIM_ApplicationSystemSoftwareFeature association.


Key properties
^^^^^^^^^^^^^^

| :ref:`Version <CIM-SoftwareFeature-Version>`
| :ref:`Vendor <CIM-SoftwareFeature-Vendor>`
| :ref:`Name <CIM-SoftwareFeature-Name>`
| :ref:`IdentifyingNumber <CIM-SoftwareFeature-IdentifyingNumber>`
| :ref:`ProductName <CIM-SoftwareFeature-ProductName>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-SoftwareFeature-Vendor:

``string`` **Vendor**

    The scoping Product's supplier.

    
.. _CIM-SoftwareFeature-Name:

``string`` **Name**

    The Name property defines the unique label by which the SoftwareFeature is identified. This label should be a human-readable name that uniquely identifies the element in the context of the element's namespace.

    
.. _CIM-SoftwareFeature-IdentifyingNumber:

``string`` **IdentifyingNumber**

    The scoping Product's identification.

    
.. _CIM-SoftwareFeature-ProductName:

``string`` **ProductName**

    The scoping Product's commonly used name.

    
.. _CIM-SoftwareFeature-Version:

``string`` **Version**

    The scoping Product's version.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

