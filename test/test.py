# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

class Test_test(unittest.TestCase):
    def test_returns_True_if_string_matches_pattern(self):
        eq(self, R.test(r'^x', 'xyz'), True)

    def test_returns_False_if_string_does_not_match_pattern(self):
        eq(self, R.test(r'^y', 'xyz'), False)

    def test_is_referentially_transparent(self):
        pattern = r'x'
        # eq(self, pattern.lastIndex, 0)
        eq(self, R.test(pattern, 'xyz'), True)
        # eq(self, pattern.lastIndex, 0)
        eq(self, R.test(pattern, 'xyz'), True)

    # def test_throws_if_first_argument_is_not_a_regexp(self):
    #     assert.throws(
    #         function() { R.test('foo', 'bar') },
    #         function(err) {
    #             return err.constructor == TypeError &&
    #                          err.message == '‘test’ requires a value of type RegExp ' +
    #                                                          'as its first argument received "foo"'
    #         }
    #     )


if __name__ == '__main__':
    unittest.main()
