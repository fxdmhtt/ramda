# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_multiply(unittest.TestCase):
    def test_multiplies_together_two_numbers(self):
        eq(self, R.multiply(6, 7), 42)


if __name__ == '__main__':
    unittest.main()
