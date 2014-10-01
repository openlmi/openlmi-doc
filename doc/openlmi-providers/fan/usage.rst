Usage
=====

Examples for common use cases listed below are written in `lmishell`_.

Set up
------
*OpenLMI Fan* provider uses `lm-sensors`_ to find, observe and manage installed
fans. In order to make the fans exposed to it, one operation needs to be done:

.. code-block:: sh

    sensors-detect

``sensors-detect`` is a script shiped with ``lm_sensors`` package in *Fedora*
which tries to load correct modules for various sensor devices found in system.
It also writes a config used by ``sensors`` library which is utilised in this
provider. Please refer to its *sensors-detect (8)* man-page.

Examples
--------
Listing installed fans
~~~~~~~~~~~~~~~~~~~~~~
::

    c = connect("host", "user", "pass")
    for fan in c.root.cimv2.LMI_Fan.instances():
        print(fan.ElementName)

.. seealso::
    :ref:`LMI_Fan<LMI-Fan>`

Getting fan's speed
~~~~~~~~~~~~~~~~~~~
Current value can be read from :ref:`CurrentReading<CIM-NumericSensor-CurrentReading>`
property. It's measured in *revolutions per minute*.

::

        c = connect("host", "user", "pass")
        for fan in c.root.cimv2.LMI_FanSensor.instances():
            print("%s:\t%s RPM" % (fan.Name, fan.CurrentReading))

.. seealso::
    :ref:`LMI_FanSensor<LMI-FanSensor>`

.. *****************************************************************************
.. _lmishell:      https://fedorahosted.org/openlmi/wiki/shell
.. _lm-sensors: http://lm-sensors.org/
