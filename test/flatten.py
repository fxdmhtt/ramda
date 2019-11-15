# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_flatten(unittest.TestCase):
    def test_turns_a_nested_list_into_one_flat_list(self):
        nest = [1, [2], [3, [4, 5], 6, [[[7], 8]]], 9, 10]
        eq(self, R.flatten(nest), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        nest = [[[[3]], 2, 1], 0, [[-1, -2], -3]]
        eq(self, R.flatten(nest), [3, 2, 1, 0, -1, -2, -3])
        eq(self, R.flatten([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_is_not_destructive(self):
        nest = [1, [2], [3, [4, 5], 6, [[[7], 8]]], 9, 10]
        self.assertIsNot(R.flatten(nest), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

    def test_handles_ridiculously_large_inputs(self):
        eq(self, len(R.flatten([[None] * 1000000, R.range(0, 56000), 5, 1, 3])), 1056003)

    # def test_handles_array_like_objects(self):
    #     o = {'length': 3, 0: [1, 2, [3]], 1: [], 2: ['a', 'b', 'c', ['d', 'e']]}
    #     eq(self, R.flatten(o), [1, 2, 3, 'a', 'b', 'c', 'd', 'e'])

    def test_flattens_an_array_of_empty_arrays(self):
        eq(self, R.flatten([[], [], []]), [])
        eq(self, R.flatten([]), [])


if __name__ == '__main__':
    unittest.main()
