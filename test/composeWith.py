# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_composeWith(unittest.TestCase):
    def test_performs_right_to_left_function_composition_with_function_applying(self):
        #    f :: (String, Number?) -> ([Number] -> [Number])
        f = R.composeWith(lambda f, res: \
            f(res)
        )([R.map, R.multiply, lambda x, base=10: int(x, base=base)])

        eq(self, f.length, 2)
        eq(self, f('10')([1, 2, 3]), [10, 20, 30])
        eq(self, f('10', 2)([1, 2, 3]), [2, 4, 6])

    def test_performs_right_to_left_function_while_not_nil_result(self):
        isOdd = R.flip(R.mathMod)(2)
        composeWhenNotNil = R.composeWith(lambda f, res: \
            None if R.isNil(res) else f(res)
        )

        f = composeWhenNotNil([R.inc, R.ifElse(isOdd, R.identity, R.always(None)), lambda x, base=10: int(x, base=base)])

        eq(self, f.length, 2)
        eq(self, f('1'), 2)
        eq(self, f('2'), None)

    # def test_performs_right_to_left_function_using_promise_chaining(self):
    #     then = lambda f, p:{ p.then(f) }
    #     composeP = R.composeWith(then)
    #     toListPromise = lambda a:{ Promise(function(res) { res([a]) }) }
    #     doubleListPromise = lambda a:{ Promise(function(res) { res(R.concat(a, a)) }) }
    #     f = composeP([
    #         doubleListPromise,
    #         toListPromise
    #     ])

    #     return f(1)
    #         .then(function(res) {
    #             eq(self, res, [1, 1])
    #         })


if __name__ == '__main__':
    unittest.main()
