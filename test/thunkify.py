# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest
from ..source.internal import jsify

class Test_thunkify(unittest.TestCase):
    def test_returns_a_function_with_the_same_arity_as_the_given_function(self):
        input = jsify(lambda a0, a1: None)
        thunk = R.thunkify(input)
        self.assertTrue(callable(thunk))
        eq(self, thunk.length, input.length)

    def test_returns_a_function_that_expects_arguments_and_returns_a_new_invoker_function(self):
        input = jsify(lambda a0, a1: None)
        thunk = R.thunkify(input)
        self.assertTrue(callable(thunk(42, 'xyz')))

    def test_calls_the_original_function_with_the_provided_arguments_when_all_were_supplied(self):
        thunk = R.thunkify(R.add(2))
        eq(self, thunk(40)(), 42)


if __name__ == '__main__':
    unittest.main()
