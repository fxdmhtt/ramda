# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_splitWhen(unittest.TestCase):
    def test_splits_an_array_at_the_first_instance_to_satisfy_the_predicate(self):
        eq(self, R.splitWhen(R.equals(2), [1, 2, 3]), [[1], [2, 3]])

    def test_retains_all_original_elements(self):
        eq(self, R.splitWhen(R.T, [1, 1, 1]), [[], [1, 1, 1]])

    def test_only_splits_once(self):
        eq(self, R.splitWhen(R.equals(2), [1, 2, 3, 1, 2, 3]), [[1], [2, 3, 1, 2, 3]])


if __name__ == '__main__':
    unittest.main()
