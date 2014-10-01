#pylint: disable-all
"""
A Python Singleton mixin class that makes use of some of the ideas
found at http://c2.com/cgi/wiki?PythonSingleton. Just inherit
from it and you have a singleton. No code is required in
subclasses to create singleton behavior -- inheritance from
Singleton is all that is needed.

Singleton creation is threadsafe.

USAGE:

Just inherit from Singleton. If you need a constructor, include
an __init__() method in your class as you usually would. However,
if your class is S, you instantiate the singleton using S.get_instance()
instead of S(). Repeated calls to S.get_instance() return the
originally-created instance.

For example:

class S(Singleton):

    def __init__(self, a, b=1):
        pass

S1 = S.get_instance(1, b=3)


Most of the time, that's all you need to know. However, there are some
other useful behaviors. Read on for a full description:

1) Getting the singleton:

    S.get_instance()

returns the instance of S. If none exists, it is created.

2) The usual idiom to construct an instance by calling the class, i.e.

    S()

is disabled for the sake of clarity.

For one thing, the S() syntax means instantiation, but get_instance()
usually does not cause instantiation. So the S() syntax would
be misleading.

Because of that, if S() were allowed, a programmer who didn't
happen to notice the inheritance from Singleton (or who
wasn't fully aware of what a Singleton pattern
does) might think he was creating a new instance,
which could lead to very unexpected behavior.

So, overall, it is felt that it is better to make things clearer
by requiring the call of a class method that is defined in
Singleton. An attempt to instantiate via S() will result
in a SingletonException being raised.

3) Use __S.__init__() for instantiation processing,
since S.get_instance() runs S.__init__(), passing it the args it has received.

If no data needs to be passed in at instantiation time,
you don't need S.__init__().

4) If S.__init__(.) requires parameters, include them ONLY in the
first call to S.get_instance(). If subsequent calls have arguments,
a SingletonException is raised by default.

If you find it more convenient for subsequent calls to be allowed to
have arguments, but for those argumentsto be ignored, just include
'ignoreSubsequent = True' in your class definition, i.e.:

  class S(Singleton):

      ignoreSubsequent = True

      def __init__(self, a, b=1):
          pass

5) For testing, it is sometimes convenient for all existing singleton
instances to be forgotten, so that new instantiations can occur. For that
reason, a _forget_all_singletons() function is included. Just call

  _forget_all_singletons()

and it is as if no earlier instantiations have occurred.

6) As an implementation detail, classes that inherit
from Singleton may not have their own __new__
methods. To make sure this requirement is followed,
an exception is raised if a Singleton subclass includ
es __new__. This happens at subclass instantiation
time (by means of the MetaSingleton metaclass.


By Gary Robinson, grobinson@flyfi.com. No rights reserved --
placed in the public domain -- which is only reasonable considering
how much it owes to other people's code and ideas which are in the
public domain. The idea of using a metaclass came from
a  comment on Gary's blog (see
http://www.garyrobinson.net/2004/03/python_singleto.html#comments).
Other improvements came from comments and email from other
people who saw it online. (See the blog post and comments
for further credits.)

Not guaranteed to be fit for any particular purpose. Use at your
own risk.
"""

import threading

class SingletonException(Exception):
    """
    Base exception related to singleton handling.
    """
    pass

_ST_SINGLETONS = set()
_LOCK_FOR_SINGLETONS = threading.RLock()
# Ensure only one instance of each Singleton class is created. This is not
# bound to the _LOCK_FOR_SINGLETON_CREATION = threading.RLock() individual
# Singleton class since we need to ensure that there is only one mutex for each
# Singleton class, which would require having a lock when setting up the
# Singleton class, which is what this is anyway.  So, when any Singleton is
# created, we lock this lock and then we don't need to lock it again for that
# class.
_LOCK_FOR_SINGLETON_CREATION = threading.RLock()

