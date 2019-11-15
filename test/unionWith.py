# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_unionWith(unittest.TestCase):
    def setUp(self):
        self.Ro = [{'a': 1}, {'a': 2}, {'a': 3}, {'a': 4}]
        self.So = [{'a': 3}, {'a': 4}, {'a': 5}, {'a': 6}]
        self.eqA = lambda r, s: r['a'] == s['a']

    def test_combines_two_lists_into_the_set_of_all_their_elements_based_on_the_passed_in_equality_predicate(self):
        self.assertSequenceEqual(list(R.unionWith(self.eqA, self.Ro, self.So)), [{'a': 1}, {'a': 2}, {'a': 3}, {'a': 4}, {'a': 5}, {'a': 6}])


if __name__ == '__main__':
    unittest.main()
