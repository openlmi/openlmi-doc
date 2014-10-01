.. _CIM-SAPAvailableForElement:

CIM_SAPAvailableForElement
--------------------------

Class reference
===============
CIM_SAPAvailableForElement conveys the semantics of a Service Access Point that is available for a ManagedElement. When CIM_SAPAvailableForElement is not instantiated, then the SAP is assumed to be generally available. If instantiated, the SAP is available only for the associated ManagedElements. For example, a device might provide management access through a URL. This association allows the URL to be advertised for the device.


Key properties
^^^^^^^^^^^^^^

| :ref:`ManagedElement <CIM-SAPAvailableForElement-ManagedElement>`
| :ref:`AvailableSAP <CIM-SAPAvailableForElement-AvailableSAP>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-SAPAvailableForElement-AvailableSAP:

:ref:`CIM_ServiceAccessPoint <CIM-ServiceAccessPoint>` **AvailableSAP**

    The Service Access Point that is available.

    
.. _CIM-SAPAvailableForElement-ManagedElement:

:ref:`CIM_ManagedElement <CIM-ManagedElement>` **ManagedElement**

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

