Usage
=====

Examples for common use cases listed below are written in `lmishell`_. Where
appropriate, an example for ``lmi`` meta-command, which is a part of
*OpenLMI-Scripts* project, is added. Please refer to its `documentation`_
for installation notes and usage.

.. note::
    Examples below are written for ``openlmi-tools`` version ``0.9``.

Listing installed packages
--------------------------
Simple
~~~~~~
Simple but very slow way: ::

    c = connect("host", "user", "pass")
    cs = c.root.cimv2.PG_ComputerSystem.first_instance()
    for identity in cs.associators(
            AssocClass="LMI_InstalledSoftwareIdentity",
            Role="System",
            ResultRole="InstalledSoftware",
            ResultClass="LMI_SoftwareIdentity"):
        print(identity.ElementName)

.. note::
    Here we use ``PG_ComputerSystem`` as a class representing computer
    system. It is part of ``sblim-cmpi-base`` package, which is obsoleted.
    If you use *Pegasus* as your *CIMOM* you may safely switch to
    ``PG_ComputerSystem``.

.. seealso::
    :ref:`LMI_InstalledSoftwareIdentity<LMI-InstalledSoftwareIdentity>`

Faster
~~~~~~
This is much faster. Here we enumerate association class
:ref:`LMI_InstalledSoftwareIdentity<LMI-InstalledSoftwareIdentity>` and
get information from its key properties. ::

        c = connect("host", "user", "pass")
        for iname in c.root.cimv2.LMI_InstalledSoftwareIdentity.instance_names():
            print(iname.InstalledSoftware.InstanceID
                    [len("LMI:LMI_SoftwareIdentity:"):])

.. note::
    Whole instance is not available. To get it from association instance name,
    you need to add: ::

        iname.InstalledSoftware.to_instance()


``lmi`` meta-command
~~~~~~~~~~~~~~~~~~~~
::

    lmi -h $HOST sw list pkgs

Listing repositories
--------------------
lmishell
~~~~~~~~
::

    c = connect("host", "user", "pass")
    for repo in c.root.cimv2.LMI_SoftwareIdentityResource.instance_names():
        print(repo.Name)

.. seealso::
    :ref:`LMI_SoftwareIdentityResource<LMI-SoftwareIdentityResource>`

``lmi`` meta-command
~~~~~~~~~~~~~~~~~~~~
::

    lmi -h $HOST sw list pkgs

Listing available packages
--------------------------
lmishell
~~~~~~~~
Enumerating of :ref:`LMI_SoftwareIdentity<LMI-SoftwareIdentity>` is
disabled due to a huge amount of data being generated. That's why we
enumerate them for particular repository represented by
:ref:`LMI_SoftwareIdentityResource<LMI-SoftwareIdentityResource>`. ::

    c = connect("host", "user", "pass")
    for repo in c.root.cimv2.LMI_SoftwareIdentityResource.instances():
        if repo.EnabledState != c.root.cimv2.LMI_SoftwareIdentityResource. \
                EnabledStateValues.Enabled:
            continue                  # skip disabled repositories
        print(repo.Name)
        for identity in repo.associator_names(
                AssocClass="LMI_ResourceForSoftwareIdentity",
                Role="AvailableSAP",
                ResultRole="ManagedElement",
                ResultClass="LMI_SoftwareIdentity"):
            print("  " + identity.InstanceID[len("LMI:LMI_SoftwareIdentity:"):])

.. note::
    This is not the same as running: ::

        yum list available

    which outputs all available, not installed packages. The example above
    yields available packages without any regard to their installation status.

.. seealso::
    :ref:`LMI_ResourceForSoftwareIdentity<LMI-ResourceForSoftwareIdentity>`

``lmi`` meta-command
~~~~~~~~~~~~~~~~~~~~
::

    lmi -h $HOST sw list --available pkgs

Listing files of package
------------------------
Let's list files of packages ``openlmi-tools``. Note that package must
be installed on system in order to list its files.

