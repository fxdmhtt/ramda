# -*- coding: utf-8 -*-

__package__ = 'ramda.test.internal'

from ..shared.eq import eq
from ...source.__ import __ as _
from ...source.internal._curry3 import _curry3

import unittest
class Test__curry3(unittest.TestCase):
    def test_supports_placeholder(self):
        f = lambda a, b, c: [a, b, c]
        g = _curry3(f)

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


if __name__ == '__main__':
    unittest.main()
