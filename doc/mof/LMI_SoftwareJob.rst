.. _LMI-SoftwareJob:

LMI_SoftwareJob
---------------

Class reference
===============
Subclass of :ref:`LMI_ConcreteJob <LMI-ConcreteJob>`

A concrete version of Job. This class represents a generic and instantiable unit of work, such as a batch or a print job.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ConcreteJob-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-SoftwareJob-InstanceID:

``string`` **InstanceID**

    Within the scope of the instantiating Namespace, InstanceID opaquely and uniquely identifies an instance of this class. In order to ensure uniqueness within the NameSpace, the value of InstanceID SHOULD be constructed using the following 'preferred' algorithm: 

    <OrgID>:<LocalID> 

    Where <OrgID> and <LocalID> are separated by a colon ':', and where <OrgID> must include a copyrighted, trademarked or otherwise unique name that is owned by the business entity that is creating or defining the InstanceID, or that is a registered ID that is assigned to the business entity by a recognized global authority. (This requirement is similar to the <Schema Name>_<Class Name> structure of Schema class names.) In addition, to ensure uniqueness <OrgID> must not contain a colon (':'). When using this algorithm, the first colon to appear in InstanceID must appear between <OrgID> and <LocalID>. 

    <LocalID> is chosen by the business entity and should not be re-used to identify different underlying (real-world) elements. If the above 'preferred' algorithm is not used, the defining entity must assure that the resulting InstanceID is not re-used across any InstanceIDs produced by this or other providers for the NameSpace of this instance. 

    For DMTF defined instances, the 'preferred' algorithm must be used with the <OrgID> set to 'CIM'.

    
.. _LMI-SoftwareJob-Priority:

``uint32`` **Priority**

    Indicates the urgency or importance of execution of the Job. The lower the number, the higher the priority. Note that this property is also present in the JobProcessingStatistics class. This class is necessary to capture the setting information that would influence the results of a job.

    
.. _LMI-SoftwareJob-CommunicationStatus:

``uint16`` **CommunicationStatus**

    CommunicationStatus indicates the ability of the instrumentation to communicate with the underlying ManagedElement. CommunicationStatus consists of one of the following values: Unknown, None, Communication OK, Lost Communication, or No Contact. 

    A Null return indicates the implementation (provider) does not implement this property. 

    "Unknown" indicates the implementation is in general capable of returning this property, but is unable to do so at this time. 

    "Not Available" indicates that the implementation (provider) is capable of returning a value for this property, but not ever for this particular piece of hardware/software or the property is intentionally not used because it adds no meaningful information (as in the case of a property that is intended to add additional info to another property). 

    "Communication OK " indicates communication is established with the element, but does not convey any quality of service. 

    "No Contact" indicates that the monitoring system has knowledge of this element, but has never been able to establish communications with it. 

    "Lost Communication" indicates that the Managed Element is known to exist and has been contacted successfully in the past, but is currently unreachable.

    
    ======== ==================
    ValueMap Values            
    ======== ==================
    0        Unknown           
    1        Not Available     
    2        Communication OK  
    3        Lost Communication
    4        No Contact        
    ..       DMTF Reserved     
    0x8000.. Vendor Reserved   
    ======== ==================
    
.. _LMI-SoftwareJob-MethodName:

``string`` **MethodName**

    If not NULL, the name of the intrinsic operation or extrinsic method for which this Job represents an invocation.

    When not NULL, and if an extrinsic method, the format shall be <classPath>.MethodName, where classPath is a WBEM-URI-TypedClassPath or a WBEM-URI-UntypedClassPath as defined by DSP0207. And where methodName is a method of that class.

    When not NULL, and if an intrinsic operation, the format shall be <namespacePath>.OperationName, where namespacePath is a WBEM-URI-TypedNamespacePath or a WBEM-URI-UntypedNamespacePath as defined by DSP0207. And where OperationName is either the name of a generic operation as defined in DSP0223 or is the name of a protocol specific operation as defined for the protocol used to retrieve the instance.

    
.. _LMI-SoftwareJob-Description:

``string`` **Description**

    The Description property provides a textual description of the object.

    
.. _LMI-SoftwareJob-ErrorCode:

