# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_intersection(unittest.TestCase):
    def setUp(self):
        self.M = [1, 2, 3, 4]
        self.M2 = [1, 2, 3, 4, 1, 2, 3, 4]
        self.N = [3, 4, 5, 6]
        self.N2 = [3, 3, 4, 4, 5, 5, 6, 6]

    def test_combines_two_lists_into_the_set_of_common_elements(self):
        self.assertSequenceEqual(list(R.intersection(self.M, self.N)), [3, 4])

    def test_does_not_allow_duplicates_in_the_output_even_if_the_input_lists_had_duplicates(self):
        self.assertSequenceEqual(list(R.intersection(self.M2, self.N2)), [3, 4])

    # def test_has_R.equals_semantics(self):
    #     function Just(x) { this.value = x }
    #     Just.prototype.equals = function(x) {
    #         return x instanceof Just && R.equals(x.value, this.value)
    #     }

    #     self.assertSequenceEqual(R.intersection([0], [-0]).length, 0)
    #     self.assertSequenceEqual(R.intersection([-0], [0]).length, 0)
    #     self.assertSequenceEqual(R.intersection([NaN], [NaN]).length, 1)
    #     self.assertSequenceEqual(R.intersection([Just([42])], [Just([42])]).length, 1)


if __name__ == '__main__':
    unittest.main()
