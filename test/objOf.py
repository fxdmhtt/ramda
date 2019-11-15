# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_objOf(unittest.TestCase):
    def test_creates_an_object_containing_a_single_key_value_pair(self):
        eq(self, R.objOf('foo', 42), {'foo': 42})
        eq(self, R.objOf('foo')(42), {'foo': 42})


if __name__ == '__main__':
    unittest.main()
