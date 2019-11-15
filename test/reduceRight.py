# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_reduceRight(unittest.TestCase):
    def setUp(self):
        self.avg = lambda a, b: (a + b) / 2

    def test_folds_lists_in_the_right_order(self):
        eq(self, R.reduceRight(lambda a, b: a + b, '', ['a', 'b', 'c', 'd']), 'abcd')

    def test_folds_subtract_over_arrays_in_the_right_order(self):
        eq(self, R.reduceRight(lambda a, b: a - b, 0, [1, 2, 3, 4]), -2)

    def test_folds_simple_functions_over_arrays_with_the_supplied_accumulator(self):
        eq(self, R.reduceRight(self.avg, 54, [12, 4, 10, 6]), 12.0)

    def test_returns_the_accumulator_for_an_empty_array(self):
        eq(self, R.reduceRight(self.avg, 0, []), 0)


if __name__ == '__main__':
    unittest.main()
