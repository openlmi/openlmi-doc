.. _CIM-RecordForLog:

CIM_RecordForLog
----------------

Class reference
===============
Subclass of :ref:`CIM_ManagedElement <CIM-ManagedElement>`

The RecordForLog class is used to instantiate records to be aggregated to a Log.


Key properties
^^^^^^^^^^^^^^


Local properties
^^^^^^^^^^^^^^^^

.. _CIM-RecordForLog-Locale:

``string`` **Locale**

    **Deprecated!** 
    This property is being deprecated to avoid conflicts with localization implementations using CIM/XML over HTTP protocol, the preferred mechanism. 

    A locale indicates a particular geographical, political, or cultural region. The Locale specifies the language used in creating the RecordForLog data. If the Locale property is empty, it is assumed that the default locale is en_US (English). 

    The locale string consists of three sub-strings, separated by underscores: 

    - The first sub-string is the language code, as specified in ISO639. 

    - The second sub-string is the country code, as specified in ISO3166. 

    - The third sub-string is a variant, which is vendor specific. 

    For example, US English appears as: "en_US_WIN", where the "WIN" variant would specify a Windows browser-specific collation (if one exists). Since the variant is not standardized, it is not commonly used and generally is limited to easily recognizable values ("WIN", "UNIX", "EURO", etc.) used in standard environments. The language and country codes are required; the variant may be empty.

    
.. _CIM-RecordForLog-RecordFormat:

``string`` **RecordFormat**

    A string describing the data structure of the information in the property, RecordData. If the RecordFormat string is <empty>, RecordData should be interpreted as a free-form string. 

    

    To describe the data structure of RecordData, the RecordFormat string should be constructed as follows: 

    - The first character is a delimiter character and is used to parse the remainder of the string into sub-strings. 

    - Each sub-string is separated by the delimiter character and should be in the form of a CIM property declaration (i.e., datatype and property name). This set of declarations may be used to interpret the similarly delimited RecordData property. 

    For example, using a '*' delimiter, RecordFormat = "*string ThisDay*uint32 ThisYear*datetime SomeTime" 

    may be used to interpret: RecordData = "*This is Friday*2002*20020807141000.000000-300".

    
.. _CIM-RecordForLog-PerceivedSeverity:

``uint16`` **PerceivedSeverity**

    An enumerated value that describes the severity of the Indication from the notifier's point of view: 

    1 - Other, by CIM convention, is used to indicate that the Severity's value can be found in the OtherSeverity property. 

    3 - Degraded/Warning should be used when its appropriate to let the user decide if action is needed. 

    4 - Minor should be used to indicate action is needed, but the situation is not serious at this time. 

    5 - Major should be used to indicate action is needed NOW. 

    6 - Critical should be used to indicate action is needed NOW and the scope is broad (perhaps an imminent outage to a critical resource will result). 

    7 - Fatal/NonRecoverable should be used to indicate an error occurred, but it's too late to take remedial action. 

    2 and 0 - Information and Unknown (respectively) follow common usage. Literally, the Indication is purely informational or its severity is simply unknown.

    
    ======== ====================
    ValueMap Values              
    ======== ====================
    0        Unknown             
    1        Other               
    2        Information         
    3        Degraded/Warning    
    4        Minor               
    5        Major               
    6        Critical            
    7        Fatal/NonRecoverable
    ======== ====================
    
.. _CIM-RecordForLog-RecordData:

``string`` **RecordData**

    A string containing LogRecord data. 

    If the corresponding RecordFormat property is <empty>, or cannot be parsed according to the recommended format, RecordData should be interpreted as a free-form string. If the RecordFormat property contains parseable format information (as recommended in the RecordFormat Description qualifier), the RecordData string SHOULD be parsed in accordance with this format. In this case, RecordData SHOULD begin with the delimiter character and this character SHOULD be used to separate substrings in the manner described. The RecordData string can then be parsed by the data consumer and appropriately typed.

    

Local methods
^^^^^^^^^^^^^

*None*

Inherited properties
^^^^^^^^^^^^^^^^^^^^

| ``string`` :ref:`ElementName <CIM-ManagedElement-ElementName>`
| ``string`` :ref:`Description <CIM-ManagedElement-Description>`
| ``string`` :ref:`Caption <CIM-ManagedElement-Caption>`
| ``uint64`` :ref:`Generation <CIM-ManagedElement-Generation>`
| ``string`` :ref:`InstanceID <CIM-ManagedElement-InstanceID>`

Inherited methods
^^^^^^^^^^^^^^^^^

*None*

