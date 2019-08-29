# -*- coding: utf-8 -*-

from ... import source as R

def eq(self, actual, expected):
    self.assertIsNotNone(actual) and self.assertIsNotNone(expected)
    self.assertEqual(R.toString(actual), R.toString(expected))
