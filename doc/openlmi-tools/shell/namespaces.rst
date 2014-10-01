.. _namespaces:

Namespaces
==========
Namespaces in CIM and LMIShell provide a natural way, how to organize all
the available classes and their instances. In the shell, they provide a
hierarchic access point to other namespaces and corresponding classes.

The *root* namespace plays a special role in the managed system; it is the
first entry point from the connection object and provides the access to other
clamped namespaces.

.. _namespaces_available_namespaces:

Available namespaces
--------------------
To get a :py:class:`.LMINamespace` object for the root namespace of the managed
system, run following:

.. code-block:: python

    > root_namespace = c.root
    >

To list all available namespace from the root one, run following code:

.. code-block:: python

    > c.root.print_namespaces()
    ...
    > ns_lst = c.root.namespaces
    >

If you want to access any namespace deeper (e.g. `cimv2`), run this:

.. code-block:: python

    > cimv2_namespace = c.root.cimv2
    > cimv2_namespace = c.get_namespace("root/cimv2")
    >

.. _namespaces_available_classes:

Available classes
-----------------
Each namespace object can print its available classes. To print/get the list of
the classes, run this:

.. code-block:: python

    > c.root.cimv2.print_classes()
    ...
    > classes_lst = c.root.cimv2.classes()
    >

.. _namespaces_queries:

Queries
-------
Using a :py:class:`.LMINamespace` object, it is possible to retrieve a list of
:py:class:`.LMIInstance` objects. The LMIShell supports 2 query languages:

* *WQL*
* *CQL*

Following code illustrates, how to execute *WQL* and *CQL* queries:

.. code-block:: python

   > instances_lst = namespace.wql("query")
   > instances_lst = namespace.cql("query")
   >
