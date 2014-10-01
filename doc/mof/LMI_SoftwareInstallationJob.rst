.. _LMI-SoftwareInstallationJob:

LMI_SoftwareInstallationJob
---------------------------

Class reference
===============
Subclass of :ref:`LMI_SoftwareJob <LMI-SoftwareJob>`

A concrete version of Job. This class represents a generic and instantiable unit of work, such as a batch or a print job.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ConcreteJob-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

*None*

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`HealthState <CIM-ManagedSystemElement-HealthState>`
| ``string[]`` :ref:`StatusDescriptions <CIM-ManagedSystemElement-StatusDescriptions>`
| ``string`` :ref:`InstanceID <LMI-SoftwareJob-InstanceID>`
| ``uint32`` :ref:`Priority <LMI-SoftwareJob-Priority>`
| ``uint16`` :ref:`CommunicationStatus <LMI-SoftwareJob-CommunicationStatus>`
| ``string`` :ref:`JobOutParameters <CIM-ConcreteJob-JobOutParameters>`
| ``uint32`` :ref:`JobRunTimes <CIM-Job-JobRunTimes>`
| ``string`` :ref:`OtherRecoveryAction <CIM-Job-OtherRecoveryAction>`
| ``string`` :ref:`Status <CIM-ManagedSystemElement-Status>`
| ``datetime`` :ref:`UntilTime <CIM-Job-UntilTime>`
| ``string`` :ref:`MethodName <LMI-SoftwareJob-MethodName>`
| ``string`` :ref:`Description <LMI-SoftwareJob-Description>`
| ``sint8`` :ref:`RunDay <CIM-Job-RunDay>`
| ``datetime`` :ref:`TimeOfLastStateChange <LMI-ConcreteJob-TimeOfLastStateChange>`
| ``uint8`` :ref:`RunMonth <CIM-Job-RunMonth>`
| ``uint16`` :ref:`ErrorCode <LMI-SoftwareJob-ErrorCode>`
| ``uint16`` :ref:`RecoveryAction <LMI-SoftwareJob-RecoveryAction>`
| ``uint16`` :ref:`PercentComplete <LMI-ConcreteJob-PercentComplete>`
| ``uint16`` :ref:`LocalOrUtcTime <LMI-ConcreteJob-LocalOrUtcTime>`
| ``datetime`` :ref:`TimeBeforeRemoval <LMI-ConcreteJob-TimeBeforeRemoval>`
| ``uint16`` :ref:`DetailedStatus <CIM-ManagedSystemElement-DetailedStatus>`
| ``string`` :ref:`Name <LMI-ConcreteJob-Name>`
| ``datetime`` :ref:`InstallDate <CIM-ManagedSystemElement-InstallDate>`
| ``sint8`` :ref:`RunDayOfWeek <CIM-Job-RunDayOfWeek>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`JobStatus <LMI-SoftwareJob-JobStatus>`
| ``datetime`` :ref:`ElapsedTime <LMI-ConcreteJob-ElapsedTime>`
| ``string`` :ref:`Caption <LMI-SoftwareJob-Caption>`
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

