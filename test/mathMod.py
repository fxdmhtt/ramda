# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest
import math

class Test_mathMod(unittest.TestCase):
    def test_requires_integer_arguments(self):
        self.assertTrue(math.isnan(R.mathMod('s', 3)))
        self.assertTrue(math.isnan(R.mathMod(3, 's')))
        self.assertTrue(math.isnan(R.mathMod(12.2, 3)))
        self.assertTrue(math.isnan(R.mathMod(3, 12.2)))

    def test_behaves_differently_than_JS_modulo(self):
        # self.assertIsNot(R.mathMod(-17, 5), -17 % 5)
        self.assertIsNot(R.mathMod(17.2, 5), 17.2 % 5)
        self.assertIsNot(R.mathMod(17, -5), 17 % -5)

    def test_computes_the_True_modulo_function(self):
        eq(self, R.mathMod(-17, 5), 3)
        eq(self, R.identical(math.nan, R.mathMod(17, -5)), True)
        eq(self, R.identical(math.nan, R.mathMod(17, 0)), True)
        eq(self, R.identical(math.nan, R.mathMod(17.2, 5)), True)
        eq(self, R.identical(math.nan, R.mathMod(17, 5.5)), True)


if __name__ == '__main__':
    unittest.main()
