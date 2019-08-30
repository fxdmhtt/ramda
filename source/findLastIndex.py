# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._dispatchable import _dispatchable
from .internal._xfindLastIndex import _xfindLastIndex

def findLastIndex(fn, list):
    idx = len(list) - 1
    while idx >= 0:
        if fn(list[idx]):
            return idx
        idx -= 1
    return -1
findLastIndex = _curry2(_dispatchable([], _xfindLastIndex, findLastIndex))
