.. _LMI-Locale:

LMI_Locale
----------

Class reference
===============
Subclass of :ref:`CIM_SystemSetting <CIM-SystemSetting>`

Class representing Linux Locale. The system locale controls the language settings of system services and of the UI before the user logs in, such as the display manager, as well as the default for users after login.


Key properties
^^^^^^^^^^^^^^

| :ref:`CreationClassName <CIM-SystemSetting-CreationClassName>`
| :ref:`SettingID <CIM-Setting-SettingID>`
| :ref:`SystemName <CIM-SystemSetting-SystemName>`
| :ref:`SystemCreationClassName <CIM-SystemSetting-SystemCreationClassName>`

Local properties
^^^^^^^^^^^^^^^^

.. _LMI-Locale-LCIdentification:

``string`` **LCIdentification**

    Defines the settings that relate to the metadata for the locale. 

    The property should be in format [language[_territory][.codeset][@modifier]], for example, 'en_AU.UTF-8' (Australian English using the UTF-8 encoding).

    
.. _LMI-Locale-X11Model:

``string`` **X11Model**

    Model of default keyboard mapping for X11. The property should be a keyboard model name (such as 'pc105' or 'thinkpad60').

    
.. _LMI-Locale-VConsoleKeymap:

``string`` **VConsoleKeymap**

    System keyboard mapping used on the text console. The property should be a keyboard mapping name (such as 'de' or 'us'). 

    
.. _LMI-Locale-LCMeasurement:

``string`` **LCMeasurement**

    Defines the settings relating to the measurement system in the locale (i.e., metric versus US customary units). 

    The property should be in format [language[_territory][.codeset][@modifier]], for example, 'en_AU.UTF-8' (Australian English using the UTF-8 encoding).

    
.. _LMI-Locale-X11Layouts:

``string`` **X11Layouts**

    System default keyboard mapping for X11 - the graphical UI before the user logs in, such as the display manager, as well as the default for users after login. The property should be a keyboard mapping name (such as 'de' or 'us'). Individual layouts are comma separated (e. g. 'us,cz,de').

    
.. _LMI-Locale-CanNTP:

``boolean`` **CanNTP**

    Indicates whether there's avalilable NTP service on the system. If true, the NTP service is available. If false, the NTP service is not available. 

    
.. _LMI-Locale-LCAddress:

``string`` **LCAddress**

    Defines the rules for the formats (e.g., postal addresses) used to describe locations and geography-related items. 

    The property should be in format [language[_territory][.codeset][@modifier]], for example, 'en_AU.UTF-8' (Australian English using the UTF-8 encoding).

    
.. _LMI-Locale-LCNumeric:

``string`` **LCNumeric**

    Defines the information used by the input/output functions, when they are advised to use the locale settings. 

    The property should be in format [language[_territory][.codeset][@modifier]], for example, 'en_AU.UTF-8' (Australian English using the UTF-8 encoding).

    
.. _LMI-Locale-LCTelephone:

``string`` **LCTelephone**

    Defines the settings that describe the formats to be used with telephone services. 

    The property should be in format [language[_territory][.codeset][@modifier]], for example, 'en_AU.UTF-8' (Australian English using the UTF-8 encoding).

    
.. _LMI-Locale-LCPaper:

``string`` **LCPaper**

    Defines the settings relating to the dimensions of the standard paper size (e.g., US letter versus A4). 

    The property should be in format [language[_territory][.codeset][@modifier]], for example, 'en_AU.UTF-8' (Australian English using the UTF-8 encoding).

    
.. _LMI-Locale-VConsoleKeymapToggle:

``string`` **VConsoleKeymapToggle**

    Toggle keyboard mapping used on the text console. The property should be a keyboard mapping name (such as 'de' or 'us'). 

    
.. _LMI-Locale-Lang:

``string`` **Lang**

    Main locale property. When defined, its value is used as default for all other non-defined LC* categories. 

    The property should be in format [language[_territory][.codeset][@modifier]], for example, 'en_AU.UTF-8' (Australian English using the UTF-8 encoding).

    
.. _LMI-Locale-LCCType:

``string`` **LCCType**

    Defines behavior of the character handling and classification functions. 

    The property should be in format [language[_territory][.codeset][@modifier]], for example, 'en_AU.UTF-8' (Australian English using the UTF-8 encoding).

    
