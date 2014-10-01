# Copyright (C) 2013-2014 Michal Minar <miminar@redhat.com>
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.
"""
This module defines LmiCheckResult command class and related utilities.
"""

import abc

from lmi.scripts.common import Configuration
from lmi.scripts.common import get_logger
from lmi.scripts.common import formatter
from lmi.scripts.common import errors
from lmi.scripts.common.command import meta
from lmi.scripts.common.command.session import LmiSessionCommand

LOG = get_logger(__name__)

class LmiResultFailed(errors.LmiFailed):
    """
    Exception raised when associated function returns unexpected result. This
    is evaluated by :py:meth:`LmiCheckResult.check_result` method.
    """
    pass

def _make_result_failed(expected, result):
    """
    Instantiate :py:exc:`LmiResultFailed` exception with descriptive message
    composed of what was expected and what was returned instead.

    :rtype: :py:class:`LmiResultFailed`
    """
    return LmiResultFailed('failed (%s != %s)' % (repr(expected), repr(result)))

class LmiCheckResult(LmiSessionCommand):
    """
    Run an associated action and check its result. It implicitly makes no
    output if the invocation is successful and expected result matches.

    List of additional recognized properties:

        ``EXPECT`` :
            Value, that is expected to be returned by invoked associated
            function. This can also be a callable taking two arguments:

                1. options - Dictionary with parsed command line options
                   returned by ``docopt``.
                2. result - Return value of associated function.

    Using metaclass: :py:class:`~.meta.CheckResultMetaClass`.
    """
    __metaclass__ = meta.CheckResultMetaClass

    def __init__(self, *args, **kwargs):
        LmiSessionCommand.__init__(self, *args, **kwargs)

    def formatter_factory(self):
        return formatter.TableFormatter

    @abc.abstractmethod
    def check_result(self, options, result):
        """
        Check the returned value of associated function.

        :param dictionary options: Dictionary as returned by ``docopt`` parser
            after running
            :py:meth:`~.endpoint.LmiEndPointCommand.transform_options`.
        :param result: Any return value that will be compared against what is
            expected.
        :returns:  Whether the result is expected value or not. If ``tuple``
            is returned, it contains ``(passed_flag, error_description)``.
        :rtype: boolean or tuple.
        """
        raise NotImplementedError("check_result must be overriden in subclass")

    def take_action(self, connection, args, kwargs):
        """
        Invoke associated method and check its return value for single host.

        :param list args: List of arguments to pass to the associated
            function.
        :param dictionary kwargs: Keyword arguments to pass to the associated
            function.
        :returns: Exit code (0 on success).
        :rtype: integer
        """
        try:
            result = self.execute_on_connection(connection, *args, **kwargs)
            passed = self.check_result(self._options, result)
            if isinstance(passed, tuple):
                if len(passed) != 2:
                    raise errors.LmiUnexpectedResult('check_result() must'
                        ' return either boolean or (passed_flag,'
                        ' error_description), not "%s"' % repr(passed))
                if not passed[0]:
                    raise LmiResultFailed(passed[1])
            elif not passed and hasattr(self.check_result, 'expected'):
                err = _make_result_failed(self.check_result.expected, result)
                raise err
        except LmiResultFailed:
            raise
        except Exception as err:
            LOG().debug("Failed to execute wrapped function.", exc_info=err)
            raise
        return 0

    def process_host_result(self, hostname, success, result):
        pass

    def process_session_results(self, session, results):
        if len(self.session) > 1:
            LOG().debug('Successful runs: %d\n',
                    len([r for r in results.values() if r[0]]))
        LmiSessionCommand.process_session_results(self, session, results)
