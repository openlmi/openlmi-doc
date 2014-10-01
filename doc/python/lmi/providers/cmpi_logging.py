# -*- Coding:utf-8 -*-
#
# Copyright (C) 2012-2014 Red Hat, Inc.  All rights reserved.
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
"""
Contains handlers and loggers specific to providers logging running
under cimom.
"""

import logging
import functools
import inspect
from itertools import chain
import os
import sys

# Custom logging levels
TRACE_WARNING = logging.DEBUG - 1
TRACE_INFO = logging.DEBUG - 2
TRACE_VERBOSE = logging.DEBUG - 3

#: Mapping from level name to its number.
LOGGING_LEVELS = {
        "critical"      : logging.CRITICAL,
        "error"         : logging.ERROR,
        "warning"       : logging.WARNING,
        "warn"          : logging.WARNING,
        "info"          : logging.INFO,
        "debug"         : logging.DEBUG,
        "trace_warning" : TRACE_WARNING,
        "trace_info"    : TRACE_INFO,
        "trace_verbose" : TRACE_VERBOSE
}

#: This associates special format strings to various logger names
SPECIAL_FORMAT_STRINGS = {
    "lmi.providers.cmpi_logging.trace_function_or_method" :
            "%(levelname)s:%(message)s"
}

#: Default format string to use in stderr and cmpi handlers.
DEFAULT_FORMAT_STRING = \
    "%(levelname)s:%(module)s:%(funcName)s:%(lineno)d - %(message)s"

class DispatchingFormatter(object):
    """
    Formatter class for logging module. It allows to predefine different
    format string for paricular module names.

    There is no way, how to setup this formatter in configuration file.
    """
    def __init__(self, formatters, default):
        """
        *format* in parameters description can be either ``string`` or
        another formatter object.

        :param formatters (``dict``) Mapping of module names to *format*.
        :param default Default *format*.
        """
        for k, formatter in formatters.items():
            if isinstance(formatter, basestring):
                formatters[k] = logging.Formatter(formatter)
        self._formatters = formatters
        if isinstance(default, basestring):
            default = logging.Formatter(default)
        self._default_formatter = default

    def format(self, record):
        """
        Interface for logging module.
        """
        formatter = self._formatters.get(record.name, self._default_formatter)
        return formatter.format(record)

class CMPILogHandler(logging.Handler):
    """
        A handler class, which sends log messages to CMPI log.
    """

    def __init__(self, cmpi_logger, *args, **kwargs):
        self.cmpi_logger = cmpi_logger
        logging.Handler.__init__(self, *args, **kwargs)

    def emit(self, record):
        msg = self.format(record)
        if record.levelno >= logging.ERROR:
            self.cmpi_logger.log_error(msg)
        elif record.levelno >= logging.WARNING:
            self.cmpi_logger.log_warn(msg)
        elif record.levelno >= logging.INFO:
            self.cmpi_logger.log_info(msg)
        elif record.levelno >= logging.DEBUG:
            self.cmpi_logger.log_debug(msg)
        elif record.levelno >= TRACE_WARNING:
            self.cmpi_logger.trace_warn(record.filename, msg)
        elif record.levelno >= TRACE_INFO:
            self.cmpi_logger.trace_info(record.filename, msg)
        elif record.levelno >= TRACE_VERBOSE:
            self.cmpi_logger.trace_verbose(record.filename, msg)

class CMPILogger(logging.getLoggerClass()):
    """
        A logger class, which adds trace_method level log methods.
    """
    def trace_warn(self, msg, *args, **kwargs):
        """ Log message with TRACE_WARNING severity. """
        self.log(TRACE_WARNING, msg, *args, **kwargs)

    def trace_info(self, msg, *args, **kwargs):
        """ Log message with TRACE_INFO severity. """
        self.log(TRACE_INFO, msg, *args, **kwargs)

    def trace_verbose(self, msg, *args, **kwargs):
        """ Log message with TRACE_VERBOSE severity. """
        self.log(TRACE_VERBOSE, msg, *args, **kwargs)

    def _log(self, level, msg, args, exc_info=None, extra=None):
        """
        Overrides ``_log()`` function of basic ``Logger``. The purpose is to
        log tracebacks with different level instead of ERROR to prevent them
        being logged to syslog.
        """
        if logging._srcfile:
            #IronPython doesn't track Python frames, so findCaller throws an
            #exception on some versions of IronPython. We trap it here so that
            #IronPython can use logging.
            try:
                fn, lno, func = self.findCaller()
            except ValueError:
                fn, lno, func = "(unknown file)", 0, "(unknown function)"
        else:
            fn, lno, func = "(unknown file)", 0, "(unknown function)"
        if exc_info:
            if not isinstance(exc_info, tuple):
                exc_info = sys.exc_info()
            record = self.makeRecord(self.name, level, fn, lno, msg, args,
                    None, func, extra)
            self.handle(record)
            record = self.makeRecord(self.name, TRACE_WARNING, fn,
                    lno, str(exc_info[1]), tuple(), exc_info, func, extra)
        else:
            record = self.makeRecord(self.name, level, fn, lno, msg,
                    args, exc_info, func, extra)
        self.handle(record)

