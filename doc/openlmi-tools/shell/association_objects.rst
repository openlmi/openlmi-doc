Association Objects
===================
CIM defines an association relationship between managed objects. Following text
describes the means of retrieving association objects within a given one. An
association object is the object, which defines the relationship between two
other objects.

.. _references_instances:

Association Instances
---------------------
To get association :py:class:`.LMIInstance` objects that refer to a particular
target object, run following:

.. code-block:: python

    > association_objects = instance.references(
    ...    ResultClass=cls,
    ...    Role=role,
    ...    IncludeQualifiers=include_qualifiers,
    ...    IncludeClassOrigin=include_class_origin,
    ...    PropertyList=property_lst)
    > first_association_object = instance.first_reference(
    ...    ResultClass=cls,
    ...    Role=role,
    ...    IncludeQualifiers=include_qualifiers,
    ...    IncludeClassOrigin=include_class_origin,
    ...    PropertyList=property_lst)
    >

.. only:: html

   **NOTE:** Refer to :py:meth:`.LMIInstance.references` and
   :py:meth:`.LMIInstance.first_reference`

.. only:: man

    The list of returned association objects can be filtered by:

    * ``ResultClass`` -- Each returned object shall be an instance of this class
      (or one of its subclasses) or this class (or one of its subclasses). Default
      value is `None`.

    * ``Role`` -- Each returned object shall refer to the target object through a
      property with a name that matches the value of this parameter. Default value is
      `None`.

    Other parameters reffer to:

    * ``IncludeQualifiers`` -- Each object (including qualifiers on the object and
      on any returned properties) shall be included as ``<QUALIFIER>`` elements in the
      response. Default value is `False`.

    * ``IncludeClassOrigin`` -- Flag indicating, if the ``CLASSORIGIN`` attribute shall
      be present on all appropriate elements in each returned object. Default value
      is `False`.

    * ``PropertyList`` -- The members of the list define one or more property
      names. Each returned object shall not include elements for any properties
      missing from this list. If PropertyList is an empty list, no properties are
      included in each returned object. If PropertyList is None, no additional
      filtering is defined. Default value is `None`.

.. _references_instance_names:

Association Instance Names
--------------------------
To get a list of association :py:class:`.LMIInstanceName` objects, run
following:

.. code-block:: python

    > association_object_names = instance.reference_names(
    ...    ResultClass=cls,
    ...    Role=role)
    > first_association_object_name = instance.first_reference_name(
    ...    ResultClass=cls,
    ...    Role=role)
    >

.. only:: html

   **NOTE:** Refer to :py:meth:`.LMIInstance.reference_names` and
   :py:meth:`.LMIInstance.first_reference_name`.

.. only:: man

    The list of returned association instance names can be filtered by:

    * ``ResultClass`` -- Each returned Object Name identify an instance of this
      class (or one of its subclasses) or this class (or one of its subclasses).
      Default value is `None`.

    * ``Role`` -- Each returned object name shall identify an object that refers to
      the target instance through a property with a name that matches the value of
      this parameter. Default value is `None`.
