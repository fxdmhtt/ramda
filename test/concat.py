# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_concat(unittest.TestCase):
    def test_adds_combines_the_elements_of_the_two_lists(self):
        eq(self, R.concat(['a', 'b'], ['c', 'd']), ['a', 'b', 'c', 'd'])
        eq(self, R.concat([], ['c', 'd']), ['c', 'd'])

    def setUp(self):
        self.z1 = {
            'x': 'z1',
            'concat': lambda that: 'z1' + ' ' + that['x']
        }
        self.z2 = {
            'x': 'z2'
        }

    def test_adds_combines_the_elements_of_the_two_lists(self):
        eq(self, R.concat(['a', 'b'], ['c', 'd']), ['a', 'b', 'c', 'd'])
        eq(self, R.concat([], ['c', 'd']), ['c', 'd'])

    def test_works_on_strings(self):
        eq(self, R.concat('foo', 'bar'), 'foobar')
        eq(self, R.concat('x', ''), 'x')
        eq(self, R.concat('', 'x'), 'x')
        eq(self, R.concat('', ''), '')

    def test_delegates_to_non_String_object_with_a_concat_method_as_second_param(self):
        eq(self, R.concat(self.z1, self.z2), 'z1 z2')

    def test_throws_if_attempting_to_combine_an_array_with_a_non_array(self):
        with self.assertRaises(TypeError):
            R.concat([1], 2)

    def test_throws_if_not_an_array_String_or_object_with_a_concat_method(self):
        with self.assertRaises(TypeError):
            R.concat({}, {})


if __name__ == '__main__':
    unittest.main()
