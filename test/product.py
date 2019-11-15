# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_product(unittest.TestCase):
    def test_multiplies_together_the_array_of_numbers_supplied(self):
        eq(self, R.product([1, 2, 3, 4]), 24)


if __name__ == '__main__':
    unittest.main()
