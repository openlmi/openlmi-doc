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

import keyword
import os.path
import rlcompleter

from lmi.shell.LMIReturnValue import LMIReturnValue
from lmi.shell.LMIConstantValues import LMIConstantValues
from lmi.shell.LMINamespace import LMINamespace
from lmi.shell.LMINamespace import LMINamespaceRoot
from lmi.shell.LMIClass import LMIClass
from lmi.shell.LMIInstance import LMIInstance
from lmi.shell.LMIInstanceName import LMIInstanceName
from lmi.shell.LMIMethod import LMIMethod
from lmi.shell.LMIConnection import LMIConnection


class LMICompleter(rlcompleter.Completer):
    """
    This LMIShell completer, which is used in the interactive mode, provides
    tab-completion for user friendliness.

    :param dictionary namespace: dictionary, where to perform a completion. If
        unspecified, the default namespace where completions are performed is
        :samp:`__main__` (technically, :samp:`__main__.__dict__`).
    """
    def __init__(self, namespace=None):
        rlcompleter.Completer.__init__(self, namespace)

    def _callable_postfix(self, val, word):
        """
        :param val: object, which is checked, if it is callable
        :param string word: input string
        :returns: string with opening parentheses, if the value is callable
        """
        if hasattr(val, word) and callable(getattr(val, word)):
            word = word + "("
        return word

    def complete(self, text, state):
        """
        :param string text: string to be completed.
        :param state: order number of the completion, see rlcompleter
        :returns: completed string
        """
        if not text:
            return ("\t", None)[state]
        return rlcompleter.Completer.complete(self, text, state)

    def global_matches(self, text):
        """
        :param string text: expression to complete
        :returns: list of all keywords, built-in functions and names
        :rtype: list of strings
        """
        names = rlcompleter.Completer.global_matches(self, text)
        prefix = os.path.commonprefix(names)
        if prefix and prefix != text:
            return [prefix]
        return names

    def attr_matches(self, text):
        """
        :param string text: expression to complete
        :returns: list of attributes of a given expression; if the expression
            is instance of LMI wrapper class, its important
            properties/attributes/ methods/parameters will be added too
        :rtype: list of strings
        """
        expr, attr = text.rsplit(".", 1)
        if "(" in expr or ")" in expr:
            # Do not evaluate a callable
            return

        obj = eval(expr, self.namespace)
        words = []
        if isinstance(obj, LMINamespace):
            words.extend([cls for cls in obj.classes() if cls[0] != "_"])
            if isinstance(obj, LMINamespaceRoot):
                words.extend(obj.namespaces)
        elif isinstance(obj, LMIClass):
            words.extend([p + "Values" for p in obj.valuemap_properties()])
        elif isinstance(obj, LMIInstance):
            words.extend([m + "(" for m in obj.methods()])
            words.extend(obj.properties())
        elif isinstance(obj, LMIInstanceName):
            words.extend([m + "(" for m in obj.methods()])
            words.extend(obj.key_properties())
        elif isinstance(obj, LMIMethod):
            words.extend([p + "Values" for p in obj.valuemap_parameters()])
        elif isinstance(obj, LMIConstantValues):
            words.extend(obj.values())
        elif isinstance(obj, LMIReturnValue):
            words.extend(obj.properties())
        words.extend([self._callable_postfix(obj, member)
                      for member in dir(obj) if member[0] != "_"])

        # Search for words, which can complete the current expression.
        names = filter(lambda word: word.startswith(attr), words)

        # Search for common prefix of all available words we currently got. If
        # there is any, return such completion.
        prefix = os.path.commonprefix(names)
        if prefix and prefix != attr:
            return ["%s.%s" % (expr, prefix)]

        # Return all the possible completions or an empty list, if there is no
        # completion available (to prevent rlcompleter to erase the whole
        # text).
        return names + [" "] if names else []
