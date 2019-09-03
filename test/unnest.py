# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_unnest(unittest.TestCase):
    def test_only_flattens_one_layer_deep_of_a_nested_list(self):
        nest = [1, [2], [3, [4, 5], 6, [[[7], 8]]], 9, 10]
        eq(self, R.unnest(nest), [1, 2, 3, [4, 5], 6, [[[7], 8]], 9, 10])
        nest = [[[[3]], 2, 1], 0, [[-1, -2], -3]]
        eq(self, R.unnest(nest), [[[3]], 2, 1, 0, [-1, -2], -3])
        eq(self, R.unnest([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_is_not_destructive(self):
        nest = [1, [2], [3, [4, 5], 6, [[[7], 8]]], 9, 10]
        eq(self, R.unnest(nest), [1, 2, 3, [4, 5], 6, [[[7], 8]], 9, 10])

    # def test_handles_array_like_objects(self):
    #     o = {'length': 3, 0: [1, 2, [3]], 1: [], 2: ['a', 'b', 'c', ['d', 'e']]}
    #     eq(self, R.unnest(o), [1, 2, [3], 'a', 'b', 'c', ['d', 'e']])

    def test_flattens_an_array_of_empty_arrays(self):
        eq(self, R.unnest([[], [], []]), [])
        eq(self, R.unnest([]), [])

    # def test_is_equivalent_to_R.chain(R.identity)(self):
    #     Nothing = Maybe.Nothing
    #     Just = Maybe.Just

    #     eq(self, R.unnest(Nothing), Nothing)
    #     eq(self, R.unnest(Just(Nothing)), Nothing)
    #     eq(self, R.unnest(Just(Just(Nothing))), Just(Nothing))
    #     eq(self, R.unnest(Just(Just(42))), Just(42))
    #     eq(self, R.unnest(Just(Just(Just(42)))), Just(Just(42)))


if __name__ == '__main__':
    unittest.main()
