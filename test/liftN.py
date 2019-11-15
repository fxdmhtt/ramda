# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

addN = lambda *arguments: \
    R.reduce(lambda a, b: a + b, 0, arguments)
add3 = R.curry(lambda a, b, c: \
    a + b + c
)



class Test_liftN(unittest.TestCase):
    def setUp(self):
        self.addN3 = R.liftN(3, addN)
        self.addN4 = R.liftN(4, addN)
        self.addN5 = R.liftN(5, addN)

    def test_returns_a_function(self):
        self.assertTrue(R.liftN(3, add3))

    def test_limits_a_variadic_function_to_the_specified_arity(self):
        eq(self, self.addN3([1, 10], [2], [3]), [6, 15])

    def test_can_lift_functions_of_any_arity(self):
        eq(self, self.addN3([1, 10], [2], [3]), [6, 15])
        eq(self, self.addN4([1, 10], [2], [3], [40]), [46, 55])
        eq(self, self.addN5([1, 10], [2], [3], [40], [500, 1000]), [546, 1046, 555, 1055])

    # def test_works_with_other_functors_such_as_Maybe(self):
    #     addM = R.liftN(2, R.add)
    #     eq(self, addM(Maybe.Just(3), Maybe.Just(5)), Maybe.Just(8))

    def test_interprets_a_as_a_functor(self):
        eq(self, self.addN3([1, 2, 3], [10, 20], [100, 200, 300]), [111, 211, 311, 121, 221, 321, 112, 212, 312, 122, 222, 322, 113, 213, 313, 123, 223, 323])
        eq(self, self.addN3([1], [2], [3]), [6])
        eq(self, self.addN3([1, 2], [10, 20], [100, 200]), [111, 211, 121, 221, 112, 212, 122, 222])

    def test_interprets_r_as_a_functor(self):
        convergedOnInt = self.addN3(R.add(2), R.multiply(3), R.subtract(4))
        convergedOnBool = R.liftN(2, R.and_)(R.gt(R.__, 0), R.lt(R.__, 3))
        self.assertTrue(callable(convergedOnInt))
        self.assertTrue(callable(convergedOnBool))
        eq(self, convergedOnInt(10), (10 + 2) + (10 * 3) + (4 - 10))
        # jscs:disable disallowYodaConditions
        eq(self, convergedOnBool(0), (0 > 0) and (0 < 3))
        eq(self, convergedOnBool(1), (1 > 0) and (1 < 3))
        eq(self, convergedOnBool(2), (2 > 0) and (2 < 3))
        eq(self, convergedOnBool(3), (3 > 0) and (3 < 3))
        # jscs:enable disallowYodaConditions


if __name__ == '__main__':
    unittest.main()