lmishell
~~~~~~~~
We need to know exact *NEVRA* [1]_ of package we want to operate on. If
we don't know it, we can find out using
:ref:`FindIdentity()<LMI-SoftwareInstallationService-FindIdentity>` method.
See example under `Searching for packages`_. ::

    c = connect("host", "user", "pass")
    identity = c.root.cimv2.LMI_SoftwareIdentity.new_instance_name(
            {"InstanceID" : "LMI:LMI_SoftwareIdentity:openlmi-tools-0:0.5-2.fc18.noarch"})
    for filecheck in identity.to_instance().associator_names(
            AssocClass="LMI_SoftwareIdentityChecks",
            Role="Element",
            ResultRole="Check",
            ResultClass="LMI_SoftwareIdentityFileCheck"):
        print("%s" % filecheck.Name)

.. seealso::
    :ref:`LMI_SoftwareIdentityFileCheck<LMI-SoftwareIdentityFileCheck>`

``lmi`` meta-command
~~~~~~~~~~~~~~~~~~~~
::

    lmi -h $HOST sw list files openlmi-tools

Searching for packages
----------------------
If we know just a fraction of informations needed to identify a package,
we may query package database in the following way.

``lmishell``
~~~~~~~~~~~~
::

    c = connect("host", "user", "pass")
    service = c.root.cimv2.LMI_SoftwareInstallationService.first_instance()
    # let's find all packages with "openlmi" in Name or Summary without
    # architecture specific code
    ret = service.FindIdentity(Name="openlmi", Architecture="noarch")
    for identity in ret.rparams["Matches"]:
        # we've got only references to instances
        print identity.Name[len("LMI:LMI_SoftwareIdentity:"):]

.. seealso::
    :ref:`FindIdentity()<LMI-SoftwareInstallationService-FindIdentity>` method

Please don't use this method to get an instance of package you know
precisely. If you know all the identification details, you may just
construct the instance name this way: ::

    c = connect("host", "user", "pass")
    iname = c.root.cimv2.LMI_SoftwareIdentity.new_instance_name(
            {"InstanceID" : "LMI:LMI_SoftwareIdentity:openlmi-software-0:0.1.1-2.fc20.noarch"})
    identity = iname.to_instance()

``lmi`` meta-command
~~~~~~~~~~~~~~~~~~~~
See help on ``sw`` command for more information on this. ::

    lmi -h $HOST sw list pkgs openlmi

.. _package_installation:

Package installation
--------------------
There are two approaches to package installation. One is synchronous
and the other asynchronous.

Synchronous installation
~~~~~~~~~~~~~~~~~~~~~~~~
This is a very simple and straightforward approach. We install package by
creating a new instance of
:ref:`LMI_InstalledSoftwareIdentity<LMI-InstalledSoftwareIdentity>`
with a reference to some available software identity. ::

    c = connect("host", "user", "pass")
    identity = c.root.cimv2.LMI_SoftwareIdentity.new_instance_name(
        {"InstanceID" : "LMI:LMI_SoftwareIdentity:sblim-sfcb-0:1.3.16-3.fc19.x86_64"})
    cs = c.root.cimv2.PG_ComputerSystem.first_instance_name()
    installed_assoc = c.root.cimv2.LMI_InstalledSoftwareIdentity.create_instance(
        properties={
                "InstalledSoftware" : identity,
                "System"            : cs
    })

If the package is already installed, this operation will fail with
the :py:class:`pywbem.CIMError` exception being raised initialized with
``CIM_ERR_ALREADY_EXISTS`` error code.

Asynchronous installation
~~~~~~~~~~~~~~~~~~~~~~~~~
Method
:ref:`InstallFromSoftwareIdentity()<LMI-SoftwareInstallationService-InstallFromSoftwareIdentity>`
needs to be invoked with desired options. After the options are checked
by provider, a job will be returned representing installation process running
at background. Please refer to `Asynchronous Jobs`_ for more details.

