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
import ssl
import time
import pywbem
import random
import socket
import string
import threading

from xml.sax.saxutils import escape

from SocketServer import BaseRequestHandler
from SocketServer import ThreadingMixIn
from BaseHTTPServer import HTTPServer
from BaseHTTPServer import BaseHTTPRequestHandler

from lmi.shell.LMIExceptions import ConnectionError
from lmi.shell.compat import http


class CIMIndicationHandlerCallback(object):
    """
    Helper class, which stores indication handler callback with its arguments
    and keyword arguments.

    :param callback: callback, which is called, when a indication arrives
    :param tuple args: positional arguments for callback
    :param kwargs: keyword arguments for callback
    """
    def __init__(self, callback, *args, **kwargs):
        self.callback = callback
        self.args = args
        self.kwargs = kwargs


class CIMIndicationHandler(ThreadingMixIn, BaseHTTPRequestHandler):
    """
    Class representing indication handler. The class is derived from
    :py:class:`BaseHTTPRequestHandler`, because the indications are transported
    by http protocol, and from :py:class:`ThreadingMixIn`; the indication
    listener is designed as concurrent server to properly handle each incoming
    indication.
    """
    CIMLISTENER_PREFIX = "/CIMListener"

    @staticmethod
    def make_indication_response(cim_version, dtd_version, message_id,
                                protocol_version):
        """
        Returns CIM-XML indication response with CIM, DTD, Protocol version
        and Message ID filled.
        """
        return "<?xml version=\"1.0\" encoding=\"utf-8\" ?>\n" \
            "<CIM CIMVERSION=\"%s\" DTDVERSION=\"%s\">\n" \
            "<MESSAGE ID=\"%s\" PROTOCOLVERSION=\"%s\">\n" \
            "<SIMPLEEXPRSP>\n" \
            "<EXPMETHODRESPONSE NAME=\"ExportIndication\">\n" \
            "</EXPMETHODRESPONSE>\n" \
            "</SIMPLEEXPRSP>\n" \
            "</MESSAGE>\n" \
            "</CIM>\n" % tuple(escape(arg) for arg in (
                cim_version, dtd_version, message_id, protocol_version))

    def send_indication_response(self, response):
        """
        Sends indication response.
        """
        http_version = self.request_version
        http_response = http.HTTPResponse(200, http_version, wfile=self.wfile)
        http_response[http.HEADER_NAME_CONTENT_TYPE] = http.HEADER_VALUE_CONTENT_TYPE
        if http_version == http.HTTP_1_1:
            http_response[http.HEADER_NAME_TRANSFER_ENCODING] = http.HEADER_VALUE_CHUNKED
        else:
            http_response[http.HEADER_NAME_CONTENT_LENGTH] = len(response)
        http_response[http.HEADER_NAME_CIM_EXPORT] = http.HEADER_VALUE_CIM_EXPORT_METHOD_RESPONSE
        http_response[http.HEADER_NAME_TRAILER] = ", ".join([
            http.HEADER_VALUE_CIM_STATUS_CODE,
            http.HEADER_VALUE_CIM_STATUS_CODE_DESCRIPTION,
            http.HEADER_VALUE_CONTENT_LANGUAGE])
        http_response.body = response
        http_response.send()

    def do_POST(self):
        """
        Overridden method, which is called, when a indication is received. It
        parses the indication message and searches for a matching handler for
        the indication name.  Each subscribed indication should have it's
        Destination set something similar:

        ``<schema>://<destination>/<indication_name>``

        where the ``indication_name`` is a string, which properly defines the
        indication.
        """
        # If HTTP/1.1 used, try to get a message body length. If Content-Length
        # header is not present, set length to -1; rfile.read() will block,
        # until the connection is closed. Knowing the exact content length
        # makes the routine to finish early, even if the TCP connection is not
        # closed.
        length = int(self.headers.get("Content-Length", "-1"))
        msg = self.rfile.read(length)
        tt = pywbem.parse_cim(pywbem.xml_to_tupletree(msg))
        message = tt[2]
        export_methods = {}
        if message[0].upper() != "MESSAGE":
            return

        message_params = message[2]
        if not message_params:
            return

        for param in message_params:
            if param[0].upper() != "SIMPLEEXPREQ":
                continue
            export_method_call = param[2]
            export_method_name = export_method_call[1]["NAME"]
            exp_params = export_method_call[2]
            export_method_params = {}
            for method_param in exp_params:
                export_method_params[method_param[0]] = method_param[1]
            export_methods[export_method_name] = export_method_params

        ind = None
        if export_methods:
            ind_dict = export_methods.values()[0]
            if "NewIndication" in ind_dict:
                ind = ind_dict["NewIndication"]

        # Inform the CIMOM, that we got the indication.
        cim_version = tt[1]["CIMVERSION"]
        dtd_version = tt[1]["DTDVERSION"]
        message_id = message[1]["ID"]
        protocol_version = message[1]["PROTOCOLVERSION"]
        self.send_indication_response(
            self.make_indication_response(
                cim_version, dtd_version, message_id, protocol_version))

        path = self.path
        cimlistener_ind = path.find(self.CIMLISTENER_PREFIX)
        if cimlistener_ind != -1:
            # We got an indication with lmiwbem's CIMListener substring
            # present. We are using pywbem now, so it's necessary to strip the
            # prefix also with the substring (from the beginning). We try to
            # mimic Pegasus::CIMListener behavior here.
            path = path[cimlistener_ind + len(self.CIMLISTENER_PREFIX):]

        if path[0] == '/':
            # Path of the received indication may be prefixed by additional
            # slash. Drop it then.
            path = path[1:]

        if path in self.server._handlers:
            # We found the indication handler. Execute the callback.
            cb = self.server._handlers[path]
            cb.callback(ind, *cb.args, **cb.kwargs)


