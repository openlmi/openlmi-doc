Usage
=====
*LMI metacommand* is a command line utility build on top of client-side
libraries. It can not do much on its own. Its functionality is extended by
commands that are installed separately. Each command operates on a set of
providers that need to be installed on managed machine. Commands can be invoked
directly from shell or within `interactive mode`_.

Running from command line
-------------------------
It can run single command given on command line like this:

.. code-block:: sh

    lmi -h ${hostname} service list --all

Getting help
------------
For detailed help run:

.. code-block:: sh

    lmi --help

To get a list of available commands with short descriptions:

.. code-block:: sh

    lmi help

For help on a particular registered command:

.. code-block:: sh

    lmi help service

Interactive mode
----------------
Or it can be run in interactive mode when command is omitted:

.. code-block:: sh

    $ lmi -h ${hostname}
    lmi> help
    ...
    lmi> sw search django
    ...
    lmi> sw install python-django
    ...
    lmi> exit

``help`` command is always your good friend. Following two lines gets you the
same help message: ::

    lmi> help storage raid
    ...
    lmi> storage raid --help
    ...

Built-in commands
~~~~~~~~~~~~~~~~~
Interactive mode comes with few special commands not available from command
line. To get their list, type:

.. code-block:: sh

    lmi> : help

They are prefixed with ``:`` and optional space. Currently only namespace nesting
commands are supported. Those are ``:cd``, ``:..`` and ``:pwd``.

They work as expected: ::

    lmi> :pwd                       # top-level namespace
    /lmi
    lmi> :cd storage                # you can do storage specific stuff here
    >storage> :pwd
    /lmi/storage
    >storage> :cd raid              # we don't care about anything but raid
    >>raid> :pwd
    /lmi/storage/raid
    >>raid> :cd /lmi/sw             # let's manage packages now
    >sw> :..
    lmi>

Static commands
~~~~~~~~~~~~~~~
Aren't prepended with ``:`` and except for ``help`` are again available only in
interactive mode.

    +------+------------------------------------------------------------------+
    | EOF  | Same as hitting ``^D``. If some nested into some command's       |
    |      | namespace, it will map to ``:cd ..`` and parent namespace will   |
    |      | become active. If the top-level namespace is active, program     |
    |      | will exit.                                                       |
    +------+------------------------------------------------------------------+
    | exit | Exits immediately. It accepts optional exit code as an argument. |
    +------+------------------------------------------------------------------+
    | help | Lists available commands. Accepts command path as an optional    |
    |      | argument.                                                        |
    +------+------------------------------------------------------------------+

Extending *metacommand*
-----------------------
In order to make the *LMI metacommand* useful, you'll need to install some
commands. If you run Fedora, the easiest way to get them is with your favorite
package manager:

.. code-block:: sh

    sudo dnf install 'openlmi-scripts-*'

.. note::
    On *RHEL* you'll need to add `EPEL`_ to your repositories before installing
    them with `yum`.

They will be automatically discovered by *LMI metacommand*. You can ensure their presence with this simple test: ::

    $ lmi help
    Commands:
      file     - File and directory management functions.
      group    - POSIX group information and management.
      help     - Print the list of supported commands with short description.
      hwinfo   - Display hardware information.
      journald - Test for provider version requirements
      locale   - System locale management.
      net      - Networking service management.
      power    - System power state management.
      service  - System service management.
      sssd     - SSSD system service management.
      storage  - Basic storage device information.
      sw       - System software management.
      system   - Display general system information.
      user     - POSIX user information and management.

    For more informations about particular command type:
        help <command>

As Python eggs
~~~~~~~~~~~~~~
They may be installed on any distribution. Go for them also if you want to be
more up to date. They are available for download from `PyPI`_. The easiest way
to install them is with `pip` (shipped with `python-pip` package):

.. code-block:: sh

    pip search openlmi-scripts
    pip install --user openlmi-scripts-{hardware,system,service,storage}

Bleeding edge
~~~~~~~~~~~~~
Commands are available from our `git repository`_. Follow instructions there to
install the most up to date versions.

Documentation
~~~~~~~~~~~~~
.. ifconfig:: with_commands

    Check out documentation of currently implemented commands.

.. ifconfig:: not with_commands

    All the commands' documentation is available online:

.. include:: commands.txt

.. _EPEL: https://fedoraproject.org/wiki/EPEL
.. _PyPI: https://pypi.python.org/pypi?%3Aaction=search&term=openlmi-scripts*&submit=search
.. _git repository: https://github.com/openlmi/openlmi-scripts
