# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_propEq(unittest.TestCase):
    def setUp(self):
        self.obj1 = {'name': 'Abby', 'age': 7, 'hair': 'blond'}
        self.obj2 = {'name': 'Fred', 'age': 12, 'hair': 'brown'}

    def test_determines_whether_a_particular_property_matches_a_given_value_for_a_specific_object(self):
        eq(self, R.propEq('name', 'Abby', self.obj1), True)
        eq(self, R.propEq('hair', 'brown', self.obj2), True)
        eq(self, R.propEq('hair', 'blond', self.obj2), False)

    # def test_has_R.equals_semantics(self):
    #     function Just(x) { this.value = x }
    #     Just.prototype.equals = function(x) {
    #         return x instanceof Just && R.equals(x.value, this.value)
    #     }

    #     eq(self, R.propEq('value', 0, {value: -0}), False)
    #     eq(self, R.propEq('value', -0, {value: 0}), False)
    #     eq(self, R.propEq('value', NaN, {value: NaN}), True)
    #     eq(self, R.propEq('value', Just([42]), {value: Just([42])}), True)

    def test_returns_False_if_called_with_a_None_or_None_object(self):
        eq(self, R.propEq('name', 'Abby', None), False)
        eq(self, R.propEq('name', 'Abby', None), False)


if __name__ == '__main__':
    unittest.main()
