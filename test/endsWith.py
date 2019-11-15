# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_startsWith(unittest.TestCase):
    def test_should_return_True_when_a_string_ends_with_the_provided_value(self):
        eq(self, R.endsWith('c', 'abc'), True)

    def test_should_return_True_when_a_long_string_ends_with_the_provided_value(self):
        eq(self, R.endsWith('ology', 'astrology'), True)

    def test_should_return_False_when_a_string_does_not_end_with_the_provided_value(self):
        eq(self, R.endsWith('b', 'abc'), False)

    def test_should_return_False_when_a_long_string_does_not_end_with_the_provided_value(self):
        eq(self, R.endsWith('olog', 'astrology'), False)

    def test_should_return_True_when_an_array_ends_with_the_provided_value(self):
        eq(self, R.endsWith(['c'], ['a', 'b', 'c']), True)

    def test_should_return_True_when_an_array_ends_with_the_provided_values(self):
        eq(self, R.endsWith(['b', 'c'], ['a', 'b', 'c']), True)

    def test_should_return_False_when_an_array_does_not_end_with_the_provided_value(self):
        eq(self, R.endsWith(['b'], ['a', 'b', 'c']), False)

    def test_should_return_False_when_an_array_does_not_end_with_the_provided_values(self):
        eq(self, R.endsWith(['a', 'b'], ['a', 'b', 'c']), False)


if __name__ == '__main__':
    unittest.main()
