# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_length(unittest.TestCase):
    def test_returns_the_length_of_a_list(self):
        eq(self, R.length([]), 0)
        eq(self, R.length(['a', 'b', 'c', 'd']), 4)

    def test_returns_the_length_of_a_string(self):
        eq(self, R.length(''), 0)
        eq(self, R.length('xyz'), 3)

    def test_returns_the_length_of_a_function(self):
        eq(self, R.length(lambda: None), 0)
        eq(self, R.length(lambda x, y, z: z), 3)

    def test_returns_the_length_of_an_arguments_object(self):
        eq(self, R.length((lambda *arguments: list(arguments))()), 0)
        eq(self, R.length((lambda *arguments: list(arguments))('x', 'y', 'z')), 3)

    def test_returns_NaN_for_value_of_unexpected_type(self):
        eq(self, R.identical(float('nan'), R.length(0)), True)
        eq(self, R.identical(float('nan'), R.length({})), True)
        eq(self, R.identical(float('nan'), R.length(None)), True)
        eq(self, R.identical(float('nan'), R.length(None)), True)

    def test_returns_NaN_for_length_property_of_unexpected_type(self):
        eq(self, R.identical(float('nan'), R.length({'length': ''})), True)
        eq(self, R.identical(float('nan'), R.length({'length': '1.23'})), True)
        eq(self, R.identical(float('nan'), R.length({'length': None})), True)
        eq(self, R.identical(float('nan'), R.length({'length': None})), True)
        eq(self, R.identical(float('nan'), R.length({})), True)


if __name__ == '__main__':
    unittest.main()
