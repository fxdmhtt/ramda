# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_chain(unittest.TestCase):
    def setUp(self):
        # intoArray = R.into([])
        self.add1 = lambda x: [x + 1]
        self.dec = lambda x: [x - 1]
        self.times2 = lambda x: [x * 2]

    def test_maps_a_function_over_a_nested_list_and_returns_the_shallow_flattened_result(self):
        eq(self, R.chain(self.times2, [1, 2, 3, 1, 0, 10, -3, 5, 7]), [2, 4, 6, 2, 0, 20, -6, 10, 14])
        eq(self, R.chain(self.times2, [1, 2, 3]), [2, 4, 6])

    def test_does_not_flatten_recursively(self):
        f = lambda xs: \
            [xs[0]] if xs and xs[0] else []
        eq(self, R.chain(f, [[1], [[2], 100], [], [3, [4]]]), [1, [2], 3])

    # def test_maps_a_function_(a__>_[b])_into_a_(shallow)_flat_result(self):
    #     eq(self, intoArray(R.chain(self.times2), [1, 2, 3, 4]), [2, 4, 6, 8])

    def test_interprets_r_as_a_monad(self):
        h = lambda r: r * 2
        f = lambda a: \
            lambda r: \
                r + a
        bound = R.chain(f, h)
        # (>>=) :: (r -> a) -> (a -> r -> b) -> (r -> b)
        # h >>= f = \w -> f (h w) w
        eq(self, bound(10), (10 * 2) + 10)

        eq(self, R.chain(R.append, R.head)([1, 2, 3]), [1, 2, 3, 1])

    def test_dispatches_to_objects_that_implement_chain(self):
        obj = {'x': 100, 'chain': lambda f: f(100)}
        eq(self, R.chain(self.add1, obj), [101])

    # def test_dispatches_to_transformer_objects(self):
    #     eq(self, _isTransformer(R.chain(self.add1, listXf)), True)

    def test_composes(self):
        mdouble = R.chain(self.times2)
        mdec = R.chain(self.dec)
        eq(self, mdec(mdouble([10, 20, 30])), [19, 39, 59])

    # def test_can_compose_transducer_style(self):
    #     mdouble = R.chain(self.times2)
    #     mdec = R.chain(self.dec)
    #     xcomp = R.compose(mdec, mdouble)
    #     eq(self, intoArray(xcomp, [10, 20, 30]), [18, 38, 58])


if __name__ == '__main__':
    unittest.main()
