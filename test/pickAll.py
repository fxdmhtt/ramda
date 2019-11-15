# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_pickAll(unittest.TestCase):
    def setUp(self):
        self.obj = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}

    def test_copies_the_named_properties_of_an_object_to_the_new_object(self):
        eq(self, R.pickAll(['a', 'c', 'f'], self.obj), {'a': 1, 'c': 3, 'f': 6})

    def test_includes_properties_not_present_on_the_input_object(self):
        eq(self, R.pickAll(['a', 'c', 'g'], self.obj), {'a': 1, 'c': 3, 'g': None})


if __name__ == '__main__':
    unittest.main()
