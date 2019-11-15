# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_eqBy(unittest.TestCase):
    def test_determines_whether_two_values_map_to_the_same_value_in_the_codomain(self):
        eq(self, R.eqBy(abs, 5, 5), True)
        eq(self, R.eqBy(abs, 5, -5), True)
        eq(self, R.eqBy(abs, -5, 5), True)
        eq(self, R.eqBy(abs, -5, -5), True)
        eq(self, R.eqBy(abs, 42, 99), False)

    # def test_has_R.equals_semantics(self):
    #     function Just(x) { this.value = x }
    #     Just.prototype.equals = function(x) {
    #         return x instanceof Just && R.equals(x.value, this.value)
    #     }

    #     eq(self, R.eqBy(R.identity, 0, -0), False)
    #     eq(self, R.eqBy(R.identity, -0, 0), False)
    #     eq(self, R.eqBy(R.identity, NaN, NaN), True)
    #     eq(self, R.eqBy(R.identity, Just([42]), Just([42])), True)


if __name__ == '__main__':
    unittest.main()
