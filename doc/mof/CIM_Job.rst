.. _CIM-Job:

CIM_Job
-------

Class reference
===============
Subclass of :ref:`CIM_LogicalElement <CIM-LogicalElement>`

A Job is a LogicalElement that represents an executing unit of work, such as a script or a print job. A Job is distinct from a Process in that a Job can be scheduled or queued, and its execution is not limited to a single system.


Key properties
^^^^^^^^^^^^^^


Local properties
^^^^^^^^^^^^^^^^

.. _CIM-Job-Priority:

``uint32`` **Priority**

    Indicates the urgency or importance of execution of the Job. The lower the number, the higher the priority. Note that this property is also present in the JobProcessingStatistics class. This class is necessary to capture the setting information that would influence the results of a job.

    
.. _CIM-Job-JobRunTimes:

``uint32`` **JobRunTimes**

    The number of times that the Job should be run. A value of 1 indicates that the Job is not recurring, while any non-zero value indicates a limit to the number of times that the Job will recur. Zero indicates that there is no limit to the number of times that the Job can be processed, but that it is terminated either after the UntilTime or by manual intervention. By default, a Job is processed once.

    
.. _CIM-Job-OtherRecoveryAction:

``string`` **OtherRecoveryAction**

    A string describing the recovery action when the RecoveryAction property of the instance is 1 ("Other").

    
.. _CIM-Job-UntilTime:

``datetime`` **UntilTime**

    The time after which the Job is invalid or should be stopped. This time can be represented by an actual date and time, or by an interval relative to the time that this property is requested. A value of all nines indicates that the Job can run indefinitely.

    
.. _CIM-Job-RunDay:

``sint8`` **RunDay**

    The day in the month on which the Job should be processed. There are two different interpretations for this property, depending on the value of DayOfWeek. In one case, RunDay defines the day-in-month on which the Job is processed. This interpretation is used when the DayOfWeek is 0. A positive or negative integer indicates whether the RunDay should be calculated from the beginning or end of the month. For example, 5 indicates the fifth day in the RunMonth and -1 indicates the last day in the RunMonth. 

    

    When RunDayOfWeek is not 0, RunDay is the day-in-month on which the Job is processed, defined in conjunction with RunDayOfWeek. For example, if RunDay is 15 and RunDayOfWeek is Saturday, then the Job is processed on the first Saturday on or after the 15th day in the RunMonth (for example, the third Saturday in the month). If RunDay is 20 and RunDayOfWeek is -Saturday, then this indicates the first Saturday on or before the 20th day in the RunMonth. If RunDay is -1 and RunDayOfWeek is -Sunday, then this indicates the last Sunday in the RunMonth.

    
.. _CIM-Job-RunMonth:

``uint8`` **RunMonth**

    The month during which the Job should be processed. Specify 0 for January, 1 for February, and so on.

    
    ======== =========
    ValueMap Values   
    ======== =========
    0        January  
    1        February 
    2        March    
    3        April    
    4        May      
    5        June     
    6        July     
    7        August   
    8        September
    9        October  
    10       November 
    11       December 
    ======== =========
    
.. _CIM-Job-ErrorCode:

``uint16`` **ErrorCode**

    A vendor-specific error code. The value must be set to zero if the Job completed without error. Note that this property is also present in the JobProcessingStatistics class. This class is necessary to capture the processing information for recurring Jobs, because only the 'last' run error can be stored in this single-valued property.

    
.. _CIM-Job-RecoveryAction:

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
    
.. _CIM-Job-PercentComplete:

``uint16`` **PercentComplete**

    The percentage of the job that has completed at the time that this value is requested. Note that this property is also present in the JobProcessingStatistics class. This class is necessary to capture the processing information for recurring Jobs, because only the 'last' run data can be stored in this single-valued property. 

    Note that the value 101 is undefined and will be not be allowed in the next major revision of the specification.

    
.. _CIM-Job-LocalOrUtcTime:

``uint16`` **LocalOrUtcTime**

    This property indicates whether the times represented in the RunStartInterval and UntilTime properties represent local times or UTC times. Time values are synchronized worldwide by using the enumeration value 2, "UTC Time".

    
    ======== ==========
    ValueMap Values    
    ======== ==========
    1        Local Time
    2        UTC Time  
    ======== ==========
    
.. _CIM-Job-RunDayOfWeek:

``sint8`` **RunDayOfWeek**

    A positive or negative integer used in conjunction with RunDay to indicate the day of the week on which the Job is processed. RunDayOfWeek is set to 0 to indicate an exact day of the month, such as March 1. A positive integer (representing Sunday, Monday, ..., Saturday) means that the day of week is found on or after the specified RunDay. A negative integer (representing -Sunday, -Monday, ..., -Saturday) means that the day of week is found on or BEFORE the RunDay.

    
    ======== ===============
    ValueMap Values         
    ======== ===============
    -7       -Saturday      
    -6       -Friday        
    -5       -Thursday      
    -4       -Wednesday     
    -3       -Tuesday       
    -2       -Monday        
    -1       -Sunday        
    0        ExactDayOfMonth
    1        Sunday         
    2        Monday         
    3        Tuesday        
    4        Wednesday      
    5        Thursday       
    6        Friday         
    7        Saturday       
    ======== ===============
    