logging.setLoggerClass(CMPILogger)

def render_value(val):
    """
    When logging values, we want to avoid excessively long messages caused
    by rendering argument values like lists, dictionaries etc.
    Let's shorten these iterable objects to just one or few items.

    :param val: Any value for rendering.
    :returns: Representation string of value, possibly shortened.
    :rtype: string
    """
    if isinstance(val, list):
        if len(val) < 2:
            return repr(val)
        else:
            return "[%s, ... (%d more items)]" % (
                    render_value(val[0]), len(val) - 1)
    elif isinstance(val, dict):
        if len(val) < 2:
            return repr(val)
        else:
            key = next(iter(val))
            return '{%s: %s, ... (%d more items)}' % (
                    render_value(key), render_value(val[key]), len(val) - 1)
    elif isinstance(val, set):
        if len(val) < 2:
            return repr(val)
        else:
            return '{%s, ... (%d more items)}' % (
                    render_value(val[0]), len(val) - 1)
    elif isinstance(val, tuple):
        return "(%s%s)" % (
                ", ".join(render_value(i) for i in val),
                ", " if len(val) < 2 else '')
    return repr(val)

def _trace_function_or_method(is_method=False, frame_level=1):
    """
    Factory for function and method decorators. Generated decorators
    log every calls and exits of decorated functions or methods.

    Logged information contain the caller's module and line together with
    called function's module, function name and line number.

    :param boolean is_method: Whether returned decorator is targeted
        for use upon a method of a class. It modified logged function by
        prepending owning class name.
    :param integer frame_level: Number of nested frames to skip when
        searching for called function scope by inspecting stack upwards.
        When the result of this function is applied directly on the definition
        of function, it's value should be 1. When used from inside of some
        other factory, it must be increased by 1.
    """

    assert frame_level >= 1

    def _decorator(func):
        """
        Decorator for logging entries and exits of function or method.
        """
        if not inspect.ismethod(func) and not inspect.isfunction(func):
            raise TypeError("func must be a function")

        module = func.__module__.split('.')[-1]
        frm = inspect.currentframe()
        for _ in range(frame_level):
            frm = frm.f_back
        lineno = frm.f_lineno
        del frm
        classname = inspect.getouterframes(
                inspect.currentframe())[frame_level][3]

        @functools.wraps(func)
        def _wrapper(*args, **kwargs):
            """
            Wrapper for function or method, that does the logging.
            """
            logger = logging.getLogger(__name__+'.trace_function_or_method')
            logargs = {}
            if logger.isEnabledFor(TRACE_VERBOSE):
                frm = inspect.currentframe()
                logargs.update({
                    "caller_file" : os.path.basename(os.path.splitext(
                        frm.f_back.f_code.co_filename)[0]),
                    "caller_lineno" : frm.f_back.f_lineno,
                    "module" : module,
                    "func"   : classname + "." + func.__name__
                        if is_method else func.__name__,
                    "lineno" : lineno,
                    "action" : "entering",
                    "args"   : ", ".join(chain(
                                (render_value(a) for a in args),
                                (   "%s=%s"%(k, render_value(v))
                                for k, v in kwargs.items())))
                })

                if not logargs["args"]:
                    logargs["args"] = ""
                else:
                    logargs["args"] = " with args=(%s)" % logargs["args"]
                logger.trace_verbose("%(caller_file)s:%(caller_lineno)d - "
                    "%(action)s %(module)s:%(func)s:%(lineno)d%(args)s",
                    logargs)
            try:
                result = func(*args, **kwargs)
                if logger.isEnabledFor(TRACE_VERBOSE):
                    logargs["action"] = "exiting"
                    logger.trace_verbose("%(caller_file)s:%(caller_lineno)d"
                        " - %(action)s %(module)s:%(func)s:%(lineno)d",
                        logargs)
            except Exception as exc:
                if logger.isEnabledFor(TRACE_VERBOSE):
                    logargs['action'] = 'exiting'
                    logargs['error'] = str(exc)
                    logger.trace_verbose("%(caller_file)s:%(caller_lineno)d"
                        " - %(action)s %(module)s:%(func)s:%(lineno)d"
                        " with error: %(error)s", logargs)
                raise
            return result

        return _wrapper

    return _decorator

def _trace_function(func, frame_level=1):
    """ Convenience function used for decorating simple functions. """
    return trace_function_or_method(frame_level=frame_level + 1)(func)

def _trace_method(func, frame_level=1):
    """ Convenience function used for decorating methods. """
    return trace_function_or_method(True, frame_level + 1)(func)

def _identity_decorator(func, *args, **kwargs):
    """ Decorator returning the function itself. """
    return func

