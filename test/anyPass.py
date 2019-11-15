# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_anyPass(unittest.TestCase):
    def setUp(self):
        self.odd = lambda n: n % 2 != 0
        self.gt20 = lambda n: n > 20
        self.lt5 = lambda n: n < 5
        self.plusEq = lambda w, x, y, z: w + x == y + z

    def test_reports_whether_any_predicates_are_satisfied_by_a_given_value(self):
        ok = R.anyPass([self.odd, self.gt20, self.lt5])
        eq(self, ok(7), True)
        eq(self, ok(9), True)
        eq(self, ok(10), False)
        eq(self, ok(18), False)
        eq(self, ok(3), True)
        eq(self, ok(22), True)

    def test_returns_False_for_an_empty_predicate_list(self):
        eq(self, R.anyPass([])(3), False)

    def test_returns_a_curried_function_whose_arity_matches_that_of_the_highest_arity_predicate(self):
        eq(self, R.anyPass([self.odd, self.lt5, self.plusEq]).length, 4)
        eq(self, R.anyPass([self.odd, self.lt5, self.plusEq])(6, 7, 8, 9), False)
        eq(self, R.anyPass([self.odd, self.lt5, self.plusEq])(6)(7)(8)(9), False)


if __name__ == '__main__':
    unittest.main()
