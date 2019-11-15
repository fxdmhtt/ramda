# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_init(unittest.TestCase):
    def test_returns_all_but_the_last_element_of_an_ordered_collection(self):
        eq(self, R.init([1, 2, 3]), [1, 2])
        eq(self, R.init([2, 3]), [2])
        eq(self, R.init([3]), [])
        eq(self, R.init([]), [])

        eq(self, R.init('abc'), 'ab')
        eq(self, R.init('bc'), 'b')
        eq(self, R.init('c'), '')
        eq(self, R.init(''), '')

    def test_throws_if_applied_to_None_or_None(self):
        with self.assertRaises(TypeError):
            R.init(None)

    def test_handles_array_like_object(self):
        args = (lambda *arguments: list(arguments))(1, 2, 3, 4, 5)
        eq(self, R.init(args), [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
