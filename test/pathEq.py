# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_pathEq(unittest.TestCase):
    def setUp(self):
        self.obj = {
            'a': 1,
            'b': [{
                'ba': 2
            }, {
                'ba': 3
            }]
        }

    def test_returns_True_if_the_path_matches_the_value(self):
        eq(self, R.pathEq(['a'], 1, self.obj), True)
        eq(self, R.pathEq(['b', 1, 'ba'], 3, self.obj), True)

    def test_returns_False_for_non_matches(self):
        eq(self, R.pathEq(['a'], '1', self.obj), False)
        eq(self, R.pathEq(['b', 0, 'ba'], 3, self.obj), False)

    def test_returns_False_for_non_existing_values(self):
        eq(self, R.pathEq(['c'], 'foo', self.obj), False)
        eq(self, R.pathEq(['c', 'd'], 'foo', self.obj), False)

    def test_accepts_empty_path(self):
        eq(self, R.pathEq([], 42, {'a': 1, 'b': 2}), False)
        eq(self, R.pathEq([], self.obj, self.obj), True)

    # def test_has_R.equals_semantics(self):
    #     function Just(x) { this.value = x }
    #     Just.prototype.equals = function(x) {
    #         return x instanceof Just && R.equals(x.value, this.value)
    #     }

    #     eq(self, R.pathEq(['value'], 0, {value: -0}), False)
    #     eq(self, R.pathEq(['value'], -0, {value: 0}), False)
    #     eq(self, R.pathEq(['value'], NaN, {value: NaN}), True)
    #     eq(self, R.pathEq(['value'], Just([42]), {value: Just([42])}), True)


if __name__ == '__main__':
    unittest.main()
