# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_path(unittest.TestCase):
    def setUp(self):
        self.deepObject = {'a': {'b': {'c': 'c'}}, 'FalseVal': False, 'NoneVal': None, 'NoneVal': None, 'arrayVal': ['arr']}

    def test_takes_a_path_and_an_object_and_returns_the_value_at_the_path_or_None(self):
        obj = {
            'a': {
                'b': {
                    'c': 100,
                    'd': 200
                },
                'e': {
                    'f': [100, 101, 102],
                    'g': 'G'
                },
                'h': 'H'
            },
            'i': 'I',
            'j': ['J']
        }
        eq(self, R.path(['a', 'b', 'c'], obj), 100)
        eq(self, R.path([], obj), obj)
        eq(self, R.path(['a', 'e', 'f', 1], obj), 101)
        eq(self, R.path(['j', 0], obj), 'J')
        eq(self, R.path(['j', 1], obj), None)

    def test_takes_a_path_that_contains_indices_into_arrays(self):
        obj = {
            'a': [[{}], [{'x': 'first'}, {'x': 'second'}, {'x': 'third'}, {'x': 'last'}]]
        }
        eq(self, R.path(['a', 0, 0], obj), {})
        eq(self, R.path(['a', 0, 1], obj), None)
        eq(self, R.path(['a', 1, 0, 'x'], obj), 'first')
        eq(self, R.path(['a', 1, 1, 'x'], obj), 'second')
        eq(self, R.path([0], ['A']), 'A')

    def test_takes_a_path_that_contains_negative_indices_into_arrays(self):
        eq(self, R.path(['x', -2], {'x': ['a', 'b', 'c', 'd']}), 'c')
        eq(self, R.path([-1, 'y'], [{'x': 1, 'y': 99}, {'x': 2, 'y': 98}, {'x': 3, 'y': 97}]), 97)

    def test_gets_a_deep_propertys_value_from_objects(self):
        eq(self, R.path(['a', 'b', 'c'], self.deepObject), 'c')
        eq(self, R.path(['a'], self.deepObject), self.deepObject['a'])

    def test_returns_None_for_items_not_found(self):
        eq(self, R.path(['a', 'b', 'foo'], self.deepObject), None)
        eq(self, R.path(['bar'], self.deepObject), None)
        eq(self, R.path(['a', 'b'], {'a': None}), None)

    # def test_works_with_falsy_items(self):
    #     eq(self, R.path(['toString'], False), str)


if __name__ == '__main__':
    unittest.main()
