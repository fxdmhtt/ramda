# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_tryCatch(unittest.TestCase):
    def setUp(self):
        self.headX = lambda ls: \
            ls[0]['x']

        self.catcher = lambda *_: \
            10101

    def test_takes_two_functions_and_return_a_function(self):
        mayThrow = R.tryCatch(self.headX, self.catcher)
        self.assertTrue(callable(mayThrow))

    def test_returns_a_function_with_the_same_arity_as_the_tryer_function(self):
        a1 = lambda a: a
        a2 = lambda a, b: b
        a3 = lambda a, b, c: c
        a4 = lambda a, b, c, d: d

        eq(self, R.tryCatch(a1, self.catcher).length, 1)
        eq(self, R.tryCatch(a2, self.catcher).length, 2)
        eq(self, R.tryCatch(a3, self.catcher).length, 3)
        eq(self, R.tryCatch(a4, self.catcher).length, 4)

    def test_returns_the_value_of_the_first_function_if_it_does_not_throw(self):
        mayThrow = R.tryCatch(self.headX, self.catcher)
        eq(self, mayThrow([{'x': 10}, {'x': 20}, {'x': 30}]), 10)

    def test_returns_the_value_of_the_second_function_if_the_first_function_throws(self):
        def throw10(*_):
            raise Exception(10)

        def eCatcher(e):
            return e.args[0]

        mayThrow = R.tryCatch(self.headX, self.catcher)
        eq(self, mayThrow([]), 10101)

        willThrow = R.tryCatch(throw10, eCatcher)
        eq(self, willThrow([]), 10)
        eq(self, willThrow([{}, {}, {}]), 10)

    def test_the_second_function_gets_passed_the_error_object_and_the_same_arguments_as_the_first_function(self):
        def thrower(a, b, c):
            raise Exception('throwerError')

        def catch3(e, a, b, c):
            return ' '.join([e.args[0], a, b, c])

        mayThrow = R.tryCatch(thrower, catch3)
        eq(self, mayThrow('A', 'B', 'C'), 'throwerError A B C')


if __name__ == '__main__':
    unittest.main()
