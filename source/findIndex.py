# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._dispatchable import _dispatchable
from .internal._xfindIndex import _xfindIndex

def findIndex(fn, list):
    idx = 0
    len = len(list)
    while idx < len:
        if fn(list[idx]):
            return idx
        idx += 1
    return -1
findIndex = _curry2(_dispatchable([], _xfindIndex, findIndex))
