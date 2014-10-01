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

Or print everything::

    # get all available settings
    locale.doc()

Setting system locale
---------------------
Set LANG and/or set individual locale variables. Lang, LCCType, LCAddress, LCNumeric,
LCTelephone, LCCollate, LCPaper, LCMonetary, LCTime, LCMessages, LCIdentification,
LCName and LCMeasurement properties correspond to likewise named Linux locale
environmental variables::

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
