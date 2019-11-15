# -*- coding: utf-8 -*-

import ramda as R
from shared.eq import eq

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


class Test_sortBy(unittest.TestCase):
    def test_sorts_by_a_simple_property_of_the_objects(self):
        sortedAlbums = R.sortBy(R.prop('title'), albums)
        eq(self, len(sortedAlbums), len(albums))
        eq(self, sortedAlbums[0]['title'], 'A Farewell to Kings')
        eq(self, sortedAlbums[11]['title'], 'Timeout')

    def test_preserves_object_identity(self):
        a = {'value': 'a'}
        b = {'value': 'b'}
        result = R.sortBy(R.prop('value'), [b, a])
        eq(self, result[0], a)
        eq(self, result[1], b)

    def test_sorts_array_like_object(self):
        args = (lambda *arguments: list(arguments))('c', 'a', 'b')
        result = R.sortBy(R.identity, args)
        eq(self, result[0], 'a')
        eq(self, result[1], 'b')
        eq(self, result[2], 'c')


if __name__ == '__main__':
    unittest.main()
