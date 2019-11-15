# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._dispatchable import _dispatchable
from .internal._xfindLast import _xfindLast

def findLast(fn, list):
    idx = len(list) - 1
    while idx >= 0:
        if fn(list[idx]):
            return list[idx]
        idx -= 1
findLast = _curry2(_dispatchable([], _xfindLast, findLast))
