# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_assoc(unittest.TestCase):
    def test_makes_a_shallow_clone_of_an_object_overriding_only_the_specified_property(self):
        obj1 = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4, 'f': 5}
        obj2 = R.assoc('e', {'x': 42}, obj1)
        eq(self, obj2, {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': {'x': 42}, 'f': 5})
        # Note: reference equality below!
        self.assertEqual(obj2['a'], obj1['a'])
        self.assertEqual(obj2['b'], obj1['b'])
        self.assertEqual(obj2['f'], obj1['f'])

    def test_is_the_equivalent_of_clone_and_set_if_the_property_is_not_on_the_original(self):
        obj1 = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4, 'f': 5}
        obj2 = R.assoc('z', {'x': 42}, obj1)
        eq(self, obj2, {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4, 'f': 5, 'z': {'x': 42}})
        # Note: reference equality below!
        self.assertEqual(obj2['a'], obj1['a'])
        self.assertEqual(obj2['b'], obj1['b'])
        self.assertEqual(obj2['f'], obj1['f'])


if __name__ == '__main__':
    unittest.main()
