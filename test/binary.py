# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_binary(unittest.TestCase):
    def test_turns_multiple_argument_function_into_binary_one(self):
        def function(*arguments):
            x, y, z, *_ = *arguments, None, None, None
            eq(self, len(arguments), 2)
            eq(self, z, None)
        R.binary(function)(10, 20, 30)

    def test_initial_arguments_are_passed_through_normally(self):
        def function(*arguments):
            x, y, z, *_ = *arguments, None, None, None
            eq(self, x, 10)
            eq(self, y, 20)
            assert z is None
        R.binary(function)(10, 20, 30)


if __name__ == '__main__':
    unittest.main()
