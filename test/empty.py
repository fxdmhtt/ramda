# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_empty(unittest.TestCase):
    # def test_dispatches_to_empty_method(self):
    #     function Nothing() {}
    #     Nothing.prototype.empty = lambda :{ Nothing() }

    #     function Just(x) { this.value = x }
    #     Just.prototype.empty = lambda :{ Nothing() }

    #     eq(self, R.empty(Nothing()).constructor, Nothing)
    #     eq(self, R.empty(Just(123)).constructor, Nothing)

    # def test_dispatches_to_empty_function_on_constructor(self):
    #     function Nothing() {}
    #     Nothing.empty = lambda :{ Nothing() }

    #     function Just(x) { this.value = x }
    #     Just.empty = lambda :{ Nothing() }

    #     eq(self, R.empty(Nothing()).constructor, Nothing)
    #     eq(self, R.empty(Just(123)).constructor, Nothing)

    def test_returns_empty_array_given_array(self):
        eq(self, R.empty([1, 2, 3]), [])

    # def test_returns_empty_typed_array_of_equivalent_type_given_typed_array(self):
    #     eq(self, R.empty(Uint8Array.from('123')), Uint8Array.from(''))
    #     eq(self, R.empty(Uint8Array.from('123')).constructor.name, 'Uint8Array')
    #     eq(self, R.empty(Float32Array([1, 2, 3])), Float32Array([]))
    #     eq(self, R.empty(Float32Array([1, 2, 3])).constructor.name, 'Float32Array')

    def test_returns_empty_object_given_object(self):
        eq(self, R.empty({'x': 1, 'y': 2}), {})

    def test_returns_empty_string_given_string(self):
        eq(self, R.empty('abc'), '')
        eq(self, R.empty(str('abc')), '')

    def test_returns_empty_arguments_object_given_arguments_object(self):
        x = (lambda *arguments: arguments)(1, 2, 3)
        eq(self, R.empty(x), list((lambda *arguments: arguments)()))


if __name__ == '__main__':
    unittest.main()