# Tracing decorators may be disabled by environment variable.
if os.getenv("LMI_DISABLE_TRACING_DECORATORS", "0").lower() in \
        ("1", "true", "yes", "on"):
    # Tracing decators disabled. Functions and method won't get modified
    # in any way.
    trace_function_or_method = _identity_decorator
    trace_function           = _identity_decorator
    trace_method             = _identity_decorator
else:
    # Tracing decorators enabled.
    trace_function_or_method = _trace_function_or_method
    trace_function           = _trace_function
    trace_method             = _trace_method

def try_setup_from_file(config):
    """
    Try to configure logging with a file specified in configuration.

    :returns: ``True`` if the file configuration is given,  successfuly
        parsed and carried out.
    :rtype: boolean
    """
    try:
        path = config.file_path('Log', 'FileConfig')
        if not os.path.exists(path):
            logging.getLogger(__name__).error('given FileConfig "%s" does'
                    ' not exist', path)
        else:
            logging.config.fileConfig(path)
            return True
    except Exception:
        if config.config.has_option('Log', 'FileConfig'):
            logging.getLogger(__name__).exception(
                    'failed to setup logging from FileConfig')
    return False

def setup(env, config, special_format_strings=None):
    """
    Set up the logging with options stored in
    :py:class:`lmi.base.BaseConfiguration` instance. This should be called
    at provider's startup before any message is sent to log.

    :param ProviderEnvironment env: Provider environment, taken from CIMOM
        callback (e.g. ``get_providers()``).
    :param config:  Configuration with Log section containing settings for
        logging.
    :type config: :py:class:`lmi.base.BaseConfiguration`
    :param dictionary special_format_strings: Assignes to various loggers
        special format strings. It overrides pairs in
        :py:data:`SPECIAL_FORMAT_STRINGS`. Its format is following: ::

            { ( 'logger_name' : 'format_string_to_use' ), ... }
    """
    if (   special_format_strings is not None
       and not isinstance(special_format_strings, dict)):
        raise TypeError("special_format_strings must be a dictionary")
    if try_setup_from_file(config):
        return
    logging_level = logging.ERROR
    if not config.logging_level in LOGGING_LEVELS:
        logging.getLogger(__name__).error(
                'level name "%s" not supported', config.logging_level)
    else:
        logging_level = LOGGING_LEVELS[config.logging_level]
    logger = logging.getLogger()
    logger.setLevel(logging_level)
    # remove any previously set handlers
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    format_strings = SPECIAL_FORMAT_STRINGS.copy()
    if special_format_strings is not None:
        format_strings.update(special_format_strings)
    # set up new ones
    if config.stderr:
        err_handler = logging.StreamHandler()
        err_handler.setLevel(logging_level)
        err_handler.setFormatter(
                DispatchingFormatter(format_strings, DEFAULT_FORMAT_STRING))
        logger.addHandler(err_handler)
    cmpi_handler = CMPILogHandler(env.get_logger(), logging_level)
    cmpi_handler.setFormatter(
            DispatchingFormatter(format_strings, DEFAULT_FORMAT_STRING))
    logger.addHandler(cmpi_handler)

class LogManager(object):
    """
        Class, which takes care of CMPI logging.
        There should be only one instance of this class and it should be
        instantiated as soon as possible, even before reading a config.
        The config file can be provided later by set_config call.

        Use of this manager is an alternative to single call to ``setup()``
        function of this module.
    """

    def __init__(self, env):
        """
            Initialize logging.
        """
        self._env = env
        self._config = None

    @property
    def config(self):
        """ Provider configuration object. """
        return self._config
    @config.setter
    def config(self, config):
        """
            Set a configuration of logging. It applies its setting immediately
            and also subscribes for configuration changes.
        """
        self._config = config
        config.add_listener(self._config_changed)
        # apply the config
        self._config_changed(config)

    @property
    def cmpi_handler(self):
        """ Returns cmpi log handler passing logged messages to cimom. """
        for handler in logging.getLogger('').handlers:
            if isinstance(handler, CMPILogHandler):
                return handler
        return CMPILogHandler(self._env.get_logger())

    @trace_method
    def _config_changed(self, config):
        """
            Apply changed configuration, i.e. start/stop sending to stderr
            and set appropriate log level.
        """
        setup(self._env, config)

    def destroy(self):
        """
            Shuts down the logging framework. No logging can be done
            afterwards.
        """
        logging.getLogger(__name__).debug('shutting down logging')
        logging.shutdown()

def get_logger(module_name):
    """
    Convenience function for getting callable returning logger for particular
    module name. It's supposed to be used at module's level to assign its
    result to global variable like this:

        LOG = cmpi_logging.get_logger(__name__)

    This can be used in module's functions and classes like this:

        def module_function(param):
            LOG().debug("this is debug statement logging param: %s", param)

    Thanks to ``LOG`` being a callable, it always returns valid logger object
    with current configuration, which may change overtime.
    """
    def _logger():
        """ Callable used to obtain current logger object. """
        return logging.getLogger(module_name)
    return _logger
