# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_partition(unittest.TestCase):
    def test_splits_a_list_into_two_lists_according_to_a_predicate(self):
        pred = lambda n: n % 2
        self.assertSequenceEqual(R.partition(pred, []), [[], []])
        self.assertSequenceEqual(R.partition(pred, [0, 2, 4, 6]), [[], [0, 2, 4, 6]])
        self.assertSequenceEqual(R.partition(pred, [1, 3, 5, 7]), [[1, 3, 5, 7], []])
        self.assertSequenceEqual(R.partition(pred, [0, 1, 2, 3]), [[1, 3], [0, 2]])

    def test_works_with_objects(self):
        pred = lambda n: n % 2
        self.assertSequenceEqual(R.partition(pred, {}), [{}, {}])
        self.assertSequenceEqual(R.partition(pred, { 'a': 0, 'b': 2, 'c': 4, 'd': 6 }),
            [{}, { 'a': 0, 'b': 2, 'c': 4, 'd': 6 }]
        )
        self.assertSequenceEqual(R.partition(pred, { 'a': 1, 'b': 3, 'c': 5, 'd': 7 }),
            [{ 'a': 1, 'b': 3, 'c': 5, 'd': 7 }, {}]
        )
        self.assertSequenceEqual(R.partition(pred, { 'a': 0, 'b': 1, 'c': 2, 'd': 3 }),
            [{ 'b': 1, 'd': 3 }, { 'a': 0, 'c': 2 }]
        )

    # def test_works_with_other_filterables(self):
    #     self.assertSequenceEqual(R.partition(R.isEmpty, S.Just(3)),
    #         [S.Nothing(), S.Just(3)]
    #     )
    #     self.assertSequenceEqual(R.partition(R.complement(R.isEmpty), S.Just(3)),
    #         [S.Just(3), S.Nothing()]
    #     )


if __name__ == '__main__':
    unittest.main()
