# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_toPairsIn(unittest.TestCase):
    def test_converts_an_object_into_an_array_of_two_element_key_value_arrays(self):
        self.assertSequenceEqual(list(R.toPairsIn({'a': 1, 'b': 2, 'c': 3})), [('a', 1), ('b', 2), ('c', 3)])

    # def test_iterates_properties_on_the_objects_prototype_chain(self):
    #     function sortPairs(a, b) {
    #         return a[0] > b[0] ? 1 : a[0] < b[0] ? -1 : 0
    #     }
    #     F = function() {
    #         this.x = 1
    #         this.y = 2
    #     }
    #     F.prototype.protoProp = 'you can see me'
    #     f = F()
    #     eq(self, R.toPairsIn(f).sort(sortPairs), [['protoProp', 'you can see me'], ['x', 1], ['y', 2]])


if __name__ == '__main__':
    unittest.main()
