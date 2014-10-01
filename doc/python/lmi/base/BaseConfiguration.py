# Copyright (C) 2012 Red Hat, Inc.  All rights reserved.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
#
# Authors: Jan Safranek <jsafrane@redhat.com>
# Authors: Michal Minar <miminar@redhat.com>
# -*- coding: utf-8 -*-
"""
Module for BaseConfiguration class.

BaseConfiguration
--------------------

.. autoclass:: BaseConfiguration
    :members:

"""

import ConfigParser
import logging
import os
import socket

from lmi.base.singletonmixin import Singleton

def convert_value(section, option, convert_func, value):
    """
    Return result of application of ``convert_func`` on value.
    If the conversion failes, error is logged and ValueError is raised.

    :param section: (``str``) Section of configuration file. Used for
        error message.
    :param option: (``str``) Option of configuration file. Used for
        error message.
    :param convert_func: (``type``) Conversion function to apply on passed
        value.
    :param value: (``basestring``) Value to convert.
    """
    if not isinstance(value, basestring):
        raise TypeError("value must be a string")
    try:
        if convert_func is bool:
            return value.lower() in ('1', 'y', 'yes', 'on', 'true')
        if convert_func is str and isinstance(value, unicode):
            return value.encode('utf-8')
        if convert_func is unicode and isinstance(value, str):
            return value.decode('utf-8')
        return convert_func(value)
    except ValueError as exc:
        logging.getLogger(__name__).error(
                'failed to convert value of "[%s]%s: %s', section, option,
                exc)
        raise

