Instances
=========
Each :py:class:`.LMIInstance` in LMIShell represents a CIM instance provided by
a certain provider.

Operations that can be performed within a :py:class:`.LMIInstance`:

* get and set properties
* list/print/execute its methods
* print a documentation string
* get a list of associated objects
* get a list of association objects
* push (update) a modified object to CIMOM
* delete a single instance from the CIMOM.

.. _instances_methods:

Instance Methods
----------------
To get a list of methods, run following:

.. code-block:: python

    > instance.print_methods()
    ...
    > method_lst = instance.methods()
    >

To execute a method within an object, run this:

.. code-block:: python

    > instance.Method(
    ...    {"Param1" : value1,
    ...     "Param2" : value2, ...})
    LMIReturnValue(
        rval=ReturnValue,
        rparams=ReturnParametersDictionary,
        errorstr="Possible error string"
    )
    >

**NOTE:** Instances **do not** auto-refresh after a method calls. It is
necessary to perform this operation by hand (See :ref:`instances_refreshing`).

To get the result from a method call, see following:

.. code-block:: python

    > rval, rparams, errorstr = instance.Method(
    ...    {"Param1" : value1,
    ...     "Param2" : value2, ...})
    >

The tuple in the previous example will contain return value of the method call
(``rval``), returned parameters (``rparams``) and possible error string
(``errorstr``).

.. _instance_sync_methods:

Synchronous methods
^^^^^^^^^^^^^^^^^^^
LMIShell can perform synchronous method call, which means, that the LMIShell is
able to synchronously wait for a Job object to change its state to `Finished`
state and then return the job's return parameters.

Most of the implemented methods in OpenLMI providers are *asynchronous*
methods, which means that user can execute such method and do other desired
actions while waiting for the result(s).

LMIShell can perform the synchronous method call, if the given method returns a
object of following classes:

* :py:class:`LMI_SELinuxJob`
* :py:class:`LMI_StorageJob`
* :py:class:`LMI_SoftwareInstallationJob`
* :py:class:`LMI_SoftwareVerificationJob`
* :py:class:`LMI_NetworkJob`

LMIShell first tries to use indications as the waiting method. If it fails,
then it uses polling method instead.

Following example illustrates, how to perform a synchronous method call:

.. code-block:: python

    > rval, rparams, errorstr = instance.SyncMethod(
    ...    {"Param1" : value1,
    ...     "Param2" : value2, ...})
    >

**NOTE:** See the prefix `Sync` of a method name.

When a synchronous method call is done:

* ``rval`` will contain the job's return value
* ``rparams`` will contain the job's return parameters
* ``errorstr`` will contain job's possible error string

It is possible to force LMIShell to use only polling method, see the next
example:

.. code-block:: python

    > rval, rparams, errorstr = instance.SyncMethod(
    ...    {"Param1" : value1,
    ...     "Param2" : value2, ...},
    ...    PreferPolling=True)
    >

