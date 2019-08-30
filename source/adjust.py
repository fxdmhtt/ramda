# -*- coding: utf-8 -*-

from .internal._concat import _concat
from .internal._curry3 import _curry3

@_curry3
def adjust(idx, fn, list):
    if idx >= len(list) or idx < -len(list):
        return list
    start = len(list) if idx < 0 else 0
    _idx = start + idx
    _list = _concat(list)
    _list[_idx] = fn(list[_idx])
    return _list
