# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_pathOr(unittest.TestCase):
    def setUp(self):
        self.deepObject = {'a': {'b': {'c': 'c'}}, 'FalseVal': False, 'NoneVal': None, 'NoneVal': None, 'arrayVal': ['arr']}

    def test_takes_a_path_and_an_object_and_returns_the_value_at_the_path_or_the_default_value(self):
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
        eq(self, R.pathOr('Unknown', ['a', 'b', 'c'], obj), 100)
        eq(self, R.pathOr('Unknown', [], obj), obj)
        eq(self, R.pathOr('Unknown', ['a', 'e', 'f', 1], obj), 101)
        eq(self, R.pathOr('Unknown', ['j', 0], obj), 'J')
        eq(self, R.pathOr('Unknown', ['j', 1], obj), 'Unknown')
        eq(self, R.pathOr('Unknown', ['a', 'b', 'c'], None), 'Unknown')

    def test_gets_a_deep_propertys_value_from_objects(self):
        eq(self, R.pathOr('Unknown', ['a', 'b', 'c'], self.deepObject), 'c')
        eq(self, R.pathOr('Unknown', ['a'], self.deepObject), self.deepObject['a'])

    def test_returns_the_default_value_for_items_not_found(self):
        eq(self, R.pathOr('Unknown', ['a', 'b', 'foo'], self.deepObject), 'Unknown')
        eq(self, R.pathOr('Unknown', ['bar'], self.deepObject), 'Unknown')

    def test_returns_the_default_value_for_None_None(self):
        eq(self, R.pathOr('Unknown', ['toString'], None), 'Unknown')
        eq(self, R.pathOr('Unknown', ['toString'], None), 'Unknown')

    # def test_works_with_falsy_items(self):
    #     eq(self, R.pathOr('Unknown', ['toString'], False), Boolean.prototype.toString)


if __name__ == '__main__':
    unittest.main()
