# -*- coding: utf-8 -*-

from .internal._curry2 import _curry2

@_curry2
def xprod(a, b):
    idx = 0
    ilen = len(a)
    jlen = len(b)
    result = []
    while idx < ilen:
        j = 0
        while j < jlen:
            result.append([a[idx], b[j]])
            j += 1
        idx += 1
    return result
