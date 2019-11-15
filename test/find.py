# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_find(unittest.TestCase):
    def setUp(self):
        self.obj1 = {'x': 100}
        self.obj2 = {'x': 200}
        self.a = [11, 10, 9, 'cow', self.obj1, 8, 7, 100, 200, 300, self.obj2, 4, 3, 2, 1, 0]
        self.even = lambda x: isinstance(x, (int, float)) and x % 2 == 0
        self.gt100 = lambda x: isinstance(x, (int, float)) and x > 100
        self.isStr = lambda x: isinstance(x, str)
        self.xGt100 = lambda o: o and isinstance(o, dict) and o['x'] > 100
        # intoArray = R.into([])

    def test_returns_the_first_element_that_satisfies_the_predicate(self):
        eq(self, R.find(self.even, self.a), 10)
        eq(self, R.find(self.gt100, self.a), 200)
        eq(self, R.find(self.isStr, self.a), 'cow')
        eq(self, R.find(self.xGt100, self.a), self.obj2)

    # def test_transduces_the_first_element_that_satisfies_the_predicate_into_an_array(self):
    #     eq(self, intoArray(R.find(self.even), self.a), [10])
    #     eq(self, intoArray(R.find(self.gt100), self.a), [200])
    #     eq(self, intoArray(R.find(self.isStr), self.a), ['cow'])
    #     eq(self, intoArray(R.find(self.xGt100), self.a), [self.obj2])

    def test_returns_None_when_no_element_satisfies_the_predicate(self):
        eq(self, R.find(self.even, ['zing']), None)

    # def test_returns_None_in_array_when_no_element_satisfies_the_predicate_into_an_array(self):
    #     eq(self, intoArray(R.find(self.even), ['zing']), [None])

    def test_returns_None_when_given_an_empty_list(self):
        eq(self, R.find(self.even, []), None)

    # def test_returns_None_into_an_array_when_given_an_empty_list(self):
    #     eq(self, intoArray(R.find(self.even), []), [None])

    # def test_dispatches_to_transformer_objects(self):
    #     eq(self, R.find(R.identity, listXf), {
    #         f: R.identity,
    #         found: False,
    #         xf: listXf


if __name__ == '__main__':
    unittest.main()
