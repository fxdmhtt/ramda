# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

alice = {
    'name': 'Alice Jones',
    'address': ['22 Walnut St', 'San Francisco', 'CA'],
    'pets': {'dog': 'joker', 'cat': 'batman'}
}

nameLens = R.lens(R.prop('name'), R.assoc('name'))
addressLens = R.lensProp('address')
headLens = R.lensIndex(0)
dogLens = R.lensPath(['pets', 'dog'])


class Test_lens(unittest.TestCase):
    def test_may_be_applied_to_a_lens_created_by_lensPath(self):
        eq(self, R.view(dogLens, alice), 'joker')

    def test_may_be_applied_to_a_lens_created_by_lensProp(self):
        eq(self, R.view(nameLens, alice), 'Alice Jones')

        eq(self, R.over(nameLens, R.toUpper, alice), {
            'name': 'ALICE JONES',
            'address': ['22 Walnut St', 'San Francisco', 'CA'],
            'pets': {'dog': 'joker', 'cat': 'batman'}
        })
    
        eq(self, R.set(nameLens, 'Alice Smith', alice), {
            'name': 'Alice Smith',
            'address': ['22 Walnut St', 'San Francisco', 'CA'],
            'pets': {'dog': 'joker', 'cat': 'batman'}
        })

    def test_may_be_applied_to_a_lens_created_by_lensIndex(self):
        eq(self, R.view(headLens, alice['address']), '22 Walnut St')

        eq(self, R.over(headLens, R.toUpper, alice['address']),
            ['22 WALNUT ST', 'San Francisco', 'CA']
        )

        eq(self, R.set(headLens, '52 Crane Ave', alice['address']),
            ['52 Crane Ave', 'San Francisco', 'CA']
        )

    def test_may_be_applied_to_composed_lenses(self):
        streetLens = R.compose(addressLens, headLens)
        dogLens = R.compose(R.lensPath(['pets']), R.lensPath(['dog']))

        eq(self, R.view(dogLens, alice), R.view(R.lensPath(['pets', 'dog']), alice))

        eq(self, R.view(streetLens, alice), '22 Walnut St')

        eq(self, R.over(streetLens, R.toUpper, alice), {
            name: 'Alice Jones',
            address: ['22 WALNUT ST', 'San Francisco', 'CA'],
            pets: {dog: 'joker', cat: 'batman'}
        })
    
        eq(self, R.set(streetLens, '52 Crane Ave', alice), {
            name: 'Alice Jones',
            address: ['52 Crane Ave', 'San Francisco', 'CA'],
            pets: {dog: 'joker', cat: 'batman'}
        })


if __name__ == '__main__':
    unittest.main()
