Usage
=====

The OpenLMI Realmd provider allows for basic configuration of the managed
systems Active Directory or Kerberos realms membership. It relies on the Realmd
system service.

Querying a domain membership
----------------------------

To verify if the remote machine is part of the domain, it is enough to query the
value of the :ref:`LMI_RealmdService.Domain<LMI-RealmdService-Domain>` property:
If non-NULL it contains the name of the joined domain::

    #!/usr/bin/lmishell
    c = connect("localhost", "pegasus", "test")
    realmsrv = c.root.cimv2.LMI_RealmdService.first_instance()
    dom = realmsrv.Domain
    if (dom):
        print "Joined to the domain: " + dom
    else:
        print "No domain joined."

Joining a domain
----------------

The :ref:`LMI_RealmdService.JoinDomain()<LMI-RealmdService-JoinDomain>` method
can be used to join a domain. It takes three mandatory arguments: username and
password for the authentication and the domain name::

    #!/usr/bin/lmishell
    c = connect("localhost", "pegasus", "test")
    realmsrv = c.root.cimv2.LMI_RealmdService.first_instance()
    realmsrv.JoinDomain(Password='ZisIzSECRET', User='admin', Domain='AD.EXAMPLE.COM')

Leaving a domain
----------------

Similarly to joining a domain the
:ref:`LMI_RealmdService.LeaveDomain()<LMI-RealmdService-LeaveDomain>` can be used
to leave the joined domain. It requires the same arguments as the
:ref:`JoinDomain()<LMI-RealmdService-JoinDomain>` method::

    #!/usr/bin/lmishell
    c = connect("localhost", "pegasus", "test")
    realmsrv = c.root.cimv2.LMI_RealmdService.first_instance()
    realmsrv.LeaveDomain(Password='ZisIzSECRET', User='admin', Domain='AD.EXAMPLE.COM')
