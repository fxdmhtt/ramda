# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_union(unittest.TestCase):
    def setUp(self):
        self.M = [1, 2, 3, 4]
        self.N = [3, 4, 5, 6]

    def test_combines_two_lists_into_the_set_of_all_their_elements(self):
        self.assertSequenceEqual(list(R.union(self.M, self.N)), [1, 2, 3, 4, 5, 6])

    # def test_has_R.equals_semantics(self):
    #     function Just(x) { this.value = x }
    #     Just.prototype.equals = function(x) {
    #         return x instanceof Just && R.equals(x.value, this.value)
    #     }

    #     eq(self, R.union([0], [-0]).length, 2)
    #     eq(self, R.union([-0], [0]).length, 2)
    #     eq(self, R.union([NaN], [NaN]).length, 1)
    #     eq(self, R.union([Just([42])], [Just([42])]).length, 1)


if __name__ == '__main__':
    unittest.main()
