.. _LMI-NetworkRemoteAccessAvailableToElement:

LMI_NetworkRemoteAccessAvailableToElement
-----------------------------------------

Class reference
===============
Subclass of :ref:`CIM_RemoteAccessAvailableToElement <CIM-RemoteAccessAvailableToElement>`

Describes an element's knowledge regarding accessing other (i.e., remote) Servers and Systems.


Key properties
^^^^^^^^^^^^^^

| :ref:`Dependent <CIM-Dependency-Dependent>`
| :ref:`Antecedent <CIM-Dependency-Antecedent>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-NetworkRemoteAccessAvailableToElement-Dependent:

:ref:`CIM_ServiceAccessPoint <CIM-ServiceAccessPoint>` **Dependent**

    The ServiceAccessPoint which has knowledge of the remote server or system.

    
.. _LMI-NetworkRemoteAccessAvailableToElement-Antecedent:

:ref:`LMI_NetworkRemoteServiceAccessPoint <LMI-NetworkRemoteServiceAccessPoint>` **Antecedent**

    The remote server or system.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``uint16`` :ref:`OrderOfAccess <CIM-RemoteAccessAvailableToElement-OrderOfAccess>`
| ``boolean`` :ref:`IsDefault <CIM-RemoteAccessAvailableToElement-IsDefault>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

