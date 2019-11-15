# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest
from ..source.internal._curry2 import _curry2

class Test_tap(unittest.TestCase):
    def setUp(self):
        self.pushToList = _curry2(lambda lst, x: lst.append(x))

    def test_returns_a_function_that_always_returns_its_argument(self):
        f = R.tap(R.identity)
        self.assertTrue(callable(f))
        eq(self, f(100), 100)
        eq(self, f(None), None)

    def test_may_take_a_function_as_the_first_argument_that_executes_with_taps_argument(self):
        sideEffect = 0
        eq(self, sideEffect, 0)
        def function(x):
            nonlocal sideEffect
            sideEffect = 'string ' + str(x)
        rv = R.tap(function, 200)
        eq(self, rv, 200)
        eq(self, sideEffect, 'string 200')

    # def test_can_act_as_a_transducer(self):
    #     sideEffect = []
    #     numbers = [1,2,3,4,5]

    #     xf = R.compose(R.map(R.identity), R.tap(self.pushToList(sideEffect)))

    #     eq(self, R.into([], xf, numbers), numbers)
    #     eq(self, sideEffect, numbers)

    # def test_dispatches_to_transformer_objects(self):
    #     sideEffect = []
    #     pushToSideEffect = self.pushToList(sideEffect)

    #     eq(self, R.tap(pushToSideEffect, listXf), {
    #         f: pushToSideEffect,
    #         xf: listXf
    #     })


if __name__ == '__main__':
    unittest.main()
