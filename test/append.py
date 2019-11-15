# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_append(unittest.TestCase):
    def test_adds_the_element_to_the_end_of_the_list(self):
        eq(self, R.append('z', ['x', 'y']), ['x', 'y', 'z'])
        eq(self, R.append(['a', 'z'], ['x', 'y']), ['x', 'y', ['a', 'z']])

    def test_works_on_empty_list(self):
        eq(self, R.append(1, []), [1])


if __name__ == '__main__':
    unittest.main()
