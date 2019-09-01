# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_ap(unittest.TestCase):
    def setUp(self):
        self.mult2 = lambda x: x * 2
        self.plus3 = lambda x: x + 3

    def test_interprets_a_as_an_applicative(self):
        eq(self, R.ap([self.mult2, self.plus3], [1, 2, 3]), [2, 4, 6, 4, 5, 6])

    def test_interprets_r_as_an_applicative(self):
        f = lambda r: \
            lambda a: \
                r + a
        g = lambda r: r * 2
        h = R.ap(f, g)
        # (<*>) :: (r -> a -> b) -> (r -> a) -> (r -> b)
        # f <*> g = \x -> f x (g x)
        eq(self, h(10), 10 + (10 * 2))

        eq(self, R.ap(R.add)(g)(10), 10 + (10 * 2))

    def test_dispatches_to_the_passed_object_s_ap_method_when_values_is_a_non_Array_object(self):
        obj = {'ap': lambda n: 'called ap with ' + str(n)}
        eq(self, R.ap(obj, 10), obj['ap'](10))


if __name__ == '__main__':
    unittest.main()
