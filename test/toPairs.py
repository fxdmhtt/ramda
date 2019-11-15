# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

import unittest

class Test_toPairs(unittest.TestCase):
    def test_converts_an_object_into_an_array_of_two_element_key_value_arrays(self):
        self.assertSequenceEqual(list(R.toPairs({'a': 1, 'b': 2, 'c': 3})), [('a', 1), ('b', 2), ('c', 3)])

    # def test_only_iterates_the_objects_own_properties(self):
    #     F = function() {
    #         this.x = 1
    #         this.y = 2
    #     }
    #     F.prototype.protoProp = 'you can\'t see me'
    #     f = F()
    #     eq(self, R.toPairs(f), [['x', 1], ['y', 2]])


if __name__ == '__main__':
    unittest.main()
