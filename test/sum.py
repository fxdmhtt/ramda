# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_sum(unittest.TestCase):
    def test_adds_together_the_array_of_numbers_supplied(self):
        eq(self, R.sum([1, 2, 3, 4]), 10)

    def test_does_not_save_the_state_of_the_accumulator(self):
        eq(self, R.sum([1, 2, 3, 4]), 10)
        eq(self, R.sum([1]), 1)
        eq(self, R.sum([5, 5, 5, 5, 5]), 25)


if __name__ == '__main__':
    unittest.main()
