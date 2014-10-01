# Copyright (C) 2013-2014 Michal Minar <miminar@redhat.com>
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
"""
Utility functions used in command sub-package.
"""

import inspect
import os
import re

#: Regular expression matching bracket argument such as ``<arg_name>``.
RE_OPT_BRACKET_ARGUMENT = re.compile('^<(?P<name>[^>]+)>$')
#: Regular expression matching argument written in upper case such as
#:``ARG_NAME``.
RE_OPT_UPPER_ARGUMENT = re.compile('^(?P<name>[A-Z0-9]+(?:[_-][A-Z0-9]+)*)$')
#: Regular expression matching showt options. They are one character
#: long, prefixed with single dash.
RE_OPT_SHORT_OPTION = re.compile('^-(?P<name>[a-z])$', re.IGNORECASE)
#: Regular expression matching long options (prefixed with double dash).
RE_OPT_LONG_OPTION = re.compile('^--(?P<name>[a-z0-9_-]+)$', re.IGNORECASE)
#: Command name can also be a single or double dash.
RE_COMMAND_NAME = re.compile(r'^([a-z]+(-[a-z0-9]+)*|--?)$')

def is_abstract_method(clss, method, missing_is_abstract=False):
    """
    Check, whether the given method is abstract in given class or list of
    classes. May be used to check, whether we should override particular
    abstract method in a meta-class in case that no non-abstract
    implementation is defined.

    :param clss: Class or list of classes that is
        searched for non-abstract implementation of particular method.
        If the first class having particular method in this list contain
        non-abstract implementation, ``False`` is returned.
    :type clss: type or tuple
    :param string method: Name of method to look for.
    :param boolean missing_is_abstract: This is a value returned, when
        not such method is defined in a set of given classes.
    :returns: Are all occurences of given method abstract?
    :rtype: boolean
    """
    if (   not isinstance(clss, (list, tuple, set))
       and not isinstance(clss, type)):
        raise TypeError("clss must be either a class or a tuple of classes")
    if not isinstance(method, basestring):
        raise TypeError("method must be a string")
    if isinstance(clss, type):
        clss = [clss]
    for cls in clss:
        if hasattr(cls, method):
            if getattr(getattr(cls, method), "__isabstractmethod__", False):
                return True
            else:
                return False
    return missing_is_abstract

def get_module_name(frame_level=2):
    """
    Get a module name of caller from particular outer frame.

    :param integer frame_level: Number of nested frames to skip when searching
        for called function scope by inspecting stack upwards. When the result
        of this function is applied directly on the definition of function,
        it's value should be 1. When used from inside of some other factory, it
        must be increased by 1.

        Level 0 returns name of this module. Level 1 returns module name of
        caller. Level 2 returns module name of caller's caller.
    :returns: Module name.
    :rtype: string
    """
    frame = inspect.currentframe()
    while frame_level > 0 and frame.f_back:
        frame = frame.f_back
        frame_level -= 1
    module = getattr(frame, 'f_globals', {}).get('__name__', None)
    if module is None:
        if hasattr(frame, 'f_code'):
            module = os.path.basename(frame.f_code.co_filename.splitext())[0]
        else:
            module = '_unknown_'
    return module
