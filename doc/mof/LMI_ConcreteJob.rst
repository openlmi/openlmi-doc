.. _LMI-ConcreteJob:

LMI_ConcreteJob
---------------

Class reference
===============
Subclass of :ref:`CIM_ConcreteJob <CIM-ConcreteJob>`

A concrete version of Job. This class represents a generic and instantiable unit of work, such as a batch or a print job.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ConcreteJob-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-ConcreteJob-JobState:

``uint16`` **JobState**

    JobState is an integer enumeration that indicates the operational state of a Job. It can also indicate transitions between these states, for example, 'Shutting Down' and 'Starting'. Following is a brief description of the states: 

    New (2) indicates that the job has never been started. 

    Starting (3) indicates that the job is moving from the 'New', 'Suspended', or 'Service' states into the 'Running' state. 

    Running (4) indicates that the Job is running. 

    Suspended (5) indicates that the Job is stopped, but can be restarted in a seamless manner. 

    Shutting Down (6) indicates that the job is moving to a 'Completed', 'Terminated', or 'Killed' state. 

    Completed (7) indicates that the job has completed normally. 

    Terminated (8) indicates that the job has been stopped by a 'Terminate' state change request. The job and all its underlying processes are ended and can be restarted (this is job-specific) only as a new job. 

    Killed (9) indicates that the job has been stopped by a 'Kill' state change request. Underlying processes might have been left running, and cleanup might be required to free up resources. 

    Exception (10) indicates that the Job is in an abnormal state that might be indicative of an error condition. Actual status might be displayed though job-specific objects. 

    Service (11) indicates that the Job is in a vendor-specific state that supports problem discovery, or resolution, or both.

    Query pending (12) waiting for a client to resolve a query

    
    ============ ===============
    ValueMap     Values         
    ============ ===============
    2            New            
    3            Starting       
    4            Running        
    5            Suspended      
    6            Shutting Down  
    7            Completed      
    8            Terminated     
    9            Killed         
    10           Exception      
    11           Service        
    12           Query Pending  
    13..32767    DMTF Reserved  
    32768..65535 Vendor Reserved
    ============ ===============
    
.. _LMI-ConcreteJob-TimeOfLastStateChange:

``datetime`` **TimeOfLastStateChange**

    The date or time when the state of the Job last changed. If the state of the Job has not changed and this property is populated, then it must be set to a 0 interval value. If a state change was requested, but rejected or not yet processed, the property must not be updated.

    
.. _LMI-ConcreteJob-PercentComplete:

``uint16`` **PercentComplete**

    The percentage of the job that has completed at the time that this value is requested. Note that this property is also present in the JobProcessingStatistics class. This class is necessary to capture the processing information for recurring Jobs, because only the 'last' run data can be stored in this single-valued property. 

    Note that the value 101 is undefined and will be not be allowed in the next major revision of the specification.

    
.. _LMI-ConcreteJob-LocalOrUtcTime:

``uint16`` **LocalOrUtcTime**

    This property indicates whether the times represented in the RunStartInterval and UntilTime properties represent local times or UTC times. Time values are synchronized worldwide by using the enumeration value 2, "UTC Time".

    
    ======== ==========
    ValueMap Values    
    ======== ==========
    1        Local Time
    2        UTC Time  
    ======== ==========
    
.. _LMI-ConcreteJob-TimeBeforeRemoval:

``datetime`` **TimeBeforeRemoval**

    The amount of time that the Job is retained after it has finished executing, either succeeding or failing in that execution. The job must remain in existence for some period of time regardless of the value of the DeleteOnCompletion property. 

    The default is five minutes.

    
.. _LMI-ConcreteJob-Name:

``string`` **Name**

    The user-friendly name for this instance of a Job. In addition, the user-friendly name can be used as a property for a search or query. (Note: Name does not have to be unique within a namespace.)

    
.. _LMI-ConcreteJob-DeleteOnCompletion:

``boolean`` **DeleteOnCompletion**

    Indicates whether or not the job should be automatically deleted upon completion. Note that the 'completion' of a job includes when the Job is terminated by manual intervention. 

    If this property is set to false and the job completes, then the intrinsic method DeleteInstance must be used to delete the job instead of updating this property.

    If this property is set to true and the job completes, then the job may be deleted after the TimeBeforeRemoval interval.

    If there is a CIM_DiagnosticServiceJobCapabilities associated to the service that spawned the job, then the DeleteOnCompletion should be TRUE if CIM_DiagnosticServiceJobCapabilities.DeleteJobSupported is FALSE. If DeleteOnCompletion is FALSE, then CIM_DiagnosticServiceJobCapabilities.CleanupInterval should be non-NULL.

    
.. _LMI-ConcreteJob-ElapsedTime:

``datetime`` **ElapsedTime**

    The time interval that the Job has been executing or the total execution time if the Job is complete. Note that this property is also present in the JobProcessingStatistics class. This class is necessary to capture the processing information for recurring Jobs, because only the 'last' run time can be stored in this single-valued property.

    
