.. _LMI-SSSDDomain:

LMI_SSSDDomain
--------------

Class reference
===============
Subclass of :ref:`CIM_ManagedElement <CIM-ManagedElement>`

SSSD domain.


Key properties
^^^^^^^^^^^^^^

| :ref:`Name <LMI-SSSDDomain-Name>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-SSSDDomain-IsSubdomain:

``boolean`` **IsSubdomain**

    True if this is an autodiscovered subdomain.

    
.. _LMI-SSSDDomain-Realm:

``string`` **Realm**

    The Kerberos realm this domain is configured with.

    
.. _LMI-SSSDDomain-Name:

``string`` **Name**

    Name of the domain.

    
.. _LMI-SSSDDomain-BackupServers:

``string[]`` **BackupServers**

    List of backup servers for this domain.

    
.. _LMI-SSSDDomain-ParentDomain:

``string`` **ParentDomain**

    Name of the parent domain. It is not set if this domain is on top of the domain hierarchy.

    
.. _LMI-SSSDDomain-FullyQualifiedNameFormat:

``string`` **FullyQualifiedNameFormat**

    Format of fully qualified name this domain uses.

    
.. _LMI-SSSDDomain-UseFullyQualifiedNames:

``boolean`` **UseFullyQualifiedNames**

    True if objects from this domain can be accessed only via fully qualified name.

    
.. _LMI-SSSDDomain-MinId:

``uint32`` **MinId**

    Minimum UID and GID value for this domain.

    
.. _LMI-SSSDDomain-Provider:

``string`` **Provider**

    Main provider for this domain.

    
.. _LMI-SSSDDomain-PrimaryServers:

``string[]`` **PrimaryServers**

    List of primary servers for this domain.

    
.. _LMI-SSSDDomain-Forest:

``string`` **Forest**

    The domain forest this domain belongs to.

    
.. _LMI-SSSDDomain-Enumerate:

``boolean`` **Enumerate**

    True if this domain supports enumeration.

    
.. _LMI-SSSDDomain-MaxId:

``uint32`` **MaxId**

    Maximum UID and GID value for this domain.

    
.. _LMI-SSSDDomain-LoginFormat:

``string`` **LoginFormat**

    The login format this domain expects.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

