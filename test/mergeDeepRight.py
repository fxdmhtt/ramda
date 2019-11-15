# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_mergeDeepRight(unittest.TestCase):
    def test_takes_two_objects_recursively_merges_their_own_properties_and_returns_a_new_object(self):
        a = { 'w': 1, 'x': 2, 'y': { 'z': 3 }}
        b = { 'a': 4, 'b': 5, 'c': { 'd': 6 }}
        eq(self, R.mergeDeepRight(a, b), { 'w': 1, 'x': 2, 'y': { 'z': 3 }, 'a': 4, 'b': 5, 'c': { 'd': 6 }})

    def test_overrides_properties_in_the_first_object_with_properties_in_the_second_object(self):
        a = { 'a': { 'b': 1, 'c': 2 }, 'y': 0 }
        b = { 'a': { 'b': 3, 'd': 4 }, 'z': 0 }
        eq(self, R.mergeDeepRight(a, b), { 'a': { 'b': 3, 'c': 2, 'd': 4 }, 'y': 0, 'z': 0 })

    def test_is_not_destructive(self):
        a = { 'w': 1, 'x': { 'y': 2 }}
        res = R.mergeDeepRight(a, { 'x': { 'y': 3 }})
        self.assertIsNot(a, res)
        self.assertIsNot(a['x'], res['x'])
        eq(self, res, { 'w': 1, 'x': { 'y': 3 }})

    # def test_reports_only_own_properties(self):
    #     a = { 'w': 1, 'x': { 'y': 2 }}
    #     function Cla() {}
    #     Cla.prototype.y = 5
    #     eq(self, R.mergeDeepRight({ 'x': Cla() }, a), { 'w': 1, 'x': { 'y': 2 }})
    #     eq(self, R.mergeDeepRight(a, { 'x': Cla() }), { 'w': 1, 'x': { 'y': 2 }})


if __name__ == '__main__':
    unittest.main()
