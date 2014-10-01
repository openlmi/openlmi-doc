.. _LMI-SoftwareMethodResult:

LMI_SoftwareMethodResult
------------------------

Class reference
===============
Subclass of :ref:`LMI_MethodResult <LMI-MethodResult>`

Jobs are sometimes used to represent extrinsic method invocations that execute for times longer than the length of time is reasonable to require a client to wait. The method executing continues beyond the method return to the client. The class provides the result of the execution of a Job that was itself started by the side-effect of this extrinsic method invocation. 

The indication instances embedded an instance of this class shall be the same indications delivered to listening clients or recorded, all or in part, to logs. Basically, this approach is a corollary to the functionality provided by an instance of ListenerDestinationLog (as defined in the Interop Model). The latter provides a comprehensive, persistent mechanism for recording Job results, but is also more resource-intensive and requires supporting logging functionality. Both the extra resources and logging may not be available in all environments (for example, embedded environments). Therefore, this instance-based approach is also provided. 

The MethodResult instances shall not exist after the associated ConcreteJob is deleted.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-SoftwareMethodResult-ElementName:

``string`` **ElementName**

    A user-friendly name for the object. This property allows each instance to define a user-friendly name in addition to its key properties, identity data, and description information. 

    Note that the Name property of ManagedSystemElement is also defined as a user-friendly name. But, it is often subclassed to be a Key. It is not reasonable that the same property can convey both identity and a user-friendly name, without inconsistencies. Where Name exists and is not a Key (such as for instances of LogicalDevice), the same information can be present in both the Name and ElementName properties. Note that if there is an associated instance of CIM_EnabledLogicalElementCapabilities, restrictions on this properties may exist as defined in ElementNameMask and MaxElementNameLen properties defined in that class.

    
.. _LMI-SoftwareMethodResult-Description:

``string`` **Description**

    The Description property provides a textual description of the object.

    
.. _LMI-SoftwareMethodResult-Caption:

``string`` **Caption**

    The Caption property is a short textual description (one- line string) of the object.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`InstanceID <LMI-MethodResult-InstanceID>`
| ``instance`` :ref:`PostCallIndication <CIM-MethodResult-PostCallIndication>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``instance`` :ref:`PreCallIndication <CIM-MethodResult-PreCallIndication>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

