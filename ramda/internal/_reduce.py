# -*- coding: utf-8 -*-

from ._isArrayLike import _isArrayLike
_xwrap = None
# from ..bind import bind

# ignore: _arrayReduce

# ignore: _iterableReduce

# ignore: _methodReduce

def _reduce(fn, acc, list):
    # ignore: _reduce

    if callable(getattr(list, 'reduce', None)):
        return getattr(list, 'reduce')(acc)
    elif isinstance(list, dict) and callable(list.get('reduce')):
        return list['reduce'](acc)
    else:
        from functools import reduce
        return reduce(fn, list, acc)
