# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_splitEvery(unittest.TestCase):
    def test_splits_a_collection_into_slices_of_the_specified_length(self):
        self.assertSequenceEqual(list(R.splitEvery(1, [1, 2, 3, 4])), [[1], [2], [3], [4]])
        self.assertSequenceEqual(list(R.splitEvery(2, [1, 2, 3, 4])), [[1, 2], [3, 4]])
        self.assertSequenceEqual(list(R.splitEvery(3, [1, 2, 3, 4])), [[1, 2, 3], [4]])
        self.assertSequenceEqual(list(R.splitEvery(4, [1, 2, 3, 4])), [[1, 2, 3, 4]])
        self.assertSequenceEqual(list(R.splitEvery(5, [1, 2, 3, 4])), [[1, 2, 3, 4]])
        self.assertSequenceEqual(list(R.splitEvery(3, [])), [])
        self.assertSequenceEqual(list(R.splitEvery(1, 'abcd')), ['a', 'b', 'c', 'd'])
        self.assertSequenceEqual(list(R.splitEvery(2, 'abcd')), ['ab', 'cd'])
        self.assertSequenceEqual(list(R.splitEvery(3, 'abcd')), ['abc', 'd'])
        self.assertSequenceEqual(list(R.splitEvery(4, 'abcd')), ['abcd'])
        self.assertSequenceEqual(list(R.splitEvery(5, 'abcd')), ['abcd'])
        self.assertSequenceEqual(list(R.splitEvery(3, '')), [])

    def test_throws_if_first_argument_is_not_positive(self):
        with self.assertRaises(Exception):
            list(R.splitEvery(0, []))
            list(R.splitEvery(0, ''))
            list(R.splitEvery(-1, []))
            list(R.splitEvery(-1, ''))


if __name__ == '__main__':
    unittest.main()
