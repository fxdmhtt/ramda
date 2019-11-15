# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

add3 = R.curry(lambda a, b, c: \
    a + b + c
)
add4 = R.curry(lambda a, b, c, d: \
    a + b + c + d
)
add5 = R.curry(lambda a, b, c, d, e: \
    a + b + c + d + e
)
madd3 = R.lift(add3)
madd4 = R.lift(add4)
madd5 = R.lift(add5)


class Test_lift(unittest.TestCase):
    def test_returns_a_function_if_called_with_just_a_function(self):
        self.assertTrue(callable(R.lift(R.add)))

    def test_produces_a_cross_product_of_array_values(self):
        eq(self, madd3([1, 2, 3], [1, 2], [1, 2, 3]), [3, 4, 5, 4, 5, 6, 4, 5, 6, 5, 6, 7, 5, 6, 7, 6, 7, 8])
        eq(self, madd3([1], [2], [3]), [6])
        eq(self, madd3([1, 2], [3, 4], [5, 6]), [9, 10, 10, 11, 10, 11, 11, 12])

    def test_can_lift_functions_of_any_arity(self):
        eq(self, madd3([1, 10], [2], [3]), [6, 15])
        eq(self, madd4([1, 10], [2], [3], [40]), [46, 55])
        eq(self, madd5([1, 10], [2], [3], [40], [500, 1000]), [546, 1046, 555, 1055])

    # def test_works_with_other_functors_such_as_"Maybe"(self):
    #     addM = R.lift(R.add)
    #     eq(self, addM(Maybe.Just(3), Maybe.Just(5)), Maybe.Just(8))


if __name__ == '__main__':
    unittest.main()
