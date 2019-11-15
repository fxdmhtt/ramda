# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_split(unittest.TestCase):
    def test_splits_a_string_into_an_array(self):
        eq(self, R.split('.', 'a.b.c.xyz.d'), ['a', 'b', 'c', 'xyz', 'd'])

    def test_the_split_string_can_be_arbitrary(self):
        eq(self, R.split('at', 'The Cat in the Hat sat on the mat'), ['The C', ' in the H', ' s', ' on the m', ''])


if __name__ == '__main__':
    unittest.main()
