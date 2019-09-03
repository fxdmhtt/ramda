# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_findLast(unittest.TestCase):
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
        eq(self, R.findLast(self.even, self.a), 0)
        eq(self, R.findLast(self.gt100, self.a), 300)
        eq(self, R.findLast(self.isStr, self.a), 'cow')
        eq(self, R.findLast(self.xGt100, self.a), self.obj2)

    # def test_returns_the_index_of_the_last_element_that_satisfies_the_predicate_into_an_array(self):
    #     eq(self, intoArray(R.findLast(even), a), [0])
    #     eq(self, intoArray(R.findLast(gt100), a), [300])
    #     eq(self, intoArray(R.findLast(isStr), a), ['cow'])
    #     eq(self, intoArray(R.findLast(xGt100), a), [obj2])

    def test_returns_None_when_no_element_satisfies_the_predicate(self):
        eq(self, R.findLast(self.even, ['zing']), None)

    # def test_returns_None_into_an_array_when_no_element_satisfies_the_predicate(self):
    #     eq(self, intoArray(R.findLast(even), ['zing']), [None])

    def test_works_when_the_first_element_matches(self):
        eq(self, R.findLast(self.even, [2, 3, 5]), 2)

    def test_does_not_go_into_an_infinite_loop_on_an_empty_array(self):
        eq(self, R.findLast(self.even, []), None)

    # def test_dispatches_to_transformer_objects(self):
    #     eq(self, R.findLast(R.identity, listXf), {
    #         f: R.identity,
    #         xf: listXf


if __name__ == '__main__':
    unittest.main()
