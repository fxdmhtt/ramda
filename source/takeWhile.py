# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._dispatchable import _dispatchable
from .internal._xtakeWhile import _xtakeWhile
from .slice import slice

def takeWhile(fn, xs):
    idx = 0
    len = len(xs)
    while idx < len and fn(xs[idx]):
        idx += 1
    return slice(0, idx, xs)
takeWhile = _curry2(_dispatchable(['takeWhile'], _xtakeWhile, takeWhile)
