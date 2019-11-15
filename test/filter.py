# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_filter(unittest.TestCase):
    def setUp(self):
        self.even = lambda x: x % 2 == 0

    def test_reduces_an_array_to_those_matching_a_filter(self):
        self.assertSequenceEqual(list(R.filter(self.even, [1, 2, 3, 4, 5])), [2, 4])

    def test_returns_an_empty_array_if_no_element_matches(self):
        self.assertSequenceEqual(list(R.filter(lambda x: x > 100, [1, 9, 99])), [])

    def test_returns_an_empty_array_if_asked_to_filter_an_empty_array(self):
        self.assertSequenceEqual(list(R.filter(lambda x: x > 100, [])), [])

    def test_filters_objects(self):
        positive = lambda x: x > 0
        self.assertDictEqual(R.filter(positive, {}), {})
        self.assertDictEqual(R.filter(positive, {'x': 0, 'y': 0, 'z': 0}), {})
        self.assertDictEqual(R.filter(positive, {'x': 1, 'y': 0, 'z': 0}), {'x': 1})
        self.assertDictEqual(R.filter(positive, {'x': 1, 'y': 2, 'z': 0}), {'x': 1, 'y': 2})
        self.assertDictEqual(R.filter(positive, {'x': 1, 'y': 2, 'z': 3}), {'x': 1, 'y': 2, 'z': 3})

    def test_dispatches_to_passed_in_non_Array_object_with_a_filter_method(self):
        f = {'filter': lambda f: f('called f.filter')}
        self.assertSequenceEqual(list(R.filter(lambda s: s, f)), 'called f.filter')


if __name__ == '__main__':
    unittest.main()