def _create_singleton_instance(cls, lst_args, dct_kw_args):
    """
    Creates singleton instance and stores its class in set.
    """
    _LOCK_FOR_SINGLETON_CREATION.acquire()
    try:
        if cls._is_instantiated(): # some other thread got here first
            return

        instance = cls.__new__(cls)
        try:
            instance.__init__(*lst_args, **dct_kw_args)
        except TypeError, exc:
            if '__init__() takes' in exc.message:
                raise SingletonException, (
                    'If the singleton requires __init__ args,'
                    ' supply them on first call to get_instance().')
            else:
                raise
        cls.c_instance = instance
        _add_singleton(cls)
    finally:
        _LOCK_FOR_SINGLETON_CREATION.release()

def _add_singleton(cls):
    """
    Adds class to singleton set.
    """
    _LOCK_FOR_SINGLETONS.acquire()
    try:
        assert cls not in _ST_SINGLETONS
        _ST_SINGLETONS.add(cls)
    finally:
        _LOCK_FOR_SINGLETONS.release()

def _remove_singleton(cls):
    """
    Removes class from singleton set.
    """
    _LOCK_FOR_SINGLETONS.acquire()
    try:
        if cls in _ST_SINGLETONS:
            _ST_SINGLETONS.remove(cls)
    finally:
        _LOCK_FOR_SINGLETONS.release()

def _forget_all_singletons():
    '''
    This is useful in tests, since it is hard to know which singletons need
    to be cleared to make a test work.
    '''
    _LOCK_FOR_SINGLETONS.acquire()
    try:
        for cls in _ST_SINGLETONS.copy():
            cls._forget_class_instance_reference_for_testing()

        # Might have created some Singletons in the process of tearing down.
        # Try one more time - there should be a limit to this.
        i_num_singletons = len(_ST_SINGLETONS)
        if len(_ST_SINGLETONS) > 0:
            for cls in _ST_SINGLETONS.copy():
                cls._forget_class_instance_reference_for_testing()
                i_num_singletons -= 1
                assert i_num_singletons == len(_ST_SINGLETONS), \
                        'Added a singleton while destroying ' + str(cls)
        assert len(_ST_SINGLETONS) == 0, _ST_SINGLETONS
    finally:
        _LOCK_FOR_SINGLETONS.release()

class MetaSingleton(type):
    """
    Metaclass for Singleton base class.
    """
    def __new__(mcs, str_name, tup_bases, dct):
        if dct.has_key('__new__'):
            raise SingletonException, 'Can not override __new__ in a Singleton'
        return super(MetaSingleton, mcs).__new__(
                mcs, str_name, tup_bases, dct)

    def __call__(cls, *lst_args, **dictArgs):
        raise SingletonException, \
                'Singletons may only be instantiated through get_instance()'

class Singleton(object):
    """
    Base class for all singletons.
    """
    __metaclass__ = MetaSingleton

    def get_instance(cls, *lst_args, **dct_kw_args):
        """
        Call this to instantiate an instance or retrieve the existing instance.
        If the singleton requires args to be instantiated, include them the first
        time you call get_instance.
        """
        if cls._is_instantiated():
            if (   (lst_args or dct_kw_args)
               and not hasattr(cls, 'ignoreSubsequent')):
                raise SingletonException, (
                        'Singleton already instantiated, but get_instance()'
                        ' called with args.')
        else:
            _create_singleton_instance(cls, lst_args, dct_kw_args)

        return cls.c_instance   #pylint: disable=E1101
    get_instance = classmethod(get_instance)

    def _is_instantiated(cls):
        """
        Don't use hasattr(cls, 'c_instance'), because that screws things
        up if there is a singleton that extends another singleton.
        hasattr looks in the base class if it doesn't find in subclass.
        """
        return 'c_instance' in cls.__dict__
    _is_instantiated = classmethod(_is_instantiated)

    # This can be handy for public use also
    isInstantiated = _is_instantiated

    def _forget_class_instance_reference_for_testing(cls):
        """
        This is designed for convenience in testing -- sometimes you
        want to get rid of a singleton during test code to see what
        happens when you call get_instance() under a new situation.

        To really delete the object, all external references to it
        also need to be deleted.
        """
        try:
            if hasattr(cls.c_instance, '_prepare_to_forget_singleton'):
                # tell instance to release anything it might be holding onto.
                cls.c_instance._prepare_to_forget_singleton()
            del cls.c_instance
            _remove_singleton(cls)
        except AttributeError:
            # run up the chain of base classes until we find the one that has
            # the instance and then delete it there
            for base_class in cls.__bases__:
                if issubclass(base_class, Singleton):
                    base_class._forget_class_instance_reference_for_testing()
    _forget_class_instance_reference_for_testing = classmethod(
        _forget_class_instance_reference_for_testing)


