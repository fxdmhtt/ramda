# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_none(unittest.TestCase):
    def setUp(self):
        self.even = lambda n: n % 2 == 0
        self.T = lambda: True
        # intoArray = R.into([])

    def test_returns_True_if_no_elements_satisfy_the_predicate(self):
        eq(self, R.none(self.even, [1, 3, 5, 7, 9, 11]), True)

    def test_returns_False_if_any_element_satisfies_the_predicate(self):
        eq(self, R.none(self.even, [1, 3, 5, 7, 8, 11]), False)

    def test_returns_True_for_an_empty_list(self):
        eq(self, R.none(self.T, []), True)

    # def test_returns_into_array(self):
    #     eq(self, intoArray(R.none(self.even), [1, 3, 5, 7, 9, 11]), [True])
    #     eq(self, intoArray(R.none(self.even), [1, 3, 5, 7, 8, 11]), [False])
    #     eq(self, intoArray(R.none(self.T), []), [True])

    def test_works_with_more_complex_objects(self):
        xs = [{'x': 'abcd'}, {'x': 'adef'}, {'x': 'fghiajk'}]
        len3 = lambda o: len(o['x']) == 3
        hasA = lambda o: o['x'].index('a') >= 0
        eq(self, R.none(len3, xs), True)
        eq(self, R.none(hasA, xs), False)


if __name__ == '__main__':
    unittest.main()