.. _LMI-ConcreteJob-TimeSubmitted:

``datetime`` **TimeSubmitted**

    The time that the Job was submitted to execute. A value of all zeroes indicates that the owning element is not capable of reporting a date and time. Therefore, the ScheduledStartTime and StartTime are reported as intervals relative to the time their values are requested.

    
.. _LMI-ConcreteJob-OperationalStatus:

``uint16[]`` **OperationalStatus**

    Indicates the current statuses of the element. Various operational statuses are defined. Many of the enumeration's values are self-explanatory. However, a few are not and are described here in more detail. 

    "Stressed" indicates that the element is functioning, but needs attention. Examples of "Stressed" states are overload, overheated, and so on. 

    "Predictive Failure" indicates that an element is functioning nominally but predicting a failure in the near future. 

    "In Service" describes an element being configured, maintained, cleaned, or otherwise administered. 

    "No Contact" indicates that the monitoring system has knowledge of this element, but has never been able to establish communications with it. 

    "Lost Communication" indicates that the ManagedSystem Element is known to exist and has been contacted successfully in the past, but is currently unreachable. 

    "Stopped" and "Aborted" are similar, although the former implies a clean and orderly stop, while the latter implies an abrupt stop where the state and configuration of the element might need to be updated. 

    "Dormant" indicates that the element is inactive or quiesced. 

    "Supporting Entity in Error" indicates that this element might be "OK" but that another element, on which it is dependent, is in error. An example is a network service or endpoint that cannot function due to lower-layer networking problems. 

    "Completed" indicates that the element has completed its operation. This value should be combined with either OK, Error, or Degraded so that a client can tell if the complete operation Completed with OK (passed), Completed with Error (failed), or Completed with Degraded (the operation finished, but it did not complete OK or did not report an error). 

    "Power Mode" indicates that the element has additional power model information contained in the Associated PowerManagementService association. 

    "Relocating" indicates the element is being relocated.

    OperationalStatus replaces the Status property on ManagedSystemElement to provide a consistent approach to enumerations, to address implementation needs for an array property, and to provide a migration path from today's environment to the future. This change was not made earlier because it required the deprecated qualifier. Due to the widespread use of the existing Status property in management applications, it is strongly recommended that providers or instrumentation provide both the Status and OperationalStatus properties. Further, the first value of OperationalStatus should contain the primary status for the element. When instrumented, Status (because it is single-valued) should also provide the primary status of the element.

    
    ======== ==========================
    ValueMap Values                    
    ======== ==========================
    0        Unknown                   
    1        Other                     
    2        OK                        
    3        Degraded                  
    4        Stressed                  
    5        Predictive Failure        
    6        Error                     
    7        Non-Recoverable Error     
    8        Starting                  
    9        Stopping                  
    10       Stopped                   
    11       In Service                
    12       No Contact                
    13       Lost Communication        
    14       Aborted                   
    15       Dormant                   
    16       Supporting Entity in Error
    17       Completed                 
    18       Power Mode                
    19       Relocating                
    ..       DMTF Reserved             
    0x8000.. Vendor Reserved           
    ======== ==========================
    
.. _LMI-ConcreteJob-StartTime:

``datetime`` **StartTime**

    The time that the Job was actually started. This time can be represented by an actual date and time, or by an interval relative to the time that this property is requested. Note that this property is also present in the JobProcessingStatistics class. This class is necessary to capture the processing information for recurring Jobs, because only the 'last' run time can be stored in this single-valued property.

    

Local methods
^^^^^^^^^^^^^

    .. _LMI-ConcreteJob-RequestStateChange:

``uint32`` **RequestStateChange** (``uint16`` RequestedState, ``datetime`` TimeoutPeriod)

    Requests that the state of the job be changed to the value specified in the RequestedState parameter. Invoking the RequestStateChange method multiple times could result in earlier requests being overwritten or lost. 

    If 0 is returned, then the task completed successfully. Any other return code indicates an error condition.

    
    ============ ==============================================
    ValueMap     Values                                        
    ============ ==============================================
    0            Completed with No Error                       
    1            Not Supported                                 
    2            Unknown/Unspecified Error                     
    3            Can NOT complete within Timeout Period        
    4            Failed                                        
    5            Invalid Parameter                             
    6            In Use                                        
    ..           DMTF Reserved                                 
    4096         Method Parameters Checked - Transition Started
    4097         Invalid State Transition                      
    4098         Use of Timeout Parameter Not Supported        
    4099         Busy                                          
    4100..32767  Method Reserved                               
    32768..65535 Vendor Specific                               
    ============ ==============================================
    
    **Parameters**
    
        *IN* ``uint16`` **RequestedState**
            RequestStateChange changes the state of a job. The possible values are as follows: 

            Start (2) changes the state to 'Running'. 

            Suspend (3) stops the job temporarily. The intention is to subsequently restart the job with 'Start'. It might be possible to enter the 'Service' state while suspended. (This is job-specific.) 

            Terminate (4) stops the job cleanly, saving data, preserving the state, and shutting down all underlying processes in an orderly manner. 

            Kill (5) terminates the job immediately with no requirement to save data or preserve the state. 

            Service (6) puts the job into a vendor-specific service state. It might be possible to restart the job.

            
            ============ ===============
            ValueMap     Values         
            ============ ===============
            2            Start          
            3            Suspend        
            4            Terminate      
            5            Kill           
            6            Service        
            7..32767     DMTF Reserved  
            32768..65535 Vendor Reserved
            ============ ===============
            
        
        *IN* ``datetime`` **TimeoutPeriod**
            A timeout period that specifies the maximum amount of time that the client expects the transition to the new state to take. The interval format must be used to specify the TimeoutPeriod. A value of 0 or a null parameter indicates that the client has no time requirements for the transition. 

            If this property does not contain 0 or null and the implementation does not support this parameter, a return code of 'Use Of Timeout Parameter Not Supported' must be returned.

            
        
    
    .. _LMI-ConcreteJob-GetError:

