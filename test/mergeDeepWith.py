# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_mergeDeepWith(unittest.TestCase):
    def setUp(self):
        self.last = lambda x, y: y

    def test_takes_two_objects_recursively_merges_their_own_properties_and_returns_a_new_object(self):
        a = { 'w': 1, 'x': 2, 'y': { 'z': 3 }}
        b = { 'a': 4, 'b': 5, 'c': { 'd': 6 }}
        eq(self, R.mergeDeepWith(self.last, a, b), { 'w': 1, 'x': 2, 'y': { 'z': 3 }, 'a': 4, 'b': 5, 'c': { 'd': 6 }})

    def test_applies_the_provided_function_to_the_value_from_the_first_object_and_the_value_from_the_second_object_to_determine_the_value_for_keys_that_exist_in_both_objects(self):
        a = { 'a': { 'b': 'B1', 'c': 'C' }, 'y': 'Y' }
        b = { 'a': { 'b': 'B2', 'd': 'D' }, 'z': 'Z' }
        c = R.mergeDeepWith(lambda a, b: a + b, a, b)
        eq(self, c, { 'a': { 'b': 'B1B2', 'c': 'C', 'd': 'D' }, 'y': 'Y', 'z': 'Z' })

    def test_is_not_destructive(self):
        a = { 'w': 1, 'x': { 'y': 2 }}
        res = R.mergeDeepWith(self.last, a, { 'x': { 'y': 3 }})
        self.assertIsNot(a, res)
        self.assertIsNot(a['x'], res['x'])
        eq(self, res, { 'w': 1, 'x': { 'y': 3 }})

    # def test_reports_only_own_properties(self):
    #     a = { 'w': 1, 'x': { 'y': 2 }}
    #     function Cla() {}
    #     Cla.prototype.y = 5
    #     eq(self, R.mergeDeepWith(self.last, { 'x': Cla() }, a), { 'w': 1, 'x': { 'y': 2 }})
    #     eq(self, R.mergeDeepWith(self.last, a, { 'x': Cla() }), { 'w': 1, 'x': { 'y': 2 }})


if __name__ == '__main__':
    unittest.main()
