# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_splitEvery(unittest.TestCase):
    def test_splits_a_collection_into_slices_of_the_specified_length(self):
        eq(self, R.splitEvery(1, [1, 2, 3, 4]), [[1], [2], [3], [4]])
        eq(self, R.splitEvery(2, [1, 2, 3, 4]), [[1, 2], [3, 4]])
        eq(self, R.splitEvery(3, [1, 2, 3, 4]), [[1, 2, 3], [4]])
        eq(self, R.splitEvery(4, [1, 2, 3, 4]), [[1, 2, 3, 4]])
        eq(self, R.splitEvery(5, [1, 2, 3, 4]), [[1, 2, 3, 4]])
        eq(self, R.splitEvery(3, []), [])
        eq(self, R.splitEvery(1, 'abcd'), ['a', 'b', 'c', 'd'])
        eq(self, R.splitEvery(2, 'abcd'), ['ab', 'cd'])
        eq(self, R.splitEvery(3, 'abcd'), ['abc', 'd'])
        eq(self, R.splitEvery(4, 'abcd'), ['abcd'])
        eq(self, R.splitEvery(5, 'abcd'), ['abcd'])
        eq(self, R.splitEvery(3, ''), [])

    def test_throws_if_first_argument_is_not_positive(self):
        with self.assertRaises(Exception):
            R.splitEvery(0, [])
            R.splitEvery(0, '')
            R.splitEvery(-1, [])
            R.splitEvery(-1, '')


if __name__ == '__main__':
    unittest.main()
