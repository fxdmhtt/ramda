# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_eqProps(unittest.TestCase):
    def test_reports_whether_two_objects_have_the_same_value_for_a_given_property(self):
        eq(self, R.eqProps('name', {'name': 'fred', 'age': 10}, {'name': 'fred', 'age': 12}), True)
        eq(self, R.eqProps('name', {'name': 'fred', 'age': 10}, {'name': 'franny', 'age': 10}), False)

    # def test_has_R.equals_semantics(self):
    #     function Just(x) { this.value = x }
    #     Just.prototype.equals = function(x) {
    #         return x instanceof Just && R.equals(x.value, this.value)
    #     }

    #     eq(self, R.eqProps('value', {value: 0}, {value: -0}), False)
    #     eq(self, R.eqProps('value', {value: -0}, {value: 0}), False)
    #     eq(self, R.eqProps('value', {value: NaN}, {value: NaN}), True)
    #     eq(self, R.eqProps('value', {value: Just([42])}, {value: Just([42])}), True)


if __name__ == '__main__':
    unittest.main()