::

    c = connect("host", "user", "pass")
    service = c.root.cimv2.LMI_SoftwareInstallationService.first_instance()
    identity = c.root.cimv2.LMI_SoftwareIdentity.new_instance_name(
            {"InstanceID" : "LMI:LMI_SoftwareIdentity:sblim-sfcb-0:1.3.16-5.fc19.x86_64"})
    cs = c.root.cimv2.PG_ComputerSystem.first_instance_name()
    ret = service.InstallFromSoftwareIdentity(
            Source=identity,
            Target=cs,
            # these options request to install available, not installed package
            InstallOptions=[4]     # [Install]
            # this will force installation if package is already installed
            # (possibly in different version)
            #InstallOptions=[4, 3] # [Install, Force installation]
    )

The result can be checked by polling resulting job for finished status: ::

    finished_statuses = {
          c.root.cimv2.CIM_ConcreteJob.JobState.Completed
        , c.root.cimv2.CIM_ConcreteJob.JobState.Exception
        , c.root.cimv2.CIM_ConcreteJob.JobState.Terminated
        }
    job = ret.rparams["Job"].to_instance()
    while job.JobStatus not in finished_statuses:
        # wait for job to complete
        time.sleep(1)
        job.refresh()
    print c.root.cimv2.LMI_SoftwareJob.JobStateValues.value_name(job.JobState)
    # get an associated job method result and check the return value
    print "result: %s" % job.first_associator(
            AssocClass='LMI_AssociatedSoftwareJobMethodResult').__ReturnValue
    # get installed software identity
    installed = job.first_associator(
            Role='AffectingElement',
            ResultRole='AffectedElement',
            AssocClass="LMI_AffectedSoftwareJobElement",
            ResultClass='LMI_SoftwareIdentity')
    print "installed %s at %s" % (installed.ElementName, installed.InstallDate)

You may also subscribe to indications related to
:ref:`LMI_SoftwareInstallationJob<LMI-SoftwareInstallationJob>` and listen for
events instead of the polling done above

As you can see, you may force the installation allowing for reinstallation
of already installed package. For more options please refer to the
documentation of this method.

Combined way
~~~~~~~~~~~~
We can combine both approaches by utilizing a feature of lmishell_. Method
above can be called in a synchronous way (from the perspective of script's
code). It's done like this: ::

    # note the use of "Sync" prefix
    ret = service.SyncInstallFromSoftwareIdentity(
            Source=identity,
            Target=cs,
            # these options request to install available, not installed package
            InstallOptions=[4]     # [Install]
            # this will force installation if package is already installed
            # (possibly in different version)
            #InstallOptions=[4, 3] # [Install, Force installation]
    )
    print "result: %s" % ret.rval

The value of
:ref:`LMI_SoftwareMethodResult<LMI-SoftwareMethodResult>` ``.__ReturnValue`` is
placed to the ``ret.rval`` attribute. Waiting for job's completion is taken care
of by lmishell_. But we lose the reference to the job itself and we can not
enumerate affected elements (that contain, among other things, installed
package).

Installation from URI
~~~~~~~~~~~~~~~~~~~~~
This is also possible with: ::

    c = connect("host", "user", "pass")
    service = c.root.cimv2.LMI_SoftwareInstallationService.first_instance()
    cs = c.root.cimv2.PG_ComputerSystem.first_instance_name()
    ret = service.to_instance().InstallFromSoftwareURI(
            Source="http://someserver.com/fedora/repo/package.rpm",
            Target=cs,
            InstallOptions=[4])  # [Install]

Supported *URI* schemes are:

    * ``http``
    * ``https``
    * ``ftp``
    * ``file``

In the last cast, the file must be located on the remote system hosting
the *CIMOM*.


