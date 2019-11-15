# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest
import random

class Test_curry(unittest.TestCase):
    def test_curries_a_single_value(self):
        f = R.curry(lambda a, b, c, d: (a + b * c) / d) # f(12, 3, 6, 2) == 15
        g = f(12)
        eq(self, g(3, 6, 2), 15.0)

    def test_curries_multiple_values(self):
        f = R.curry(lambda a, b, c, d: (a + b * c) / d) # f(12, 3, 6, 2) == 15
        g = f(12, 3)
        eq(self, g(6, 2), 15.0)
        h = f(12, 3, 6)
        eq(self, h(2), 15.0)

    def test_allows_further_currying_of_a_curried_function(self):
        f = R.curry(lambda a, b, c, d: (a + b * c) / d) # f(12, 3, 6, 2) == 15
        g = f(12)
        eq(self, g(3, 6, 2), 15.0)
        h = g(3)
        eq(self, h(6, 2), 15.0)
        eq(self, g(3, 6)(2), 15.0)

    def test_properly_reports_the_length_of_the_curried_function(self):
        f = R.curry(lambda a, b, c, d: (a + b * c) / d)
        eq(self, f.length, 4)
        g = f(12)
        eq(self, g.length, 3)
        h = g(3)
        eq(self, h.length, 2)
        eq(self, g(3, 6).length, 1)

    # def test_preserves_context(self):
    #     ctx = {x: 10}
    #     f = lambda a, b:{ a + b * this.x }
    #     g = R.curry(f)

    #     eq(self, g.call(ctx, 2, 4), 42)
    #     eq(self, g.call(ctx, 2).call(ctx, 4), 42)

    def test_supports_placeholder(self):
        f = lambda a, b, c: [a, b, c]
        g = R.curry(f)
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
        f = lambda a, b, c: [a, b, c]
        g = R.curry(f)
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
        from ..source.internal import sig
        @sig(names=['a', 'b', 'c'])
        def f(*arguments):
            a, b, c, *_ = *arguments, None, None, None
            return list(arguments[:])
        g = R.curry(f)

        eq(self, g(1, 2, 3), [1, 2, 3])
        eq(self, g(1, 2, 3, 4), [1, 2, 3, 4])
        eq(self, g(1, 2)(3, 4), [1, 2, 3, 4])
        eq(self, g(1)(2, 3, 4), [1, 2, 3, 4])
        eq(self, g(1)(2)(3, 4), [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
