# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_unary_functions_like_map(unittest.TestCase):
    def setUp(self):
        self.times2 = lambda x: x * 2
        self.addIndexParam = lambda x, idx: x + idx
        self.squareEnds = lambda x, idx, list: x * x if idx == 0 or idx == len(list) - 1 else x
        self.mapIndexed = R.addIndex(R.map)

    def test_works_just_like_a_normal_map(self):
        eq(self, self.mapIndexed(self.times2, [1, 2, 3, 4]), [2, 4, 6, 8])

    def test_passes_the_index_as_a_second_parameter_to_the_callback(self):
        eq(self, self.mapIndexed(self.addIndexParam, [8, 6, 7, 5, 3, 0, 9]), [8, 7, 9, 8, 7, 5, 15])

    def test_passes_the_entire_list_as_a_third_parameter_to_the_callback(self):
        eq(self, self.mapIndexed(self.squareEnds, [8, 6, 7, 5, 3, 0, 9]), [64, 6, 7, 5, 3, 0, 81])

    def test_acts_as_a_curried_function(self):
        makeSquareEnds = self.mapIndexed(self.squareEnds)
        eq(self, makeSquareEnds([8, 6, 7, 5, 3, 0, 9]), [64, 6, 7, 5, 3, 0, 81])

class Test_binary_functions_like_reduce(unittest.TestCase):
    def setUp(self):
        self.reduceIndexed = R.addIndex(R.reduce)
        self.timesIndexed = lambda tot, num, idx: tot + (num * idx)
        self.objectify = lambda acc, elem, idx: (acc.__setitem__(elem, idx), acc)[-1]

    def test_passes_the_index_as_a_third_parameter_to_the_predicate(self):
        eq(self, self.reduceIndexed(self.timesIndexed, 0, [1, 2, 3, 4, 5]), 40)
        eq(self, self.reduceIndexed(self.objectify, {}, ['a', 'b', 'c', 'd', 'e']), {a: 0, b: 1, c: 2, d: 3, e: 4})

    def test_passes_the_entire_list_as_a_fourth_parameter_to_the_predicate(self):
        list = [1, 2, 3]
        self.reduceIndexed(lambda acc, x, idx, ls: (eq(self, ls, list), acc)[-1], 0, list)

class Test_works_with_functions_like_all_that_do_not_typically_have_index_applied(unittest.TestCase):
    def setUp(self):
        self.allIndexed = R.addIndex(R.all)
        self.superDiagonal = self.allIndexed(R.gt)

    def test_passes_the_index_as_a_second_parameter(self):
        eq(self, self.superDiagonal([8, 6, 5, 4, 9]), true)
        eq(self, self.superDiagonal([8, 6, 1, 3, 9]), false)

class Test_works_with_arbitrary_user_defined_functions(unittest.TestCase):
    def setUp(self):
        self.mapFilter = lambda m, f, list: R.filter(R.compose(f, m), list)
        self.mapFilterIndexed = R.addIndex(self.mapFilter)

    def test_passes_the_index_as_an_additional_parameter(self):
        eq(self, self.mapFilterIndexed(
            R.multiply,
            R.gt(R.__, 13),
            [8, 6, 7, 5, 3, 0, 9]
        ), [7, 5, 9])


if __name__ == '__main__':
    unittest.main()
