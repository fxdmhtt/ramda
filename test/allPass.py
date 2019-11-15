# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_allPass(unittest.TestCase):
    def setUp(self):
        self.odd = lambda n: n % 2 != 0
        self.lt20 = lambda n: n < 20
        self.gt5 = lambda n: n > 5
        self.plusEq = lambda w, x, y, z: w + x == y + z

    def test_reports_whether_all_predicates_are_satisfied_by_a_given_value(self):
        ok = R.allPass([self.odd, self.lt20, self.gt5])
        eq(self, ok(7), True)
        eq(self, ok(9), True)
        eq(self, ok(10), False)
        eq(self, ok(3), False)
        eq(self, ok(21), False)

    def test_returns_True_on_empty_predicate_list(self):
        eq(self, R.allPass([])(3), True)

    def test_returns_a_curried_function_whose_arity_matches_that_of_the_highest_arity_predicate(self):
        eq(self, R.allPass([self.odd, self.gt5, self.plusEq]).length, 4)
        eq(self, R.allPass([self.odd, self.gt5, self.plusEq])(9, 9, 9, 9), True)
        eq(self, R.allPass([self.odd, self.gt5, self.plusEq])(9)(9)(9)(9), True)


if __name__ == '__main__':
    unittest.main()