class BaseConfiguration(Singleton):
    """
        OpenLMI configuration file. By default, it resides in
        /etc/openlmi/${provider_prefix}/${provider_prefix}.conf.

        There should be only one instance of this class.
    """

    #: Allow to access global configuration object also from lmi.providers
    #: subpackage where ``get_instance()`` can not be used.
    #: This variable shall be set in ``__init__()`` method.
    INSTANCE = None
    CONFIG_DIRECTORY_TEMPLATE_TOPLEVEL = '/etc/openlmi/'
    CONFIG_DIRECTORY_TEMPLATE_PROVIDER = '/etc/openlmi/%(provider_prefix)s/'
    CONFIG_FILE_PATH_TEMPLATE_TOPLEVEL = \
            CONFIG_DIRECTORY_TEMPLATE_TOPLEVEL + 'openlmi.conf'
    CONFIG_FILE_PATH_TEMPLATE_PROVIDER = \
            CONFIG_DIRECTORY_TEMPLATE_PROVIDER + '%(provider_prefix)s.conf'

    PERSISTENT_PATH_TEMPLATE = '/var/lib/openlmi-%(provider_prefix)s/'
    SETTINGS_DIR = 'settings/'

    DEFAULT_OPTIONS = {
        'Namespace'       : 'root/cimv2',
        'SystemClassName' : 'PG_ComputerSystem',
        # Default logging level
        "Level"           : "ERROR",
        'DebugBlivet'     : 'false',
        'Stderr'          : 'false',
    }

    @classmethod
    def provider_prefix(cls):
        """
        This is responsibility of a subclass.

        :rtype: (``string`) Prefix of providers in lowercase. For example
            configuration class for storage providers would return "storage".

        Result is used to construct configuration paths.
        """
        raise NotImplementedError

    @classmethod
    def default_options(cls):
        """ :rtype: (``dict``) Dictionary of default values. """
        return cls.DEFAULT_OPTIONS

    @classmethod
    def config_directory_toplevel(cls):
        """ Base directory with toplevel configuration settings. """
        return cls.CONFIG_DIRECTORY_TEMPLATE_TOPLEVEL

    @classmethod
    def config_directory_provider(cls):
        """ Base directory with provider specific configuration settings. """
        return cls.CONFIG_DIRECTORY_TEMPLATE_PROVIDER % {
                'provider_prefix' : cls.provider_prefix() }


    @classmethod
    def persistent_path(cls):
        """ Base directory with persistent settings. """
        return cls.PERSISTENT_PATH_TEMPLATE % {
                'provider_prefix': cls.provider_prefix() }

    @classmethod
    def config_file_path_toplevel(cls):
        """ File path of toplevel configuration file. """
        return cls.CONFIG_FILE_PATH_TEMPLATE_TOPLEVEL

    @classmethod
    def config_file_path_provider(cls):
        """ File path of provider specific configuration file. """
        return cls.CONFIG_FILE_PATH_TEMPLATE_PROVIDER % {
                'provider_prefix' : cls.provider_prefix() }


    @classmethod
    def mandatory_sections(cls):
        """
            Return list of sections, that must be present in configuration
            file. If not present, they will be created in memory.
        """
        return ['Log', 'CIM']

    def __init__(self):
        """ Initialize and load a configuration file."""
        self._listeners = set()
        self.config = ConfigParser.SafeConfigParser(
                defaults=self.default_options())
        self.load()
        BaseConfiguration.INSTANCE = self

    def add_listener(self, callback):
        """
            Add a callback, which will be called when configuration is updated.
            The callback will be called with instance of this class as
            parameter:
              callback(config)
        """
        self._listeners.add(callback)

    def remove_listener(self, callback):
        """
            Remove previously registered callback.
        """

        self._listeners.remove(callback)

    def _call_listeners(self):
        """
            Call all listeners that configuration has updated.
        """
        for callback in self._listeners:
            callback(self)

    def load(self):
        """
            Load configuration from config files. Provider specific options
            overrides toplevel openlmi configuration.
            The files do not need to exist.
        """
        self.config.read([self.config_file_path_toplevel(), self.config_file_path_provider()])
        for section in self.mandatory_sections():
            if not self.config.has_section(section):
                self.config.add_section(section)
        self._call_listeners()

    @property
    def namespace(self):
        """ Return namespace of OpenLMI provider. """
        return self.config.get('CIM', 'Namespace')

    @property
    def system_class_name(self):
        """ Return SystemClassName of OpenLMI provider. """
        return self.config.get('CIM', 'SystemClassName')

    @property
    def logging_level(self):
        """ Return name of logging level in lower case. """
        return self.config.get('Log', 'Level').lower()

    @property
    def stderr(self):
        """ Return True if logging to stderr is enabled. """
        return self.config.getboolean('Log', 'Stderr')

    def file_path(self, section, option):
        """
        Return absolute file path for requested option.
        Relative path is converted to absolute one with config's directory
        as a prefix.
        """
        path = self.config.get(section, option)
        if not os.path.isabs(path):
            path = os.path.join(self.config_directory_provider(), path)
        return path

    def get_safe(self, section, option, convert=str, fallback=None,
            *args, **kwargs):
        """
        Get the configuration option value as specified type in a safe way.
        Value is searched in this order:
            config_file -> defaults_dict -> fallback

        :param section: (``str``) Section name of option.
        :param option: (``str``) Option name.
        :param convert: (``type``) Is a conversion function for obtained
            value. If the value could not be converted, error message is
            generated and ``fallback`` is returned. This function is not
            applied to ``fallback`` value. Supported values are:
                str, unicode, int ,float, long, bool

        :param fallback: Value returned, when section or option does not
            exists and no default value is given, or when the obtained value
            could not be converted by supplied function.

        All the other parameters are passed to the ``SafeConfigParser.get()``
        method.
        """
        if not isinstance(section, basestring):
            raise TypeError('section must be a string')
        if not isinstance(option, basestring):
            raise TypeError("option must be a string")
        if not convert in (str, unicode, int, float, long, bool):
            raise ValueError("unsupported type for conversion: %s:",
                    getattr(convert, '__name__', 'unknown'))
        if (   not self.config.has_option(section, option)
           and not option.lower() in self.default_options()):
            logging.getLogger(__name__).warn(
                    'no option value and no default supplied for "[%s]%s"',
                    section, option)
            return fallback
        try:
            value = self.config.get(section, option, *args, **kwargs)
        except ConfigParser.Error as exc:
            logging.getLogger(__name__).error(
                    'failed to get value of "[%s]%s": %s', section, option,
                    exc)
            return fallback
        try:
            # first try to convert value from config
            return convert_value(section, option, convert, value)
        except ValueError as exc:
            logging.getLogger(__name__).error(
                    'failed to convert value of "[%s]%s: %s', section, option,
                    exc)
            # if it failes, try the value from defaults
            if (   option.lower() in self.default_options()
               and self.default_options()[option.lower()] != value):
                try:
                    return convert_value(section, option, convert,
                            self.default_options()[option.lower()])
                except ValueError:
                    pass    # error is already logged, no more options left
            return fallback
