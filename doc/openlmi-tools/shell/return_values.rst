Return Values
=============
Method calls return an object, that represents a return value of the given method. This
type of object can be converted into python's typical 3-item tuple and consists of 3
items:

* ``rval`` -- return value
* ``rparams`` -- return value parameters
* ``errorstr`` -- error string, if any

Following example shows, how to use and convert :py:class:`.LMIReturnValue` object to
tuple:

.. code-block:: python

    > return_value = instance.MethodCall()
    > return_value.rval
    0
    > return_value.rparams
    []
    > return_value.errorstr

    > (rval, rparams, errorstr) = return_value
    > rval
    0
    > rparams
    []
    > errorstr

    >
