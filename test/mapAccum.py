# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_mapAccum(unittest.TestCase):
    def setUp(self):
        self.add = lambda a, b: [a + b, a + b]
        self.mult = lambda a, b: [a * b, a * b]
        self.concat = lambda a, b: [a + b, a + b]

    def test_map_and_accumulate_simple_functions_over_arrays_with_the_supplied_accumulator(self):
        eq(self, R.mapAccum(self.add, 0, [1, 2, 3, 4]), [10, [1, 3, 6, 10]])
        eq(self, R.mapAccum(self.mult, 1, [1, 2, 3, 4]), [24, [1, 2, 6, 24]])

    def test_returns_the_list_and_accumulator_for_an_empty_array(self):
        eq(self, R.mapAccum(self.add, 0, []), [0, []])
        eq(self, R.mapAccum(self.mult, 1, []), [1, []])
        eq(self, R.mapAccum(self.concat, [], []), [[], []])


if __name__ == '__main__':
    unittest.main()
