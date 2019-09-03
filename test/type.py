# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_type(unittest.TestCase):
    def test_Array_if_given_an_array_literal(self):
        eq(self, R.type([1, 2, 3]), 'list')

    # def test_Arguments_if_given_an_arguments_object(self):
    #     args = (lambda :{ arguments }())
    #     eq(self, R.type(args), 'Arguments')
    # })

    def test_Object_if_given_an_object_literal(self):
        eq(self, R.type({'batman': 'na na na na na na na'}), 'dict')

    # def test_RegExp_if_given_a_RegExp_literal(self):
    #     eq(self, R.type(/[A-z]/), 'RegExp')

    def test_Number_if_given_a_numeric_value(self):
        eq(self, R.type(4), 'int')

    def test_Number_if_given_the_NaN_value(self):
        eq(self, R.type(float('nan')), 'float')

    def test_String_if_given_a_String_literal(self):
        eq(self, R.type('Gooooodd Mornning Ramda!!'), 'str')

    # def test_String_if_given_a_String_object(self):
    #     eq(self, R.type(String('I am a String object')), 'String')

    def test_Null_if_given_the_None_value(self):
        eq(self, R.type(None), 'None')

    # def test_Undefined_if_given_the_None_value(self):
    #     eq(self, R.type(None), 'Undefined')


if __name__ == '__main__':
    unittest.main()
