# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_isEmpty(unittest.TestCase):
    def test_returns_False_for_None(self):
        eq(self, R.isEmpty(None), False)

    def test_returns_False_for_None(self):
        eq(self, R.isEmpty(None), False)

    def test_returns_True_for_empty_string(self):
        eq(self, R.isEmpty(''), True)
        eq(self, R.isEmpty(' '), False)

    def test_returns_True_for_empty_array(self):
        eq(self, R.isEmpty([]), True)
        eq(self, R.isEmpty([[]]), False)

    # def test_returns_True_for_empty_typed_array(self):
    #     eq(self, R.isEmpty(Uint8Array.from('')), True)
    #     eq(self, R.isEmpty(Float32Array.from('')), True)
    #     eq(self, R.isEmpty(Float32Array([])), True)
    #     eq(self, R.isEmpty(Uint8Array.from('1')), False)
    #     eq(self, R.isEmpty(Float32Array.from('1')), False)
    #     eq(self, R.isEmpty(Float32Array([1])), False)

    def test_returns_True_for_empty_object(self):
        eq(self, R.isEmpty({}), True)
        eq(self, R.isEmpty({'x': 0}), False)

    def test_returns_True_for_empty_arguments_object(self):
        eq(self, R.isEmpty((lambda *arguments: list(arguments))()), True)
        eq(self, R.isEmpty((lambda *arguments: list(arguments))(0)), False)

    def test_returns_False_for_every_other_value(self):
        eq(self, R.isEmpty(0), False)
        eq(self, R.isEmpty(float('nan')), False)
        eq(self, R.isEmpty(['']), False)


if __name__ == '__main__':
    unittest.main()
