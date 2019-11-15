# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_findIndex(unittest.TestCase):
    def setUp(self):
        self.obj1 = {'x': 100}
        self.obj2 = {'x': 200}
        self.a = [11, 10, 9, 'cow', self.obj1, 8, 7, 100, 200, 300, self.obj2, 4, 3, 2, 1, 0]
        self.even = lambda x: isinstance(x, (int, float)) and x % 2 == 0
        self.gt100 = lambda x: isinstance(x, (int, float)) and x > 100
        self.isStr = lambda x: isinstance(x, str)
        self.xGt100 = lambda o: o and isinstance(o, dict) and o['x'] > 100
        # intoArray = R.into([])

    def test_returns_the_index_of_the_first_element_that_satisfies_the_predicate(self):
        eq(self, R.findIndex(self.even, self.a), 1)
        eq(self, R.findIndex(self.gt100, self.a), 8)
        eq(self, R.findIndex(self.isStr, self.a), 3)
        eq(self, R.findIndex(self.xGt100, self.a), 10)

    # def test_returns_the_index_of_the_first_element_that_satisfies_the_predicate_into_an_array(self):
    #     eq(self, intoArray(R.findIndex(even), a), [1])
    #     eq(self, intoArray(R.findIndex(gt100), a), [8])
    #     eq(self, intoArray(R.findIndex(isStr), a), [3])
    #     eq(self, intoArray(R.findIndex(xGt100), a), [10])

    def test_returns__1_when_no_element_satisfies_the_predicate(self):
        eq(self, R.findIndex(self.even, ['zing']), -1)
        eq(self, R.findIndex(self.even, []), -1)

    # def test_returns__1_in_array_when_no_element_satisfies_the_predicate_into_an_array(self):
    #     eq(self, intoArray(R.findIndex(even), ['zing']), [-1])

    # def test_dispatches_to_transformer_objects(self):
    #     eq(self, R.findIndex(R.identity, listXf), {
    #         f: R.identity,
    #         found: False,
    #         idx: -1,
    #         xf: listXf


if __name__ == '__main__':
    unittest.main()
