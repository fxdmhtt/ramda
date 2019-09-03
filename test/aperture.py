# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_aperture(unittest.TestCase):
    def setUp(self):
        self.sevenLs = [1, 2, 3, 4, 5, 6, 7]

    def test_creates_a_list_of_n_tuples_from_a_list(self):
        eq(self, R.aperture(1, self.sevenLs), [[1], [2], [3], [4], [5], [6], [7]])
        eq(self, R.aperture(2, self.sevenLs), [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
        eq(self, R.aperture(3, self.sevenLs), [[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6], [5, 6, 7]])
        eq(self, R.aperture(4, [1, 2, 3, 4]), [[1, 2, 3, 4]])

    def test_returns_an_empty_list_when_n_list_length(self):
        eq(self, R.aperture(6, [1, 2, 3]), [])
        eq(self, R.aperture(1, []), [])

    # def test_can_act_as_a_transducer(self):
    #     eq(self, R.into([], R.aperture(2), self.sevenLs), [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])


if __name__ == '__main__':
    unittest.main()
