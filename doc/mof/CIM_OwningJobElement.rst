.. _CIM-OwningJobElement:

CIM_OwningJobElement
--------------------

Class reference
===============
OwningJobElement represents an association between a Job and the ManagedElement responsible for the creation of the Job. This association may not be possible, given that the execution of jobs can move between systems and that the lifecycle of the creating entity may not persist for the total duration of the job. However, this can be very useful information when available. This association defines a more specific 'owner' than is provided by the CIM_Job.Owner string.


Key properties
^^^^^^^^^^^^^^

| :ref:`OwningElement <CIM-OwningJobElement-OwningElement>`
| :ref:`OwnedElement <CIM-OwningJobElement-OwnedElement>`

Local properties
^^^^^^^^^^^^^^^^

.. _CIM-OwningJobElement-OwningElement:

:ref:`CIM_ManagedElement <CIM-ManagedElement>` **OwningElement**

    The ManagedElement responsible for the creation of the Job.

    
.. _CIM-OwningJobElement-OwnedElement:

:ref:`CIM_Job <CIM-Job>` **OwnedElement**

    The Job created by the ManagedElement.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

*None*

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

