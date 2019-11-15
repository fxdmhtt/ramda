# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_zipObj(unittest.TestCase):
    def test_combines_an_array_of_keys_with_an_array_of_values_into_a_single_object(self):
        eq(self, R.zipObj(['a', 'b', 'c'], [1, 2, 3]), {'a': 1, 'b': 2, 'c': 3})

    def test_ignores_extra_values(self):
        eq(self, R.zipObj(['a', 'b', 'c'], [1, 2, 3, 4, 5, 6, 7]), {'a': 1, 'b': 2, 'c': 3})

    def test_ignores_extra_keys(self):
        eq(self, R.zipObj(['a', 'b', 'c', 'd', 'e', 'f'], [1, 2, 3]), {'a': 1, 'b': 2, 'c': 3})

    def test_last_one_in_wins_when_there_are_duplicate_keys(self):
        eq(self, R.zipObj(['a', 'b', 'c', 'a'], [1, 2, 3, 'LAST']), {'a': 'LAST', 'b': 2, 'c': 3})


if __name__ == '__main__':
    unittest.main()
