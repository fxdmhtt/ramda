# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_startsWith(unittest.TestCase):
    def test_should_return_True_when_a_string_starts_with_the_provided_value(self):
        eq(self, R.startsWith('a', 'abc'), True)

    def test_should_return_True_when_a_long_string_starts_with_the_provided_value(self):
        eq(self, R.startsWith('astro', 'astrology'), True)

    def test_should_return_False_when_a_string_does_not_start_with_the_provided_value(self):
        eq(self, R.startsWith('b', 'abc'), False)

    def test_should_return_False_when_a_long_string_does_not_start_with_the_provided_value(self):
        eq(self, R.startsWith('stro', 'astrology'), False)

    def test_should_return_True_when_an_array_starts_with_the_provided_value(self):
        eq(self, R.startsWith(['a'], ['a', 'b', 'c']), True)

    def test_should_return_True_when_an_array_starts_with_the_provided_values(self):
        eq(self, R.startsWith(['a', 'b'], ['a', 'b', 'c']), True)

    def test_should_return_False_when_an_array_does_not_start_with_the_provided_value(self):
        eq(self, R.startsWith(['b'], ['a', 'b', 'c']), False)

    def test_should_return_False_when_an_array_does_not_start_with_the_provided_values(self):
        eq(self, R.startsWith(['b', 'c'], ['a', 'b', 'c']), False)


if __name__ == '__main__':
    unittest.main()
