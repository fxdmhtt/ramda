# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_applyTo(unittest.TestCase):
    def test_applies_the_function_to_its_first_argument(self):
        eq(self, R.applyTo(21, R.multiply(2)), 42)

    def test_has_length_2(self):
        eq(self, R.applyTo.length, 2)


if __name__ == '__main__':
    unittest.main()
