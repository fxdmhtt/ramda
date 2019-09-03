# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_useWith(unittest.TestCase):
    def setUp(self):
        self.add1 = lambda x: x + 1
        self.mult2 = lambda x: x * 2
        self.div3 = lambda x: x / 3
        self.f = R.useWith(max, [self.add1, self.mult2, self.div3])

    def test_takes_a_list_of_function_and_returns_a_function(self):
        self.assertTrue(callable(R.useWith(max, [])))
        self.assertTrue(callable(R.useWith(max, [self.add1])))
        self.assertTrue(callable(R.useWith(max, [self.add1, self.mult2, self.div3])))

    def test_passes_the_arguments_received_to_their_respective_functions(self):
        eq(self, self.f(7, 8, 9), 16) # max(7 + 1, 8 * 2, 9 / 3)

    def test_passes_additional_arguments_to_the_main_function(self):
        eq(self, self.f(7, 8, 9, 10), 16)
        eq(self, self.f(7, 8, 9, 20), 20)

    def test_has_the_correct_arity(self):
        eq(self, self.f.length, 3)

    # def test_passes_context_to_its_functions(self):
    #     a = lambda x:{ this.f1(x) }
    #     b = lambda x:{ this.f2(x) }
    #     c = lambda x, y:{ this.f3(x, y) }
    #     d = R.useWith(c, [a, b])
    #     context = {f1: R.add(1), f2: R.add(2), f3: R.add}
    #     eq(self, a.call(context, 1), 2)
    #     eq(self, b.call(context, 1), 3)
    #     eq(self, d.apply(context, [1, 1]), 5)
    #     eq(self, d.apply(context, [2, 3]), 8)


if __name__ == '__main__':
    unittest.main()
