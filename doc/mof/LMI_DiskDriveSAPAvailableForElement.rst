.. _LMI-DiskDriveSAPAvailableForElement:

LMI_DiskDriveSAPAvailableForElement
-----------------------------------

Class reference
===============
Subclass of :ref:`CIM_SAPAvailableForElement <CIM-SAPAvailableForElement>`

CIM_SAPAvailableForElement conveys the semantics of a Service Access Point that is available for a ManagedElement. When CIM_SAPAvailableForElement is not instantiated, then the SAP is assumed to be generally available. If instantiated, the SAP is available only for the associated ManagedElements. For example, a device might provide management access through a URL. This association allows the URL to be advertised for the device.


Key properties
^^^^^^^^^^^^^^

| :ref:`ManagedElement <CIM-SAPAvailableForElement-ManagedElement>`
| :ref:`AvailableSAP <CIM-SAPAvailableForElement-AvailableSAP>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-DiskDriveSAPAvailableForElement-AvailableSAP:

:ref:`LMI_DiskDriveATAProtocolEndpoint <LMI-DiskDriveATAProtocolEndpoint>` **AvailableSAP**

    The Service Access Point that is available.

    
.. _LMI-DiskDriveSAPAvailableForElement-ManagedElement:

:ref:`LMI_DiskDrive <LMI-DiskDrive>` **ManagedElement**

    The ManagedElement for which the SAP is available.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

