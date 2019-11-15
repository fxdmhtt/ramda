# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_mergeWithKey(unittest.TestCase):
    def setUp(self):
        self.last = lambda k, x, y: y

    def test_takes_two_objects_merges_their_own_properties_and_returns_a_new_object(self):
        a = {'w': 1, 'x': 2}
        b = {'y': 3, 'z': 4}
        eq(self, R.mergeWithKey(self.last, a, b), {'w': 1, 'x': 2, 'y': 3, 'z': 4})

    def test_applies_the_provided_function_to_the_key_the_value_from_the_first_object_and_the_value_from_the_second_object_to_determine_the_value_for_keys_that_exist_in_both_objects(self):
        a = {'a': 'b', 'x': 'd'}
        b = {'a': 'c', 'y': 'e'}
        c = R.mergeWithKey(lambda k, a, b: k + a + b, a, b)
        eq(self, c, {'a': 'abc', 'x': 'd', 'y': 'e'})

    def test_is_not_destructive(self):
        a = {'w': 1, 'x': 2}
        res = R.mergeWithKey(self.last, a, {'x': 5})
        self.assertIsNot(a, res)
        eq(self, res, {'w': 1, 'x': 5})

    # def test_reports_only_own_properties(self):
    #     a = {'w': 1, 'x': 2}
    #     function Cla() {}
    #     Cla.prototype.x = 5
    #     eq(self, R.mergeWithKey(self.last, Cla(), a), {'w': 1, 'x': 2})
    #     eq(self, R.mergeWithKey(self.last, a, Cla()), {'w': 1, 'x': 2})


if __name__ == '__main__':
    unittest.main()
