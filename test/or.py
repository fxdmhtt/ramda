# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_or(unittest.TestCase):
    def test_compares_two_values_with_js_or(self):
        eq(self, R.or_(True, True), True)
        eq(self, R.or_(True, False), True)
        eq(self, R.or_(False, True), True)
        eq(self, R.or_(False, False), False)


if __name__ == '__main__':
    unittest.main()
