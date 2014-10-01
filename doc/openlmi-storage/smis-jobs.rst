SMI-S Job Control Subprofile
============================

OpenLMI-Storage implements the Job Control Subprofile with these adjustments:

* All indications are implemented, however the CQL query is different. SMI-S
  uses optional CQL extensions, e.g. ``ANY`` keyword, and our CIMOMs do not
  support that. Therefore all the CQL queries for
  ``OperationalStatus[*]`` were reworked to use ``JobState`` property.


Implementation
--------------

All mandatory classes and methods are implemented.

Classes
^^^^^^^

Implemented SMI-S classes:

* :ref:`LMI_AffectedStorageJobElement <LMI-AffectedStorageJobElement>`

* :ref:`LMI_AssociatedStorageJobMethodResult <LMI-AssociatedStorageJobMethodResult>`

* :ref:`LMI_StorageJob <LMI-StorageJob>`

* :ref:`StorageMethodResult <LMI-StorageMethodResult>`

* :ref:`LMI_OwningStorageJobElement <LMI-OwningStorageJobElement>`

Methods
^^^^^^^

* :ref:`GetErrors <LMI-ConcreteJob-GetErrors>`

* :ref:`GetError <LMI-ConcreteJob-GetError>`

* :ref:`RequestStateChange <LMI-ConcreteJob-RequestStateChange>`

Indications
^^^^^^^^^^^

See list of indications in :ref:`Jobs<job_indications>` chapter.
