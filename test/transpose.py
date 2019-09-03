# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_transpose(unittest.TestCase):
    def test_returns_an_array_of_two_arrays(self):
        input = [['a', 1], ['b', 2], ['c', 3]]
        eq(self, R.transpose(input), [['a', 'b', 'c'], [1, 2, 3]])

    def test_skips_elements_when_rows_are_shorter(self):
        actual = R.transpose([[10, 11], [20], [], [30, 31, 32]])
        expected = [[10, 20, 30], [11, 31], [32]]
        eq(self, actual, expected)

    def test_copes_with_empty_arrays(self):
        eq(self, R.transpose([]), [])

    def test_copes_with_True_False_None_None_elements_of_arrays(self):
        actual = R.transpose([[True, False, None, None], [None, None, False, True]])
        expected = [[True, None], [False, None], [None, False], [None, True]]
        eq(self, actual, expected)


if __name__ == '__main__':
    unittest.main()
