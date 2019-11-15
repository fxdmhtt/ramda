# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq
from ramda.internal._isArrayLike import _isArrayLike

import unittest

class Test_unless(unittest.TestCase):
    def test_calls_the_whenFalse_function_if_the_validator_returns_a_falsy_value(self):
        eq(self, R.unless(_isArrayLike, R.of)(10), [10])

    def test_returns_the_argument_unmodified_if_the_validator_returns_a_truthy_value(self):
        eq(self, R.unless(_isArrayLike, R.of)([10]), [10])

    def test_returns_a_curried_function(self):
        eq(self, R.unless(_isArrayLike)(R.of)(10), [10])
        eq(self, R.unless(_isArrayLike)(R.of)([10]), [10])


if __name__ == '__main__':
    unittest.main()
