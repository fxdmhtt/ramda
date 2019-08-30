# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def groupWith(fn, list):
    res = []
    idx = 0
    len_ = len(list)
    while idx < len_:
        nextidx = idx + 1
        while nextidx < len_ and fn(list[nextidx - 1], list[nextidx]):
            nextidx += 1
        res.append(list[idx:nextidx])
        idx = nextidx
    return res
