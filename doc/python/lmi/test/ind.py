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
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301 USA
#
# Authors: Alois Mahdal <amahdal@redhat.com>
#
"""
LMI indication testing framework
"""

import os
import string
import time

import lmi.shell
import lmi.test.util
import lmi.test.lmibase


class IndicationStreamTestCase(lmi.test.lmibase.LmiTestCase):
    """
    Base class for indication test cases with helper methods.

    This class is intended to be used as base for new test
    cases that are testing indications.  It provides utility
    methods to simplify definifion of test cases and reduce
    code repetition.

    Also provides mechanism to set defaults for driver options.
    Set cls.default_driver_options for hardcoded defaults per
    test case class.  These can be overrided on runtime by
    environment variables as defined in import_driver_options,
    and furthermore in each test case, by updating
    driver_options property.

    driver_default_argset can be set in similar manner (save
    for ENV), although it's not recommended to make extensive
    use of these; most of the time it's better to be explicit
    or use driver options instead.
    """

    # what to use as default options
    # override this as self.driver_options in your
    # subclassed testcase or as ENV variables
    default_driver_options = {
        'listener_host': 'localhost',
        'listener_port': 12000,
        'delay_action': 0.1,
        'delay_chillout': 5,
        'gen_prefix': 'lmi_test_ind_',
        'gen_strength': 10,
    }

    # what to import, where in options and what handler to use
    # for conversion to proper format
    import_driver_options = [
        ("LMI_IND_DELAY_CHILLOUT", 'delay_chillout', float),
        ("LMI_IND_DELAY_ACTION", 'delay_action', float),
        ("LMI_IND_GEN_PREFIX", 'gen_prefix', str),
        ("LMI_IND_GEN_STRENGTH", 'gen_strength', int),
        ("LMI_IND_LISTENER_HOST", 'listener_host', str),
        ("LMI_IND_LISTENER_PORT", 'listener_port', int),
    ]

    def setUp(self):
        self.set_driver_options()
        self.set_driver_default_argset()
        self.driver_options['conn'] = self.conn
        self.driver_default_argset['name'] = self._testMethodName

    def assertExpectedSIStream(self, probe, case):
        """
        Assert correct sequence of SourceInstances was delivered.

        Uses probe interface to obtain description of
        SourceInstance class names delivered and compares that
        to value under expected_si_stream key of the case
        argument.
        """
        es = case['expected_si_stream']
        oracle = lmi.test.util.PackedSequence.normalize(es)
        result = probe.describe_source_instance_stream()
        msg = ("Expected source instances not delivered:\n"
               "..subscriptions:                %r\n"
               "..triggered actions:            %r\n"
               "..expected source instances:    %r\n"
               "..got:                          %r\n"
               % (case['subscriptions'], probe.describe_actions(),
                  oracle, result))
        assert result == oracle, msg

    def assertExpectedIndStream(self, probe, case):
        """
        Assert correct sequence of indication classes was delivered.

        Uses probe interface to obtain description of class
        names delivered and compares that to value under
        expected_ind_stream key of the case argument.
        """
        es = case['expected_ind_stream']
        oracle = lmi.test.util.PackedSequence.normalize(es)
        result = probe.describe_indication_stream()
        msg = ("Expected indications not delivered:\n"
               "..subscriptions:                %r\n"
               "..triggered actions:            %r\n"
               "..expected indications:         %r\n"
               "..got:                          %r\n"
               % (case['subscriptions'], probe.describe_actions(),
                  oracle, result))
        assert result == oracle, msg

    def execute(self, case):
        """
        Just instantiate new driver and run it with case data.

        Instantiate self.driver_class with self.driver_options
        and self.driver_default_argset, and call its run method,
        returning the result untouched.

        This constitutes preferred scenario of how the drivers
        should be used, i.e. one throw-away instance per each
        test case.
        """
        drv = self.driver_class(self.driver_options,
                                self.driver_default_argset)
        return drv.run(case)

    def mknumcase(self, counts, names):
        """
        Construct case based on numbers of events/suscriptions.

        This is to support scenarios when you want to create
        test cases automatically, and you are only interested
        in number (possibly zero) of events, or relevant
        subscriptions and handlers.

        For example, you want to check that with M handlers,
        N subscriptions and P actions, Q indications are
        generated.  I.e. you only want to define the numbers,
        not whole cases.
        """
        c_hans, c_subs, c_acts, c_expect = counts
        action, ind, si = names
        return {
            'handlers': '%dpr' % c_hans,
            'subscriptions': '%d%s' % (c_subs, action),
            'actions': '%d%s' % (c_acts, action),
            'expected_ind_stream': "%d%s" % (c_expect, ind),
            'expected_si_stream': "%d%s" % (c_expect, si),
        }

    def set_driver_default_argset(self):
        """
        Set driver default argset from class defaults
        """
        self.driver_default_argset = {}
        if hasattr(self, "default_driver_default_argset"):
            self.driver_default_argset.update(
                self.default_driver_default_argset.copy())

    def set_driver_options(self):
        """
        Set driver options from class defaults and ENV
        """
        self.driver_options = {}
        # 1. class default
        if hasattr(self, "default_driver_options"):
            self.driver_options.update(self.default_driver_options.copy())
        # 2. import from ENV
        if hasattr(self, "import_driver_options"):
            for envkey, optkey, convert in self.import_driver_options:
                if envkey in os.environ:
                    self.driver_options[optkey] = convert(os.environ[envkey])


