# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest
import random

class Test_curryN(unittest.TestCase):
    def setUp(self):
        self.source = lambda a, b, c, d=None: \
            a * b * c

    def test_accepts_an_arity(self):
        curried = R.curryN(3, self.source)
        eq(self, curried(1)(2)(3), 6)
        eq(self, curried(1, 2)(3), 6)
        eq(self, curried(1)(2, 3), 6)
        eq(self, curried(1, 2, 3), 6)

    def test_can_be_partially_applied(self):
        curry3 = R.curryN(3)
        curried = curry3(self.source)
        eq(self, curried.length, 3)
        eq(self, curried(1)(2)(3), 6)
        eq(self, curried(1, 2)(3), 6)
        eq(self, curried(1)(2, 3), 6)
        eq(self, curried(1, 2, 3), 6)

    # def test_preserves_context(self):
    #     ctx = {x: 10}
    #     f = lambda a, b:{ a + b * this.x }
    #     g = R.curryN(2, f)

    #     eq(self, g.call(ctx, 2, 4), 42)
    #     eq(self, g.call(ctx, 2).call(ctx, 4), 42)

    def test_supports_placeholder(self):
        f = lambda *arguments: list(arguments[:])
        g = R.curryN(3, f)
        _ = R.__

        eq(self, g(1)(2)(3), [1, 2, 3])
        eq(self, g(1)(2, 3), [1, 2, 3])
        eq(self, g(1, 2)(3), [1, 2, 3])
        eq(self, g(1, 2, 3), [1, 2, 3])

        eq(self, g(_, 2, 3)(1), [1, 2, 3])
        eq(self, g(1, _, 3)(2), [1, 2, 3])
        eq(self, g(1, 2, _)(3), [1, 2, 3])

        eq(self, g(1, _, _)(2)(3), [1, 2, 3])
        eq(self, g(_, 2, _)(1)(3), [1, 2, 3])
        eq(self, g(_, _, 3)(1)(2), [1, 2, 3])

        eq(self, g(1, _, _)(2, 3), [1, 2, 3])
        eq(self, g(_, 2, _)(1, 3), [1, 2, 3])
        eq(self, g(_, _, 3)(1, 2), [1, 2, 3])

        eq(self, g(1, _, _)(_, 3)(2), [1, 2, 3])
        eq(self, g(_, 2, _)(_, 3)(1), [1, 2, 3])
        eq(self, g(_, _, 3)(_, 2)(1), [1, 2, 3])

        eq(self, g(_, _, _)(_, _)(_)(1, 2, 3), [1, 2, 3])
        eq(self, g(_, _, _)(1, _, _)(_, _)(2, _)(_)(3), [1, 2, 3])

    def test_supports_functional_placeholder(self):
        f = lambda *arguments: list(arguments[:])
        g = R.curryN(3, f)
        _ = {'@@functional/placeholder': True, 'x': random.random()}

        eq(self, g(1)(2)(3), [1, 2, 3])
        eq(self, g(1)(2, 3), [1, 2, 3])
        eq(self, g(1, 2)(3), [1, 2, 3])
        eq(self, g(1, 2, 3), [1, 2, 3])

        eq(self, g(_, 2, 3)(1), [1, 2, 3])
        eq(self, g(1, _, 3)(2), [1, 2, 3])
        eq(self, g(1, 2, _)(3), [1, 2, 3])

        eq(self, g(1, _, _)(2)(3), [1, 2, 3])
        eq(self, g(_, 2, _)(1)(3), [1, 2, 3])
        eq(self, g(_, _, 3)(1)(2), [1, 2, 3])

        eq(self, g(1, _, _)(2, 3), [1, 2, 3])
        eq(self, g(_, 2, _)(1, 3), [1, 2, 3])
        eq(self, g(_, _, 3)(1, 2), [1, 2, 3])

        eq(self, g(1, _, _)(_, 3)(2), [1, 2, 3])
        eq(self, g(_, 2, _)(_, 3)(1), [1, 2, 3])
        eq(self, g(_, _, 3)(_, 2)(1), [1, 2, 3])

        eq(self, g(_, _, _)(_, _)(_)(1, 2, 3), [1, 2, 3])
        eq(self, g(_, _, _)(1, _, _)(_, _)(2, _)(_)(3), [1, 2, 3])

    def test_forwards_extra_arguments(self):
        f = lambda *arguments: list(arguments[:])
        g = R.curryN(3, f)

        eq(self, g(1, 2, 3), [1, 2, 3])
        eq(self, g(1, 2, 3, 4), [1, 2, 3, 4])
        eq(self, g(1, 2)(3, 4), [1, 2, 3, 4])
        eq(self, g(1)(2, 3, 4), [1, 2, 3, 4])
        eq(self, g(1)(2)(3, 4), [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
