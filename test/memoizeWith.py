# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_memoizeWith(unittest.TestCase):
    def test_calculates_the_value_for_a_given_input_only_once(self):
        ctr = 0
        def function(n):
            nonlocal ctr
            ctr += 1
            return n if n < 2 else fib(n - 2) + fib(n - 1)
        fib = R.memoizeWith(R.identity, function)
        result = fib(10)
        eq(self, result, 55)
        eq(self, ctr, 11) # fib(0), fib(1), ... fib(10), no memoization would take 177 iterations.

    def test_handles_multiple_parameters(self):
        f = R.memoizeWith(lambda a, b, c: \
            a + b + c
        , lambda a, b, c: a + ', ' + b + c)
        eq(self, f('Hello', 'World' , '!'), 'Hello, World!')
        eq(self, f('Goodbye', 'Cruel World' , '!!!'), 'Goodbye, Cruel World!!!')
        eq(self, f('Hello', 'how are you' , '?'), 'Hello, how are you?')
        eq(self, f('Hello', 'World' , '!'), 'Hello, World!')

    def test_does_not_rely_on_reported_arity(self):
        identity = R.memoizeWith(R.identity, lambda *arguments: arguments[0])
        eq(self, identity('x'), 'x')
        eq(self, identity('y'), 'y')

    def test_can_be_applied_to_Noneary_function(self):
        count = 0
        def function():
            nonlocal count
            count += 1
            return 42
        f = R.memoizeWith(R.identity, function)
        eq(self, f(), 42)
        eq(self, f(), 42)
        eq(self, f(), 42)
        eq(self, count, 1)

    def test_can_be_applied_to_function_with_optional_arguments(self):
        count = 0
        from ramda.internal import sig
        @sig(names=['a', 'b'])
        def concat(*arguments):
            a, b, *_ = *arguments, None, None
            nonlocal count
            count += 1
            if len(arguments) == 0: a = 'foo'
            if len(arguments) in [0, 1]: b = 'bar'
            return a + b
        f = R.memoizeWith(R.concat, concat)
        eq(self, f(), 'foobar')
        eq(self, f(), 'foobar')
        eq(self, f(), 'foobar')
        eq(self, count, 1)

    def test_retains_arity(self):
        f = R.memoizeWith(R.concat, lambda a, b:{ a + b })
        eq(self, f.length, 2)


if __name__ == '__main__':
    unittest.main()
