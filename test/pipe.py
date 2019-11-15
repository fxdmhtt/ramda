# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_pipe(unittest.TestCase):
    def test_is_a_variadic_function(self):
        self.assertTrue(callable(R.pipe))
        eq(self, R.pipe.length, 0)

    def test_performs_left_to_right_function_composition(self):
        #    f :: (String, Number?) -> ([Number] -> [Number])
        f = R.pipe(lambda x, base=10: int(x, base), R.multiply, R.map)

        eq(self, f.length, 2)
        eq(self, f('10')([1, 2, 3]), [10, 20, 30])
        eq(self, f('10', 2)([1, 2, 3]), [2, 4, 6])

    # def test_passes_context_to_functions(self):
    #     function x(val) {
    #         return this.x * val
    #     }
    #     function y(val) {
    #         return this.y * val
    #     }
    #     function z(val) {
    #         return this.z * val
    #     }
    #     context = {
    #         a: R.pipe(x, y, z),
    #         x: 4,
    #         y: 2,
    #         z: 1
    #     }
    #     eq(self, context.a(5), 40)

    def test_throws_if_given_no_arguments(self):
        with self.assertRaises(Exception):
            R.pipe()

    def test_can_be_applied_to_one_argument(self):
        f = lambda a, b, c: [a, b, c]
        g = R.pipe(f)
        eq(self, g.length, 3)
        eq(self, g(1, 2, 3), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
