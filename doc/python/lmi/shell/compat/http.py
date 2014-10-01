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

from abc import ABCMeta
from abc import abstractmethod
from collections import OrderedDict
from BaseHTTPServer import BaseHTTPRequestHandler

# HTTP responses dict.
responses = BaseHTTPRequestHandler.responses

# HTTP string versions
HTTP_0_9 = "HTTP/0.9"
HTTP_1_0 = "HTTP/1.0"
HTTP_1_1 = "HTTP/1.1"

# HTTP headers with values.
HEADER_NAME_CIM_EXPORT = "CIMExport"
HEADER_NAME_CONTENT_LENGTH = "Content-Length"
HEADER_NAME_CONTENT_TYPE = "Content-Type"
HEADER_NAME_TRAILER = "Trailer"
HEADER_NAME_TRANSFER_ENCODING = "transfer-encoding"
HEADER_VALUE_CIM_EXPORT_METHOD_RESPONSE = "MethodResponse"
HEADER_VALUE_CHUNKED = "chunked"
HEADER_VALUE_CIM_STATUS_CODE = "CIMStatusCode"
HEADER_VALUE_CIM_STATUS_CODE_DESCRIPTION = "CIMStatusCodeDescription"
HEADER_VALUE_CONTENT_LANGUAGE = "Content-Language"
HEADER_VALUE_CONTENT_TYPE = "application/xml; charset=utf-8"

CRLF = "\r\n"


class HTTPBase(object):
    """
    Base class for HTTP messages.
    """
    def __init__(self, wfile):
        self.wfile = wfile


class HTTPMessage(HTTPBase):
    """
    Class for sending a HTTP message.
    """
    __metaclass__ = ABCMeta

    # RFC 2616 doesn't define chunk size limit. Let's pick one.
    CHUNK_MAX = 4 * 1024

    def __init__(self, http_version, headers=None, body=None, wfile=None):
        super(HTTPMessage, self).__init__(wfile)
        self.http_version = http_version
        self.headers = OrderedDict(headers or {})
        self.body = body or ""

    def __getitem__(self, name):
        """
        Returns a HTTP header.
        """
        return self.headers[name]

    def __setitem__(self, name, value):
        """
        Updates or adds a new HTTP header.
        """
        self.headers[name] = value

    @staticmethod
    def is_message_chunked(headers):
        """
        Returns True, if the headers contain "chunked" encoding entry.
        """
        return headers.get(
            HEADER_NAME_TRANSFER_ENCODING) == \
            HEADER_VALUE_CHUNKED

    def send_crlf(self):
        """
        Sends CRLF symbols.
        """
        self.wfile.write(CRLF)

    def send_chunk(self, chunk=""):
        """
        Sends a one chunk of the message.
        """
        self.wfile.write("%x" % len(chunk))
        self.wfile.write(CRLF)
        self.wfile.write(chunk)
        self.wfile.write(CRLF)

    def send_message_body(self, body):
        """
        Sends a response body.
        """
        if not self.is_message_chunked(self.headers) or \
                self.http_version != HTTP_1_1:
            self.wfile.write(body)
        else:
            pos = 0
            msg_len = len(body)
            while pos < msg_len:
                if msg_len - pos >= self.CHUNK_MAX:
                    to_send = self.CHUNK_MAX
                else:
                    to_send = msg_len - pos
                # Send a chunk of data.
                self.send_chunk(body[pos:pos+to_send])
                pos += to_send

            # Terminating chunk
            self.send_chunk()

    def send_header(self, name, value):
        """
        Sends a HTTP header.
        """
        if self.http_version == HTTP_0_9:
            return
        self.wfile.write("%s: %s" % (name, value))
        self.send_crlf()

    def send_end_headers(self):
        """
        Sends HTTP headers terminator.
        """
        if self.http_version == HTTP_0_9:
            return
        self.send_crlf()

    def send_message_headers(self, headers):
        """
        Sends HTTP headers.
        """
        for name, value in headers.iteritems():
            self.send_header(name, value)
        self.send_end_headers()

    @abstractmethod
    def send(self, *args, **kwargs):
        """
        Sends either HTTP message.
        """
        pass


class HTTPResponse(HTTPMessage):
    """
    HTTP Response class.
    """
    def __init__(self, code, http_version, headers=None, body=None, wfile=None):
        super(HTTPResponse, self).__init__(http_version, headers, body, wfile)
        self.code = code

    def send_message_response_line(self, http_version, code):
        """
        Sends a HTTP response status line.
        """
        if http_version in (HTTP_1_0, HTTP_1_1):
            self.wfile.write("%s %d" % (http_version, code))
            if code in responses:
                self.wfile.write(" %s" % responses[code][0])
            self.send_crlf()
        elif http_version == HTTP_0_9:
            self.wfile.write("%s %d" % (http_version, code))
            self.send_crlf()

    def send(self, wfile=None):
        """
        Sends a response header and message.
        """
        if wfile is not None:
            self.wfile = wfile
        assert self.wfile is not None, "wfile can't be None"
        self.send_message_response_line(self.http_version, self.code)
        self.send_message_headers(self.headers)
        self.send_message_body(self.body)
