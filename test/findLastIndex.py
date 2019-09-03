# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_findLastIndex(unittest.TestCase):
    def setUp(self):
        self.obj1 = {'x': 100}
        self.obj2 = {'x': 200}
        self.a = [11, 10, 9, 'cow', self.obj1, 8, 7, 100, 200, 300, self.obj2, 4, 3, 2, 1, 0]
        self.even = lambda x: isinstance(x, (int, float)) and x % 2 == 0
        self.gt100 = lambda x: isinstance(x, (int, float)) and x > 100
        self.isStr = lambda x: isinstance(x, str)
        self.xGt100 = lambda o: o and isinstance(o, dict) and o['x'] > 100
        # intoArray = R.into([])

    def test_returns_the_index_of_the_last_element_that_satisfies_the_predicate(self):
        eq(self, R.findLastIndex(self.even, self.a), 15)
        eq(self, R.findLastIndex(self.gt100, self.a), 9)
        eq(self, R.findLastIndex(self.isStr, self.a), 3)
        eq(self, R.findLastIndex(self.xGt100, self.a), 10)

    def test_returns__1_when_no_element_satisfies_the_predicate(self):
        eq(self, R.findLastIndex(self.even, ['zing']), -1)

    # def test_returns_the_index_of_the_last_element_into_an_array_that_satisfies_the_predicate(self):
    #     eq(self, intoArray(R.findLastIndex(even), a), [15])
    #     eq(self, intoArray(R.findLastIndex(gt100), a), [9])
    #     eq(self, intoArray(R.findLastIndex(isStr), a), [3])
    #     eq(self, intoArray(R.findLastIndex(xGt100), a), [10])

    # def test_returns__1_into_an_array_when_no_element_satisfies_the_predicate(self):
    #     eq(self, intoArray(R.findLastIndex(even), ['zing']), [-1])

    def test_works_when_the_first_element_matches(self):
        eq(self, R.findLastIndex(self.even, [2, 3, 5]), 0)

    def test_does_not_go_into_an_infinite_loop_on_an_empty_array(self):
        eq(self, R.findLastIndex(self.even, []), -1)

    # def test_dispatches_to_transformer_objects(self):
    #     eq(self, R.findLastIndex(R.identity, listXf), {
    #         f: R.identity,
    #         idx: -1,
    #         lastIdx: -1,
    #         xf: listXf


if __name__ == '__main__':
    unittest.main()
