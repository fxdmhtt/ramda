# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_invertObj(unittest.TestCase):
    def test_takes_a_list_or_object_and_returns_an_object(self):
        self.assertTrue(isinstance(R.invertObj([]), dict))
        self.assertTrue(isinstance(R.invertObj({}), dict))

    def test_returns_an_empty_object_when_applied_to_a_primitive(self):
        eq(self, R.invertObj(42), {})
        eq(self, R.invertObj('abc'), {})

    def test_returns_an_empty_object_when_applied_to_None_None(self):
        eq(self, R.invertObj(None), {})

    def test_returns_the_input_s_values_as_keys_and_keys_as_values(self):
        eq(self, R.invertObj(['a', 'b', 'c']),             {'a':0, 'b':1, 'c':2})
        eq(self, R.invertObj({'x':'a', 'y':'b', 'z':'c'}), {'a':'x', 'b':'y', 'c':'z'})

    def test_prefers_the_last_key_found_when_handling_keys_with_the_same_value(self):
        eq(self, R.invertObj(['a', 'b', 'a']), {'a':2, 'b':1})
        eq(self, R.invertObj({'x':'a', 'y':'b', 'z':'a', '_id':'a'}), {'a': '_id', 'b': 'y'})

    # this one is more of a sanity check
    def test_is_not_destructive(self):
        input = {'x':'a', 'y':'b', 'z':'a', '_id':'a'}
        R.invertObj(input)
        eq(self, input, {'x':'a', 'y':'b', 'z':'a', '_id':'a'})


if __name__ == '__main__':
    unittest.main()