.. seealso::
    :ref:`InstallFromURI()<LMI-SoftwareInstallationService-InstallFromURI>`
    method

    Please refer to `Asynchronous installation`_ above for the consequent
    procedure and how to deal with ``ret`` value.

``lmi`` meta-command
~~~~~~~~~~~~~~~~~~~~
::

    lmi -h $HOST sw install sblim-sfcb

.. _package_removal:

Package removal
---------------
Again both asynchronous and synchronous approaches are available.

Synchronous removal
~~~~~~~~~~~~~~~~~~~
The aim is achieved by issuing an opposite operation than before. The instance
of :ref:`LMI_InstalledSoftwareIdentity<LMI-InstalledSoftwareIdentity>` is
deleted here. ::

    c = connect("host", "user", "pass")
    identity = c.root.cimv2.LMI_SoftwareIdentity.new_instance_name(
            {"InstanceID" : "LMI:LMI_SoftwareIdentity:sblim-sfcb-0:1.3.16-3.fc19.x86_64"})
    installed_assocs = identity.to_instance().reference_names(
            Role="InstalledSoftware",
            ResultClass="LMI_InstalledSoftwareIdentity")
    if len(installed_assocs) > 0:
        for assoc in installed_assocs:
            assoc.to_instance().delete()
            print("deleted %s" % assoc.InstalledSoftware.InstanceID)
    else:
        print("no package removed")

Asynchronous removal
~~~~~~~~~~~~~~~~~~~~
::

    c = connect("host", "user", "pass")
    service = c.root.cimv2.LMI_SoftwareInstallationService.first_instance()
    identity = c.root.cimv2.LMI_SoftwareIdentity.new_instance_name(
            {"InstanceID" : "LMI:LMI_SoftwareIdentity:sblim-sfcb-0:1.3.16-5.fc19.x86_64"})
    cs = c.root.cimv2.PG_ComputerSystem.first_instance_name()
    ret = service.InstallFromSoftwareIdentity(
            Source=identity,
            Target=cs,
            InstallOptions=[9])  # [Uninstall]

Again please refer to `Asynchronous installation`_ for examples on how to
deal with the ``ret`` value.

``lmi`` meta-command
~~~~~~~~~~~~~~~~~~~~
::

    lmi -h $HOST sw remove sblim-sfcb

.. _package_update:

Package update
--------------
Only asynchronous method is provided for this purpose. But with the possibility
of synchronous invocation.

``lmishell``
~~~~~~~~~~~~
Example below shows the synchronous invocation of asynchronous method. ::

    c = connect("host", "user", "pass")
    service = c.root.cimv2.LMI_SoftwareInstallationService.first_instance()
    identity = c.root.cimv2.LMI_SoftwareIdentity.new_instance_name(
            {"InstanceID" : "LMI:LMI_SoftwareIdentity:sblim-sfcb-0:1.3.16-5.fc19.x86_64"})
    cs = c.root.cimv2.PG_ComputerSystem.first_instance_name()
    ret = service.SyncInstallFromSoftwareIdentity(
            Source=identity,
            Target=cs,
            InstallOptions=[5]       # [Update]
            # to force update, when package is not installed
            #InstallOptions=[4, 5]   # [Install, Update]
    )
    print "installation " + ("successful" if rval == 0 else "failed")

``lmi`` meta-command
~~~~~~~~~~~~~~~~~~~~
::

    lmi -h $HOST sw update sblim-sfcb

.. _package_verification:

Package verification
--------------------
Installed *RPM* packages can be verified. Attributes of installed files
are compared with those stored in particular *RPM* package. If some value
of attribute does not match or the file does not exist, it fails the
verification test. Following attributes come into play in this process:

    * File size - in case of regular file
    * User ID
    * Group ID
    * Last modification time
    * Mode
    * Device numbers - in case of device file
    * Link Target - in case the file is a symbolic link
    * Checksum - in case of regular file

