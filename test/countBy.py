# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

import ramda as R
from .shared.eq import eq

import unittest

albums = [
    {'title': 'Art of the Fugue', 'artist': 'Glenn Gould', 'genre': 'Baroque'},
    {'title': 'A Farewell to Kings', 'artist': 'Rush', 'genre': 'Rock'},
    {'title': 'Timeout', 'artist': 'Dave Brubeck Quartet', 'genre': 'Jazz'},
    {'title': 'Fly By Night', 'artist': 'Rush', 'genre': 'Rock'},
    {'title': 'Goldberg Variations', 'artist': 'Daniel Barenboim', 'genre': 'Baroque'},
    {'title': 'New World Symphony', 'artist': 'Leonard Bernstein', 'genre': 'Romantic'},
    {'title': 'Romance with the Unseen', 'artist': 'Don Byron', 'genre': 'Jazz'},
    {'title': 'Somewhere In Time', 'artist': 'Iron Maiden', 'genre': 'Metal'},
    {'title': 'In Times of Desparation', 'artist': 'Danny Holt', 'genre': 'Modern'},
    {'title': 'Evita', 'artist': 'Various', 'genre': 'Broadway'},
    {'title': 'Five Leaves Left', 'artist': 'Nick Drake', 'genre': 'Folk'},
    {'title': 'The Magic Flute', 'artist': 'John Eliot Gardiner', 'genre': 'Classical'}
]
remap = {
    'Baroque': 'Classical',
    'Modern': 'Classical',
    'Romantic': 'Classical',
    'Metal': 'Rock'
}
def function(album):
    genre = R.prop('genre', album)
    return remap.get(genre) or genre
derivedGenre = function


class Test_countBy(unittest.TestCase):
    def test_counts_by_a_simple_property_of_the_objects(self):
        eq(self, R.countBy(R.prop('genre'), albums), {
            'Baroque': 2, 'Rock': 2, 'Jazz': 2, 'Romantic': 1, 'Metal': 1, 'Modern': 1, 'Broadway': 1, 'Folk': 1, 'Classical': 1
        })
    
    def test_counts_by_a_more_complex_function_on_the_objects(self):
        eq(self, R.countBy(derivedGenre, albums), {
            'Classical': 5, 'Rock': 3, 'Jazz': 2, 'Broadway': 1, 'Folk': 1
        })
    
    def test_ignores_inherited_properties(self):
        result = R.countBy(R.identity, ['abc', 'toString'])
        eq(self, result['abc'], 1)
        eq(self, result['toString'], 1)

    # def test_can_act_as_a_transducer(self):
    #     transducer = R.compose(
    #         R.countBy(R.prop('genre')),
    #         R.map(R.adjust(1, R.toString)))
    #     eq(self, R.into({}, transducer, albums), {
    #         Baroque: '2', Rock: '2', Jazz: '2', Romantic: '1', Metal: '1', Modern: '1', Broadway: '1', Folk: '1', Classical: '1'


if __name__ == '__main__':
    unittest.main()
