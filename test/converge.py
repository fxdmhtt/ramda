# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_converge(unittest.TestCase):
    def setUp(self):
        self.mult = lambda a, b: a * b

        self.f1 = R.converge(self.mult, [
            lambda a: a,
            lambda a: a
        ])
        self.f2 = R.converge(self.mult, [
            lambda a: a,
            lambda a, b: b
        ])
        self.f3 = R.converge(self.mult, [
            lambda a: a,
            lambda a, b, c: c
        ])

    def test_passes_the_results_of_applying_the_arguments_individually_to_two_separate_functions_into_a_single_one(self):
        eq(self, R.converge(self.mult, [R.add(1), R.add(3)])(2), 15) # self.mult(add1(2), add3(2)) = self.mult(3, 5) = 3 * 15

    def test_returns_a_function_with_the_length_of_the_longest_argument(self):
        eq(self, self.f1.length, 1)
        eq(self, self.f2.length, 2)
        eq(self, self.f3.length, 3)

    # def test_passes_context_to_its_functions(self):
    #     a = lambda x: this.f1(x)
    #     b = lambda x: this.f2(x)
    #     c = lambda x, y: this.f3(x, y)
    #     d = R.converge(c, [a, b])
    #     context = {'f1': R.add(1), 'f2': R.add(2), 'f3': R.add}
    #     eq(self, a.call(context, 1), 2)
    #     eq(self, b.call(context, 1), 3)
    #     eq(self, d.call(context, 1), 5)

    def test_returns_a_curried_function(self):
        eq(self, self.f2(6)(7), 42)
        eq(self, self.f3(R.__).length, 3)

    def test_works_with_empty_functions_list(self):
        fn = R.converge(lambda *arguments: len(arguments), [])
        eq(self, fn.length, 0)
        eq(self, fn(), 0)


if __name__ == '__main__':
    unittest.main()
