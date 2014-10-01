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

import os
import abc
import sys
import tempfile
import subprocess
from textwrap import TextWrapper

from lmi.shell.LMIUtil import lmi_raise_or_dump_exception

from lmi.shell.LMIExceptions import LMINoPagerError


def _is_executable(fpath):
    """
    :param string fpath: path of executable
    :returns: True, if provided path is executable, False otherwise
    """
    return os.path.exists(fpath) and os.access(fpath, os.X_OK)


def _which(program):
    """
    :param string program: executable name
    :returns: full path of a selected executable
    :rtype: string
    """
    fpath, fname = os.path.split(program)
    if fpath:
        if _is_executable(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if _is_executable(exe_file):
                return exe_file
    return None


def _get_pager_with_params():
    """
    :returns: list containing a executable with its CLI arguments
    """
    if "PAGER" in os.environ:
        path = _which(os.environ["PAGER"])
        if path:
            return [path]
    for p in ["less", "more"]:
        path = _which(p)
        if not path:
            continue
        elif p == "less":
            return [path, "-S"]
        return [path]
    lmi_raise_or_dump_exception(LMINoPagerError("No default pager found"))
    return []


class LMITextFormatter(object):
    """
    Text formatter class. Used when printing a block of text to output stream.

    :param string text: text to be formatted
    """
    SUB_INDENT = 4

    def __init__(self, text):
        self._text = text

    def format(self, indent=0, width=80, f=sys.stdout,
               separator=True):
        """
        Formats a block of text and prints it to the output stream.

        :param int indent: number of spaces to indent the text block
        :param int width: total text block width
        :param f: output stream
        :param dictionary kwargs: supported keyword arguments
        :param bool separator: if True, there will be a new line appended after
            the formatted text; default value is True
        """
        if indent > width:
            return  # NOTE: this is wrong!
        wrapper = TextWrapper()
        wrapper.width = width - indent
        wrapper.subsequent_indent = " " * LMITextFormatter.SUB_INDENT
        for l in wrapper.wrap(self._text):
            f.write("%s%s\n" % (" " * indent, l))
        if separator:
            f.write("\n")


class LMIFormatter(object):
    """
    Abstract class for derived subclasses.
    """
    __metaclass__ = abc.ABCMeta

    def __init__(self):
        stty_dim = os.popen("stty size 2> /dev/null", "r").read().split()
        self._width = int(stty_dim[1]) if stty_dim else 80

    @abc.abstractmethod
    def format(self, indent=0, width=80, f=sys.stdout):
        """
        Formats a block of text and prints it to the output stream.

        :param int indent: number of spaces to indent the text block
        :param int width: total text block width
        :param f: output stream
        """
        pass

    def fancy_format(self, interactive):
        """
        Formats a block of text. If the LMIShell is running in interactive
        mode, pager will be used, otherwise the output will be written to
        standard output.

        :param bool interactive: defines, if to use pager
        """
        if interactive:
            tmpfile = tempfile.mkstemp()
            f = os.fdopen(tmpfile[0], "w")
            self.format(0, self._width, f)
            f.close()
            subprocess_params = _get_pager_with_params()
            if not subprocess_params:
                return
            subprocess_params.append(tmpfile[1])
            subprocess.call(subprocess_params)
            os.remove(tmpfile[1])
        else:
            self.format(0, self._width)


class LMIMethodFormatter(LMIFormatter):
    """
    Method formatter is used to print out :py:class:`wbem.CIMMethod`
    representation.
    """
    def __init__(self, cim_method):
        super(LMIMethodFormatter, self).__init__()
        self._cim_method = cim_method

    def format_qualifier(self, qualif, indent, width, f):
        """
        Prints out a parameter of :py:class:`wbem.CIMMethod`.

        :param int indent: number of spaces to indent the text block
        :param int width: total text block width
        :param f: output stream
        """
        val = "[qualifier] %s %s" % (qualif.type, qualif.name)
        if qualif.value:
            if isinstance(qualif.value, list):
                val += ": { " + ", ".join(
                    ["'" + str(v) + "'" for v in qualif.value]) + " }"
            else:
                val += ": '%s'" % str(qualif.value)
        LMITextFormatter(val).format(indent, width, f)

    def format_parameter(self, param, indent, width, f):
        """
        Prints out a parameter of :py:class:`wbem.CIMMethod`.

        :param int indent: number of spaces to indent the text block
        :param int width: total text block width
        :param f: output stream
        """
        ref_classname = ""
        if param.type == "reference":
            ref_classname = " (%s)" % param.reference_class
        formatter = LMITextFormatter("[param] %s%s %s" % (
            param.type, ref_classname, param.name))
        formatter.format(indent, width, f)

    def format_method(self, method, indent, width, f):
        """
        Prints out a method of :py:class:`wbem.CIMClass`.

        :param int indent: number of spaces to indent the text block
        :param int width: total text block width
        :param f: output stream
        """
        has_args = "..." if method.parameters else ""
        formatter = LMITextFormatter(
            "[method] %s %s(%s)" % (method.return_type, method.name, has_args))
        formatter.format(indent, width, f)
        for q in method.qualifiers.itervalues():
            self.format_qualifier(q, indent+4, width, f)
        for p in method.parameters.itervalues():
            self.format_parameter(p, indent+4, width, f)

    def format(self, indent=0, width=80, f=sys.stdout):
        """
        Prints out :py:class`CIMMethod` object.

        :param int indent: number of spaces to indent the text block
        :param int width: total text block width
        :param f: output stream
        """
        self.format_method(self._cim_method, indent, width, f)


class LMIClassFormatter(LMIMethodFormatter):
    """
    Class formatter is used to print out :py:class:`wbem.CIMClass`
    representation.

    :param CIMClass cim_class: object to print out
    """
    def __init__(self, cim_class):
        # Call LMIFormatter ctor directly and use inly LMIMethodFormatter
        # methods for LMIClass documentation formatting.
        LMIFormatter.__init__(self)
        self._cim_class = cim_class

    def format_property(self, prop, indent, width, f):
        """
        Prints out a property of :py:class:`wbem.CIMClass`.

        :param int indent: number of spaces to indent the text block
        :param int width: total text block width
        :param f: output stream
        """
        is_array_str = " array" if prop.is_array else ""
        val = "[property%s] %s %s" % (is_array_str, prop.type, prop.name)
        LMITextFormatter(val).format(indent, width, f)
        for q in prop.qualifiers.itervalues():
            self.format_qualifier(q, indent+4, width, f)

    def format(self, indent=0, width=80, f=sys.stdout):
        """
        Formats out :py:class:`wbem.CIMClass` object.

        :param int indent: number of spaces to indent the text block
        :param int width: total text block width
        :param f: output stream
        """
        formatter = LMITextFormatter("Class: %s (%s)" % (
            self._cim_class.classname,
            self._cim_class.superclass))
        formatter.format(indent, width, f)
        for q in self._cim_class.qualifiers.itervalues():
            self.format_qualifier(q, indent+4, width, f)
        for p in self._cim_class.properties.itervalues():
            self.format_property(p, indent+4, width, f)
        for m in self._cim_class.methods.itervalues():
            self.format_method(m, indent+4, width, f)


class LMIInstanceFormatter(LMIFormatter):
    """
    Instance formatter is used to print out :py:class:`wbem.CIMInstance`
    representation.

    :param CIMInstance cim_instance: object to print out
    """
    def __init__(self, cim_instance):
        super(LMIInstanceFormatter, self).__init__()
        self._cim_instance = cim_instance

    def format_property(self, prop, indent, width, f):
        """
        Prints out a property of :py:class:`wbem.CIMInstance`.

        :param int indent: number of spaces to indent the text block
        :param int width: total text block width
        :param f: output stream
        """
        is_array_str = " array" if prop.is_array else ""
        val = "[property%s] %s %s" % (is_array_str, prop.type, prop.name)
        if prop.value:
            if isinstance(prop.value, list):
                val += " = { " + ", ".join(
                    ["'" + str(v) + "'" for v in prop.value]) + " }"
            else:
                val += " = '%s'" % str(prop.value)
        LMITextFormatter(val).format(indent, width, f)
        for q in prop.qualifiers.itervalues():
            self.format_qualifier(q, indent+4, width, f)

    def format(self, indent=0, width=80, f=sys.stdout):
        """
        Prints out :py:class`CIMInstance` object.

        :param int indent: number of spaces to indent the text block
        :param int width: total text block width
        :param f: output stream
        """
        formatter = LMITextFormatter(
            "Instance of %s" % self._cim_instance.classname)
        formatter.format(indent, width, f)
        for p in self._cim_instance.properties.itervalues():
            self.format_property(p, indent+4, width, f)


class LMIMofFormatter(LMIFormatter):
    """
    MOF formatter is used to print out MOF representation of a CIM object.

    :param obj: object, which has :py:meth:`tomof` method
    """
    def __init__(self, obj):
        super(LMIMofFormatter, self).__init__()
        if not hasattr(obj, "tomof") or not callable(obj.tomof):
            raise TypeError("object needs provide tomof() method")
        self._obj = obj

    def format(self, indent=0, width=80, f=sys.stdout):
        """
        Formats a MOF object and prints it to the output stream.

        :param int indent: number of spaces to indent the text block
        :param int width: total text block width
        :param f: output stream
        """
        f.write(self._obj.tomof())
