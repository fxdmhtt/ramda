# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_forEachObjIndexed(unittest.TestCase):
    def setUp(self):
        self.obj = { 'x': 1, 'y': 2, 'z': 123 }

    def test_performs_the_passed_in_function_on_each_key_and_value_of_the_object(self):
        sideEffect = {}
        def function(value, key):
            sideEffect[key] = value
        R.forEachObjIndexed(function, self.obj)
        eq(self, sideEffect, self.obj)

    def test_returns_the_original_object(self):
        s = ''
        def function(value):
            nonlocal s
            s += str(value)
        eq(self, R.forEachObjIndexed(function, self.obj), self.obj)
        eq(self, '12123', s)


if __name__ == '__main__':
    unittest.main()
