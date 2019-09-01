# -*- coding: utf-8 -*-

from ._isArrayLike import _isArrayLike
_xwrap = None
# from ..bind import bind

# ignore: _arrayReduce

# ignore: _iterableReduce

# ignore: _methodReduce

def _reduce(fn, acc, list):
    # ignore: _reduce

    from functools import reduce
    return reduce(fn, list, acc)
