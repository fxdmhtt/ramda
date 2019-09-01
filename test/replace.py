# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_replace(unittest.TestCase):
    def test_replaces_substrings_of_the_input_string(self):
        eq(self, R.replace('1', 'one', '1 two three'), 'one two three')

    def test_replaces_regex_matches_of_the_input_string(self):
        eq(self, R.replace(r'\d+', 'num', '1 2 three'), 'num num three')


if __name__ == '__main__':
    unittest.main()
