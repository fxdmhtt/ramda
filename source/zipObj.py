# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def zipObj(keys, values):
    idx = 0
    len = min(len(keys), len(values))
    out = {}
    while idx < len:
        out[keys[idx]] = values[idx]
        idx += 1
    return out
