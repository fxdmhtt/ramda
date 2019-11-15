# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_compose(unittest.TestCase):
    def test_is_a_variadic_function(self):
        self.assertTrue(callable(R.compose))
        eq(self, R.compose.length, 0)

    def test_performs_right_to_left_function_composition(self):
        #    f :: (String, Number?) -> ([Number] -> [Number])
        f = R.compose(R.map, R.multiply, lambda x, base=10: int(x, base=base))

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
    #         a: R.compose(x, y, z),
    #         x: 4,
    #         y: 2,
    #         z: 1
    #     }
    #     eq(self, context.a(5), 40)
    # })

    def test_throws_if_given_no_arguments(self):
        with self.assertRaises(ValueError):
            R.compose()

    def test_can_be_applied_to_one_argument(self):
        f = lambda a, b, c: [a, b, c]
        g = R.compose(f)
        eq(self, g.length, 3)
        eq(self, g(1, 2, 3), [1, 2, 3])


if __name__ == '__main__':
    unittest.main()