``lmishell``
~~~~~~~~~~~~
It's done via invocation of
:ref:`VerifyInstalledIdentity()<LMI-SoftwareInstallationService-VerifyInstalledIdentity>`.
This is an asynchronous method. We can not use synchronous invocation
if we want to be able to list failed files.

::

    c = connect("host", "user", "pass")
    service = c.root.cimv2.LMI_SoftwareInstallationService.first_instance()
    identity = c.root.cimv2.LMI_SoftwareIdentity.new_instance_name(
            {"InstanceID" : "LMI:LMI_SoftwareIdentity:sblim-sfcb-0:1.3.16-5.fc19.x86_64"})
    results = service.VerifyInstalledIdentity(
            Source=identity,
            Target=ns.PG_ComputerSystem.first_instance_name())
    nevra = (    identity.ElementName if isinstance(identity, LMIInstance)
            else identity.InstanceID[len('LMI:LMI_SoftwareIdentity:'):])
    if results.rval != 4096:
        msg = 'failed to verify identity "%s (rval=%d)"' % (nevra, results.rval)
        if results.errorstr:
            msg += ': ' + results.errorstr
        raise Exception(msg)

    job = results.rparams['Job'].to_instance()

    # wait by polling or listening for indication
    wait_for_job_finished(job)

    if not LMIJob.lmi_is_job_completed(job):
        msg = 'failed to verify package "%s"' % nevra
        if job.ErrorDescription:
            msg += ': ' + job.ErrorDescription
        raise Exception(msg)

    # get the failed files
    failed = job.associators(
            AssocClass="LMI_AffectedSoftwareJobElement",
            Role='AffectingElement',
            ResultRole='AffectedElement',
            ResultClass='LMI_SoftwareIdentityFileCheck')
    for iname in failed:
        print iname.Name    # print their paths

Polling, as a way of waiting for job completion, has been already shown in the
example under `Asynchronous installation`_.

.. seealso::
    :ref:`LMI_SoftwareIdentityFileCheck<LMI-SoftwareIdentityFileCheck>`

``lmi`` meta-command
~~~~~~~~~~~~~~~~~~~~
::

    lmi -h $HOST sw verify sblim-sfcb

Enable and disable repository
-----------------------------

``lmishell``
~~~~~~~~~~~~
::

    c = connect("host", "user", "pass")
    repo = c.root.cimv2.LMI_SoftwareIdentityResource.first_instance_name(
            key="Name",
            value="fedora-updates-testing")
    # disable repository
    repo.to_instance().RequestStateChange(
        RequestedState=c.root.cimv2.LMI_SoftwareIdentityResource. \
            RequestedStateValues.Disabled)
    repo = c.root.cimv2.LMI_SoftwareIdentityResource.first_instance_name(
            key="Name",
            value="fedora-updates")
    # enable repository
    repo.to_instance().RequestStateChange(
        RequestedState=c.root.cimv2.LMI_SoftwareIdentityResource. \
            RequestedStateValues.Enabled)

``lmi`` meta-command
~~~~~~~~~~~~~~~~~~~~
::

    lmi -h $HOST sw disable fedora-updates-testing
    lmi -h $HOST sw enable fedora-updates


Supported event filters
-----------------------
There are various events related to asynchronous job you may be interested
about. All of them can be subscribed to with static filters presented below.
Usage of custom query strings is not supported due to a complexity of
its parsing. These filters should be already registered in *CIMOM* if
*OpenLMI Software* providers are installed. You may check them by enumerating
``LMI_IndicationFilter`` class located in ``root/interop`` namespace.
All of them apply to two different software job classes you may want to
subscribe to:

    :ref:`LMI_SoftwareInstallationJob<LMI-SoftwareInstallationJob>`
        Represents a job requesting to install, update or remove some package.

    :ref:`LMI_SoftwareVerificationJob<LMI-SoftwareVerificationJob>`
        Represents a job requesting verification of installed package.

