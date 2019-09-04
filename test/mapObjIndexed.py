# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_mapObjIndexed(unittest.TestCase):
    def setUp(self):
        self.times2 = lambda x: x * 2
        self.addIndexed = lambda x, key: str(x) + key
        def function(x, key):
            vowels = ['a', 'e', 'i', 'o', 'u']
            return x * x if R.includes(key, vowels) else x
        self.squareVowels = function

    def test_works_just_like_a_normal_mapObj(self):
        eq(self, R.mapObjIndexed(self.times2, {'a': 1, 'b': 2, 'c': 3, 'd': 4}), {'a': 2, 'b': 4, 'c': 6, 'd': 8})

    def test_passes_the_index_as_a_second_parameter_to_the_callback(self):
        eq(self, R.mapObjIndexed(self.addIndexed, {'a': 8, 'b': 6, 'c': 7, 'd': 5, 'e': 3, 'f': 0, 'g': 9}),
            {'a': '8a', 'b': '6b', 'c': '7c', 'd': '5d', 'e': '3e', 'f': '0f', 'g': '9g'}
        )

    def test_passes_the_entire_list_as_a_third_parameter_to_the_callback(self):
        eq(self, R.mapObjIndexed(self.squareVowels, {'a': 8, 'b': 6, 'c': 7, 'd': 5, 'e': 3, 'f': 0, 'g': 9}),
            {'a': 64, 'b': 6, 'c': 7, 'd': 5, 'e': 9, 'f': 0, 'g': 9}
        )


if __name__ == '__main__':
    unittest.main()
