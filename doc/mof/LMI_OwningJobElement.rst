.. _LMI-OwningJobElement:

LMI_OwningJobElement
--------------------

Class reference
===============
Subclass of :ref:`CIM_OwningJobElement <CIM-OwningJobElement>`

OwningJobElement represents an association between a Job and the ManagedElement responsible for the creation of the Job. This association may not be possible, given that the execution of jobs can move between systems and that the lifecycle of the creating entity may not persist for the total duration of the job. However, this can be very useful information when available. This association defines a more specific 'owner' than is provided by the CIM_Job.Owner string.


Key properties
^^^^^^^^^^^^^^

| :ref:`OwningElement <CIM-OwningJobElement-OwningElement>`
| :ref:`OwnedElement <CIM-OwningJobElement-OwnedElement>`

Local properties
^^^^^^^^^^^^^^^^

*None*

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| :ref:`CIM_ManagedElement <CIM-ManagedElement>` :ref:`OwningElement <CIM-OwningJobElement-OwningElement>`
| :ref:`CIM_Job <CIM-Job>` :ref:`OwnedElement <CIM-OwningJobElement-OwnedElement>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

