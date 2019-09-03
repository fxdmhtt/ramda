# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_join(unittest.TestCase):
    def test_concatenates_a_lists_elements_to_a_string_with_an_separator_string_between_elements(self):
        list = [1, 2, 3, 4]
        eq(self, R.join('~', list), '1~2~3~4')


if __name__ == '__main__':
    unittest.main()
