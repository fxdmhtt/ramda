# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_match(unittest.TestCase):
    def setUp(self):
        self.re = r'[A-Z]\d\d\-[a-zA-Z]+'
        self.matching = 'B17-afn'
        self.notMatching = 'B1-afn'

    def test_determines_whether_a_string_matches_a_regex(self):
        eq(self, len(R.match(self.re, self.matching)), 1)
        eq(self, R.match(self.re, self.notMatching), [])

    def test_defaults_to_a_different_empty_array_each_time(self):
        first = R.match(self.re, self.notMatching)
        second = R.match(self.re, self.notMatching)
        self.assertIsNot(first, second)

    def test_throws_on_None_input(self):
        with self.assertRaises(TypeError):
            R.match(self.re, None)


if __name__ == '__main__':
    unittest.main()