.. _CIM-Job-JobStatus:

``string`` **JobStatus**

    A free-form string that represents the status of the job. The primary status is reflected in the inherited OperationalStatus property. JobStatus provides additional, implementation-specific details.

    
.. _CIM-Job-ElapsedTime:

``datetime`` **ElapsedTime**

    The time interval that the Job has been executing or the total execution time if the Job is complete. Note that this property is also present in the JobProcessingStatistics class. This class is necessary to capture the processing information for recurring Jobs, because only the 'last' run time can be stored in this single-valued property.

    
.. _CIM-Job-DeleteOnCompletion:

``boolean`` **DeleteOnCompletion**

    Indicates whether or not the job should be automatically deleted upon completion. Note that the 'completion' of a recurring job is defined by its JobRunTimes or UntilTime properties, or when the Job is terminated by manual intervention. If this property is set to false and the job completes, then the extrinsic method DeleteInstance must be used to delete the job instead of updating this property.

    
.. _CIM-Job-TimeSubmitted:

``datetime`` **TimeSubmitted**

    The time that the Job was submitted to execute. A value of all zeroes indicates that the owning element is not capable of reporting a date and time. Therefore, the ScheduledStartTime and StartTime are reported as intervals relative to the time their values are requested.

    
.. _CIM-Job-ErrorDescription:

``string`` **ErrorDescription**

    A free-form string that contains the vendor error description. Note that this property is also present in the JobProcessingStatistics class. This class is necessary to capture the processing information for recurring Jobs, because only the 'last' run error can be stored in this single-valued property.

    
.. _CIM-Job-RunStartInterval:

``datetime`` **RunStartInterval**

    The time interval after midnight when the Job should be processed. For example, 

    00000000020000.000000:000 

    indicates that the Job should be run on or after two o'clock, local time or UTC time (distinguished using the LocalOrUtcTime property.

    
.. _CIM-Job-ScheduledStartTime:

``datetime`` **ScheduledStartTime**

    The time that the current Job is scheduled to start. This time can be represented by the actual date and time, or an interval relative to the time that this property is requested. A value of all zeroes indicates that the Job is already executing. The property is deprecated in lieu of the more expressive scheduling properties, RunMonth, RunDay, RunDayOfWeek, and RunStartInterval.

    
.. _CIM-Job-Notify:

``string`` **Notify**

    The User who is to be notified upon the Job completion or failure.

    
.. _CIM-Job-StartTime:

``datetime`` **StartTime**

    The time that the Job was actually started. This time can be represented by an actual date and time, or by an interval relative to the time that this property is requested. Note that this property is also present in the JobProcessingStatistics class. This class is necessary to capture the processing information for recurring Jobs, because only the 'last' run time can be stored in this single-valued property.

    
.. _CIM-Job-Owner:

``string`` **Owner**

    The User that submitted the Job, or the Service or method name that caused the job to be created.

    

Local methods
^^^^^^^^^^^^^

    .. _CIM-Job-KillJob:

``uint32`` **KillJob** (``boolean`` DeleteOnKill)

    **Deprecated!** 
    KillJob is being deprecated because there is no distinction made between an orderly shutdown and an immediate kill. CIM_ConcreteJob.RequestStateChange() provides 'Terminate' and 'Kill' options to allow this distinction. 

    A method to kill this job and any underlying processes, and to remove any 'dangling' associations.

    
    ============ ===============
    ValueMap     Values         
    ============ ===============
    0            Success        
    1            Not Supported  
    2            Unknown        
    3            Timeout        
    4            Failed         
    6            Access Denied  
    7            Not Found      
    ..           DMTF Reserved  
    32768..65535 Vendor Specific
    ============ ===============
    
    **Parameters**
    
        *IN* ``boolean`` **DeleteOnKill**
            Indicates whether or not the Job should be automatically deleted upon termination. This parameter takes precedence over the property, DeleteOnCompletion.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``uint16`` :ref:`CommunicationStatus <CIM-ManagedSystemElement-CommunicationStatus>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`Name <CIM-ManagedSystemElement-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint16`` :ref:`PrimaryStatus <CIM-ManagedSystemElement-PrimaryStatus>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``uint16[]`` :ref:`OperationalStatus <CIM-ManagedSystemElement-OperationalStatus>`
| ``uint16`` :ref:`OperatingStatus <CIM-ManagedSystemElement-OperatingStatus>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

