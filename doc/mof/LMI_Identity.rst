.. _LMI-Identity:

LMI_Identity
------------

Class reference
===============
Subclass of :ref:`CIM_Identity <CIM-Identity>`

An instance of an Identity represents a ManagedElement that acts as a security principal within the scope in which it is defined and authenticated. (Note that the Identity's scope is specified using the association, CIM_IdentityContext.) ManagedElements with Identities can be OrganizationalEntities, Services, Systems, etc. The ManagedElement 'behind' an Identity is described using the AssignedIdentity association. 



Within a given security context, an Identity may be imparted a level of trust, usually based on its credentials. A trust level is defined using the CIM_SecuritySensitivity class, and associated with Identity using CIM_ElementSecuritySensitivity. Whether an Identity is currently authenticated is evaluated by checking the CurrentlyAuthenticated boolean property. This property is set and cleared by the security infrastructure, and should only be readable within the management infrastructure. The conditions which must be met/authenticated in order for an Identity's CurrentlyAuthenticated Boolean to be TRUE are defined using a subclass of PolicyCondition - AuthenticationCondition. The inheritance tree for AuthenticationCondition is defined in the CIM Policy Model. 



Subclasses of Identity may include specific information related to a given AuthenticationService or authority (such as a security token or computer hardware port/communication details) that more specifically determine the authenticity of the Identity. An instance of Identity may be persisted even though it is not CurrentlyAuthenticated, in order to maintain static relationships to Roles, associations to accounting information, and policy data defining authentication requirements. Note however, when an Identity is not authenticated (CurrentlyAuthenticated = FALSE), then Privileges or rights SHOULD NOT be authorized. The lifetime, validity, and propagation of the Identity is dependent on a security infrastructure's policies.


Key properties
^^^^^^^^^^^^^^

| :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Local properties
^^^^^^^^^^^^^^^^

*None*

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`InstanceID <CIM-Identity-InstanceID>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``boolean`` :ref:`CurrentlyAuthenticated <CIM-Identity-CurrentlyAuthenticated>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

