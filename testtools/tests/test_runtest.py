# Copyright (c) 2009 Jonathan M. Lange. See LICENSE for details.

"""Tests for the RunTest single test execution logic."""

import unittest

from testtools import (
    RunTest,
    TestCase,
    TestResult,
    )
from testtools.tests.helpers import (
    LoggingResult,
    Python26TestResult,
    Python27TestResult,
    ExtendedTestResult,
    )


class TestRunTest(TestCase):
    
    def test___init__(self):
        run = RunTest("bar", "foo")
        self.assertEqual(run.case, "bar")
        # to transition code we pass the existing run logic into RunTest.
        self.assertEqual(run.wrapped, "foo")

    def test___call__(self):
        # run() invokes wrapped
        log = []
        run = RunTest(self, lambda x:log.append('foo'))
        run()
        self.assertEqual(['foo'], log)

    def test___call___with_result(self):
        # run() invokes wrapped
        log = []
        run = RunTest("bar", lambda x:log.append(x))
        run('foo')
        self.assertEqual(['foo'], log)

    def test___call___no_result_manages_new_result(self):
        log = []
        run = RunTest(self, lambda x:log.append(x) or x)
        result = run()
        self.assertEqual(1, len(log))
        self.assertIsInstance(log[0], TestResult)
        self.assertEqual(result, log[0])


def test_suite():
    from unittest import TestLoader
    return TestLoader().loadTestsFromName(__name__)
