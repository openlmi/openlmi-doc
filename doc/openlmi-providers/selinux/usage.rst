.. _selinux-usage:

Usage
=====
All further code assumes that a connection object has been created and the
default namespace (root/cimv2) is used. Also, the LMI_SELinuxService instance
must have been acquired.

::

  c = connect("https://myhost", "user", "secret")
  service = c.root.cimv2.LMI_SELinuxService.first_instance()
  system = c.root.cimv2.PG_ComputerSystem.first_instance()

As a convenience helper function for further use, `lmi_unixfile_instance_name`
is defined. It provides an easy way to get file references for methods that
require an LMI_UnixFile reference as a parameter.

::

  def lmi_unixfile_instance_name(path):
      props = {"CSName":system.name,
               "CSCreationClassName":system.classname,
               "FSCreationClassName":"ignored",
               "FSName":"ignored",
               "LFCreationClassName":"ignored",
               "LFName":path}
      return c.root.cimv2.LMI_UnixFile.new_instance_name(props)

SELinux state
-------------

General information about SELinux is available via the `service` instance::

  def state_to_str(state):
      if state == 0: return "Disabled"
      elif state == 1: return "Permissive"
      elif state == 2: return "Enabled"
      else: return "Unknown"

  print "Policy version:   %s" % service.PolicyVersion
  print "Policy type:      %s" % service.PolicyType
  print "Current state:    %s" % state_to_str(service.SELinuxState)
  print "Persistent state: %s" % state_to_str(service.SELinuxDefaultState)

Set service state, for example, set the default (persistent) state to Enforcing::

  # 2 == Enforcing
  service.SetSELinuxState({"NewState":2,
                           "MakeDefault":True})


Booleans
--------
List all booleans and print their current and default values::

  booleans = c.root.cimv2.LMI_SELinuxBoolean.instances()
  for boolean in booleans:
      print "%-50s (%s, %s)" % (boolean.ElementName, boolean.State, boolean.DefaultState)

To enable the `httpd_use_sasl` boolean in the current runtime, but not permanently::

  target = c.root.cimv2.LMI_SELinuxBoolean.new_instance_name({"InstanceID":"LMI:LMI_SELinuxBoolean:httpd_use_sasl"})
  res = service.SetBoolean({"Target":target,
                            "Value":True,
                            "MakeDefault":False})

Ports
-----
List all ports::

  ports = c.root.cimv2.LMI_SELinuxPort.instances()
  for port in sorted(ports):
      print "%-30s %-10s %s" % (port.ElementName,
                                "tcp" if port.Protocol else "udp",
                                ", ".join(port.Ports))


Label the TCP port 8080 with `http_port_t`::

  target = c.root.cimv2.LMI_SELinuxPort.new_instance_name({"InstanceID":"LMI:LMI_SELinuxPort:TCP:http_port_t"})
  service.SetPortLabel({"Target":target,
                        "PortRange":"8080"})

It is also possible to specify `PortRange` as an actual range, for example "8080-8090".

File labels
-----------
To see what SELinux context a file holds, the `LogicalFile <http://www.openlmi.org/sites/default/files/doc/admin/openlmi-providers/latest/logicalfile/index.html>`_ provider is used::

  target = lmi_unixfile_instance_name("/tmp/file")
  file = target.to_instance()
  print file.SELinuxCurrentContext
  print file.SELinuxExpectedContext

Set a file context::

  target = lmi_unixfile_instance_name("/root")
  service.SetFileLabel({"Target":target,
                        "Label":"my_user_u:my_role_r:my_type_t"})

Restore SELinux contexts of all the files in `/etc/` recursively::

  # 1 == Restore
  target = lmi_unixfile_instance_name("/etc/")
  service.RestoreLabels({"Target":target,
                         "Action":1,
                         "Recursively":True})
