# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_uniq(unittest.TestCase):
    def test_returns_a_set_from_any_array_purges_duplicate_elements(self):
        list = [1, 2, 3, 1, 2, 3, 1, 2, 3]
        eq(self, R.uniq(list), [1, 2, 3])

    def test_keeps_elements_from_the_left(self):
        eq(self, R.uniq([1, 2, 3, 4, 1]), [1, 2, 3, 4])

    def test_returns_an_empty_array_for_an_empty_array(self):
        eq(self, R.uniq([]), [])

    # def test_has_R.equals_semantics(self):
    #     function Just(x) { this.value = x }
    #     Just.prototype.equals = function(x) {
    #         return x instanceof Just and R.equals(x.value, this.value)
    #     }

    #     eq(self, R.uniq([-0, -0]).length, 1)
    #     eq(self, R.uniq([0, -0]).length, 2)
    #     eq(self, R.uniq([NaN, NaN]).length, 1)
    #     eq(self, R.uniq([[1], [1]]).length, 1)
    #     eq(self, R.uniq([Just([42]), Just([42])]).length, 1)

    def test_handles_None_and_None_elements(self):
        eq(self, R.uniq([None, None, None, None]), [None])

    def test_uses_reference_equality_for_functions(self):
        eq(self, len(R.uniq([R.add, R.identity, R.add, R.identity, R.add, R.identity])), 2)


if __name__ == '__main__':
    unittest.main()
