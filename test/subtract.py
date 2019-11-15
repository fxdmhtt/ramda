# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest
from datetime import timedelta

class Test_subtract(unittest.TestCase):
    def test_subtracts_two_numbers(self):
        eq(self, R.subtract(22, 7), 15)

    def test_coerces_its_arguments_to_numbers(self):
        # eq(self, R.subtract('1', '2'), -1)
        # eq(self, R.subtract(1, '2'), -1)
        eq(self, R.subtract(True, False), 1)
        eq(self, R.subtract(float('nan'), float('nan')), float('nan'))
        eq(self, R.subtract(timedelta(1), timedelta(2)), timedelta(-1))


if __name__ == '__main__':
    unittest.main()