if __name__ == '__main__':

    from lmi.test import unittest
    import time

    class SingletonMixinPublicTestCase(unittest.TestCase):
        """
        TestCase for singleton class.
        """
        def testReturnsSameObject(self):    #pylint: disable=C0103
            """
            Demonstrates normal use -- just call get_instance and it returns a singleton instance
            """

            class Foo(Singleton):
                """Singleton child class."""
                def __init__(self):
                    super(Foo, self).__init__()

            a1 = Foo.get_instance()
            a2 = Foo.get_instance()
            self.assertEquals(id(a1), id(a2))

        def testInstantiateWithMultiArgConstructor(self):#pylint: disable=C0103
            """
            If the singleton needs args to construct, include them in the first
            call to get instances.
            """

            class Bar(Singleton):
                """Singleton child class."""

                def __init__(self, arg1, arg2):
                    super(Bar, self).__init__()
                    self.arg1 = arg1
                    self.arg2 = arg2

            b1 = Bar.get_instance('arg1 value', 'arg2 value')
            b2 = Bar.get_instance()
            self.assertEquals(b1.arg1, 'arg1 value')
            self.assertEquals(b1.arg2, 'arg2 value')
            self.assertEquals(id(b1), id(b2))

        def testInstantiateWithKeywordArg(self):
            """
            Test instantiation with keyword arguments.
            """

            class Baz(Singleton):
                """Singleton child class."""
                def __init__(self, arg1=5):
                    super(Baz, self).__init__()
                    self.arg1 = arg1

            b1 = Baz.get_instance('arg1 value')
            b2 = Baz.get_instance()
            self.assertEquals(b1.arg1, 'arg1 value')
            self.assertEquals(id(b1), id(b2))

        def testTryToInstantiateWithoutNeededArgs(self):
            """
            This tests, improper instantiation.
            """

            class Foo(Singleton):
                """Singleton child class."""
                def __init__(self, arg1, arg2):
                    super(Foo, self).__init__()
                    self.arg1 = arg1
                    self.arg2 = arg2

            self.assertRaises(SingletonException, Foo.get_instance)

        def testPassTypeErrorIfAllArgsThere(self):
            """
            Make sure the test for capturing missing args doesn't interfere
            with a normal TypeError.
            """
            class Bar(Singleton):
                """Singleton child class."""
                def __init__(self, arg1, arg2):
                    super(Bar, self).__init__()
                    self.arg1 = arg1
                    self.arg2 = arg2
                    raise TypeError, 'some type error'

            self.assertRaises(TypeError, Bar.get_instance, 1, 2)

        def testTryToInstantiateWithoutGetInstance(self):
            """
            Demonstrates that singletons can ONLY be instantiated through
            get_instance, as long as they call Singleton.__init__ during
            construction.

            If this check is not required, you don't need to call
            Singleton.__init__().
            """

            class A(Singleton):
                def __init__(self):
                    super(A, self).__init__()

            self.assertRaises(SingletonException, A)

        def testDontAllowNew(self):

            def instantiatedAnIllegalClass():
                class A(Singleton):
                    def __init__(self):
                        super(A, self).__init__()

                    def __new__(metaclass, str_name, tup_bases, dct):
                        return super(MetaSingleton, metaclass).__new__(
                                metaclass, str_name, tup_bases, dct)

            self.assertRaises(SingletonException, instantiatedAnIllegalClass)


        def testDontAllowArgsAfterConstruction(self):
            class B(Singleton):

                def __init__(self, arg1, arg2):
                    super(B, self).__init__()
                    self.arg1 = arg1
                    self.arg2 = arg2

            B.get_instance('arg1 value', 'arg2 value')
            self.assertRaises(SingletonException, B, 'arg1 value', 'arg2 value')

        def test_forgetClassInstanceReferenceForTesting(self):
            class A(Singleton):
                def __init__(self):
                    super(A, self).__init__()
            class B(A):
                def __init__(self):
                    super(B, self).__init__()

            # check that changing the class after forgetting the instance
            # produces an instance of the new class
            a = A.get_instance()
            assert a.__class__.__name__ == 'A'
            A._forget_class_instance_reference_for_testing()
            b = B.get_instance()
            assert b.__class__.__name__ == 'B'

            # check that invoking the 'forget' on a subclass still deletes
            # the instance
            B._forget_class_instance_reference_for_testing()
            a = A.get_instance()
            B._forget_class_instance_reference_for_testing()
            b = B.get_instance()
            assert b.__class__.__name__ == 'B'

        def test_forgetAllSingletons(self):
            # Should work if there are no singletons
            _forget_all_singletons()

            class A(Singleton):
                ciInitCount = 0
                def __init__(self):
                    super(A, self).__init__()
                    A.ciInitCount += 1

            A.get_instance()
            self.assertEqual(A.ciInitCount, 1)

            A.get_instance()
            self.assertEqual(A.ciInitCount, 1)

            _forget_all_singletons()
            A.get_instance()
            self.assertEqual(A.ciInitCount, 2)

        def test_threadedCreation(self):
            # Check that only one Singleton is created even if multiple threads
            # try at the same time. If fails, would see assert in _add_singleton
            class Test_Singleton(Singleton):
                def __init__(self):
                    super(Test_Singleton, self).__init__()

            class Test_SingletonThread(threading.Thread):
                def __init__(self, fTargetTime):
                    super(Test_SingletonThread, self).__init__()
                    self._fTargetTime = fTargetTime
                    self._eException = None

                def run(self):
                    try:
                        fSleepTime =  self._fTargetTime - time.time()
                        if fSleepTime > 0:
                            time.sleep(fSleepTime)
                        Test_Singleton.get_instance()
                    except Exception, exc:
                        self._eException = exc

            fTargetTime = time.time() + 0.1
            lstThreads = []
            for _ in xrange(100):
                t = Test_SingletonThread(fTargetTime)
                t.start()
                lstThreads.append(t)
            eException = None
            for t in lstThreads:
                t.join()
                if t._eException and not eException:
                    eException = t._eException
            if eException:
                raise eException

        def testNoInit(self):
            """
            Demonstrates use with a class not defining __init__
            """

            class A(Singleton):
                pass

                #INTENTIONALLY UNDEFINED:
                #def __init__(self):
                #    super(A, self).__init__()

            A.get_instance() #Make sure no exception is raised

        def testMultipleGetInstancesWithArgs(self):

            class A(Singleton):

                ignoreSubsequent = True

                def __init__(self, a, b=1):
                    pass

            a1 = A.get_instance(1)
            # ignores the second call because of ignoreSubsequent
            a2 = A.get_instance(2)

            class B(Singleton):

                def __init__(self, a, b=1):
                    pass

            b1 = B.get_instance(1)
            # No ignoreSubsequent included
            self.assertRaises(SingletonException, B.get_instance, 2)

            class C(Singleton):

                def __init__(self, a=1):
                    pass

            c1 = C.get_instance(a=1)
            # No ignoreSubsequent included
            self.assertRaises(SingletonException, C.get_instance, a=2)

        def testInheritance(self):
            """
            It's sometimes said that you can't subclass a singleton (see, for instance,
            http://steve.yegge.googlepages.com/singleton-considered-stupid point e). This
            test shows that at least rudimentary subclassing works fine for us.
            """

            class A(Singleton):

                def set_x(self, x):
                    self.x = x

                def setZ(self, z):
                    raise NotImplementedError

            class B(A):

                def set_x(self, x):
                    self.x = -x

                def set_y(self, y):
                    self.y = y

            a = A.get_instance()
            a.set_x(5)
            b = B.get_instance()
            b.set_x(5)
            b.set_y(50)
            self.assertEqual((a.x, b.x, b.y), (5, -5, 50))
            self.assertRaises(AttributeError, eval, 'a.set_y', {}, locals())
            self.assertRaises(NotImplementedError, b.setZ, 500)

    unittest.main()

