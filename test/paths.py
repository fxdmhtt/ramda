# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_paths(unittest.TestCase):
    def setUp(self):
        self.obj = {
            'a': {
                'b': {
                    'c': 1,
                    'd': 2
                }
            },
            'p': [{'q': 3}, 'Hi'],
            'x': {
                'y': 'Alice',
                'z': [[{}]]
            }
        }

    def test_takes_paths_and_returns_values_at_those_paths(self):
        eq(self, R.paths([['a', 'b', 'c'], ['x', 'y']], self.obj), [1, 'Alice'])
        eq(self, R.paths([['a', 'b', 'd'], ['p', 'q']], self.obj), [2, None])

    def test_takes_a_paths_that_contains_indices_into_arrays(self):
        eq(self, R.paths([['p', 0, 'q'], ['x', 'z', 0, 0]], self.obj), [3, {}])
        eq(self, R.paths([['p', 0, 'q'], ['x', 'z', 2, 1]], self.obj), [3, None])

    def test_takes_a_path_that_contains_negative_indices_into_arrays(self):
        eq(self, R.paths([['p', -2, 'q'], ['p', -1]], self.obj), [3, 'Hi'])
        eq(self, R.paths([['p', -4, 'q'], ['x', 'z', -1, 0]], self.obj), [None, {}])

    def test_gets_a_deep_propertys_value_from_objects(self):
        eq(self, R.paths([['a', 'b']], self.obj), [self.obj['a']['b']])
        eq(self, R.paths([['p', 0]], self.obj), [self.obj['p'][0]])

    def test_returns_None_for_items_not_found(self):
        eq(self, R.paths([['a', 'x', 'y']], self.obj), [None])
        eq(self, R.paths([['p', 2]], self.obj), [None])


if __name__ == '__main__':
    unittest.main()