class IndicationTestStub(object):
    """
    Test stub - imitation of a system called by OpenLMI
    """

    @staticmethod
    def probe_report(ind, probe, *args, **kwargs):
        probe.report_indication(ind, args, kwargs)


class IndicationTestProbe(object):
    """
    Hold details about actions trigerred and indications seen.

    Provides methods to be called from listener handler, to
    allow for tracking what indications were seen and when, and
    by action trigger, to track when event was triggered.

    These reports can then be queried by get_* methods, to help
    make assertions and report discrepancies.
    """

    class _ActionReport(object):

        def __init__(self, action, rv):
            self.time = time.time()
            self.action = action
            self.rv = rv

        def __cmp__(self, other):
            return cmp(self.time, other.time)

    class _IndicationReport(object):

        def __init__(self, ind, args, kwargs):
            self.time = time.time()
            self.ind = ind
            self.args = args
            self.kwargs = kwargs

        def __cmp__(self, other):
            a = self.ind['IndicationTime']
            b = other.ind['IndicationTime']
            return cmp(a, b)

    def __init__(self):
        self.indication_reports = []
        self.action_reports = []
        self.classname_aliases = {}

    def _tryalias(self, classname):
        """
        Give classname alias if exists, otherwise return classname.
        """
        try:
            return self.classname_aliases[classname]
        except KeyError:
            return classname

    def describe_actions(self):
        """
        Describe stream of actions (triggered and) logged to probe.

        Return string describing sequence of action names found
        in probe reports, sorted in order as they were triggered.
        Description is created using lmi.test.util.PackedSequence
        and the names in known_actions.
        """
        ps = lmi.test.util.PackedSequence()
        [ps.append(r.action) for r in sorted(self.action_reports)]
        return str(ps)

    def describe_indication_stream(self):
        """
        Describe stream of CIM indications delivered to probe.

        Return string describing sequence of all indications
        from all probe reports.

        Description is created using lmi.test.util.PackedSequence
        and if aliases are defined for class names, those are
        used instead of full names.  Items are sorted by time
        embedded in the indication (IndicationTime).
        """
        ps = lmi.test.util.PackedSequence()
        for i in self.get_indications(sort=True):
            ps.append(self._tryalias(i.classname))
        return str(ps)

    def describe_source_instance_stream(self):
        """
        Describe stream of SourceInstances delivered to probe.

        Return string describing sequence of SourceInstances from
        indications from all probe reports.

        Description is created using lmi.test.util.PackedSequence
        and if aliases are defined for class names, those are
        used instead of full names.  Items are sorted by time
        embedded in the enclosing indication (IndicationTime).
        """
        ps = lmi.test.util.PackedSequence()
        for si in self.get_source_instances(sort=True):
            ps.append(self._tryalias(si.classname))
        return str(ps)

    def get_indications(self, sort=False):
        """
        Get CIM indications delivered to probe.

        Return sequence of all indications from all probe
        reports.  If sort is true, items are sorted by time
        embedded in the indication (IndicationTime).
        """
        irs = (sorted(self.indication_reports)
               if sort else self.indication_reports)
        for ir in irs:
            yield ir.ind

    def get_source_instances(self, sort=False):
        """
        Get SourceInstances delivered to probe.

        Return sequence of all SourceInstances from all probe
        reports.  If sort is true, items are sorted by time
        embedded in the enclosing indication (IndicationTime).
        """
        irs = (sorted(self.indication_reports)
               if sort else self.indication_reports)
        for ir in irs:
            yield ir.ind['SourceInstance']

    def report_indication(self, ind, args, kwargs):
        r = self._IndicationReport(ind, args, kwargs)
        self.indication_reports.append(r)

    def report_action(self, action, rv):
        r = self._ActionReport(action, rv)
        self.action_reports.append(r)