Filters below are written for :ref:`LMI_SoftwareInstallationJob<LMI-SoftwareInstallationJob>` only. If you deal with the other one, just replace the
class name right after the ``ISA`` operator and classname in filter's name.

Percent Updated
~~~~~~~~~~~~~~~
Indication is sent when the
:ref:`LMI_SoftwareJob.PercentComplete<LMI-ConcreteJob-PercentComplete>`
property of a job changes.

::

    SELECT * FROM LMI_SoftwareInstModification WHERE
        SourceInstance ISA LMI_SoftwareInstallationJob AND
        SourceInstance.CIM_ConcreteJob::PercentComplete <>
        PreviousInstance.CIM_ConcreteJob::PercentComplete

Registered under filter name
``"LMI:LMI_SoftwareInstallationJob:PercentUpdated"``.

Job state change
~~~~~~~~~~~~~~~~
Indication is sent when the
:ref:`LMI_SoftwareJob.JobState<LMI-ConcreteJob-JobState>`
property of a job changes.

::

    SELECT * FROM LMI_SoftwareInstModification WHERE
        SourceInstance ISA LMI_SoftwareInstallationJob AND
        SourceInstance.CIM_ConcreteJob::JobState <>
        PreviousInstance.CIM_ConcreteJob::JobState

Registered under filter name ``"LMI:LMI_SoftwareInstallationJob:Changed"``.

Job Completed
~~~~~~~~~~~~~
This event occurs when the state of job becomes ``COMPLETED/OK`` [2]_.

::

    SELECT * FROM LMI_SoftwareInstModification WHERE
        SourceInstance ISA LMI_SoftwareInstallationJob AND
        SourceInstance.CIM_ConcreteJob::JobState = 17

Registered under filter name ``"LMI:LMI_SoftwareInstallationJob:Succeeded"``.

Error
~~~~~
This event occurs when the state of job becomes ``COMPLETED/Error`` [3]_.

::

    SELECT * FROM LMI_SoftwareInstModification WHERE
        SourceInstance ISA LMI_SoftwareInstallationJob AND
        SourceInstance.CIM_ConcreteJob::JobState = 10

Registered under filter name ``"LMI:LMI_SoftwareInstallationJob:Failed"``.

New Job
~~~~~~~
This event occurs when the new instance of
:ref:`LMI_SoftwareJob<LMI-SoftwareJob>` is created.

::

    SELECT * FROM LMI_SoftwareInstCreation WHERE
         SourceInstance ISA LMI_SoftwareInstallationJob

Registered under filter name ``"LMI:LMI_SoftwareInstallationJob:Created"``.

------------------------------------------------------------------------------

.. [1] Stands for

    .. raw:: html

        <b>N</b>ame, <b>E</b>poch, <b>V</b>ersion, <b>R</b>elease,
        <b>A</b>rchitecure.

    .. raw:: latex

        \textbf{N}ame, \textbf{E}poch, \textbf{V}ersion, \textbf{R}elease,
        \textbf{A}rchitecture.

    .. only:: not html and not latex

            Name, Epoch, Version, Release, Architecure.

    Please refer to :ref:`identifying_software_identity` for more details.

.. [2] This is a composition of values in
       :ref:`OperationalStatus<LMI-ConcreteJob-OperationalStatus>` array.
       It corresponds to value ``Completed`` of
       :ref:`JobState<LMI-ConcreteJob-JobState>` property.

.. [3] This is a composition of values in
       :ref:`OperationalStatus<LMI-ConcreteJob-OperationalStatus>` array.
       It corresponds to value ``Exception`` of
       :ref:`JobState<LMI-ConcreteJob-JobState>` property.


.. *****************************************************************************
.. _documentation: https://fedorahosted.org/openlmi/wiki/scripts
.. _lmishell:      https://fedorahosted.org/openlmi/wiki/shell
.. _`Asynchronous Jobs`:    http://jsafrane.fedorapeople.org/openlmi-storage/api/0.6.0/concept-job.html#asynchronous-jobs
