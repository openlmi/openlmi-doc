# Copyright (C) 2012-2014 Peter Hatina <phatina@redhat.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

from functools import wraps

from lmi.shell.compat import *

from lmi.shell.LMIReturnValue import LMIReturnValue
from lmi.shell.LMIUtil import lmi_wrap_cim_class
from lmi.shell.LMIUtil import lmi_raise_or_dump_exception

from lmi.shell.LMIExceptions import CIMError
from lmi.shell.LMIExceptions import ConnectionError
from lmi.shell.LMIExceptions import LMIDeletedObjectError


class lmi_return_expr_if_fail(object):
    """
    Decorator, which calls a specified expression and returns its return value
    instead of calling the decorated method, if provided test expression is
    False; otherwise a method is called.

    :param expr_test: expression which determines, if to execute a return value
        expression
    :param expr_ret: expression, which is called, if the ``expr_test`` returns
        False
    :param expr_ret_args: ``expr_ret`` position arguments
    :param expr_ret_kwargs: ``expr_ret`` keyword arguments
    :param bool Self: flag, which specifies, if to pass ``self`` variable to
        the ``expr_ret``, if ``expr_test`` failed

    Example of usage:

    .. code-block:: python

        class Foo:
            def __init__(self, member):
                self._member = member

            def failed(self):
                print "expression failed"
                return False

            # NOTE: the self parameter to the method call needs to be passed
            # via expr_ret_args, therefore, there is a dummy lambda obj: obj,
            # which is basically self variable.
            @lmi_return_expr_if_fail(lambda obj: obj._member, failed,
                                     lambda obj: obj)
            def some_method(self):
                print "some_method called"
                return True

        f = Foo(None)
        f.some_method() == False

        f = Foo(True)
        f.some_method() == True
    """
    def __init__(self, expr_test, expr_ret, Self=False, *expr_ret_args,
                 **expr_ret_kwargs):
        self._expr_test = expr_test
        self._expr_ret = expr_ret
        self._expr_ret_pass_self = Self
        self._expr_ret_args = expr_ret_args
        self._expr_ret_kwargs = expr_ret_kwargs

    def __call__(self, fn):
        """
        Executes a method call, if the test passed.

        :param instancemethod fn: decorated method
        """
        @wraps(fn)
        def wrapper(self_wr, *args, **kwargs):
            failed = False
            try:
                if not self._expr_test(self_wr):
                    failed = True
            except AttributeError, e:
                failed = True
            if failed:
                if self._expr_ret_pass_self:
                    return self._expr_ret(self_wr, *self._expr_ret_args,
                                          **self._expr_ret_kwargs)
                return self._expr_ret(*self._expr_ret_args,
                                      **self._expr_ret_kwargs)
            return fn(self_wr, *args, **kwargs)
        return wrapper


class lmi_return_val_if_fail(lmi_return_expr_if_fail):
    """
    Decorator, which returns a specified value and no method call is performed,
    if provided test expression is False; otherwise a method is called.

    :param expr_test: if the expression returns False, a method call is called
    :param rval: return value of the method, if the object attribute as
        expression failed

    Example of usage:

    .. code-block:: python

        class Foo:
            def __init__(self, member):
                self._member = member

            @lmi_return_val_if_fail(lambda obj: obj._member, False)
            def some_method(self):
                print "some_method called"
                return True

        f = Foo(None)
        f.some_method() == False

        f = Foo(True)
        f.some_method() == True
    """
    def __init__(self, expr_test, rval):
        lmi_return_expr_if_fail.__init__(self, expr_test, lambda: rval)


