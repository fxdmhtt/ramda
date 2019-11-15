# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_unary_functions_like_map(unittest.TestCase):
    def setUp(self):
        self.times2 = lambda x: x * 2
        self.addIndexParam = lambda x, idx: x + idx
        self.squareEnds = lambda x, idx, list: x * x if idx == 0 or idx == len(list) - 1 else x

    def test_works_just_like_a_normal_map(self):
        self.assertSequenceEqual(list(R.mapIndexed(self.times2, [1, 2, 3, 4])), [2, 4, 6, 8])

    def test_passes_the_index_as_a_second_parameter_to_the_callback(self):
        self.assertSequenceEqual(list(R.mapIndexed(self.addIndexParam, [8, 6, 7, 5, 3, 0, 9])), [8, 7, 9, 8, 7, 5, 15])

    def test_passes_the_entire_list_as_a_third_parameter_to_the_callback(self):
        self.assertSequenceEqual(list(R.mapIndexed(self.squareEnds, [8, 6, 7, 5, 3, 0, 9])), [64, 6, 7, 5, 3, 0, 81])

    def test_acts_as_a_curried_function(self):
        makeSquareEnds = R.mapIndexed(self.squareEnds)
        self.assertSequenceEqual(list(makeSquareEnds([8, 6, 7, 5, 3, 0, 9])), [64, 6, 7, 5, 3, 0, 81])


if __name__ == '__main__':
    unittest.main()
