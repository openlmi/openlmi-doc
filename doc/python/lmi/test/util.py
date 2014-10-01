# Copyright (C) 2012-2014 Red Hat, Inc.  All rights reserved.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
#
# Authors: Michal Minar <miminar@redhat.com>
#
"""
LMI test utilities.
"""

import abc
import copy
import os
import hashlib
import random
import tempfile
import socket
import string
import subprocess
from collections import OrderedDict

from lmi.test import unittest
from lmi.test import wbem

def is_this_system(system_name):
    """
    :returns: Whether the given *system_name* matches the hostname of currently
    running system.
    :rtype: boolean
    """
    return (socket.gethostbyaddr(system_name)[0]
            == socket.gethostbyaddr(socket.gethostname())[0])


def get_environvar(variable, default='', convert=str):
    """
    Get the value of environment variable.

    :param string variable: Name of environment variable.
    :param default: Any value that should be returned when the variable is not
        set. If None, the conversion won't be done.
    :param callable convert: Function transforming value to something else.
    :returns: Converted value of the environment variable.
    """
    val = os.environ.get(variable, default)
    if convert is bool:
        return val.lower() in ('true', 'yes', 'on', '1')
    if val is None:
        return None
    return convert(val)


def mark_dangerous(method):
    """
    Decorator for methods of :py:class:`unittest.TestCase` subclasses that
    skips dangerous tests if an environment variable says so.
    ``LMI_RUN_DANGEROUS`` is the environment variabled read.

    These tests will be skipped by default.
    """
    if get_environvar('LMI_RUN_DANGEROUS', '0', bool):
        return method
    else:
        return unittest.skip("This test is marked as dangerous.")(method)


def mark_tedious(method):
    """
    Decorator for methods of :py:class:`unittest.TestCase` subclasses that
    skips tedious tests. Those running for very long time and usually need a
    lot of memory. They are run by default. Environment variable
    ``LMI_RUN_TEDIOUS`` can be used to skip them.
    """
    if get_environvar('LMI_RUN_TEDIOUS', '1', bool):
        return method
    else:
        return unittest.skip("This test is marked as tedious.")(method)


def check_inames_equal(fst, snd):
    """
    Compare two objects of :py:class:`lmiwbem.CIMInstanceName`. Their ``host``
    property is not checked. Be benevolent when checking names system
    creation class names.

    :returns: ``True`` if both instance names are equal.
    :rtype: boolean
    """

    def isa_CIMInstanceName(x):
        return isinstance(x, wbem.CIMInstanceName)

    def isa_cs(x):
        return x.classname.endswith('_ComputerSystem')

    def isa_basestring(x):
        return isinstance(x, basestring)

    def isa_str(x):
        return isinstance(x, str)

    def chkparam(x, n):
        if not isa_CIMInstanceName(x):
            msg = ("%s argument must be a lmiwbem.CIMInstanceName, not %s.%s"
                   % (n, type(x).__module__, type(x).__name__))
            raise TypeError(msg)

    def decode_utf8_if_str(x):
        return x.decode('utf-8') if isa_str(x) else x

    chkparam(fst, "fst")
    chkparam(snd, "snd")

    if fst.classname != snd.classname or fst.namespace != snd.namespace:
        return False

    snd_keys = dict((k, v) for (k, v) in snd.keybindings.iteritems())
    for key, value in fst.keybindings.iteritems():
        if key not in snd_keys:
            return False
        snd_value = snd_keys.pop(key)
        if isa_CIMInstanceName(value) and isa_CIMInstanceName(snd_value):
            if not check_inames_equal(value, snd_value):
                return False

        # accept also aliases in the Name attribute of ComputerSystem
        elif ((isa_cs(fst) and key.lower() == 'name')
              or (key.lower() == 'systemname'
                  and 'SystemCreationClassName' in fst)
              ):
            if (value != snd_value
                and (not is_this_system(value)
                     or not is_this_system(snd_value))):
                return False

        elif (isa_cs(fst) and key.lower() == 'creationclassname'):
            if (value != snd_value
                and 'CIM_ComputerSystem' not in [
                    p['CreationClassName'] for p in (fst, snd)]):
                return False

        elif isa_basestring(value) and isa_basestring(snd_value):
            value = decode_utf8_if_str(value)
            snd_value = decode_utf8_if_str(snd_value)
            if value != snd_value:
                return False

        elif value != snd_value:
            return False

    if snd_keys:    # second path has more key properties than first one
        return False

    return True


