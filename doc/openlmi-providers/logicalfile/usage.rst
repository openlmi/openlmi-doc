.. _logicalfile-usage:

Usage
=====

There are two basic types of classes in the LogicalFile provider.

:ref:`CIM_LogicalFile <CIM-LogicalFile>` subclasses:

* :ref:`LMI_FIFOPipeFile <LMI-FIFOPipeFile>`
* :ref:`LMI_UnixDeviceFile <LMI-UnixDeviceFile>`
* :ref:`LMI_UnixDirectory <LMI-UnixDirectory>`
* :ref:`LMI_UnixSocket <LMI-UnixSocket>`
* :ref:`LMI_DataFile <LMI-DataFile>`
* :ref:`LMI_SymbolicLink <LMI-SymbolicLink>`

Subclasses derived from :ref:`CIM_LogicalFile <CIM-LogicalFile>` represent basic types of files and their
system independent properties, such as if the file is readable or its
modification time. The classes' names are self-explanatory. :ref:`LMI_SymbolicLink
<LMI-SymbolicLink>` represents symbolic link files, :ref:`LMI_UnixDeviceFile
<LMI-UnixDeviceFile>` represents unix device files, etc.

The other type of class is :ref:`LMI_UnixFile <LMI-UnixFile>`. It is used in the
Unix-like environment. Its properties are tied to the system -- Linux in our
case. For example, the group id of the owner or the inode number are among those
properties.

To provide ways to connect the file subclasses together, LogicalFile also
defines a few associations.

Association classes:

* :ref:`LMI_RootDirectory <LMI-RootDirectory>`
* :ref:`LMI_FileIdentity <LMI-FileIdentity>`
* :ref:`LMI_DirectoryContainsFile <LMI-DirectoryContainsFile>`

:ref:`LMI_RootDirectory <LMI-RootDirectory>` is used to connect the computer
system to its root directory.

:ref:`LMI_FileIdentity <LMI-FileIdentity>` associates the system-independent
:ref:`CIM_LogicalFile <CIM-LogicalFile>` subclasses to their respective
:ref:`LMI_UnixFile <LMI-UnixFile>` equivalents that are dependent on the
system.

:ref:`LMI_DirectoryContainsFile <LMI-DirectoryContainsFile>` serves as a tool to
show contents of a directory. Note that directory is usually just a type of
file.

Deviations from the schema
--------------------------

No classes that represent files have the ``EnumerateInstances`` method
implemented. The reason for this is that it would be very resource intensive to
list all the files on the given filesystem. Even more so, for example, all the
symlinks on the filesystem. For that reason, every LogicalFile class
implements only its ``GetInstance`` method.

The objectpath of the logical file classes consists of these properties:

* :ref:`CSCreationClassName <CIM-LogicalFile-CSCreationClassName>`
* :ref:`CSName <CIM-LogicalFile-CSName>`
* :ref:`FSCreationClassName <CIM-LogicalFile-FSCreationClassName>`
* :ref:`FSName <CIM-LogicalFile-FSName>`
* :ref:`CreationClassName <CIM-LogicalFile-CreationClassName>`
  (:ref:`LFCreationClassName <CIM-UnixFile-LFCreationClassName>` for
  :ref:`LMI_UnixFile <LMI-UnixFile>`)
* :ref:`Name <CIM-LogicalFile-Name>` (:ref:`LFName <CIM-UnixFile-LFName>` for
  :ref:`LMI_UnixFile <LMI-UnixFile>`)

When getting an instance, it's usually required that all of the key properties
are specified. However, it is impossible, or at least needlessly complicated, to
know some of them when querying remote machines. For example, if I want to see
information about the file '/home/user/myfile' on a remote computer, I don't
want to specify the filesystem it resides on or the type of the file.

Therefore, the only mandatory key properties are :ref:`CSCreationClassName
<CIM-LogicalFile-CSCreationClassName>`, :ref:`CSName <CIM-LogicalFile-CSName>`
and :ref:`Name <CIM-LogicalFile-Name>` (of :ref:`LFName <CIM-UnixFile-LFName>`
in case of :ref:`LMI_UnixFile <LMI-UnixFile>`). :ref:`FSName
<CIM-UnixFile-FSName>`, :ref:`FSCreationClassName
<CIM-LogicalFile-FSCreationClassName>` and :ref:`CreationClassName
<CIM-LogicalFile-CreationClassName>` are ignored. They are correctly filled in
after the instance has been properly returned.

To have an entry point into the Unix filesystems, an association has been
added. It binds the computer system and its root directory. See
:ref:`LMI_RootDirectory <LMI-RootDirectory>`.

:ref:`LMI_UnixFile <LMI-UnixFile>` has been extended to hold additional
properties. Currently, those are :ref:`SELinuxCurrentContext
<LMI-UnixFile-SELinuxCurrentContext>` and :ref:`SELinuxExpectedContext
<LMI-UnixFile-SELinuxExpectedContext>`. Should there be need for more
additions, this class can be easily extended.

Getting files
-------------
All further code assumes that a connection object has been created and the
default namespace (root/cimv2) is used. Also, the system's instance must have
been acquired.

::

   # plain http connections will likely be refused
   c = connect('https://myhost')
   # namespace alias for convenience
   ns = c.root.cimv2
   system = ns.PG_ComputerSystem.first_instance()

Get an instance of the home directory::

  name_dict =  {'CSCreationClassName':system.classname,
                'CSName':system.name,
                'CreationClassName':'ignored',
                'FSCreationClassName':'ignored',
                'FSName':'ignored',
                'Name':'/home/jsynacek'}
  name = ns.LMI_UnixDirectory.new_instance_name(name_dict)
  home = name.to_instance()
  print home.Name

Get an instance of a temporary file and see its selinux contexts using the
:ref:`LMI_FileIdentity <LMI-FileIdentity>`::

  name_dict =  {'CSCreationClassName':system.classname,
                'CSName':system.name,
                'LFCreationClassName':'ignored',
                'FSCreationClassName':'ignored',
                'FSName':'ignored',
                'LFName':'/var/tmp/data_file'}
  name = ns.LMI_UnixFile.new_instance_name(name_dict)
  unixdata = name.to_instance()
  data = unixdata.first_associator(AssocClass='LMI_FileIdentity')
  print unixdata.SELinuxCurrentContext
  print unixdata.SELinuxExpectedContext
  print data.Readable
  print data.Writeable
  print data.Executable

Get an instance of a symlink and check where it points to::

  name_dict =  {'CSCreationClassName':system.classname,
                'CSName':system.name,
                'LFCreationClassName':'ignored',
                'FSCreationClassName':'ignored',
                'FSName':'ignored',
                'LFName':'/home/jsynacek/test-link'}
  name = ns.LMI_UnixFile.new_instance_name(name_dict)
  unixsymlink = name.to_instance()
  symlink = unixsymlink.first_associator(AssocClass='LMI_FileIdentity')
  print symlink.TargetFile

Association classes examples
----------------------------

List a directory::

  files = home.associators(AssocClass='LMI_DirectoryContainsFile')
  for f in sorted(files, key=lambda x: x.Name):
      print f.Name


Get the root directory::

  root = system.first_associator(AssocClass='LMI_RootDirectory')
  print root.Name

.. note::

   For a more complex example of how to use the LogicalFile provider, please
   refer to the `OpenLMI LogicalFile script
   <https://github.com/openlmi/openlmi-scripts/tree/master/commands/logicalfile/lmi/scripts/logicalfile>`_.