``uint16`` **ErrorCode**

    A vendor-specific error code. The value must be set to zero if the Job completed without error. Note that this property is also present in the JobProcessingStatistics class. This class is necessary to capture the processing information for recurring Jobs, because only the 'last' run error can be stored in this single-valued property.

    
.. _LMI-SoftwareJob-RecoveryAction:

``uint16`` **RecoveryAction**

    Describes the recovery action to be taken for an unsuccessfully run Job. The possible values are: 

    0 = "Unknown", meaning it is unknown as to what recovery action to take 

    1 = "Other", indicating that the recovery action will be specified in the OtherRecoveryAction property 

    2 = "Do Not Continue", meaning stop the execution of the job and appropriately update its status 

    3 = "Continue With Next Job", meaning continue with the next job in the queue 

    4 = "Re-run Job", indicating that the job should be re-run 

    5 = "Run Recovery Job", meaning run the Job associated using the RecoveryJob relationship. Note that the recovery Job must already be in the queue from which it will run.

    
    ======== ======================
    ValueMap Values                
    ======== ======================
    0        Unknown               
    1        Other                 
    2        Do Not Continue       
    3        Continue With Next Job
    4        Re-run Job            
    5        Run Recovery Job      
    ======== ======================
    
.. _LMI-SoftwareJob-JobStatus:

``string`` **JobStatus**

    A free-form string that represents the status of the job. The primary status is reflected in the inherited OperationalStatus property. JobStatus provides additional, implementation-specific details.

    
.. _LMI-SoftwareJob-Caption:

``string`` **Caption**

    The Caption property is a short textual description (one- line string) of the object.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`JobOutParameters <CIM-ConcreteJob-JobOutParameters>`
| ``uint32`` :ref:`JobRunTimes <CIM-Job-JobRunTimes>`
| ``string`` :ref:`OtherRecoveryAction <CIM-Job-OtherRecoveryAction>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``datetime`` :ref:`UntilTime <CIM-Job-UntilTime>`
| ``sint8`` :ref:`RunDay <CIM-Job-RunDay>`
| ``datetime`` :ref:`TimeOfLastStateChange <LMI-ConcreteJob-TimeOfLastStateChange>`
| ``uint8`` :ref:`RunMonth <CIM-Job-RunMonth>`
| ``uint16`` :ref:`PercentComplete <LMI-ConcreteJob-PercentComplete>`
| ``uint16`` :ref:`LocalOrUtcTime <LMI-ConcreteJob-LocalOrUtcTime>`
| ``datetime`` :ref:`TimeBeforeRemoval <LMI-ConcreteJob-TimeBeforeRemoval>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`Name <LMI-ConcreteJob-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``sint8`` :ref:`RunDayOfWeek <CIM-Job-RunDayOfWeek>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``datetime`` :ref:`ElapsedTime <LMI-ConcreteJob-ElapsedTime>`
| ``boolean`` :ref:`DeleteOnCompletion <LMI-ConcreteJob-DeleteOnCompletion>`
| ``datetime`` :ref:`TimeSubmitted <LMI-ConcreteJob-TimeSubmitted>`
| ``uint16`` :ref:`JobState <LMI-ConcreteJob-JobState>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``string`` :ref:`JobInParameters <CIM-ConcreteJob-JobInParameters>`
| ``string`` :ref:`ErrorDescription <CIM-Job-ErrorDescription>`
| ``datetime`` :ref:`RunStartInterval <CIM-Job-RunStartInterval>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``datetime`` :ref:`ScheduledStartTime <CIM-Job-ScheduledStartTime>`
| ``uint16[]`` :ref:`OperationalStatus <LMI-ConcreteJob-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`Notify <CIM-Job-Notify>`
| ``datetime`` :ref:`StartTime <LMI-ConcreteJob-StartTime>`
| ``string`` :ref:`Owner <CIM-Job-Owner>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`RequestStateChange <LMI-ConcreteJob-RequestStateChange>`
| :ref:`ResumeWithAction <CIM-ConcreteJob-ResumeWithAction>`
| :ref:`GetError <LMI-ConcreteJob-GetError>`
| :ref:`KillJob <CIM-Job-KillJob>`
| :ref:`ResumeWithInput <CIM-ConcreteJob-ResumeWithInput>`
| :ref:`GetErrors <LMI-ConcreteJob-GetErrors>`

