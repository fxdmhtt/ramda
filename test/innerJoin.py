# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

a = {'id': 1, 'name': 'a'}
b = {'id': 2, 'name': 'b'}
c = {'id': 3, 'name': 'c'}
f = R.innerJoin(lambda r, id: r['id'] == id)


class Test_innerJoin(unittest.TestCase):
    def test_only_returns_elements_from_the_first_list(self):
        eq(self, f([a, b, c], []), [])
        eq(self, f([a, b, c], [1]), [a])
        eq(self, f([a, b, c], [1, 2]), [a, b])
        eq(self, f([a, b, c], [1, 2, 3]), [a, b, c])
        eq(self, f([a, b, c], [1, 2, 3, 4]), [a, b, c])

    def test_does_not_remove_duplicates(self):
        eq(self, f([a, a, a], [1, 2, 3]), [a, a, a])
        eq(self, f([a, b, c], [1, 1, 1]), [a])


if __name__ == '__main__':
    unittest.main()
