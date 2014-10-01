# Copyright (C) 2012-2014 Peter Hatina <phatina@redhat.com>
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

from lmi.shell.compat import *

from lmi.shell.LMIObjectFactory import LMIObjectFactory

# NOTE: the enumeration comes from DMTF standard.
JOB_STATE_COMPLETED, \
    JOB_STATE_TERMINATED, \
    JOB_STATE_KILLED, \
    JOB_STATE_EXCEPTION = range(7, 11)

# Job finish states are used in
# LMIMethod.__handle_synchro_method_call_indication()
#    JOB_FINISH_DELAYED -- a job has completed its action later,
#       an indication or polling method was used
#    JOB_FINISHED_EARLY -- no waiting method was used
JOB_NOT_FINISHED, \
    JOB_FINISH_DELAYED, \
    JOB_FINISH_EARLY = range(3)


def _lmi_get_job_state(job):
    """
    Helper function, which returns a numeric Job state value.

    :param job: :py:class:`.LMIInstance` or :py:class:`wbem.CIMInstance`
        representing a job
    """
    if isinstance(job, LMIObjectFactory().LMIInstance):
        return job.JobState
    elif isinstance(job, wbem.CIMInstance):
        return job["JobState"]
    raise TypeError("'job' object needs to be instance of either LMIInstance "
                    "or CIMInstance")


def lmi_is_job_finished(job):
    """
    Helper function, which returns bool flag, if the job is in finished state.

    :param job: :py:class:`.LMIInstance` or :py:class:`wbem.CIMInstance`
        representing a job
    """
    return _lmi_get_job_state(job) in (
        JOB_STATE_COMPLETED,
        JOB_STATE_TERMINATED,
        JOB_STATE_KILLED,
        JOB_STATE_EXCEPTION)


def lmi_is_job_completed(job):
    """
    Helper function, which returns bool flag, if the job is in completed state.

    :param job: :py:class:`.LMIInstance` or :py:class:`wbem.CIMInstance`
        representing a job
    """
    return _lmi_get_job_state(job) == JOB_STATE_COMPLETED


def lmi_is_job_terminated(job):
    """
    Helper function, which returns bool flag, if the job is in terminated
    state.

    :param job: :py:class:`.LMIInstance` or :py:class:`wbem.CIMInstance`
        representing a job
    """
    return _lmi_get_job_state(job) == JOB_STATE_TERMINATED


def lmi_is_job_killed(job):
    """
    Helper function, which returns bool flag, if the job is killed.

    :param job: :py:class:`.LMIInstance` or :py:class:`wbem.CIMInstance`
        representing a job
    """
    return _lmi_get_job_state(job) == JOB_STATE_KILLED


def lmi_is_job_exception(job):
    """
    Helper function, which returns bool flag, if the job is in the exception
    state.

    :param job: :py:class:`.LMIInstance` or :py:class:`wbem.CIMInstance`
        representing a job
    """
    return _lmi_get_job_state(job) == JOB_STATE_EXCEPTION
