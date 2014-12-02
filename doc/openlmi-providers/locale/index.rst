.. _openlmi-locale-provider:

Locale Provider
===============

.. rubric:: Overview

OpenLMI-Locale is CIM provider for managing Linux locale settings (using the
`systemd/localed D-Bus interface <http://www.freedesktop.org/wiki/Software/systemd/localed/>`_
and
`systemd/timedated D-Bus interface <http://www.freedesktop.org/wiki/Software/systemd/timedated/>`_).

.. rubric:: Clients

The API can be accessed by any WBEM-capable client. OpenLMI already provides:

* Python module :ref:`lmi.scripts.locale <openlmi-scripts-locale-python>`,
  part of
  :ref:`OpenLMI scripts <openlmi-scripts-python>`.

* Command line tool: :ref:`LMI metacommand <lmi_metacommand>`, with
  :ref:`'locale' <openlmi-scripts-locale-cmd>` subcommand.

.. rubric:: Features

* Get/set system locale represented by environment variables (LANG,
  LANGUAGE, LC_CTYPE, LC_NUMERIC, LC_TIME, LC_COLLATE, LC_MONETARY, LC_MESSAGES,
  LC_PAPER, LC_NAME, LC_ADDRESS, LC_TELEPHONE, LC_MEASUREMENT and LC_IDENTIFICATION).
* Get/set the default key mapping of the X11 servers (keyboard layouts, model, variant
  and options).
* Get/set the default key mapping for virtual console.
* Set the system time.
* Get/set the system timezone.
* Get/set whether RTC is maintained in local time or UTC.
* Get/set whether the system clock is synchronized with a remote NTP server using
  systemd-timesyncd.

.. rubric:: Examples

For examples how to use OpenLMI-Locale provider remotely
from `LMIShell <http://pythonhosted.org/openlmi-tools/index.html#lmishell>`_,
see the :ref:`usage <locale-usage>`.

.. rubric:: Notes

If you set a new system locale with SetLocale() method, all old system locale
settings will be dropped, and the new settings will be saved to disk. It will
also be passed to the system manager, and subsequently started daemons will
inherit the new system locale from it. Already running daemons will not learn
about the new system locale.

Setting key mapping with SetVConsoleKeyboard() method instantly applies the new
keymapping to the console, while setting the key mapping of X11 server using
SetX11Keyboard() method simply sets a default that may be used by later sessions.

.. rubric:: Table of Contents

.. toctree::
   :maxdepth: 2

   usage
