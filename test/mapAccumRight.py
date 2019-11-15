# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_mapAccumRight(unittest.TestCase):
    def setUp(self):
        self.add = lambda a, b: [a + b, a + b]
        self.mult = lambda a, b: [a * b, a * b]

    def test_map_and_accumulate_simple_functions_over_arrays_with_the_supplied_accumulator(self):
        eq(self, R.mapAccumRight(self.add, 0, [1, 2, 3, 4]), [10, [10, 9, 7, 4]])
        eq(self, R.mapAccumRight(self.mult, 1, [1, 2, 3, 4]), [24, [24, 24, 12, 4]])

    def test_returns_the_list_and_accumulator_for_an_empty_array(self):
        eq(self, R.mapAccumRight(self.add, 0, []), [0, []])
        eq(self, R.mapAccumRight(self.mult, 1, []), [1, []])
        eq(self, R.mapAccumRight(R.concat, [], []), [[], []])


if __name__ == '__main__':
    unittest.main()
