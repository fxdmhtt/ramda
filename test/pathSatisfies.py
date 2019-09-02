# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_pathSatisfies(unittest.TestCase):
    def setUp(self):
        self.isPositive = lambda n: n > 0

    def test_returns_True_if_the_specified_object_path_satisfies_the_given_predicate(self):
        eq(self, R.pathSatisfies(self.isPositive, ['x', 1, 'y'], {'x': [{'y': -1}, {'y': 1}]}), True)

    # def test_returns_False_if_the_specified_path_does_not_exist(self):
    #     eq(self, R.pathSatisfies(self.isPositive, ['x', 'y'], {'x': {'z': 42}}), False)

    def test_handles_empty_paths_by_applying_pred_to_data_positive(self):
        eq(self, R.pathSatisfies(R.is_(dict), [], {'x': {'z': 42}}), True)

    def test_handles_empty_paths_by_applying_pred_to_data_negative(self):
        eq(self, R.pathSatisfies(R.has('y'), [], {'x': {'z': 42}}), False)

    def test_returns_False_otherwise(self):
        eq(self, R.pathSatisfies(self.isPositive, ['x', 'y'], {'x': {'y': 0}}), False)


if __name__ == '__main__':
    unittest.main()
