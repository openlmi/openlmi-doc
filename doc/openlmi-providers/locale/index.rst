Locale Provider
===============

OpenLMI Locale is CIM provider for managing Linux locale settings (using the
`systemd/localed D-Bus interface <http://www.freedesktop.org/wiki/Software/systemd/localed/>`_).

It allows to set system locale represented by environment variables (LANG,
LC_CTYPE, LC_NUMERIC, LC_TIME, LC_COLLATE, LC_MONETARY, LC_MESSAGES, LC_PAPER,
LC_NAME, LC_ADDRESS, LC_TELEPHONE, LC_MEASUREMENT and LC_IDENTIFICATION),
set the default key mapping of the X11 servers (keyboard layouts, model, variant
and options) and the default key mapping for virtual console.

If you set a new system locale with SetLocale() method, all old system locale
settings will be dropped, and the new settings will be saved to disk. It will
also be passed to the system manager, and subsequently started daemons will
inherit the new system locale from it.

Note that already running daemons will not learn about the new system locale.

Also note that setting key mapping with SetVConsoleKeyboard() method instantly
applies the new keymapping to the console, while setting the key mapping of X11
server using SetX11Keyboard() method simply sets a default that may be used by
later sessions.

Contents:

.. toctree::
   :maxdepth: 2

   usage

.. ifconfig:: includeClasses

    CIM Classes:

    .. toctree::
       :maxdepth: 1

       mof/tree
       mof/index
