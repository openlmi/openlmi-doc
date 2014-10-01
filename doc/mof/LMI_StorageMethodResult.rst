.. _LMI-StorageMethodResult:

LMI_StorageMethodResult
-----------------------

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

*None*

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`InstanceID <LMI-MethodResult-InstanceID>`
| ``instance`` :ref:`PostCallIndication <CIM-MethodResult-PostCallIndication>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``instance`` :ref:`PreCallIndication <CIM-MethodResult-PreCallIndication>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

