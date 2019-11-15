# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_mean(unittest.TestCase):
    def test_returns_mean_of_a_nonempty_list(self):
        eq(self, R.mean([2]), 2.0)
        eq(self, R.mean([2, 7]), 4.5)
        eq(self, R.mean([2, 7, 9]), 6.0)
        eq(self, R.mean([2, 7, 9, 10]), 7.0)

    def test_returns_NaN_for_an_empty_list(self):
        eq(self, R.identical(float('nan'), R.mean([])), True)

    def test_handles_array_like_object(self):
        eq(self, R.mean((lambda *arguments: arguments)(1, 2, 3)), 2.0)


if __name__ == '__main__':
    unittest.main()
