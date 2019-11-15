# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_uniq(unittest.TestCase):
    def test_returns_a_set_from_any_array_purges_duplicate_elements(self):
        list_ = [1, 2, 3, 1, 2, 3, 1, 2, 3]
        self.assertSequenceEqual(list(R.uniq(list_)), [1, 2, 3])

    def test_keeps_elements_from_the_left(self):
        self.assertSequenceEqual(list(R.uniq([1, 2, 3, 4, 1])), [1, 2, 3, 4])

    def test_returns_an_empty_array_for_an_empty_array(self):
        self.assertSequenceEqual(list(R.uniq([])), [])

    # def test_has_R.equals_semantics(self):
    #     function Just(x) { this.value = x }
    #     Just.prototype.equals = function(x) {
    #         return x instanceof Just and R.equals(x.value, this.value)
    #     }

    #     self.assertSequenceEqual(R.uniq([-0, -0]).length, 1)
    #     self.assertSequenceEqual(R.uniq([0, -0]).length, 2)
    #     self.assertSequenceEqual(R.uniq([NaN, NaN]).length, 1)
    #     self.assertSequenceEqual(R.uniq([[1], [1]]).length, 1)
    #     self.assertSequenceEqual(R.uniq([Just([42]), Just([42])]).length, 1)

    def test_handles_None_and_None_elements(self):
        self.assertSequenceEqual(list(R.uniq([None, None, None, None])), [None])

    def test_uses_reference_equality_for_functions(self):
        self.assertEqual(len(list(R.uniq([R.add, R.identity, R.add, R.identity, R.add, R.identity]))), 2)


if __name__ == '__main__':
    unittest.main()