class CIMIndicationServer(ThreadingMixIn, HTTPServer):
    """
    Class representing indication server, derived from HTTPServer and designed
    as concurrent server.
    """
    daemon_threads = True


class CIMIndicationListener(object):
    """
    Class representing indication listener, which provides a unified API for
    the server startup and shutdown and for registering an indication handler.

    :param str hostname: bind hostname
    :param int port: listening port
    :param str cert_file: path to X509 certificate
    :param str key_file:  path to X509 private key; may be None, if
        cert_file also contains private key
    :param str trust_store: path to trust store
    """
    def __init__(self, hostname, port, certfile=None, keyfile=None,
                 trust_store=None):
        self._handlers = {}
        self._hostname = hostname
        self._port = port
        self._certfile = certfile
        self._keyfile = keyfile
        self._trust_store = trust_store

        self._server = None
        self._server_thread = None

    def start(self, retries=1):
        """
        Starts a indication listener.

        The indication listener runs in a newly-created thread.

        :param int retries: number of bind retries.
        """
        # Try to create a listener for retries-times.
        for i in xrange(retries):
            try:
                self._server = CIMIndicationServer(
                    (self._hostname, self._port), CIMIndicationHandler)
                break
            except socket.error as e:
                # We raise the exception, when we run out of retries or TCP port
                # is out of range.
                self._port += 1
                if i == retries - 1 or self._port >= 65536:
                    raise ConnectionError(e)
        self._server._handlers = self._handlers
        self._server_thread = threading.Thread(
            target=self._server.serve_forever)
        self._server_thread.daemon = True
        self._server_uses_ssl = False
        if self._certfile:
            self._server.socket = ssl.wrap_socket(
                self._server.socket,
                certfile=self._certfile,
                keyfile=self._keyfile,
                server_side=True,
                ca_certs=self._trust_store)
            self._server_uses_ssl = True
        self._server_thread.start()

    def stop(self):
        """
        Stops the indication listener.

        This method will also terminate the listener thread.
        """
        if self._server:
            self._server.shutdown()
        if self._server_thread:
            self._server_thread.join()
        self._server = None
        self._server_thread = None

    @property
    def is_alive(self):
        """
        :returns: flag indicating, if the indication listener is running
        :rtype: bool
        """
        if self._server_thread:
            return self._server_thread.is_alive()
        return False

    @property
    def uses_ssl(self):
        """
        :returns: True, if :py:class:`.CIMIndicationListener` uses secure
            connection; False otherwise
        :rtype: bool
        """
        if not self._server:
            return False
        return self._server_uses_ssl

    @property
    def hostname(self):
        """
        :returns: hostname or address, where the indication listener is waiting
            for messages
        :rtype: string
        """
        return self._hostname

    @property
    def port(self):
        """
        :returns: port, where the indication listener is waiting for messages
        :rtype: int
        """
        return self._port

    @property
    def handlers(self):
        """
        :returns: list of string of handler keys
        :rtype: list
        """
        return self._handlers.keys()

    def add_handler(self, handler_name, handler, *args, **kwargs):
        """
        Registers a handler into the indication listener. Returns a string,
        which is used for the indication recognition, when a message arrives.

        :param string handler_name: handler name
        :param handler: callable, which will be executed, when a indication is
            received
        :param tuple args: positional arguments for the handler
        :param dictionary kwargs: keyword arguments for the handler
        """
        self._handlers[handler_name] = CIMIndicationHandlerCallback(
            handler, *args, **kwargs)

    def remove_handler(self, name):
        """
        Removes a specified handler from the indication listener database.

        :param string name: indication name; returned by
            :py:meth:`.CIMIndicationListener.add_handler`
        """
        if name not in self._handlers:
            raise KeyError("No such handler registered: %s" % name)
        self._handlers.pop(name)
