# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_takeLastWhile(unittest.TestCase):
    def test_continues_taking_elements_while_the_function_reports_True(self):
        eq(self, R.takeLastWhile(lambda x: x != 5, [1, 3, 5, 7, 9]), [7, 9])

    def test_starts_at_the_right_arg_and_acknowledges_None(self):
        def function():
            self.fail()
        eq(self, R.takeLastWhile(function, []), [])
        eq(self, R.takeLastWhile(lambda x: bool(x), [1, 3, None, 5, 7]), [5, 7])

    def test_can_operate_on_strings(self):
        eq(self, R.takeLastWhile(lambda x: x != 'R', 'Ramda'), 'amda')


if __name__ == '__main__':
    unittest.main()