class IndicationTestDriver(lmi.test.util.BaseTestDriver):
    """
    Test Driver for OpenLMI Indications.

    This driver wraps common "correct" scenario to register
    indications and listener and triggering actions of interest.
    It then allows running the scenario with arbitrary
    variations of what sequence of events is triggered and what
    is expected.

    To make use of the driver, subclass it and in __init__, add
    your queries, handlers and actions to respective
    self.known_* dictionaries.  Keys under which you add them
    become "aliases", which you then use when describing the
    test case.

    Behavior inherited by lmi.test.util.BaseTestDriver is that
    test case is described by a dict argument passed to run().
    Eventually _do_run() is called, where your implementation
    refers to above as self.argset.

    This implementation of _do_run expects following values
    passed as options when instantiating:

    *   'listener_host' and 'listener_port', hostname/ip/port
         where listener should be started; this is also where
         subscriptions are directed.

    *   'delay_action'/'delay_chillout', delay between each
        triggered action, and after last action, respectively.

    *   'gen_prefix'/'gen_strength', whenever driver needs to
        "make up" own name e.g. for username, it will use this
        prefix, and add this number of random ASCII characters.

    and following in the argset dictionary when calling run():

    *   'name' - a short descriptive name to be used to
        construct handler and subsctiption names; aim is
        basically to help in case of debugging

    rest of them have special format to be used with
    `PackedSequence`:

    *   'subscriptions' describes list of subscriptions to
        register; these are currently only WQL queries; the
        rest of subscription parameters is inferred from
        options or left to default

    *   'handlers' describes list of handlers to pair with
        subscriptions.

        This is optional. By default each subscription will be
        paired with simple reporting handler that only passes
        indication to the probe, so it should  suffice in most
        cases.  However, if you specify this  argument, you
        need to ensure mapping to subscription works as you
        want, i.e. you normally want to specify same amount of
        handlers as subscriptions.

    *   'actions' describes sequence of events to be triggered,
        such as creation of account or installation of a
        software package or whatever you have provided in
        known_actions.

    Return value of run() is a IndicationTestProbe instance that
    contains records of all important events and contains helper
    methods, to query these, so that assertions can be made to
    complete the test.

    """

    def __init__(self, *args, **kwargs):
        super(IndicationTestDriver, self).__init__(*args, **kwargs)

        # create essential objects
        self.probe = IndicationTestProbe()
        self.listener = lmi.shell.LMIIndicationListener(
            self.options['listener_host'],
            self.options['listener_port'])
        self.known_queries = {}
        self.known_handlers = {}
        self.known_actions = {}

        # register cleanup handlers
        uai = self.options['conn'].unsubscribe_all_indications
        self.cleanup_handlers.append(uai)
        self.cleanup_handlers.append(self.listener.stop)

        # add basic handler
        self.known_handlers['pr'] = IndicationTestStub.probe_report

        # add basic actions
        self.known_actions['SL1'] = lambda: time.sleep(1)
        self.known_actions['SL2'] = lambda: time.sleep(2)
        self.known_actions['SL5'] = lambda: time.sleep(5)

    def _prepare_handlers(self):
        """Create listener, add handlers and start listener"""
        hnames = []
        prefix = self.argset['name'] + "_"
        chars = filter(lambda c: c != 'X',
                       string.ascii_letters + string.digits)
        for h in lmi.test.util.PackedSequence(self.argset['handlers']):
            name = lmi.test.util.random_string(prefix=prefix, chars=chars)
            fn = self.known_handlers[h]
            hname = self.listener.add_handler(name, fn, self.probe, name)
            hnames.append(hname)
        self.hnames = hnames

    def _prepare_subscriptions(self):
        """Register all subscriptions"""

        dest = "http://%(listener_host)s:%(listener_port)s" % self.options

        def getname():
            """Pop from handler names or make up new"""
            try:
                return self.hnames.pop()
            except IndexError:
                prefix = "_orphan_%s_" % sub
                return lmi.test.util.random_string(prefix=prefix)

        for sub in lmi.test.util.PackedSequence(self.argset['subscriptions']):
            rval = self.options['conn'].subscribe_indication(
                Query=self.known_queries[sub],
                Name=getname(),
                Destination=dest
            )
            assert rval.rval, "subscribing indication failed"

    def _trigger_actions(self):

        actions = lmi.test.util.PackedSequence(self.argset['actions'])

        for action in actions:
            if action not in self.known_actions:
                raise ValueError("unknown action in sequence: " + action)
            rv = self.known_actions[action]()
            self.probe.report_action(action, rv)
            time.sleep(self.options['delay_action'])

    def _do_run(self):
        self._prepare_handlers()
        self._prepare_subscriptions()
        self.listener.start()
        self._trigger_actions()
        time.sleep(self.options['delay_chillout'])
        return self.probe