def random_string(strength=6, chars=None, prefix=""):
    """
    Generate a random string, e.g. usable as UID/GID

    strength is count of random characters in the final string.  chars
    is sequence of characters to choose from, and prefix can be provided
    to prepend it to final string.
    """
    if chars is None:
        chars = string.ascii_uppercase + string.digits
    salt = ''.join([random.choice(chars) for x in range(strength)])
    return prefix + salt


class BackupStorage():
    """
    Simple file backup storage.

    * Only supports files.
    * Only supports absolute paths.
    * Consecutive backups rewrite each other.
    * Does not autodestroy the backup.
    """

    def __init__(self):
        self.root = tempfile.mkdtemp(prefix=self.__class__.__name__ + ".")
        self.backups = OrderedDict()
        subprocess.check_call(["mkdir", "-p", self.root])

    def _copy(self, src, dest):
        """
        Copy src to dst --- force, keep meta, no questions asked
        """
        subprocess.check_call(["cp", "-a", "-f", src, dest])

    def _get_bpath(self, path):
        """
        Take original path and return path to backup.
        """
        if not path.startswith("/"):
            raise ValueError("only absolute paths are supported")
        digest = hashlib.sha1(path).hexdigest()
        return self.root + "/" + digest

    def _update_index(self):
        """
        Create/update an index file to help in case of backup investigation

        For convenience, index file is sorted by real path.
        """
        paths = sorted(self.backups.keys())
        with open(self.root + "/index", "w+") as fh:
            for path in paths:
                fh.write("%s %s\n" % (self.backups[path], path))

    def add_files(self, paths):
        """
        Add list of tiles to backup storage
        """
        for path in paths:
            self.add_file(path)

    def add_file(self, path):
        """
        Add a file to backup storage
        """
        bpath = self._get_bpath(path)
        self._copy(path, bpath)
        self.backups[path] = bpath
        self._update_index()

    def restore(self, path):
        """
        Restore particular path
        """
        try:
            self._copy(self.backups[path], path)
        except KeyError:
            raise ValueError("path not stored: %s" % path)

    def restore_all(self):
        """
        Restore all stored paths in same order as they were stored
        """
        for key in self.backups.keys():
            self.restore(key)

    def destroy_backup(self):
        """
        Destroy the temporary backup
        """
        subprocess.call(["rm", "-rf", self.root])


