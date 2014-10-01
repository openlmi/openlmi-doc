Interactive Interface
=====================
This section covers some features, that are present in the interactive
interface or are related to the LMIShell.

History
-------
When using the interactive interface of the LMIShell, you can use up/down
arrows to navigate in history of all the commands you previously used.

Clearing the history
^^^^^^^^^^^^^^^^^^^^
If you want to clear the history, simply run::

    > clear_history()
    >

Reversed search
^^^^^^^^^^^^^^^
The LMIShell can also search in the history of commands by hitting ``<ctrl+r>``
and typing the command prefix (as your default shell does). See following:

.. code-block:: python

    (reverse-i-search)'connect': c = connect("host", "username")

Exception handling
------------------
Exception handling by the shell can be turned off -- since then, all the
exceptions need to be handled by your code. By default, LMIShell **handles**
the exceptions and uses C-like return values (See section :doc:`return_values`)
To allow all the exceptions to propagate to your code, run this:

.. code-block:: python

    > use_exceptions()
    >

To turn exception handling by the shell back on, run this:

.. code-block:: python

    > use_exceptions(False)
    >

Cache
-----
The LMIShell's connection objects use a temporary cache for storing CIM class
names and CIM classes to save network communication.

The cache can be cleared, see following example:

.. code-block:: python

    > c.clear_cache()
    >

The cache can be also turned off, see next example:

.. code-block:: python

    > c.use_cache(False)
    >

Tab-completion
--------------
Interactive interface also supports tab-completion for basic programming
structures and also for CIM objects (such as namespace, classes, methods and
properties completion, etc).

Following code shows few examples:

.. code-block:: python

    > c = conn<tab>
    > c = connect(

    > lmi_service_class = c.root.c<tab>
    > lmi_service_class = c.root.cimv2
    > lmi_service_class = c.root.cimv2.lmi_ser<tab>
    > lmi_service_class = c.root.cimv2.LMI_Service

    > sshd_service = lmi_s<tab>
    > sshd_service = lmi_service_class

    > sshd_service.Stat<tab>
    > sshd_service.Status

    > sshd_service.Res<tab>
    > sshd_service.RestartService(

    > lmi_service_class.Req<tab>
    > lmi_service_class.RequestedStateChangeValues
    > lmi_service_class.RequestesStateChangeValues.Sh<tab>
    > lmi_service_class.RequestedStateChangeValues.Shutdown
    > # similar for method calls, as well
    >
