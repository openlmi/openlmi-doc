Classes
=======
Each :py:class:`.LMIClass` in LMIShell represents a class implemented by a
certain provider. You can get a list of its properties, methods, instances,
instance names and ValueMap properties. It is also possible to print a
documentation string, create a new instance or new instance name.

Getting a class object
----------------------
To get a class which is provided by a broker, you can do following:

.. code-block:: python

    > cls = c.root.cimv2.ClassName
    >

.. _class_fetching_a_class:

Fetching a class
----------------
Objects of :py:class:`.LMIClass` use lazy fetching method, because some methods
do not need the :py:class:`wbem.CIMClass` object.

To manually fetch the :py:class:`wbem.CIMClass` object, call following:

.. code-block:: python

    > cls.fetch()
    >

The methods, which need the :py:class:`wbem.CIMClass` object to be fetched
from CIMOM, do this action automatically, without the need of calling
:py:meth:`.LMIClass.fetch` method by hand.

.. _class_methods:

Class Methods
-------------
Following example illustrates, how to work with :py:class:`.LMIClass` methods:

.. code-block:: python

    > cls.print_methods()
    ...
    > cls_method_lst = cls.methods()
    >

.. _class_properties:

Class Properties
----------------
To get a list of properties of a specific class, run following code:

.. code-block:: python

    > cls.print_properties()
    ...
    > cls_property_lst = cls.properties()
    >

.. _class_instances:

Instances
---------
Following part described basic work flow with :py:class:`.LMIInstance` and
:py:class:`.LMIInstanceName` objects.

.. _class_get_instances:

Get Instances
^^^^^^^^^^^^^
Using a class object, you can access its instances. You can easily get a list
of (filtered) instances, or the first one from the list. The filtering is uses
input dictionary, if present, where the dictionary keys represent the instance
properties and the dictionary values represent your desired instance property
values.

To get :py:class:`.LMIInstance` object, execute the following example:

.. code-block:: python

    > inst = cls.first_instance()
    > inst_lst = cls.instances()
    >

.. _class_get_instance_names:

Get Instance Names
^^^^^^^^^^^^^^^^^^
The :py:class:`wbem.CIMInstanceName` objects clearly identify
:py:class:`wbem.CIMInstance` objects. LMIShell can retrieve
:py:class:`.LMIInstanceName` objects, by calling following:

.. code-block:: python

    > inst_name = cls.first_instance_name()
    > inst_names_lst = cls.instance_names()
    >

.. _class_instance_filtering:

Filtering
^^^^^^^^^
Both methods :py:meth:`.LMIClass.instances` or :py:meth:`.LMIClass.instance_names`
can filter returned objects by their keys/values. The filtering is achieved by
passing a dictionary of ``{property : value}`` to the corresponding method. See
following example:

.. code-block:: python

    > inst_lst = cls.instances({"FilterProperty" : FilterValue})
    > inst_names_lst = cls.instance_names({"FilterProperty" : FilterValue})
    >

.. _class_new_instance_name:

New Instance Name
^^^^^^^^^^^^^^^^^
LMIShell is able to create a new wrapped :py:class:`wbem.CIMInstanceName`, if
you know all the primary keys of a remote object. This instance name object can
be then used to retrieve the whole instance object.

See the next example:

.. code-block:: python

    > inst_name = cls({Property1 : Value1, Property2 : Value2, ...})
    > inst = inst_name.to_instance()
    >

.. _class_create_instance:

Creating a new instance
^^^^^^^^^^^^^^^^^^^^^^^
LMIShell is able to create an object of specific class, if the provider support
this operation.

See the following example:

.. code-block:: python

    > cls.create_instance({"Property1" : Value1, "Property2" : Value2})
    >

**NOTE:** ``Value`` can be a :py:class:`LMIInstance` object, as well. LMIShell
will auto-cast such object.

ValueMap Properties
-------------------
A CIM class may contain *ValueMap* properties (aliases for constant values) in
its MOF definition. These properties contain constant values, which can be
useful, when calling a method, or checking a returned value.

ValueMap properties are formed from 2 MOF properties of a class definition:

* *Values* -- list of string names of the "constant" values
* *ValueMap* -- list of values

.. _class_get_valuemap_properties:

Get ValueMap properties
^^^^^^^^^^^^^^^^^^^^^^^
To get a list of all available constants, their values, use the following
code:

.. code-block:: python

    > cls.print_valuemap_properties()
    ...
    > valuemap_properties = cls.valuemap_properties()
    ...
    > cls.PropertyValues.print_values()
    ...
    >

**NOTE:** The suffix "**Values**" provides a way, how to access ValueMap
properties.

.. _class_get_valuemap_property_value:

Get ValueMap property value
^^^^^^^^^^^^^^^^^^^^^^^^^^^
Following example shows, how to retrieve a constant value:

.. code-block:: python

    > constant_value_names_lst = cls.PropertyValues.values()
    > cls.PropertyValues.ConstantValueName
    ConstantValue
    > cls.PropertyValues.value("ConstantValueName")
    ConstantValue
    >

.. _class_get_valuemap_property_name:

Get ValueMap property value name
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
LMIShell can also return string representing constant value. See the following
code:

.. code-block:: python

    > cls.PropertyValue.value_name(ConstantValue)
    'ConstantValueName'
    >

Useful Properties
-----------------
Following part describes few useful :py:class:`.LMIClass` properties.

Class Name
^^^^^^^^^^
Every class object can return a name of the CIM class, see following:

.. code-block:: python

    > cls.classname
    ClassName
    >

Namespace
^^^^^^^^^
Every class belongs to certain namespace, to get a string containing the
corresponding namespace for each class, run following:

.. code-block:: python

    > cls.namespace
    Namespace
    >

Connection Object
^^^^^^^^^^^^^^^^^
This property returns a connection object, which was used to retrieve the
class (refer to :ref:`startup_connection`). See next example:

.. code-block:: python

   > cls.connection
   LMIConnection(URI='uri', user='user'...)
   >

Wrapped Object
^^^^^^^^^^^^^^
This property returns a wrapped :py:mod:`wbem` object. See the example:

.. code-block:: python

    > instance.wrapped_object
    CIMClass(u'ClassName', ...)
    >

Documentation
-------------
To see a class documentation (based on *MOF* definitions), run:

.. code-block:: python

    > cls.doc()
    # ... pretty verbose output displayed in a pages (can be modified by
    #     setting environment variable PAGER) ...
    >
