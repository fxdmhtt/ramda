# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3
from .map import map
from .sequence import sequence

@_curry3
def traverse(of, f, traversable):
    return (
        traversable['fantasy-land/traverse'](f, of) if callable(traversable['fantasy-land/traverse'])
        else sequence(of, map(f, traversable))
    )
