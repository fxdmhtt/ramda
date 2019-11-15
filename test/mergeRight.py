# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_mergeRight(unittest.TestCase):
    def test_takes_two_objects_merges_their_own_properties_and_returns_a_new_object(self):
        a = {'w': 1, 'x': 2}
        b = {'y': 3, 'z': 4}
        self.assertEqual(R.mergeRight(a, b), {'w': 1, 'x': 2, 'y': 3, 'z': 4})

    def test_overrides_properties_in_the_first_object_with_properties_in_the_second_object(self):
        a = {'w': 1, 'x': 2}
        b = {'w': 100, 'y': 3, 'z': 4}
        self.assertEqual(R.mergeRight(a, b), {'w': 100, 'x': 2, 'y': 3, 'z': 4})

    def test_is_not_destructive(self):
        a = {'w': 1, 'x': 2}
        res = R.mergeRight(a, {'x': 5})
        self.assertIsNot(a, res)
        self.assertEqual(res, {'w': 1, 'x': 5})

    # def test_reports_only_own_properties(self):
    #     a = {'w': 1, 'x': 2}
    #     function Cla() {}
    #     Cla.prototype['x'] = 5
    #     self.assertEqual(R.mergeRight(Cla(), a), {'w': 1, 'x': 2})
    #     self.assertEqual(R.mergeRight(a, Cla()), {'w': 1, 'x': 2})

    def test_is_shallow(self):
        a = { 'x': { 'u': 1, 'v': 2 }, 'y': 0 }
        b = { 'x': { 'u': 3, 'w': 4 }, 'z': 0 }
        res = R.mergeRight(a, b)
        self.assertEqual(b['x'], res['x'])
        self.assertEqual(res, { 'x': { 'u': 3, 'w': 4 }, 'y': 0, 'z': 0 })


if __name__ == '__main__':
    unittest.main()
