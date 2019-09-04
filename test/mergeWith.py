# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_mergeWith(unittest.TestCase):
    def setUp(self):
        self.last = lambda x, y: y

    def test_takes_two_objects_merges_their_own_properties_and_returns_a_new_object(self):
        a = {'w': 1, 'x': 2}
        b = {'y': 3, 'z': 4}
        self.assertEqual(R.mergeWith(self.last, a, b), {'w': 1, 'x': 2, 'y': 3, 'z': 4})

    def test_applies_the_provided_function_to_the_value_from_the_first_object_and_the_value_from_the_second_object_to_determine_the_value_for_keys_that_exist_in_both_objects(self):
        a = {'x': 'a', 'y': 'c'}
        b = {'x': 'b', 'z': 'd'}
        c = R.mergeWith(lambda a, b: a + b, a, b)
        self.assertEqual(c, {'x': 'ab', 'y': 'c', 'z': 'd'})

    def test_is_not_destructive(self):
        a = {'w': 1, 'x': 2}
        res = R.mergeWith(self.last, a, {'x': 5})
        self.assertIsNot(a, res)
        self.assertEqual(res, {'w': 1, 'x': 5})

    # def test_reports_only_own_properties(self):
    #     function Cla() {}
    #     Cla.prototype.x = 5
    #     self.assertEqual(R.mergeWith(self.last, Cla(), {'w': 1, 'x': 2}), {'w': 1, 'x': 2})
    #     self.assertEqual(R.mergeWith(self.last, {'w': 1, 'x': 2}, Cla()), {'w': 1, 'x': 2})
    #     self.assertEqual(R.mergeWith(self.last, Cla(), {'w': 1}), {'w': 1})


if __name__ == '__main__':
    unittest.main()
