# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest
from ..source.internal import sig

class Test_nAry(unittest.TestCase):
    def setUp(self):
        self.toArray = lambda args: list(args[:])

    def test_turns_multiple_argument_function_into_a_Noneary_one(self):
        fn = R.nAry(0, sig(names=list('xyz'))(lambda *arguments: self.toArray(arguments)))
        self.assertEqual(fn.length, 0)
        self.assertEqual(fn(1, 2, 3), [])

    def test_turns_multiple_argument_function_into_a_ternary_one(self):
        fn = R.nAry(3, sig(names=list('abcd'))(lambda *arguments: self.toArray(arguments)))
        self.assertEqual(fn.length, 3)
        self.assertEqual(fn(1, 2, 3, 4), [1, 2, 3])
        self.assertEqual(fn(1), [1, None, None])

    def test_creates_functions_of_arity_less_than_or_equal_to_ten(self):
        fn = R.nAry(10, lambda *arguments: self.toArray(arguments))
        self.assertEqual(fn.length, 10)
        self.assertEqual(fn(*R.range(0, 25)), R.range(0, 10))

        undefs = fn()
        ns = list(R.repeat(None, 10))
        self.assertEqual(len(undefs), len(ns))
        idx = len(undefs) - 1
        while idx >= 0:
            self.assertEqual(undefs[idx], ns[idx])
            idx -= 1

    def test_throws_if_n_is_greater_than_ten(self):
        with self.assertRaises(Exception):
            R.nAry(11, lambda *_: None)


if __name__ == '__main__':
    unittest.main()