class lmi_return_if_fail(lmi_return_val_if_fail):
    """
    Decorator, which returns None and no method call is performed, if provided
    test expression is False; otherwise a method is called.

    :param expr_test: if the expression ``expr_test`` returns True, a method is
        called

    Example of usage:

    .. code-block:: python

        class Foo:
            def __init__(self, member):
                self._member = member

            @lmi_return_if_fail(lambda obj: obj._member)
            def some_method(self):
                print "some_method called"
                return True

        f = Foo(None)
        f.some_method() == None

        f = Foo(True)
        f.some_method() == True
    """
    def __init__(self, expr_test):
        lmi_return_val_if_fail.__init__(self, expr_test, None)


class lmi_possibly_deleted(lmi_return_expr_if_fail):
    """
    Decorator, which returns None, if provided test expression is True.

    :param expr_ret: callable or return value used, if ``expr_test`` fails
    :param expr_ret_args: expr_ret position arguments
    :param expr_ret_kwargs: expr_ret keyword arguments
    :param bool Self: flag, which specifies, if to pass ``self`` variable to
        the ``expr_ret``, if ``expr_test`` failed

    Example of usage:

    .. code-block:: python

        class Foo:
            def __init__(self, deleted):
                self._deleted = deleted

            @lmi_possibly_deleted(lambda obj: obj._member, lambda: False)
            def some_method(self):
                print "some_method called"
                return True

        f = Foo(None)
        f.some_method() == False

        f = Foo(True)
        f.some_method() == True
    """
    def __init__(self, expr_ret, Self=False, *expr_ret_args,
                 **expr_ret_kwargs):
        call_expr = expr_ret if callable(expr_ret) else lambda: expr_ret
        lmi_return_expr_if_fail.__init__(
            self, lambda obj: not obj._deleted, call_expr, Self=Self,
            *expr_ret_args, **expr_ret_kwargs)

    def __call__(self, fn):
        """
        Executes a method call, if the test passed. If the test expression
        returns False, specified return value in the constructor is returned.
        If the LMIShell does not dump exceptions, an appropriate exception is
        raised.

        :param instancemethod fn: decorated method
        :raises: :py:exc:`.LMIDeletedObjectError`
        """
        @wraps(fn)
        def wrapper(self_wr, *args, **kwargs):
            failed = False
            try:
                if not self._expr_test(self_wr):
                    failed = True
            except AttributeError, e:
                failed = True
            if failed:
                errorstr = "This instance has been deleted from a CIM broker"
                lmi_raise_or_dump_exception(LMIDeletedObjectError(errorstr))
                if self._expr_ret_pass_self:
                    return self._expr_ret(self_wr, *self._expr_ret_args,
                                          **self._expr_ret_kwargs)
                return self._expr_ret(*self._expr_ret_args,
                                      **self._expr_ret_kwargs)
            return fn(self_wr, *args, **kwargs)
        return wrapper


class lmi_class_fetch_lazy(object):
    """
    Decorator for :py:class:`.LMIClass`, which first fetches a wrapped
    :py:class:`wbem.CIMClass` object and then executes a wrapped method.

    :param bool full_fetch: True, if :py:class:`wbem.CIMClass` should include
        qualifiers and class origin. Default value is False.
    """
    def __init__(self, full_fetch=False):
        self._full_fetch = full_fetch

    def __call__(self, fn):
        """
        Fetches a :py:class:`wbem.CIMClass` if necessary and executes a wrapped
        method.

        :param instancemethod fn: decorated method
        """
        @wraps(fn)
        def wrapped(self_wr, *args, **kwargs):
            if not self_wr.is_fetched(self._full_fetch):
                self_wr.fetch(self._full_fetch)
            return fn(self_wr, *args, **kwargs)
        return wrapped

