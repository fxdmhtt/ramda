# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_invert(unittest.TestCase):
    def test_takes_a_list_or_object_and_returns_an_object_of_lists(self):
        self.assertTrue(isinstance(R.invert([]), dict))
        self.assertTrue(isinstance(R.invert({}), dict))

        inverted = R.invert([0])
        keys = R.keys(inverted)
        eq(self, R.is_(list, inverted[keys.pop()]), True)

    def test_returns_an_empty_object_when_applied_to_a_primitive(self):
        eq(self, R.invert(42), {})
        eq(self, R.invert('abc'), {})

    def test_returns_an_empty_object_when_applied_to_None_None(self):
        eq(self, R.invert(None), {})

    def test_returns_the_input_s_values_as_keys_and_keys_as_values_of_an_array(self):
        eq(self, R.invert(['a', 'b', 'c']),             {'a':[0], 'b':[1], 'c':[2]})
        eq(self, R.invert({'x':'a', 'y':'b', 'z':'c'}), {'a':['x'], 'b':['y'], 'c':['z']})

    def test_puts_keys_that_have_the_same_value_into_the_appropriate_an_array(self):
        eq(self, R.invert(['a', 'b', 'a']), {'a':[0, 2], 'b':[1]})

        inverted = R.invert({'x':'a', 'y':'b', 'z':'a', '_id':'a'})
        eq(self, R.indexOf('x', inverted['a']) >= 0, True)
        eq(self, R.indexOf('z', inverted['a']) >= 0, True)
        eq(self, R.indexOf('_id', inverted['a']) >= 0, True)
        eq(self, inverted['b'], ['y'])

    # this one is more of a sanity check
    def test_is_not_destructive(self):
        input = {'x':'a', 'y':'b', 'z':'a', '_id':'a'}
        R.invert(input)
        eq(self, input, {'x':'a', 'y':'b', 'z':'a', '_id':'a'})

    def test_ignores_inherited_properties(self):
        eq(self, R.invert({'x': 'hasOwnProperty'}), {
            'hasOwnProperty': ['x']
        })


if __name__ == '__main__':
    unittest.main()
