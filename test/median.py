# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_median(unittest.TestCase):
    def test_returns_middle_value_of_an_odd_length_list(self):
        eq(self, R.median([2]), 2.0)
        eq(self, R.median([2, 9, 7]), 7.0)

    def test_returns_mean_of_two_middle_values_of_a_nonempty_even_length_list(self):
        eq(self, R.median([7, 2]), 4.5)
        eq(self, R.median([7, 2, 10, 9]), 8.0)

    def test_returns_NaN_for_an_empty_list(self):
        eq(self, R.identical(float('nan'), R.median([])), True)

    def test_handles_array_like_object(self):
        eq(self, R.median((lambda *arguments: arguments)(1, 2, 3)), 2.0)


if __name__ == '__main__':
    unittest.main()
