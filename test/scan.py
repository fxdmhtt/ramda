# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_scan(unittest.TestCase):
    def setUp(self):
        self.add = lambda a, b: a + b
        self.mult = lambda a, b: a * b

    def test_scans_simple_functions_over_arrays_with_the_supplied_accumulator(self):
        eq(self, R.scan(self.add, 0, [1, 2, 3, 4]), [0, 1, 3, 6, 10])
        eq(self, R.scan(self.mult, 1, [1, 2, 3, 4]), [1, 1, 2, 6, 24])

    def test_returns_the_accumulator_for_an_empty_array(self):
        eq(self, R.scan(self.add, 0, []), [0])
        eq(self, R.scan(self.mult, 1, []), [1])


if __name__ == '__main__':
    unittest.main()