class lmi_instance_name_fetch_lazy(object):
    """
    Decorator for :py:class:`.LMIInstanceName`, which first fetches a wrapped
    :py:class:`wbem.CIMInstance` object and then executes a wrapped method.

    :param bool full_fetch: True, if :py:class:`wbem.CIMClass` should include
        qualifiers and class origin. Default value is False.
    """
    def __init__(self, full_fetch=False):
        self._full_fetch = full_fetch

    def __call__(self, fn):
        """
        Fetches a :py:class:`.LMIClass`, if necessary, and exeutes a wrapped
        method.

        :param instancemethod fn: decorated method
        """
        @wraps(fn)
        def wrapped(self_wr, *args, **kwargs):
            if self_wr._lmi_class is None:
                self_wr._lmi_class = lmi_wrap_cim_class(
                    self_wr._conn,
                    self_wr._cim_instance_name.classname,
                    self_wr._cim_instance_name.namespace)
                self_wr._lmi_class.fetch(self._full_fetch)
            return fn(self_wr, *args, **kwargs)
        return wrapped


class lmi_wrap_cim_exceptions(object):
    """
    Decorator used for CIM-XML exception wrapping.

    :param rval: rval passed to :py:meth:`.LMIReturnValue.__init__`
    :param error_callable: callable used for processing
        :py:exc:`wbem.CIMError` and :py:exc:`.ConnectionError`
    :param str prefix: string prefix for wrapped exception's args

    **NOTE:** callables need to take 2 arguments: return value and error
    string.
    """

    def __init__(self, rval=None, error_callable=None, prefix=""):
        self._rval = rval
        self._error_callable = self.default_error_callable \
            if error_callable is None else error_callable
        self._prefix = prefix

    def __call__(self, fn):
        """
        Execute a wrapped method.

        :param instancemethod fn: decorated method
        :raises: :py:exc:`.CIMError`, :py:exc:`.ConnectionError`
        """
        @wraps(fn)
        def wrapped(*args, **kwargs):
            try:
                rval = fn(*args, **kwargs)
            except wbem.CIMError, e:
                cim_error = self.make_cim_error(e)
                lmi_raise_or_dump_exception(cim_error)
                return self._error_callable(self._rval, cim_error)
            except wbem.ConnectionError, e:
                conn_error = self.make_connection_error(e)
                lmi_raise_or_dump_exception(conn_error)
                return self._error_callable(self._rval, conn_error)
            except wbem.AuthError, e:
                # PyWBEM's AuthError does not have HTTP error code in the
                # exception args. We add the code by hand.
                conn_error = ConnectionError(401, self.make_prefix() + "Unauthorized")
                lmi_raise_or_dump_exception(conn_error)
                return self._error_callable(self._rval, conn_error)
            return rval
        return wrapped

    @staticmethod
    def default_error_callable(rval, exc):
        """
        Default exception handler, which translates exception into
        :py:class:`.LMIReturnValue`.
        """
        errorstr = exc.args[1] if len(exc.args) > 1 else exc.args[0]
        return LMIReturnValue(rval=rval, errorstr=errorstr)

    def make_prefix(self):
        """
        Returns prefix string for a CIM exception.
        """
        if not self._prefix:
            return ""
        return self._prefix + ": "

    def make_exception_args(self, exc, prefix):
        """
        Returns a list of exception arguments. String argument is prefixed by
        :py:meth:`make_prefix`.
        """
        def prefix_arg(arg):
            if isinstance(arg, basestring):
                return self.make_prefix() + arg
            else:
                return arg

        return [prefix_arg(arg) for arg in exc.args]

    def make_cim_error(self, cim_error):
        """
        Returns wrapped CIMError from wbem.CIMError.
        """
        return CIMError(
            *self.make_exception_args(
                cim_error, self.make_prefix()))

    def make_connection_error(self, conn_error):
        """
        Returns wrapped ConnectionError from wbem.ConnectionError.
        """
        return ConnectionError(
            *self.make_exception_args(
                conn_error, self.make_prefix()))


class lmi_wrap_cim_exceptions_rval(lmi_wrap_cim_exceptions):
    """
    Decorator used for CIM-XML exception wrapping.

    :param rval: return value of a decorated method in case of exception
    """
    def __init__(self, rval=None, prefix=""):
        super(lmi_wrap_cim_exceptions_rval, self).__init__(
            rval, lambda r, e: r, prefix)
