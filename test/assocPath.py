# -*- 'coding': utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from shared.eq import eq

import unittest

class Test_assocPath(unittest.TestCase):
    def test_makes_a_shallow_clone_of_an_object_overriding_only_what_is_necessary_for_the_path(self):
        obj1 = {'a': {'b': 1, 'c': 2, 'd': {'e': 3}}, 'f': {'g': {'h': 4, 'i': [5, 6, 7], 'j': {'k': 6, 'l': 7}}}, 'm': 8}
        obj2 = R.assocPath(['f', 'g', 'i', 1], 42, obj1)
        eq(self, obj2['f']['g']['i'], [5, 42, 7])
        # Note: reference equality below!
        self.assertEqual(obj2['a'], obj1['a'])
        self.assertEqual(obj2['m'], obj1['m'])
        self.assertEqual(obj2['f']['g']['h'], obj1['f']['g']['h'])
        self.assertEqual(obj2['f']['g']['j'], obj1['f']['g']['j'])

    def test_is_the_equivalent_of_clone_and_setPath_if_the_property_is_not_on_the_original(self):
        obj1 = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4, 'f': 5}
        obj2 = R.assocPath(['x', 0, 'y'], 42, obj1)
        eq(self, obj2, {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4, 'f': 5, 'x': [{'y': 42}]})
        # Note: reference equality below!
        self.assertEqual(obj2['a'], obj1['a'])
        self.assertEqual(obj2['b'], obj1['b'])
        self.assertEqual(obj2['e'], obj1['e'])
        self.assertEqual(obj2['f'], obj1['f'])

    def test_empty_path_replaces_the_the_whole_object(self):
        eq(self, R.assocPath([], 3, {'a': 1, 'b': 2}), 3)

    def test_replaces_None_with_a_new_object(self):
        eq(self, R.assocPath(['foo', 'bar', 'baz'], 42, {'foo': None}), {'foo': {'bar': {'baz': 42}}})

    def test_replaces_None_with_a_new_object(self):
        eq(self, R.assocPath(['foo', 'bar', 'baz'], 42, {'foo': None}), {'foo': {'bar': {'baz': 42}}})


if __name__ == '__main__':
    unittest.main()
