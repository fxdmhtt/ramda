# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def groupWith(fn, list):
    res = []
    idx = 0
    len = len(list)
    while idx < len:
        nextidx = idx + 1
        while nextidx < len and fn(list[nextidx - 1], list[nextidx]):
            nextidx += 1
        res.append(list[idx, nextidx])
        idx = nextidx
    return res