.. _LMI-Locale-Language:

``string`` **Language**

    Sets a priority list of languages.  GNU gettext gives preference to it over LC_ALL and LANG for the purpose of message handling.

    The property should be in format [language][:[language]]..., for example, 'ru:en' (Russian preffered, but if it is not available, use English.)

    
.. _LMI-Locale-LocalRTC:

``boolean`` **LocalRTC**

    Indicates whether the system RTC is in local or UTC timezone. If true, the system RTC is in local timezone. If false, the system RTC is in UTC timezone.

    
.. _LMI-Locale-X11Options:

``string`` **X11Options**

    Options for default keyboard mapping for X11. The property should be a keyboard option name (such as 'altwin:menu' or 'grp:lalt_toggle'). Individual options are comma separated (e. g. 'grp:alt_shift_toggle,shift:both_capslock').

    
.. _LMI-Locale-LCCollate:

``string`` **LCCollate**

    Defines the behavior of the functions, which are used to compare and/or sort strings in the local alphabet. 

    The property should be in format [language[_territory][.codeset][@modifier]], for example, 'en_AU.UTF-8' (Australian English using the UTF-8 encoding).

    
.. _LMI-Locale-X11Variant:

``string`` **X11Variant**

    Variant of default keyboard mapping for X11. The property should be a keyboard variant name (such as 'dvorak' or 'qwerty').

    
.. _LMI-Locale-NTP:

``boolean`` **NTP**

    Indicates whether the NTP service is enabled/started or disabled/stopped. If true, the NTP service is enabled/started. If false, the NTP service is disabled/stopped.

    
.. _LMI-Locale-LCName:

``string`` **LCName**

    Defines the settings that describe the formats used to address persons. 

    The property should be in format [language[_territory][.codeset][@modifier]], for example, 'en_AU.UTF-8' (Australian English using the UTF-8 encoding).

    
.. _LMI-Locale-LCMonetary:

``string`` **LCMonetary**

    Defines the way numbers are usually printed, with details such as decimal point versus decimal comma. 

    The property should be in format [language[_territory][.codeset][@modifier]], for example, 'en_AU.UTF-8' (Australian English using the UTF-8 encoding).

    
.. _LMI-Locale-Timezone:

``string`` **Timezone**

    The system timezone. The property should be a zone name in the uniform naming convention form used by tz database (e. g. 'Europe/Prague').

    
.. _LMI-Locale-LCTime:

``string`` **LCTime**

    Defines how to display the current time in a locally acceptable form; for example, most of Europe uses a 24-hour clock versus the 12-hour clock used in the United States. 

    The property should be in format [language[_territory][.codeset][@modifier]], for example, 'en_AU.UTF-8' (Australian English using the UTF-8 encoding).

    
.. _LMI-Locale-LCMessages:

``string`` **LCMessages**

    Defines the language messages are displayed in and what an affirmative or negative answer looks like. 

    The property should be in format [language[_territory][.codeset][@modifier]], for example, 'en_AU.UTF-8' (Australian English using the UTF-8 encoding).

    

Local methods
^^^^^^^^^^^^^

    .. _LMI-Locale-SetLocale:

