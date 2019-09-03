# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

class Test_indexBy(unittest.TestCase):
    def test_indexes_list_by_the_given_property(self):
        list = [{'id': 'xyz', 'title': 'A'}, {'id': 'abc', 'title': 'B'}]
        indexed = R.indexBy(R.prop('id'), list)
        self.assertEqual(indexed, {'abc': {'id': 'abc', 'title': 'B'}, 'xyz': {'id': 'xyz', 'title': 'A'}})

    def test_indexes_list_by_the_given_property_upper_case(self):
        list = [{'id': 'xyz', 'title': 'A'}, {'id': 'abc', 'title': 'B'}]
        indexed = R.indexBy(R.compose(R.toUpper, R.prop('id')), list)
        self.assertEqual(indexed, {'ABC': {'id': 'abc', 'title': 'B'}, 'XYZ': {'id': 'xyz', 'title': 'A'}})

    # def test_can_act_as_a_transducer(self):
    #     list = [{'id': 'xyz', 'title': 'A'}, {'id': 'abc', 'title': 'B'}]
    #     transducer = R.compose(
    #         R.indexBy(R.prop('id')),
    #         R.map(R.pipe(
    #             R.adjust(0, R.toUpper),
    #             R.adjust(1, R.omit(['id']))
    #         )))
    #     result = R.into({}, transducer, list)
    #     self.assertEqual(result, {'ABC': {'title': 'B'}, 'XYZ': {'title': 'A'}})


if __name__ == '__main__':
    unittest.main()
