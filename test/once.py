# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_once(unittest.TestCase):
    def test_returns_a_function_that_calls_the_supplied_function_only_the_first_time_called(self):
        ctr = 0
        def function(*_):
            nonlocal ctr
            ctr += 1
        fn = R.once(function)
        fn()
        eq(self, ctr, 1)
        fn()
        eq(self, ctr, 1)
        fn()
        eq(self, ctr, 1)

    def test_passes_along_arguments_supplied(self):
        fn = R.once(lambda a, b: a + b)
        result = fn(5, 10)
        eq(self, result, 15)

    def test_retains_and_returns_the_first_value_calculated_even_if_different_arguments_are_passed_later(self):
        ctr = 0
        def function(a, b):
            nonlocal ctr
            ctr += 1
            return a + b
        fn = R.once(function)
        result = fn(5, 10)
        eq(self, result, 15)
        eq(self, ctr, 1)
        result = fn(20, 30)
        eq(self, result, 15)
        eq(self, ctr, 1)

    def test_retains_arity(self):
        f = R.once(lambda a, b: a + b)
        eq(self, f.length, 2)


if __name__ == '__main__':
    unittest.main()
