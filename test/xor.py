# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest
import datetime

class Test_xor(unittest.TestCase):
    def test_compares_two_values_with_exclusive_or(self):
        eq(self, R.xor(True, True), False)
        eq(self, R.xor(True, False), True)
        eq(self, R.xor(False, True), True)
        eq(self, R.xor(False, False), False)

    def test_when_both_values_are_truthy_it_should_return_False(self):
        eq(self, R.xor(True, 'foo'), False)
        eq(self, R.xor(42, True), False)
        eq(self, R.xor('foo', 42), False)
        # eq(self, R.xor({}, True), False)
        # eq(self, R.xor(True, []), False)
        eq(self, R.xor([], {}), False)
        eq(self, R.xor(datetime.datetime.now(), True), False)
        eq(self, R.xor(True, float('inf')), False)
        eq(self, R.xor(float('inf'), datetime.datetime.now()), False)

    def test_when_both_values_are_falsy_it_should_return_False(self):
        eq(self, R.xor(None, False), False)
        eq(self, R.xor(False, None), False)
        eq(self, R.xor(None, None), False)
        eq(self, R.xor(0, False), False)
        # eq(self, R.xor(False, float('nan')), False)
        # eq(self, R.xor(float('nan'), 0), False)
        eq(self, R.xor('', False), False)

    def test_when_one_argument_is_truthy_and_the_other_is_falsy_it_should_return_True(self):
        eq(self, R.xor('foo', None), True)
        eq(self, R.xor(None, 'foo'), True)
        eq(self, R.xor(None, 42), True)
        eq(self, R.xor(42, None), True)
        # eq(self, R.xor(float('inf'), float('nan')), True)
        # eq(self, R.xor(float('nan'), float('inf')), True)
        # eq(self, R.xor({}, ''), True)
        # eq(self, R.xor('', {}), True)
        eq(self, R.xor(datetime.datetime.now(), 0), True)
        eq(self, R.xor(0, datetime.datetime.now()), True)
        # eq(self, R.xor([], None), True)
        # eq(self, R.xor(None, []), True)

    def test_returns_a_curried_function(self):
        eq(self, R.xor()(True)(True), False)
        eq(self, R.xor()(True)(False), True)
        eq(self, R.xor()(False)(True), True)
        eq(self, R.xor()(False)(False), False)


if __name__ == '__main__':
    unittest.main()
