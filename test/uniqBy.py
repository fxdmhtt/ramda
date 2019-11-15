# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_uniqBy(unittest.TestCase):
    def test_returns_a_set_from_any_array_based_on_predicate(self):
        self.assertSequenceEqual(list(R.uniqBy(abs, [-2, -1, 0, 1, 2])), [-2, -1, 0])

    def test_keeps_elements_from_the_left(self):
        self.assertSequenceEqual(list(R.uniqBy(abs, [-1, 2, 4, 3, 1, 3])), [-1, 2, 4, 3])

    def test_returns_an_empty_array_for_an_empty_array(self):
        self.assertSequenceEqual(list(R.uniqBy(R.identity, [])), [])

    # def test_has_R.equals_semantics(self):
    #     function Just(x) {
    #         this.value = x
    #     }
    #     Just.prototype.equals = function(x) {
    #         return x instanceof Just && R.equals(x.value, this.value)
    #     }
    #     eq(self, R.uniqBy(R.identity, [-0, 0]).length, 2)
    #     eq(self, R.uniqBy(R.identity, [NaN, NaN]).length, 1)
    #     eq(self, R.uniqBy(R.identity, [Just([1, 2, 3]), Just([1, 2, 3])]).length, 1)


if __name__ == '__main__':
    unittest.main()
