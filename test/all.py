# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_all(unittest.TestCase):
    def setUp(self):
        self.even = lambda n: n % 2 == 0
        self.T = lambda: True
        self.isFalse = lambda x: x == False
        self.intoArray = R.into([])

    def test_returns_True_if_all_elements_satisfy_the_predicate(self):
        eq(self, R.all(self.even, [2, 4, 6, 8, 10, 12]), True)
        eq(self, R.all(self.isFalse, [False, False, False]), True)

    def test_returns_False_if_any_element_fails_to_satisfy_the_predicate(self):
        eq(self, R.all(self.even, [2, 4, 6, 8, 9, 10]), False)

    def test_returns_True_for_an_empty_list(self):
        eq(self, R.all(self.T, []), True)

    def test_returns_True_into_array_if_all_elements_satisfy_the_predicate(self):
        eq(self, self.intoArray(R.all(self.even), [2, 4, 6, 8, 10, 12]), [True])
        eq(self, self.intoArray(R.all(self.isFalse), [False, False, False]), [True])

    def test_returns_False_into_array_if_any_element_fails_to_satisfy_the_predicate(self):
        eq(self, self.intoArray(R.all(self.even), [2, 4, 6, 8, 9, 10]), [False])

    def test_returns_True_into_array_for_an_empty_list(self):
        eq(self, self.intoArray(R.all(self.T), []), [True])

    def test_works_with_more_complex_objects(self):
        xs = [{'x': 'abc'}, {'x': 'ade'}, {'x': 'fghiajk'}]
        len3 = lambda o: o.x.length == 3
        hasA = lambda o: o.x.indexOf('a') > -1
        eq(self, R.all(len3, xs), False)
        eq(self, R.all(hasA, xs), True)

    def test_dispatches_when_given_a_transformer_in_list_position(self):
        eq(self, R.all(self.even, self.listXf), {
            'all': True,
            'f': even,
            'xf': self.listXf
        })


if __name__ == '__main__':
    unittest.main()
