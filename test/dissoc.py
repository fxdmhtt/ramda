# -*- 'coding': utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_dissoc(unittest.TestCase):
    def test_copies_an_object_omitting_the_specified_property(self):
        eq(self, R.dissoc('b', {'a': 1, 'b': 2, 'c': 3}), {'a': 1, 'c': 3})
        eq(self, R.dissoc('d', {'a': 1, 'b': 2, 'c': 3}), {'a': 1, 'b': 2, 'c': 3})

    # def test_includes_prototype_properties(self):
    #     function Rectangle(width, height) {
    #         this.width = width
    #         this.height = height
    #     }
    #     area = Rectangle.prototype.area = function() {
    #         return this.width * this.height
    #     }
    #     rect = Rectangle(7, 6)

    #     eq(self, R.dissoc('area', rect), {'width': 7, 'height': 6})
    #     eq(self, R.dissoc('width', rect), {'height': 6, 'area': area})
    #     eq(self, R.dissoc('depth', rect), {'width': 7, 'height': 6, 'area': area})

    def test_coerces_non_string_types(self):
        eq(self, R.dissoc(42, {'a': 1, 'b': 2, 42: 3}), {'a': 1, 'b': 2})
        # eq(self, R.dissoc(None, {'a': 1, 'b': 2, 'None': 3}), {'a': 1, 'b': 2})
        eq(self, R.dissoc(None, {'a': 1, 'b': 2, None: 3}), {'a': 1, 'b': 2})


if __name__ == '__main__':
    unittest.main()
