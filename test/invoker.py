# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_invoker(unittest.TestCase):
    def setUp(self):
        from collections import UserList
        class Array(UserList):
            def concat(self, *values):
                self.data.extend(values)
                return self.data
        self.Array = Array
        self.concat2 = R.invoker(2, 'concat')

    def test_returns_a_function_with_correct_arity(self):
        eq(self, self.concat2.length, 3)

    def test_calls_the_method_on_the_object(self):
        eq(self, self.concat2(3, 4, self.Array([1, 2])), [1, 2, 3, 4])

    def test_throws_a_descriptive_TypeError_if_method_does_not_exist(self):
        with self.assertRaises(TypeError):
            R.invoker(0, 'foo')(None)
            R.invoker(0, 'foo')(self.Array([1, 2, 3]))
            R.invoker(0, 'length')(self.Array([1, 2, 3]))

    # def test_does_not_rely_on_constructor_identity(self):
    #     eq(self, self.concat2([2], [3], vm.runInNewContext('[1]')), [1, 2, 3])

    def test_curries_the_method_call(self):
        eq(self, self.concat2(3)(4)(self.Array([1, 2])), [1, 2, 3, 4])
        eq(self, self.concat2(3, 4)(self.Array([1, 2])), [1, 2, 3, 4])
        eq(self, self.concat2(3)(4, self.Array([1, 2])), [1, 2, 3, 4])


if __name__ == '__main__':
    unittest.main()
