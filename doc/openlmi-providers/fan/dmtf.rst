DMTF profiles
=============
*OpenLMI Fan* provider implements *Fan Profile*

Fan Profile
--------------------------
Implemented *DMTF* version: ``1.0.1``

Described by `DSP1013`_

It defines the classes used to describe the fans and the possible redundancy
of the fans in a managed system. The document also defines association
classes that describe the relationship of the fan to the fan’s physical
aspects (such as FRU data) to the sensors monitoring the fans, to other
cooling devices, to redundancy status, and to DMTF profile version
information. The information in this specification is intended to be
sufficient for a provider or consumer of this data to identify unambiguously
the classes, properties, methods, and values that are mandatory to be
instantiated and manipulated to represent and manage fans and redundant fans
of managed systems and subsystems that are modeled using the DMTF CIM core
and extended model definitions.

Not implemented features
~~~~~~~~~~~~~~~~~~~~~~~~
*DMTF* profile defines many classes that are not instrumented due to
limitations of low level libraries giving informations about fans.
Here is a list of not implemented classes:

    ``CIM_ManagedSystemElement``
        Models the piece of hardware being cooled by particular fan. It's
        associated with :ref:`LMI_Fan<LMI-Fan>` through ``CIM_AssociatedColling`` which
        is also not instrumented.

    ``CIM_RedundancySet``
        Represents redundacy of fans belonging to particular computer
        system. It's associated with :ref:`LMI_Fan<LMI-Fan>` through
        ``CIM_MemberOfCollection`` and ``CIM_IsSpare`` associations.
        There is no way how to detect whether the fan is spare or not.

Classes that shall be implemented
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
There are still classes missing implementation and are planned to
be delivered in future versions.

    ``CIM_SystemDevice``
        Associates :ref:`LMI_Fan<LMI-Fan>` to ``CIM_ComputerSystem``.

    ``CIM_EnabledLogicalElementCapacilities``
        Represents the capabilities of associated fan. It's associated
        to :ref:`LMI_Fan<LMI-Fan>` through ``CIM_ElementCapabilities``.

Not implemented optional features
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
*Physical Asset* association from :ref:`LMI_Fan<LMI-Fan>` to ``CIM_PhysicalPackage``
through ``CIM_Realizes`` association class is not instrumented.
This is an optional feature. It may be implemented later.

*Physical Asset* is a related profile implemented by *OpenLMI Hardware*
provider.

Class overview
~~~~~~~~~~~~~~

    +---------------------------------------------------------+---------------------------------------------------+------------------+
    | Class-name                                              | Parent_class                                      | Type             |
    +=========================================================+===================================================+==================+
    | :ref:`LMI_Fan<LMI-Fan>`                                 | :ref:`CIM_Fan<CIM-Fan>`                           | Plain            |
    +---------------------------------------------------------+---------------------------------------------------+------------------+
    | :ref:`LMI_FanSensor<LMI-FanSensor>`                     | :ref:`CIM_NumericSensor<CIM-NumericSensor>`       | Plain            |
    +---------------------------------------------------------+---------------------------------------------------+------------------+
    | :ref:`LMI_FanAssociatedSensor<LMI-FanAssociatedSensor>` | :ref:`CIM_AssociatedSensor<CIM-AssociatedSensor>` | Association      |
    +---------------------------------------------------------+---------------------------------------------------+------------------+

LMI_Fan
^^^^^^^
Represents the the fan installed and connected to computer.
One of the most important keys is :ref:`DeviceID<LMI-Fan-DeviceID>`. It's a
*sys* path to kernel driver's abstraction for fan combined with its name.

Typical sys directory for fan looks like this: ::

    /sys/class/hwmon/hwmon1/device/
    ├── driver -> ../../../bus/platform/drivers/thinkpad_hwmon
    ├── fan1_input
    ├── hwmon
    │   └── hwmon1
    │       ├── device -> ../../../thinkpad_hwmon
    │       ├── power
    │       │   ├── async
    │       │   ├── autosuspend_delay_ms
    │       │   ├── control
    │       │   ├── runtime_active_kids
    │       │   ├── runtime_active_time
    │       │   ├── runtime_enabled
    │       │   ├── runtime_status
    │       │   ├── runtime_suspended_time
    │       │   └── runtime_usage
    │       ├── subsystem -> ../../../../../class/hwmon
    │       └── uevent
    ├── modalias
    ├── name
    ├── power
    │   ├── async
    │   ├── autosuspend_delay_ms
    │   ├── control
    │   ├── runtime_active_kids
    │   ├── runtime_active_time
    │   ├── runtime_enabled
    │   ├── runtime_status
    │   ├── runtime_suspended_time
    │   └── runtime_usage
    ├── pwm1
    ├── pwm1_enable
    ├── subsystem -> ../../../bus/platform
    └── uevent

Corresponding ``DeviceID`` is ``/sys/class/hwmon/hwmon1/device/fan1``. The fan
name is the prefix of ``*_input`` file which gives the current
:abbr:`RPM(Revolutions per minute)` value.

It has several other interesting properties:

    :ref:`OtherIdentifyingInfo<CIM-LogicalDevice-OtherIdentifyingInfo>` : ``string []``
        Has the name of chip controlling the fan as the first item.

LMI_FanSensor
^^^^^^^^^^^^^
Represents a sensor measuring a speed of particular fan. It's exactly the same
keys and values except for
:ref:`CreationClassName<CIM-LogicalDevice-CreationClassName>` containg the name
of corresponding class ``LMI_Fan``.

It inherts many methods that are not supported because underlying library does
not offer such functionality. Controlling of fans is very hardware dependent.
Different drivers may provide different ways and possibilities to manage
connected fans.

..
    ***************************************************************************

.. _DSP1013: http://www.dmtf.org/sites/default/files/standards/documents/DSP1013_1.0.1.pdf

