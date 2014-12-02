.. _locale-usage:

Usage
=====

Some common use cases are described in the following parts.

Getting locale settings
-----------------------
Create connection, get instance (assuming the default namespace 'root/cimv2' is used)::

    c = connect("https://myhost")
    # optionally create namespace alias
    ns = c.root.cimv2
    locale = ns.LMI_Locale.first_instance()

Print what you're interested in::

    # get LANG setting
    print locale.Lang
    # get X11Layouts
    print locale.X11Layouts
    # get VConsoleKeymap
    print locale.VConsoleKeymap
    # get system timezone
    print locale.timezone
    # get whether the RTC is maintained in local time
    print locale.LocalRTC
    # get whether the system can be synchronized by NTP
    # and whether synchronization is enabled/disabled at the moment
    print locale.CanNTP
    print locale.NTP

Or print everything::

    # get all available settings
    locale.doc()

Setting system locale
---------------------
Set LANG and/or set individual locale variables. Lang, Language, LCCType, LCAddress,
LCNumeric, LCTelephone, LCCollate, LCPaper, LCMonetary, LCTime, LCMessages,
LCIdentification, LCName and LCMeasurement properties correspond to likewise named
Linux locale environmental variables::

    # set LANG (LANG value is used also for all other locale categories by default)
    locale.SetLocale(Lang="en_US.UTF-8")
    # set LANG and set different value for LC_TELEPHONE
    # note that SetLocale() clears previous setting - if you want to preserve
    # LANG value, you have to set it again
    locale.SetLocale(Lang="en_US.UTF-8",LCTelephone="cs_CZ.UTF-8")

Setting default key mapping of the X11 servers
----------------------------------------------
Set default key mapping for X11 server::

    locale.SetX11Keyboard(Layouts="de")

Optionally set keyboard model and variant::

    locale.SetX11Keyboard(Layouts="us",Model="dellsk8125",Variant="qwertz")

Set more than one layout and set option for switching between them::

    locale.SetX11Keyboard(Layouts="us,cz,de",Options="grp:alt_shift_toggle")

You can set Convert parameter to 'True', mapping for virtual console will be set
also then (nearest console keyboard setting for the chosen X11 setting)::

    locale.SetX11Keyboard(Layouts="us",Convert="True")

Setting default key mapping of the virtual console
--------------------------------------------------
Set default key mapping for virtual console::

    locale.SetVConsoleKeyboard(Keymap="us")

Again, setting Convert to 'True' will set the nearest X11 keyboard setting for
the chosen console setting::

    locale.SetVConsoleKeyboard(Keymap="us",Convert="True")

Setting system time
-------------------
There are two possibilities of setting the system time. You can pass
a value of microseconds (sic!) since 1 Jan 1970 UTC (Unix time a.k.a.
POSIX time or Epoch time)::

    # set system time to Wed Nov 26 13:50:20 2014
    locale.SetTime(UsecUTC=1417006220000000,Relative=False)

Or you can set Relative parameter to 'True' and the passed usec value will be
added to the current system time::

    # move the system time 15 second backwards from current system time
    locale.SetTime(UsecUTC=-15000000,Relative=True)

Setting system timezone
-----------------------
Set the system timezone::

    locale.SetTimezone(Timezone="Europe/Prague")

Note that if the RTC is configured to be maintained in local time it will
be updated accordingly.

Setting whether the RTC is maintained in local time/UTC
-------------------------------------------------------
Set that the RTC is maintained in local time::

    locale.SetLocalRTC(LocalRTC=True,FixSystem=False)

If the FixSystem parameter is set to 'True', the time from the RTC is read
again and the system clock adjusted according to the new setting. (This is
useful in cases where the RTC is probably more reliable than the system time.)

Setting whether the system clock is syncrhonized with a remote NTP server
-------------------------------------------------------------------------
Enable synchronization of the system clock with a remote NTP server::

    locale.SetNTP(UseNTP=True)
