# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_groupWith(unittest.TestCase):
    def test_splits_the_list_into_groups_according_to_the_grouping_function(self):
        eq(self, R.groupWith(R.equals, [1, 2, 2, 3]), [[1], [2, 2], [3]])
        eq(self, R.groupWith(R.equals, [1, 1, 1, 1]), [[1, 1, 1, 1]])
        eq(self, R.groupWith(R.equals, [1, 2, 3, 4]), [[1], [2], [3], [4]])

    def test_splits_the_list_into_streaks_testing_adjacent_elements(self):
        isConsecutive = lambda a, b: a + 1 == b
        eq(self, R.groupWith(isConsecutive, []), [])
        eq(self, R.groupWith(isConsecutive, [4, 3, 2, 1]), [[4], [3], [2], [1]])
        eq(self, R.groupWith(isConsecutive, [1, 2, 3, 4]), [[1, 2, 3, 4]])
        eq(self, R.groupWith(isConsecutive, [1, 2, 2, 3]), [[1, 2], [2, 3]])
        eq(self, R.groupWith(isConsecutive, [1, 2, 9, 3, 4]), [[1, 2], [9], [3, 4]])

    def test_returns_an_empty_array_if_given_an_empty_array(self):
        eq(self, R.groupWith(R.equals, []), [])

    def test_can_be_turned_into_the_original_list_through_concatenation(self):
        list = [1, 1, 2, 3, 4, 4, 5, 5]
        eq(self, R.unnest(R.groupWith(R.equals, list)), list)
        eq(self, R.unnest(R.groupWith(R.complement(R.equals), list)), list)
        eq(self, R.unnest(R.groupWith(R.T, list)), list)
        eq(self, R.unnest(R.groupWith(R.F, list)), list)

    def test_also_works_on_strings(self):
        eq(self, R.groupWith(R.equals)('Mississippi'), ['M','i','ss','i','ss','i','pp','i'])


if __name__ == '__main__':
    unittest.main()
