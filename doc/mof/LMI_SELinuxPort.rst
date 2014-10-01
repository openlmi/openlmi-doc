.. _LMI-SELinuxPort:

LMI_SELinuxPort
---------------

Class reference
===============
Subclass of :ref:`LMI_SELinuxElement <LMI-SELinuxElement>`

Class representing an SELinux port. It can encompass multiple individual network ports, or even their ranges.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-SELinuxPort-Protocol:

``uint16`` **Protocol**

    Protocol type. Only UDP and TCP are supported.

    
    ======== ======
    ValueMap Values
    ======== ======
    0        UDP   
    1        TCP   
    ======== ======
    
.. _LMI-SELinuxPort-SELinuxContext:

``string`` **SELinuxContext**

    SELinux context.

    
.. _LMI-SELinuxPort-Ports:

``string[]`` **Ports**

    Array of open ports that the SELinux port corresponds to.

    Individual values can be specified either as a single number, or a range.

    The range would be represented as '<port_low>-<port_high>', e.g. '1024-2048'.Note that a network port can be labeled with multiple labels at the same time.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`InstanceID <LMI-SELinuxElement-InstanceID>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

