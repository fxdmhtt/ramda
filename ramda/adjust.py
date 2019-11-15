# -*- coding: utf-8 -*-

from .internal._curry3 import _curry3

@_curry3
def adjust(idx, fn, list_):
    if idx >= len(list_) or idx < -len(list_):
        return list_
    _list = list(list_[:])
    _list[idx] = fn(list_[idx])
    return _list
