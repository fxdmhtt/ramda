# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest
import numbers

class Test_when(unittest.TestCase):
    def test_calls_the_whenTrue_function_if_the_validator_returns_a_truthy_value(self):
        eq(self, R.when(R.is_(numbers.Number), R.add(1))(10), 11)

    def test_returns_the_argument_unmodified_if_the_validator_returns_a_falsy_value(self):
        eq(self, R.when(R.is_(numbers.Number), R.add(1))('hello'), 'hello')

    def test_returns_a_curried_function(self):
        ifIsNumber = R.when(R.is_(numbers.Number))
        eq(self, ifIsNumber(R.add(1))(15), 16)
        eq(self, ifIsNumber(R.add(1))('hello'), 'hello')


if __name__ == '__main__':
    unittest.main()