Signal handling
"""""""""""""""
LMIShell can properly handle *SIGINT* and *SIGTERM*, which instruct the shell
to cancel the synchronous call. When such signal is received, the background
job, for which the LMIShell is waiting, will be asked to terminate, as well.

.. _instances_properties:

Instance Properties
-------------------
To get a list of properties, see following:

.. code-block:: python

   > instance.print_properties()
   ...
   > instance_prop_lst = instance.properties()
   >

It is possible to access an instance object properties. To get a property, see the
following example:

.. code-block:: python

    > instance.Property
    PropertyValue
    >

To modify a property, execute following:

.. code-block:: python

    > instance.Property = NewPropertyValue
    > instance.push()
    LMIReturnValue(rval=0, rparams={}, errorstr="")
    >

**NOTE:** If you change an instance object property, you have to execute a
:py:meth:`.LMIInstance.push` method to propagate the change to the CIMOM.

ValueMap Parameters
-------------------
A CIM Method may contain *ValueMap* parameters (aliases for constant values) in
its *MOF* definition.

To access these parameters, which contain constant values, see following code:

.. code-block:: python

    > instance.Method.print_valuemap_parameters()
    ...
    > valuemap_parameters = instance.Method.valuemap_parameters()
    >

Get ValueMap parameter value
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
By using a *ValueMap* parameters, you can retrieve a constant value defined in
the *MOF* file for a specific method.

To get a list of all available constants, their values, use the following
code:

.. code-block:: python

    > instance.Method.ParameterValues.print_values()
    ...
    >

**NOTE:** The suffix *Values* provides a way, how to access *ValueMap* parameters.

To retrieve a constant value, see the next example:

.. code-block:: python

    > constant_value_names_lst = instance.Method.ParameterValues.values()
    > instance.Method.ParameterValues.ConstantValueName
    ConstantValue
    > instance.Method.ParameterValues.value("ConstantValueName")
    ConstantValue
    >

Get ValueMap parameter
^^^^^^^^^^^^^^^^^^^^^^
Method can also contain a mapping between constant property name and
corresponding value. Following code demonstrates, how to access such
parameters:

.. code-block:: python

    > instance.Method.ConstantValueName
    >

Get ValueMap parameter value name
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
LMIShell can also return string representing constant value. See the following
code:

.. code-block:: python

    > instance.Method.ParameterValue.value_name(ConstantValue)
    ConstantValueName
    >

.. _instances_refreshing:

Instance refreshing
-------------------
Local objects used by LMIShell, which represent CIM objects at CIMOM side, can
get outdated, if such object changes while working with LMIShell's one.

To update object's properties, methods, etc. follow the next example:

.. code-block:: python

    > instance.refresh()
    LMIReturnValue(rval=True, rparams={}, errorstr="")
    >

.. _instances_delete:

Instance deletion
-----------------
A single instance can be removed from the CIMOM by executing:

.. code-block:: python

    > instance.delete()
    True
    >

**NOTE:** After executing the :py:meth:`.LMIInstance.delete` method, all the
object properties, methods will become inaccessible.

Deletion of the instance can be verified by:

.. code-block:: python

    > instance.is_deleted
    True
    >

Documentation
-------------
For an instance object, you can also use a documentation method, which will
display verbose information of its properties and values.

See next example:

.. code-block:: python

    > instance.doc()
    # ... pretty verbose output displayed in a pages (can be modified by
    #     setting environment variable PAGER) ...
    >

MOF representation
------------------
An instance object can also print out its *MOF* representation. This can be
achieved by running:

.. code-block:: python

    > instance.tomof()
    ... verbose output of the instance in MOF syntax ...
    >

Useful Properties
-----------------
Following part describes :py:class:`.LMIInstance` useful properties.

Class Name
^^^^^^^^^^
Each instance object provide a property, that returns its class name. To get a
string of the class name, run following:

.. code-block:: python

    > instance.classname
    ClassName
    >

Namespace
^^^^^^^^^
Each instance object also provides a property, that returns a namespace name.
To get a string of the namespace name, run following:

.. code-block:: python

    > instance.namespace
    Namespace
    >

Path
^^^^
To retrieve a unique, wrapped, identification object for the instance,
:py:class:`.LMIInstanceName`, execute following:

.. code-block:: python

    > instance.path
    LMIInstanceName(classname="ClassName"...)
    >

Connection Object
^^^^^^^^^^^^^^^^^
This property returns a connection object, which was used to retrieve the
instance (refer to :ref:`startup_connection`). See next example:

.. code-block:: python

   > instance.connection
   LMIConnection(URI='uri', user='user'...)
   >

Wrapped Object
^^^^^^^^^^^^^^
This property returns a wrapped :py:mod:`wbem` object. See the example:

.. code-block:: python

    > instance.wrapped_object
    CIMInstance(classname=u'ClassName', ...)
    >
