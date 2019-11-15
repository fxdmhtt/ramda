# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_symmetricDifference(unittest.TestCase):
    def setUp(self):
        self.M = [1, 2, 3, 4]
        self.M2 = [1, 2, 3, 4, 1, 2, 3, 4]
        self.N = [3, 4, 5, 6]
        self.N2 = [3, 3, 4, 4, 5, 5, 6, 6]
        self.Z = [3, 4, 5, 6, 10]
        self.Z2 = [1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 8]

    def test_finds_the_set_of_all_elements_in_the_first_or_second_list_but_not_both(self):
        eq(self, R.symmetricDifference(self.M, self.N), [1, 2, 5, 6])

    def test_does_not_allow_duplicates_in_the_output_even_if_the_input_lists_had_duplicates(self):
        eq(self, R.symmetricDifference(self.M2, self.N2), [1, 2, 5, 6])

    # def test_has_R.equals_semantics(self):
    #     function Just(x) { this.value = x }
    #     Just.prototype.equals = function(x) {
    #         return x instanceof Just && R.equals(x.value, this.value)
    #     }

    #     eq(self, R.symmetricDifference([0], [-0]).length, 2)
    #     eq(self, R.symmetricDifference([-0], [0]).length, 2)
    #     eq(self, R.symmetricDifference([NaN], [NaN]).length, 0)
    #     eq(self, R.symmetricDifference([Just([42])], [Just([42])]).length, 0)

    def test_works_for_arrays_of_different_lengths(self):
        eq(self, R.symmetricDifference(self.Z, self.Z2), [10, 1, 2, 7, 8])
        eq(self, R.symmetricDifference(self.Z2, self.Z), [1, 2, 7, 8, 10])

    def test_will_not_create_a_sparse_array(self):
        eq(self, len(R.symmetricDifference(self.M2, [3])), 3)

    def test_returns_an_empty_array_if_there_are_no_different_elements(self):
        eq(self, R.symmetricDifference(self.M2, self.M), [])
        eq(self, R.symmetricDifference(self.M, self.M2), [])


if __name__ == '__main__':
    unittest.main()