class BaseCrippler:
    """
    Helper class for crippling system files.

    To use the class, you need to sub-class it and implement
    _define_cases method.
    """

    LINE_LENGTH = 500
    LINE_COUNT = 50
    BINARY_LENGTH = 10 * 1024 * 1024

    # # virtual
    #

    def _define_cases(self):
        """
        Define cases per file supported

        This function must return a dict with one set of cases per
        file: key is path and value is another dict defining cases
        as pairs of name ([a-zA-Z_]) and content.

        Quick example:

            {
                '/etc/file1': {
                    'case1': "some triggering content",
                    'case2': "some other triggering content",
                    'case3': "some funny triggering content",
                },
                '/etc/file2': {
                    'case1': "some triggering content",
                    'case2': "some other triggering content",
                    'case3': "some funny triggering content",
                },
            }

        Note that trailing newline is added automatically to each content
        string. Also, whether content will be appended or replaced is decided
        by caller of the BaseCrippler.cripple method.
        """
        pass

    # # internal
    #

    def __init__(self):
        self.autocases = {
            'empty': lambda: '',
            'random_line': self._random_line,
            'random_lines': self._random_lines,
            'random_binary': self._random_binary,
        }
        self.cases = self._define_cases()

    def _append_to(self, path, content):
        with open(path, 'a+') as fh:
            fh.write(content)

    def _clobber(self, path, content):
        with open(path, 'w+') as fh:
            fh.write(content)

    def _random_binary(self, size=BINARY_LENGTH):
        chars = ''.join([chr(i) for i in xrange(256)])
        return random_string(strength=size, chars=chars)

    def _random_line(self, size=LINE_LENGTH):
        chars = string.letters + string.punctuation + " \t"
        return random_string(strength=size, chars=chars) + "\n"

    def _random_lines(self, size=LINE_LENGTH, count=LINE_COUNT):
        return "".join([self._random_line(size) for i in xrange(count)])

    def _get_content(self, path, case):

        try:
            content = self.autocases[case]()
        except KeyError:
            try:
                content = self.cases[path][case] + "\n"
            except KeyError:
                raise ValueError("unknown case: %s for: %s" % (case, path))
        return content

    # # public
    #

    def all_cases_for(self, path):
        """
        Return list of cases available for path
        """
        return self.cases[path].keys() + self.autocases.keys()

    def all_paths(self):
        """
        Return list of paths served by this implementation
        """
        return self.cases.keys()

    def cripple(self, path, case, op="replace"):
        """
        Cripple file according to selected case.

        op is either "append" or "replace" and means that the content will
        be appended to the file, otherwise it will replace it.
        """
        if op == 'replace':
            self._clobber(path, self._get_content(path, case))
        elif op == 'append':
            self._append_to(path, self._get_content(path, case))
        else:
            raise ValueError("unknown op: %s" % op)


class PackedSequence(object):
    """
    Iterator for arbitrarily long sequence of repeating symbols

    This class serves to help describe (and store) sequence of
    events in a human-readable way.

    For example, instead of writing:

        mytest(["a", "b", "c", "c", ... "c", "a", "c"])

    you can write

        mytest(PackedSequence("a,b,1000c,a,c"))

    except that no huge array needs to be stored and the notation
    is really simple and concise, no matter how huge your sequence
    actually is.

    You can add items to the PackedSequence object using append
    method.  So you can use it to report a sequence of events in
    a concise way, e.g.:

        ps = PackedSequence()
        for i in long:              # e.g. above list
            ps.append(i)
        print str(ps)               # "a,b,1000c,a,c"

    Note that from list-like operations, only append, next, len and
    iter are supported.
    """

    class _PackedItem(object):

        def __init__(self, item, num=1):
            self.item = item
            self.num = num

        def __str__(self):
            if self.num:
                n = "" if self.num == 1 else str(self.num)
                return "%s%s" % (n, self.item)
            return ""

        def __add__(self, other):
            if self.item == other.item:
                return self.__class__(self.item, self.num + other.num)
            else:
                raise TypeError("items cannot be added")

        def __nonzero__(self):
            return bool(self.num)

        def __repr__(self):
            return "%s(%s,%s)" % (self.__class__.__name__, self.item, self.num)

    def __init__(self, seq=None):
        self._items = self._squash(self._parse(seq)) if seq else []

    def __iter__(self):
        return self

    def __len__(self):
        return sum([i.num for i in self._items if i.num])

    def __str__(self):
        return ",".join([str(i) for i in self._items])

    def _squash(self, sparse):
        """
        Squash items, i.e. "b,1a,0a,0a,a,2a" to "1b,4a"
        """
        comp = []
        while sparse:
            nxt = sparse.pop()
            if not nxt:             # skip zero items
                continue
            elif comp:
                try:
                    comp[-1] += nxt
                except TypeError:   # cannot add -> append
                    comp.append(nxt)
            else:
                comp.append(nxt)
        comp.reverse()
        return comp

    def _parse(self, seq):
        """
        Parse sequence string
        """
        return [self._parse1(itm) for itm in seq.split(",")]

    def _parse1(self, itm):
        ns = ""
        while itm.startswith(tuple("1234567890")):
            ns += itm[:1]
            itm = itm[1:]
        n = int(ns) if ns else 1
        return PackedSequence._PackedItem(itm, n)

    def append(self, item):
        if self._items:
            lst = self._items[-1]
            if lst.item == item:
                lst.num += 1
                return
        self._items.append(PackedSequence._PackedItem(item))

    def next(self):

        while self._items:
            nxt = self._items[0]
            if nxt.num:
                nxt.num -= 1
                return nxt.item
            else:
                self._items.pop(0)

        raise StopIteration

    @classmethod
    def normalize(cls, seq):
        return str(cls(seq))


