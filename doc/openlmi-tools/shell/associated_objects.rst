Associated Objects
==================
An association from CIM perspective is a type of class that contains two or
more references. Associations represent relationships between two or more
classes.

Associations are classes which establish a relationship between classes without
affecting any of the related classes. In other words, the addition of an
association has no effect on any of the related classes.

Following text describes the means of retrieving associated objects within
a given one.

.. _associators_instances:

Associated Instances
--------------------
To get a list of associated :py:class:`.LMIInstance` objects with a given
object, run following:

.. code-block:: python

    > associated_objects = instance.associators(
    ...    AssocClass=cls,
    ...    ResultClass=cls,
    ...    ResultRole=role,
    ...    IncludeQualifiers=include_qualifiers,
    ...    IncludeClassOrigin=include_class_origin,
    ...    PropertyList=property_lst)
    > first_associated_object = instance.first_associator(
    ...    AssocClass=cls,
    ...    ResultClass=cls,
    ...    ResultRole=role,
    ...    IncludeQualifiers=include_qualifiers,
    ...    IncludeClassOrigin=include_class_origin,
    ...    PropertyList=property_lst))

.. only:: html

   **NOTE:** Refer to :py:meth:`.LMIInstance.associators` and
   :py:meth:`.LMIInstance.first_associator`.

.. only:: man

    The list of returned associated objects can be filtered by:

    * ``AssocClass`` -- Each returned object shall be associated to the source
      object through an instance of this class or one of its subclasses. Default
      value is `None`.

    * ``ResultClass`` -- Each returned object shall be either an instance of this
      class (or one of its subclasses) or be this class (or one of its subclasses).
      Default value is `None`.

    * ``Role`` -- Each returned object shall be associated with the source object
      through an association in which the source object plays the specified role.
      That is, the name of the property in the association class that refers to the
      source object shall match the value of this parameter. Default value is `None`.

    * ``ResultRole`` -- Each returned object shall be associated to the source
      object through an association in which the returned object plays the specified
      role. That is, the name of the property in the association class that refers to
      the returned object shall match the value of this parameter. Default value is
      `None`.

    Other parameters refer to:

    * ``IncludeQualifiers`` -- Bool flag indicating, if all qualifiers for each
      object (including qualifiers on the object and on any returned properties)
      shall be included as ``<QUALIFIER>`` elements in the response. Default value is
      `False`.

    * ``IncludeClassOrigin`` -- Bool flag indicating, if the CLASSORIGIN attribute
      shall be present on all appropriate elements in each returned object. Default
      value is `False`.

    * ``PropertyList`` -- The members of the array define one or more property
      names. Each returned object shall not include elements for any properties
      missing from this list. If PropertyList is an empty list, no properties are
      included in each returned object. If it is None, no additional filtering is
      defined. Default value is `None`.

.. _associators_instance_names:

Associated Instance Names
-------------------------
To get a list of associated :py:class:`.LMIInstanceName` objects with a given
object, run following:

.. code-block:: python

    > associated_object_names = instance.associator_names(
    ...    AssocClass=cls,
    ...    ResultClass=cls,
    ...    Role=role,
    ...    ResultRole=result_role)
    > first_associated_object_name = instance.first_associator_name(
    ...    AssocClass=cls,
    ...    ResultClass=cls,
    ...    Role=role,
    ...    ResultRole=result_role)
    >

.. only:: html

   **NOTE:** Refer to :py:meth:`.LMIInstance.associator_names` and
   :py:meth:`.LMIInstance.first_associator_name`.

.. only:: man

    The list of returned associated instance names can be filtered by:

    * ``AssocClass`` -- Each returned name identify an object that shall be
      associated to the source object through an instance of this class or one of its
      subclasses. Default value is `None`.

    * ``ResultClass`` -- Each returned name identify an object that shall be either
      an instance of this class (or one of its subclasses) or be this class (or one
      of its subclasses). Default value is `None`.

    * ``Role`` -- Each returned name identify an object that shall be associated to
      the source object through an association in which the source object plays the
      specified role. That is, the name of the property in the association class that
      refers to the source object shall match the value of this parameter. Default
      value is `None`.

    * ``ResultRole`` -- Each returned name identify an object that shall be
      associated to the source object through an association in which the named
      returned object plays the specified role. That is, the name of the property in
      the association class that refers to the returned object shall match the value
      of this parameter. Default value is `None`.
