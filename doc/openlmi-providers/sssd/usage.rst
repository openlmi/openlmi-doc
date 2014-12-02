Usage
=====

All further below code assumes that a connection object has been created and the
default namespace (root/cimv2) is used::

    c = connect("https://myhost", "user", "secret")

Also, the ``sssd`` system service must be running.

List domains
------------

To list domains that SSSD knows about, simply list
:ref:`LMI_SSSDDomain <LMI-SSSDDomain>` instances::

    domains = c.root.cimv2.LMI_SSSDDomain.instances()
    for d in domains:
        print 'Domain:', d.Name
        print '  Realm:', d.Realm
        print '  Parent domain:', d.ParentDomain

Disable a domain
----------------

To disable a domain, call :ref:`Disable() <LMI-SSSDComponent-disable>` method on
:ref:`LMI_SSSDBackend <LMI-SSSDBackend>`, associated to appropriate
:ref:`LMI_SSSDDomain <LMI-SSSDDomain>` instance::

    # Find LMI_SSSDDomain
    domain = c.root.cimv2.LMI_SSSDDomain.first_instance({'Name': 'mydomain.example.com'})
    # Find associated LMI_SSSDBackendDomain
    backend = domain.first_associator(ResultClass='LMI_SSSDBackend')
    backend.Disable()

To enable domain, simply call :ref:`Enable() <LMI-SSSDComponent-enable>` method
instead.

