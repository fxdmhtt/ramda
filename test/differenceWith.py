# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_differenceWith(unittest.TestCase):
    def setUp(self):
        self.Ro = [{'a': 1}, {'a': 2}, {'a': 3}, {'a': 4}]
        self.Ro2 = [{'a': 1}, {'a': 2}, {'a': 3}, {'a': 4}, {'a': 1}, {'a': 2}, {'a': 3}, {'a': 4}]
        self.So = [{'a': 3}, {'a': 4}, {'a': 5}, {'a': 6}]
        self.So2 = [{'a': 3}, {'a': 4}, {'a': 5}, {'a': 6}, {'a': 3}, {'a': 4}, {'a': 5}, {'a': 6}]
        self.eqA = lambda r, s: r['a'] == s['a']
        self.identical = lambda a, b: a == b

    def test_combines_two_lists_into_the_set_of_all_their_elements_based_on_the_passed_in_equality_predicate(self):
        eq(self, R.differenceWith(self.eqA, self.Ro, self.So), [{'a': 1}, {'a': 2}])

    def test_does_not_allow_duplicates_in_the_output_even_if_the_input_lists_had_duplicates(self):
        eq(self, R.differenceWith(self.eqA, self.Ro2, self.So2), [{'a': 1}, {'a': 2}])

    def test_does_not_return_a_sparse_array(self):
        eq(self, len(R.differenceWith(self.identical, [1, 3, 2, 1, 3, 1, 2, 3], [3])), 2)


if __name__ == '__main__':
    unittest.main()