``uint32`` **SetLocale** (``string`` Lang, ``string`` Language, ``string`` LCCType, ``string`` LCNumeric, ``string`` LCTime, ``string`` LCCollate, ``string`` LCMonetary, ``string`` LCMessages, ``string`` LCPaper, ``string`` LCName, ``string`` LCAddress, ``string`` LCTelephone, ``string`` LCMeasurement, ``string`` LCIdentification)

    Method used to set the system locale. If you set a new system locale, all old system locale settings will be dropped, and the new settings will be saved to disk. It will also be passed to the system manager, and subsequently started daemons will inherit the new system locale from it. Note that already running daemons will not learn about the new system locale.

    
    **Parameters**
    
        *IN* ``string`` **Lang**
            Sets the Lang property. 

            The value should be in format [language[_territory][.codeset][@modifier]], for example, 'en_AU.UTF-8' (Australian English using the UTF-8 encoding).

            
        
        *IN* ``string`` **Language**
            Sets the LANGUAGE property. 

            The value should be in format [language][:[language]]..., for example, 'ru:en' (Russian preffered, but if it is not available, use English).

            
        
        *IN* ``string`` **LCCType**
            Sets the LCCType property. 

            The value should be in format [language[_territory][.codeset][@modifier]], for example, 'en_AU.UTF-8' (Australian English using the UTF-8 encoding).

            
        
        *IN* ``string`` **LCNumeric**
            Sets the LCNumeric property. 

            The value should be in format [language[_territory][.codeset][@modifier]], for example, 'en_AU.UTF-8' (Australian English using the UTF-8 encoding).

            
        
        *IN* ``string`` **LCTime**
            Sets the LCTime property. 

            The value should be in format [language[_territory][.codeset][@modifier]], for example, 'en_AU.UTF-8' (Australian English using the UTF-8 encoding).

            
        
        *IN* ``string`` **LCCollate**
            Sets the LCCollate property. 

            The value should be in format [language[_territory][.codeset][@modifier]], for example, 'en_AU.UTF-8' (Australian English using the UTF-8 encoding).

            
        
        *IN* ``string`` **LCMonetary**
            Sets the LCMonetar property. 

            The value should be in format [language[_territory][.codeset][@modifier]], for example, 'en_AU.UTF-8' (Australian English using the UTF-8 encoding).

            
        
        *IN* ``string`` **LCMessages**
            Sets the LCMessages property. 

            The value should be in format [language[_territory][.codeset][@modifier]], for example, 'en_AU.UTF-8' (Australian English using the UTF-8 encoding).

            
        
        *IN* ``string`` **LCPaper**
            Sets the LCPaper property. 

            The value should be in format [language[_territory][.codeset][@modifier]], for example, 'en_AU.UTF-8' (Australian English using the UTF-8 encoding).

            
        
        *IN* ``string`` **LCName**
            Sets the LCName property. 

            The value should be in format [language[_territory][.codeset][@modifier]], for example, 'en_AU.UTF-8' (Australian English using the UTF-8 encoding).

            
        
        *IN* ``string`` **LCAddress**
            Sets the LCAddress property. 

            The value should be in format [language[_territory][.codeset][@modifier]], for example, 'en_AU.UTF-8' (Australian English using the UTF-8 encoding).

            
        
        *IN* ``string`` **LCTelephone**
            Sets the LCTelephone property. 

            The value should be in format [language[_territory][.codeset][@modifier]], for example, 'en_AU.UTF-8' (Australian English using the UTF-8 encoding).

            
        
        *IN* ``string`` **LCMeasurement**
            Sets the LCMeasurement property. 

            The value should be in format [language[_territory][.codeset][@modifier]], for example, 'en_AU.UTF-8' (Australian English using the UTF-8 encoding).

            
        
        *IN* ``string`` **LCIdentification**
            Sets the LCIdentification property. 

            The value should be in format [language[_territory][.codeset][@modifier]], for example, 'en_AU.UTF-8' (Australian English using the UTF-8 encoding).

            
        
    
    .. _LMI-Locale-SetX11Keyboard:

``uint32`` **SetX11Keyboard** (``string`` Layouts, ``string`` Model, ``string`` Variant, ``string`` Options, ``boolean`` Convert)

    Method used to set the default key mapping of the X11 server. 

    
    **Parameters**
    
        *IN* ``string`` **Layouts**
            Sets X11 keyboard mapping (such as 'de' or 'us'). Individual layouts are comma separated (e. g. 'us,cz,de'). Required parameter.

            
        
        *IN* ``string`` **Model**
            Sets X11 keyboard model (such as 'pc105' or 'thinkpad60'). Optional parameter.

            
        
        *IN* ``string`` **Variant**
            Sets X11 keyboard variant (such as 'dvorak' or 'qwerty'). Optional parameter.

            
        
        *IN* ``string`` **Options**
            Sets X11 keyboard options (such as 'altwin:menu' or 'grp:lalt_toggle'). Individual options are comma separated (e. g. 'grp:alt_shift_toggle,shift:both_capslock'). Optional parameter.

            
        
        *IN* ``boolean`` **Convert**
            Convert may be set to optionally convert the X11 keyboard mapping to console keyboard configuration. Optional parameter. If set to TRUE, the nearest console keyboard setting for the chosen X11 setting is set.

            
        
    
    .. _LMI-Locale-SetNTP:

