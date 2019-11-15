# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq
from ramda.internal._isArrayLike import _isArrayLike

import unittest

class Test_until(unittest.TestCase):
    def test_applies_fn_until_pred_is_satisfied(self):
        eq(self, R.until(R.gt(R.__, 100), R.multiply(2), 1), 128)

    def test_works_with_lists(self):
        eq(self, R.until(R.none(_isArrayLike), R.unnest)([1, [2], [[3]]]), [1, 2, 3])

    def test_ignores_fn_if_predicate_is_always_True(self):
        eq(self, R.until(R.T, R.T, False), False)


if __name__ == '__main__':
    unittest.main()
