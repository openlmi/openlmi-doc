Startup
=======
By running the following, you will gain an interactive interface of the shell.
The *LMIShell* is waiting for the end of an input to quit -- by hitting
:kbd:`<ctrl+d>` you can exit from it:

.. code-block:: shell

    $ lmishell
    > <ctrl+d>
    $

or:

.. code-block:: shell

    $ lmishell
    > quit()
    $

.. _startup_connection:

Establish a connection
----------------------
Following examples demonstrate, how to connect to a `CIMOM` by issuing a
:py:func:`.connect` call.

Username/Password authentication
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Common means of performing the authentication is done by providing a *username*
and *password* to :py:func:`.connect` function. See the following example:

.. code-block:: python

    > c = connect("host", "username")
    password: # <not echoed>
    >

or:

.. code-block:: python

    > c = connect("host", "username", "password")
    >

.. Certificate authentication
   ^^^^^^^^^^^^^^^^^^^^^^^^^^
   LMIShell is capable of creating a connection by using a *X509* certificate. For
   the purpose of creating a connection object, it is necessary to provide two file
   names, which contain a *certificate* and a *private key*.

   See the following example:

   .. code-block:: python

      > c = connect("host", key_file="key_file", cert_file="cert_file")
      >

Unix socket
^^^^^^^^^^^
LMIShell can connect directly to the CIMOM using Unix socket. For this type of
connection, the shell needs to be run under root user and the destination
machine has to be either **localhost**, **127.0.0.1** or **::1**. This type of
connection is supported by TOG-Pegasus and there needs to be a Unix socket file
present at :file:`/var/run/tog-pegasus/cimxml.socket`. If the condition is not
met, classic username/password method will be used.

See following example:

.. code-block:: python

    > c = connect("localhost")
    >

Credentials validation
^^^^^^^^^^^^^^^^^^^^^^
Function :py:func:`.connect` returns either :py:class:`LMIConnection` object, if
the connection can be established, otherwise ``None`` is returned. Suppose, the
LMIShell is run in verbose mode (:option:`-v`, :option:`--verbose`, :option:`-m`
or :option:`--more-verbose` is used). See following example of creating a connection:

.. code-block:: python

    > # correct username or password
    > c = connect("host", "username", "password")
    INFO: Connected to host
    > isinstance(c, LMIConnection)
    True
    > # wrong login username or password
    > c = connect("host", "wrong_username", "wrong_password")
    ERROR: Error connecting to host, <error message>
    > c is None
    True
    >

**NOTE:** By default, LMIShell prints out only error messages, when calling a
:py:func:`.connect`; no INFO messages will be print out. It is possible to
suppress all the messages by passing :option:`-q` or :option:`--quiet`).

Server's certificate validation
-------------------------------
When using https transport protocol, LMIShell tries to validate each
server-side certificate against platform provided `CA trust store`. It is
necessary to copy the server's certificate from each CIMOM to the platform
specific trust store directory.

**NOTE:** It is possible to make LMIShell skip the certificate validation
process by :program:`lmishell` :option:`-n` or :option:`--noverify`.

See following example:

.. code-block:: shell

    $ lmishell --noverify
    >

