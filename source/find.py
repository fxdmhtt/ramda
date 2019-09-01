# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2
from .internal._dispatchable import _dispatchable
_xfind = None

def find(fn, list):
    idx = 0
    len_ = len(list)
    while idx < len_:
        if fn(list[idx]):
            return list[idx]
        idx += 1
find = _curry2(_dispatchable(['find'], _xfind, find))