``uint32`` **SetNTP** (``boolean`` UseNTP)

    Method used to set whether the system clock is synchronized with the network using systemd-timesyncd. This will enable/start resp. disable/stop the systemd-timesyncd service.

    
    **Parameters**
    
        *IN* ``boolean`` **UseNTP**
            If set to TRUE, systemd-timesyncd service will be will enabled/started. If it is FALSE, systemd-timesyncd service will be disableed/stopped.

            
        
    
    .. _LMI-Locale-SetTime:

``uint32`` **SetTime** (``sint64`` UsecUTC, ``boolean`` Relative)

    Method used to set the system clock.

    
    **Parameters**
    
        *IN* ``sint64`` **UsecUTC**
            New system clock (microseconds since 1 Jan 1970 UTC).

            
        
        *IN* ``boolean`` **Relative**
            If set to TRUE, the passed UsecUTC value will be added to the current system time. If it is FALSE, the current system time will be set to the passed UsecUTC value.

            
        
    
    .. _LMI-Locale-SetVConsoleKeyboard:

``uint32`` **SetVConsoleKeyboard** (``string`` Keymap, ``string`` KeymapToggle, ``boolean`` Convert)

    Method used to set the key mapping on the virtual console. 

    
    **Parameters**
    
        *IN* ``string`` **Keymap**
            Sets the keyboard mapping on the virtual console (such as 'us' or 'cz-qwerty'), new mapping is applied instantly. Required parameter.

            
        
        *IN* ``string`` **KeymapToggle**
            Sets toggle keyboard mapping on the virtual console (such as 'us' or 'cz-qwerty'). Optional parameter.

            
        
        *IN* ``boolean`` **Convert**
            Convert may be set to optionally convert the console keyboard configuration to X11 keyboard mappings. Optional parameter. If set to TRUE, the nearest X11 keyboard setting for the chosen console setting is set.

            
        
    
    .. _LMI-Locale-SetTimezone:

``uint32`` **SetTimezone** (``string`` Timezone)

    Method used to set the system timezone. 

    
    **Parameters**
    
        *IN* ``string`` **Timezone**
            New timezone (such as 'Europe/Prague').

            
        
    
    .. _LMI-Locale-SetLocalRTC:

``uint32`` **SetLocalRTC** (``boolean`` LocalRTC, ``boolean`` FixSystem)

    Method used to set whether the RTC is in local time or UTC.

    
    **Parameters**
    
        *IN* ``boolean`` **LocalRTC**
            If set to TRUE, the RTC value is assumed to be stored in local time. If it is FALSE, the RTC value is assumed to be stored in UTC.

            
        
        *IN* ``boolean`` **FixSystem**
            If set to TRUE, the time from the RTC is read again and the system is clock adjusted according to the new setting. If it is FALSE, the system time is written to the RTC taking the new setting into account.

            
        
    

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`
| ``string`` :ref:`SystemName <CIM-SystemSetting-SystemName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``string`` :ref:`SettingID <CIM-SystemSetting-SettingID>`
| ``string`` :ref:`CreationClassName <CIM-SystemSetting-CreationClassName>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`SystemCreationClassName <CIM-SystemSetting-SystemCreationClassName>`

Inherited methods
^^^^^^^^^^^^^^^^^

| :ref:`VerifyOKToApplyToCollection <CIM-Setting-VerifyOKToApplyToCollection>`
| :ref:`VerifyOKToApplyIncrementalChangeToCollection <CIM-Setting-VerifyOKToApplyIncrementalChangeToCollection>`
| :ref:`VerifyOKToApplyIncrementalChangeToMSE <CIM-Setting-VerifyOKToApplyIncrementalChangeToMSE>`
| :ref:`ApplyToCollection <CIM-Setting-ApplyToCollection>`
| :ref:`ApplyToMSE <CIM-Setting-ApplyToMSE>`
| :ref:`ApplyIncrementalChangeToCollection <CIM-Setting-ApplyIncrementalChangeToCollection>`
| :ref:`ApplyIncrementalChangeToMSE <CIM-Setting-ApplyIncrementalChangeToMSE>`
| :ref:`VerifyOKToApplyToMSE <CIM-Setting-VerifyOKToApplyToMSE>`

