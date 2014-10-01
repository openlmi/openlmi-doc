.. _LMI-MethodResult:

LMI_MethodResult
----------------

Class reference
===============
Subclass of :ref:`CIM_MethodResult <CIM-MethodResult>`

Jobs are sometimes used to represent extrinsic method invocations that execute for times longer than the length of time is reasonable to require a client to wait. The method executing continues beyond the method return to the client. The class provides the result of the execution of a Job that was itself started by the side-effect of this extrinsic method invocation. 

The indication instances embedded an instance of this class shall be the same indications delivered to listening clients or recorded, all or in part, to logs. Basically, this approach is a corollary to the functionality provided by an instance of ListenerDestinationLog (as defined in the Interop Model). The latter provides a comprehensive, persistent mechanism for recording Job results, but is also more resource-intensive and requires supporting logging functionality. Both the extra resources and logging may not be available in all environments (for example, embedded environments). Therefore, this instance-based approach is also provided. 

The MethodResult instances shall not exist after the associated ConcreteJob is deleted.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-MethodResult-InstanceID:

``string`` **InstanceID**

    Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. In order to ensure uniqueness within the NameSpace, the value of InstanceID SHOULD be constructed using the following 'preferred' algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon ':', and where <OrgID> MUST include a copyrighted, trademarked or otherwise unique name that is owned by the business entity creating/defining the InstanceID, or is a registered ID that is assigned to the business entity by a recognized global authority (This is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness <OrgID> MUST NOT contain a colon (':'). When using this algorithm, the first colon to appear in InstanceID MUST appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and SHOULD not be re-used to identify different underlying (real-world) elements. If the above 'preferred' algorithm is not used, the defining entity MUST assure that the resultant InstanceID is not re-used across any InstanceIDs produced by this or other providers for this instance's NameSpace. 

    For DMTF defined instances, the 'preferred' algorithm MUST be used with the <OrgID> set to 'CIM'.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``instance`` :ref:`PostCallIndication <CIM-MethodResult-PostCallIndication>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``instance`` :ref:`PreCallIndication <CIM-MethodResult-PreCallIndication>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

