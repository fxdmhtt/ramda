# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_fromPairs(unittest.TestCase):
    def test_combines_an_array_of_two_element_arrays_into_an_object(self):
        eq(self, R.fromPairs([['a', 1], ['b', 2], ['c', 3]]), {'a': 1, 'b': 2, 'c': 3})

    def test_gives_later_entries_precedence_over_earlier_ones(self):
        eq(self, R.fromPairs([['x', 1], ['x', 2]]), {'x': 2})


if __name__ == '__main__':
    unittest.main()
