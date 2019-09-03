# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_partial(unittest.TestCase):
    def setUp(self):
        self.disc = lambda a, b, c: \
            b * b - 4 * a * c  # note self.disc(3, 7, 4) => 1

    def test_caches_the_initially_supplied_arguments(self):
        f = R.partial(self.disc, [3])
        eq(self, f(7, 4), 1)
        g = R.partial(self.disc, [3, 7])
        eq(self, g(4), 1)

    def test_correctly_reports_the_arity_of_the_new_function(self):
        f = R.partial(self.disc, [3])
        eq(self, f.length, 2)
        g = R.partial(self.disc, [3, 7])
        eq(self, g.length, 1)


if __name__ == '__main__':
    unittest.main()
