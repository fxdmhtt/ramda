# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_dissocPath(unittest.TestCase):
    def test_makes_a_shallow_clone_of_an_object_omitting_only_what_is_necessary_for_the_path(self):
        obj1 = {'a': {'b': 1, 'c': 2, 'd': {'e': 3}}, 'f': [{ 'g': 4}, {'h': 5, 'i': 6, 'j': {'k': 7, 'l': 8}}], 'm': 9}
        obj2 = R.dissocPath(['f', 1, 'i'], obj1)
        eq(self, obj2,
            {'a': {'b': 1, 'c': 2, 'd': {'e': 3}}, 'f': [{'g': 4}, {'h': 5, 'j': {'k': 7, 'l': 8}}], 'm': 9}
        )
        # Note: reference equality below!
        self.assertEqual(obj2['a'], obj1['a'])
        self.assertEqual(obj2['m'], obj1['m'])
        self.assertEqual(obj2['f'][0], obj1['f'][0])
        self.assertEqual(obj2['f'][1]['h'], obj1['f'][1]['h'])
        self.assertEqual(obj2['f'][1]['j'], obj1['f'][1]['j'])

    def test_does_not_try_to_omit_inner_properties_that_do_not_exist(self):
        obj1 = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4, 'f': 5}
        obj2 = R.dissocPath(['x', 0, 'z'], obj1)
        eq(self, obj2, {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4, 'f': 5})
        # Note: reference equality below!
        self.assertEqual(obj2['a'], obj1['a'])
        self.assertEqual(obj2['b'], obj1['b'])
        self.assertEqual(obj2['f'], obj1['f'])

    def test_leaves_an_empty_object_when_all_properties_omitted(self):
        obj1 = {'a': 1, 'b': {'c': 2}, 'd': 3}
        obj2 = R.dissocPath(['b', 'c'], obj1)
        eq(self, obj2,
            {'a': 1, 'b': {}, 'd': 3}
        )

    def test_leaves_an_empty_array_when_all_indexes_are_omitted(self):
        obj1 = {'a': 1, 'b': [2], 'd': 3}
        obj2 = R.dissocPath(['b', 0], obj1)
        eq(self, obj2,
            {'a': 1, 'b': [], 'd': 3}
        )

    # def test_flattens_properties_from_prototype(self):
    #     F = function() {}
    #     F.prototype.a = 1
    #     obj1 = F()
    #     obj1.b = {'c': 2, 'd': 3}
    #     obj2 = R.dissocPath(['b', 'c'], obj1)
    #     eq(self, obj2,
    #         {'a': 1, 'b': {'d': 3}}
    #     )

    def test_accepts_empty_path(self):
        eq(self, R.dissocPath([], {'a': 1, 'b': 2}), {'a': 1, 'b': 2})

    def test_allow_integer_to_be_used_as_key_for_object(self):
        eq(self, R.dissocPath([42], {'a': 1, 'b': 2, 42: 3}), {'a': 1, 'b': 2})


if __name__ == '__main__':
    unittest.main()
