# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_includes(unittest.TestCase):
    def test_returns_True_if_an_element_is_in_a_list(self):
        eq(self, R.includes(7, [1, 2, 3, 9, 8, 7, 100, 200, 300]), True)

    def test_returns_False_if_an_element_is_not_in_a_list(self):
        eq(self, R.includes(99, [1, 2, 3, 9, 8, 7, 100, 200, 300]), False)

    def test_returns_False_for_the_empty_list(self):
        eq(self, R.includes(1, []), False)

    # def test_has_R.equals_semantics(self):
    #     function Just(x) { this.value = x }
    #     Just.prototype.equals = function(x) {
    #         return x instanceof Just && R.equals(x.value, this.value)
    #     }

    #     eq(self, R.includes(0, [-0]), False)
    #     eq(self, R.includes(-0, [0]), False)
    #     eq(self, R.includes(NaN, [NaN]), True)
    #     eq(self, R.includes(Just([42]), [Just([42])]), True)

    def test_returns_True_if_substring_is_part_of_string(self):
        eq(self, R.includes('ba', 'banana'), True)


if __name__ == '__main__':
    unittest.main()
