# -*- coding: utf-8 -*-

__package__ = 'ramda.test.internal'

from ..shared.eq import eq
from ...source.__ import __ as _
from ...source.internal._curry2 import _curry2

import unittest
class Test__curry2(unittest.TestCase):
    def test_supports_placeholder(self):
        f = lambda a, b: [a, b]
        g = _curry2(f)

        eq(self, g(1)(2), [1, 2])
        eq(self, g(1, 2), [1, 2])

        eq(self, g(_, 2)(1), [1, 2])
        eq(self, g(1, _)(2), [1, 2])

        eq(self, g(_, _)(1)(2), [1, 2])
        eq(self, g(_, _)(1, 2), [1, 2])
        eq(self, g(_, _)(_)(1, 2), [1, 2])
        eq(self, g(_, _)(_, 2)(1), [1, 2])


if __name__ == '__main__':
    unittest.main()