class BaseTestDriver(object):
    """
    Common test driver base class.

    As user of this class, all you need to do is instantiate
    the driver and call run method.

    options is a dict holding general options that need to be
    specified for the process to work, but are not part of test
    definition.  This is passed during instantiation, typically
    in a setUp method, and can be accessed as self.options.

    Other argument for initiating is default_argset, which can
    be used to prepare fallback values for cases that omit
    values from argset in run() call.  However, default_argset
    should only be used in marginal cases;  most of the time
    it's better to be explicit, or to consider moving the value
    to options.

    As test developer, you need to implement at least _do_run
    method.  Also if you need to call a cleanup method after
    each test, append that to cleanup_handlers.  Passing
    arguments to cleanup methods is not supported.

    Use of options vs. argset

    Typical example when we want to use options would be, when
    writing functional data-driven tests for a server that,
    say, accepts two arguments from range 0 to 100.  We want to
    cover the argument input values, we don't care about on
    which TCP port the server will run.

    So instead of saying

        argsets = [
            {'addr': 'localhost, 'port': 1234, 'arg1': 0, 'arg2' 0}
            {'addr': 'localhost, 'port': 1234, 'arg1': 0, 'arg2' 1}
            {'addr': 'localhost, 'port': 1234, 'arg1': 1, 'arg2' 0}
            {'addr': 'localhost, 'port': 1234, 'arg1': 1, 'arg2' 1}
            ...
        ]
        for argset in argsets:
            drv = OurServerTestDriver()
            result = drv.run(argset)

    we say:

        argsets = [
            {'arg1': 0, 'arg2' 0}
            {'arg1': 0, 'arg2' 1}
            {'arg1': 1, 'arg2' 0}
            {'arg1': 1, 'arg2' 1}
            ...
        ]
        for argset in argsets:
            drv = OurServerTestDriver(options={'addr': 'localhost',
                                               'port': 1234})
            result = drv.run(argset)

    so we can concentrate on coverage instead of boring environment
    details.
    """
    __metaclass__ = abc.ABCMeta

    # # internal
    #

    def __init__(self, options, default_argset={}):
        self.options = options
        self.argset = copy.deepcopy(default_argset)
        self.result = None
        self.cleanup_handlers = []

    def __cleanup(self):
        """
        Run each handler from self.cleanup_handlers
        """
        [h() for h in self.cleanup_handlers]

    # # virtual
    #

    @abc.abstractmethod
    def _do_run(self):
        """
        Abstract method to implement body of run() method

        This method needs to be overriden in subclass, and deal
        with actual running of the test.  self.argset and
        self.options are already assigned.

        return value of this method will become return value of
        run()

        Methods registered in self.cleanup_handlers will be
        called after this method.
        """
        pass

    # # public
    #

    def run(self, argset):
        """
        Run the actual test with argset

        Will set argset correctly, run the implemented _do_run
        method and eventually call any cleanup handlers.

        Return value is that of the _do_run method
        """
        self.argset.update(argset)
        result = self._do_run()
        self.__cleanup()
        return result
