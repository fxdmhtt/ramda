# -*- coding: utf-8 -*-

__package__ = 'ramda.test'

from .. import source as R
from .shared.eq import eq

import unittest

albums = [
    {'title': 'A Farewell to Kings', 'artist': 'Rush', 'genre': 'Rock', 'score': 3},
    {'title': 'Timeout', 'artist': 'Dave Brubeck Quartet', 'genre': 'Jazz', 'score': 3},
    {'title': 'Fly By Night', 'artist': 'Rush', 'genre': 'Rock', 'score': 5},
    {'title': 'Goldberg Variations', 'artist': 'Daniel Barenboim', 'genre': 'Baroque', 'score': 3},
    {'title': 'Art of the Fugue', 'artist': 'Glenn Gould', 'genre': 'Baroque', 'score': 3},
    {'title': 'New World Symphony', 'artist': 'Leonard Bernstein', 'genre': 'Romantic', 'score': 4},
    {'title': 'Romance with the Unseen', 'artist': 'Don Byron', 'genre': 'Jazz', 'score': 5},
    {'title': 'Somewhere In Time', 'artist': 'Iron Maiden', 'genre': 'Metal', 'score': 2},
    {'title': 'In Times of Desparation', 'artist': 'Danny Holt', 'genre': 'Modern', 'score': 1},
    {'title': 'Evita', 'artist': 'Various', 'genre': 'Broadway', 'score': 3},
    {'title': 'Five Leaves Left', 'artist': 'Nick Drake', 'genre': 'Folk', 'score': 1},
    {'title': 'The Magic Flute', 'artist': 'John Eliot Gardiner', 'genre': 'Classical', 'score': 4}
]


class Test_sortWith(unittest.TestCase):
    def test_sorts_by_a_simple_property_of_the_objects(self):
        sortedAlbums = R.sortWith([
            R.ascend(R.prop('title'))
        ], albums)
        eq(self, len(sortedAlbums), len(albums))
        eq(self, sortedAlbums[0]['title'], 'A Farewell to Kings')
        eq(self, sortedAlbums[11]['title'], 'Timeout')

    def test_sorts_by_multiple_properties_of_the_objects(self):
        sortedAlbums = R.sortWith([
            R.ascend(R.prop('score')),
            R.ascend(R.prop('title'))
        ], albums)
        eq(self, len(sortedAlbums), len(albums))
        eq(self, sortedAlbums[0]['title'], 'Five Leaves Left')
        eq(self, sortedAlbums[1]['title'], 'In Times of Desparation')
        eq(self, sortedAlbums[11]['title'], 'Romance with the Unseen')

    def test_sorts_by_3_properties_of_the_objects(self):
        sortedAlbums = R.sortWith([
            R.ascend(R.prop('genre')),
            R.ascend(R.prop('score')),
            R.ascend(R.prop('title'))
        ], albums)
        eq(self, len(sortedAlbums), len(albums))
        eq(self, sortedAlbums[0]['title'], 'Art of the Fugue')
        eq(self, sortedAlbums[1]['title'], 'Goldberg Variations')
        eq(self, sortedAlbums[11]['title'], 'New World Symphony')

    def test_sorts_by_multiple_properties_using_ascend_and_descend(self):
        sortedAlbums = R.sortWith([
            R.descend(R.prop('score')),
            R.ascend(R.prop('title'))
        ], albums)
        eq(self, len(sortedAlbums), len(albums))
        eq(self, sortedAlbums[0]['title'], 'Fly By Night')
        eq(self, sortedAlbums[1]['title'], 'Romance with the Unseen')
        eq(self, sortedAlbums[11]['title'], 'In Times of Desparation')

    def test_preserves_object_identity(self):
        a = {'value': 'a'}
        b = {'value': 'b'}
        result = R.sortWith([R.ascend(R.prop('value'))], [b, a])
        eq(self, result[0], a)
        eq(self, result[1], b)

    def test_sorts_array_like_object(self):
        args = (lambda *arguments: list(arguments))('c', 'a', 'b')
        result = R.sortWith([R.ascend(R.identity)], args)
        eq(self, result[0], 'a')
        eq(self, result[1], 'b')
        eq(self, result[2], 'c')


if __name__ == '__main__':
    unittest.main()
