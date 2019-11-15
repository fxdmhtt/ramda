# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_cond(unittest.TestCase):
    def test_returns_a_function(self):
        self.assertTrue(callable(R.cond([])))

    def test_returns_a_conditional_function(self):
        fn = R.cond([
            [R.equals(0), R.always('water freezes at 0°C')],
            [R.equals(100), R.always('water boils at 100°C')],
            [R.T, lambda temp: 'nothing special happens at ' + str(temp) + '°C']
        ])
        eq(self, fn(0), 'water freezes at 0°C')
        eq(self, fn(50), 'nothing special happens at 50°C')
        eq(self, fn(100), 'water boils at 100°C')

    def test_returns_a_function_which_returns_None_if_none_of_the_predicates_matches(self):
        fn = R.cond([
            [R.equals('foo'), R.always(1)],
            [R.equals('bar'), R.always(2)]
        ])
        eq(self, fn('quux'), None)

    def test_predicates_are_tested_in_order(self):
        fn = R.cond([
            [R.T, R.always('foo')],
            [R.T, R.always('bar')],
            [R.T, R.always('baz')]
        ])
        eq(self, fn(), 'foo')

    def test_forwards_all_arguments_to_predicates_and_to_transformers(self):
        fn = R.cond([
            [lambda _, x: x == 42, lambda *arguments: len(arguments)]
        ])
        eq(self, fn(21, 42, 84), 3)

    def test_retains_highest_predicate_arity(self):
        fn = R.cond([
            [R.nAry(2, R.T), R.T],
            [R.nAry(3, R.T), R.T],
            [R.nAry(1, R.T), R.T]
        ])
        eq(self, fn.length, 3)


if __name__ == '__main__':
    unittest.main()
