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

import sys
import time
import random
import string

from lmi.shell.compat import *

from lmi.shell.LMIExceptions import LMIHandlerNamePatternError


class LMIIndicationListener(wbem.CIMIndicationListener):
    """
    Class representing indication listener, which provides a unified API for
    the server startup and shutdown and for registering an indication handler.

    :param str hostname: bind hostname
    :param int port: TCP port, where the server should listen for incoming
        messages
    :param str certfile: path to certificate file, if SSL used
    :param str keyfile: path to key file, if SSL used
    :param str trust_store: path to trust store
    """
    # Minimum replacable "X" characters in handler pattern string.
    HANDLER_MINIMUM_REPL_CHARS_COUNT = 8

    def __init__(self, hostname, port, certfile=None, keyfile=None,
                 trust_store=None):
        super(LMIIndicationListener, self).__init__(
            hostname, port, certfile, keyfile, trust_store)

    def __create_handler_name(self, handler_name_pattern):
        """
        Returns unique handler name by replacing "**X**" characters for random
        characters at the end of the handler_name_pattern.

        :param string handler_name_pattern: string containing replaceable
            characters at the end
        :returns: unique handler name
        :rtype: string
        """
        placeholder_char = "X"
        allowed_chars = string.ascii_uppercase + string.digits
        min_strength = LMIIndicationListener.HANDLER_MINIMUM_REPL_CHARS_COUNT

        def draw_string_of(strength):
            return "".join(random.choice(allowed_chars)
                           for x in xrange(strength))

        prefix = handler_name_pattern.rstrip(placeholder_char)
        strength = len(handler_name_pattern) - len(prefix)

        if strength == 0:
            return handler_name_pattern
        elif strength < min_strength:
            raise LMIHandlerNamePatternError(
                "Not enough replaceable characters provided")
        else:   # construct the handler name
            while True:
                handler_name = prefix + draw_string_of(strength)
                if handler_name not in self.handlers:
                    return handler_name

    def add_handler(self, handler_name_pattern, handler, *args, **kwargs):
        """
        Registers a handler into the indication listener. Returns a string,
        which is used for the indication recognition, when a message arrives.

        :param string handler_name_pattern: string, which may contain set of
            "**X**" characters at the end of the string. The "**X**" characters
            will be replaced by random characters and the whole string will
            form a unique string.
        :param handler: callable, which will be executed, when a indication is
            received
        :param tuple args: positional arguments for the handler
        :param dictionary kwargs: keyword arguments for the handler
        :returns: handler unique name
        :rtype: string
        """
        handler_name = self.__create_handler_name(handler_name_pattern)
        wbem.CIMIndicationListener.add_handler(
            self, handler_name, handler, *args, **kwargs)
        return handler_name
