Instance Names
==============
:py:class:`.LMIInstanceName` is a object, which holds a set of primary keys and
their values. This type of object exactly identifies an instance.

.. _instance_names_key_properties:

Key properties
--------------
To get a list of key properties, see following example:

.. code-block:: python

    > instance_name.print_key_properties()
    ...
    > instance_name.key_properties()
    ...
    > instance_name.SomeKeyProperty
    ...
    >

.. _instance_names_delete:

Instance Names deletion
-----------------------
A single instance can be removed from the CIMOM by executing:

.. code-block:: python

    > instance_name.delete()
    True
    >

**NOTE:** After executing the :py:meth:`.LMIInstanceName.delete` method, all
the object key properties, methods will become inaccessible.

Deletion of the instance can be verified by:

.. code-block:: python

    > instance_name.is_deleted
    True
    >

.. _instance_names_conversion:

Conversion to a LMIInstance
---------------------------
This type of object may be returned from a method call. Each instance name can
be converted into the instance, see next example:

.. code-block:: python

    > instance = instance_name.to_instance()
    >

Useful Properties
-----------------

Following part describes :py:class:`.LMIInstanceName` useful properties.

Class Name
^^^^^^^^^^
The property returns a string representation of the class name. See next
example:

.. code-block:: python

    > instance_name.classname
    ClassName
    >

Namespace
^^^^^^^^^
The property returns a string representation of namesapce. See next example:

.. code-block:: python

   > instance_name.namespace
   Namespace
   >

Host Name
^^^^^^^^^
This property returns a string representation of the host name, where the CIM
instance is located.

.. code-block:: python

   > instance_name.hostname
   Hostname
   >

Connection Object
^^^^^^^^^^^^^^^^^
This property returns a connection object, which was used to retrieve the
instance name (refer to :ref:`startup_connection`). See next example:

.. code-block:: python

   > instance.connection
   LMIConnection(URI='uri', user='user'...)
   >

Wrapped Object
^^^^^^^^^^^^^^
This property returns a wrapped :py:mod:`lmiwbem` object. See the example:

.. code-block:: python

    > instance.wrapped_object
    CIMInstanceName(classname='ClassName', keybindings=NocaseDict(...), host='hostname', namespace='namespace')
    >
