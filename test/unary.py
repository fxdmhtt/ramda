# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest
from ramda.internal import sig

class Test_unary(unittest.TestCase):
    def test_turns_multiple_argument_function_into_unary_one(self):
        @sig(names=str('xyz'))
        def function(*arguments):
            x, y, z, *_ = *arguments, None, None, None
            eq(self, len(arguments), 1)
            self.assertTrue(y is None)
            self.assertTrue(z is None)
        R.unary(function)(10, 20, 30)

    def test_initial_argument_is_passed_through_normally(self):
        R.unary(lambda x, y, z: \
            eq(self, x, 10)
        )(10, 20, 30)


if __name__ == '__main__':
    unittest.main()
