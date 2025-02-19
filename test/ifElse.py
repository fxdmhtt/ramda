# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest
import numbers

class Test_ifElse(unittest.TestCase):
    def setUp(self):
        self.t = lambda a: a + 1
        self.identity = lambda a: a
        self.isArray = lambda a: isinstance(a, (list, tuple))

    def test_calls_the_truth_case_function_if_the_validator_returns_a_truthy_value(self):
        v = lambda a: isinstance(a, numbers.Number)
        eq(self, R.ifElse(v, self.t, self.identity)(10), 11)

    def test_calls_the_False_case_function_if_the_validator_returns_a_falsy_value(self):
        v = lambda a: isinstance(a, numbers.Number)
        eq(self, R.ifElse(v, self.t, self.identity)('hello'), 'hello')

    def test_calls_the_True_case_on_array_items_and_the_False_case_on_non_array_items(self):
        list = [[1, 2, 3, 4, 5], 10, [0, 1], 15]
        arrayToLength = R.map(R.ifElse(self.isArray, len, self.identity))
        eq(self, arrayToLength(list), [5, 10, 2, 15])

    def test_passes_the_arguments_to_the_True_case_function(self):
        v = lambda *_: True
        def onTrue(a, b):
            eq(self, a, 123)
            eq(self, b, 'abc')
        R.ifElse(v, onTrue, self.identity)(123, 'abc')

    def test_passes_the_arguments_to_the_False_case_function(self):
        v = lambda *_: False
        def onFalse(a, b):
            eq(self, a, 123)
            eq(self, b, 'abc')
        R.ifElse(v, self.identity, onFalse)(123, 'abc')

    def test_returns_a_function_whose_arity_equals_the_max_arity_of_the_three_arguments_to_ifElse(self):
        a0 = lambda *_: 0
        a1 = lambda x: x
        a2 = lambda x, y: x + y

        eq(self, R.ifElse(a0, a1, a2).length, 2)
        eq(self, R.ifElse(a0, a2, a1).length, 2)
        eq(self, R.ifElse(a1, a0, a2).length, 2)
        eq(self, R.ifElse(a1, a2, a0).length, 2)
        eq(self, R.ifElse(a2, a0, a1).length, 2)
        eq(self, R.ifElse(a2, a1, a0).length, 2)

    def test_returns_a_curried_function(self):
        v = lambda a: isinstance(a, numbers.Number)
        ifIsNumber = R.ifElse(v)
        eq(self, ifIsNumber(self.t, self.identity)(15), 16)
        eq(self, ifIsNumber(self.t, self.identity)('hello'), 'hello')

        fn = R.ifElse(R.gt, R.subtract, R.add)
        eq(self, fn(2)(7), 9)
        eq(self, fn(2, 7), 9)
        eq(self, fn(7)(2), 5)
        eq(self, fn(7, 2), 5)


if __name__ == '__main__':
    unittest.main()
