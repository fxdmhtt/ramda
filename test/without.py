# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_without(unittest.TestCase):
    def test_returns_an_array_not_containing_values_in_the_first_argument(self):
        eq(self, R.without([1, 2], [1, 2, 1, 4, 5]), [4, 5])

    # def test_can_act_as_a_transducer(self):
    #     eq(self, R.into([], R.without([1]), [1]), [])

    # def test_has_R.equals_semantics(self):
    #     function Just(x) { this.value = x }
    #     Just.prototype.equals = function(x) {
    #         return x instanceof Just && R.equals(x.value, this.value)
    #     }

    #     eq(self, R.without([0], [-0]).length, 1)
    #     eq(self, R.without([-0], [0]).length, 1)
    #     eq(self, R.without([NaN], [NaN]).length, 0)
    #     eq(self, R.without([[1]], [[1]]).length, 0)
    #     eq(self, R.without([Just([42])], [Just([42])]).length, 0)


if __name__ == '__main__':
    unittest.main()
