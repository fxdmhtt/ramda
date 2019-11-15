# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_reject(unittest.TestCase):
    def setUp(self):
        self.even = lambda x: x % 2 == 0

    def test_reduces_an_array_to_those_not_matching_a_filter(self):
        eq(self, R.reject(self.even, [1, 2, 3, 4, 5]), [1, 3, 5])

    def test_returns_an_empty_array_if_no_element_matches(self):
        eq(self, R.reject(lambda x: x < 100, [1, 9, 99]), [])

    def test_returns_an_empty_array_if_asked_to_filter_an_empty_array(self):
        eq(self, R.reject(lambda x: x > 100, []), [])

    def test_returns_an_empty_array_if_no_element_matches(self):
        eq(self, R.reject(lambda x: x < 100, [1, 9, 99]), [])

    def test_returns_an_empty_array_if_asked_to_filter_an_empty_array(self):
        eq(self, R.reject(lambda x: x > 100, []), [])

    def test_filters_objects(self):
        eq(self, R.reject(R.equals(0), {}), {})
        eq(self, R.reject(R.equals(0), {'x': 0, 'y': 0, 'z': 0}), {})
        eq(self, R.reject(R.equals(0), {'x': 1, 'y': 0, 'z': 0}), {'x': 1})
        eq(self, R.reject(R.equals(0), {'x': 1, 'y': 2, 'z': 0}), {'x': 1, 'y': 2})
        eq(self, R.reject(R.equals(0), {'x': 1, 'y': 2, 'z': 3}), {'x': 1, 'y': 2, 'z': 3})

    # def test_dispatches_to_filter_method(self):
    #     function Nothing() {}
    #     Nothing.value = Nothing()
    #     Nothing.prototype.filter = function() {
    #         return this
    #     }

    #     function Just(x) { this.value = x }
    #     Just.prototype.filter = function(pred) {
    #         return pred(this.value) ? this : Nothing.value
    #     }

    #     m = Just(42)
    #     eq(self, R.filter(R.T, m), m)
    #     eq(self, R.filter(R.F, m), Nothing.value)
    #     eq(self, R.reject(R.T, m), Nothing.value)
    #     eq(self, R.reject(R.F, m), m)


if __name__ == '__main__':
    unittest.main()
