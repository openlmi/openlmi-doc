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


class LMISubscription(object):
    """
    Class holding information about a indication subscription.

    :param LMIShellClient client: client object used for CIMOM communication
    :param tuple cim_filter: contains filter object and bool indicator,
        if the filter object was created temporarily
    :param tuple cim_handler: contains handler object and bool indicator,
        if the handler object was created temporarily
    :param cim_subscription: subscription object
    :param bool permanent: indicates, if the indication should be deleted on
        the LMIShell's quit
    """
    def __init__(self, client, cim_filter, cim_handler, cim_subscription,
                 permanent):
        self._client = client
        self._cim_filter_tpl = cim_filter
        self._cim_handler_tpl = cim_handler
        self._cim_subscription = cim_subscription
        self._permanent = permanent

    def delete(self):
        """
        Cleans up the indication subscription.

        First it deletes subscription object. If
        :py:attr:`.LMISubscription._cim_filter_tpl` contains a flag, that the
        filter object was created temporarily, it will be deleted by this call.
        If :py:attr:`.LMISubscription._cim_handler_tlp` contains an flag, that
        the handler object was created temporarily, it will be deleted as well.

        This is called from :py:class:`.LMIConnection` object, which holds an
        internal list of all subscribed indications by the LMIShell (if not
        created by hand).
        """
        self._client.delete_instance(self._cim_subscription.path)
        if self._cim_filter_tpl[1]:
            self._client.delete_instance(self._cim_filter_tpl[0].path)
        if self._cim_handler_tpl[1]:
            self._client.delete_instance(self._cim_handler_tpl[0].path)

    @property
    def permanent(self):
        return self._permanent