``uint32`` **GetError** (``string`` Error)

    **Deprecated!** 
    GetError is deprecated because Error should be an array,not a scalar.

    When the job is executing or has terminated without error, then this method returns no CIM_Error instance. However, if the job has failed because of some internal problem or because the job has been terminated by a client, then a CIM_Error instance is returned.

    
    ============ =================
    ValueMap     Values           
    ============ =================
    0            Success          
    1            Not Supported    
    2            Unspecified Error
    3            Timeout          
    4            Failed           
    5            Invalid Parameter
    6            Access Denied    
    ..           DMTF Reserved    
    32768..65535 Vendor Specific  
    ============ =================
    
    **Parameters**
    
        *OUT* ``string`` **Error**
            If the OperationalStatus on the Job is not "OK", then this method will return a CIM Error instance. Otherwise, when the Job is "OK", null is returned.

            
        
    
    .. _LMI-ConcreteJob-GetErrors:

``uint32`` **GetErrors** (``string[]`` Errors)

    If JobState is "Completed" and Operational Status is "Completed" then no instance of CIM_Error is returned. 

    If JobState is "Exception" then GetErrors may return intances of CIM_Error related to the execution of the procedure or method invoked by the job.

    If Operatational Status is not "OK" or "Completed"then GetErrors may return CIM_Error instances related to the running of the job.

    
    ============ =================
    ValueMap     Values           
    ============ =================
    0            Success          
    1            Not Supported    
    2            Unspecified Error
    3            Timeout          
    4            Failed           
    5            Invalid Parameter
    6            Access Denied    
    ..           DMTF Reserved    
    32768..65535 Vendor Specific  
    ============ =================
    
    **Parameters**
    
        *OUT* ``string[]`` **Errors**
            If the OperationalStatus on the Job is not "OK", then this method will return one or more CIM Error instance(s). Otherwise, when the Job is "OK", null is returned.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ConcreteJob-InstanceID>`
| ``uint32`` :ref:`Priority <CIM-Job-Priority>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`JobOutParameters <CIM-ConcreteJob-JobOutParameters>`
| ``uint32`` :ref:`JobRunTimes <CIM-Job-JobRunTimes>`
| ``string`` :ref:`OtherRecoveryAction <CIM-Job-OtherRecoveryAction>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``datetime`` :ref:`UntilTime <CIM-Job-UntilTime>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``sint8`` :ref:`RunDay <CIM-Job-RunDay>`
| ``uint8`` :ref:`RunMonth <CIM-Job-RunMonth>`
| ``uint16`` :ref:`ErrorCode <CIM-Job-ErrorCode>`
| ``uint16`` :ref:`RecoveryAction <CIM-Job-RecoveryAction>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``sint8`` :ref:`RunDayOfWeek <CIM-Job-RunDayOfWeek>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`JobStatus <CIM-Job-JobStatus>`
| ``string`` :ref:`MethodName <CIM-ConcreteJob-MethodName>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``string`` :ref:`JobInParameters <CIM-ConcreteJob-JobInParameters>`
| ``string`` :ref:`ErrorDescription <CIM-Job-ErrorDescription>`
| ``datetime`` :ref:`RunStartInterval <CIM-Job-RunStartInterval>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``datetime`` :ref:`ScheduledStartTime <CIM-Job-ScheduledStartTime>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`
| ``string`` :ref:`Notify <CIM-Job-Notify>`
| ``string`` :ref:`Owner <CIM-Job-Owner>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`ResumeWithAction <CIM-ConcreteJob-ResumeWithAction>`
| :ref:`KillJob <CIM-Job-KillJob>`
| :ref:`ResumeWithInput <CIM-ConcreteJob-ResumeWithInput>`

